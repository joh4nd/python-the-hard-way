try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description': 'My Project',
    'author': 'Johan',
    'url': 'github.com/joh4nd',
    'download_url': 'Where to download it.',
    'author_email': 'My email',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
]

setup(**config)
