from setuptools import setup

with open('README.md') as g:
    disc = g.read()

setup(
    name='letnum',
    version='0.0.1',
    packages='letnum',
    discription='a simple library to generate random combinations of letters and numbers',
    long_description=disc,
    long_description_content_type='text/markdown',
    author='Sokisa',
    url = 'https://github.com/sokisa/letnum',
    author_email=None,
    license='MIT',
    install_requires=[],
    classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries',
    ],
)