from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from collections import defaultdict
from deps import get_db
import models

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])
templates = Jinja2Templates(directory="templates")

MESES_PT = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}


@router.get("/")
def pagina_pedidos(request: Request, db: Session = Depends(get_db)):
    user = request.cookies.get("user")

    if not user:
        return RedirectResponse("/login", status_code=303)

    produtos = db.query(models.Produto).all()
    pedidos = db.query(models.Pedido).all()

    valor_pendente = sum((p.total or 0) for p in pedidos if p.status == "Pendente")
    total_faturado = sum((p.total or 0) for p in pedidos if p.status == "Entregue")
    total_pedidos = len(pedidos)
    entregues = len([p for p in pedidos if p.status == "Entregue"])
    pendentes = len([p for p in pedidos if p.status == "Pendente"])

    grafico_labels = [p.cliente for p in pedidos]
    grafico_values = [(p.total or 0) for p in pedidos]

    
    faturamento_por_mes = defaultdict(float)
    for p in pedidos:
        if p.status == "Entregue" and p.data_criacao:
            numero_mes = p.data_criacao.month
            nome_mes = MESES_PT[numero_mes]
            faturamento_por_mes[nome_mes] += p.total or 0

    
    meses_ordenados = sorted(
        faturamento_por_mes.keys(),
        key=lambda m: list(MESES_PT.values()).index(m)
    )

    faturamento_labels = meses_ordenados
    faturamento_values = [round(faturamento_por_mes[m], 2) for m in meses_ordenados]

    return templates.TemplateResponse("pedidos.html", {
        "request": request,
        "produtos": produtos,
        "pedidos": pedidos,
        "valor_pendente": valor_pendente,
        "total_faturado": total_faturado,
        "total_pedidos": total_pedidos,
        "entregues": entregues,
        "pendentes": pendentes,
        "grafico_labels": grafico_labels,
        "grafico_values": grafico_values,
        "faturamento_labels": faturamento_labels,
        "faturamento_values": faturamento_values
    })


@router.post("/cadastrar-produto")
def cadastrar_produto(
    nome: str = Form(...),
    estoque: int = Form(...),
    valor: float = Form(...),
    db: Session = Depends(get_db)
):
    nome = nome.strip()

    if not nome:
        return RedirectResponse("/pedidos/", status_code=303)

    if estoque < 0 or valor <= 0:
        return RedirectResponse("/pedidos/", status_code=303)

    novo = models.Produto(nome=nome, estoque=estoque, valor=valor)

    db.add(novo)
    db.commit()

    return RedirectResponse("/pedidos/", status_code=303)


@router.post("/criar-pedido")
def criar_pedido(
    cliente: str = Form(...),
    produto_id: int = Form(...),
    qtd: int = Form(...),
    db: Session = Depends(get_db)
):
    cliente = cliente.strip()
    produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()

    if not produto:
        return RedirectResponse("/pedidos/", status_code=303)

    if not cliente:
        return RedirectResponse("/pedidos/", status_code=303)

    if qtd <= 0:
        return RedirectResponse("/pedidos/", status_code=303)

    if produto.estoque < qtd:
        return RedirectResponse("/pedidos/", status_code=303)

    total = produto.valor * qtd

    novo_pedido = models.Pedido(
        cliente=cliente,
        produto=produto.nome,
        quantidade=qtd,
        total=total,
        status="Pendente"
    )

    produto.estoque -= qtd

    db.add(novo_pedido)
    db.commit()

    return RedirectResponse("/pedidos/", status_code=303)


@router.post("/entregar/{pedido_id}")
def entregar(pedido_id: int, db: Session = Depends(get_db)):
    pedido = db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()

    if pedido and pedido.status != "Entregue" and pedido.status != "Cancelado":
        pedido.status = "Entregue"
        db.commit()

    return RedirectResponse("/pedidos/", status_code=303)


@router.post("/cancelar/{pedido_id}")
def cancelar(pedido_id: int, db: Session = Depends(get_db)):
    pedido = db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()

    if pedido and pedido.status != "Entregue" and pedido.status != "Cancelado":
        pedido.status = "Cancelado"
        db.commit()

    return RedirectResponse("/pedidos/", status_code=303)
