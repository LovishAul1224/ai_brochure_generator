LINK_SELECTION_PROMPT = """
You are an AI assistant helping generate a professional company brochure.

Below is a list of links found on the company's website.

Your task is to select only the links that are useful for understanding the company.

Prioritize pages such as:
- About
- Company
- Products
- Services
- Solutions
- Features
- Careers
- Team
- Mission
- Vision

Ignore pages such as:
- Login
- Sign In
- Register
- Privacy Policy
- Terms of Service
- Cookie Policy
- Sitemap
- Blog
- News
- Press
- Contact

Return only a valid Python list.

Links:
{links}
"""


BROCHURE_PROMPT = """
You are an expert marketing copywriter.

Use the information below to write a professional brochure in Markdown format.

Requirements:
- Begin with the company name as a heading.
- Add a short company overview.
- Describe the products or services.
- Highlight the company's strengths.
- Keep the brochure concise and engaging.
- Do not invent information that is not provided.

Website Content:

{content}
"""