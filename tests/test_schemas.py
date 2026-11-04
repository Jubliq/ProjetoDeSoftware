from app.schemas import ScaleLogCreate
import pytest
from pydantic import ValidationError


def success_scale_log_creation():
    data = {
        "coop_name": "Maria das Dores Oliveira",
        "material_category": "Papelão Ondulado",
        "weight_kg": 42.50,
        "operator_cpf": "123.456.789-00",
    }
    log = ScaleLogCreate(**data)
    assert log.weight_kg == 42.50
    assert log.coop_name == "Maria das Dores Oliveira"


def test_invalid_negative_weight():
    data = {
        "coop_name": "Maria das Dores Oliveira",
        "material_category": "Papelão Ondulado",
        "weight_kg": -5.00,  # Inválido: menor que zero
        "operator_cpf": "123.456.789-00",
    }
    with pytest.raises(ValidationError):
        ScaleLogCreate(**data)


def test_invalid_zero_weight():
    data = {
        "coop_name": "Maria das Dores Oliveira",
        "material_category": "Papelão Ondulado",
        "weight_kg": 0.0,  # Inválido: zero
        "operator_cpf": "123.456.789-00",
    }
    with pytest.raises(ValidationError):
        ScaleLogCreate(**data)