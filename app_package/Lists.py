


class Lists:
    """
    There is created lists with data - all values about races and participants.
    'Lists' contains normalised data, 'Tables' contains rewrited data which users like to see.
    """

    def __init__(self):

        self.isTablesActual = True

        self.listsOfAllLists = []
        self.list_mainLists = []  # Index colide with table number.
        self.list_usersTables = []  # Index usualy colide with table number.
        self.list_accessories = []
        self.list_additionalListsAndTables = []

        # l0_CompetitionInfo = L0_CompetitionInfo(self.listsOfAllLists)
        # l1_Races = L1_Races(self.listsOfAllLists)
        # l2_Categories = L2_Categories(self.listsOfAllLists)
        # l3_GroupsList = L3_GroupsList(self.listsOfAllLists)
        # l4_CommonParticipantNumbers = L4_CommonParticipantNumbers(self.listsOfAllLists)
        # l5_Participants = L5_Participants(self.listsOfAllLists)
        # l6_AssignGroupsToParticipants = L6_AssignGroupsToParticipants(self.listsOfAllLists)
        # l7_Results = L7_Results(self.listsOfAllLists)
        # self.list_mainLists.extend([
        #     l0_CompetitionInfo, l1_Races, l2_Categories, l3_GroupsList, l4_CommonParticipantNumbers, l5_Participants, l6_AssignGroupsToParticipants, l7_Results,
        # ])
        #
        # t0_CompetitionInfo = T0_CompetitionInfo(self.listsOfAllLists)
        # t1_Races = T1_Races(self.listsOfAllLists)
        # t2_Categories = T2_Categories(self.listsOfAllLists)
        # t3_GroupsList = T3_GroupsList(self.listsOfAllLists)
        # t4_CommonParticipantNumbers = T4_CommonParticipantNumbers(self.listsOfAllLists)
        # t5_Participants = T5_Participants(self.listsOfAllLists)
        # t6_AssignGroupsToParticipants = T6_AssignGroupsToParticipants(self.listsOfAllLists)
        # t7_Results = T7_Results(self.listsOfAllLists)
        # t8_ResultsGroup = T8_ResultsGroup(self.listsOfAllLists)
        # t5_Participants_oneParticipant = T5_Participants(self.listsOfAllLists)
        # t9_ResultsParticipants = T9_ResultsParticipants(self.listsOfAllLists)
        # self.list_usersTables.extend([
        #     t0_CompetitionInfo, t1_Races, t2_Categories, t3_GroupsList, t4_CommonParticipantNumbers, t5_Participants, t6_AssignGroupsToParticipants, t7_Results, t8_ResultsGroup, t9_ResultsParticipants, t5_Participants_oneParticipant,
        # ])
        #
        # emptyLists = EmptyLists(self.listsOfAllLists)
        # self.list_accessories.extend([
        #     emptyLists,
        # ])

        self.list_mainLists = [
            L0_CompetitionInfo(self.listsOfAllLists),
            L1_Races(self.listsOfAllLists),
            L2_Categories(self.listsOfAllLists),
            L3_GroupsList(self.listsOfAllLists),
            L4_CommonParticipantNumbers(self.listsOfAllLists),
            L5_Participants(self.listsOfAllLists),
            L6_AssignGroupsToParticipants(self.listsOfAllLists),
            L7_Results(self.listsOfAllLists),
        ]

        self.list_usersTables = [
            T0_CompetitionInfo(self.listsOfAllLists),
            T1_Races(self.listsOfAllLists),
            T2_Categories(self.listsOfAllLists),
            T3_GroupsList(self.listsOfAllLists),
            T4_CommonParticipantNumbers(self.listsOfAllLists),
            T5_Participants(self.listsOfAllLists),
            T6_AssignGroupsToParticipants(self.listsOfAllLists),
            T7_Results(self.listsOfAllLists),
            T8_ResultsGroup(self.listsOfAllLists),  # index 8.
            T5_Participants(self.listsOfAllLists),  # index 9.
            T9_ResultsParticipants(self.listsOfAllLists),  # index 10.
        ]

        self.list_accessories = [
            EmptyArrays(self.listsOfAllLists),
            EmptyList(self.listsOfAllLists),
            CommonVariables(self.listsOfAllLists),
        ]

        self.listsOfAllLists.extend([
            self.list_mainLists,  # Main lists.
            self.list_usersTables,  # User's tables.
            self.list_accessories,
            self.list_additionalListsAndTables,  # Special using tables.
                                ])


    def checkActualityTables(self):
        if not self.isTablesActual:
            return False
        for i1 in range(len(self.listsOfAllLists[1])):
            if not self.listsOfAllLists[1][i1].isTablesActual:
                self.isTablesActual = False
                return False
        return True


    def setTablesIsActual(self):
        self.isTablesActual = True
        for i1 in range(len(self.listsOfAllLists[1])):
            self.listsOfAllLists[1][i1].isTablesActual = True


    def returnStateOfActualityTables(self):
        if self.checkActualityTables():
            return "je aktuální"
        else:
            return "NENI AKTUÁLNÍ"


    def quantityRowsInList(self):
        """
        Determine quantity of rows of each list (main list).
        """
        for i1 in range(len(self.listsOfAllLists[0])):
            self.listsOfAllLists[0][i1].sumOfRows = len(self.listsOfAllLists[0][i1].table)


    def determineUnassignedRowsFromIncludedList(self):
        """
        Compare base lists and determine unassigned rows in both lists.
        """
        listOfTablesAndColumnsNeedToCheck = (
            ((5, 0), (6, 1)),  # L5 -> L6.
            ((6, 0), (7, 1)),  # L6 -> L7.
                                             )
        for i1 in listOfTablesAndColumnsNeedToCheck:
            stringUnassignedRows = ""
            if len(self.listsOfAllLists[0][i1[0][0]].table) > 0:
                for i2 in range(len(self.listsOfAllLists[0][i1[0][0]].table)):
                    hasFound = False
                    for i3 in range(len(self.listsOfAllLists[0][i1[1][0]].table)):
                        if self.listsOfAllLists[0][i1[0][0]].table[i2][i1[0][1]] == self.listsOfAllLists[0][i1[1][0]].table[i3][i1[1][1]]:
                            hasFound = True
                            break
                    if not hasFound:
                        if len(stringUnassignedRows) > 0:
                            stringUnassignedRows = stringUnassignedRows[:-1] + ", "
                        stringUnassignedRows += str(self.listsOfAllLists[0][i1[0][0]].table[i2][i1[0][1]]) + "."
                if len(stringUnassignedRows) == 0:
                    stringUnassignedRows = "Žádné."
            else:
                stringUnassignedRows = "-"
            self.listsOfAllLists[0][i1[1][0]].notAssignedRowsFromIncludedList = stringUnassignedRows


    def fillTablesFromLists(self):
        """
        Fill user's tables.
        """
        self.quantityRowsInList()
        self.determineUnassignedRowsFromIncludedList()

        # Fill each table.
        stringWithProblems = ""
        for i1 in range(len(self.listsOfAllLists[1])):
            if i1 == 9:
                self.listsOfAllLists[1][9].table = []
                continue
            if i1 == 10:
                self.listsOfAllLists[1][10].table = []
                continue
            returnedValue = self.listsOfAllLists[1][i1].fillSingleTableFromList()
            if len(returnedValue) > 0:
                if len(stringWithProblems) == 0:
                    stringWithProblems = "Problémy (tabulka a ID):   " + returnedValue
                else:
                    stringWithProblems += " ;   " + returnedValue
        self.setTablesIsActual()

        if len(stringWithProblems) > 0 and stringWithProblems[-1] != ".":
            stringWithProblems += "."
        return stringWithProblems


    def removeDataFromList_allLists(self):
        for i1 in range(len(self.listsOfAllLists[0])):
            self.listsOfAllLists[0][i1].removeDataFromList(True)
        self.fillTablesFromLists()


    def removeDataFromList_singleList(self, numberOfList):
        self.listsOfAllLists[0][numberOfList].removeDataFromList()



