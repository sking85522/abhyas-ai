import pytest
from fastapi.testclient import TestClient
from services.auth_service.main import app
from services.auth_service.database.session import Base, engine, get_db
from sqlalchemy.orm import sessionmaker

# Create in-memory sqlite db for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
from sqlalchemy import create_engine
test_engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

Base.metadata.create_all(bind=test_engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "auth"}

def test_register_user():
    response = client.post("/auth/register", json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
    assert "id" in response.json()

def test_register_existing_user():
    response = client.post("/auth/register", json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 400
    assert response.json()["message"] == "Email already registered"

def test_login_user():
    response = client.post("/auth/login", json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_wrong_password():
    response = client.post("/auth/login", json={"email": "test@example.com", "password": "wrongpassword"})
    assert response.status_code == 401
