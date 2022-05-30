import unicodedata


def strip_accents(text: str):
    """strip accents of text"""
    return "".join(
        c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn"
    )
