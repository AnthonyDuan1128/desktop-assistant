import requests
from bs4 import BeautifulSoup

class SearchService:
    def __init__(self):
        pass

    def search_baidu(self, query):
        url = f"https://www.baidu.com/s?wd={query}"
        response = requests.get(url)
        return self.parse_search_results(response.text)

    def search_bing(self, query):
        url = f"https://www.bing.com/search?q={query}"
        response = requests.get(url)
        return self.parse_search_results(response.text)

    def custom_search(self, url, query):
        response = requests.get(f"{url}?q={query}")
        return self.parse_search_results(response.text)

    def parse_search_results(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        results = []
        for item in soup.find_all('h2'):
            link = item.find('a')
            if link:
                title = item.text
                url = link['href']
                # Simple heuristic to filter out ads
                if "ad" not in title.lower() and "sponsored" not in title.lower():
                    results.append({'title': title, 'url': url})
        return results