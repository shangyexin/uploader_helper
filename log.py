#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Yasin
# @Time   : 2022-06-15
# @File   : log.py

import os
import sys

from loguru import logger

APP_NAME = 'uploader_helper'
DEFAULT_LOG_LEVEL = 'DEBUG'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

log_file_path = os.path.join(BASE_DIR, 'logs', APP_NAME + '.log')
err_log_file_path = os.path.join(BASE_DIR, 'logs', APP_NAME + '_err.log')

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")  # 标准输出日志格式

logger.add(log_file_path, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",  # 文件日志格式
           rotation="10 MB",  # 单个日志文件最大10M
           retention="10 days",  # 最多保存10天
           encoding='utf-8',
           enqueue=True,
           level=DEFAULT_LOG_LEVEL)

logger.add(err_log_file_path, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",  # 错误文件日志格式
           rotation="10 MB",  # 单个日志文件最大10M
           retention="2 weeks",  # 最多保存2周
           encoding='utf-8',
           enqueue=True,
           level='ERROR')

# logger.add(log_file_path, backtrace=True, diagnose=True) # 异常时显示堆栈以跟踪错误
