from time import gmtime, strftime



class ImportExport:

    def __init__(self, received_lists):

        self.lists = received_lists
        self.idMark = "RunnersLists-export"
        self.splitMark = ";"
        self.wrapMark = "_"


    def importData(self, filePath):
        message = ""
        self.lists.removeDataFromList_allLists()
        if filePath:
            if filePath[-4:] != ".txt" and filePath[-4:] != ".csv":
                return "Problém: nepodporovaná přípona souboru."

            with open(filePath) as fp:
                currentTableNumber = -1

                line = fp.readline()
                line = line.strip()
                if line:
                    if len(line) != len(self.idMark):
                        return "Požadovaný soubor neni validní - nesouhlasí první řádek."
                    if line != self.idMark:
                        return "Požadovaný soubor neni validní - nesouhlasí první řádek."

                line = fp.readline()
                while line:
                    line = line.strip()
                    if line:
                        if 2 <= len(line) <= 3 and line[0] == "L" and line[1].isalnum():
                            try:
                                currentTableNumber = int(line[1:])
                            except ValueError:
                                return "Požadovaný soubor neni validní - nesouhlasí identifikační značka Lx. Načtení přerušeno."
                        # elif len(line) > 2 and currentTableNumber >= 0 and line[0] == self.wrapMark and 47 < ord(line[1]) < 58:
                        elif len(line) > 2 and currentTableNumber >= 0 and 47 < ord(line[0]) < 58:
                            try:
                                self.appendRowToTable(self.lists.listsOfAllLists[0][currentTableNumber], line)
                            except ValueError:
                                return "Chyba: ValueError, u některé z hodnot, (někde kolem listu L" + str(currentTableNumber) + ", ID " + str(self.lists.listsOfAllLists[0][currentTableNumber].table[len(self.lists.listsOfAllLists[0][currentTableNumber].table) - 1][0] + 1) + "(+)). Načtení přerušeno."
                            except Exception:
                                return "Chyba: u některé z hodnot, (někde kolem listu L" + str(currentTableNumber) + ", ID " + str(self.lists.listsOfAllLists[0][currentTableNumber].table[len(self.lists.listsOfAllLists[0][currentTableNumber].table) - 1][0] + 1) + "(+)). Načtení přerušeno."

                    line = fp.readline()
                    message = "Soubor načten. Aktualizujte tabulky."

        return message


    def appendRowToTable(self, myList, line):
        row = line.split(self.splitMark)
        for i1 in range(len(row)):
            # row[i1] = row[i1].strip(self.wrapMark)
            if myList.columnsType[i1] == "int" and len(row[i1]) > 0:
                row[i1] = int(row[i1])
        if myList.IDValue <= int(row[0]):
            myList.IDValue = int(row[0]) + 1
        myList.table.append(row)


    def exportData_all(self, filePath):
        """
        Write data from lists into file.
        First row in file contains identification mark, second date and time of created.
        Before every table datas is describing and identification rows of any table.
        List data must begin by numeric character, other rows must not.
        """
        message = ""
        if filePath:
            # Check file name.
            for i1 in range(len(filePath) - 1, 0, -1):
                if filePath[i1] == ".":
                    fileEnd = ""
                    for i2 in range(i1 + 1, len(filePath)):
                        fileEnd += filePath[i2]
                    if fileEnd != "txt" and fileEnd != "csv":
                        filePath = filePath[:i1] + ".txt"
                    break
                if filePath[i1] == "\\" or filePath[i1] == "/" or i1 == 1:
                    filePath += ".txt"
                    break

            # Write to file.
            outFile = None
            try:
                outFile = open(filePath, "w")
                outFile.write(self.idMark + "\n")
                outFile.write("Date, time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
                outFile.write("\n\n")

                for i1 in range(len(self.lists.listsOfAllLists[0])):
                    self.writeTableToFile(outFile, self.lists.listsOfAllLists[0][i1])
            finally:
                if outFile is not None:
                    outFile.close()
            message = "Soubor uložen."

        return message


    def writeTableToFile(self, outFile, myList):
        outFile.write(myList.tableName[:2] + "\n")
        outFile.write(myList.tableName + "\n")

        columnsString = ""
        for i3 in range(myList.columnsQuantityUsed):
            if i3 > 0:
                columnsString += self.splitMark
            columnsString += myList.columnNames[i3]
        outFile.write(columnsString + "\n")

        for i1 in range(len(myList.table)):
            row = ""
            for i2 in range(len(myList.table[i1])):
                if i2 > 0:
                    row += self.splitMark
                # row += self.wrapMark + str(myList.table[i1][i2]) + self.wrapMark
                row += str(myList.table[i1][i2])
            outFile.write(row)
            outFile.write("\n")

        outFile.write("\n\n")


    def writeTableToFile_results(self, outFile):
        """
        Methot targeted to export human readable table to CSV file.
        """
        # Write competition info from L0.
        listWithInfo = self.lists.listsOfAllLists[1][0]
        outFile.write("Info o soutěži:" + "\n\n")
        for i4 in listWithInfo.table:
            outFile.write(i4[1] + "\n")
        outFile.write("\n\n\n")

        # Write results.
        listWithResults = self.lists.listsOfAllLists[1][8]
        outFile.write("Výsledky:" + "\n\n")
        # Write column names.
        columnsString = ""
        for i3 in range(1, listWithResults.columnsQuantityUsed):
            if i3 > 1:
                columnsString += ";"
            columnsString += listWithResults.columnNames[i3]
        outFile.write(columnsString + "\n")

        # Write table content.
        for i1 in range(len(listWithResults.table)):
            row = ""
            for i2 in range(1, len(listWithResults.table[i1])):
                if i2 > 1:
                    row += ";"
                row += str(listWithResults.table[i1][i2])
            outFile.write(row)
            outFile.write("\n")

        outFile.write("\n\n\n")


    def exportData_T8(self, filePath):
        message = ""
        if filePath:
            # Check file name.
            for i1 in range(len(filePath) - 1, 0, -1):
                if filePath[i1] == ".":
                    fileEnd = ""
                    for i2 in range(i1 + 1, len(filePath)):
                        fileEnd += filePath[i2]
                    if fileEnd != "txt" and fileEnd != "csv":
                        filePath = filePath[:i1] + ".csv"
                    break
                if filePath[i1] == "\\" or filePath[i1] == "/" or i1 == 1:
                    filePath += ".csv"
                    break

            # Write to file.
            outFile = None
            try:
                outFile = open(filePath, "w")
                outFile.write("Seřazené výsledky." + "\n")
                outFile.write("Tabulka výsledků účastníků roztříděných podle závodů a kategorií, a seřazených podle času." + "\n")
                outFile.write("Datum a čas exportu: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
                outFile.write("\n\n\n")

                self.writeTableToFile_results(outFile)
            finally:
                if outFile is not None:
                    outFile.close()
            message = "Soubor uložen."

        return message
