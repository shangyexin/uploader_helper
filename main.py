#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Yasin
# @Time   : 2022-06-15
# @File   : main.py

import traceback

from log import logger

if __name__ == "__main__":
    try:
        logger.debug("Thank you for using uploader helper...")
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
