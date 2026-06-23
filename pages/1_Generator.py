import os

import streamlit as st
from dotenv import load_dotenv

from generator import generate_listing

load_dotenv()

st.set_page_config(page_title="Generator | Etsy Description Generator", page_icon="🛍️", layout="centered")

st.title("Etsy Description Generator")
st.caption("日本語で入力すると、英語の Etsy 出品文を生成します。")

with st.form("listing_form"):
    product_name = st.text_input("商品名", placeholder="例: 手作りレザーブレスレット")
    mood = st.text_input("商品の雰囲気", placeholder="例: ナチュラルで落ち着いた")
    color = st.text_input("メインカラー", placeholder="例: ブラウン")
    target = st.text_input("ターゲット", placeholder="例: 20〜30代の女性")
    use_case = st.text_input("用途", placeholder="例: 日常使い・プレゼント")

    submitted = st.form_submit_button("生成する", type="primary")

if submitted:
    if not all([product_name, mood, color, target, use_case]):
        st.error("すべての項目を入力してください。")
    elif not os.environ.get("OPENAI_API_KEY"):
        st.error("OPENAI_API_KEY が設定されていません。.env ファイルを確認してください。")
    else:
        with st.spinner("生成中..."):
            try:
                result = generate_listing(
                    product_name=product_name,
                    mood=mood,
                    color=color,
                    target=target,
                    use_case=use_case,
                )
                st.markdown(result)
                st.download_button(
                    label="テキストをダウンロード",
                    data=result,
                    file_name="etsy-listing.txt",
                    mime="text/plain",
                )
            except Exception as exc:
                st.error(f"生成に失敗しました: {exc}")
