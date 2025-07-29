from sqlalchemy import Column, Integer, String, UniqueConstraint
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint("email", name="uq_user_email"),
    )
