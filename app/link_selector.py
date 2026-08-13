import ast

from app.llm import OpenRouterClient
from app.prompts import LINK_SELECTION_PROMPT


class LinkSelector:
    """Uses an LLM to choose the most relevant website links."""

    def __init__(self, llm: OpenRouterClient) -> None:
        self.llm = llm

    def select(self, links: list[str]) -> list[str]:
        prompt = LINK_SELECTION_PROMPT.format(
            links="\n".join(links)
        )

        response = self.llm.generate(
            prompt,
            temperature=0,
        )

        try:
            selected = ast.literal_eval(response)

            if isinstance(selected, list):
                return selected

        except (SyntaxError, ValueError):
            pass

        return []