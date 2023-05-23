from setuptools import setup

setup(
    name='clean_folder',
    author='Denis G.',
    maintainer_email='webmastak2016@gmail.com',
    version='1.0',
    packages=['clean_folder'],
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main'
        ]
    }
)
