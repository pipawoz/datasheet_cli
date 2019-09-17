from setuptools import setup

setup(
    name='datasheet',
    version='0.1',
    description='Simple datasheet search CLI',
    author='Pedro Wozniak',
    license='MIT',
    author_email='pwozniaklorice@est.frba.utn.edu.ar',
    py_modules=['datasheet'],
    install_requires=[
        'Click', 'bs4', 'requests'
    ],
    entry_points='''    
        [console_scripts]
        datasheet=datasheet:main
    ''',
)
