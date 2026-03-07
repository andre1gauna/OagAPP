from Normalizador import normalizar
from BuscaTabela import busca_produto


items = [
    {
        "json": {
            "descricao": "Bucha aço carbono 1/2\" BSP"
        }
    }
]

resultadoNormalizado = normalizar(items)
for item in resultadoNormalizado:
    candidados = busca_produto(item["json"]["texto_normalizado"])
    for candidato in candidados:
        print(candidato)