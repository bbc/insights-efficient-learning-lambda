from setuptools import find_packages, setup

setup(
    name='insights-efficient-learning-lambda',
    version='1.7.7',
    license='',
    description='Python Lambda which fetches Questions for Quizzes and Evaluates Results.',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    author='BBC Education',
)
