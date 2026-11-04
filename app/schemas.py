from pydantic import BaseModel, Field, field_validator


class LoginSchema(BaseModel):
    cpf: str = Field(..., description="CPF do operador")
    password: str = Field(..., description="Senha de acesso")


class ScaleLogCreate(BaseModel):
    coop_name: str = Field(..., min_length=2, description="Nome do cooperado")
    material_category: str = Field(..., description="Categoria do material")
    weight_kg: float = Field(
        ..., gt=0.0, description="Peso em kg deve ser estritamente maior que zero"
    )
    operator_cpf: str = Field(..., description="CPF do operador responsável")

    @field_validator("weight_kg")
    @classmethod
    def validate_weight(cls, value: float) -> float:
        if value > 10000.0:
            raise ValueError(
                "Peso excede o limite máximo permitido para a balança (10.000 kg)."
            )
        return round(value, 2)