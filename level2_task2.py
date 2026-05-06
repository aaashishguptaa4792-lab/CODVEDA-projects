import requests
from bs4 import BeautifulSoup
import csv

def scrape_data(url, output_file="scraped_data.csv"):
    try:
        # Step 1: Fetch the web page (SSL verification disabled to avoid errors)
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()
        html_content = response.text

        # Step 2: Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # Step 3: Extract specific data (example: headlines in <h2>)
        headlines = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]

        # Step 4: Save data into CSV
        with open(output_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Headline"])
            for headline in headlines:
                writer.writerow([headline])

        print(f"✅ Scraping complete. {len(headlines)} items saved to {output_file}")

    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Example site with valid headlines
    target_url = "https://www.bbc.com/news"
    scrape_data(target_url)
