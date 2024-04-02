import requests
import pytest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# List of URLs to be tested
urls = [
    "https://www.kingbillycasino6.com/de",
    "https://www.kingbillycasino6.com/de/jackpots",
    "https://www.kingbillycasino6.com/de/promotions",
    "https://www.kingbillycasino6.com/de/tournaments",
    "https://www.kingbillycasino6.com/de/the-legend",
    "https://www.kingbillycasino6.com/de/online-casino-payments",
    "https://www.kingbillycasino6.com/de/casino-faq",
    "https://www.kingbillycasino6.com/de/dictionary",
    "https://www.kingbillycasino6.com/de/btc-faq",
    "https://www.kingbillycasino6.com/de/complaints",
    "https://www.kingbillycasino6.com/de/terms-and-conditions",
    "https://www.kingbillycasino6.com/de/privacy-policy",
    "https://www.kingbillycasino6.com/de/responsible-gaming",
    "https://www.kingbillycasino6.com/de/cookie-policy",
    "https://www.kingbillycasino6.com/de/bonus-terms-conditions",
    "https://www.kingbillycasino6.com/de/affiliate/affiliate-terms-conditions"
]

@pytest.mark.parametrize("url", urls)
def test_url_response(url):
    logger.info(f"Testing URL: {url}")
    response = requests.get(url)
    if response.status_code not in [404, 500]:
        logger.info(f"URL {url} returned status code {response.status_code}")
    else:
        logger.error(f"URL {url} returned status code {response.status_code}")
    assert response.status_code not in [404, 500], f"URL {url} returned status code {response.status_code}"
