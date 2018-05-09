from setuptools import setup

setup (
    name = 'tttAudioSplicer',
    version = '1.0',
    author = 'Drew Alexander',
    url = 'https://github.com/DrewAlexander98/TtT-Transcript-Splicer.git',
    py_modules= ['tttAudioSplicer']
    install_requires=[
        'pydub',
        'glob'
    )
