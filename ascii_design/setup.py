
from setuptools import setup

setup(
    name='ascii_design',
    version='1.0.0',
    description='Tool for create designs in asii code',
    author='蛇道',
    author_email='contact.d4niel9@gmail.com',
    url='https:/github.com/caminodelaserpiente/ascii_design',
    packages=['ascii_design']
    install_requires=['Pillow']
    classifiers=[
        'Development Status :: 3 - Alpha',
		'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Artistic Software',
        'Topic :: Text Processing :: Fonts'
    ]
)