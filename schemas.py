from pydantic import BaseModel

class PedidoCreate(BaseModel):
    cliente: str
    produto: str
    quantidade: int
    valor_unitario: float

class PedidoResponse(PedidoCreate):
    id: int
    total: float
    status: str

    class Config:
        from_attributes = True