from playwright.sync_api import sync_playwright
import time

def get_rank(keyword):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://www.google.com/search?q={keyword}&gl=uk&hl=en")
        time.sleep(3)
        results = page.query_selector_all('div.g a')
        for i, r in enumerate(results[:10]):
            if "ranklabel.co.uk" in r.get_attribute("href") or "ranklabel.carrd.co" in r.get_attribute("href"):
                browser.close()
                return i + 1
        browser.close()
        return ">10"

# Test
if __name__ == "__main__":
    print(get_rank("seo agency london"))
