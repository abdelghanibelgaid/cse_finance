from setuptools import setup

setup(
    name="cse_finance",
    version="0.0.1",
    author="cse_finance team",
    description="Download and Analyze Casablanca Stock Market Data.",
    url='https://github.com/abdelghanibelgaid/cse_fianance',
    license='Apache',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['pandas>=1.3.0', 'numpy>=1.20.0', 'requests>=2.26.0', 'cloudscraper>=1.2.60', 'bs4>=4.10.0'],
    keywords='Casablanca Stock Exchange, Financial Market, Kingdom of Morocco',
)
