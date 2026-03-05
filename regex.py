import re


def construir_normalizador(equivalencias):

    mapa = {eq["termo"]: eq["normalizado"] for eq in equivalencias}

    termos = map(re.escape, mapa.keys())

    regex = re.compile(r"\b(" + "|".join(termos) + r")\b")

    def substituir(match):
        return mapa[match.group(0)]

    return regex, substituir


def normalizar_textos(items, equivalencias):

    regex, substituir = construir_normalizador(equivalencias)

    for item in items:
        texto = item["json"]["texto_higienizado"]
        texto = regex.sub(substituir, texto)

        item["json"]["texto_normalizado"] = texto

    return items
