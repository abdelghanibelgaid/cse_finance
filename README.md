# cse_finance
Download and Analyze Casablanca Stock Exchange Data.

## Description
`cse_finance` is a Python library for downloading and analyzing Casablanca Stock Exchange data. It aims to improve financial information accessibility for research and educational purposes. The library currently has five main functions:
- `get_price`: returns historical stock price given a period.
- `get_index`: returns MASI, MADEX and MSI20 values given a period.
- `get_info`: returns financial information regarding a company quoted at the CSE.
- `all_command`: returns list of `cse_finance` available commands.
- `get_tickers`: returns list of tickers available on cse_finance.

## Quick Start

```
!pip install cse_finance
import cse_finance as cf

# Get Index values
masi = cf.get_index(index_symbol=['MASI'], start = '2021-01-01', end = '2022-01-01')

# Get financial Info on a company. Default from 2018 to 2020.
get_info('BCP', year='2020')

# Get price of a stock or group of stock.
data = cf.get_price(['CIH', 'BCP'], start = '2021-01-01', end = '2022-01-01')

# Compute a ratio for a stock
data['CIH_ratio'] = cf.stats.ewma(data['Close']])
```

## Notebook
Check out our Jupyter Notebook with examples of how to use `cse_finance`. **_Section in Progress_**

## Installation

Install `cse_finance` using `pip`:

```
$ pip install cse_finance --upgrade --no-cache-dir
```

### Requirements

-   [Python](https://www.python.org) \>= 3.5+
-   [Pandas](https://github.com/pydata/pandas) \>=1.3.5
-   [Numpy](http://www.numpy.org) \>= 1.20.3
-   [Requests](http://docs.python-requests.org/en/master/) \>= 2.26.0
-   [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) \>= 4.10.0
-   [Cloudscraper](https://github.com/venomous/cloudscraper) \>= 1.2.58


**Note:** `cse_finance` is not affiliated with, endorsed, or vetted by our API providers. It is an open-source tool that uses publicly available APIs and is intended for research and educational purposes.


About the cse_finance team
The cse_finance team is committed to providing accessible financial information to researchers and educators.



## Contributing
Github issues and pull requests are welcome. Your feedback is much appreciated!

`cse_finance` team
