from flask import request


def response_handler(reason, book_name):
    name = book_name[:-1]
    return {
        "response": {
            "not_found": f"{name} data not found",
            "already_exists": f"{name} data already exists",
            "data_added": f"{name} data added successfully",
            "data_updated": f"{name} data updated successfully",
            "data_deleted": f"{name} data deleted successfully"
        }[reason]
    }


def request_handler():
    if request.method == "POST":
        return request.form.to_dict()
    else:
        query_string = list(filter(
            lambda i: len(i) == 2, [
                s.split("=") for s in request.query_string.decode("utf-8").split("&")
            ]
        ))
        return {
            x[0]: x[1] for x in query_string
        }


def query_all(book):
    return list(map(
        lambda x: {
            arg: x.__dict__[arg] for arg in book.args["all"] + [book.repr]
        }, book.query.all()
    ))


def query_filter(book, data, *ignore):
    return list(filter(
        lambda x: all([
            True if arg in list(ignore) else x[arg] == data[arg] for arg in data
        ]), query_all(book)
    ))


def get_data(db, name):
    book = db.__dict__[name]
    request_data = request_handler()
    data = book.set_data(request_data, "get")
    if data:
        book_data = query_filter(book, data)
        if book_data:
            return {"response": book_data}
        else:
            return response_handler("not_found", name)
    else:
        return response_handler("not_found", name)


def add_data(db, name):
    book = db.__dict__[name]
    request_data = request_handler()
    data = book.set_data(request_data, "add")
    if data:
        query_data = []
        for k, v in data.items():
            query_data.extend(query_filter(book, {k: v}))
        if query_data:
            return response_handler("already_exists", name)
        else:
            db.session.add(book(data=data))
            db.session.commit()
            return response_handler("data_added", name)
    else:
        return response_handler("not_found", name)


def update_data(db, name):
    book = db.__dict__[name]
    request_data = request_handler()
    data = book.set_data(request_data, "update")
    if data:
        ignores = list(filter(lambda i: i.startswith("new_"), data))
        query_data = query_filter(book, data, *ignores)
        if query_data:
            for x in ignores:
                y = x.split("new_")[-1]
                data[y] = data[x]
                data.pop(x)
            db.session.query(book).filter(
                book.id == query_data[0]["id"]
            ).update(data)
            db.session.commit()
            return response_handler("data_updated", name)
        else:
            return response_handler("not_found", name)
    else:
        return response_handler("not_found", name)


def delete_data(db, name):
    book = db.__dict__[name]
    request_data = request_handler()
    data = book.set_data(request_data, "delete")
    if data:
        query_data = query_filter(book, data)
        if query_data:
            db.session.query(book).filter(
                book.id == query_data[0]["id"]
            ).delete()
            db.session.commit()
            return response_handler("data_deleted", name)
        else:
            return response_handler("not_found", name)
    else:
        return response_handler("not_found", name)
