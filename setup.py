from setuptools import setup, find_packages

setup(
    name='your_python_app',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'Flask==3.0.0'
    ],
    entry_points={
        'console_scripts': [
            'app=app:run'
        ]
    }
)
