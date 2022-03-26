from config import create_app, create_db, add_routes, Cfg
app = create_app()
db = create_db(app)
add_routes(app, db)


def run():
    app.run(**Cfg.get("server"))
