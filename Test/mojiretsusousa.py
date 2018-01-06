#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
string = "alarm(sjfafaijkn)    "
# moji = string[:string.index("(")]
if '(' in string:
    moji = string[:string.index("(")]
else:
    moji = string
print(moji)

# >>> import re
# >>> r = re.compile("(.*)(,)(.*)")
# >>> m = r.match("hello, this is test program.")
# >>> print m.group(1)
# hello
# >>>
