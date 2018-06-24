from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor



class InheretedTable(QTableWidget):
    """
    To be inherit.
    """

    def __init__(self, received_lists, received_thisList, *args):
        super(InheretedTable, self).__init__(*args)
        """
        Received listsTuple: (lists, number of group in listsOfAllLists, number of list in group of listsOfAllLists)
        """
        self.lists = received_lists
        self.thisList = received_thisList

        # Color of rows.
        self.colorRowsCount = 0  # 0, 2, 3 or higher.
        self.colorClickedRow = 1  # 0, 1 or 2.
        self.color_contentDefault = QColor(255, 255, 255)
        self.color_contentClicked = QColor(246, 248, 246)
        self.color_clickedRow = QColor(220, 220, 226)
        self.color_markedRow = QColor(230, 240, 230)
        self.color_lastColoredRow = -1

        self.setColumnCount(self.thisList.columnsQuantityUsed)
        # Set the table headers.
        self.setHorizontalHeaderLabels(self.thisList.columnNames[:self.thisList.columnsQuantityUsed])
        # Set the alignment to the headers.
        for i1 in range(self.thisList.columnsQuantityUsed):
            self.horizontalHeaderItem(i1).setTextAlignment(Qt.AlignLeft)
            self.setColumnWidth(i1, self.thisList.columnsWidth[i1])
        self.verticalHeader().setDefaultSectionSize(20)
        self.verticalHeader().setVisible(False)



class MainTable(InheretedTable):
    """
    Show data from 'table' (2D list).
    """

    def __init__(self, received_lists, received_thisList, *args):
        super(MainTable, self).__init__(received_lists, received_thisList, *args)
        self.table = self.thisList.table
        self.list_numberOfMarkedRows =  self.thisList.list_numberOfMarkedRows


    def paintTable(self):
        """
        Fill table.
        colorRows means number or each row color, if is not 0.
        """

        # Paint empty table, if base list is empty.
        self.table = self.thisList.table
        self.list_numberOfMarkedRows = self.thisList.list_numberOfMarkedRows
        if len(self.table) == 0:
            self.table = self.lists.listsOfAllLists[2][0].emptyList_2DWithLabel

        # Paint data from list (table).
        self.setRowCount(len(self.table))
        for i1 in range(len(self.table)):
            for i2 in range(self.thisList.columnsQuantityUsed):
                self.setItem(i1, i2, QTableWidgetItem(str(self.table[i1][i2])))

        if self.colorRowsCount != 0 and len(self.table) > self.colorRowsCount:
            for j1 in range(0, len(self.table), self.colorRowsCount):
                for j2 in range(self.thisList.columnsQuantityUsed):
                    self.item(j1, j2).setBackground(self.color_contentClicked)

        # Color marked rows.
        if len(self.list_numberOfMarkedRows) > 0:
            for k1 in self.list_numberOfMarkedRows:
                for k2 in range(self.thisList.columnsQuantityUsed):
                    self.item(k1, k2).setBackground(self.color_markedRow)

        self.cellClicked.connect(self.cellWasClicked)


    def cellWasClicked(self, row, column):
        """
        Color row when is clicked.
        """
        if len(self.table) < 2:
            return

        def colorRow(thisRow, color):
            if thisRow in self.list_numberOfMarkedRows:  # Marked rows not recolor.
                return
            for j1 in range(self.thisList.columnsQuantityUsed):
                self.item(thisRow, j1).setBackground(color)

        # if self.colorClickedRow == 0: Do not color.
        if self.colorClickedRow == 1:

            # Last colored row color take back.
            # if self.color_lastColoredRow in self.list_numberOfMarkedRows:  # Marked rows not recolor.
            #     return
            if self.color_lastColoredRow >= 0:
                if self.color_lastColoredRow == row:
                    return
                if self.colorRowsCount != 0 and len(self.table) > 2:
                    if self.color_lastColoredRow == 0 or self.color_lastColoredRow % self.colorRowsCount == 0:
                        recolor = self.color_contentClicked
                    else:
                        recolor = self.color_contentDefault
                else:
                    recolor = self.color_contentDefault
                colorRow(self.color_lastColoredRow, recolor)
                # for i1 in range(self.thisList.columnsQuantityUsed):
                #     self.item(self.color_lastColoredRow, i1).setBackground(color)

            # Color clicked row.
            colorRow(row, self.color_clickedRow)
            self.color_lastColoredRow = row

        elif self.colorClickedRow == 2:
            # Last colored rows keep.
            colorRow(row, self.color_clickedRow)



class OneRowTable(InheretedTable):
    """
    Paint table with one row.
    Table ability to inserting values by user, and get this values.
    """

    def __init__(self, received_lists, received_thisList, *args):
        super(OneRowTable, self).__init__(received_lists, received_thisList, *args)


    def paintTable(self, row):
        """
        Received row must be list and should be contains at least first value.
        """
        if type(row) != list:
            return
        for i2 in range(len(row)):
            row[i2] = str(row[i2])
        row += (self.thisList.columnsQuantityUsed - len(row)) * ["", ]

        self.setRowCount(1)
        for i1 in range(self.thisList.columnsQuantityUsed):
            item = QTableWidgetItem(row[i1])
            if i1 == 0:
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.setItem(0, i1, item)


    def getValues(self):

        # Others cell improve, can be helpful:
        #
        # Get entered value in a cell.
        # self.cellChanged.connect(self.anyMethod)
        # def anyMethod(self):
        #     row = self.currentRow()
        #     col = self.currentColumn()
        #     value = self.item(row, col)
        #     value = value.text() # Output.
        # item = QTableWidgetItem("value")
        # self.form_widget.setCurrentCell(1, 0)
        # self,form_widget.setItem(1, 1, item)

        row = []
        for i1 in range(self.thisList.columnsQuantityUsed):
            item = self.item(0, i1).text()
            if len(item) == 0:
                row.append("")
            else:
                row.append(item)
        return row



class LastInsertedTable(InheretedTable):
    """
    Show data from 'tableLastInserted' (2D list).
    """

    def __init__(self, received_lists, received_thisList, *args):
        super(LastInsertedTable, self).__init__(received_lists, received_thisList, *args)


    def paintTable(self):
        table = self.thisList.tableLastInserted
        if len(table) == 0:
            table = self.lists.listsOfAllLists[2][0].emptyList_2D
        self.setRowCount(len(table))
        columnQuantity = self.thisList.columnsQuantityUsed
        for i1 in range(len(table)):
            if len(table[i1]) < columnQuantity:
                columnQuantity = len(table[i1])
            for i2 in range(columnQuantity):
                self.setItem(len(table) - 1 - i1, i2, QTableWidgetItem(str(table[i1][i2]))) # len(table) - 1 - i1 -> First write last inserted.
