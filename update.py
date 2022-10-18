import sys, os
import shutil

e = input('1. Remove files\n2. Build package\n\n>>> ')
if str(e) == '1':
    deldirs = ['__pycache__', 'enlaypy.egg-info', 'build', 'dist']
    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            if name in deldirs:
                shutil.rmtree(os.path.join(root, name))
    os.system('pipreqs enlaypy')

elif str(e) == '2':
    os.system('python setup.py sdist')
    os.system('python setup.py bdist_wheel')
