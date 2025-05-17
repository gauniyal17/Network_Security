"Setup.py is the main file which will help us to packaging and distributing our project as a package containnig impt data such as metadata and requirements"




from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """This function will return list of requirements"""
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement = line.strip()
                # Improved check: ignore empty lines and anything starting with -e.
                if requirement and not requirement.startswith('-e '):
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt not found')
    
    return requirement_lst


setup(
    name="Network Security",
    version="0.0.1",
    author="Rahul Gauniyal",
    packages=find_packages(),
    install_requires=get_requirements()
    
)