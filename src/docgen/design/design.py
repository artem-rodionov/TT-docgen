# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'docgen.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFormLayout, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1078, 763)
        self.tableWIthDataAction = QAction(MainWindow)
        self.tableWIthDataAction.setObjectName(u"tableWIthDataAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 491, 311))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pathLineEdit = QTextEdit(self.formLayoutWidget)
        self.pathLineEdit.setObjectName(u"pathLineEdit")

        self.horizontalLayout.addWidget(self.pathLineEdit)

        self.browseButton = QPushButton(self.formLayoutWidget)
        self.browseButton.setObjectName(u"browseButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen))
        self.browseButton.setIcon(icon)
        self.browseButton.setFlat(False)

        self.horizontalLayout.addWidget(self.browseButton)


        self.formLayout.setLayout(5, QFormLayout.ItemRole.LabelRole, self.horizontalLayout)

        self.projectsComboBox = QComboBox(self.formLayoutWidget)
        self.projectsComboBox.setObjectName(u"projectsComboBox")
        self.projectsComboBox.setEditable(True)
        self.projectsComboBox.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.projectsComboBox)

        self.projectInfoButton = QPushButton(self.formLayoutWidget)
        self.projectInfoButton.setObjectName(u"projectInfoButton")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.projectInfoButton)

        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(620, 0, 321, 211))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textBrowser_2 = QTextBrowser(self.formLayoutWidget_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.horizontalLayout_4.addWidget(self.textBrowser_2)

        self.startDate = QDateEdit(self.formLayoutWidget_2)
        self.startDate.setObjectName(u"startDate")

        self.horizontalLayout_4.addWidget(self.startDate)


        self.formLayout_3.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.textBrowser_3 = QTextBrowser(self.formLayoutWidget_2)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.horizontalLayout_5.addWidget(self.textBrowser_3)

        self.endDate = QDateEdit(self.formLayoutWidget_2)
        self.endDate.setObjectName(u"endDate")

        self.horizontalLayout_5.addWidget(self.endDate)


        self.formLayout_3.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.textBrowser = QTextBrowser(self.formLayoutWidget_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_6.addWidget(self.textBrowser)

        self.currentDate = QDateEdit(self.formLayoutWidget_2)
        self.currentDate.setObjectName(u"currentDate")

        self.horizontalLayout_6.addWidget(self.currentDate)


        self.formLayout_3.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.textBrowser_4 = QTextBrowser(self.formLayoutWidget_2)
        self.textBrowser_4.setObjectName(u"textBrowser_4")

        self.horizontalLayout_7.addWidget(self.textBrowser_4)

        self.headWorkerBox = QComboBox(self.formLayoutWidget_2)
        self.headWorkerBox.setObjectName(u"headWorkerBox")

        self.horizontalLayout_7.addWidget(self.headWorkerBox)


        self.formLayout_3.setLayout(3, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.textBrowser_5 = QTextBrowser(self.formLayoutWidget_2)
        self.textBrowser_5.setObjectName(u"textBrowser_5")

        self.horizontalLayout_8.addWidget(self.textBrowser_5)

        self.styleComboBox = QComboBox(self.formLayoutWidget_2)
        self.styleComboBox.setObjectName(u"styleComboBox")
        self.styleComboBox.setEditable(False)
        self.styleComboBox.setModelColumn(0)

        self.horizontalLayout_8.addWidget(self.styleComboBox)


        self.formLayout_3.setLayout(4, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_8)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 690, 118, 23))
        self.progressBar.setValue(0)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(300, 370, 231, 117))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.taskCheckBox = QCheckBox(self.horizontalLayoutWidget)
        self.taskCheckBox.setObjectName(u"taskCheckBox")

        self.verticalLayout.addWidget(self.taskCheckBox)

        self.statementCheckBox = QCheckBox(self.horizontalLayoutWidget)
        self.statementCheckBox.setObjectName(u"statementCheckBox")

        self.verticalLayout.addWidget(self.statementCheckBox)

        self.actsCheckBox = QCheckBox(self.horizontalLayoutWidget)
        self.actsCheckBox.setObjectName(u"actsCheckBox")

        self.verticalLayout.addWidget(self.actsCheckBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.generateButton = QPushButton(self.horizontalLayoutWidget)
        self.generateButton.setObjectName(u"generateButton")

        self.horizontalLayout_2.addWidget(self.generateButton)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(620, 300, 313, 91))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_9.addWidget(self.label)

        self.workTypeCheckBox = QCheckBox(self.verticalLayoutWidget)
        self.workTypeCheckBox.setObjectName(u"workTypeCheckBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workTypeCheckBox.sizePolicy().hasHeightForWidth())
        self.workTypeCheckBox.setSizePolicy(sizePolicy)
        self.workTypeCheckBox.setMinimumSize(QSize(50, 26))
        self.workTypeCheckBox.setMaximumSize(QSize(50, 26))
        self.workTypeCheckBox.setStyleSheet(u"/* \u0422\u0440\u0435\u043a (\u0444\u043e\u043d \u043f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0430\u0442\u0435\u043b\u044f) */\n"
"QCheckBox {\n"
"    background-color: #bdc3c7;\n"
"    border-radius: 13px;\n"
"    width: 50px;\n"
"    height: 26px;\n"
"}\n"
"\n"
"/* \u0418\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440 (\u043f\u043e\u043b\u0437\u0443\u043d\u043e\u043a) - \u043e\u0431\u0449\u0438\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 */\n"
"QCheckBox::indicator {\n"
"    width: 22px;\n"
"    height: 22px;\n"
"    border-radius: 11px;\n"
"    margin: 2px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \"\u0412\u043a\u043b\u044e\u0447\u0435\u043d\u043e\" (\u0432\u044b\u0431\u0440\u0430\u043d \u0432\u0442\u043e\u0440\u043e\u0439 \u0442\u0438\u043f) */\n"
"QCheckBox::indicator:checked {\n"
"    background-color: black;\n"
"    margin-left: 26px;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d"
                        "\u0438\u0435 \"\u0412\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043e\" (\u0432\u044b\u0431\u0440\u0430\u043d \u043f\u0435\u0440\u0432\u044b\u0439 \u0442\u0438\u043f) */\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: white;\n"
"    margin-left: 2px;\n"
"    margin-right: 26px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.workTypeCheckBox)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_9.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(410, 550, 541, 80))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1078, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.tableWIthDataAction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tableWIthDataAction.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.pathLineEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pathLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.browseButton.setText("")
        self.projectsComboBox.setCurrentText("")
        self.projectInfoButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430</p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f</p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u0430\u0442\u0430 \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u0438</p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c \u043f\u0440\u043e\u0435\u043a\u0442\u0430</p></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u0442\u0438\u043b\u044c</p></body></html>", None))
        self.taskCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.statementCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0435\u043d\u0438\u0435", None))
        self.actsCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u044b", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0422\u0438\u043f \u0440\u0430\u0431\u043e\u0442\u044b</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.workTypeCheckBox.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
    # retranslateUi

