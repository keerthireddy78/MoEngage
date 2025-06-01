import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import re

async def extract_text_from_url(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_timeout(5000)  # wait 5 seconds for JS to load content

        content = await page.content()
        await browser.close()
        return content

def get_clean_text_from_url(url):
    html_content = asyncio.run(extract_text_from_url(url))
    soup = BeautifulSoup(html_content, "html.parser")

    # MoEngage article main content is inside div with class 'article-body'
    article = soup.find("div", class_="article-body")

    if not article:
        return "Could not find main content area."

    # Extract text with new lines between paragraphs
    text = article.get_text(separator="\n").strip()

    # Remove citation brackets like [1], [2] if present
    clean_text = re.sub(r'\[\d+\]', '', text)

    return clean_text


# For local testing
if __name__ == "__main__":
    test_url = "https://help.moengage.com/hc/en-us/articles/360001520773-What-is-an-Event-"
    print(get_clean_text_from_url(test_url))
