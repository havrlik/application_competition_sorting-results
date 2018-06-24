import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox
from PyQt5.QtCore import QSize, Qt

from app_package import Lists, MainHome_Layout, Help_Layout, Tables_Layout, ImportExport_Layout

# Created by Matous on 23.01.2018. Code need this library: 'PyQt5'.
# Application ability to sort participants and their results in race or competition.
# Application, where you can insert races and categories, and participans with race numbers. After inserting results it automatically sort in each category.
# My first Python application. Writed during learning Python, and I know, thats bad code in all cases. Code has not reviewed by more experienced developers.
# User's language is czech. For right understanding to this code and application performance rather use also czech language, because user labels are actualy only in czech language.

# TODO:
# Zkontrolovat, zda nejde přiřadit jednoho účastníka do více závodů patřící do stejné skupiny startovních čísel.
# Přepsat nápis tlažítka pro vkládání záznamů pří opravě záznamu z 'přidat' na 'přepsat'.
# Při zadávání do L7 do skupiny závodu společných startovních čísel: kromě jména závodu můžu zadat i jméno skupiny?
# Udělat testy.
# Možnost vkládat do výsledků jiné hodnoty než čas ( třeba vzdálenost).
# Možnost pozměnit ID, aby bylo možné vytvářet záznamy paralelně a offline na více počítačích. Nebo i online.
# Jak řešit pořadí účastníků se stejným časem? Nepřiřadit jim stejné umístění?
# Combo napovídající hodnoty pro relační políčka.
# Export do PDF.
# Překontrolovat všechny hodnoty v listech.



