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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 379, 224))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.apiTokenLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.apiTokenLineEdit.setObjectName(u"apiTokenLineEdit")

        self.horizontalLayout_6.addWidget(self.apiTokenLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.workerTableLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.workerTableLineEdit.setObjectName(u"workerTableLineEdit")

        self.horizontalLayout.addWidget(self.workerTableLineEdit)

        self.workerBrowseButton = QPushButton(self.verticalLayoutWidget)
        self.workerBrowseButton.setObjectName(u"workerBrowseButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen))
        self.workerBrowseButton.setIcon(icon)
        self.workerBrowseButton.setFlat(False)

        self.horizontalLayout.addWidget(self.workerBrowseButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.taskPathLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.taskPathLineEdit.setObjectName(u"taskPathLineEdit")

        self.horizontalLayout_2.addWidget(self.taskPathLineEdit)

        self.taskBrowseButton = QPushButton(self.verticalLayoutWidget)
        self.taskBrowseButton.setObjectName(u"taskBrowseButton")
        self.taskBrowseButton.setIcon(icon)
        self.taskBrowseButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.taskBrowseButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.statementPathLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.statementPathLineEdit.setObjectName(u"statementPathLineEdit")

        self.horizontalLayout_4.addWidget(self.statementPathLineEdit)

        self.statementBrowseButton = QPushButton(self.verticalLayoutWidget)
        self.statementBrowseButton.setObjectName(u"statementBrowseButton")
        self.statementBrowseButton.setIcon(icon)
        self.statementBrowseButton.setFlat(False)

        self.horizontalLayout_4.addWidget(self.statementBrowseButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.actPathLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.actPathLineEdit.setObjectName(u"actPathLineEdit")

        self.horizontalLayout_3.addWidget(self.actPathLineEdit)

        self.actBrowseButton = QPushButton(self.verticalLayoutWidget)
        self.actBrowseButton.setObjectName(u"actBrowseButton")
        self.actBrowseButton.setIcon(icon)
        self.actBrowseButton.setFlat(False)

        self.horizontalLayout_3.addWidget(self.actBrowseButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.savePathLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.savePathLineEdit.setObjectName(u"savePathLineEdit")

        self.horizontalLayout_5.addWidget(self.savePathLineEdit)

        self.saveBrowseButton = QPushButton(self.verticalLayoutWidget)
        self.saveBrowseButton.setObjectName(u"saveBrowseButton")
        self.saveBrowseButton.setIcon(icon)
        self.saveBrowseButton.setFlat(False)

        self.horizontalLayout_5.addWidget(self.saveBrowseButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(310, 230, 81, 61))
        self.buttonBox.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"API \u0442\u043e\u043a\u0435\u043d", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0441 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430\u043c\u0438", None))
        self.workerBrowseButton.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u0428\u0430\u0431\u043b\u043e\u043d\u044b</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.taskBrowseButton.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0432\u0435\u0440\u0435\u043d\u0438\u0435", None))
        self.statementBrowseButton.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0410\u043a\u0442", None))
        self.actBrowseButton.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435", None))
        self.saveBrowseButton.setText("")
    # retranslateUi

