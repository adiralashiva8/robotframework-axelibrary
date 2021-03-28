import sys
from os.path import abspath, dirname, join

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


PY3 = sys.version_info > (3,)

VERSION = None
version_file = join(dirname(abspath(__file__)), 'src', 'AxeLibrary', 'version.py')
with open(version_file) as file:
    code = compile(file.read(), version_file, 'exec')
    exec(code)

DESCRIPTION = """
Robot Framework keyword library wrapper around the axe-selenium-python library.
"""[1:-1]

CLASSIFIERS = """
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]


setup(
      name='robotframework-axelibrary',
      version=VERSION,
      description='Robot Framework keyword library wrapper around axe-selenium-python library',
      long_description=DESCRIPTION,
      author='Shiva Adirala',
      author_email='adiralashiva8@gmail.com',
      url='https://github.com/adiralashiva8/robotframework-axelibrary',
      license='MIT',
      keywords='robotframework testing automation axe-selenium-python',
      platforms='any',
      classifiers=CLASSIFIERS.splitlines(),
      package_dir={'': 'src'},
      packages=['AxeLibrary'],
      install_requires=[
          'robotframework',
          'axe-selenium-python'
      ],)