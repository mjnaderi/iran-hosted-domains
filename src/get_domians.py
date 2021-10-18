from collections import Iterable

import requests

from lxml.html.soupparser import fromstring
import constants as consts


def g2b_ito_gov() -> Iterable[str]:
    resp = requests.post(consts.g2b_gov_url,
                         allow_redirects=True,
                         verify=False,
                         data="__RequestVerificationToken=duB0tkYUqhE6tkRpAl2Py5n7A8TgiG5gvw6aJOkccAmOdT72ONRHgmKxLbT0Pd_J2cQTRACu7OHJB1ofYqCkr4wwF3KoIC7EYUpLvaeIWvU1&ExportExcel=true",
                         headers={
                             'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                             'Cookie': '__RequestVerificationToken=28Ler0j0Udsc1-A5gpuq2ODdS9qbv7NHP1MaI40R7NvUC2fxIu5L6ynPRPl68jwZQhBb7ktjitJnoIh_Jr97cYse2MvVW7xh_55WSQflekU1; ASP.NET_SessionId=kjn05bvrle2ulrchfvx1tjpa'
                         })
    resp.raise_for_status()

    tree = fromstring(resp.text)
    return (row.text for row in tree.xpath('//td[1]'))


def adsl_tci() -> Iterable[str]:
    with open(consts.adsl_tci_file_path, "r") as file:
        return (line.strip() for line in file.readlines())


def ads() -> Iterable[str]:
    with open(consts.ad_domains_path, "r") as fp:
        return sorted(fp.read().splitlines())
