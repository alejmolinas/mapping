from setuptools import find_packages, setup
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('mapping/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name='mapping',
    packages=find_packages(),
    version=main_ns["version"],
    description='TODO',
    author='Alejandro Molinas',
    license='',
    python_requires='>=2.7',
    install_requires=['lxml'],
    entry_points = {
        'console_scripts': [
            'fmap = mapping.script:main',
        ]
    },
    include_package_data=True,
    package_data={'': ['files/*.svg']},

)
