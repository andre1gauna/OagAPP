import psycopg2

def busca_produto_tabela_matchings(texto_normalizado):
    with connMatchings.cursor() as cursor:
        cursor.execute("""
            SELECT produto_id
            FROM semantic_matches
            WHERE texto_normalizado = %s
            LIMIT 5
        """, (texto_normalizado,))

        resultado = cursor.fetchall()

        return resultado if resultado else []

def buscar_produto_tabela_produtos(texto_normalizado):
    with connProducts.cursor() as cursor:
        cursor.execute("""
            SELECT id, nome
            FROM products
            WHERE texto_canonico ILIKE %s
            LIMIT 5;
        """, (f"%{texto_normalizado}%",))

        resultado = cursor.fetchall()

        return resultado if resultado else []   

def busca_produto(texto_normalizado):
    result = busca_produto_tabela_matchings(texto_normalizado)
    if not result:
        result = buscar_produto_tabela_produtos(texto_normalizado)
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