from setuptools import setup, find_packages




setup(
    name='Custom text chunker',
    version='0.1',
    description='A simple Python library for splitting a text using langchain RecursiveCharacterTextSplitter .',
    author='Rajesh Pollepalli',
    packages=find_packages(include=['text_chunker']),
    install_requires=["langchain"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)