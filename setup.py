from setuptools import setup, find_packages

setup(name='setuptools_app',
      version='0.0.1',
      author="yourname",
      author_email="your@email.com",
      url="http://example.com",
      packages=find_packages(),
      package_data={'setuptools_app': ['contents/hello']},
      scripts=['bin/say_hello'],
      description=("an example app packaged with setuptools"),
      long_description=open('README.rst').read(),
      install_requires=['jinja2'],
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: MIT License",
          "Development Status :: 3 - Alpha"
      ]
      )
