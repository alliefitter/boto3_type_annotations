from boto3.session import Session

from build_scripts.writers import write_services


def build(session: Session):
    write_services(session, False, 'boto3_type_annotations')


def build_with_docs(session: Session):
    write_services(session, True, 'boto3_type_annotations_with_docs')


if __name__ == '__main__':
    build(Session())
    build_with_docs(Session())
