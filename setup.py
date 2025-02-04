from setuptools import setup, find_packages

setup(
    name="app_python",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Flask==2.3.2",
        "pytz==2023.3",
        "pytest==7.4.0",
    ],
)