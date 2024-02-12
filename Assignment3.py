import csv
import re
import argparse
import requests

def download_log_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("web_log.csv", "wb") as file:
            file.write(response.content)
    else:
        print("Failed to download the log file.")
        exit()

def process_log_file():
    image_hits = 0
    total_hits = 0
    browsers = {"Firefox": 0, "Chrome": 0, "Internet Explorer": 0, "Safari": 0}

    with open("web_log.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(row) == 5:
                total_hits += 1
                path, _, user_agent, _, _ = row

                # Search for image hits
                if re.search(r'\.(jpg|gif|png)$', path, re.IGNORECASE):
                    image_hits += 1

                # Find the most popular browser
                if re.search(r'Firefox', user_agent, re.IGNORECASE):
                    browsers["Firefox"] += 1
                elif re.search(r'Chrome', user_agent, re.IGNORECASE):
                    browsers["Chrome"] += 1
                elif re.search(r'Internet Explorer', user_agent, re.IGNORECASE):
                    browsers["Internet Explorer"] += 1
                elif re.search(r'Safari', user_agent, re.IGNORECASE):
                    browsers["Safari"] += 1

    return image_hits, total_hits, browsers

def main():
    parser = argparse.ArgumentParser(description="Web Log Analysis")
    parser.add_argument("--url", help="URL of the web log file", required=True)
    args = parser.parse_args()

    # Part I: Download the web log file
    download_log_file(args.url)

    # Part II: Process the log file using CSV
    image_hits, total_hits, browsers = process_log_file()

    # Part III: Search for image hits
    image_percentage = (image_hits / total_hits) * 100
    print(f"Image requests account for {image_percentage:.1f}% of all requests")

    # Part IV: Finding the most popular browser
    most_popular_browser = max(browsers, key=browsers.get)
    print(f"The most popular browser is {most_popular_browser}")

if __name__ == "__main__":
    main()

