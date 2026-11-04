from pydantic import BaseModel, ConfigDict
from typing import Optional

class OperatorLogin(BaseModel):
    cpf: str
    password: Optional[str] = None

class ReceiptCreate(BaseModel):
    coop_name: str
    material_category: str
    weight_kg: float
    operator_cpf: str

class ReceiptResponse(ReceiptCreate):
    id: Optional[int] = None
    total_value: Optional[float] = None

    model_config = ConfigDict(from_attributes=True)