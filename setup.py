from setuptools import find_packages, setup

setup(
    name='irca_flask_serv',
    version='1.0.6',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
