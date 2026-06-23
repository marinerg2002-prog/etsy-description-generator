def build_prompt(
    product_name: str,
    mood: str,
    color: str,
    target: str,
    use_case: str,
) -> str:
    return f"""あなたはEtsy SEOの専門家です。

以下の商品情報を参考にしてください。

商品名: {product_name}
商品の雰囲気: {mood}
メインカラー: {color}
ターゲット: {target}
用途: {use_case}

重要:
入力内容は日本語ですが、以下の出力内容はすべて英語で作成してください。

出力項目:
1. Etsy Title
2. Product Description
3. 13 Etsy SEO Tags
4. Main Color
5. Instagram Caption

英語圏の購入者向けに自然で魅力的な英語で作成してください。
Etsy SEOを意識し、検索されやすい表現を使用してください。

出力形式:
各項目を次の見出しで区切ってください。

## Etsy Title
（140文字以内。主要キーワードを前半に配置）

## Product Description
（冒頭で商品の魅力を簡潔に伝え、素材・サイズ・使い方・ギフト用途などを含む。読みやすい段落構成）

## Etsy SEO Tags
（13個。各タグは20文字以内。カンマ区切りで1行）

## Main Color
（Etsyのカラー設定用。英語で1つ）

## Instagram Caption
（絵文字を適度に使い、ハッシュタグは3〜5個）
"""
