import requests


class YouTubeApp:

    def __init__(self):
        self.data_search = {}
        self.url = "https://www.youtube.com"

    def handler_function(self, video_title, iterations=3, max_iterations=False):
        search = lambda Title: requests.utils.unquote(requests.get(f"{self.url}/results?search_query={Title}").text)
        watch = lambda videoId: requests.utils.unquote(requests.get(f"{self.url}/watch?v={videoId}").text)
        data = self.check_searches(video_title=video_title, data= self.data_search, checking=self.checking)
        if data == {}:
            if max_iterations:
                iterations = "max"
            data.update(self.get_data_by_id(video_title=video_title,
                                                search=search,
                                                watch=watch,
                                                get_meta_data=self.get_meta_data,
                                                iterations=iterations))
            for video in list(data.keys()):
                video_data = data[video]
                for prop in ["url", "title", "image"]:
                    try:
                        data[video][f"video_{prop}"] = video_data["property"][f"og:{prop}"]
                    except KeyError:
                        pass
            self.data_search.update({video_title: data})
        return data

    @staticmethod
    def checking(x, y, word_tokenize, stopwords):
        x_list, y_list = word_tokenize(x), word_tokenize(y)
        sw = stopwords.words('english')
        l1, l2 = [], []
        x_set = {w for w in x_list if w not in sw}
        y_set = {w for w in y_list if w not in sw}
        r_vector = x_set.union(y_set)
        c = 0
        for w in r_vector:
            if w in x_set:
                l1.append(1)
            else:
                l1.append(0)
            if w in y_set:
                l2.append(1)
            else:
                l2.append(0)
        n = sum(l1) * sum(l2)
        if n != 0:
            for i in range(len(r_vector)):
                c += l1[i] * l2[i]
            return c / (float(n) ** 0.5)
        else:
            return 0.0

    @staticmethod
    def check_searches(video_title, data, checking):
        stopwords, word_tokenize = [], []
        video_data = {}
        video = None
        if video_title in list(data.keys()):
            video = list(data.keys()).index(video_title)
        else:
            test = [v in video_title for v in list(data.keys())]
            if any(test):
                video = list(data.keys())[test.index(True)]
            else:
                for v in list(data.keys()):
                    if checking(
                            x=v, y=video_title,
                            stopwords=stopwords, word_tokenize=word_tokenize) * 100.0 > 80.0:
                        video = v
                        break
        if video is not None:
            video_data.update(data[video])
        return video_data

    @staticmethod
    def get_data_by_id(video_title, search, watch, get_meta_data, iterations):
        source = search(Title=video_title)
        data = {}
        if iterations == "max":
            iterations = source.count('videoId')
        for i in range(iterations):
            lower = source.find(f'"videoId"')
            upper = lower + len(f'"videoId":"') + 12
            string_data = source[lower:upper].split(':')
            if len(string_data) == 1:
                break
            videoId = string_data[1].replace('"', '')
            source = source[upper:]
            if videoId not in list(data.keys()):
                video_source = watch(videoId=videoId)
                print(video_source)
                meta_data = get_meta_data(video_source=video_source, videoId=videoId)
                data.update(meta_data)
        return data

    @staticmethod
    def get_meta_data(video_source, videoId):
        counter = video_source.count("meta")
        meta_data = {videoId: {"http-equiv": {}, "name": {}, "property": {}, "itemprop": {}}}
        for j in range(counter):
            lower = video_source.find("<meta")
            upper = lower + video_source[lower:].find(">") + 1
            string_meta = video_source[lower:upper]
            video_source = video_source[upper:]
            string_meta = string_meta.replace("<meta ", "").replace(">", "").split('" ')
            if len(string_meta) >= 2:
                attr_1, attr_2 = string_meta[0], string_meta[1]
                attr_1, attr_2 = attr_1.split('="'), attr_2.split('="')
                meta_data[videoId][attr_1[0]].update({attr_1[1].replace('"', ''): attr_2[1].replace('"', '')})
        return meta_data

    @staticmethod
    def search_list_template(search_list):
        _template = ""
        wrapper_template = lambda Id, title, url, image: f'''<li id={Id} class="cell">
        <p class="card-header w-100">{title}</p>
            <img class="card-content w-100" src="{image}">            
            <button class="card-content w-100 button primary text-center fg-teal fg-light-hover bg-light bg-teal-hover"
                    value={url} onClick="youtubeDownloader('{Id}');">Download Video</button>
        </li>'''
        get_template = [_template + wrapper_template(
            j, search_list[j]["video_title"],
            search_list[j]["video_url"],
            search_list[j]["video_image"])
                        for j in range(len(search_list))]
        for string in get_template:
            _template += string
        return _template