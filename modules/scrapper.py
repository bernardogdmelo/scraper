import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Scraper:
    def __init__(self, url):
        self.url = url

    async def scrape_with_selenium(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=chrome_options)
        try:
            driver.get(self.url)
            await asyncio.sleep(2)  # wait for content to load
            return (
                driver.find_element(By.XPATH, "/html/body").text.split("\n"),
                driver.page_source,
            )
        finally:
            driver.quit()
