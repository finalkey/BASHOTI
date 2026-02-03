import os
from typing import List, Any
import aiohttp
import asyncio

from app.core.config import settings

class LLMService:
    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY
        # Example: use OpenAI-compatible HTTP API. Replace with your provider.
        self.base_url = "https://api.openai.com/v1"

    def build_prompt(self, query: str, contexts: List[Any]) -> str:
        ctx_text = "\n\n".join([c.get("payload", {}).get("text", "") for c in contexts])
        prompt = f"Use the following context to answer the question.\n\nContext:\n{ctx_text}\n\nQuestion: {query}\n\nAnswer:"
        return prompt

    async def complete(self, prompt: str, model: str = "gpt-4o-mini") -> str:
        # Minimal async HTTP call to an OpenAI-like completion API
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {"model": model, "prompt": prompt, "max_tokens": 512}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/completions", json=payload, headers=headers) as resp:
                data = await resp.json()
                # Adapt parsing to provider format
                return data.get("choices", [{}])[0].get("text", "").strip()
