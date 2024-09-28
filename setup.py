from setuptools import setup

setup(
    name='Image-Generator',
    version='1.0',
    description='A Langflow component that generates images from text using Stable Diffusion.',
    author='Rhogger',
    author_email='rhoggerrv@gmail.com',
    packages=['Generators'],
    install_requires=[
        'torch',
        'transformers',
        'diffusers',
        'Pillow',
        'langflow',
    ],
)
