from views import blueprints
from container.view import container
blueprints["container"] = container


def add_view(app, *names):
    for name in names:
        blp = blueprints.get(name)
        if blp:
            app.register_blueprint(blp)
