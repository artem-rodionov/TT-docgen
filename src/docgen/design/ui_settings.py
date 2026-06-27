# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 379, 190))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.browseButton = QPushButton(self.verticalLayoutWidget)
        self.browseButton.setObjectName(u"browseButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen))
        self.browseButton.setIcon(icon)
        self.browseButton.setFlat(False)

        self.horizontalLayout.addWidget(self.browseButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.browseButton_2 = QPushButton(self.verticalLayoutWidget)
        self.browseButton_2.setObjectName(u"browseButton_2")
        self.browseButton_2.setIcon(icon)
        self.browseButton_2.setFlat(False)

        self.horizontalLayout_2.addWidget(self.browseButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        self.browseButton_4 = QPushButton(self.verticalLayoutWidget)
        self.browseButton_4.setObjectName(u"browseButton_4")
        self.browseButton_4.setIcon(icon)
        self.browseButton_4.setFlat(False)

        self.horizontalLayout_4.addWidget(self.browseButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.browseButton_3 = QPushButton(self.verticalLayoutWidget)
        self.browseButton_3.setObjectName(u"browseButton_3")
        self.browseButton_3.setIcon(icon)
        self.browseButton_3.setFlat(False)

        self.horizontalLayout_3.addWidget(self.browseButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_5.addWidget(self.lineEdit_5)

        self.browseButton_5 = QPushButton(self.verticalLayoutWidget)
        self.browseButton_5.setObjectName(u"browseButton_5")
        self.browseButton_5.setIcon(icon)
        self.browseButton_5.setFlat(False)

        self.horizontalLayout_5.addWidget(self.browseButton_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 270, 94, 26))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0441 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430\u043c\u0438", None))
        self.browseButton.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u0428\u0430\u0431\u043b\u043e\u043d\u044b</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.browseButton_2.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0432\u0435\u0440\u0435\u043d\u0438\u0435", None))
        self.browseButton_4.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0410\u043a\u0442", None))
        self.browseButton_3.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435", None))
        self.browseButton_5.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

