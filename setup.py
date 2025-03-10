from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

setup(name='evalidate',
      version='1.0.2',
      url='http://github.com/yaroslaff/evalidate',
      author='Yaroslav Polyakov',
      author_email='xenon@sysattack.com',
      license='MIT',
      packages=['evalidate'],
      description = 'Validation and secure evaluation of untrusted python expressions',
      long_description = read('README.md'),
      long_description_content_type='text/markdown',
      zip_safe=False)

