from PyQt5.QtWidgets import QWidget, QStackedWidget, QScrollArea, QLabel, QPushButton, QLineEdit, QMessageBox, QTableWidgetItem, QCheckBox, QRadioButton, QGroupBox, QVBoxLayout
from PyQt5.QtCore import Qt
from app_package import Tables_LayoutTable



class Tables_Layout(QWidget):
    """
    To be inherit. Inherit by layouts with tables to show to users - only tables, not inserting fields. Lyouts with inserting fields etc inherit "TableAndList".
    """

    def __init__(self, received_lists, received_listTablesLayout, *args, **kwargs):
        super(Tables_Layout, self).__init__(*args, **kwargs)

        # self.listsTuple = received_listsTuple
        # self.lists = self.listsTuple[0]
        # self.thisListGroup = self.listsTuple[1]
        # self.thisListNumber = self.listsTuple[2]
        # self.thisList = self.lists.listsOfAllLists[self.thisListGroup][self.thisListNumber]
        self.lists = received_lists
        self.listTablesLayout = received_listTablesLayout

        self.thisList = self.lists.listsOfAllLists[2][1]
        # self.thisListNumber = -1  # DEL
        self.listOfTablesToActualize = []
        self.colorRowsInTable = 3
        self.colorClickedRowInTable = 1
        self.specialExceptSolution_isDisplayedThisLayout = False  # Bad solution.
        self.layout_yPosition = 70

        self.font_h1 = self.font()
        self.font_h1.setPointSize(14)
        self.fontB = self.font()
        self.fontB.setBold(True)

        self.initializeFirst1()
        self.initializeFirst2()

        self.placeContent_layout()

        self.setDefaultValues1()


    def initializeFirst1(self):
        """
        To be override.
        """
        pass


    def initializeFirst2(self):
        """
        To be override.
        """
        pass


    def placeContent_layout(self):
        """
        To be override.
        """
        pass


    # Layout parts.
    def layout_head(self):
        self.button1a = QPushButton("<- Zpět", self)
        self.button1a.setGeometry(15, 12, 120, 22)

        label1 = QLabel("Tabulka: " + self.thisList.tableName, self)
        label1.setFont(self.font_h1)
        label1.setGeometry(170, 10, 930, 24)

        self.button2 = QPushButton("Aktualizovat", self)
        self.button2.setGeometry(920, 12, 180, 22)
        self.layout_yPosition = 50


    def layout_bottom(self):
        self.button1b = QPushButton("<- Zpět", self)
        self.button1b.setGeometry(15, self.layout_yPosition, 120, 22)
        self.layout_yPosition += 50


    def layout_table(self, useList=-1, height=555, showLabel=True):
        if useList == -1:
            useList = self.thisList
        if showLabel:
            label1 = QLabel("Tabulka: " + useList.tableName, self)
            label1.setGeometry(15, self.layout_yPosition, 1085, 20)
            self.layout_yPosition += 25

        table = Tables_LayoutTable.MainTable(self.lists, useList, self)
        table.paintTable()
        self.listOfTablesToActualize.append(table)
        table.setGeometry(15, self.layout_yPosition, 1085, height)
        self.layout_yPosition += height + 10


    def layout_labelStatus(self, xDiameter=1100):
        label1 = QLabel("Stav:", self)
        label1.setFont(self.fontB)
        label1.setGeometry(15, self.layout_yPosition, 80, 20)
        self.label5 = QLabel("-", self)
        self.label5.setFont(self.fontB)
        self.label5.setGeometry(100, self.layout_yPosition, xDiameter - 100, 20)
        self.layout_yPosition += 35


    def layout_findString(self):
        label1 = QLabel("Hledat slovo:", self)
        label1.setGeometry(15, self.layout_yPosition, 180, 20)

        self.editText4 = QLineEdit(self)
        self.editText4.setGeometry(200, self.layout_yPosition, 80, 20)

        button1 = QPushButton("Najít", self)
        button1.clicked.connect(self.event_button9_findString)
        button1.setGeometry(300, self.layout_yPosition, 120, 22)
        self.layout_yPosition += 35

        # Not used: label "Nalezeno:".
        # label12 = QLabel("Stav:", self)
        # label12.setGeometry(15, self.layout_yPosition, 180, 20)
        #
        # self.label13 = QLabel("-", self)
        # self.label13.setGeometry(200, self.layout_yPosition, 700, 20)
        # self.layout_yPosition += 35


    # Events.
    def setDefaultValues1(self):
        """
        Can be override.
        Set default values at inserting table and editTexts, check IDvalue.
        """
        self.editText4.setText("")
        self.label5.setText("-")

        self.setColoringTables()


    def setColoringTables(self):
        """
        Set which row to color.
        """
        for i1 in self.listOfTablesToActualize:
            i1.colorRowsCount = self.colorRowsInTable
            i1.colorClickedRow = self.colorClickedRowInTable


    def refreshTables(self):
        for i1 in range(len(self.listOfTablesToActualize)):
            self.listOfTablesToActualize[i1].paintTable()
        self.refreshTables2()
        self.refreshTables3()


    def refreshTables2(self):
        """
        To be override.
        """
        pass


    def refreshTables3(self):
        """
        To be override.
        Additional items in any layout.
        """
        pass


    def refreshValuesAtLayout(self):
        # Current layout.
        pass


    def findStringInTable(self, thisList, findString):
        """
        Function finding received string in table at received list.
        Finding at every item in 2D table, string can be part of item. Each item convert to string.
        Return string message with problem or with results.
        """
        result = ""
        count1 = 0
        count2 = 0
        if thisList.table is None:
            return "Najít - probém: tabulka je prázdná."
        elif len(thisList.table) == 0:
            return "Najít - probém: tabulka je prázdná."
        if findString is None:
            message = "Najít: žádný výraz nezadán."
        elif len(findString) == 0:
            message = "Najít: žádný výraz nezadán."
        elif len(findString) > 20:
            message = "Najít: zadejte nějaký kratší výraz  :-) "
        else:
            try:
                lastFoundID = -1
                for i1 in range(len(thisList.table)):
                    if count1 > 100000 or count2 > 60:
                        break
                    for i2 in range(1, thisList.columnsQuantityUsed):
                        count1 += 1
                        if findString in str(thisList.table[i1][i2]):
                            if lastFoundID == thisList.table[i1][0]:  # Each row only once.
                                continue
                            count2 += 1
                            if len(result) > 0:
                                result += ", "
                            result += str(thisList.table[i1][0])
                            lastFoundID = thisList.table[i1][0]
            except ValueError:
                return "Chyba programu: vyjímka ValueError při prohledávání tabulky."
            if len(result) == 0:
                message = "Výraz v tabulce nenalezen."
            else:
                message = "Výraz nalezen v těchto ID:  " + result + "."
        return message


    def event_button9_findString(self):
        # Button: find string in user's table.
        self.label5.setText(self.findStringInTable(self.thisList, self.editText4.text()))



