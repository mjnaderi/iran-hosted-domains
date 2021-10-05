from typing import Iterable
from functools import reduce

import xlrd

import constants as consts
import utils


def g2b_ito_gov() -> Iterable[str]:
    utils.download(consts.g2b_gov_url, consts.g2b_gov_file_path)

    workbook = xlrd.open_workbook(
        consts.g2b_gov_file_path,
        ignore_workbook_corruption=True
    )
    sheet = workbook.sheet_by_index(0)
    return (sheet.row_values(row)[0] for row in range(sheet.nrows))


def adsl_tci() -> Iterable[str]:
    utils.download(consts.adsl_tci_url, consts.adsl_tci_file_path)

    with open(consts.adsl_tci_file_path, "r") as fp:
        # Skip first 2 lines!
        return (line.strip() for line in fp.readlines()[2:])


def collect_and_clean_domains(*domain_set: Iterable[Iterable[str]]) -> Iterable[str]:
    domains = reduce(lambda x, y: set(x).union(set(y)), domain_set)
    domains = (domain.lower() for domain in domains)
    domains = map(utils.extract_domain, domains)
    domains = filter(utils.is_url, domains)
    domains = filter(utils.is_not_ip, domains)
    domains = map(utils.convert_utf8, domains)
    return sorted(domains)


if __name__ == "__main__":
    import os

    import create_config
    from data.custom_domains import custom_domains

    if not os.path.exists("download"):
        os.mkdir("download")
    if not os.path.exists("output"):
        os.mkdir("output")

    # load other domains list
    proxy_domains = sorted(custom_domains["proxy"])

    with open(consts.ad_domains_path, "r") as fp:
        ad_domains = sorted(fp.read().splitlines())

    # Request data from sources and cleanup
    all_domains = collect_and_clean_domains(
        g2b_ito_gov(),
        adsl_tci(),
        custom_domains["direct"]
    )

    # Divide info
    ir_domains = sorted(filter(utils.is_ir, all_domains))
    other_domains = sorted(set(all_domains).difference(ir_domains))

    # Generate output files
    utils.save_to_file(consts.ir_domains_path, "\n".join(ir_domains))
    utils.save_to_file(consts.other_domains_path, "\n".join(other_domains))
    utils.save_to_file(consts.all_domains_path, "\n".join(all_domains))

    create_config.qv2ray(other_domains, proxy_domains, ad_domains)
    create_config.shadowrocket(all_domains)
    create_config.clash(all_domains)
    create_config.switchy_omega(other_domains)
