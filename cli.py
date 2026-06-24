import argparse
import os
import sys

from dotenv import load_dotenv

from generator import generate_listing

load_dotenv()


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Etsy listing copy from Japanese inputs.")
    parser.add_argument("--product-name", required=True, help="商品名")
    parser.add_argument("--mood", required=True, help="商品の雰囲気")
    parser.add_argument("--color", required=True, help="メインカラー")
    parser.add_argument("--target", required=True, help="ターゲット")
    parser.add_argument("--use-case", required=True, help="用途")
    parser.add_argument("--model", default="gpt-4o-mini", help="OpenAI model name")
    args = parser.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY is not set.", file=sys.stderr)
        sys.exit(1)

    result = generate_listing(
        product_name=args.product_name,
        mood=args.mood,
        color=args.color,
        target=args.target,
        use_case=args.use_case,
        model=args.model,
    )
    print(result)


if __name__ == "__main__":
    main()
