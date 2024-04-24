import asyncio
from bs4 import BeautifulSoup

from modules.scrapper import Scraper
from modules.phone_numbers import PhoneNumberExtractor, PhoneNumbersFilter
from modules.logo_finder import LogoFinder


output_total = []


async def process_response(url, response, html_content, semaphore):
    if response:

        extractor = PhoneNumberExtractor(response)
        phone_numbers = extractor.extract_phone_numbers()

        phone_number_filter = PhoneNumbersFilter(phone_numbers)
        filtered_numbers = phone_number_filter.filter_numbers()

        soup_object = BeautifulSoup(html_content, "html.parser")
        logo_finder = LogoFinder(url, soup_object)
        logos = logo_finder.search_for_logos()

        print({"logos": logos, "phones": filtered_numbers, "website": url})
        output_total.append(
            {"logos": logos, "phones": filtered_numbers, "website": url}
        )

    semaphore.release()


async def scrape_and_process(url, semaphore):
    async with semaphore:
        try:
            scraper = Scraper(url)
            response, html_content = await scraper.scrape_with_selenium()

            await process_response(url, response, html_content, semaphore)
        except Exception as e:
            print("There was a problem with:", url, e)


async def main(urls):
    semaphore = asyncio.Semaphore(10)

    tasks = []
    for url in urls:
        async with semaphore:
            tasks.append(asyncio.create_task(scrape_and_process(url, semaphore)))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    print("Starting scrapper....")
    file_path = "websites.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()

    websites_list = [line.strip() for line in lines]

    asyncio.run(main(websites_list))

    print("Data found:")
    for json in output_total:
        print(json)
