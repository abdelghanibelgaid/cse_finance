## Import Libraries
import sys
import pandas as _pd
import numpy as _np
import datetime as _datetime
import time as _time
import json as _json
import requests as _requests
import cloudscraper as _cloudscraper
from bs4 import BeautifulSoup as _BeautifulSoup

import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
scraper = _cloudscraper.create_scraper()


## Set URLs
# URL for CSE Company's Key Financial Information (from CSE)
_BASE_URL_COMPANY_INFO_ = 'https://www.casablanca-bourse.com/bourseweb/Societe-Cote.aspx?codeValeur='

# URL for CSE Stock Data (from leboursier.ma)
_BASE_URL_STOCKS_LEBOURSIER_ = 'https://www.leboursier.ma/api?method=getPriceHistory&ISIN='

# URL for CSE MASI Index (from leboursier.ma)
_BASE_URL_MASI_LEBOURSIER_ = "https://www.leboursier.ma/api?method=getMasiHistory&periode="

# URL for CSE MADEX Index (from leboursier.ma)
_BASE_URL_MADEX_LEBOURSIER_ = 'https://www.leboursier.ma/api?method=getMadexHistory&periode='
