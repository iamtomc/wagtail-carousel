import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''

install_requires = [
    'wagtail>=0.7'
    'wagtail-model-utils>0.0.1'
]

setup(
    name='wagtail-carousel',
    version=__import__('carousel').__version__,
    author='Gilson Filho',
    author_email='contato@gilsondev.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/gilsondev/wagtail-carousel',
    license='MIT',
    description=' '.join(__import__('carousel').__doc__.splitlines()).strip(),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=read_file('README.rst'),
    install_requires=install_requires,
    test_suite="runtests.runtests",
    zip_safe=False,
)
