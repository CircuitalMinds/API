from bs4 import BeautifulSoup
import requests


class WikiSearch:

    url = 'https://en.wikipedia.org/wiki'

    def query_video_by_title(self, title):
        data = dict()
        title = title.split()
        search = '_'.join(title[:title.index('-')]) if '-' in title else '_'.join(title)
        response = requests.get(f'{self.url}/{search}').text
        try:
            html_parser = BeautifulSoup(response, 'html.parser').find('table').find_all('tr')
            for tr in html_parser:
                if tr.find('th') is not None and tr.find('td') is not None:
                    content = list(dict.fromkeys(tr.find('td').text.split('\n')).keys())
                    if '' in content:
                        content.remove('')
                    if len(content) == 1:
                        data[tr.find('th').text] = content[0]
                    else:
                        data[tr.find('th').text] = content
        except AttributeError:
            pass
        return data

    def get_wiki_data(self, video_containers):
        for video_container in video_containers:
            for title in video_container.video_list.keys():
                video_container.search_data[title] = self.query_video_by_title(title=title)
            video_container.save_search_data()
