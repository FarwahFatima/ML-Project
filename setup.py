# is a module use to  build python packages
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''function will return the list of requirements'''
    requirements = []
    with open(file_path) as obj_file:
        requirements = obj_file.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = 'mainproject', 
    version = "1.2.0",
    author = 'FarwahFatima',
    author_email= 'farwahfatima7@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)