class AbstractList:
    """
    To be inherit.
    Lists and tables property.
    """

    def __init__(self, received_listsOfAllLists):
        self.listsOfAllLists = received_listsOfAllLists
        self.sortAtColumn = 0

        self.tableNumber = -1
        self.tableName = ""
        self.table = []
        self.columnsQuantityUsed = 0
        self.columnNames = ()
        self.columnsWidth = ()  # Suma: 1060 (max).

        # Special variables.
        self.isTablesActual = True
        self.sumOfRows = 0
        self.temp_table_sort = []


    def findValueAtRowWithReceivedValue(self, value, table, findAtColumn, returnFromColumn=0):
        """
        It find value in receiver 2D list 'table'.     # DEL   base list (listsOfAllLists[0][tableNumber].table).
        Received value (and rather also checked values in base table) must not be none or empty (string with length 0).
        Other received values: number of list, number of column where to find received value, return value from column.
        """
        returnValue = False
        if type(table) != list or type(value) == str and len(value) == 0 or type(value) == bool:
            return False
        # try:
        #     value = str(value)
        # except ValueError:
        #     return False
        #table = self.listsOfAllLists[0][tableNumber].table
        if len(table) == 0:
            return False
        # Mistake.
        # if type(value) != type(table[0][findAtColumn]):
        #     return False

        for i1 in range(len(table)):
            if table[i1][findAtColumn] == value:
                return table[i1][returnFromColumn]

        return returnValue


    def getKey(self, item):
        return item[self.sortAtColumn]


    def sortByColumns(self, table, sortAtColumns, sortColumnsBackward=()):
        """
        Received sortAtColumns type is integer, or tuple or list if also sort at more columns.
        """
        if len(table) == 0:
            return
        if type(sortAtColumns) != list and type(sortAtColumns) != tuple:
            return
        if type(sortColumnsBackward) != list and type(sortColumnsBackward) != tuple:
            return
        if len(sortAtColumns) == 0:
            return
        if len(sortColumnsBackward) != 0 and len(sortAtColumns) != len(sortColumnsBackward):
            return
        if len(sortColumnsBackward) == 0:
            sortColumnsBackward = []
            for i1 in range(len(sortAtColumns)):
                sortColumnsBackward.append(False)

        self.sortByColumns_recursive(table, sortAtColumns, 0, len(table), sortColumnsBackward)


    def sortByColumns_recursive(self, table, sortAtColumns, fromRow, toRow, sortColumnsBackward):
        """
        Received sortAtColumns type is tuple or list.
        Received value toRow mean number of row 'without'.
        In every recurse we need sortAtColumns[0]. If is availeble sortAtColumns[1:], use it for next recursion round.
        """
        if fromRow == toRow - 1:
            # If there is only one row.
            return

        # Sort by column sortAtColumns[0].
        self.sortAtColumn = sortAtColumns[0]
        table[fromRow:toRow] = sorted(table[fromRow:toRow], key = self.getKey)

        # Sort backward, if it is required.
        if sortColumnsBackward[0]:
            fromRow_backward = fromRow
            toRow_backward = toRow - 1  # To row 'with'.
            while fromRow_backward < toRow_backward:
                temp_tableRow = table[fromRow_backward]
                table[fromRow_backward] = table[toRow_backward]
                table[toRow_backward] = temp_tableRow

                fromRow_backward += 1
                toRow_backward -= 1

        # Sort by column sortAtColumns[1] - recurse.
        if len(sortAtColumns) > 1 and fromRow < toRow - 1:
            fromRow_2 = fromRow
            for toRow_2 in range(fromRow + 1, toRow):
                if table[fromRow_2][sortAtColumns[0]] != table[toRow_2][sortAtColumns[0]]:
                    self.sortByColumns_recursive(table, sortAtColumns[1:], fromRow_2, toRow_2, sortColumnsBackward[1:])
                    fromRow_2 = toRow_2
            # Sort last group. Because cyclus 'for' can not.
            self.sortByColumns_recursive(table, sortAtColumns[1:], fromRow_2, toRow, sortColumnsBackward[1:])