class TableAndList(Tables_Layout):
    """
    To be inherit. Inherit by layouts with inserting fields etc.
    This class could be part of "Tables_Layout" class, but there is specific functions to editing lists, so I place it to this class.
    """

    def __init__(self, received_lists, received_listTablesLayout, *args, **kwargs):
        self.thisBaseList = received_lists.listsOfAllLists[2][1]
        self.listOfTablesToActualize_lastInserted = []
        self.listOfLabelsToActualize_sumOfRows = []
        self.rewriteExistsRow = False
        super(TableAndList, self).__init__(received_lists, received_listTablesLayout, *args, **kwargs)


    def initializeFirst1(self):
        self.thisBaseList = self.lists.listsOfAllLists[2][1]
        self.rewriteExistsRow = False


    # Layout parts.
    def layout_labelRowsInTable(self):
        label1 = QLabel("Počet záznamů v listu L" + str(self.thisBaseList.tableNumber) + ":", self)
        label1.setGeometry(15, self.layout_yPosition, 150, 20)
        label6 = QLabel("-", self)
        self.listOfLabelsToActualize_sumOfRows.append(label6)
        label6.setGeometry(170, self.layout_yPosition, 950, 20)
        self.layout_yPosition += 25


    def layout_addRow1(self):
        # Add row: by table.
        label1 = QLabel("Přidat nový", self)
        label1.setFont(self.font_h1)
        label1.setGeometry(15, self.layout_yPosition, 1100, 24)
        self.layout_yPosition += 35

        self.table_oneRow = Tables_LayoutTable.OneRowTable(self.lists, self.thisBaseList, self)
        self.table_oneRow.paintTable([self.thisBaseList.IDValue, ])
        self.table_oneRow.setGeometry(15, self.layout_yPosition, 1085, 44)
        self.layout_yPosition += 70

        self.layout_labelStatus(900)
        self.layout_yPosition -= 35

        self.button4 = QPushButton("Přidat", self)
        self.button4.clicked.connect(self.event_button4_addRow)
        self.button4.setGeometry(920, self.layout_yPosition, 180, 22)


    def layout_addRow2(self):
        # Add row: by text fields.
        label1 = QLabel("Přidat nový (2)", self)
        label1.setFont(self.font_h1)
        label1.setGeometry(15, self.layout_yPosition, 1100, 24)
        self.layout_yPosition += 35

        layout_xPosition = 20
        # Create items.
        self.labelP1_0_a = QLabel("-", self)
        self.labelP1_0_b = QLabel("-", self)
        self.array1TLabels = []
        self.array2TextFields = []
        for i1 in range(self.thisBaseList.columnsQuantityUsed):
            # [0] not used.
            # Index of EditText and Labels colide with column index.
            self.array1TLabels.append(QLabel("-", self))
            self.array2TextFields.append(QLineEdit(self))
        # Locate items.
        self.labelP1_0_a.setGeometry(layout_xPosition, self.layout_yPosition, self.thisBaseList.columnsWidth[0] - 12, 20)
        self.labelP1_0_a.setText(self.thisBaseList.columnNames[0])
        self.labelP1_0_b.setGeometry(layout_xPosition, self.layout_yPosition + 25, self.thisBaseList.columnsWidth[0] - 20, 20)
        layout_xPosition += self.thisBaseList.columnsWidth[0]
        for i1 in range(1, self.thisBaseList.columnsQuantityUsed):
            self.array1TLabels[i1].setGeometry(layout_xPosition, self.layout_yPosition, self.thisBaseList.columnsWidth[i1] - 12, 20)
            self.array1TLabels[i1].setText(self.thisBaseList.columnNames[i1])
            self.array2TextFields[i1].setGeometry(layout_xPosition, self.layout_yPosition + 25, self.thisBaseList.columnsWidth[i1] - 20, 20)
            layout_xPosition += self.thisBaseList.columnsWidth[i1]
        # Not used items locate out.
        self.array1TLabels[0].setGeometry(-20, 0, 10, 10)
        self.array2TextFields[0].setGeometry(-20, 0, 10, 10)
        self.layout_yPosition += 60


        self.buttonP1_1 = QPushButton("Přidat (2)", self)
        self.buttonP1_1.clicked.connect(self.event_buttonP1_1_addRow2)
        self.buttonP1_1.setGeometry(920, self.layout_yPosition, 180, 22)


    def layout_addRow_cleanButton(self):
        button1 = QPushButton("Vyčistit", self)
        button1.clicked.connect(self.event_button6)
        button1.setGeometry(15, self.layout_yPosition, 80, 22)


    def layout_tableLastInserted(self, useList=-1):
        if useList == -1:
            useList = self.thisBaseList
            label1 = QLabel("Naposledy přidané (poslední je nahoře):", self)
        else:
            label1 = QLabel("Naposled přidané - list: " + useList.tableName, self)

        label1.setGeometry(15, self.layout_yPosition, 1100, 20)
        self.layout_yPosition += 25

        table_lastInserted = Tables_LayoutTable.LastInsertedTable(self.lists, useList, self)
        table_lastInserted.paintTable()
        self.listOfTablesToActualize_lastInserted.append(table_lastInserted)
        table_lastInserted.setGeometry(15, self.layout_yPosition, 1085, 105)
        self.layout_yPosition += 115


    def layout_editRows(self):
        label1 = QLabel("Úpravy záznamů", self)
        label1.setFont(self.font_h1)
        label1.setGeometry(15, self.layout_yPosition, 1100, 24)
        self.layout_yPosition += 40

        label2 = QLabel("Kopírovat hodnoty z ID:", self)
        label2.setGeometry(15, self.layout_yPosition, 180, 20)

        self.editText1 = QLineEdit(self)
        self.editText1.setGeometry(200, self.layout_yPosition, 80, 20)

        button1 = QPushButton("Kopírovat", self)
        button1.clicked.connect(self.event_button5)
        button1.setGeometry(300, self.layout_yPosition, 120, 22)
        self.layout_yPosition += 35

        label3 = QLabel("Opravit stávající záznam, ID:", self)
        label3.setGeometry(15, self.layout_yPosition, 180, 20)

        self.editText2 = QLineEdit(self)
        self.editText2.setGeometry(200, self.layout_yPosition, 80, 20)

        button2 = QPushButton("Načíst", self)
        button2.clicked.connect(self.event_button7)
        button2.setGeometry(300, self.layout_yPosition, 120, 22)
        self.layout_yPosition += 35

        label4 = QLabel("Smazat záznam, ID:", self)
        label4.setGeometry(15, self.layout_yPosition, 180, 20)

        self.editText3 = QLineEdit(self)
        self.editText3.setGeometry(200, self.layout_yPosition, 80, 20)

        button3 = QPushButton("Smazat", self)
        button3.clicked.connect(self.event_button8)
        button3.setGeometry(300, self.layout_yPosition, 120, 22)
        self.layout_yPosition += 35


    # Events.
    def setDefaultValues1(self):
        """
        Overridden.
        Set default values at inserting table and editTexts, check IDvalue.
        """
        for i1 in range(len(self.thisBaseList.table)):
            if self.thisBaseList.IDValue <= self.thisBaseList.table[i1][0]:
                self.thisBaseList.IDValue = self.thisBaseList.table[i1][0] + 1
        self.setEmptyInsertingRow()
        self.label5.setText("-")
        self.rewriteExistsRow = False
        self.setDefaultValues2()
        self.setDefaultValues3()
        for i2 in self.listOfLabelsToActualize_sumOfRows:
            i2.setText("-")

        self.setColoringTables()


    def setDefaultValues2(self):
        # Set default values at editTexts to edit tables (at bottom of layout).
        self.editText1.setText("")
        self.editText2.setText("")
        self.editText3.setText("")
        self.editText4.setText("")


    def setDefaultValues3(self):
        """
        To be override.
        Additional items in any layout.
        """
        pass


    def refreshTables2(self):
        """
        Overridden.
        """
        self.refreshTables_lastInserted()
        for i1 in self.listOfLabelsToActualize_sumOfRows:
            i1.setText(str(self.thisBaseList.sumOfRows))


    def refreshTables_lastInserted(self):
        for i1 in range(len(self.listOfTablesToActualize_lastInserted)):
            self.listOfTablesToActualize_lastInserted[i1].paintTable()


    def setEmptyInsertingRow(self, row=()):
        if type(row) != list:
            row = []
        if len(row) == 0:
            row.append(self.thisBaseList.IDValue)
        for i1 in range(len(row)):
            row[i1] = str(row[i1])
        row += (self.thisBaseList.columnsQuantityUsed - len(row)) * ["", ]

        self.table_oneRow.paintTable(row)

        self.labelP1_0_b.setText(row[0])
        for i2 in range(1, self.thisBaseList.columnsQuantityUsed):
            self.array2TextFields[i2].setText(row[i2])


    def event_button4_addRow(self):
        # Add values to list from inserting table.
        row = self.table_oneRow.getValues()
        self.event_addRow(row)


    def event_buttonP1_1_addRow2(self):
        # Add values to list from inserting editTexts.
        row = [self.labelP1_0_b.text()]
        for i1 in range(1, self.thisBaseList.columnsQuantityUsed):
            row.append(self.array2TextFields[i1].text())
        self.event_addRow(row)


    def event_addRow(self, row):
        """
        Received row add to list.
        """

        newRow, message = self.thisBaseList.mainTable_appendRow(row[:], self.rewriteExistsRow)
        if message:
            row, message = self.event_addRow_additional1(row, message)
        else:
            newRow2 = []
            if self.rewriteExistsRow:
                message = "Řádek s ID " + str(newRow[0]) + " úspěšně PŘEPSÁN."
                self.rewriteExistsRow = False
            else:
                message = "Řádek s ID " + str(newRow[0]) + " úspěšně přidán."
                self.thisBaseList.IDValue += 1

                # Special functions.
                newRow2, message2 = self.event_addRow_additional2(row, newRow)
                message += message2

            self.setEmptyInsertingRow(newRow2)
            self.refreshTables_lastInserted()

        self.setDefaultValues2()
        self.label5.setText(message)
        return message


    def event_addRow_additional1(self, row, message):
        """
        To be override.
        """
        return [row, message]


    def event_addRow_additional2(self, row, newRow):
        """
        To be override.
        """
        row = []
        message = ""

        return row, message


    # def event_addRow_insertSomeValuesFromLastRow(self, row):
    #     """
    #     To be override.
    #     """
    #     newRow = []
    #     return newRow


    def event_button5(self):
        # Copy values from another row.
        i1 = self.editText1.text()
        try:
            i1 = int(i1)
        except ValueError:
            self.label5.setText("Chyba: nezadali jste číslo.")
            return
        for i2 in range(len(self.thisBaseList.table)):
            if i1 == int(self.thisBaseList.table[i2][0]):
                row_insertionTable = self.thisBaseList.table[i2][:]
                row_insertionTable[0] = str(self.thisBaseList.IDValue)
                self.setEmptyInsertingRow(row_insertionTable)
                self.label5.setText("Hodnoty řádku s ID " + str(i1) + " nakopírovány.")
                return
        self.label5.setText("Problém: ID nenalezeno.")


    def event_button6(self):
        # Clean inserting fields.
        self.rewriteExistsRow = False
        self.setEmptyInsertingRow()
        self.label5.setText("Vkládací políčka vyčištěna.")


    def event_button7(self):
        # Button: rewrite row.
        insertedValue = self.editText2.text()
        try:
            insertedValue = int(insertedValue)
        except ValueError:
            self.label5.setText("Chyba: nezadali jste číslo.")
            return
        for i2 in range(len(self.thisBaseList.table)):
            if insertedValue == int(self.thisBaseList.table[i2][0]):
                self.setEmptyInsertingRow(self.thisBaseList.table[i2][:])
                self.label5.setText("Načteno ID " + str(insertedValue) + ".   POZOR: hodnoty u tohoto ID budou přepsány - opraveny. Jedná se o opravu stávajícího záznamu.")
                self.rewriteExistsRow = True
                return
        self.label5.setText("Problém: ID nenalezeno.")


    def event_button8(self):
        # Button: remove row.
        i1 = self.editText3.text()
        try:
            i1 = int(i1)
        except ValueError:
            self.label5.setText("Problém: nezadali jste číslo.")
            return
        buttonReply = QMessageBox.question(self, "Potvrďte akci", "Opravdu smazat záznam s ID " + str(i1) + "?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            message = self.thisBaseList.mainTable_deleteRow(i1)
            if message:
                self.label5.setText(message)
            else:
                self.label5.setText("Řádek s ID " + str(i1) + " odstraněn.")
                self.editText3.setText("")



class Layout_TableT0(TableAndList):

    def __init__(self, received_lists, received_listTablesLayout, *args, **kwargs):
        super(Layout_TableT0, self).__init__(received_lists, received_listTablesLayout, *args, **kwargs)


    def initializeFirst2(self):
        self.thisList = self.lists.listsOfAllLists[1][0]
        self.thisBaseList = self.lists.listsOfAllLists[0][self.thisList.baseListNumber]


    def placeContent_layout(self):

        self.layout_head()

        self.layout_table(showLabel=False)

        self.layout_labelRowsInTable()
        self.layout_yPosition += 55

        self.layout_addRow1()
        self.layout_yPosition += 35

        self.layout_addRow_cleanButton()
        self.layout_yPosition += 35
        self.layout_yPosition += 55

        self.layout_addRow2()
        self.layout_yPosition += 90

        self.layout_editRows()
        self.layout_findString()
        self.layout_yPosition += 25

        self.layout_bottom()



class Layout_TableT1(TableAndList):

    def __init__(self, received_lists, received_listTablesLayout, *args, **kwargs):
        super(Layout_TableT1, self).__init__(received_lists, received_listTablesLayout, *args, **kwargs)


    def initializeFirst2(self):
        self.thisList = self.lists.listsOfAllLists[1][1]
        self.thisBaseList = self.lists.listsOfAllLists[0][self.thisList.baseListNumber]


    def placeContent_layout(self):

        self.layout_head()

        self.layout_table(showLabel=False)

        self.layout_labelRowsInTable()
        self.layout_yPosition += 55

        self.layout_addRow1()
        self.layout_yPosition += 35

        self.layout_addRow_cleanButton()
        self.layout_yPosition += 35
        self.layout_yPosition += 55

        self.layout_addRow2()
        self.layout_yPosition += 90

        self.layout_tableLastInserted()
        self.layout_yPosition += 75

        self.layout_editRows()
        self.layout_findString()
        self.layout_yPosition += 25

        self.layout_bottom()



class Layout_TableT2(TableAndList):

    def __init__(self, received_lists, received_listTablesLayout, *args, **kwargs):
        super(Layout_TableT2, self).__init__(received_lists, received_listTablesLayout, *args, **kwargs)


    def initializeFirst2(self):
        self.thisList = self.lists.listsOfAllLists[1][2]
        self.thisBaseList = self.lists.listsOfAllLists[0][self.thisList.baseListNumber]


    def placeContent_layout(self):

        self.layout_head()

        self.layout_table(showLabel=False)

        self.layout_labelRowsInTable()
        self.layout_yPosition += 55

        self.layout_addRow1()
        self.layout_yPosition += 35

        self.layout_addRow_cleanButton()
        self.layout_yPosition += 35
        self.layout_yPosition += 55

        self.layout_addRow2()
        self.layout_yPosition += 90

        self.layout_tableLastInserted()
        self.layout_yPosition += 75

        self.layout_editRows()
        self.layout_findString()
        self.layout_yPosition += 25

        self.layout_bottom()



class Layout_TableT3(TableAndList):

    def __init__(self, received_lists, received_listTablesLayout, *args, **kwargs):
        super(Layout_TableT3, self).__init__(received_lists, received_listTablesLayout, *args, **kwargs)


    def initializeFirst2(self):
        self.thisList = self.lists.listsOfAllLists[1][3]
        self.thisBaseList = self.lists.listsOfAllLists[0][self.thisList.baseListNumber]


    def placeContent_layout(self):

        self.layout_head()

        self.layout_table(showLabel=False)

        self.layout_labelRowsInTable()
        self.layout_yPosition += 55

        self.layout_addRow1()
        self.layout_yPosition += 35

        self.layout_addRow_cleanButton()
        self.layout_yPosition += 35
        self.layout_yPosition += 55

        self.layout_addRow2()
        self.layout_yPosition += 90

        self.layout_tableLastInserted()
        self.layout_yPosition += 75

        self.layout_table(self.lists.listsOfAllLists[1][1], 200)
        self.layout_table(self.lists.listsOfAllLists[1][2], 200)
        self.layout_yPosition += 60

        self.layout_editRows()
        self.layout_findString()
        self.layout_yPosition += 25

        self.layout_bottom()



class Layout_TableT4(TableAndList):

    def __init__(self, received_lists, received_listTablesLayout, *args, **kwargs):
        super(Layout_TableT4, self).__init__(received_lists, received_listTablesLayout, *args, **kwargs)


    def initializeFirst2(self):
        self.thisList = self.lists.listsOfAllLists[1][4]
        self.thisBaseList = self.lists.listsOfAllLists[0][self.thisList.baseListNumber]


    def placeContent_layout(self):

        self.layout_head()

        self.layout_table(showLabel=False)

        self.layout_labelRowsInTable()
        self.layout_addRow1()
        self.layout_addRow_cleanButton()
        self.layout_yPosition += 35
        self.layout_addRow2()
        self.layout_tableLastInserted()
        self.layout_editRows()
        self.layout_findString()

        self.layout_bottom()



class Layout_TableT5(TableAndList):

    def __init__(self, received_lists, received_listTablesLayout, *args, **kwargs):
        super(Layout_TableT5, self).__init__(received_lists, received_listTablesLayout, *args, **kwargs)


    def initializeFirst2(self):
        self.thisList = self.lists.listsOfAllLists[1][5]
        self.thisBaseList = self.lists.listsOfAllLists[0][self.thisList.baseListNumber]


    def placeContent_layout(self):

        self.layout_head()

        self.layout_table(showLabel=False)

        self.layout_labelRowsInTable()
        self.layout_yPosition += 55

        self.layout_addRow1()
        self.layout_yPosition += 35

        self.layout_addRow_cleanButton()
        self.layout_yPosition += 35
        self.layout_yPosition += 55

        self.layout_addRow2()
        self.layout_yPosition += 90

        self.layout_tableLastInserted()
        self.layout_yPosition += 75

        self.layout_table(self.lists.listsOfAllLists[1][3], 200)
        self.layout_yPosition += 40

        self.layout_tableLastInserted(self.lists.listsOfAllLists[0][6])
        self.layout_table(self.lists.listsOfAllLists[1][6], 200)
        self.layout_yPosition += 60

        self.layout_editRows()
        self.layout_findString()
        self.layout_yPosition += 25

        self.layout_bottom()


    def event_addRow_additional2(self, row, newRow):
        """
        Overridden.
        Add values into L6.
        """
        message = ""
        if (not self.rewriteExistsRow) and (len(row[6]) > 0 or len(row[7]) > 0 or len(row[8]) > 0):
            row_L6 = [self.lists.listsOfAllLists[0][6].IDValue, row[0], row[6], row[7], row[8]]
            for i1 in range(len(row_L6)):
                row_L6[i1] = str(row_L6[i1])
            receivedMessage = self.listTablesLayout[6][0].event_addRow(row_L6)
            message += "   Vložení do listu L6: " + receivedMessage
        row = []

        return row, message


class Layout_TableT6(TableAndList):

    def __init__(self, received_lists, received_listTablesLayout, *args, **kwargs):
        super(Layout_TableT6, self).__init__(received_lists, received_listTablesLayout, *args, **kwargs)


    def initializeFirst2(self):
        self.thisList = self.lists.listsOfAllLists[1][6]
        self.thisBaseList = self.lists.listsOfAllLists[0][self.thisList.baseListNumber]


    def placeContent_layout(self):

        self.layout_head()

        self.layout_table(showLabel=False)

        self.layout_labelRowsInTable()

        self.layout_stringWithAnyIDs()
        self.layout_yPosition += 55

        self.layout_addRow1()
        self.layout_yPosition += 35

        self.layout_addRow_cleanButton()
        self.layout_yPosition += 35
        self.layout_yPosition += 55

        self.layout_addRow2()
        self.layout_yPosition += 90

        self.layout_tableLastInserted()
        self.layout_yPosition += 75

        self.layout_table(self.lists.listsOfAllLists[1][3], 200)
        self.layout_table(self.lists.listsOfAllLists[1][5], 200)
        self.layout_yPosition += 60

        self.layout_editRows()
        self.layout_findString()
        self.layout_yPosition += 25

        self.layout_bottom()


    # Layout parts.
    def layout_stringWithAnyIDs(self):
        label1 = QLabel("Účastníci z listu '" + self.lists.listsOfAllLists[0][5].tableName + "' bez žádného startovního čísla:", self)
        label1.setGeometry(15, self.layout_yPosition, 320, 20)
        self.label9 = QLabel("-", self)
        self.label9.setGeometry(340, self.layout_yPosition, 760, 20)
        self.layout_yPosition += 35


    def event_addRow_additional1(self, row, message):
        """
        Overridden.
        If add row to L6 during add row to L5, and in L6 had mistake, show values in inserting row.
        """
        self.setEmptyInsertingRow(row)

        return [row, message]


    # Events.
    def refreshTables3(self):
        """
        Overridden.
        """
        self.label9.setText(self.thisBaseList.notAssignedRowsFromIncludedList)



class Layout_TableT7(TableAndList):

    def __init__(self, received_lists, received_listTablesLayout, *args, **kwargs):
        super(Layout_TableT7, self).__init__(received_lists, received_listTablesLayout, *args, **kwargs)


    def initializeFirst2(self):
        self.thisList = self.lists.listsOfAllLists[1][7]
        self.thisBaseList = self.lists.listsOfAllLists[0][self.thisList.baseListNumber]


    def placeContent_layout(self):

        self.layout_head()

        self.layout_table(showLabel=False)

        self.layout_labelRowsInTable()

        self.layout_stringWithAnyIDs()
        self.layout_yPosition += 55

        self.layout_addRow1()
        self.layout_yPosition += 35

        self.layout_addRow_cleanButton()
        self.layout_yPosition += 35

        self.layout_chooseInsertingPreferences()
        self.layout_yPosition += 55

        self.layout_addRow2()
        self.layout_yPosition += 90

        self.layout_tableLastInserted()
        self.layout_yPosition += 75

        self.layout_editRows()
        self.layout_findString()
        self.layout_yPosition += 25

        self.layout_bottom()


    # Layout parts.
    def layout_chooseInsertingPreferences(self):
        # Check box.
        self.checkBox1 = QCheckBox("Kopírovat hodnoty 'závod' a 'čas' z posledního záznamu", self)
        # self.checkBox1.toggle() # This is a QCheckBox constructor.
        self.checkBox1.setChecked(False)
        self.checkBox1.stateChanged.connect(self.event_checkBox1)
        self.checkBox1.setGeometry(15, self.layout_yPosition, 1000, 22)
        self.layout_yPosition += 35

        self.checkBox2 = QCheckBox("Ostřihnout desetinou část u času při přidání řádku, a nezobrazovat ji v tabulkách.", self)
        self.checkBox2.setChecked(False)
        self.checkBox2.stateChanged.connect(self.event_checkBox2)
        self.checkBox2.setGeometry(15, self.layout_yPosition, 1000, 22)
        self.layout_yPosition += 35

        # Radio buttons.
        qgroupbox1 = QGroupBox("Volba hodnot, které zadávat pro identifikaci účastníka ")
        radioButtonsGroup1 = QVBoxLayout()

        self.radioButton0 = QRadioButton("Zadávat pouze 'ID přiřazení účastníka - skupina'")
        # self.radioButton0.toggled.connect(self.event_radioButtonsGroup1)
        radioButtonsGroup1.addWidget(self.radioButton0)
        self.radioButton1 = QRadioButton("Zadávat společně hodnoty 'závod' a 'startovní číslo'")
        radioButtonsGroup1.addWidget(self.radioButton1)
        self.radioButton1.setChecked(True)
        self.radioButton1.toggled.connect(self.event_radioButtonsGroup1)

        radioButtonsGroup1.addStretch()
        qgroupbox1.setLayout(radioButtonsGroup1)

        myStWi = QStackedWidget(self)
        # myStWi.setContentsMargins(10, 10, 10, 10)
        myStWi.addWidget(qgroupbox1)

        myStWi.setGeometry(15, self.layout_yPosition, 1085, 80)
        self.layout_yPosition += 90


    def layout_stringWithAnyIDs(self):
        label1 = QLabel("Záznamy listu '" + self.lists.listsOfAllLists[0][6].tableName + "' bez přiřazeného času:", self)
        label1.setGeometry(15, self.layout_yPosition, 370, 20)
        self.label9 = QLabel("-", self)
        self.label9.setGeometry(400, self.layout_yPosition, 700, 20)
        self.layout_yPosition += 35


    # Events.
    def setDefaultValues3(self):
        """
        Overridden.
        """
        self.checkBox1.setChecked(False)
        self.checkBox2.setChecked(False)
        self.radioButton1.setChecked(True)


    def refreshTables3(self):
        """
        Overridden.
        """
        self.label9.setText(self.thisBaseList.notAssignedRowsFromIncludedList)


    def event_addRow_additional2(self, row, newRow):
        """
        Overridden.
        Insert some values from last row to inserting fields.
        """
        message = ""
        newRow2 = []
        if self.thisBaseList.insertSomeValuesFromLastRow:
            newRow2 = [self.thisBaseList.IDValue, "", "", newRow[3], "", newRow[5][0:7]]

        return newRow2, message


    def event_checkBox1(self, state):
        if state == Qt.Checked:
            self.thisBaseList.insertSomeValuesFromLastRow = True
        else:
            self.thisBaseList.insertSomeValuesFromLastRow = False


    def event_checkBox2(self, state):
        if state == Qt.Checked:
            self.lists.listsOfAllLists[2][2].timeValue_useEndAfterDot = False
            if self.specialExceptSolution_isDisplayedThisLayout: # Bad solution.
                QMessageBox.information(self, "Informace o akci", "Hodnota v políčku 'čas': nyní u nově přidávaných záznamů bude část za desetinným oddělovačem umazána. U stávajících bude zachována, pokud byla zadána, a také bude brána v potaz při seřazení výsledků. Ale nyní vidět v uživatelských tabulkách nebude (na to pozor, pokud tu takové záznamy s desetinou částí již jsou - případně tuto funkci později zase vypněte).", QMessageBox.Ok)
        else:
            self.lists.listsOfAllLists[2][2].timeValue_useEndAfterDot = True
            if self.specialExceptSolution_isDisplayedThisLayout:
                QMessageBox.information(self, "Informace o akci", "Hodnota v políčku 'čas': u přidávaných záznamů bude část za desetinným oddělovačem zachovaána. Dále bude vidět v uživatelských tabulkách.", QMessageBox.Ok)


    def event_radioButtonsGroup1(self):
        if self.radioButton0.isChecked():
            self.thisBaseList.columnsCompulsorion_usedVersion = 0
        elif self.radioButton1.isChecked():
            self.thisBaseList.columnsCompulsorion_usedVersion = 1

        self.thisBaseList.columnsCompulsorion = self.thisBaseList.columnsCompulsorion_versions[self.thisBaseList.columnsCompulsorion_usedVersion]



class Layout_TableT8(Tables_Layout):

    def __init__(self, received_lists, received_listTablesLayout, *args, **kwargs):
        super(Layout_TableT8, self).__init__(received_lists, received_listTablesLayout, *args, **kwargs)


    def initializeFirst2(self):
        self.thisList = self.lists.listsOfAllLists[1][8]
        self.thisBaseList = self.lists.listsOfAllLists[0][self.thisList.baseListNumber]


    def placeContent_layout(self):

        self.layout_head()

        self.layout_table(showLabel=False)
        self.layout_yPosition += 20

        self.layout_findString()

        self.layout_label_foundString()
        self.layout_yPosition += 15

        self.layout_bottom()


    # Layout parts.
    def layout_label_foundString(self):
        label1 = QLabel("Nalezená ID:", self)
        label1.setGeometry(15, self.layout_yPosition, 80, 20)
        self.label5 = QLabel("-", self)
        self.label5.setGeometry(100, self.layout_yPosition, 800, 20)
        self.layout_yPosition += 35


    # Events.
    def setColoringTables(self):
        """
        Set which row to color.
        """
        for i1 in self.listOfTablesToActualize:
            i1.colorRowsCount = 0
            i1.colorClickedRow = self.colorClickedRowInTable



class Layout_TableT9(Tables_Layout):

    def __init__(self, received_lists, received_listTablesLayout, *args, **kwargs):
        super(Layout_TableT9, self).__init__(received_lists, received_listTablesLayout, *args, **kwargs)


    def initializeFirst2(self):
        self.thisList = self.lists.listsOfAllLists[1][10]
        self.thisBaseList = self.lists.listsOfAllLists[0][self.thisList.baseListNumber]


    def placeContent_layout(self):

        self.layout_head()

        self.layout_showWhere()

        self.layout_labelStatus()

        self.layout_L9Label()

        self.layout_table(self.lists.listsOfAllLists[1][9], 44, False)  # TODO:
        self.layout_yPosition += 10

        self.layout_table(height=390, showLabel=False)
        self.layout_yPosition += 30

        self.layout_table(self.lists.listsOfAllLists[1][5], 400)
        self.layout_yPosition += 10

        self.layout_findString()
        self.layout_yPosition += 15

        self.layout_bottom()


    # Layout parts.
    def layout_showWhere(self):
        label1 = QLabel("Zadat ID účastníka:", self)
        label1.setGeometry(15, self.layout_yPosition, 180, 20)

        self.editText5 = QLineEdit(self)
        self.editText5.setGeometry(200, self.layout_yPosition, 100, 20)

        button1 = QPushButton("Zobrazit", self)
        button1.clicked.connect(self.event_button10)
        button1.setGeometry(340, self.layout_yPosition, 80, 22)
        self.layout_yPosition += 35


    def layout_L9Label(self):
        label1 = QLabel("Info účastníka a jeho závody s výsledky:", self)
        label1.setGeometry(15, self.layout_yPosition, 1085, 20)
        self.layout_yPosition += 25


    def layout_findString(self):
        label1 = QLabel("Hledat slovo v tabulce '" + self.lists.listsOfAllLists[1][5].tableName + "':", self)
        label1.setGeometry(15, self.layout_yPosition, 240, 20)

        self.editText4 = QLineEdit(self)
        self.editText4.setGeometry(260, self.layout_yPosition, 80, 20)

        button1 = QPushButton("Najít", self)
        button1.clicked.connect(self.event_button9_findString)
        button1.setGeometry(360, self.layout_yPosition, 120, 22)
        self.layout_yPosition += 35


    # Events.
    def refreshTables3(self):
        """
        Overridden.
        """
        self.lists.listsOfAllLists[1][9].table = self.lists.listsOfAllLists[2][0].emptyList_2DWithLabel


    def event_button10(self):
        # Button, table 9: show one row table with one participant info and participant's results.
        # Paint empty tables.
        self.lists.listsOfAllLists[1][9].table = self.lists.listsOfAllLists[2][0].emptyList_2DWithLabel
        self.thisList.table = self.lists.listsOfAllLists[2][0].emptyList_2DWithLabel
        for i1 in range(len(self.listOfTablesToActualize)):
            self.listOfTablesToActualize[i1].paintTable()

        # Take string from edit text.
        participantID = self.editText5.text()
        try:
            participantID = int(participantID)
        except ValueError:
            self.label5.setText("Problém: nezadali jste číslo.")
            return
        participantID = self.thisList.findValueAtRowWithReceivedValue(participantID, self.lists.listsOfAllLists[0][5].table, 0)
        if type(participantID) != int:
            self.label5.setText("Problém: ID nenalezeno.")
            return

        # Fill tables.
        if not self.lists.checkActualityTables():
            self.lists.fillTablesFromLists()
        self.lists.listsOfAllLists[1][9].fillSingleTableFromList((participantID, 0))
        self.lists.listsOfAllLists[1][10].fillSingleTableFromList((participantID, 1), True)
        for i1 in range(len(self.listOfTablesToActualize)):
            self.listOfTablesToActualize[i1].paintTable()
        self.label5.setText("Zobrazeno.")


    def event_button9_findString(self):
        # Button: find string in user's table.
        self.label5.setText(self.findStringInTable(self.lists.listsOfAllLists[1][5], self.editText4.text()))



class Table_Layout_ScrollArea(QWidget):

    def __init__(self, table_Layout, *args, **kwargs):
        super(Table_Layout_ScrollArea, self).__init__(*args, **kwargs)
        """
        This class perform scrolling screen. I do not know better solution.
        """

        widget = table_Layout
        widget.setMinimumWidth(1125)
        widget.setMinimumHeight(widget.layout_yPosition)

        myStack = QStackedWidget()
        myStack.addWidget(widget)

        scroll = QScrollArea(self)
        scroll.setWidget(myStack)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(622)
        scroll.setFixedWidth(1152)
        scroll.setGeometry(-1, -1, 622, 1152)
