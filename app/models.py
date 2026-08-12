from dataclasses import dataclass
from typing import List


@dataclass
class WebPage:
    """Represents the content extracted from a web page."""

    url: str
    title: str
    content: str


@dataclass
class Brochure:
    """Represents the generated brochure."""

    company_name: str
    website: str
    markdown: str


@dataclass
class WebsiteData:
    """Stores all information collected from a website."""

    company_name: str
    website: str
    pages: List[WebPage]