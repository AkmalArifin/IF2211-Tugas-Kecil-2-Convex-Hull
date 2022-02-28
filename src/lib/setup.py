from setuptools import find_packages, setup

setup(
    name='myConvexHull',
    packages=find_packages(include=['myConvexHull']),
    version='0.1.0',
    description='My Convex Hull library',
    author='Muhammad Akmal Arifin',
    license='ITB',
    install_requires=['numpy']
)