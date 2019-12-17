from setuptools import setup

setup(
    name='splitpdf',
    version='0.1',
    py_modules=['splitpdf'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        splitpdf=splitpdf:split_pdf
    ''',
)
