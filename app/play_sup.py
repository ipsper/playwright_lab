"""collection of playwrigth support functions"""
import asyncio
import re
from playwright.sync_api import sync_playwright, Page, expect
from playwright.async_api import async_playwright

def play_sync_screenshot(url, browsers):
    """let playwrigth get all screenshot syncroniced"""
    filenames = []
    with sync_playwright() as p:
        browser_list = [getattr(p, browser_name) for browser_name in browsers]
        for browser_type in browser_list:
            browser = browser_type.launch()
            page = browser.new_page()
            page.goto(url)
            filename = f'example-{browser_type.name}.png'
            page.screenshot(path=filename)
            filenames.append(filename)
            browser.close()
        return filenames

def play_sync_index_title(url, browsers):
    """let playwrigth get all index title syncroniced"""
    titlar = []
    with sync_playwright() as p:
        browser_list = [getattr(p, browser_name) for browser_name in browsers]
        for browser_type in browser_list:
            browser = browser_type.launch()
            page = browser.new_page()
            print('play_sync_index_title', page)
            page.goto(url)
            title = page.title()
            print('syncgurka', title)
            titlar.append(title)
            browser.close()
        return titlar


async def helper_async_screenshot(url, browsers):
    """helper screenshot asyncroniced"""
    async with async_playwright() as p:
        browser_list = [getattr(p, browser_name) for browser_name in browsers]
        for browser_type in browser_list:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto(url)
            await page.screenshot(path=f'example-{browser_type.name}.png')
            await browser.close()

def play_async_screenshot(url, browsers):
    """let playwrigth get all screenshot asyncroniced"""
    asyncio.run(helper_async_screenshot(url, browsers))

async def do_get_title(browser_type, url):
    """doer index title asyncroniced"""
    browser = await browser_type.launch()
    page = await browser.new_page()
    await page.goto(url)
    title = await page.title()
    print('syncgurka', title)
    return title

async def play_async_title(url, browsers):
    """helper index title asyncroniced"""
    titles = []
    async with async_playwright() as p:
        browser_list = [getattr(p, browser_name) for browser_name in browsers]
        for browser_type in browser_list:
            title = await do_get_title(browser_type, url)
            titles.append(title)
    return titles

def play_async_index_title(url, browsers):
    """let playwrigth get all index title asyncroniced"""
    results = asyncio.run(play_async_title(url, browsers))
    return results

async def main():
    """let playwrigth main"""
    async with async_playwright() as p:
        browser_list = [p.chromium, p.firefox, p.webkit]
        for browser_type in browser_list:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto('http://playwright.dev')
            await page.screenshot(path=f'example-{browser_type.name}.png')
            await browser.close()

def run_start():
    """let playwrigth bla"""
    asyncio.run(main())



def test_has_title(page: Page):
    """playwrigth has_title"""
    page.goto("https://playwright.dev")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    """playwrigth get_started_link"""
    page.goto("https://playwright.dev/")
    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_is_title(page: Page):
    """playwrigth is_title"""
    page.goto("https://example.com")
    assert page.title() == "Example Domain"


def all_elements_is_same(title, lista, len_browsers):
    """check if all elements is the same"""
    if len(lista) != len_browsers:
        return False
    if not lista:
        return False
    return all(element == title for element in lista)
