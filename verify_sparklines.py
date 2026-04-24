import asyncio
from playwright.async_api import async_playwright
import os

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Wait for Streamlit to start
        max_retries = 10
        for i in range(max_retries):
            try:
                await page.goto("http://localhost:8501")
                break
            except Exception:
                if i == max_retries - 1:
                    raise
                await asyncio.sleep(2)

        # Wait for title
        await page.wait_for_selector("h1")

        # Click Monitoreo in sidebar
        await page.click("text=Monitoreo")
        await asyncio.sleep(2)

        # Click "Paso" a few times to generate history
        for _ in range(5):
            await page.click("text=Paso")
            await asyncio.sleep(1)

        # Take screenshot of Monitoreo
        os.makedirs("verification", exist_ok=True)
        await page.screenshot(path="verification/sparklines_final.png", full_page=True)

        # Verify Plotly charts exist
        plotly_charts = await page.query_selector_all(".js-plotly-plot")
        print(f"Found {len(plotly_charts)} Plotly charts")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
