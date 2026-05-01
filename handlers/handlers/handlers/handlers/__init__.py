from . import start, admin, play

def load_handlers(app):
    start.register(app)
    admin.register(app)
    play.register(app)
