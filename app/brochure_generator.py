from app.llm import OpenRouterClient
from app.models import WebsiteData
from app.prompts import BROCHURE_PROMPT


class BrochureGenerator:
    """Generates a brochure from website content."""

    def __init__(self, llm: OpenRouterClient) -> None:
        self.llm = llm

    def generate(self, website_data: WebsiteData) -> str:

        content = []

        for page in website_data.pages:
            content.append(f"# {page.title}")
            content.append(page.content)

        prompt = BROCHURE_PROMPT.format(
            content="\n\n".join(content)
        )

        return self.llm.generate(prompt)