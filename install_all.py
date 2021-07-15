from utils import Printer
from constants import organization, user_containers

text_style = Printer.text_style


def get_repositories():
    from bs4 import BeautifulSoup as Analyzer
    import requests
    accounts = [f'{user}?tab=repositories' for user in [organization, user_containers]]
    repos_data = {}
    get_request_data = lambda git_account: Analyzer(requests.get(git_account).text, 'html.parser')
    iter_links = lambda request_data: request_data.find_all(
        'a', {'itemprop': 'name codeRepository'}
    )
    is_next_page = lambda user: {user.split('?')[0]: {
            link.text.split()[0]: link.get("href") for link in iter_links(get_request_data)()
    }}
    def get_request(user_account):
        links = get_request_data(user_account).find_all('a', {'itemprop': 'name codeRepository'})
        data = dict({user_account.split('?')[0]: {
            link.text.split()[0]: user_account + link.get("href") for link in links
        }})
        next_page = Analyzer('a', {'class': 'btn btn-outline BtnGroup-item'})
        if next_page:
            request_data = Analyzer(requests.get(next_page.get('href')).text, 'html.parser')
            links = request_data.find_all('a', {'itemprop': 'name codeRepository'})
            data.update({user_account.split('?')[0]: {
                link.text.split()[0]: link.get("href") for link in links
            }})
        return data
    [repos_data.update(get_request(git_user)) for git_user in [organization, containers]]
    text_style(repos_data.__str__())
    return repos_data



get_repositories()

