import re

def find_longest_substr(s):
    m = max(re.finditer(r'([A-Za-z0-9])\1*', s), key=lambda m: m.end() - m.start())
    return [str(ord(m.group(1))), m.end() - m.start(), [m.start(), m.end() - 1]]