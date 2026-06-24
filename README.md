# Etsy Description Generator

日本語で商品情報を入力するだけで、Etsy 向けの英語出品文を自動生成するツールです。OpenAI API を使い、Title・Description・SEO Tags・Instagram Caption などを一括で作成します。

## できること

- **出品文の一括生成** — Etsy Title、商品説明、13 個の SEO Tags、Main Color、Instagram Caption を英語で出力
- **日本語入力** — 商品名・雰囲気・カラー・ターゲット・用途は日本語のまま入力可能
- **SEO を意識した文案** — Etsy で検索されやすいキーワードを盛り込んだ表現を生成

## 技術スタック

- Python
- [Streamlit](https://streamlit.io/) — ローカル Web UI
- [Vercel](https://vercel.com/) — ランディングページのホスティング
- [OpenAI API](https://platform.openai.com/) — 文案生成（デフォルト: `gpt-4o-mini`）

## セットアップ

```bash
# リポジトリをクローン
git clone https://github.com/marinerg2002-prog/etsy-description-generator.git
cd etsy-description-generator

# 仮想環境の作成と有効化（任意）
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS / Linux

# 依存パッケージのインストール
pip install -r requirements.txt

# 環境変数の設定
cp .env.example .env
# .env に OpenAI API キーを設定
```

`.env` ファイルに以下を記述してください。

```
OPENAI_API_KEY=your_openai_api_key_here
```

## 使い方

### Web UI（Streamlit・ローカル）

```bash
streamlit run streamlit_app.py
```

ブラウザでランディングページが開きます。「今すぐ生成する」から Generator ページへ進み、商品情報を入力して出品文を生成できます。生成結果はコピーまたはテキストファイルとしてダウンロードできます。

### CLI

```bash
python cli.py \
  --product-name "手作りレザーブレスレット" \
  --mood "ナチュラルで落ち着いた" \
  --color "ブラウン" \
  --target "20〜30代の女性" \
  --use-case "日常使い・プレゼント"
```

### Vercel デプロイ

`public/index.html` を静的サイトとして配信します。リポジトリを Vercel に接続するだけでデプロイできます。

```bash
vercel
```

生成機能は Streamlit 版をローカルで実行してください。

## プロジェクト構成

```
etsy-description-generator/
├── public/
│   └── index.html      # Vercel 用ランディングページ
├── streamlit_app.py    # Streamlit ランディングページ
├── pages/
│   └── 1_Generator.py  # 出品文生成フォーム
├── generator.py        # OpenAI API 呼び出し
├── prompts.py          # プロンプト定義
├── cli.py              # CLI エントリーポイント
├── vercel.json
├── requirements.txt
└── .env.example
```
