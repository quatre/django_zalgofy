from setuptools import setup, find_packages

setup(
    name='django_zalgofy',
    version='0.1',
    description='This middleware make your pages look like they were Zalgofied.',
    long_description=open('README.rst').read(),
    author='Guillaume Espanel',
    author_email='guillaume@lolnet.org',
    url='https://github.com/quatre/django_zalgofy',
    download_url='https://github.com/quatre/django_zalgofy',
    license='BSD',
    packages=find_packages(exclude=('tests', 'example')),
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
