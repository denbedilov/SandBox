import re

ip_pattern = "(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"


def check_pattern(pattern, text):
    pattern = re.compile(pattern)
    return bool(pattern.fullmatch(text))


def is_valid_ip(ip):
    return check_pattern(ip_pattern, ip)


print(is_valid_ip("150.205.1"))
print(is_valid_ip("1.1.1.1"))
print(is_valid_ip("2.255.205.1.1"))
