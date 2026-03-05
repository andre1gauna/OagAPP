from Normalizador import normalizar
from BuscaTabela import busca_produto


items = [" "," "]

resultadoNormalizado = normalizar(items)
for texto in resultadoNormalizado:
    busca_produto(texto)