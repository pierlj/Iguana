# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(509, 358)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iguane.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setObjectName("label")
        self.verticalLayout_11.addWidget(self.label)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.launch = QtWidgets.QPushButton(self.tab)
        self.launch.setObjectName("launch")
        self.verticalLayout_3.addWidget(self.launch)
        self.verticalLayout_11.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graph = QtWidgets.QListWidget(self.tab)
        self.graph.setObjectName("graph")
        self.horizontalLayout.addWidget(self.graph)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.load = QtWidgets.QPushButton(self.tab)
        self.load.setObjectName("load")
        self.verticalLayout_5.addWidget(self.load)
        self.display = QtWidgets.QPushButton(self.tab)
        self.display.setEnabled(True)
        self.display.setObjectName("display")
        self.verticalLayout_5.addWidget(self.display)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graph_2 = QtWidgets.QListWidget(self.tab_2)
        self.graph_2.setObjectName("graph_2")
        self.horizontalLayout_2.addWidget(self.graph_2)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.load_2 = QtWidgets.QPushButton(self.tab_2)
        self.load_2.setObjectName("load_2")
        self.verticalLayout_13.addWidget(self.load_2)
        self.reduc = QtWidgets.QPushButton(self.tab_2)
        self.reduc.setEnabled(True)
        self.reduc.setObjectName("reduc")
        self.verticalLayout_13.addWidget(self.reduc)
        self.horizontalLayout_2.addLayout(self.verticalLayout_13)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_12.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setEnabled(True)
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.time = QtWidgets.QSpinBox(self.tab_3)
        self.time.setMaximum(86400)
        self.time.setObjectName("time")
        self.horizontalLayout_3.addWidget(self.time)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.graph_3 = QtWidgets.QListWidget(self.tab_3)
        self.graph_3.setObjectName("graph_3")
        self.horizontalLayout_4.addWidget(self.graph_3)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.load_3 = QtWidgets.QPushButton(self.tab_3)
        self.load_3.setObjectName("load_3")
        self.verticalLayout_15.addWidget(self.load_3)
        self.color = QtWidgets.QPushButton(self.tab_3)
        self.color.setEnabled(True)
        self.color.setObjectName("color")
        self.verticalLayout_15.addWidget(self.color)
        self.color_1 = QtWidgets.QPushButton(self.tab_3)
        self.color_1.setObjectName("color_1")
        self.verticalLayout_15.addWidget(self.color_1)
        self.nCompo = QtWidgets.QPushButton(self.tab_3)
        self.nCompo.setObjectName("nCompo")
        self.verticalLayout_15.addWidget(self.nCompo)
        self.horizontalLayout_4.addLayout(self.verticalLayout_15)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_14.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Iguana"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'trebuchet MS,sans-serif\'; font-size:15px; font-variant:small-caps;\">Affichage de graphe grâce à Cytoscape</span></p></body></html>"))
        self.launch.setText(_translate("Form", "Lancer Cytoscape"))
        self.load.setText(_translate("Form", "Charger un graphe"))
        self.display.setText(_translate("Form", "Afficher le graphe"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Affichage de graphe"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'trebuchet MS,sans-serif\'; font-size:15px; font-variant:small-caps;\">Réduction de graphes</span></p></body></html>"))
        self.load_2.setText(_translate("Form", "Charger un graphe"))
        self.reduc.setText(_translate("Form", "Réduire le graphe"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Réduction d\'un graphe"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'trebuchet MS,sans-serif\'; font-size:15px; font-variant:small-caps;\">Coloration du graphe réduit grâce à IGGY-poc</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><body><p align=\"center\">Temps d\'exécution maximal (en secondes) :</p></body></html>"))
        self.load_3.setText(_translate("Form", "Charger un graphe"))
        self.color.setText(_translate("Form", "Identifier les colorations"))
        self.color_1.setText(_translate("Form", "Colorer le graphe"))
        self.nCompo.setText(_translate("Form", "N Composants"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Coloration d\'un graphe"))
