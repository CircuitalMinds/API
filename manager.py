def add_register_db(db, book_name, **data_to_add):
    response = {}
    book = db.__dict__[book_name]
    check_data = book.query.filter(
        book.__dict__[book.secondary_repr] == data_to_add[book.secondary_repr]).first() is None
    if check_data:
        data_to_add[book.repr] = len(book.query.all()) + 1
        db.session.add(book(data=data_to_add))
        db.session.commit()
        response["Response"] = f"{data_to_add} added to {book_name}"
    else:
        response["Response"] = f"{data_to_add} already exists in {book_name}"
    return response


def delete_register_db(db, book_name, **with_repr):
    response = {}
    book = db.__dict__[book_name]
    argument_key, argument_value = '', ''
    for k, v in with_repr.items():
        argument_key, argument_value = k, v
    check_data = argument_key == book.repr or argument_key == book.secondary_repr
    if check_data:
        data_to_delete = book.query.filter(book.__dict__[argument_key] == argument_value).first()
        if data_to_delete is None:
            response["Response"] = f"data with {argument_key} = {argument_value} not found in {book_name}"
        else:
            db.session.delete(data_to_delete)
            db.session.commit()
            response["Response"] = f"data with {argument_key} = {argument_value} deleted from {book_name}"
    return response


def update_register_db(db, book_name, argument_update, with_repr):
    response = {}
    book = db.__dict__[book_name]
    repr_key, repr_value = '', ''
    for k, v in with_repr.items():
        repr_key, repr_value = k, v
    check_data = repr_key == book.repr or repr_key == book.secondary_repr
    if check_data:
        from_data = book.query.filter(book.__dict__[repr_key] == repr_value)
        data_update = from_data.first()
        if data_update is None:
            response["Response"] = f"data with {repr_key} = {repr_value} not found in {book_name}"
        else:
            data = {arg: data_update.__dict__[arg] for arg in book.args}
            for argument_key, argument_value in argument_update.items():
                data[argument_key] = argument_value
            from_data.update(data)
            db.session.commit()
            argument_label = ''.join([k + ' ' for k in argument_update.keys()])[:-1]
            response[
                "Response"] = f"[{argument_label}] to {repr_key} = {repr_value} was updated from {book_name}"
    return response


def get_register_db(db, book_name, with_argument=None):
    response = {}
    book = db.__dict__[book_name]
    if with_argument is None:
        data = {}
        for q in book.query.all():
            data[q.__dict__[book.repr]] = {arg: q.__dict__[arg] for arg in book.args}
        response["Response"] = data
    else:
        argument_key, argument_value = '', ''
        for k, v in with_argument.items():
            argument_key, argument_value = k, v
        check_data = argument_key == book.repr or argument_key == book.secondary_repr
        if check_data:
            data_to_get = book.query.filter(book.__dict__[argument_key] == argument_value).first()
            if data_to_get is None:
                response["Response"] = f"data with {argument_key} = {argument_value} not found in {book_name}"
            else:
                response["Response"] = {arg: data_to_get.__dict__[arg] for arg in book.args}
    return response
