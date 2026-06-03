from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .schemas import UserCreate, UserResponse, Token
from services.auth_service.database.session import get_db
from services.auth_service.models.user import User
from shared.security import get_password_hash, verify_password, create_access_token
from shared.exceptions import AppError

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user_in.email).first()
    if db_user:
        raise AppError(message="Email already registered", status_code=400)

    hashed_password = get_password_hash(user_in.password)
    new_user = User(email=user_in.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login", response_model=Token)
def login(user_in: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user_in.email).first()
    if not db_user or not verify_password(user_in.password, db_user.hashed_password):
        raise AppError(message="Incorrect email or password", status_code=401)

    access_token = create_access_token(data={"sub": str(db_user.id)})
    return {"access_token": access_token, "token_type": "bearer"}
