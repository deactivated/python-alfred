from setuptools import setup, find_packages


setup(name='alfred',
      version="0.3",
      author="Mike Spindel",
      author_email="mike@spindel.is",
      license="MIT",
      keywords="alfred alfredapp script filter",
      url="http://github.com/deactivated/python-alfred",
      description='Utilities for Alfred script filters.',
      install_requires=['lxml'],
      packages=find_packages(),
      zip_safe=False,
      classifiers=[
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: MIT License",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Programming Language :: Python"])
