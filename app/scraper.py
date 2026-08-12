from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from app.config import MAX_CONTENT_LENGTH, REQUEST_TIMEOUT
from app.models import WebPage


class WebsiteScraper:
    """Fetches website content and extracts useful information."""

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/138.0.0.0 Safari/537.36"
                )
            }
        )

    def fetch_page(self, url: str) -> WebPage:
        """
        Fetch a web page and return its cleaned content.
        """
        response = self.session.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "Untitled"

        # Remove elements that are not useful for the LLM.
        for tag in soup(["script", "style", "noscript", "svg", "img", "footer"]):
            tag.decompose()

        content = ""

        if soup.body:
            content = soup.body.get_text(separator="\n", strip=True)

        content = content[:MAX_CONTENT_LENGTH]

        return WebPage(
            url=url,
            title=title,
            content=content,
        )

    def extract_links(self, url: str) -> list[str]:
        """
        Extract all internal links from a website.
        """
        response = self.session.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        domain = urlparse(url).netloc
        links: set[str] = set()

        for anchor in soup.find_all("a", href=True):
            absolute_url = urljoin(url, anchor["href"])

            if urlparse(absolute_url).netloc == domain:
                links.add(absolute_url)

        return sorted(links)