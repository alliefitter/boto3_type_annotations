import boto3
from docutils.core import publish_string
from html2text import html2text

from boto3_type_annotations import sqs, s3

def foo():
    """**foo**
- *bar*
"""


resource: s3.Client = boto3.resource('sqs')
resource.create_bucket()
