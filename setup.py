# setup.py

"""Setup script."""

from setuptools import setup

with open('requirements.txt', 'r', encoding='UTF-8') as f:
    required: list[str] = f.read().splitlines()

with open("README.md", 'r', encoding='UTF-8') as f:
    long_description: str = f.read()

setup(
    name='wolfsoftware.notify',
    version='0.1.2',
    author='Wolf Software',
    author_email='pypi@wolfsoftware.com',
    description='Generate console base notification messages.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=['wolfsoftware.notify'],
    tests_require=['pytest'],
    test_suite='tests',
    keywords=['python', 'notify'],
    url='https://github.com/DevelopersToolbox/notify-package',

    project_urls={
        ' Source': 'https://github.com/DevelopersToolbox/notify-package',
        ' Tracker': 'https://github.com/DevelopersToolbox/notify-package/issues/',
        ' Documentation': 'https://github.com/DevelopersToolbox/notify-package',
        ' Sponsor': 'https://github.com/sponsors/WolfSoftware',
    },

    classifiers=[
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        # 'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
    python_requires='>=3.9',
    install_requires=required,
)
