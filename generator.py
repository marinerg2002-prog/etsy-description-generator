import os

from openai import OpenAI

from prompts import build_prompt


def generate_listing(
    product_name: str,
    mood: str,
    color: str,
    target: str,
    use_case: str,
    *,
    model: str = "gpt-4o-mini",
    api_key: str | None = None,
) -> str:
    client = OpenAI(api_key=api_key or os.environ.get("OPENAI_API_KEY"))
    prompt = build_prompt(product_name, mood, color, target, use_case)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert Etsy SEO copywriter. "
                    "Follow the user's instructions exactly."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )

    content = response.choices[0].message.content
    if not content:
        raise RuntimeError("Empty response from the model.")
    return content.strip()
