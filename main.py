import asyncio

from services import browser
from services.functions import load_proxies, parse_proxies


def main():
    proxies = load_proxies()
    parsed_proxies = parse_proxies(proxies)
    asyncio.run(browser.main(parsed_proxies[0]))


if __name__ == "__main__":
    main()
