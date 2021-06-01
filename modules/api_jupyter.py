import subprocess
import yaml
import requests


class JupyterApp:
    def __init__(self):
        notebooks_url = {"engineering_basic":
                             "https://raw.githubusercontent.com/alanmatzumiya/engineering-basic/main/notebooks_data.json",
                         "data_analysis":
                             "https://raw.githubusercontent.com/alanmatzumiya/data_analysis/main/notebooks_data.json"}
        loader = lambda user: yaml.load(
            subprocess.getoutput(f"cd ./db && python3 -m get_repo_links {user}").__str__(), Loader = yaml.FullLoader)
        self.notebooks = {key: requests.get(notebooks_url[key]).json() for key in list(notebooks_url.keys())}
        self.repos = {"alanmatzumiya": lambda : loader(user="alanmatzumiya"),
                      "CircuitalMinds": lambda : loader(user="CircuitalMinds")}

    @staticmethod
    def try_key(item, keys):
        get_value = lambda data, key: data[key]
        values = item
        for key in keys:
            try:
                values = get_value(data=values, key=key)
            except KeyError:
                values = {}
                break
        return values

    def get_notebooks(self, args):
        topic, module = args["topic"].replace('-', '_'), args["module"]
        return {topic: {module: self.notebooks[topic][module]}}

    def get_repos(self, args):
        user = args["user"]
        if user in list(self.repos.keys()):
            return self.repos[user]()
        else:
            return {"Response": f"repos for user : {user} not exist"}


    def covid19(self, args=None):
        API = "https://covid19.mathdro.id/api/"
        if args is None:
            data = requests.get(API).json()
            covid_data = {}
            covid_data.update({"global_data":
                                   {"lastUpdate": data["lastUpdate"][0:10].replace('-', '/'),
                                    "confirmed": data['confirmed']['value'],
                                    "recovered": data['recovered']['value'],
                                    "deaths": data["deaths"]['value'],
                                    "source": data["source"],
                                    "countries": [country['name'] for country in requests.get(
                                        API + "countries").json()['countries']]}})
            return covid_data
        else:
            country = args["country"]
            country = country[0].upper() + country[1:]
            data = requests.get(API + "countries/" + country).json()
            covid_data = {}
            covid_data.update({country:
                                   {"recovered": data['recovered']['value'],
                                    "confirmed": data['confirmed']['value'],
                                    "deaths": data['deaths']['value']}})
            return covid_data
