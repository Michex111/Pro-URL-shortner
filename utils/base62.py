import string

CHARSET = string.digits + string.ascii_lowercase + string.ascii_uppercase
BASE = len(CHARSET)

CHARSET_MAP = {char: index for index, char in enumerate(CHARSET)}


def encode(num: int) -> str:
    if num == 0:
        return CHARSET[0]
    
    chars = []
    while num:
        num, rem = divmod(num, BASE)
        chars.append(CHARSET[rem])
    return ''.join(reversed(chars))

def decode(s: str) -> int:
    num = 0
    for char in s:
        num = num * BASE + CHARSET_MAP[char]
    return num
