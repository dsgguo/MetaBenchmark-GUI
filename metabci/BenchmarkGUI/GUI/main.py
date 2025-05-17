#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filepath: f:\Code\MetaBenchmark-GUI\metabci\BenchmarkGUI\GUI\main.py

import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QDir
from PySide6.QtUiTools import QUiLoader

# 导入四个窗口模块
from window1 import Window1
from window2 import Window2
from window3 import Window3
from window4 import Window4


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 加载UI文件
        ui_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui/mainwindow.ui")
        ui_file = QFile(ui_file_path)
        if not ui_file.open(QFile.ReadOnly):
            print(f"无法加载UI文件: {ui_file_path}")
            sys.exit(-1)  
            
        # 使用QUiLoader加载UI
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()
        
        # 设置信号连接
        self.ui.button1.clicked.connect(self.open_window1)
        self.ui.button2.clicked.connect(self.open_window2)
        self.ui.button3.clicked.connect(self.open_window3)
        self.ui.button4.clicked.connect(self.open_window4)
        
        # 存储窗口实例
        self.window1 = None
        self.window2 = None
        self.window3 = None
        self.window4 = None
    
    def open_window1(self):
        if self.window1 is None:
            self.window1 = Window1()
        self.window1.ui.show()
        self.window1.ui.activateWindow()
    
    def open_window2(self):
        if self.window2 is None:
            self.window2 = Window2()
        self.window2.ui.show()
        self.window2.ui.activateWindow()
    
    def open_window3(self):
        if self.window3 is None:
            self.window3 = Window3()
        self.window3.ui.show()
        self.window3.ui.activateWindow()
    
    def open_window4(self):
        if self.window4 is None:
            self.window4 = Window4()
        self.window4.ui.show()
        self.window4.ui.activateWindow()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 设置应用样式
    app.setStyle("Fusion")
    
    # 创建主窗口
    window = MainWindow()
    window.ui.show()
    
    sys.exit(app.exec())