class Lists_Base(AbstractList):
    """
    To be inherit.
    Customized to 'lists' (L...)
    """

    def __init__(self, received_listsOfAllLists):
        super(Lists_Base, self).__init__(received_listsOfAllLists)

        self.list_columnsRelational = ()  # Main list: ((table, column), ) -> Assign only exist values from table and column.
        self.IDValue = 0
        self.tableLastInserted = []
        self.tableLastInserted_rowsQuantity = 4
        self.columnsType = ()
        self.columnsCompulsorion = ()  # 0 - not compulsory, 100 - compulsory, 0 < value < 100 - compulsory value in one of columns with same number - number meaning number of main column where is needed value - may it be calling 'multiple columns'.
        self.columnsUniqueValue = ()  # 100 - unique, 0 - is not checked to unique, 0 < value < 100 - for columns with same numbers only unique combinations.
        self.uniqueValuesAtAnotherColumnsAndAnotherLists = ()  # ((list, column), ) Must contain also this number of list.

        # Special variables.
        self.insertSomeValuesFromLastRow = False
        self.notAssignedRowsFromIncludedList = "-"
        self.columnsCompulsorion_usedVersion = 0


    def mainTable_appendRow(self, row, rewriteRow):
        # Check, append.
        self.isTablesActual = False
        mistake = False
        row, message = self.checkRow(row, rewriteRow)
        if message:
            return row, message

        if not rewriteRow:
            self.table.append(row[:])
            self.tableLastInserted_append(row)
        else:
            for i1 in range(len(self.table)):
                if row[0] == self.table[i1][0]:
                    self.table[i1] = row[:]
                    self.tableLastInserted_append(row)
                    return row, mistake
            return row, "Chyba: řádek nepřepsán, protože stejné ID nenalezeno."

        return row, mistake


    def mainTable_deleteRow(self, rowID):
        self.isTablesActual = False
        mistake = False
        for i1 in range(len(self.table)):
            if rowID == self.table[i1][0]:
                del self.table[i1]
                return mistake
        return "Problém: ID tohoto řádku nenalezeno."


    def tableLastInserted_append(self, row):
        self.tableLastInserted.append(row)
        if len(self.tableLastInserted) > self.tableLastInserted_rowsQuantity:
            del self.tableLastInserted[0]


    def checkRow(self, row, rewriteRow=False):
        """
        Check and edit or add values at row, who insert user.
        Important is sequenc of functions, they need already checked values by functions before.
        """
        mistake = False
        try:
            if row is None:
                return row, "Chyba programu: přijaté pole (v class Lists)."
            if len(row) < self.columnsQuantityUsed:
                return row, "Chyba programu: přijaté pole (v class Lists)."

            list_functionsCheckingRow = [
                self.checkRow_additional_1,  # Special solution.
                self.checkRow_generalCheck,
                self.checkRow_additional_2,  # Special solution.
                self.checkRow_checkMultipleColumns,
                self.checkRow_addNeededValues,
                self.checkRow_checkUniqueValues,
                self.checkUniqueValueInAnotherLists,
                self.checkRow_additional_3,  # Special solution.
            ]

            for i1 in list_functionsCheckingRow:
                print("checkRow")
                row, message = i1(row, rewriteRow)
                print("checkRow - message", message)
                if message:
                    return row, message

        except Exception:
            return row, "Chyba při kontrole hodnot: Exception - blýže nespecifikovaná výjimka. Zkuste zadat jiné hodnoty. Tato chyba nemá vliv na chod programu, ale příčina mít může."

        return row, mistake


    def checkRow_additional_1(self, row, rewriteRow):
        """
        To be override.
        """
        message = False

        return row, message


    def checkRow_generalCheck(self, row, rewriteRow):
        """
        By cyclus for take every value. Strip values, check forbidden characters, check compulsorion and type of value and exists of relational value.
        """
        message = False

        i1 = 0
        try:
            for i1 in range(self.columnsQuantityUsed):
                # Remove white characters.
                row[i1] = row[i1].strip()

                # Values must not contain ";".
                for i4 in range(len(row[i1])):
                    if row[i1][i4] == ";":
                        return row, "Problém: žádná hodnota nesmí obsahovat středník ';'."

                # Check compulsory of value in column.
                if len(row[i1]) == 0 and self.columnsCompulsorion[i1] == 100:
                    return row, "Problém: vložte hodnotu do kolonky '" + self.columnNames[i1] + "'."
                    # else: # Multiple columns will be checked later.

                # Check value type in column.
                if self.columnsType[i1] == "int":
                    if len(row[i1]) > 0:
                        row[i1] = int(row[i1])

                # Check list_columnsRelational - exists wanted row with inserted value value.
                if len(self.list_columnsRelational) > 0 and len(self.list_columnsRelational[i1]) > 0 and (type(row[i1]) == int or type(row[i1]) == str and len(row[i1]) > 0):
                    value = self.findValueAtRowWithReceivedValue(row[i1], self.listsOfAllLists[0][self.list_columnsRelational[i1][0]].table, self.list_columnsRelational[i1][1])
                    if type(value) == bool and not value:
                        return row, "Problém: k hodnotě v kolonce '" + self.columnNames[i1] + "' nenalezen shodný existující záznam."

        except ValueError:
            return row, "Problém ValueError: špatně zadaná hodnota v kolonce '" + self.columnNames[i1] + "'."

        return row, message


    def checkRow_additional_2(self, row, rewriteRow):
        """
        To be override.
        """
        message = False

        return row, message


    def checkRow_checkMultipleColumns(self, row, rewriteRow):
        """
        Check, if multiple columns contain any value, and if there is more then one values if meaning same information.
        """
        message = False

        # Prepare arrays to next code.
        array_indexsOfMultipleValue = []  # Contain all number of columns with multiple value.
        array_mainColumnNumbersOfMultipleValue = []  # Contain numbers of main columns of multiple value, every number ones.
        for i1 in range(self.columnsQuantityUsed):
            if 0 < self.columnsCompulsorion[i1] < 100:
                array_indexsOfMultipleValue.append(i1)
                if not self.columnsCompulsorion[i1] in array_mainColumnNumbersOfMultipleValue:
                    array_mainColumnNumbersOfMultipleValue.append(self.columnsCompulsorion[i1])

        # Check.
        for j1 in array_mainColumnNumbersOfMultipleValue:
            # If contains any value.
            isFoundAnyValue = False
            for j2 in array_indexsOfMultipleValue:
                if self.columnsCompulsorion[j2] == j1 and (type(row[j2]) == str and len(row[j2]) > 0 or type(row[j2]) == int):  # If is value int type, it is not empty. (type(row[j2]) == str and len(row[j2]) > 0 or type(row[j2]) == int)
                    isFoundAnyValue = True
                    break
            if not isFoundAnyValue:
                # Value not found. Print warning with column names where to be added any value.
                columnNamesOfMultipleValue = ""
                for j3 in array_indexsOfMultipleValue:
                    if self.columnsCompulsorion[j3] == j1:
                        if len(columnNamesOfMultipleValue) > 0:
                            columnNamesOfMultipleValue += ", "
                        columnNamesOfMultipleValue += "'" + self.columnNames[j3] + "'"
                return row, "Problém: vložte hodnotu do jedné z kolonek: " + columnNamesOfMultipleValue + "."
            # Value equals of same information.
            baseIDValue = ""
            baseIDValue_columnName = ""
            for j4 in array_indexsOfMultipleValue:
                if j1 == self.columnsCompulsorion[j4] and not (type(row[j4]) == str and len(row[j4]) == 0):
                    if type(baseIDValue) == str and len(baseIDValue) == 0:
                        baseIDValue = self.findValueAtRowWithReceivedValue(row[j4], self.listsOfAllLists[0][self.list_columnsRelational[j4][0]].table, self.list_columnsRelational[j4][1])
                        baseIDValue_columnName = self.columnNames[j4]
                    elif baseIDValue != self.findValueAtRowWithReceivedValue(row[j4], self.listsOfAllLists[0][self.list_columnsRelational[j4][0]].table, self.list_columnsRelational[j4][1]):
                        return row, "Problém: hodnoty v kolonkách '" + baseIDValue_columnName + "' a '" + self.columnNames[j4] + "' neodkazují na stejný řádek."

        return row, message


    def checkRow_addNeededValues(self, row, rewriteRow):
        """
        Add needed values at multiple columns.
        """
        message = False

        if len(self.list_columnsRelational) > 0:
            for i1 in range(self.columnsQuantityUsed):
                if type(row[i1]) == str and len(row[i1]) == 0 and len(self.list_columnsRelational[i1]) != 0 and 0 < self.columnsCompulsorion[i1] < 100:
                    for i2 in range(self.columnsQuantityUsed):
                        if self.columnsCompulsorion[i1] == self.columnsCompulsorion[i2] and not (type(row[i2]) == str and len(row[i2]) == 0):
                            if len(self.list_columnsRelational[i2]) == 2:
                                row[i1] = self.findValueAtRowWithReceivedValue(row[i2], self.listsOfAllLists[0][self.list_columnsRelational[i2][0]].table, self.list_columnsRelational[i2][1], self.list_columnsRelational[i1][1])
                                if type(row[i1]) == bool and type(row[i1]) == False:
                                    return row, "Chyba: nenalezen záznam v tabulce, na který odkazuje zadaná hodnota v kolonce '" + self.columnNames[i2] + "'."
                            break

        return row, message


    def checkRow_checkUniqueValues(self, row, rewriteRow):
        """
        Check unique values and unique combinations.
        """
        message = False

        # Check unique values.
        if len(self.columnsUniqueValue) > 0:
            list_uniqueCombination_groupsNumbers = []
            for i1 in range(self.columnsQuantityUsed):
                if rewriteRow and i1 == 0:
                    # if editRow: ID already exists.
                    continue
                if self.columnsUniqueValue[i1] == 100:
                    foundValue = self.findValueAtRowWithReceivedValue(row[i1], self.table, i1)
                    if type(foundValue) != bool and not (rewriteRow and foundValue == row[0]):
                        return row, "Problém: hodnota v kolonce '" + self.columnNames[i1] + "' je již použita, vložte jinou."
                elif self.columnsUniqueValue[i1] > 0:
                    if not self.columnsUniqueValue[i1] in list_uniqueCombination_groupsNumbers:
                        list_uniqueCombination_groupsNumbers.append(self.columnsUniqueValue[i1])

            # Unique combination.
            for i2 in list_uniqueCombination_groupsNumbers:
                list_uniqueCombination_positions = []
                for i3 in range(self.columnsQuantityUsed):
                    if i2 == self.columnsUniqueValue[i3]:
                        list_uniqueCombination_positions.append(i3)
                for i4 in range(len(self.table)):
                    isUnique = True
                    for i5 in range(len(list_uniqueCombination_positions)):
                        if row[list_uniqueCombination_positions[i5]] == self.table[i4][
                            list_uniqueCombination_positions[i5]]:
                            isUnique = False
                        else:
                            isUnique = True
                            break
                    if not isUnique and not (rewriteRow and row[0] == self.table[i4][0]):
                        uniqueColumnNames = ""
                        for i6 in range(len(list_uniqueCombination_positions)):
                            if i6 > 0:
                                uniqueColumnNames += ", "
                            uniqueColumnNames += "'" + self.columnNames[list_uniqueCombination_positions[i6]] + "'"
                        return row, "Problém: tato kombinace hodnot je již použita (v těchto kolonkách smí být pouze unikátní kombinace hodnot: " + uniqueColumnNames + ")."

        return row, message


    def checkUniqueValueInAnotherLists(self, row, rewriteRow):
        """
        Check unique values in multiple columns and multiple lists.
        Actually checked value skip checking of same column in same table - it is already checked or there do not must be unique value in this column.
        """
        message = False

        if len(self.uniqueValuesAtAnotherColumnsAndAnotherLists) > 0:
            # Determine which columns in this row need check.
            list_columnAtThisRow = []
            for i1 in self.uniqueValuesAtAnotherColumnsAndAnotherLists:
                if i1[0] == self.tableNumber:
                    list_columnAtThisRow.append(i1[1])

            # Check values at this row.
            if len(list_columnAtThisRow) > 1:
                for i2 in range(len(list_columnAtThisRow)):
                    for i3 in range(len(list_columnAtThisRow) - 1, -1, -1):
                        if i2 == i3:
                            break
                        if row[list_columnAtThisRow[i2]] == row[list_columnAtThisRow[i3]]:
                            return row, "Problém: názevy v kolonkách '" + self.columnNames[list_columnAtThisRow[i2]] + "' a '" + self.columnNames[list_columnAtThisRow[i3]] + "' nesmí být stejné."

            # Check values of each table and column.
            for j1 in range(len(list_columnAtThisRow)):
                for j2 in self.uniqueValuesAtAnotherColumnsAndAnotherLists:
                    if self.tableNumber == j2[0] and list_columnAtThisRow[j1] == j2[1]:
                        continue  # Skip same column in same table.
                    foundSameValue = self.findValueAtRowWithReceivedValue(row[list_columnAtThisRow[j1]], self.listsOfAllLists[0][j2[0]].table, j2[1])
                    if type(foundSameValue) != bool and not (rewriteRow and j2[0] == self.tableNumber and type(foundSameValue) == int and foundSameValue == row[0]):
                        # Do not retrun, if it is same value at row with same ID in same table (rewriteRow).
                        return row, "Problém: název v kolonce '" + self.columnNames[list_columnAtThisRow[j1]] + "' je již použit někde jinde. Zvolte jiný."

        return row, message


    def checkRow_additional_3(self, row, rewriteRow):
        """
        To be override.
        """
        message = False

        return row, message


    def timeValue_checkFormat(self, row, position):
        """
        Time value format: "hhh:mm:ss.ddd".
        """
        message = False
        emptyTimeValue = "000:00:00.000"
        returnProblemString = "Problém: špatně zadaná hodnota času (formát)."
        value = row[position]

        # Check characters. After cyclus for there be only numerics, colons and dot.
        for i1 in range(len(value)):
            if value[i1] == ":":
                pass
            elif value[i1] == "-":
                value = value[:i1] + ":" + value[i1 + 1:]
            elif value[i1] == ".":
                pass
            elif value[i1] == ",":
                value = value[:i1] + "." + value[i1 + 1:]
            else:
                try:
                    int(value[i1])
                except ValueError:
                    return row, returnProblemString + " Nepodporavané znaky."
        # Check format.
        # Return problem, because user maybe something forgot.
        if value[-1] == ":" or value[-1] == ".":
            return row, returnProblemString + " Nechybí doplnit hodnotu na konci?"
        if value[0] == ":" or value[0] == ".":  # Check if is first character number.
            return row, returnProblemString + " První znak musí být číslice."
        # Check positions of colons and dots.
        hasDot = False
        hasDD = False
        for i2 in range(len(value) - 1, -1, -1):
            if value[i2] == ".":
                if hasDot:
                    return row, returnProblemString + " Smí být pouze jeden desetinný oddělovač."
                hasDot = True
                if hasDD:
                    return row, returnProblemString + " Za desetinným oddělovačem nesmí být dvojtečka."
                # value += "0" * (3 - (len(value) - i2 - 1))  # Add zeros to end.
                if len(value) != i2 + 4:  # Compulsorion of 3 digits after dot, because if another count, user maybe something forgot or mistake.
                    return row, returnProblemString + " Desetinná část musí obsahovat tři číslice."
            if value[i2] == ":":
                hasDD = True
        if not hasDot:
            value += ".000"
        if not self.listsOfAllLists[2][2].timeValue_useEndAfterDot:
            value = value[:-3] + "000"

        # Check format of numbers and colons.
        # Note: string is checked, before dot contains only numerics and colons. First character is numerics.
        # Check positions of numerics and colons. Edit format.
        # Check position of last colon and quantity of numerics characters.
        if len(value) > len(emptyTimeValue):
            return row, returnProblemString + " Hodnota je příliš dlouhá."
        if value[-5] == ":":
            return row, returnProblemString
        if len(value) > 5 and value[-6] == ":":
            return row, returnProblemString
        if len(value) > 6 and value[-7] != ":":
            return row, returnProblemString
        if len(value) > 9 and value[-10] != ":":
            return row, returnProblemString
        # Check colon and numerics characters: second colons only third character after.
        for i4 in range(1, len(value) - 6):
            if value[i4] == ":":
                if value[i4 + 1] == ":" or value[i4 + 2] == ":":
                    return row, returnProblemString
                if i4 < (len(value) - 10):
                    return row, returnProblemString
        if len(value) > 10 and value[-10] != ":":
            return row, returnProblemString

        # Add begining of value.
        value = emptyTimeValue[:-len(value)] + value

        # Check sexagesimal numbers.
        if int(value[4]) > 5 or int(value[7]) > 5:
            return row, returnProblemString + " Neodpovídá šedesátkové soustavě formátu času."

        row[position] = value

        return row, message


    def removeDataFromList(self, setDefaultID=False):
        self.table = []
        if setDefaultID:
            self.IDValue = 0
        self.tableLastInserted = []
        self.isTablesActual = False



