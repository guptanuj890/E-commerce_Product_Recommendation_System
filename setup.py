from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name = "Flipkart Recommender",
    version = "0.1",
    author = "Anuj Gupta",
    packages = find_packages(),
    install_requires = requirements,
)