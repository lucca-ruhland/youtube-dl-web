from youtube_dl_web import create_app
from youtube_dl_web.default_config import Production

app = create_app(Production)

if __name__ == '__main__':
    app.run()
