from setuptools import setup, find_packages

setup(
    name='django_zalgofy',
    version='0.1',
    description='This middleware make your pages look like they were Zalgofied.',
    long_description=open('README.rst').read(),
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Guillaume Espanel',
    author_email='guillaume@lolnet.org',
    url='https://github.com/quatre/django_zalgofy',
    download_url='https://github.com/quatre/django_zalgofy/downloads',
    license='BSD',
    packages=find_packages(exclude=('tests', 'example')),
#    tests_require=[
#        'django>=1.3,<1.5',
#    ],
#    test_suite='runtests.runtests',
    include_package_data=True,
    zip_safe=True,  # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
