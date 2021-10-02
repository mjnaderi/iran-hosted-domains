import json
import os
from functools import reduce

import requests
import xlrd

from constants import *
from data.custom_domains import *
from utils import *


def download(url: str, path: str):
    if not os.path.exists(path):
        r = requests.get(url, allow_redirects=True, verify=False)
        with open(path, "wb") as file:
            file.write(r.content)
            file.close()


def g2b_ito_gov() -> set:
    download(g2b_gov_url, g2b_gov_file_path)

    workbook = xlrd.open_workbook(g2b_gov_file_path, ignore_workbook_corruption=True)
    sheet = workbook.sheet_by_index(0)

    data = (sheet.row_values(row)[0] for row in range(sheet.nrows))
    return set(map(lambda x: cleanup(x), data))


def adsl_tci() -> set:
    download(adsl_tci_url, adsl_tci_file_path)

    # Skip first 2 lines!
    with open(adsl_tci_file_path, "r") as file:
        next(file)
        next(file)
        lines = file.readlines()

    return set(map(lambda x: cleanup(x.strip()), lines))


def save_to_file(path, content):
    with open(path, "w") as file:
        file.write(content)


def create_shadowrocket_config(domains: list):
    config = "#Shadowrocket\n" \
             "[General]\n" \
             "bypass-system = true\n" \
             "skip-proxy = 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, localhost, *.local, captive.apple.com\n" \
             "tun-excluded-routes = 10.0.0.0/8, 100.64.0.0/10, 127.0.0.0/8, 169.254.0.0/16, 172.16.0.0/12, 192.0.0.0/24, 192.0.2.0/24, 192.88.99.0/24, 192.168.0.0/16, 198.18.0.0/15, 198.51.100.0/24, 203.0.113.0/24, 224.0.0.0/4, 255.255.255.255/32\n" \
             "dns-server = system\n" \
             "ipv6 = true\n" \
             "[Rule]\n"

    for address in domains:
        config += ("DOMAIN-SUFFIX," + address + ",DIRECT\n")

    config += "USER-AGENT,Line*,PROXY\n" \
              "IP-CIDR,192.168.0.0/16,DIRECT\n" \
              "IP-CIDR,10.0.0.0/8,DIRECT\n" \
              "IP-CIDR,172.16.0.0/12,DIRECT\n" \
              "IP-CIDR,127.0.0.0/8,DIRECT\n" \
              "GEOIP,IR,DIRECT\n" \
              "FINAL,PROXY\n" \
              "[Host]\n" \
              "localhost = 127.0.0.1"
    save_to_file(shadowrocket_path, config)


def create_qv2ray_schema(directs: list, proxies: list):
    schema = {
        "description": "Iran hosted domains",
        "domainStrategy": "AsIs",
        "domains": {
            "direct": ["regexp:^.+\\.ir$"] + directs,
            "proxy": proxies,
            "block": ["geosite:category-ads-all"]
        },
        "ips": {
            "direct": ["geoip:ir"]
        },
        "name": "ir_hosted"
    }
    save_to_file(qv2ray_schema_path, json.dumps(schema))


def create_clash_config(domains: list):
    config = "# Clash\n" \
             "# Wiki: https://github.com/Dreamacro/clash/wiki/premium-core-features#rule-providers\n" \
             "payload:\n"

    for address in domains:
        config += ("  - DOMAIN-SUFFIX," + address + "\n")

    config += "  - IP-CIDR,192.168.0.0/16\n" \
              "  - IP-CIDR,10.0.0.0/8\n" \
              "  - IP-CIDR,172.16.0.0/12\n" \
              "  - IP-CIDR,127.0.0.0/8\n" \
              "  - GEOIP,IR"
    save_to_file(clash_path, config)


def create_switchy_omega_config(others: list):
    config = "127.0.0.1\n" \
             "::1\n" \
             "localhost\n" \
             "*.ir\n"

    for address in others:
        config += ("*" + address + "\n")

    save_to_file(switchy_omega_path, config)


if __name__ == "__main__":
    if not os.path.exists("download"):
        os.mkdir("download")
    if not os.path.exists("output"):
        os.mkdir("output")

    # Proxy domains
    proxy_domains = sorted(set(custom_domains["proxy"]))

    # Request data from sources and cleanup
    sets = [g2b_ito_gov(), adsl_tci(), set(custom_domains["direct"])]

    # Filter extras
    full_domains = reduce(lambda x, y: x.union(y), sets)
    full_domains = filter(lambda x: is_url(x), full_domains)
    full_domains = filter(lambda x: not is_ip(x), full_domains)
    full_domains = map(lambda x: convert_utf8(x), full_domains)
    full_domains = set(sorted(full_domains))

    # Divide info
    ir_domains = list(filter(lambda x: is_ir(x), full_domains))
    other_domains = list(full_domains.difference(ir_domains))

    # Sort
    ir_domains = sorted(ir_domains)
    other_domains = sorted(other_domains)
    full_domains = sorted(full_domains)

    # Generate output files
    save_to_file(domains_path, "\n".join(full_domains))
    create_qv2ray_schema(other_domains, proxy_domains)
    create_shadowrocket_config(full_domains)
    create_clash_config(full_domains)
    create_switchy_omega_config(other_domains)
