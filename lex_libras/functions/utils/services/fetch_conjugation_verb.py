import os
import requests as req
from bs4 import BeautifulSoup as bs


def fetchConjugation(data):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0; App:lex-libras) Gecko/20100101 Firefox/106.0"
    }

    # url = "https://www.dicionarioinformal.com.br/flexoes/falares/"
    URL = "https://www.dicionarioinformal.com.br/flexoes/"
    # div[class='col-xs-12'] > h1 > a

    if type(data) == 'str':
        # if os.environ['LEXLIBRAS_VERBOSE'] == "1":
        page = req.get(
            URL+data,
            HEADERS
        )

        body = bs(page.content, 'html.parser')

        palavra = body.select("cssQuery:string")

        return None
    else:
        raise Exception(f"Param's receive not string not implemented yet")


def fetchInfinitiveForm(data):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
    }

    # url = "https://www.dicionarioinformal.com.br/flexoes/falares/"
    URL = "https://www.dicionarioinformal.com.br/flexoes/"
    # div[class='col-xs-12'] > h1 > a

    if isinstance(data, str):
        if os.environ['LEXLIBRAS_VERBOSE'] == "1":
            print(f"Palavra em consulta: {data}")

        page = req.get(
            URL+data,
            HEADERS
        )

        body = bs(page.content, 'html.parser')

        palavra = body.select("div[class='col-xs-12'] > h1 > a")

        return palavra[0].contents[0].upper()

    else:
        raise Exception(f"Param's receive not string not implemented yet")
