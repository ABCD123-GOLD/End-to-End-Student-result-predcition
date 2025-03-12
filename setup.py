from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from a file.
    """
    requirements = []
    try:
        with open(file_path, "r") as file_obj:
            requirements = [req.strip() for req in file_obj.readlines() if req.strip()]
            
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    
    return requirements

setup(
    name="End-to-end student Performance system",
    version="0.0.1",
    author="Mathew Wuraola",
    author_email="arena663@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
