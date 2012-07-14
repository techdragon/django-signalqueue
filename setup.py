#/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from distributors.dist import SQDistribution
from distributors.clean import really_clean
from distributors.coffeescript import build_coffeescript, download_js_libs

__author__ = 'Alexander Bohn'
__version__ = (0, 3, 9)

import os

def get_coffeescript_files():
    out = []
    pattern = '.coffee'
    for root, dirs, files in os.walk(os.path.join(
        'signalqueue', 'static', 'signalqueue', 'coffee')):
        for file in files:
            if file.endswith(pattern):
                out.append(os.path.join(root, file))
    return out

setup(
    name='django-signalqueue',
    version='%s.%s.%s' % __version__,
    description='Truly asynchronous signal dispatch for Django!',
    author=__author__,
    author_email='fish2000@gmail.com',
    maintainer=__author__,
    maintainer_email='fish2000@gmail.com',
    
    license='BSD',
    url='http://github.com/fish2000/django-signalqueue/',
    keywords=['django','signals','async','asynchronous','queue'],
    
    cs_files=get_coffeescript_files(),
    js_libs=[
        'https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.js',
        'http://cdn.socket.io/stable/socket.io.js'],
    
    distclass=SQDistribution,
    cmdclass={
        'clean': really_clean,
        'build_coffeescript': build_coffeescript,
        'download_js_libs': download_js_libs },
    
    include_package_data=True,
    package_data={
        'signalqueue': [
            'fixtures/*.json',
            'settings/*.conf',
            'static/signalqueue/js/*.js',
            'static/signalqueue/coffee/*.coffee',
            'static/socket.io-client/*',
            'templates/*.html',
            'templates/admin/*.html']},
    packages=[
        'distributors',
        'distributors.urlobject',
        'signalqueue',
        'signalqueue.management',
        'signalqueue.management.commands',
        'signalqueue.settings',
        'signalqueue.templatetags',
        'signalqueue.worker'],
    
    install_requires=[
        'django-delegate>=0.2.2',
        'tornado', 'tornadio2',
        'redis', 'requests'],
    
    tests_require=[
        'nose', 'rednose', 'django-nose'],
    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'])

