import yaml
import json
from os.path import isfile
parsers = dict(
    json=dict(
        parser=json.dumps, loader=json.load,
        config=dict(indent=4, sort_keys=True, ensure_ascii=False)
    ),
    yml=dict(
        parser=yaml.dump, loader=yaml.full_load,
        config=dict(allow_unicode=False, indent=4, default_flow_style=False)
    )
)


class Obj:
    data = {}
    loader, parser, config = None, None, None

    def __init__(self, path):
        self.path = path
        self.set_dumper()
        self.load()

    def set_dumper(self):
        dumper = {}
        if self.path.endswith(".json"):
            dumper = parsers["json"]
        elif self.path.endswith(".yml"):
            dumper = parsers["yml"]
        self.__dict__.update(dumper)

    def load(self):
        if isfile(self.path):
            self.data = self.loader(open(self.path))
        return self.data

    def save(self):
        with open(self.path, "w") as f:
            f.write(self.parser(self.data, **self.config))
            f.close()
        return

    def get(self, key, *keys):
        if keys:
            value = None
            values = self.data.copy()
            for k in [key] + list(keys):
                if k in values and type(values) == dict:
                    value = values[k]
                    values = value
                else:
                    value = None
                    break
            return value
        else:
            return self.data.get(key)

    @property
    def keys(self):
        return list(self.data.keys())

    @property
    def values(self):
        return list(self.data.values())

    @property
    def items(self):
        return list(self.data.items())
