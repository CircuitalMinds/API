import requests
from bs4 import BeautifulSoup


def google_search(title):
    data = dict(lyrics='', other_information=[])
    results = BeautifulSoup(requests.get(f"https://www.google.com/search?q={title}").text,
                            'html.parser').findAll(**{'name': 'div', 'class': 'BNeawe'})
    lyrics, is_lyrics = [], True
    for result in results:
        if result.div is None:
            matches = result.text.split('\n')
            for j in range(matches.count('')):
                matches.remove('')
            for target in matches:
                if len(target.split(':')) == 2:
                    k, v = target.split(':')[:2]
                    data.update({k.strip(): v.strip()})
                    if is_lyrics:
                        is_lyrics = False
                elif is_lyrics:
                    lyrics.append(target)
                else:
                    data['other_information'].append(target)
    if lyrics:
        data.update(dict(lyrics='\n'.join(lyrics)))
    return data


def wikipedia_search(title):
    data = {}
    wiki = 'wikipedia.org/wiki'
    links = []
    unquote = requests.utils.unquote
    quote = requests.utils.quote
    safe_url = lambda url: f'{"/".join(url.split("/")[:-1])}/{quote(unquote(unquote(url.split("/")[-1])))}'
    url_query = f"https://www.google.com/search?q={'+'.join(title.split())}"
    for a in BeautifulSoup(
            requests.get(url_query).text,
            'html.parser'
    ).find_all('a'):
        href = a.get('href')
        link = href.replace('/url?q=', '').split('&')[0]
        target = unquote(unquote(link.split('/')[-1])).lower()
        if wiki in link and any([target.find(w) != -1 for w in title.split()]):
            links.append(safe_url(url=link))
    for link in links:
        try:
            html_parser = BeautifulSoup(
                requests.get(link).text,
                'html.parser'
            ).find_all('tr')
            name = unquote(unquote(link.split('/')[-1]))
            data[name] = {"description": '', 'url': link}
            for tr in html_parser:
                th, td = tr.th, tr.td
                if td is None:
                    for ti in tr.contents:
                        if ti.find('a') is None:
                            data[name]["description"] += ' '.join([ti.text])
                        else:
                            data[name]["description"] += f' {"".join([ai.get("title") for ai in ti.find_all("a")])} '
                elif None not in [th.find('a'), td.find('a')]:
                    data[name].update({th.find('a').get('title'): ' '.join(td.find('a').get('title').split())})
                elif th.find('a') is not None:
                    data[name].update({th.find('a').get('title'): ' '.join(td.text.split())})
                elif td.find('a') is not None:
                    data[name].update({th.text: ' '.join(td.find('a').get('title').split())})
        except AttributeError:
            pass
    info = dict()
    for n in data.keys():
        data_n = data[n]
        for k in data_n.keys():
            if k not in info.keys():
                info.update({k: [data_n[k]]})
            elif data_n[k] not in info[k]:
                info[k].append(data_n[k])
    return info
