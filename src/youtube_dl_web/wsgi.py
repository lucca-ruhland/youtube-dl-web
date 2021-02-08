from youtube_dl_web import create_app
from youtube_dl_web.default_config import Docker

app = create_app(Docker)

if __name__ == '__main__':
    app.run()
