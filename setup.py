
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup


config = {
'description': 'Python Tools for doing Machine Learning Homework',
'author': 'Grant DeLozier, Alex Rosenfeld',
'url': 'https://github.com/grantdelozier/ml-class',
'download_url': 'https://bitbucket.org/mev/medix-nlp',
'version': '0.1',
'install_requires': ['numpy'],
'packages': ['hw1'],
#'package_data': {
#        'hw1': ['ex1/*.txt'],
#    },
#'scripts': ['bin/label-predict'],
'name': 'mlclass'
}
setup(**config)