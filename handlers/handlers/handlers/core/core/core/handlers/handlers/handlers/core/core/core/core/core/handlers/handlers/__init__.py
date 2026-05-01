from . import start, admin, play, playlist, callbacks

def load_handlers(app):
    start.register(app)
    admin.register(app)
    play.register(app)
    playlist.register(app)
    callbacks.register(app)
