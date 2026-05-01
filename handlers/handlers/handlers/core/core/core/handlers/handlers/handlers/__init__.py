from . import start, admin, play, playlist

def load_handlers(app):
    start.register(app)
    admin.register(app)
    play.register(app)
    playlist.register(app)
