from setuptools import setup, find_packages

setup(
    name='ShooterGame',
    version='1.0.0',
    description='ShooterGame written to learn Python. The main goal of the game is to collect points by shooting at targets',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/shrike03/ShooterGame.git',
    #packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12', 
        'Operating System :: OS Independent',       
    ],
    python_requires='>=3.12', 
    install_requires = [
        'pygame>=2.6.0'
    ],

)
