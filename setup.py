from setuptools import setup, setuptools

setup(
    name='dump',
    version='1.0',    
    description='Dump Library',
    url='https://github.com/schnipdip/dump-library.git',
    author='Christopher Herzog',
    author_email='cjh30@pct.edu',
    license='MIT',
    python_requires='>=3.6',
    packages=setuptools.find_packages(),
    install_requires=['configparser',
                      'subprocess',
                      'logger',
                      'pyudev',
                      'usb',
                      'sys',
                      'os',
                      're'                     
                      ],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 1 - Planning',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
    ],
)