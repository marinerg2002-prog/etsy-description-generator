import streamlit as st

st.set_page_config(
    page_title="Etsy Description Generator",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 3rem;
        padding-bottom: 4rem;
        max-width: 960px;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        line-height: 1.2;
        margin-bottom: 1rem;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: #5f6368;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: #f8f9fb;
        border: 1px solid #e8eaed;
        border-radius: 16px;
        padding: 1.5rem;
        height: 100%;
    }
    .feature-card h3 {
        margin-top: 0;
        margin-bottom: 0.5rem;
        font-size: 1.1rem;
    }
    .feature-card p {
        margin: 0;
        color: #5f6368;
        line-height: 1.6;
    }
    .step-number {
        display: inline-block;
        width: 2rem;
        height: 2rem;
        line-height: 2rem;
        text-align: center;
        border-radius: 999px;
        background: #ff6b6b;
        color: white;
        font-weight: 700;
        margin-right: 0.75rem;
    }
  </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="hero-title">日本語で入力するだけ。<br>Etsy 出品文を英語で自動生成。</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="hero-subtitle">'
    "商品名・雰囲気・カラー・ターゲット・用途を入力するだけで、"
    "Title・Description・SEO Tags・Instagram Caption まで一括作成。"
    "</p>",
    unsafe_allow_html=True,
)

if st.button("今すぐ生成する", type="primary"):
    st.switch_page("pages/1_Generator.py")

st.divider()

st.subheader("できること")
feature_cols = st.columns(3)

features = [
    ("📝", "出品文を一括生成", "Etsy Title、商品説明、13個の SEO Tags、Main Color、Instagram Caption を英語で出力。"),
    ("🌏", "日本語入力OK", "商品情報は日本語で入力。英語圏の購入者向けに自然な文章へ変換します。"),
    ("🔍", "SEO を意識", "検索されやすいキーワードを盛り込み、Etsy で見つかりやすい表現を提案します。"),
]

for col, (icon, title, body) in zip(feature_cols, features):
    with col:
        st.markdown(
            f"""
            <div class="feature-card">
                <h3>{icon} {title}</h3>
                <p>{body}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

st.subheader("使い方")

steps = [
    "商品名・雰囲気・カラー・ターゲット・用途を入力",
    "「生成する」をクリック",
    "英語の出品文をコピーまたはダウンロード",
]

for index, step in enumerate(steps, start=1):
    st.markdown(
        f'<p><span class="step-number">{index}</span>{step}</p>',
        unsafe_allow_html=True,
    )

st.divider()

st.markdown("#### さっそく試してみる")
st.page_link("pages/1_Generator.py", label="Generator ページへ", icon="🛍️")
