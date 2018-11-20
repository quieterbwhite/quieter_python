# Python3的URL编码解码

2018年03月28日 17:01:29 [桥路丶](https://me.csdn.net/qq_33876553) 阅读数：5719

> https://blog.csdn.net/qq_33876553/article/details/79730246

# 前言

博主最近在用python3比较强大的Django开发web的时候，发现一些url的编码问题，在浏览器提交请求api时，如果url中包含汉子，就会被自动编码掉。呈现的结果是 ==> %xx%xx%xx。如果出现3个百分号为一个原字符则为utf8编码，如果2个百分号则为gb2312编码。下面为大家演示编码和解码的代码。

# 编码

```python
from urllib.parse import quote
text = quote(text, 'utf-8')
```

注：text为要进行编码的字符串

# 解码

```python
from urllib.parse import unquote
text = unquote(text, 'utf-8')
```

# 源码

```python
def unquote(string, encoding='utf-8', errors='replace'):
    """Replace %xx escapes by their single-character equivalent. The optional
    encoding and errors parameters specify how to decode percent-encoded
    sequences into Unicode characters, as accepted by the bytes.decode()
    method.
    By default, percent-encoded sequences are decoded with UTF-8, and invalid
    sequences are replaced by a placeholder character.

    unquote('abc%20def') -> 'abc def'.
    """
    if '%' not in string:
        string.split
        return string
    if encoding is None:
        encoding = 'utf-8'
    if errors is None:
        errors = 'replace'
    bits = _asciire.split(string)
    res = [bits[0]]
    append = res.append
    for i in range(1, len(bits), 2):
        append(unquote_to_bytes(bits[i]).decode(encoding, errors))
        append(bits[i + 1])
    return ''.join(res)
    
    
def quote(string, safe='/', encoding=None, errors=None):
    """quote('abc def') -> 'abc%20def'

    Each part of a URL, e.g. the path info, the query, etc., has a
    different set of reserved characters that must be quoted.

    RFC 2396 Uniform Resource Identifiers (URI): Generic Syntax lists
    the following reserved characters.

    reserved    = ";" | "/" | "?" | ":" | "@" | "&" | "=" | "+" |
                  "$" | ","

    Each of these characters is reserved in some component of a URL,
    but not necessarily in all of them.

    By default, the quote function is intended for quoting the path
    section of a URL.  Thus, it will not encode '/'.  This character
    is reserved, but in typical usage the quote function is being
    called on a path where the existing slash characters are used as
    reserved characters.

    string and safe may be either str or bytes objects. encoding and errors
    must not be specified if string is a bytes object.

    The optional encoding and errors parameters specify how to deal with
    non-ASCII characters, as accepted by the str.encode method.
    By default, encoding='utf-8' (characters are encoded with UTF-8), and
    errors='strict' (unsupported characters raise a UnicodeEncodeError).
    """
    if isinstance(string, str):
        if not string:
            return string
        if encoding is None:
            encoding = 'utf-8'
        if errors is None:
            errors = 'strict'
        string = string.encode(encoding, errors)
    else:
        if encoding is not None:
            raise TypeError("quote() doesn't support 'encoding' for bytes")
        if errors is not None:
            raise TypeError("quote() doesn't support 'errors' for bytes")
    return quote_from_bytes(string, safe)
```