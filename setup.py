from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    ''' this function will return the list of requirements '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace('\n',"") for req in requirements]
        
        # if HYPEN_E_DOT in requirements:
        #     requirements.remove(HYPEN_E_DOT)
        
    
setup(
    name = "ML Project",
    version='0.1',
    author="Aastha",
    author_email='aasthasinha1109@gmail.com',
    packages=find_packages(),
    include_package_data=False,
    install_requires = get_requirements('requirements.txt')
)