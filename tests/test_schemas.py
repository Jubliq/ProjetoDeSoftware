from app.database import Base, SessionLocal, engine, get_db
from app.models import ScaleLog, User
from app.schemas import OperatorLogin, ReceiptCreate
import pytest


def test_valid_receipt_schema():
  data = {
      "coop_name": "Cooperativa Verde",
      "material_category": "Alumínio",
      "weight_kg": 15.5,
      "operator_cpf": "123.456.789-00",
  }
  receipt = ReceiptCreate(**data)
  assert receipt.coop_name == "Cooperativa Verde"
  assert receipt.weight_kg == 15.5


def test_operator_login_schema():
  login = OperatorLogin(cpf="123.456.789-00", password="securepassword")
  assert login.cpf == "123.456.789-00"


def test_sqlalchemy_models_instantiation():
  user = User(cpf="123.456.789-00")
  assert user.cpf == "123.456.789-00"

  log = ScaleLog(
      coop_name="João",
      material_category="PET",
      weight_kg=10.0,
      estimated_value=18.0,
  )
  assert log.weight_kg == 10.0


def test_database_session_generator():
  # Cobre as linhas de criação de sessão e generator em database.py
  Base.metadata.create_all(bind=engine)
  db_gen = get_db()
  db = next(db_gen)
  assert db is not None
  try:
    db_gen.send(None)
  except StopIteration:
    pass