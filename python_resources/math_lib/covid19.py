def covid19(country=None):
    get_request = __import__("requests").get
    api = "https://covid19.mathdro.id/api"
    if country is None:
        data = get_request(api).json()
        covid_data = {}
        covid_data.update({
            "global_data": {
                "lastUpdate": data["lastUpdate"][0:10].replace('-', '/'),
                "confirmed": data['confirmed']['value'],
                "recovered": data['recovered']['value'],
                "deaths": data["deaths"]['value'],
                "source": data["source"],
                "countries": [
                    country['name'] for country in get_request(f"{api}/countries").json()['countries']
                ]
            }
        })
        return covid_data
    else:
        country = country[0].upper() + country[1:]
        data = get_request(f"{api}/countries/{country}").json()
        return {
            "recovered": data['recovered']['value'],
            "confirmed": data['confirmed']['value'],
            "deaths": data['deaths']['value']
        }
