import streamlit as st

from app.brochure_service import BrochureService
from app.llm import OpenRouterClient
from app.scraper import WebsiteScraper


st.set_page_config(
    page_title="AI Brochure Generator",
    page_icon="📄",
    layout="wide",
)

st.markdown(
    """
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}



.hero h1{
    font-size:3rem;
    margin-bottom:0.5rem;
}

.hero p{
    font-size:1.1rem;
    opacity:0.9;
}

div[data-testid="stForm"]{
    border:1px solid #333;
    padding:1.5rem;
    border-radius:16px;
}

.stDownloadButton>button{
    width:100%;
}

</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero">
<h1>📄 AI Brochure Generator</h1>
<p>
Generate beautiful company brochures using Large Language Models.
</p>
</div>
""",
    unsafe_allow_html=True,
)

left, right = st.columns([2, 1])

with left:

    with st.form("brochure_form"):

        company_name = st.text_input(
            "🏢 Company Name",
            placeholder="OpenAI",
        )

        website = st.text_input(
            "🌐 Website URL",
            placeholder="https://openai.com",
        )

        submitted = st.form_submit_button(
            " Generate Brochure",
            use_container_width=True,
        )

with right:

    st.info(
        """
### 💡 Tips

- Use the official company website.

- Large websites may take a little longer.

- The brochure is generated using AI.

- Markdown can be downloaded.
"""
    )

if submitted:

    scraper = WebsiteScraper()

    llm = OpenRouterClient()

    service = BrochureService(
        scraper=scraper,
        llm=llm,
    )

    progress = st.progress(0)

    status = st.empty()

    status.write("🌐 Scraping website...")
    progress.progress(25)

    brochure = service.generate(
        company_name=company_name,
        website_url=website,
    )

    status.write("🤖 Generating brochure...")
    progress.progress(75)

    progress.progress(100)

    status.empty()

    st.success("✅ Brochure Generated Successfully!")

    st.markdown("## 📄 Preview")

    st.markdown(brochure)

    st.download_button(
        "⬇ Download Markdown",
        brochure,
        file_name=f"{company_name.lower()}_brochure.md",
        mime="text/markdown",
        use_container_width=True,
    )