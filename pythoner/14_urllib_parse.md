# Urllib.parse

```
Firstly, the cgi.parse_qs function is deprecated and merely an alias for urllib.parse.parse_qs, you may want to adjust your import path.

Secondly, you are passing in a byte string into the parse method. If you pass in a regular (unicode) string instead the parse_qs method returns regular strings:

>>> from urllib.parse import parse_qs
>>> parse_qs(b'a_byte_string=foobar')
{b'a_byte_string': [b'foobar']}
>>> parse_qs('a_unicode_string=foobar')
{'a_unicode_string': ['foobar']}
So you'll need to decode your file-read byte string to a regular string first.
```
