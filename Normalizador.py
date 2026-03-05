import re
import unicodedata

def remover_acentos(texto):
    return unicodedata.normalize('NFD', texto)\
        .encode('ascii', 'ignore')\
        .decode('utf-8')


def normalizar(items):
    output = []
    for item in items:
        texto = item["json"].get("descricao", "")

        if texto is None:
            texto = ""

        # Remover acentos
        texto = remover_acentos(texto)

        # Uppercase
        texto = texto.upper()

        # Remover caracteres especiais indesejados (mantendo / . # ")
        texto = re.sub(r'[^\w\s"/.#-]', ' ', texto)

        # Remover múltiplos espaços
        texto = re.sub(r'\s+', ' ', texto).strip()

        item["json"]["texto_higienizado"] = texto
        output.append(item)

    return output
