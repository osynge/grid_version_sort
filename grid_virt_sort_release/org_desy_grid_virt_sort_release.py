#!/bin/env python
import re
import sys

regdelexp = re.compile('[-,.\/]')
regnumeric = re.compile('[0-9]+')

def split_line_by_delimiter(line,regex):
    splitline = []
    splititr = regex.finditer(line)
    lstart = 0
    for i in splititr:
        (mstart,mend) = i.span()
        if lstart != mstart:
            splitline.append(line[lstart:mstart])
        splitline.append(line[mstart:mend])
        lstart = mend
    linelen = len(line)
    if lstart != linelen:
        splitline.append(line[lstart:linelen])
    return splitline


def string_sort(x,y):
    xsplit = split_line_by_delimiter(x,regnumeric)
    ysplit = split_line_by_delimiter(y,regnumeric)
    ysplitlen = len(ysplit)
    xsplitlen = len(xsplit)
    minsplitlen = ysplitlen
    if xsplitlen < ysplitlen:
        minsplitlen = xsplitlen
    for i in range(minsplitlen):
        if xsplit[i] == ysplit[i]:
            continue
        if (xsplit[i].isdigit() and ysplit[i].isdigit()):
            rc = int(0)
            if int(xsplit[i]) > int(ysplit[i]):
                rc = -1
            if int(xsplit[i]) < int(ysplit[i]):
                rc = 1
            return rc
        if xsplit[i].isdigit():
            return -1
        if ysplit[i].isdigit():
            return 1
        if xsplit[i] > ysplit[i]:
            return -1
        if xsplit[i] < ysplit[i]:
            return 1
    if xsplitlen < ysplitlen:
        return 1
    if xsplitlen > ysplitlen:
        return -1
    return 0

def split_numeric_sort(x, y):
    xsplit = split_line_by_delimiter(x,regdelexp)
    ysplit = split_line_by_delimiter(y,regdelexp)
    ysplitlen = len(ysplit)
    xsplitlen = len(xsplit)
    minsplitlen = ysplitlen
    if xsplitlen < ysplitlen:
        minsplitlen = xsplitlen
    for i in range(minsplitlen):
        if xsplit[i] == ysplit[i]:
            continue
        if (xsplit[i].isdigit() and ysplit[i].isdigit()):
            rc = int(0)
            if int(xsplit[i]) > int(ysplit[i]):
                rc = -1
            if int(xsplit[i]) < int(ysplit[i]):
                rc = 1
            return rc
        if xsplit[i].isdigit():
            return -1
        if ysplit[i].isdigit():
            return 1
        rc = string_sort(xsplit[i],ysplit[i])
        if rc != 0:
            return rc
    if xsplitlen < ysplitlen:
        return 1
    if xsplitlen > ysplitlen:
        return -1
    return 0



def reverse_numeric(x, y):
    return split_numeric_sort( y,x)


class Version:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return split_numeric_sort(self.value, other.value) > 0

    def __gt__(self, other):
        return split_numeric_sort(self.value, other.value) < 0


def main():
    lines = []
    for rawline in sys.stdin:
        lines.append(Version(rawline.strip()))
    lines.sort()
    for line in lines:
        print(line.value)
