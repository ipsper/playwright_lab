"""collection of playwrigth support functions"""
import asyncio
import re
from playwright.sync_api import sync_playwright, Page, expect
from playwright.async_api import async_playwright

def play_sync_screenshot(url):
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = browser_type.launch()
            page = browser.new_page()
            print('sync', page)
            page.goto(url)
            gurka = page.screenshot(path=f'example-{browser_type.name}.png')
            print('syncgurka', gurka)
            browser.close()

def play_sync_title(url):
    titlar = []
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = browser_type.launch()
            page = browser.new_page()
            print('play_sync_title', page)
            page.goto(url)
            title = page.title()
            print('syncgurka', title)
            titlar.append(title)
            browser.close()
        return titlar


async def play_async_screenshot(url):
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto(url)
            await page.screenshot(path=f'example-{browser_type.name}.png')
            await browser.close()

def async_screenshot(url):
    asyncio.run(play_async_screenshot(url))

async def play_async_title(url):
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto(url)
            title = await page.title()
            print('syncgurka', title)
            await browser.close()

def async_title(url):
    asyncio.run(play_async_title(url))




async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto('http://playwright.dev')
            await page.screenshot(path=f'example-{browser_type.name}.png')
            await browser.close()

def run_start():
    asyncio.run(main())



def test_has_title(page: Page):
    page.goto("https://playwright.dev")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_is_title(page: Page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
