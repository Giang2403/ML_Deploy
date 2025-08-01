from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    Returns a list of requirements
    """    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="ML_Deploy",
    version="0.0.1",
    author="Giang",
    author_email="tranbachgiangcm2002@gmail.com",
    install_requires=get_requirements('requirements.txt')
)
