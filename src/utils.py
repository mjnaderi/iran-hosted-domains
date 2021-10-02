import re


def cleanup(text: str) -> str:
    text = text.lower()

    # Remove http://, https:// and www.
    text = re.sub("(http(s)?://)?(www\\.)?", "", text)

    # Remove everything after /
    text = re.sub("^(.+)/.*$", "\1", text)

    # Remove Port
    text = re.sub(":\\d{1,5}$", "", text)

    # Remove everything after %
    text = re.sub("%.+", "", text)

    # Remove ,
    text = re.sub(",", "", text)

    return text.strip()


def is_ip(text: str) -> bool:
    return bool(
        re.match("^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}(:\\d{1,5})*$", text)
    )


def is_ir(text: str) -> bool:
    return bool(re.match("^(.+)\\.ir$", text))


def is_url(text: str) -> bool:
    return bool(URL_REGEX.match(text))


def convert_utf8(text: str) -> str:
    return text.encode('utf-8', errors='ignore').decode('utf-8')


URL_REGEX = re.compile(
    r"^"
    # user:pass authentication
    r"(?:\S+(?::\S*)?@)?"
    r"(?:"
    # IP address exclusion
    # private & local networks
    r"(?!(?:10|127)(?:\.\d{1,3}){3})"
    r"(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})"
    r"(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})"
    # IP address dotted notation octets
    # excludes loopback network 0.0.0.0
    # excludes reserved space >= 224.0.0.0
    # excludes network & broadcast addresses
    # (first & last IP address of each class)
    r"(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])"
    r"(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}"
    r"(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))"
    r"|"
    # host & domain names, may end with dot
    # can be replaced by a shortest alternative
    # r"(?![-_])(?:[-\w\u00a1-\uffff]{0,63}[^-_]\.)+"
    # r"(?:(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)"
    # # domain name
    # r"(?:\.(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)*"
    r"(?:"
    r"(?:"
    r"[a-z0-9\u00a1-\uffff]"
    r"[a-z0-9\u00a1-\uffff_-]{0,62}"
    r")?"
    r"[a-z0-9\u00a1-\uffff]\."
    r")+"
    # TLD identifier name, may end with dot
    r"(?:[a-z\u00a1-\uffff]{2,}\.?)"
    r")"
    # port number (optional)
    r"(?::\d{2,5})?"
    # resource path (optional)
    r"(?:[/?#]\S*)?"
    r"$"
    , re.UNICODE | re.I
)
