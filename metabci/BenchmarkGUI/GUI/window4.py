#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Window4(QMainWindow):
    """窗口四"""
    def __init__(self):
        super().__init__()
        
        # 加载UI文件
        ui_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui/window4.ui")
        ui_file = QFile(ui_file_path)
        if not ui_file.open(QFile.ReadOnly):
            print(f"无法加载UI文件: {ui_file_path}")
            return
            
        # 使用QUiLoader加载UI
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()
        
        # 连接返回按钮信号
        self.ui.back_button.clicked.connect(self.ui.close)
