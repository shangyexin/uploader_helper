#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Yasin
# @Time   : 2022-06-15
# @File   : main.py

import sys
import traceback

from log import logger
from PyQt5.QtWidgets import QApplication, QMainWindow
import media

if __name__ == "__main__":
    try:
        logger.debug("Thank you for using uploader helper...")
        app = QApplication(sys.argv)
        myMainWindow = QMainWindow()
        myUi = media.Ui_MainWindow()
        myUi.setupUi(myMainWindow)
        myMainWindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
