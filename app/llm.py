from openai import OpenAI

from app.config import MODEL, OPENROUTER_API_KEY


class OpenRouterClient:
    """Client for interacting with OpenRouter models."""

    def __init__(self) -> None:
        self.client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
        )

    def generate(
        self,
        prompt: str,
        temperature: float = 0.7,
    ) -> str:
        """
        Generate a response from the configured LLM.
        """

        response = self.client.chat.completions.create(
            model=MODEL,
            temperature=temperature,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content.strip()