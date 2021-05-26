from api_config import CircuitalMinds
from manager import *


circuitalminds = CircuitalMinds()
server = circuitalminds.get_server()
api_modules = server.modules
settings = server.settings
app = server.app

database = circuitalminds.models
for model in database.keys():
    database[model] = circuitalminds.get_model(app=app, name=model)

api = api_modules.Api(app)


class API(api_modules.Resource):

    def __init__(self):
        self.run = app.run
        self.request = api_modules.request
        self.options = {"add": lambda query: self.get_data_to_add(query=query),
                        "delete": lambda query: self.get_data_to_delete(query=query),
                        "update": lambda query: self.get_data_to_update(query=query),
                        "get": lambda query: self.get_data_by_query(query=query)
                        }
        self.select_option = lambda option, query: self.options[option](query=query)

    def get_request_function(self):
        if self.request.method == "POST":
            return lambda argument: self.request.form[argument]
        else:
            return lambda argument: self.request.args.get(argument)

    def get_data_to_add(self, query):
        data = {}
        request_function = self.get_request_function()
        arguments = database[query].args
        for argument in arguments:
            argument_data = request_function(argument)
            if argument_data is None:
                return {"Response": f"{argument_data} not found in request"}
            else:
                data[argument] = argument_data
        return add_register_db(db=database[query], book_name=query, **data)

    def get_data_to_delete(self, query):
        data = {}
        request_function = self.get_request_function()
        repr = database[query].repr
        secondary_repr = database[query].secondary_repr
        for to_repr in [repr, secondary_repr]:
            repr_data = request_function(to_repr)
            if repr_data is not None:
                data[to_repr] = repr_data
        if data == {}:
            return {"Response": f"data to {repr} or {secondary_repr} not found in request"}
        else:
            return delete_register_db(db=database[query], book_name=query, **data)

    def get_data_to_update(self, query):
        with_repr = {}
        argument_update = {}
        request_function = self.get_request_function()
        repr = database[query].repr
        secondary_repr = database[query].secondary_repr
        for to_repr in [repr, secondary_repr]:
            repr_data = request_function(to_repr)
            if repr_data is not None:
                with_repr[to_repr] = repr_data
                break
        if with_repr == {}:
            return {"Response": f"data to {repr} or {secondary_repr} not found in request"}
        for argument in database[query].args:
            if all([argument != repr, argument != secondary_repr]):
                argument_data = request_function(argument)
                if argument_data is not None:
                    argument_update[argument] = argument_data
        if argument_update == {}:
            return {"Response": f"data to update not found in request"}
        else:
            print(with_repr, argument_update)
            return update_register_db(db=database[query],
                                      book_name=query,
                                      argument_update=argument_update,
                                      with_repr=with_repr)

    def get_data_by_query(self, query):
        data = {}
        request_function = self.get_request_function()
        repr = database[query].repr
        secondary_repr = database[query].secondary_repr
        for to_repr in [repr, secondary_repr]:
            repr_data = request_function(to_repr)
            if repr_data is not None:
                data[repr_data] = repr_data
                break
        if data == {}:
            return get_register_db(db=database[query], book_name=query)
        else:
            return get_register_db(db=database[query], book_name=query, with_argument=data)

    def get(self, query, option):
        check_query, check_option = query in list(database.keys()), option in list(self.options.keys())
        if all([check_query, check_option]):
            return api_modules.jsonify(self.select_option(option=option, query=query))
        else:
            causes = []
            if check_query is False:
                causes.append(f" [register with {query} not found in database] ")
            if check_option is False:
                causes.append(f" [option {option} not found] ")
            return api_modules.jsonify({"Response": "".join(causes)})


APP = API()

api.add_resource(API, "/get/<query>/<option>")


if __name__ == '__main__':
    APP.run(**settings)
