from setuptools import setup

# The comman used to install the dependencies from a setup.py file: pip install .
setup(
    name='pyWiki',
    version='',
    packages=['wiki', 'wiki.loops'],
    url='https://github.com/pyPadaiyal/pyWiki',
    license='',
    author='Ranjan Mohan',
    author_email='',
    description='',
    install_requires=['matplotlib>=3.4.3', 'flask', 'PyJWT', 'tornado']
)
