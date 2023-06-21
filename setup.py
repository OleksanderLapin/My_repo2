from setuptools import setup, find_namespace_packages 

setup( 
    name ='clean_folder', 
    packages = find_namespace_packages(), 
    version ='0.0.1', 
    description ='A package for cleaning up directories', 
    
    author ='Alex', 
    author_email ='alex@example.com', 
    
    url ='https://github.com/johndoe/clean_folder', 
    license = 'MIT',
    keywords =['folders', 'cleanup'],   # Keywords that define your package best 
    classifiers=[], # Classifier list: https://pypi.python.org/pypi?%3Aaction=list_classifiers  

        # This will be the command that runs the script when used from the command line

    entry_points={ 'console_scripts': [ 'clean-folder=clean_folder.clean:'] }, )