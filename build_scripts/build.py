from os import getcwd
from os.path import dirname, abspath
from sys import argv

import yaml
from boto3.session import Session

from structures import Config
from writers import write_services


def load(path: str, session_: Session) -> Config:
    with open(path, 'r') as f:
        file_contents = yaml.load(f)
    if file_contents.get('services') == 'all':
        file_contents['services'] = session_.get_available_services()
    if not all((service in session_.get_available_services() for service in file_contents.get('services'))):
        raise ValueError('Invalid service name.')
    return Config(
        file_contents.get('services', session_.get_available_services()),
        file_contents.get('with_docs', False),
        file_contents.get('with_clients', True),
        file_contents.get('with_service_resources', True),
        file_contents.get('with_paginators', True),
        file_contents.get('with_waiters', True),
        file_contents.get('package_name', 'boto3_type_annotations'),
        file_contents.get('module_name', 'boto3_type_annotations'),
        file_contents.get('version'),
        file_contents.get('readme', '../README.md'),
        file_contents.get('license', '../LICENSE')
    )


def build(session: Session, config: Config):
    write_services(session, config)


if __name__ == '__main__':
    print(dirname(abspath(__file__)))
    if len(argv) < 2:
        raise ValueError('Missing config path.')
    session = Session()
    build(session, load(argv[1], session))
