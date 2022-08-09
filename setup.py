from setuptools import setup, find_packages

requirements = [
    "brainscore_language @ git+https://github.com/brain-score/language@7527cec",
    "transformers",
    "torch",
    "datasets",
    "jupyter",
    "matplotlib",
]

setup(
    name='bmm22language',
    author="Martin Schrimpf",
    author_email='msch@mit.edu',
    url='https://github.com/mschrimpf/bmm22_language',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
)
