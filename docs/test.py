#!/usr/bin/env python3
# import sys
# from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
# from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor

# class SystemTrayIcon(QSystemTrayIcon):
#     def __init__(self, icon, app):
#         QSystemTrayIcon.__init__(self, icon, app)
#         menu = QMenu()

#         exitAction = QAction("Exit", app)
#         exitAction.triggered.connect(app.quit)

#         menu.addAction(exitAction)
#         self.setContextMenu(menu)

# def main():
#     app = QApplication(sys.argv)

#     # 创建一个 QPixmap 对象，设置其大小为 64x64
#     pixmap = QPixmap(64, 64)
#     # 使用 QPainter 绘制红色的矩形
#     painter = QPainter(pixmap)
#     painter.fillRect(pixmap.rect(), QColor('red'))
#     painter.end()

#     trayIcon = SystemTrayIcon(QIcon(pixmap), app)

#     trayIcon.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pystray

def create_image():
    # Generate an image and invert it
    image = Image.new('RGB', (64, 64), 'red')
    return image

def exit_action(icon, item):
    icon.stop()
    root.quit()

def show_message(icon, item):
    icon.stop()
    messagebox.showinfo("Hello", "Hello, World!")

def setup(icon):
    icon.visible = True
    root.update()

image = create_image()
menu = (pystray.MenuItem('Show Message', show_message), pystray.MenuItem('Exit', exit_action))
icon = pystray.Icon("test_icon", image, "My System Tray Icon", menu)

root = tk.Tk()
root.withdraw()  # hide main window

icon.run(setup)


#export XAUTHORITY=/run/user/1000/.mutter-Xwaylandauth.LJ6IM2 
#export DISPLAY=:0
