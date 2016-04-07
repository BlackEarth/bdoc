
import codecs, json, os
from setuptools import setup, find_packages

path = os.path.dirname(__file__)
longdesc = codecs.open(path.join(path, 'longdesc.rst'), 'r', 'utf-8').read()

with codecs.open(os.path.join(path, 'config.json'), encoding='utf-8') as f:
    config = json.loads(f.read())

setup(
    long_description=longdesc,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    **config
)

