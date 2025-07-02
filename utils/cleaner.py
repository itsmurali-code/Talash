import re


def clean_text(text):
    """
    Cleans Wikipedia text by removing extra whitespace, references, and markdown artifacts.
    """
    # Remove bracketed references like [1], [citation needed], etc.
    text = re.sub(r'\[\d+\]', '', text)
    text = re.sub(r'\[citation needed\]', '', text, flags=re.IGNORECASE)

    # Remove multiple newlines and trim
    text = re.sub(r'\n+', '\n', text).strip()

    # Remove excessive spaces
    text = re.sub(r' +', ' ', text)

    return text