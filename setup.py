from setuptools import setup, find_packages

setup(
        name="kerasGA",
        version="1.0",
        author = 'S. Carrazza, J. Cruz-Martinez, Roy Stegeman',
        author_email = 'juan.cruz@mi.infn.it, roy.stegeman@mi.infn.it',
        url='https://github.com/N3PDF/KerasGA',
        package_dir={'':'src'},
        packages=find_packages('src'),
        install_requires=[
            'numpy',
            'keras',
            ],
        python_requires='>=3.6'
        )
