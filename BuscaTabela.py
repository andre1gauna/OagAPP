import psycopg2

def busca_produto_tabela_matchings(texto_normalizado):
    with connMatchings.cursor() as cursor:
        cursor.execute("""
            SELECT produto_id
            FROM semantic_matches
            WHERE texto_normalizado = %s
            LIMIT 1
        """, (texto_normalizado,))

        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]
        else:
            return ''

def buscar_produto_tabela_produtos(texto_normalizado):
    with connProducts.cursor() as cursor:
        cursor.execute("""
            SELECT id, nome
            FROM products
            WHERE texto_canonico ILIKE '%' || $1 || '%'
            LIMIT 5;
        """, (texto_normalizado,))

        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]
        else:
            return ''        

def busca_produto(texto_normalizado):
    result = busca_produto_tabela_matchings(texto_normalizado)
    if result is '':
        buscar_produto_tabela_produtos(texto_normalizado)
    return result


connMatchings = psycopg2.connect(
    host="localhost",
    database="meubanco",
    user="usuario",
    password="senha"
)

connProducts = psycopg2.connect(
    host="localhost",
    database="meubanco",
    user="usuario",
    password="senha"
)