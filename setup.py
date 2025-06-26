'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older python versions) to define the 
configuration of your project ,such as its meta data,
dependencies,and moroe 
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # read lines
            lines = file.readlines()

            for line in lines:
                requirement=line.strip()

                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")  
    return requirement_lst

setup(
    name = "Network Security",
    version="0.0.1",
    author="Nikhileswar Reddy",
    author_email="nikhileswarreddy17@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)