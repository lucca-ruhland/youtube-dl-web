from youtube_dl_web import create_app
from youtube_dl_web.default_config import Production, Debug
from youtube_dl_web.parser import create_parser, get_args


def main():
    parser = create_parser()
    args = get_args(parser)

    if args.environment == 'production':
        config = Production()
    elif args.environment == 'debug':
        config = Debug()
    else:
        config = None

    app = create_app(config)
    app.run(host=args.host, port=args.port)
