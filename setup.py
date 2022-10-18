from setuptools import setup
setup(name='enlaypy',
version='0.1',
description='Enlay.io python package',
url='https://github.com/Artucuno/enlaypy',
author='Artucuno',
author_email='artucunov@gmail.com',
license='MIT',
packages=['enlaypy'],
install_requires=['requests', 'httpx', 'asyncio'],
zip_safe=False)
