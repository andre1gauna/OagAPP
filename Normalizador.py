import re
import unicodedata
import csv

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
        texto = regex.sub(substituir, texto)
        item["json"]["texto_normalizado"] = texto
        output.append(item)

    return output

def construir_normalizador(equivalencias):

    mapa = {eq["termo"]: eq["normalizado"] for eq in equivalencias}

    termos = map(re.escape, mapa.keys())

    regex = re.compile(r"\b(" + "|".join(termos) + r")\b")

    def substituir(match):
        return mapa[match.group(0)]

    return regex, substituir

def carregar_equivalencias(caminho_csv):
    equivalencias = []

    with open(caminho_csv, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            equivalencias.append({
                "termo": row["termo_original"].upper(),
                "normalizado": row["termo_normalizado"].upper()
            })

    return equivalencias


path = "TabelaEquivalencias.csv"
equivalencias = carregar_equivalencias(path)
regex, substituir = construir_normalizador(equivalencias)