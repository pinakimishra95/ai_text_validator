from setuptools import setup

setup(
    name='ai_text_validator',
    version='0.2.2',
    description='A Python package for validating AI generated text.',
    author='Pinaki Mishra',
    author_email='pinakimishra95@gmail.com',
    license='Apache License 2.0',
    url='https://github.com/pinakimishra95/ai_text_validator',
    packages=['ai_text_validator'],
    install_requires=['transformers~=4.3'],
)