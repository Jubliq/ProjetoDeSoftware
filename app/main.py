from app.database import Base, engine
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MVP Associação de Reciclagem", version="1.0.0")
templates = Jinja2Templates(directory="app/templates")

PRICES = {
    "Papelão Ondulado": 0.50,
    "Plástico PET": 1.80,
    "Alumínio": 6.50,
    "Vidro": 0.20,
}


@app.get("/", response_class=HTMLResponse)
def read_login(request: Request):
  return templates.TemplateResponse(request, "login.html")


@app.get("/scale", response_class=HTMLResponse)
def read_scale(request: Request, cpf: str = None):
  return templates.TemplateResponse(request, "scale.html")


@app.post("/receipt", response_class=HTMLResponse)
def create_receipt(
    request: Request,
    coop_name: str = Form(...),
    material_category: str = Form(...),
    weight_kg: float = Form(...),
    operator_cpf: str = Form(...),
):
  unit_price = PRICES.get(material_category, 0.50)
  estimated_value = round(weight_kg * unit_price, 2)

  data = {
      "coop_name": coop_name,
      "material_category": material_category,
      "weight_kg": weight_kg,
      "estimated_value": estimated_value,
  }
  return templates.TemplateResponse(request, "receipt.html", {"data": data})