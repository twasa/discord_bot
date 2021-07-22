from bs4 import BeautifulSoup


def parse_langrisser_wiki_search_result(html_str):
    data = BeautifulSoup(html_str, 'html.parser')
    all_div = data.find_all("div", {"class": "mw-search-result-heading"})
    if all_div:
        first_div = all_div[0]
        all_a = first_div.findAll('a')
        if all_a:
            first_a = all_a[0]
            url = first_a.get('href')
            return url
    return '找不到資訊'
