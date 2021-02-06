import argparse


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser('Youtube-DL-web application',
                                     usage='youtube-dl-web [-h] [-p PORT] [--host IP_ADDR]')
    parser.add_argument('-p', '--port', type=int, default=5000, help='set port for web app')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='set host address for web app')
    env = parser.add_mutually_exclusive_group()
    env.add_argument('--environment', type=str, choices=['debug', 'production'], help='select production or debug mode',
                     default='production')

    return parser


def get_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
    args = parser.parse_args()
    return args
