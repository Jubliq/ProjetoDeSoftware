from pydantic import BaseModel, Field


class ReceiptCreate(BaseModel):
  coop_name: str = Field(..., min_length=2)
  material_category: str
  weight_kg: float = Field(..., gt=0)
  operator_cpf: str


class OperatorLogin(BaseModel):
  cpf: str
  password: str