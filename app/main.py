from app.database import Base, engine
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Criação das tabelas no banco de dados SQLite
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MVP Associação de Reciclagem",
    version="1.0.0",
    description=(
        "API para controle de pesagem e repasse comunitário em galpões"
        " de reciclagem."
    ),
)


@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "API operando com sucesso.",
    }