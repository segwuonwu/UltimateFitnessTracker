from setuptools import setup

setup(
    name='project',
    packages=['project'],
    include_package_data=True,
    install_requires=[
        'flask>=0.2',
        'SQLAlchemy>=0.8.0'
    ],
)