class Tables_Users(AbstractList):
    """
    To be inherit.
    Customized to 'tables' (T...)
    """

    def __init__(self, received_listsOfAllLists):
        super(Tables_Users, self).__init__(received_listsOfAllLists)

        self.baseListNumber = -1  # Take values from list number ...
        self.table_columnsRelational = ()  # User's table: (('take' column,   'use in' table, 'and' column, 'take' column,   'use in' table, 'and' column, 'take' column,   ...), ) -> Way to find wanted value.
        self.list_numberOfMarkedRows = []


    def fillSingleTableFromList(self, fillWhere=(), passNotFoundValues=False):
        """
        Method to fill 'user's table' by data ftom 'main list'.

        fillWhere: [value, column in this table, next three numbers - table, column where find value, return value from column].
        """
        print("|||||||  thisListNumber", self.tableNumber)
        baseList_table = self.listsOfAllLists[0][self.baseListNumber].table

        self.table = []
        self.list_numberOfMarkedRows = []
        stringWithProblems = ""
        # Check, if base table is empty.
        if len(baseList_table) == 0:
            return ""

        self.anyFunction1()

        # Rewrite data to table.
        for i1 in range(len(baseList_table)):
            if len(fillWhere) > 1:
                valueWhere = baseList_table[i1][fillWhere[1]]
                hasFound = True
                for i6 in range(2, len(fillWhere), 3):
                    hasFound = False
                    table3 = self.listsOfAllLists[0][fillWhere[i6]].table
                    for i7 in range(len(table3)):
                        if table3[i7][fillWhere[i6 + 1]] == valueWhere:
                            valueWhere = table3[i7][fillWhere[i6 + 2]]
                            hasFound = True
                            break
                if valueWhere != fillWhere[0] or not hasFound:
                    continue
            row = []
            for i2 in range(self.columnsQuantityUsed):
                value = ""
                hadValueFound = True
                try:
                    # Take value from base list.
                    columnsRelational_innerTuple = self.table_columnsRelational[i2]
                    value = baseList_table[i1][columnsRelational_innerTuple[0]]

                    # Take value from relational way.
                    for i4 in range(1, len(columnsRelational_innerTuple), 3):
                        table2 = self.listsOfAllLists[0][columnsRelational_innerTuple[i4]].table
                        hadValueFound = False
                        for i5 in range(len(table2)):
                            if table2[i5][columnsRelational_innerTuple[i4 + 1]] == value:
                                value = table2[i5][columnsRelational_innerTuple[i4 + 2]]
                                hadValueFound = True
                                break

                    # Special except solution:
                    # Edit time value - do not show end.
                    if self.baseListNumber == 7 and columnsRelational_innerTuple[0] == 5 and not self.listsOfAllLists[2][2].timeValue_useEndAfterDot:
                        value = value[:-4]

                except Exception:
                    hadValueFound = False
                # Report if value not found.
                if not hadValueFound:
                    if not passNotFoundValues:
                        value = "(hodnota nenalezena)"
                        if len(stringWithProblems) == 0:
                            stringWithProblems = "T" + str(self.tableNumber) + ": " + str(baseList_table[i1][0]) + "."
                        elif str(baseList_table[i1][0]) != stringWithProblems[-1]:
                            stringWithProblems = stringWithProblems[:-1] + ", " + str(baseList_table[i1][0]) + "."
                    else:
                        value = "-"
                row.append(value)
            self.table.append(row)

        if len(stringWithProblems) > 0:
            return stringWithProblems

        # Sort.
        self.sortTable()

        return stringWithProblems


    def sortTable(self):
        """
        Can be override.
        """
        self.sortByColumns(self.table, (0, ))


    def anyFunction1(self):
        """
        To be override.
        """
        pass



# 'T' - Main list.
# 'L' - User's table.
class L0_CompetitionInfo(Lists_Base):
    # List with info.
    def __init__(self, received_listsOfAllLists):
        super(L0_CompetitionInfo, self).__init__(received_listsOfAllLists)

        self.tableNumber = 0
        self.tableName = "L0 Info"
        self.columnsQuantityUsed = 3
        self.columnNames = ("ID", "Info", "Priorita pořadí")
        self.columnsType = ("int", "str", "int") + 17 * ("str", )
        self.columnsCompulsorion = (100, 0, 100) + 17 * (0, )
        self.columnsUniqueValue = (100, 0, 100) + 17 * (0, )
        self.columnsWidth = (40, 980, 40) + 17 * (100, )


class T0_CompetitionInfo(Tables_Users):
    # Races list.
    def __init__(self, received_listsOfAllLists):
        super(T0_CompetitionInfo, self).__init__(received_listsOfAllLists)

        self.tableNumber = 0
        self.tableName = "T0 Info"
        self.baseListNumber = 0
        self.columnsQuantityUsed = 3
        self.columnNames = ("ID", "Info", "Priorita pořadí")
        self.table_columnsRelational = ((0, ), (1, ), (2, ))
        self.columnsWidth = (40, 980, 40)


    def sortTable(self):
        """
        Overridden.
        """
        self.sortByColumns(self.table, (2, ))


class L1_Races(Lists_Base):
    # Races list.
    def __init__(self, received_listsOfAllLists):
        super(L1_Races, self).__init__(received_listsOfAllLists)

        self.tableNumber = 1
        self.tableName = "L1 Závody"
        self.columnsQuantityUsed = 7
        self.columnNames = ("ID", "Název závodu", "Info", "Priorita pořadí", "Skupina společných startovních čísel", "Poznámka #1", "Poznámka #2")
        self.columnsType = ("int", "str", "str", "int") + 3 * ("str", )
        self.columnsCompulsorion = (100, 100, 100, 100) + 3 * (0, )
        self.columnsUniqueValue = (100, 100, 0, 100) + 3 * (0, )
        self.columnsWidth = (40, 80, 180, 80, 80, 180, 180)
        self.uniqueValuesAtAnotherColumnsAndAnotherLists = ((1, 1), (1, 4), (2, 1), (3, 5))


class T1_Races(Tables_Users):
    # Races list.
    def __init__(self, received_listsOfAllLists):
        super(T1_Races, self).__init__(received_listsOfAllLists)

        self.tableNumber = 1
        self.tableName = "T1 Závody"
        self.baseListNumber = 1
        self.columnsQuantityUsed = 7
        self.columnNames = ("ID", "Název závodu", "Info", "Priorita pořadí", "Skupina polečných startovních čísel", "Poznámka #1", "Poznámka #2")
        self.table_columnsRelational = ((0, ), (1, ), (2, ), (3, ), (4, ), (5, ), (6, ))
        self.columnsWidth = (40, 80, 180, 80, 80, 180, 180)


    def sortTable(self):
        """
        Overridden.
        """
        self.sortByColumns(self.table, (3, ))


