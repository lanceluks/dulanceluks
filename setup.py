from setuptools import setup, find_packages

setup(
    name='dulanceluks',  # Nome do pacote
    version='0.1',  # Versão inicial
    description='Uma biblioteca para calcular dias úteis com base em dias não úteis.',
    author='Lucas',
    author_email='lanceluks@gmail.com',
    url='https://github.com/lanceluks/dulanceluks',
    packages=find_packages(),
    include_package_data=True,  
    package_data={
        'dulanceluks': ['DNU.txt'],  
    },
    install_requires=[
        'pandas',  # Dependências
    ],
)
