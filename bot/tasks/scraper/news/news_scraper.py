import requests
import re
from typing import List, Optional
import re

_news_url = "https://www.mikulasske.cz/"


def _clean_url(url: str) -> str:
    """Cleans a given url."""
    url = url.replace("\"", "")
    url = url.strip()
    return url 


def _get_article_urls() -> List[str]:
    """Returns all urls of articles on the mikulasske homepage."""
    html = requests.get(_news_url).text
    output = []
    # Moves to the section with articles.
    index = html.find("vypis_clanku")
    # Adds all links to the array.
    while html.find("href=", index) < html.find("<footer", index):
        index = html.find("href=", index) + 5
        # Adds every article only once.
        if html.find("</a>", index) < html.find("Pokračovat ve čtení", index):
            end_of_url = html.find("rel=", index)
            output.append(_clean_url(html[index:end_of_url]))
    return output


article_urls = _get_article_urls()


def update_article_urls() -> None:
    """Updates the articles' urls list."""
    article_urls = _get_article_urls()
    

def _remove_html_tags(text: str) -> str:
    """Removes html tags in the given text."""
    text = re.sub("<.*?>", "", text)
    return re.sub("&.*?;", "", text)


def _get_article_from_url(url: str) -> str:
    """Returns the plain text of the article on a given url."""
    html = requests.get(url).text
    # Moves to the article section.
    index = html.find("entry-content")
    index = html.find(">", index) + 1
    article_end = html.find("</article>", index)
    return _remove_html_tags(html[index:article_end]).strip()


def get_article(index: int) -> Optional[str]:
    """
    Returns the [index]-th newest article form the page.
    If there are not enough articles on the first page, returns None.
    """
    if index >= len(article_urls):
        return
    return _get_article_from_url(article_urls[index])

def handle() -> str:
    """Return the newest message from the webpage."""
    update_article_urls()
    article = get_article(0)
    if article == None:
        return "Na školní stránce nejsou žádné články."
    return "Poslední zpráva na školních stránkách je následující:\n" + article
    

