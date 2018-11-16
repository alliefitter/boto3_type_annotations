from setuptools import setup, find_packages

with open('../README.md', 'r') as f:
    long_description = f.read()

setup(
    name='boto3_type_annotations_with_docs',
    version='0.2.4',
    packages=find_packages(),
    url='https://github.com/alliefitter/boto3_type_annotations',
    license='MIT License',
    author='Allie Fitter',
    author_email='fitterj@gmail.com',
    description='Type annotations for boto3. Adds code completion in IDEs such as PyCharm. Includes boto3 docstrings.',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
)
