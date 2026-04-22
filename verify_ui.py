import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1280, 'height': 1600})

        try:
            await page.goto('http://localhost:8501')
            await page.wait_for_timeout(5000)  # Wait for app to load

            # 1. Capture Operacion (Range Bars)
            await page.screenshot(path='/home/jules/verification/v2_operacion.png', full_page=True)

            # 2. Capture Monitoreo (Line Charts)
            await page.click('text=Monitoreo')
            await page.wait_for_timeout(2000)
            await page.screenshot(path='/home/jules/verification/v2_monitoreo.png', full_page=True)

            # 3. Capture Fluidograma (KPI Cards)
            await page.click('text=Fluidograma Integrado')
            await page.wait_for_timeout(2000)
            await page.screenshot(path='/home/jules/verification/v2_fluidograma.png', full_page=True)

            print("Screenshots captured successfully.")

        except Exception as e:
            print(f"Error during verification: {e}")
        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
