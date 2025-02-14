import sys
from PyQt5 import QtCore, QtWidgets
import Face_Identiify_ALL as FaceUI

# 创建窗口程序
app = QtWidgets.QApplication(sys.argv)
# 创建窗口载体
mainWindow = QtWidgets.QMainWindow()
# 创建人脸识别窗口的对象
ui = FaceUI.Ui_MainWindow()
# 设置人脸识别对象载体
ui.setupUi(mainWindow)
# 显示窗口
mainWindow.show()
# 点击关闭按钮时，退出程序
sys.exit(app.exec_())