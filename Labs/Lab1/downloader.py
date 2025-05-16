import requests
from concurrent.futures import ThreadPoolExecutor
from parser import parse_xml_to_json
from saver import already_downloaded, save_data

def build_url(date, base_currency):
    return (f"https://www.floatrates.com/historical-exchange-rates.html?"
            f"operation=rates&pb_id=1775&page=historical&currency_date={date}"
            f"&base_currency_code={base_currency}&format_type=xml")

def fetch_and_save(date, currency):
    date_str = date.isoformat()
    if already_downloaded(currency, date_str):
        print(f"[Cache] Skipping {currency} on {date_str}")
        return

    url = build_url(date_str, currency)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        parsed = parse_xml_to_json(response.text)
        if parsed:
            save_data(currency, date_str, parsed)
            print(f"[Saved] {currency} on {date_str}")
    except Exception as e:
        print(f"[Error] {currency} on {date_str}: {e}")

def download_currency_for_dates(currency, dates):
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(lambda d: fetch_and_save(d, currency), dates)