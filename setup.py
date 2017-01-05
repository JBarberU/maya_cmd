from setuptools import setup

setup(name='maya_cmd',
      version='1.0',
      description='A small tool for sending python code to the Maya Editor',
      author='John Barbero Unenge',
      author_email='john@jbarber.se',
      url='https://github.com/JBarberU/maya_cmd',
      py_modules=['maya_cmd'],
      entry_points={
          'console_scripts': [
              'maya_cmd=maya_cmd:main'
          ]
      })

