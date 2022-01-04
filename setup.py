from setuptools import setup

# The command used to install the dependencies from a setup.py file: "pip install ."
setup(
    name='pyWiki',
    version='2022.01.03',
    packages=['wiki', 'wiki.loops'],
    url='https://github.com/pyPadaiyal/pyWiki',
    license='',
    author='Ranjan Mohan',
    author_email='',
    description='',
    install_requires=['matplotlib>=3.4.3', 'flask', 'PyJWT', 'tornado']
)
