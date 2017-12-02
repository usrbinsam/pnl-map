# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mapeditor.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MapEditor(object):
    def setupUi(self, MapEditor):
        MapEditor.setObjectName("MapEditor")
        MapEditor.resize(535, 633)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(MapEditor)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(MapEditor)
        self.splitter.setStyleSheet("")
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.mapTableGroupBox = QtWidgets.QGroupBox(self.splitter)
        self.mapTableGroupBox.setObjectName("mapTableGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mapTableGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mapTableLayout = QtWidgets.QVBoxLayout()
        self.mapTableLayout.setObjectName("mapTableLayout")
        self.filterHLayout = QtWidgets.QHBoxLayout()
        self.filterHLayout.setObjectName("filterHLayout")
        self.rowFilterLineEdit = QtWidgets.QLineEdit(self.mapTableGroupBox)
        self.rowFilterLineEdit.setClearButtonEnabled(True)
        self.rowFilterLineEdit.setObjectName("rowFilterLineEdit")
        self.filterHLayout.addWidget(self.rowFilterLineEdit)
        self.filterRegex = QtWidgets.QCheckBox(self.mapTableGroupBox)
        self.filterRegex.setObjectName("filterRegex")
        self.filterHLayout.addWidget(self.filterRegex)
        self.mapTableLayout.addLayout(self.filterHLayout)
        self.mapTable = QtWidgets.QTableWidget(self.mapTableGroupBox)
        self.mapTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.mapTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.mapTable.setObjectName("mapTable")
        self.mapTable.setColumnCount(3)
        self.mapTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.mapTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mapTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.mapTable.setHorizontalHeaderItem(2, item)
        self.mapTable.horizontalHeader().setStretchLastSection(True)
        self.mapTableLayout.addWidget(self.mapTable)
        self.addDelHLayout = QtWidgets.QHBoxLayout()
        self.addDelHLayout.setObjectName("addDelHLayout")
        self.addRowButton = QtWidgets.QPushButton(self.mapTableGroupBox)
        self.addRowButton.setObjectName("addRowButton")
        self.addDelHLayout.addWidget(self.addRowButton)
        self.delRowButton = QtWidgets.QPushButton(self.mapTableGroupBox)
        self.delRowButton.setObjectName("delRowButton")
        self.addDelHLayout.addWidget(self.delRowButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.addDelHLayout.addItem(spacerItem)
        self.mapTableLayout.addLayout(self.addDelHLayout)
        self.verticalLayout.addLayout(self.mapTableLayout)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.actionVLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.actionVLayout.setContentsMargins(0, 0, 0, 0)
        self.actionVLayout.setObjectName("actionVLayout")
        self.newMapButton = QtWidgets.QPushButton(self.layoutWidget)
        self.newMapButton.setObjectName("newMapButton")
        self.actionVLayout.addWidget(self.newMapButton)
        self.openMapButton = QtWidgets.QPushButton(self.layoutWidget)
        self.openMapButton.setObjectName("openMapButton")
        self.actionVLayout.addWidget(self.openMapButton)
        self.saveMapButton = QtWidgets.QPushButton(self.layoutWidget)
        self.saveMapButton.setObjectName("saveMapButton")
        self.actionVLayout.addWidget(self.saveMapButton)
        self.saveAsButton = QtWidgets.QPushButton(self.layoutWidget)
        self.saveAsButton.setObjectName("saveAsButton")
        self.actionVLayout.addWidget(self.saveAsButton)
        self.quitButton = QtWidgets.QPushButton(self.layoutWidget)
        self.quitButton.setObjectName("quitButton")
        self.actionVLayout.addWidget(self.quitButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.actionVLayout.addItem(spacerItem1)
        self.configButton = QtWidgets.QPushButton(self.layoutWidget)
        self.configButton.setObjectName("configButton")
        self.actionVLayout.addWidget(self.configButton)
        self.preloadRowsButton = QtWidgets.QPushButton(self.layoutWidget)
        self.preloadRowsButton.setObjectName("preloadRowsButton")
        self.actionVLayout.addWidget(self.preloadRowsButton)
        self.horizontalLayout_2.addWidget(self.splitter)

        self.retranslateUi(MapEditor)
        self.mapTable.itemChanged['QTableWidgetItem*'].connect(self.mapTable.resizeRowsToContents)
        self.quitButton.clicked.connect(MapEditor.accept)
        QtCore.QMetaObject.connectSlotsByName(MapEditor)

    def retranslateUi(self, MapEditor):
        _translate = QtCore.QCoreApplication.translate
        MapEditor.setWindowTitle(_translate("MapEditor", "Company Map Editor"))
        self.mapTableGroupBox.setTitle(_translate("MapEditor", "Map Table"))
        self.rowFilterLineEdit.setToolTip(_translate("MapEditor", "<html><head/><body><p>Filter row names.</p><p><br/></p></body></html>"))
        self.rowFilterLineEdit.setPlaceholderText(_translate("MapEditor", "Filter row name ..."))
        self.filterRegex.setText(_translate("MapEditor", "Regular Expression"))
        self.mapTable.setToolTip(_translate("MapEditor", "Map table."))
        self.mapTable.setWhatsThis(_translate("MapEditor", "<html><head/><body><p>This is the table which represents a map file for a company conversion. A map file gives the converter wizard instructions on how to move data from the QuickBooks export to the Popeyes spreadsheet.</p><p>The <span style=\" font-weight:600;\">Row Name</span> column represents the title of a row on the Popeyes spreadsheet. The <span style=\" font-weight:600;\">Search Method</span> dropdown box tells the converter how to match the <span style=\" font-weight:600;\">Search Term</span> keyword in the QuickBooks export. For a QuickBooks export, the search term corresponds to the account names column.</p><p>For example, f the <span style=\" font-weight:600;\">Search Term</span> is set to <span style=\" font-weight:600;\">starts</span>, the converter wizard will consider the first that <span style=\" font-style:italic;\">starts with</span> the value in <span style=\" font-weight:600;\">Search Term</span>. </p><p>The <span style=\" font-weight:600;\">ends</span> method will match on the first cell that <span style=\" font-style:italic;\">ends with</span> the search term.</p><p>The <span style=\" font-weight:600;\">contains</span> method will match on the first cell which <span style=\" font-style:italic;\">contains</span> the search term (beginning, middle, or end).</p><p>The <span style=\" font-weight:600;\">exact</span> method will match on the first cell which <span style=\" font-style:italic;\">exactly</span> matches the search term (case sensitive).</p><p>The <span style=\" font-weight:600;\">re</span> method will match on the first cell which matches the Regular Expression in the search term (advanced usage).</p><p>The <span style=\" font-weight:600;\">set</span> method will explicitly set the cell to the value in the search term.</p><p>The <span style=\" font-weight:600;\">each</span> method will set each destination cell, in order, with comma separated values in the search term. For example, if there are 3 destination cells, and the search term is set to &quot;A,B,C&quot;, then cell 1 will be A, cell 2 will be B, and cell 3 will be C.</p></body></html>"))
        item = self.mapTable.horizontalHeaderItem(0)
        item.setText(_translate("MapEditor", "Row Name"))
        item = self.mapTable.horizontalHeaderItem(1)
        item.setText(_translate("MapEditor", "Search Method"))
        item = self.mapTable.horizontalHeaderItem(2)
        item.setText(_translate("MapEditor", "Search Term"))
        self.addRowButton.setToolTip(_translate("MapEditor", "Add a row to the company map file."))
        self.addRowButton.setWhatsThis(_translate("MapEditor", "Creates blank row in the table above for a new entry in the company map file."))
        self.addRowButton.setText(_translate("MapEditor", "+"))
        self.delRowButton.setToolTip(_translate("MapEditor", "Delete the currently selected row(s)."))
        self.delRowButton.setWhatsThis(_translate("MapEditor", "Deletes the currently highlighted rows in the table above."))
        self.delRowButton.setText(_translate("MapEditor", "-"))
        self.newMapButton.setToolTip(_translate("MapEditor", "Create a new map file."))
        self.newMapButton.setWhatsThis(_translate("MapEditor", "Resets the above table for a new map file."))
        self.newMapButton.setText(_translate("MapEditor", "New"))
        self.openMapButton.setToolTip(_translate("MapEditor", "Open a map file."))
        self.openMapButton.setWhatsThis(_translate("MapEditor", "Open an existing map file into the above table for editing."))
        self.openMapButton.setText(_translate("MapEditor", "Open"))
        self.saveMapButton.setToolTip(_translate("MapEditor", "Save map file."))
        self.saveMapButton.setWhatsThis(_translate("MapEditor", "Saves the above table to the hard drive."))
        self.saveMapButton.setText(_translate("MapEditor", "Save"))
        self.saveAsButton.setToolTip(_translate("MapEditor", "Save map under a different name."))
        self.saveAsButton.setWhatsThis(_translate("MapEditor", "Saves the curent map file in the table above under a different file name than what\'s currently open."))
        self.saveAsButton.setText(_translate("MapEditor", "Save As ..."))
        self.quitButton.setText(_translate("MapEditor", "Close"))
        self.configButton.setText(_translate("MapEditor", "Configuration"))
        self.preloadRowsButton.setToolTip(_translate("MapEditor", "<html><head/><body><p>Load row names from a spreadsheet.</p></body></html>"))
        self.preloadRowsButton.setWhatsThis(_translate("MapEditor", "<html><head/><body><p>Preloads Row Names from an existing Excel spreadsheet into the Row Name column. This helps create more accurate map files.</p></body></html>"))
        self.preloadRowsButton.setText(_translate("MapEditor", "Preload Rows"))

