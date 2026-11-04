from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_login():
  response = client.get("/")
  assert response.status_code == 200
  assert "Identificação do Operador" in response.text


def test_read_scale():
  response = client.get("/scale")
  assert response.status_code == 200
  assert "Registro de Pesagem de Lote" in response.text


def test_create_receipt():
  response = client.post(
      "/receipt",
      data={
          "coop_name": "João da Silva",
          "material_category": "Alumínio",
          "weight_kg": 10.0,
          "operator_cpf": "123.456.789-00",
      },
  )
  assert response.status_code == 200
  assert "Pesagem Registrada com Sucesso!" in response.text
  assert "R$ 65.0" in response.text  # 10.0 kg * R$ 6.50 (Alumínio) = R$ 65.00