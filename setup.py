from setuptools import setup

setup(
    name='UltimateFitnessTracker',
    packages=['project'],
    include_package_data=True,
    install_requires=[
        'flask>=0.2',
        'SQLAlchemy>=0.8.0'
    ],
)