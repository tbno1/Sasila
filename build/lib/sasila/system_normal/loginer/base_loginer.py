#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf-8')


class BaseLoginer(object):
    def login(self, account, password):
        cookies = ""
        return cookies