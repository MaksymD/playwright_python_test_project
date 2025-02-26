from setuptools import setup, find_packages

setup(
    name='Playwright_Python_Project',
    version='0.1.0',
    description='This is a Playwright-based automation project for testing web applications',
    author='Maksym Dotsenko',
    author_email='maksym.dotsenko@eviden.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'allure-pytest==2.13.5',
        'allure-python-commons==2.13.5',
        'anyio==4.0.0',
        'async==0.6.2',
        'httpx==0.18.2',
        'playwright==1.39.0',
        'pytest==7.4.2',
        'pytest-asyncio==0.21.1',
        'pytest-metadata==3.1.1',
        'pytest-playwright==0.5.2',
        'pytest-base-url==2.1.0',
    ],
    python_requires='>=3.9.0',
    entry_points={
    'console_scripts': [
            'playwright=playwright.cli:main',
        ],
    },
    zip_safe=False,
)
