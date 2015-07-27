from setuptools import find_packages, setup

setup(
        name ='arxiver',
        version='0.0.3',
        description='unofficial API tool for arxiv.org scientific publications',
        author='Jonathan N. Lee',
        author_email='jonathan_lee@berkeley.edu',
        url='https://github.com/jon--lee/arxiver',
        license='MIT',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Development Status :: 3 - Alpha',
	    'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
    	    'Topic :: Software Development',
	    'Topic :: Scientific/Engineering',
	    'Programming Language :: Python',
	    'Programming Language :: Python :: 2.7',
            ],
        install_requires=['beautifulsoup4'],
        packages=find_packages()
)