class L2_Categories(Lists_Base):
    # Categories list.
    def __init__(self, received_listsOfAllLists):
        super(L2_Categories, self).__init__(received_listsOfAllLists)

        self.tableNumber = 2
        self.tableName = "L2 Kategorie"
        self.columnsQuantityUsed = 6
        self.columnNames = ("ID", "Název kategorie", "Info", "Priorita pořadí", "Poznámka #1", "Poznámka #2")
        self.columnsType = ("int", "str", "str", "int") + 2 * ("str", )
        self.columnsCompulsorion = (100, 100, 100, 100) + 2 * (0, )
        self.columnsUniqueValue = (100, 100) + 4 * (0, )
        self.columnsWidth = (40, 80, 180, 80, 180, 180)
        self.uniqueValuesAtAnotherColumnsAndAnotherLists = ((1, 1), (1, 4), (2, 1), (3, 5))


class T2_Categories(Tables_Users):
    #
    def __init__(self, received_listsOfAllLists):
        super(T2_Categories, self).__init__(received_listsOfAllLists)

        self.tableNumber = 2
        self.tableName = "T2 Kategorie"
        self.baseListNumber = 2
        self.columnsQuantityUsed = 6
        self.columnNames = ("ID", "Název kategorie", "Info", "Priorita pořadí", "Poznámka #1", "Poznámka #2")
        self.table_columnsRelational = ((0, ), (1, ), (2, ), (3, ), (4, ), (5, ))
        self.columnsWidth = (40, 80, 180, 80, 180, 180)


    def sortTable(self):
        """
        Overridden.
        """
        self.sortByColumns(self.table, (3, ))


class L3_GroupsList(Lists_Base):
    # Assign categories to races (let it be call groups).
    def __init__(self, received_listsOfAllLists):
        super(L3_GroupsList, self).__init__(received_listsOfAllLists)

        self.tableNumber = 3
        self.tableName = "L3 Skupiny závod-kategorie"
        self.columnsQuantityUsed = 9
        self.columnNames = ("ID", "L1 ID závodu", "L1 Název závodu", "L2 ID kategorie", "L2 Název kategorie", "Název skupiny", "Info", "Poznámka #1", "Poznámka #2")
        self.columnsType = ("int", "int", "str", "int", "str") + 4 * ("str", )
        self.columnsCompulsorion = (100, 2, 2, 4, 4, 100) + 3 * (0, )
        self.list_columnsRelational = ((), (1, 0), (1, 1), (2, 0), (2, 1)) + 4 * ((), )
        self.columnsUniqueValue = (100, 1, 0, 1, 0, 100) + 3 * (0, )
        self.columnsWidth = (40, 80, 120, 80, 120, 180, 180, 120, 120)
        self.uniqueValuesAtAnotherColumnsAndAnotherLists = ((1, 1), (1, 4), (2, 1), (3, 5))


class T3_GroupsList(Tables_Users):
    #
    def __init__(self, received_listsOfAllLists):
        super(T3_GroupsList, self).__init__(received_listsOfAllLists)

        self.tableNumber = 3
        self.tableName = "T3 Skupiny závod-kategorie"
        self.baseListNumber = 3
        self.columnsQuantityUsed = 12
        self.columnNames = ("ID", "L1 Skupina polečných startovních čísel", "L1 ID závodu", "L1 Název závodu", "L2 ID kategorie", "L2 Název kategorie", "Název skupiny", "Info", "poznámka #1", "poznámka #2", "L1 Priorita pořadí", "L2 Priorita pořadí")
        self.table_columnsRelational = ((0, ), (1, 1, 0, 4), (1, ), (1, 1, 0, 1), (3, ), (3, 2, 0, 1), (5, ), (6, ), (7, ), (8, ), (1, 1, 0, 3), (3, 2, 0, 3))
        self.columnsWidth = (40, 120, 80, 120, 80, 120, 120, 120, 120, 120, 40, 40)


    def sortTable(self):
        """
        Overridden.
        """
        self.sortByColumns(self.table, (10, 11))


class L4_CommonParticipantNumbers(Lists_Base):
    # L4: Reserved for "Skupina společných startovních čísel". Not used.
    def __init__(self, received_listsOfAllLists):
        super(L4_CommonParticipantNumbers, self).__init__(received_listsOfAllLists)

        self.tableNumber = 4
        self.tableName = "L4 Společná startovní čísla"
        self.columnsQuantityUsed = 2
        self.columnNames = ("ID", "-")
        self.columnsType = 2 * ("str", )
        self.columnsCompulsorion = 2 * (0, )
        self.columnsUniqueValue = 2 * (0, )
        self.columnsWidth = (40, 120)


class T4_CommonParticipantNumbers(Tables_Users):
    # Not used.
    def __init__(self, received_listsOfAllLists):
        super(T4_CommonParticipantNumbers, self).__init__(received_listsOfAllLists)

        self.tableNumber = 4
        self.tableName = "T4 Společná startovní čísla"
        self.baseListNumber = 4
        self.columnsQuantityUsed = 2
        self.columnNames = ("ID", "-")
        self.table_columnsRelational = ((0, ), (1, ))
        self.columnsWidth = (40, 120)


class L5_Participants(Lists_Base):
    # Participations list.
    def __init__(self, received_listsOfAllLists):
        super(L5_Participants, self).__init__(received_listsOfAllLists)

        self.tableNumber = 5
        self.tableName = "L5 Účastníci"
        self.columnsQuantityUsed = 11
        self.columnNames = ("ID", "Příjmení", "Jméno", "Klub / team / obec / skupina", "Pohlaví", "Rok narození", "ID skupiny (bude přepsáno do L6)", "Název skupiny (bude přepsáno do L6)", "Startovní číslo (bude přepsáno do L6)", "Poznámka #1", "Poznámka #2")
        self.columnsType = ("int", "str", "str", "str", "str", "int") + 5 * ("str", )
        self.columnsCompulsorion = (100, 100, 100,  0, 100, 100) + 5 * (0, )
        self.columnsUniqueValue = (100, ) + 10 * (0, )
        self.columnsWidth = (40, 120, 120, 120, 80, 80, 80, 120, 80, 60, 60)


    def checkRow_additional_1(self, row, rewriteRow):
        """
        Overridden.
        Romove values belong to L6.
        """
        message = False
        row[6] = ""
        row[7] = ""
        row[8] = ""

        return row, message


    def checkRow_additional_2(self, row, rewriteRow):
        """
        Overridden.
        """
        mistake = False

        # In list number L3 check team column.
        column_L3_team = 3
        if len(row[column_L3_team]) == 0:
            row[column_L3_team] = "-"
        # In list number L3 need to check and edit gender column. Input: m, M / f, F, z, Z, ž, Ž. Output: M / F
        column_L3_gender = 4
        list_maleCharacters = ("m", "M")
        list_femaleCharacters = ("f", "F", "z", "Z", "ž", "Ž")
        if len(row[column_L3_gender]) != 1 or not ( row[column_L3_gender] in list_maleCharacters or row[column_L3_gender] in list_femaleCharacters):
            return row, "Problém: hodnota v kolonce '" + self.columnNames[column_L3_gender] + "' musí obsahovat jednu z těchto hodnot: m, M / f, F, z, Z, ž, Ž"
        if row[4] in list_maleCharacters:
            row[4] = "M"
        else:
            row[4] = "F"

        return row, mistake


class T5_Participants(Tables_Users):
    #
    def __init__(self, received_listsOfAllLists):
        super(T5_Participants, self).__init__(received_listsOfAllLists)

        self.tableNumber = 5
        self.tableName = "T5 Účastníci"
        self.baseListNumber = 5
        self.columnsQuantityUsed = 8
        self.columnNames = ("ID", "Příjmení", "Jméno", "Klub / team / obec / skupina", "Pohlaví", "Rok narození", "Poznámka #1", "Poznámka #2")
        self.table_columnsRelational = ((0, ), (1, ), (2, ), (3, ), (4, ), (5, ), (9, ), (10, ))
        self.columnsWidth = (40, 120, 120, 120, 80, 80, 80, 80)


    def sortTable(self):
        """
        Overridden.
        """
        self.sortByColumns(self.table, (5, 4, 1, 2, 0), (False, True, False, False, False))


