from setuptools import find_packages, setup

setup(
    name='efficient-learning-lambda',
    version='1.4.0',
    license='',
    description='Python Lambda which fetches Questions for Quizzes and Evaluates Results.',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    author='BBC Education',
)
