# Websites Scrapper

A tool developed for CIAL as part of its interview and recruitment process.

## 1 - Overview and Considerations

Project overview:
This tool is a webscrapping tool with the goal of extracting phone numbers and logo images of the inputed URL's.
- It was built using Selenium for phone number extraction because I found it easier to gather and proccess the pure text on the url using it,
Using several regex patterns to try and match a valid format of phone number.
- To find the logo images, using BeautifulSoup4 was better as it is always embedded in the HTML tags in some way.
- The whole application is ran using asyncio, a Python asynchronous programming lib. It is currently processing 10 cocurrent URL's at a time, as the machine
I was developing it in had a severe lack of memory problem, so I had to limit it. If wished, just readjust the 'semaphore' variable in main function of main.py to run more browsers cocurrently.

Considerations:
I failed to be able to run this application on a docker container. Several issues occur using Selenium that for the time being, I was not able to handle.
I was able to install ChromeBrowser and ChromeDriver in the container, the Dockerfile on this project works, but to be able to run it inside the container is a whole other range of problems, such network problems,
I tried to also run the chromedriver remotely with the standalone chromedriver image that Selenium provides for Docker, but ran into errors too and wasn't able for the time being to find the cause and solve it.

## 2 - Installation & Setup

To get started with, follow these simple installation steps:

1. Clone the repository:

```bash
git clone https://github.com/bernardogdmelo/scraper.git
```

2. Checkout to 'dev' branch:

```bash
git checkout dev
```

3. Change the directory:

```bash
cd scraper
```

4. Install all the requirements:

```bash
pip3 install -r requirements.txt
```

## 3 - Usage

To run this scraper, simply run the following command on the terminal:

```bash
python3 main.py
```

To add/remove URL's to be scrapped, use the website.txt file on the project.
