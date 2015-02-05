from setuptools import setup

setup(
    name='pyMetrik',
    version='0.1.0',
    description='a Python library for metabolome dataset preprocessing',
    author='Kozo Nishida',
    author_email='knishida@riken.jp',
    url='http://github.com/kozo2/pyMetrik',
    keywords=['metabolome', 'bioinformatics'],
    classifiers=[
        'License :: OSI Approved :: Apache License',
        'Programming Language :: Python :: 2.7',
    ],
    py_modules=['pymetrik'],
    extras_requires=[
        'pandas',
    ],
)
