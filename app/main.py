from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Registration API", description="An API for registering users with unique emails.")

@app.post("/register", response_model=schemas.UserOut, status_code=201)
def register_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists at app layer
    db_user = crud.get_user_by_email(db, email=user_in.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    try:
        user = crud.create_user(db=db, user=user_in)
        return user
    except Exception as e:
        # Handle db-level unique constraint violation
        from sqlalchemy.exc import IntegrityError
        if isinstance(e.__cause__, IntegrityError):
            raise HTTPException(status_code=400, detail="Email already registered (db constraint).")
        raise HTTPException(status_code=500, detail="An error occurred during registration.")
