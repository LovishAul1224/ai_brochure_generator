from app.brochure_generator import BrochureGenerator
from app.link_selector import LinkSelector
from app.llm import OpenRouterClient
from app.models import WebsiteData
from app.scraper import WebsiteScraper


class BrochureService:
    """Coordinates brochure generation."""

    def __init__(
        self,
        scraper: WebsiteScraper,
        llm: OpenRouterClient,
    ) -> None:

        self.scraper = scraper

        self.selector = LinkSelector(llm)

        self.generator = BrochureGenerator(llm)

    def generate(
        self,
        company_name: str,
        website_url: str,
    ) -> str:

        homepage = self.scraper.fetch_page(
            website_url
        )

        links = self.scraper.extract_links(
            website_url
        )

        selected_links = self.selector.select(
            links
        )

        pages = [homepage]

        for link in selected_links[:5]:

            try:
                pages.append(
                    self.scraper.fetch_page(link)
                )

            except Exception:
                continue

        website_data = WebsiteData(
            company_name=company_name,
            website=website_url,
            pages=pages,
        )

        return self.generator.generate(
            website_data
        )