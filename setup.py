from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)-> List[str]:
    
    '''
    THis function returns a list of requirments
    '''
    get_requirements = []
    with open(file_path) as file_obj:
        requiremnts= file_obj.readlines()
        requiremnts=[req.replace("\n","")for req in requirements]
setup(
name = 'mlproject',
version= '0.0.1',
author = 'radhey',
author_email='rgawand008@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')

)