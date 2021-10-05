from typing import Iterable

import xlrd

import constants as consts
import create_config
import utils
from data.custom_domains import custom_domains


def g2b_ito_gov() -> Iterable[str]:
    utils.download(consts.g2b_gov_url, consts.g2b_gov_file_path)

    workbook = xlrd.open_workbook(
        consts.g2b_gov_file_path, ignore_workbook_corruption=True
    )
    sheet = workbook.sheet_by_index(0)

    data = (sheet.row_values(row)[0] for row in range(sheet.nrows))
    return map(utils.cleanup, data)


def adsl_tci() -> Iterable[str]:
    utils.download(consts.adsl_tci_url, consts.adsl_tci_file_path)

    with open(consts.adsl_tci_file_path, "r") as fp:
        # Skip first 2 lines!
        lines = fp.readlines()[2:]

    return (x.strip() for x in map(utils.cleanup, lines))


if __name__ == "__main__":
    import os
    from functools import reduce

    if not os.path.exists("download"):
        os.mkdir("download")
    if not os.path.exists("output"):
        os.mkdir("output")

    # load other domains list
    proxy_domains = sorted(custom_domains["proxy"])

    with open(consts.ad_domains_path, "r") as fp:
        ad_domains = sorted(fp.read().splitlines())

    # Request data from sources and cleanup
    sets = g2b_ito_gov(), adsl_tci(), custom_domains["direct"]

    # Filter extras
    full_domains = reduce(lambda x, y: set(x).union(set(y)), sets)
    full_domains = filter(utils.is_url, full_domains)
    full_domains = filter(utils.is_ip, full_domains)
    full_domains = map(utils.convert_utf8, full_domains)
    full_domains = sorted(full_domains)

    # Divide info
    ir_domains = sorted(filter(utils.is_ir, full_domains))
    other_domains = sorted(set(full_domains).difference(ir_domains))

    # Generate output files
    utils.save_to_file(consts.ir_domains_path, "\n".join(ir_domains))
    utils.save_to_file(consts.other_domains_path, "\n".join(other_domains))
    utils.save_to_file(consts.domains_path, "\n".join(full_domains))

    create_config.qv2ray(other_domains, proxy_domains, ad_domains)
    create_config.shadowrocket(full_domains)
    create_config.clash(full_domains)
    create_config.switchy_omega(other_domains)
