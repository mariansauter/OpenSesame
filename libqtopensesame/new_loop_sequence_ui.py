# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/new_loop_sequence.ui'
#
# Created: Tue Mar  8 15:27:03 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(411, 197)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtGui.QWidget(Dialog)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_icon = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_icon.sizePolicy().hasHeightForWidth())
        self.label_icon.setSizePolicy(sizePolicy)
        self.label_icon.setText("")
        self.label_icon.setPixmap(QtGui.QPixmap(":/icons/loop_large.png"))
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout_3.addWidget(self.label_icon)
        self.label_explanation = QtGui.QLabel(self.widget_3)
        self.label_explanation.setWordWrap(True)
        self.label_explanation.setObjectName("label_explanation")
        self.horizontalLayout_3.addWidget(self.label_explanation)
        self.verticalLayout.addWidget(self.widget_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.widget_2 = QtGui.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtGui.QGroupBox(self.widget_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.combobox_new = QtGui.QComboBox(self.groupBox)
        self.combobox_new.setObjectName("combobox_new")
        self.verticalLayout_2.addWidget(self.combobox_new)
        self.button_new = QtGui.QPushButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_new.setIcon(icon)
        self.button_new.setIconSize(QtCore.QSize(16, 16))
        self.button_new.setObjectName("button_new")
        self.verticalLayout_2.addWidget(self.button_new)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.combobox_select = QtGui.QComboBox(self.groupBox_2)
        self.combobox_select.setObjectName("combobox_select")
        self.verticalLayout_3.addWidget(self.combobox_select)
        self.button_select = QtGui.QPushButton(self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_select.setIcon(icon1)
        self.button_select.setIconSize(QtCore.QSize(16, 16))
        self.button_select.setObjectName("button_select")
        self.verticalLayout_3.addWidget(self.button_select)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.button_cancel = QtGui.QPushButton(self.widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cancel.setIcon(icon2)
        self.button_cancel.setIconSize(QtCore.QSize(16, 16))
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout_2.addWidget(self.button_cancel)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.button_cancel, QtCore.SIGNAL("clicked()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_explanation.setText(QtGui.QApplication.translate("Dialog", "Explanation\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Create new item to use", None, QtGui.QApplication.UnicodeUTF8))
        self.button_new.setText(QtGui.QApplication.translate("Dialog", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Select existing item to use", None, QtGui.QApplication.UnicodeUTF8))
        self.button_select.setText(QtGui.QApplication.translate("Dialog", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
