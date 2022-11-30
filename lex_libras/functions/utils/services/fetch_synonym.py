import os
import requests as req
from bs4 import BeautifulSoup as bs


def fetchSynonym(word):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0; App:lex-libras) Gecko/20100101 Firefox/106.0"
    }

    URL = ""