class L6_AssignGroupsToParticipants(Lists_Base):
    #
    def __init__(self, received_listsOfAllLists):
        super(L6_AssignGroupsToParticipants, self).__init__(received_listsOfAllLists)

        self.tableNumber = 6
        self.tableName = "L6 Přiřazení účastník - skupina"
        self.columnsQuantityUsed = 5
        self.columnNames = ("ID", "L5 ID účastníka", "L3 ID skupiny", "L3 Název skupiny", "Startovní číslo")
        self.columnsType = ("int", "int", "int") + 2 * ("str", )
        self.columnsCompulsorion = (100, 100, 2, 2, 100)
        self.list_columnsRelational = ((), (5, 0), (3, 0), (3, 5)) + 1 * ((), )
        self.columnsUniqueValue = (100, ) + 4 * (0, )
        self.columnsWidth = (40, 80, 80, 120, 120)


    def checkRow_additional_3(self, row, rewriteRow):
        """
        Overridden.
        Unique participants ("ID účastníka") and participant numbers ("Startovní číslo") in races ("Název závodu") and in participant numbers groups ("Skupina společných startovních čísel").
        """
        mistake = False

        checkParticipantNumbers_raceID = self.findValueAtRowWithReceivedValue(row[2], self.listsOfAllLists[0][3].table, 0, 1)
        checkParticipantNumbers_groupOfNumbers = self.findValueAtRowWithReceivedValue(checkParticipantNumbers_raceID, self.listsOfAllLists[0][1].table, 0, 4)
        if type(checkParticipantNumbers_raceID) == bool or type(checkParticipantNumbers_groupOfNumbers) == bool:
            return row, "Chyba: nenalezen závod (L1 ID závodu " + checkParticipantNumbers_raceID + ") odpovídající zadané 'ID skupině' (kontrola jedinečnosti 'Startovních čísel' pro daný závod)."
        for m1 in range(len(self.table)):
            list_uniqueValues_checkColumns = (1, 4)
            for m2 in list_uniqueValues_checkColumns:
                if row[m2] == self.table[m1][m2] and not (rewriteRow and row[0] == self.table[m1][0]):
                    checkParticipantNumbers_raceID_toCompare = self.findValueAtRowWithReceivedValue(self.table[m1][2], self.listsOfAllLists[0][3].table, 0, 1)
                    if type(checkParticipantNumbers_raceID_toCompare) == bool:
                        if m2 == 1:
                            return row, "Chyba: nenalezena skupina (L2 ID závodu " + self.table[m1][
                                2] + ") odpovídající zadané 'ID skupině' (kontrola jedinečnosti 'účastníků' pro daný závod)."
                        elif m2 == 4:
                            return row, "Chyba: nenalezena skupina (L2 ID závodu " + self.table[m1][
                                2] + ") odpovídající zadané 'ID skupině' (kontrola jedinečnosti 'Startovních čísel' pro daný závod)."
                    checkParticipantNumbers_group_toCompare = self.findValueAtRowWithReceivedValue(checkParticipantNumbers_raceID_toCompare, self.listsOfAllLists[0][1].table, 0, 4)
                    if type(checkParticipantNumbers_group_toCompare) == bool:
                        if m2 == 1:
                            return row, "Chyba: nenalezen závod (L0 ID závodu " + checkParticipantNumbers_group_toCompare + ") odpovídající závodu ve skupině v tabulce L2 (kontrola jedinečnosti 'účastníků' pro daný závod)."
                        elif m2 == 4:
                            return row, "Chyba: nenalezen závod (L0 ID závodu " + checkParticipantNumbers_group_toCompare + ") odpovídající závodu ve skupině v tabulce L2 (kontrola jedinečnosti 'Startovních čísel' pro daný závod)."
                    if checkParticipantNumbers_raceID_toCompare == checkParticipantNumbers_raceID:
                        if m2 == 1:
                            return row, "Problém: v tomto 'závodě' je již tento 'účastník' přiřazen."
                        elif m2 == 4:
                            return row, "Problém: zadejte jiné 'Startovní číslo', protože toto již existuje v tomto 'závodě'."
                    elif len(checkParticipantNumbers_group_toCompare) > 0 and len(
                            checkParticipantNumbers_groupOfNumbers) > 0 and checkParticipantNumbers_group_toCompare == checkParticipantNumbers_groupOfNumbers:
                        if m2 == 1:
                            return row, "Problém: ve stejné 'Skupině společných startovních čísel' je již tento 'účastník' přiřazen."
                        elif m2 == 4:
                            return row, "Problém: zadejte jiné 'Startovní číslo', protože toto již existuje ve stejné 'Skupině společných startovních čísel'."

        return row, mistake

class T6_AssignGroupsToParticipants(Tables_Users):
    #
    def __init__(self, received_listsOfAllLists):
        super(T6_AssignGroupsToParticipants, self).__init__(received_listsOfAllLists)

        self.tableNumber = 6
        self.tableName = "T6 Přiřazení účastník - skupina"
        self.baseListNumber = 6
        self.columnsQuantityUsed = 13
        self.columnNames = ("ID", "L5 ID účastníka", "Příjmení", "Jméno", "Klub / team / obec / skupina", "Pohlaví", "Rok narození", "Startovní číslo", "L3 ID skupiny (závod-kategorie)", "L3 Název skupiny (závod-kategorie)", "L3 Info", "L1 Název závodu", "L2 Název kategorie")
        self.table_columnsRelational = ((0, ), (1, ), (1, 5, 0, 1), (1, 5, 0, 2), (1, 5, 0, 3), (1, 5, 0, 4), (1, 5, 0, 5), (4, ), (2, ), (2, 3, 0, 5), (2, 3, 0, 6), (2, 3, 0, 1, 1, 0, 1), (2, 3, 0, 3, 2, 0, 1))
        self.columnsWidth = (40, 40, 120, 120, 120, 40, 80, 80, 80, 120, 120, 80, 80)


    def sortTable(self):
        """
        Overridden.
        """
        self.sortByColumns(self.table, (6, 5, 2, 3, 1), (False, True, False, False, False))


