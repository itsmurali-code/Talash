import wikipediaapi

def extract_title_from_url(url):
    """
    Extracts the page title from a Wikipedia URL.
    Example: 'https://en.wikipedia.org/wiki/India' → 'India'
    """
    if "wiki/" not in url:
        raise ValueError("Invalid Wikipedia URL")
    return url.strip().split("wiki/")[-1]

def scrape_wikipedia_pages(url_string):
    """
    Takes a comma-separated string of Wikipedia URLs and returns a dictionary
    of {title: full text}.
    """
    # Add a proper User-Agent (important!)
    USER_AGENT = "TalashApp/1.0 (contact: your-email@example.com)"
    wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent=USER_AGENT
    )

    urls = [url.strip() for url in url_string.split(",") if url.strip()]
    page_data = {}

    for url in urls:
        title = extract_title_from_url(url)
        page = wiki.page(title)
        if not page.exists():
            print(f"Page not found: {title}")
            continue
        page_data[title] = page.text

    return page_data