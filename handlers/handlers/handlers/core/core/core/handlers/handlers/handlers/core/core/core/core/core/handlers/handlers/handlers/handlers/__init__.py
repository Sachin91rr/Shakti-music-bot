from . import start, admin, play, playlist, callbacks, playlist_save

def load_handlers(app):
    start.register(app)
    admin.register(app)
    play.register(app)
    playlist.register(app)
    callbacks.register(app)
    playlist_save.register(app)
