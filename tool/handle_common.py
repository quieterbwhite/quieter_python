import urllib2
import os.path
import sys
import re

def r1(pattern, text):
    m = re.search(pattern, text)
    if m:
        return m.group(1)

def match1(text, *patterns):
    """Scans through a string for substrings matched some patterns (first-subgroups only).

    Args:
        text: A string to be scanned.
        patterns: Arbitrary number of regex patterns.

    Returns:
        When only one pattern is given, returns a string (None if no match found).
        When more than one pattern are given, returns a list of strings ([] if no match found).
    """

    if len(patterns) == 1:
        pattern = patterns[0]
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        else:
            return None
    else:
        ret = []
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                ret.append(match.group(1))
        return ret


def unicodize(text):
    return re.sub(r'\\u([0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f])', lambda x: chr(int(x.group(0)[2:], 16)), text)


def get_secret_mobile(mobile):
    if mobile:
        return mobile[0:3] + "*****" + mobile[-3:]
    else:
        return ""


def get_secret_email(email):
    if email:
        strs = email.split("@")
        return strs[0][0:3] + "*****@" + strs[1]
    else:
        return ""


def main():

	res = parse_host("http://10.0.90.234:9004")
	print res

if __name__ == "__main__":
	main()