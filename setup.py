from setuptools import setup, find_packages

setup(
    name='yamnet',
    version='0.1.0',
    description='A Python package for sound classification using yamnet Tensorflow',
    url=' https://github.com/himanshu-iitg/yamnet.git',
    author='Himanshu Kaushik',
    author_email='himanshukaushik.iitg@gmail.com',
    license='Apache-2.0',
    packages=find_packages(),
    package_data={"":["*.csv", "*.h5"]}, # use package data for only specific files.
    install_requires=['scipy>=1.10.1',
                      'tensorflow==2.9.0',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)