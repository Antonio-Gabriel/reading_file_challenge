from utils.strip_accents import strip_accents


def text_conversor(text: str):
    """transform to minute letters and convert the text to slug"""

    if (" " in text) == True:

        transform_to_slug = strip_accents(text.lower().replace(" ", "_"))

        return transform_to_slug

    return strip_accents(text.lower())