class AA_Main(QMainWindow):
    """
    Stack with most of screens (layouts / widgets), contains switching listeners between them.
    """

    def __init__(self, *args, **kwargs):
        super(AA_Main, self).__init__(*args, **kwargs)

        font = self.font()
        font.setPointSize(9)
        self.setFont(font)

        self.lists = Lists.Lists()

        # Initialize all Table_Layout.
        list_tableClasses = [
            Tables_Layout.Layout_TableT0,
            Tables_Layout.Layout_TableT1,
            Tables_Layout.Layout_TableT2,
            Tables_Layout.Layout_TableT3,
            Tables_Layout.Layout_TableT4,
            Tables_Layout.Layout_TableT5,
            Tables_Layout.Layout_TableT6,
            Tables_Layout.Layout_TableT7,
            Tables_Layout.Layout_TableT8,
            Tables_Layout.Layout_TableT9,
        ]
        self.list_Tables_Layout = []  # Index colide with table number. Every item contains tuple of two objects: layout with tables, and scroll area with this layout.
        for i1 in range(len(list_tableClasses)):
            layout_TableTxx = list_tableClasses[i1](self.lists, self.list_Tables_Layout)
            self.list_Tables_Layout.append((layout_TableTxx, Tables_Layout.Table_Layout_ScrollArea(layout_TableTxx)))

        #self.statusBar().showMessage('Ready//////')  # Bottom bar.

        self.centralWidget = QStackedWidget()
        self.setCentralWidget(self.centralWidget)


        # At each layout / widget: initialize object, button listeners and add to stack (centralWidget).
        # Layout: MainHome.
        self.mainHome_Layout = MainHome_Layout.MainHome_Layout(self.lists, self.list_Tables_Layout)
        self.mainHome_Layout.mainWidget.button3.clicked.connect(self.show_layout_importExport)
        self.mainHome_Layout.mainWidget.button1.clicked.connect(self.show_layout_help)

        # This solution do not works. Need pass function reference and argument - maybe by use 'partials'.
        # for i1 in range(len(self.list_Tables_Layout)):
        #     self.tableNumber = i1
        #     self.layout01_Main.list_button2[i1].clicked.connect(self.show_layout03_Lxx)
        self.mainHome_Layout.mainWidget.list_button2[0].clicked.connect(self.show_layout03_T0_competitionInfo)
        self.mainHome_Layout.mainWidget.list_button2[1].clicked.connect(self.show_layout03_T1_races)
        self.mainHome_Layout.mainWidget.list_button2[2].clicked.connect(self.show_layout03_T2_categories)
        self.mainHome_Layout.mainWidget.list_button2[3].clicked.connect(self.show_layout03_T3_groupsList)
        self.mainHome_Layout.mainWidget.list_button2[5].clicked.connect(self.show_layout03_T5_participants)
        self.mainHome_Layout.mainWidget.list_button2[6].clicked.connect(self.show_layout03_T6_assignGroupsToParticipants)
        self.mainHome_Layout.mainWidget.list_button2[7].clicked.connect(self.show_layout03_T7_results)
        self.mainHome_Layout.mainWidget.list_button2[8].clicked.connect(self.show_layout03_T8_resultsGroup)
        self.mainHome_Layout.mainWidget.list_button2[9].clicked.connect(self.show_layout03_T9_resultsParticipants)

        self.mainHome_Layout.mainWidget.button4.clicked.connect(self.refreshListsAndTables)
        self.mainHome_Layout.mainWidget.button5.clicked.connect(self.setDefaultValuesOfInsertingFields)
        self.mainHome_Layout.mainWidget.checkBox1.stateChanged.connect(self.event_checkBox1_timeBackwardSorting)
        self.mainHome_Layout.mainWidget.button6.clicked.connect(self.removeData_singleList)
        self.mainHome_Layout.mainWidget.button7.clicked.connect(self.removeData_all)

        self.centralWidget.addWidget(self.mainHome_Layout)

        # Layout: ImportExport.
        self.importExport_Layout = ImportExport_Layout.ImportExport_Layout(self.lists, self.setDefaultValuesOfInsertingFields)
        self.importExport_Layout.button1.clicked.connect(self.show_layout_home)
        self.centralWidget.addWidget(self.importExport_Layout)

        # Layout: Help.
        self.help_Layout = Help_Layout.Help_Layout(self.lists)
        self.help_Layout.mainWidget.button1.clicked.connect(self.show_layout_home)
        self.centralWidget.addWidget(self.help_Layout)

        # Layout: Tables.
        for i2 in self.list_Tables_Layout:
            i2[0].button1a.clicked.connect(self.show_layout_home)
            i2[0].button1b.clicked.connect(self.show_layout_home)
            i2[0].button2.clicked.connect(self.refreshListsAndTables)
            self.centralWidget.addWidget(i2[1])


        # Set values in main frame, show layout.
        self.centralWidget.setCurrentWidget(self.mainHome_Layout)

        # self.setMinimumSize(QSize(1150, 620))
        self.setGeometry(30, 40, 1150, 620)
        self.setFixedSize(1150, 620)
        self.setWindowTitle("Řazení výsledků")
        self.show()


    # Functions at button clicked - show layouts.
    def show_layout_home(self):
        for i1 in range(len(self.list_Tables_Layout)):  # Really bad solution. Because I need show dialog at layout_table_5 only when is displayed - and not during refreshing of preferences.
            self.list_Tables_Layout[i1][0].specialExceptSolution_isDisplayedThisLayout = False
        self.centralWidget.setCurrentWidget(self.mainHome_Layout)


    def show_layout_importExport(self):
        self.centralWidget.setCurrentWidget(self.importExport_Layout)


    def show_layout_help(self):
        self.centralWidget.setCurrentWidget(self.help_Layout)


    def show_TableLayout_Txx(self, tableNumber):
        self.centralWidget.setCurrentWidget(self.list_Tables_Layout[tableNumber][1])
        self.list_Tables_Layout[tableNumber][0].specialExceptSolution_isDisplayedThisLayout = True
        self.list_Tables_Layout[tableNumber][0].refreshValuesAtLayout()

    def show_layout03_T0_competitionInfo(self):
        self.show_TableLayout_Txx(0)

    def show_layout03_T1_races(self):
        self.show_TableLayout_Txx(1)

    def show_layout03_T2_categories(self):
        self.show_TableLayout_Txx(2)

    def show_layout03_T3_groupsList(self):
        self.show_TableLayout_Txx(3)

    def show_layout03_T5_participants(self):
        self.show_TableLayout_Txx(5)

    def show_layout03_T6_assignGroupsToParticipants(self):
        self.show_TableLayout_Txx(6)

    def show_layout03_T7_results(self):
        self.show_TableLayout_Txx(7)

    def show_layout03_T8_resultsGroup(self):
        self.show_TableLayout_Txx(8)

    def show_layout03_T9_resultsParticipants(self):
        self.show_TableLayout_Txx(9)


    # Functions at button clicked - other functions.
    def refreshListsAndTables(self):
        returnedValue = self.lists.fillTablesFromLists()
        for i1 in range(len(self.list_Tables_Layout)):
            self.list_Tables_Layout[i1][0].refreshTables()
        self.mainHome_Layout.mainWidget.refresh()
        self.mainHome_Layout.mainWidget.editText1.setText("")
        self.mainHome_Layout.mainWidget.label9.setText("Tabulky aktualizovány. " + returnedValue)

    def setDefaultValuesOfInsertingFields(self):
        self.mainHome_Layout.mainWidget.label9.setText("-")
        for i1 in range(len(self.list_Tables_Layout)):
            self.list_Tables_Layout[i1][0].setDefaultValues1()

    def event_checkBox1_timeBackwardSorting(self, state):
        if state == Qt.Checked:
            self.lists.listsOfAllLists[2][2].sortTimeAndCorrectionBackwards = True
        else:
            self.lists.listsOfAllLists[2][2].sortTimeAndCorrectionBackwards = False

    def removeData_singleList(self):
        # Get number of list from edit text, remove this list.
        numberOfList = self.mainHome_Layout.mainWidget.editText1.text()
        try:
            numberOfList = int(numberOfList)
        except ValueError:
            self.mainHome_Layout.mainWidget.label9.setText("Problém: nezadali jste číslo.")
            self.mainHome_Layout.mainWidget.editText1.setText("")
            return
        if 0 <= numberOfList < len(self.lists.listsOfAllLists[0]):
            buttonReply = QMessageBox.question(self, "Potvrďte akci", "Opravdu smazat data z listu L" + str(numberOfList) + "?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.lists.listsOfAllLists[0][numberOfList].removeDataFromList()
                self.mainHome_Layout.mainWidget.label9.setText("Data smazána z listu L" + str(numberOfList) + ". Aktualizujte a zkontrolujte tabulky.")
            else:
                self.mainHome_Layout.mainWidget.label9.setText("-")
        else:
            self.mainHome_Layout.mainWidget.label9.setText("Problém: číslo neodpovídá žádnému listu.")
        self.mainHome_Layout.mainWidget.editText1.setText("")
        for i1 in range(len(self.list_Tables_Layout)):
            self.list_Tables_Layout[i1][0].setDefaultValues1()

    def removeData_all(self):
        buttonReply = QMessageBox.question(self, "Potvrďte akci", "Opravdu smazat všechna data z tabulek?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.lists.removeDataFromList_allLists()
            self.mainHome_Layout.mainWidget.editText1.setText("")
            self.mainHome_Layout.mainWidget.label9.setText("Všechna data smazána.")
        else:
            self.mainHome_Layout.mainWidget.label9.setText("-")
        self.refreshListsAndTables()
        for i1 in range(len(self.list_Tables_Layout)):
            self.list_Tables_Layout[i1][0].setDefaultValues1()



def main():
    app = QApplication(sys.argv)

    layout = AA_Main()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