class L7_Results(Lists_Base):
    # Results of participants.
    # In basic - add result to list L6. Important values in this list is 'L6 ID' and result.
    def __init__(self, received_listsOfAllLists):
        super(L7_Results, self).__init__(received_listsOfAllLists)

        self.tableNumber = 7
        self.tableName = "L7 Všechny výsledky"
        self.columnsQuantityUsed = 12
        self.columnNames = ("ID", "L6 ID přiřazení účastníka a skupiny", "L1 ID závodu (bude zjištěno L0 ID)", "L1 Název závodu (bude zjištěno L0 ID)", "L6 Startovní číslo (bude zjištěno L6 ID)", "Čas", "Korekce", "Zařadit", "Poznámka #1", "Poznámka #2", "Umístění v kategorii", "Umístění v závodě")
        self.columnsType = ("int", "int", "int", "str", "str", "str", "int", "int") + 4 * ("str", )
        self.columnsCompulsorion = 12 * (0, )
        self.list_columnsRelational = ((), (6, 0), (1, 0), (1, 1), (6, 4)) + 7 * ((), )
        self.columnsUniqueValue = (100, 100) + 10 * (0, )
        self.columnsWidth = (40, 80, 80, 140, 140, 140, 80, 80, 80, 80, 0, 0)

        self.columnsCompulsorion_versions = (
                                           (100, 100, 0, 0, 0, 100) + 14 * (0, ), # Special mode: usualy not used, because during inserting results "L6 ID" is not known.
                                           (100, 0, 1, 1, 100, 100) + 14 * (0, ), # Different races has same or similar values of "Startovní číslo" - need also "ID závodu".
        )
        self.columnsCompulsorion_usedVersion = 1
        self.columnsCompulsorion = self.columnsCompulsorion_versions[self.columnsCompulsorion_usedVersion]


    def checkRow_additional_2(self, row, rewriteRow):
        """
        Overridden.
        """
        mistake = False

        # To list L7 user can add result with another race ID (or name) from same 'racer numbers group' ("Skupina společných startovních čísel") (assigned at table L0, 5ht column).
        list7ColumnNumber_IDParticipantAndRaceNumber = 1
        list7ColumnNumber_raceID = 2
        list7ColumnNumber_raceName = 3
        list7ColumnNumber_participantRaceNumber = 4

        if self.columnsCompulsorion_usedVersion == 1 and (type(row[list7ColumnNumber_raceID]) == int or len(row[list7ColumnNumber_raceName]) > 0) and len(row[list7ColumnNumber_participantRaceNumber]) > 0:
            # In this case, it need values from positions in row [list7ColumnNumber_participantRaceNumber] and ([list7ColumnNumber_raceID] and / or [list7ColumnNumber_raceName]).

            # First, determine race ID and "Skupina společných startovních čísel", where will be finding "Startovní číslo".
            row_raceID = row[list7ColumnNumber_raceID]
            row_raceName = row[list7ColumnNumber_raceName]
            if type(row_raceID) == int and len(row_raceName) > 0:
                row_raceID_toCompareMultipleColumns = self.findValueAtRowWithReceivedValue(row_raceName, self.listsOfAllLists[0][1].table, 1)
                if type(row_raceID_toCompareMultipleColumns) != int or row_raceID != row_raceID_toCompareMultipleColumns:
                    return row, "Problém: hodnoty v kolonkách '" + self.columnNames[list7ColumnNumber_raceID] + "' a '" + self.columnNames[list7ColumnNumber_raceName] + "' neodkazují na stejný řádek."
            elif len(row_raceName) > 0:
                row_raceID = self.findValueAtRowWithReceivedValue(row_raceName, self.listsOfAllLists[0][1].table, 1)
            elif row_raceID == int:
                row_raceName = self.findValueAtRowWithReceivedValue(row_raceID, self.listsOfAllLists[0][1].table, 0, 1)
            else:
                return row, "vložte hodnotu do jedné z kolonek: '" + self.columnNames[list7ColumnNumber_raceID] + "', nebo '" + self.columnNames[list7ColumnNumber_raceName] + "'."
            if type(row_raceID) == bool or type(row_raceName) == bool:
                return row, "Problém: k hodnotě v kolonkách 'identifikece závodu' nenalezen shodný existující záznam."
            row_raceID_participantNumbersGroup = self.findValueAtRowWithReceivedValue(row_raceID, self.listsOfAllLists[0][1].table, 0, 4)
            if type(row_raceID_participantNumbersGroup) != str:
                return row, "Problém: k hodnotě v kolonkách 'identifikece závodu' nenalezen shodný existující záznam."

            # Second, take all equals 'participants numbers' and check to same 'racer numbers group'. If find 'participants numbers' in same 'racer numbers group' it is ok.
            for i3 in range(len(self.listsOfAllLists[0][6].table)):
                if self.listsOfAllLists[0][6].table[i3][4] == row[4]:
                    toCompare_raceID = self.findValueAtRowWithReceivedValue(self.listsOfAllLists[0][6].table[i3][2], self.listsOfAllLists[0][3].table, 0, 1)
                    if type(toCompare_raceID) == bool and not toCompare_raceID:
                        return row, "Chyba: nenalezen záznam z tabulky 'L2', který by odpovídal záznamu z tabulky 'L4' (ID " + self.listsOfAllLists[0][6].table[i3][0] + ")"
                    toCompare_participantNumbersGroup = self.findValueAtRowWithReceivedValue(toCompare_raceID, self.listsOfAllLists[0][1].table, 0, 4)
                    if type(toCompare_participantNumbersGroup) != str:
                        return row, "Chyba: nenalezen záznam z tabulky 'L0', který by odpovídal záznamu z tabulky 'L2' (závod s ID " + toCompare_raceID + ")"
                    if row_raceID == toCompare_raceID or len(row_raceID_participantNumbersGroup) > 0 and len(
                            toCompare_participantNumbersGroup) > 0 and row_raceID_participantNumbersGroup == toCompare_participantNumbersGroup:
                        row[list7ColumnNumber_IDParticipantAndRaceNumber] = self.listsOfAllLists[0][6].table[i3][0]
                        row[list7ColumnNumber_raceID] = toCompare_raceID
                        row_raceName_new = self.findValueAtRowWithReceivedValue(toCompare_raceID, self.listsOfAllLists[0][1].table, 0, 1)
                        if type(row_raceName_new) == bool:
                            return row, "Chyba: nenalezen název závodu v listu L1."
                        row[list7ColumnNumber_raceName] = row_raceName_new
                        break

        return row, mistake


    def checkRow_additional_3(self, row, rewriteRow):
        """
        Overridden.
        """
        mistake = False

        # In list number L5 check time value - format.
        column_L5_time = 5
        column_L5_timeCorrection = 6
        column_L5_classify = 7

        row, returnedValue = self.timeValue_checkFormat(row, column_L5_time)
        if type(returnedValue) == str and len(returnedValue) > 0:
            return row, returnedValue

        # Check time correction.
        if type(row[column_L5_timeCorrection]) == str:
            row[column_L5_timeCorrection] = 0
        if not (-1 < row[column_L5_timeCorrection] < 1000):
            return row, "Problém: hodnota v kolonce '" + self.columnNames[column_L5_timeCorrection] + "' musí být celé číslo mezi 0 a 999 včetně."

        # Check and edit value at classify column (value meaning if include this row during sorting).
        if row[column_L5_classify] != 0:
            row[column_L5_classify] = 1

        # Remove last two values.
        row[9] = ""
        row[10] = ""

        return row, mistake


class T7_Results(Tables_Users):
    #
    def __init__(self, received_listsOfAllLists):
        super(T7_Results, self).__init__(received_listsOfAllLists)

        self.tableNumber = 7
        self.tableName = "T7 Všechny výsledky"
        self.baseListNumber = 7
        self.columnsQuantityUsed = 23
        self.columnNames = ("ID", "L6 ID přiřazení účastníka a skupiny", "L1 ID závodu", "L1 Název závodu", "L2 ID kategorie", "L2 Název kategorie", "L3 ID skupiny", "L6 Startovní číslo", "Čas", "Korekce", "Zařadit", "L7 #1 poznámka", "L7 #2 poznámka", "Umístění v kategorii", "Umístění v závodě", "L5 ID účastníka", "Příjmení", "Jméno", "Klub / team / obec / skupina", "Pohlaví", "Rok narození", "L5 #1 poznámka", "L5 #2 poznámka")
        self.table_columnsRelational = ((0, ), (1, ), (1, 6, 0, 2, 3, 0, 1), (1, 6, 0, 2, 3, 0, 1, 1, 0, 1), (1, 6, 0, 2, 3, 0, 3), (1, 6, 0, 2, 3, 0, 3, 2, 0, 1), (1, 6, 0, 2), (1, 6, 0, 4), (5, ), (6, ), (7, ), (8, ), (9, ), (10, ), (11, ), (1, 6, 0, 1), (1, 6, 0, 1, 5, 0, 1), (1, 6, 0, 1, 5, 0, 2), (1, 6, 0, 1, 5, 0, 3), (1, 6, 0, 1, 5, 0, 4), (1, 6, 0, 1, 5, 0, 5), (1, 6, 0, 1, 5, 0, 9), (1, 6, 0, 1, 5, 0, 10))
        self.columnsWidth = (40, 40, 40, 100, 40, 100, 40, 60, 100, 40, 40, 80, 80, 80, 80, 40, 120, 120, 120, 60, 60, 80, 80)


    def anyFunction1(self):
        """
        Overridden.
        To list L7 add emplacements of results.
        """
        sort_baseList = self.listsOfAllLists[0][7]  # Create temp table to sort by time in each group.
        if len(sort_baseList.table) > 1:
            # User's table do not sort.
            # Here edit base list.

            # Add emplacement by time and correction.
            sort_baseList.temp_table_sort = []  # [ID, is classify, time, correction, priorityRace, race emplacement, priorityCategory, category emplacement].

            for j1 in range(len(sort_baseList.table)):
                classify =  sort_baseList.table[j1][7]  # This sort backward.

                time = sort_baseList.table[j1][5]

                time = time[:3] + time[4:6] + time[7:9] + time[10:13]
                time = int(time)

                correction = sort_baseList.table[j1][6]

                temp_groupID = sort_baseList.findValueAtRowWithReceivedValue(sort_baseList.table[j1][1], self.listsOfAllLists[0][6].table, 0, 2)
                temp_raceID = sort_baseList.findValueAtRowWithReceivedValue(temp_groupID, self.listsOfAllLists[0][3].table, 0, 1)
                priorityRace = sort_baseList.findValueAtRowWithReceivedValue(temp_raceID, self.listsOfAllLists[0][1].table, 0, 3)

                temp_categoryID = sort_baseList.findValueAtRowWithReceivedValue(temp_groupID, self.listsOfAllLists[0][3].table, 0, 3)
                priorityCategory = sort_baseList.findValueAtRowWithReceivedValue(temp_categoryID, self.listsOfAllLists[0][2].table, 0, 3)

                sort_baseList.temp_table_sort.append([sort_baseList.table[j1][0], classify, time, correction, priorityRace, "", priorityCategory, ""])


            def sortAndAddEmplacement(sortColumns, sortColumns_backward, emplacementColumn):
                """
                Sort temp_table_sort to group by received sortColumns and also by classify [1], time [2] and correction [3], add emplacement to this groups.

                sortColumns: sequence of number of main columns to sort in temp_table_sort.
                sortColumns_backward: list with same positions like sortColumns, contains if sort backward.
                emplacementColumn: number of column in [main list, temp sorted list], where need to add emplacement.
                """
                # Sort list.
                columns_classifyAndTimeAndCorrerction = (1, 2, 3)
                sortByColumns = () + sortColumns + columns_classifyAndTimeAndCorrerction
                columns_classifyAndTimeAndCorrerction_backward = (True, self.listsOfAllLists[2][2].sortTimeAndCorrectionBackwards, self.listsOfAllLists[2][2].sortTimeAndCorrectionBackwards)
                sortByColumns_backward = () + sortColumns_backward + columns_classifyAndTimeAndCorrerction_backward
                self.sortByColumns(sort_baseList.temp_table_sort, sortByColumns, sortByColumns_backward)

                # temp_table_sort: add race emplacement.
                # Write to first row.
                if sort_baseList.temp_table_sort[0][columns_classifyAndTimeAndCorrerction[0]] == 1:
                    sort_baseList.temp_table_sort[0][emplacementColumn[1]] = 1
                else:
                    sort_baseList.temp_table_sort[0][emplacementColumn[1]] = 100001
                # Write value to main list.
                for j3 in range(len(sort_baseList.table)):
                    if sort_baseList.table[j3][0] == sort_baseList.temp_table_sort[0][0]:
                        sort_baseList.table[j3][emplacementColumn[0]] = sort_baseList.temp_table_sort[0][emplacementColumn[1]]
                        break

                # Write to other rows.
                for j2 in range(1, len(sort_baseList.temp_table_sort)):
                    if sort_baseList.temp_table_sort[j2 - 1][sortColumns[0]] == sort_baseList.temp_table_sort[j2][sortColumns[0]] and \
                            (len(sortColumns) <= 1 or len(sortColumns) > 1 and sort_baseList.temp_table_sort[j2 - 1][sortColumns[1]] == sort_baseList.temp_table_sort[j2][sortColumns[1]]) and \
                            sort_baseList.temp_table_sort[j2 - 1][columns_classifyAndTimeAndCorrerction[0]] == sort_baseList.temp_table_sort[j2][columns_classifyAndTimeAndCorrerction[0]]:
                        sort_baseList.temp_table_sort[j2][emplacementColumn[1]] = sort_baseList.temp_table_sort[j2 - 1][emplacementColumn[1]] + 1
                    else:
                        if sort_baseList.temp_table_sort[j2][columns_classifyAndTimeAndCorrerction[0]] == 1:
                            sort_baseList.temp_table_sort[j2][emplacementColumn[1]] = 1
                        else:
                            sort_baseList.temp_table_sort[j2][emplacementColumn[1]] = 100001
                    # Write value to main list.
                    for j3 in range(len(sort_baseList.table)):
                        if sort_baseList.table[j3][0] == sort_baseList.temp_table_sort[j2][0]:
                            sort_baseList.table[j3][emplacementColumn[0]] = sort_baseList.temp_table_sort[j2][emplacementColumn[1]]
                            break

            # temp_table_sort: sort by: priorityRace, is classify, recomputedTime.
            sortAndAddEmplacement((4,), (False, ), (11, 5))

            # temp_table_sort: sort by: priorityRace, priorityCategory, is classify, recomputedTime.
            sortAndAddEmplacement((4, 6), (False, False), (10, 7))


