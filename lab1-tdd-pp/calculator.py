#!/usr/bin/env python3

import re

calc = (
    lambda s: sum(
        map(
            lambda s: float(s) if re.match(r"[-+]?\d+(\.\d*)?$", s) else 0,
            re.sub(r"[^\d\.+-]", " ", s).split(" "),
        )
    )
    if type(s) == str
    else 0
)