class T8_ResultsGroup(Tables_Users):
    # Only to assemble from others lists.
    def __init__(self, received_listsOfAllLists):
        super(T8_ResultsGroup, self).__init__(received_listsOfAllLists)

        self.tableNumber = 8
        self.tableName = "T8 Výsledky jednotlivých skupin"
        self.baseListNumber = 7
        self.columnsQuantityUsed = 21
        self.columnNames = ("L7 ID", "Název závodu", "Název kategorie", "ID skupiny", "Název skupiny", "Startovní číslo", "Čas", "Korekce", "Umístění v kategorii", "Umístění v závodě", "ID účastníka", "Příjmení", "Jméno", "Klub / team / obec / skupina", "Pohlaví", "Rok narození", "Zařadit", "L7 #1 poznámka", "L7 #2 poznámka", "L1 Priorita pořadí", "L2 Priorita pořadí")
        self.table_columnsRelational = ((0, ), (1, 6, 0, 2, 3, 0, 1, 1, 0, 1), (1, 6, 0, 2, 3, 0, 3, 2, 0, 1), (1, 6, 0, 2), (1, 6, 0, 2, 3, 0, 5), (1, 6, 0, 4), (5, ), (6, ), (10, ), (11, ), (1, 6, 0, 1), (1, 6, 0, 1, 5, 0, 1), (1, 6, 0, 1, 5, 0, 2), (1, 6, 0, 1, 5, 0, 3), (1, 6, 0, 1, 5, 0, 4), (1, 6, 0, 1, 5, 0, 5), (7, ), (8, ), (9, ), (1, 6, 0, 2, 3, 0, 1, 1, 0, 3), (1, 6, 0, 2, 3, 0, 3, 2, 0, 3))
        self.columnsWidth = (40, 100, 100, 40, 100, 60, 100, 60, 80, 80, 40, 120, 120, 120, 60, 60, 60, 120, 120, 40, 40)


    def addNamesBeforeGroups(self, tableLength, valueAtPosition):
        for i1 in range(2):
            tableLength, valueAtPosition = self.insertEmptyRow(tableLength, valueAtPosition)

        raceInfo = self.findValueAtRowWithReceivedValue(self.table[valueAtPosition][1], self.listsOfAllLists[0][1].table, 1, 2)
        categoryInfo = self.findValueAtRowWithReceivedValue(self.table[valueAtPosition][2], self.listsOfAllLists[0][2].table, 1, 2)
        insertRow = ["", raceInfo, "", "", categoryInfo] + (self.columnsQuantityUsed - 5) * ["", ]
        self.table.insert(valueAtPosition, insertRow)
        self.list_numberOfMarkedRows.append(valueAtPosition)
        tableLength += 1
        valueAtPosition += 1

        return tableLength, valueAtPosition


    def insertEmptyRow(self, tableLength, valueAtPosition):
        insertRow = self.columnsQuantityUsed * ["", ]
        self.table.insert(valueAtPosition, insertRow)
        tableLength += 1
        valueAtPosition += 1

        return tableLength, valueAtPosition


    def sortTable(self):
        """
        Sort by races, categories and emplacement. Split to groups by races and categories, add empty rows and labels.
        """
        if len(self.table) == 0:
            return
        tableLength = len(self.table)
        valueAtPosition = 0

        # Group by race and category - by priority and sort by results (emplacement), between groups add empty row and row with race names.
        self.sortByColumns(self.table, (19, 20, 16, 8), (False, False, True, False))
        # Insert first row with names (because cyclus for can not).
        tableLength, valueAtPosition = self.addNamesBeforeGroups(tableLength, valueAtPosition)
        valueAtPosition += 1
        # Insert other names.
        while valueAtPosition < tableLength:
            if self.table[valueAtPosition][3] != self.table[valueAtPosition - 1][3]:
                tableLength, valueAtPosition = self.addNamesBeforeGroups(tableLength, valueAtPosition)
            valueAtPosition += 1

        # Add to end.
        for i3 in range(2):
            tableLength, valueAtPosition = self.insertEmptyRow(tableLength, valueAtPosition)
        # thisList.table.append(thisList.columnsQuantityUsed * ["", ])


class T9_ResultsParticipants(Tables_Users):
    # User's table: to show results of single participant.
    def __init__(self, received_listsOfAllLists):
        super(T9_ResultsParticipants, self).__init__(received_listsOfAllLists)

        self.tableNumber = 9
        self.tableName = "T9 Výsledky jednotlivých účastníků"
        self.baseListNumber = 6
        self.columnsQuantityUsed = 14
        self.columnNames = ("L6 ID", "L7 ID", "Název závodu", "Název kategorie", "ID skupiny", "Název skupiny", "Startovní číslo", "Čas", "Korekce", "Umístění v kategorii", "Umístění v závodě", "Zařadit", "L7 #1 poznámka", "L7 #2 poznámka")
        self.table_columnsRelational = ((0, ), (0, 7, 1, 0), (2, 3, 0, 1, 1, 0, 1), (2, 3, 0, 3, 2, 0, 1), (2, ), (2, 3, 0, 5), (0, 7, 1, 4, ), (0, 7, 1, 5, ), (0, 7, 1, 6, ), (0, 7, 1, 10, ), (0, 7, 1, 11, ), (0, 7, 1, 7, ), (0, 7, 1, 8, ), (0, 7, 1, 9, ))
        self.columnsWidth = (40, 40, 120, 120, 40, 120, 80, 100, 40, 80, 80, 40, 80, 80)


    def sortTable(self):
        """
        Overridden.
        """
        self.sortByColumns(self.table, (0, ))


class EmptyArrays:

    def __init__(self, received_listsOfAllLists):

        self.listsOfAllLists = received_listsOfAllLists

        self.emptyRow = 30 * ("", )
        self.emptyList_2D = (30 * ("", ), )
        self.emptyList_2DWithLabel = (("(empty)", ) + 29 * ("", ), )


class EmptyList(AbstractList):

    def __init__(self, received_listsOfAllLists):
        super(EmptyList, self).__init__(received_listsOfAllLists)

        self.tableName = "---- Empty list."


class CommonVariables:

    def __init__(self, received_listsOfAllLists):
        listsOfAllLists = received_listsOfAllLists

        self.timeValue_useEndAfterDot = True
        self.sortTimeAndCorrectionBackwards = False
