from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QGroupBox, QStackedWidget, QVBoxLayout, QRadioButton, QScrollArea, QCheckBox
from PyQt5.QtGui import QFont



class MainWidget(QWidget):
    """
    Home screen.
    """

    def __init__(self, received_lists, received_list_Tables_Layout, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)

        self.lists = received_lists
        self.list_Tables_Layout = received_list_Tables_Layout

        label1 = QLabel("Home", self)
        font_h1 = self.font()
        font_h1.setPointSize(14)
        label1.setFont(font_h1)
        label1.setGeometry(15, 10, 1100, 24)

        self.layout_yPosition = 45

        label2 = QLabel("Začněte: můžete proklikávat mezi jednotlivými panely, každý z nich má nějakou užitečnou funkci.", self)
        label2.setGeometry(15, self.layout_yPosition, 1100, 20)

        self.button3 = QPushButton("Import a export do souborů", self)  # Layout: ImportExport.
        self.button3.setGeometry(900, self.layout_yPosition, 180, 22)

        self.button1 = QPushButton("Info, help", self)  # Layout: Help.
        self.button1.setGeometry(900, self.layout_yPosition + 35, 180, 22)

        # self.layout_yPosition += 25
        #
        # label3 = QLabel("Můžete proklikávat mezi jednotlivými panely, každý z nich má nějakou užitečnou funkci.", self)
        # label3.setGeometry(15, self.layout_yPosition, 1100, 20)
        self.layout_yPosition += 35


        # Layout: Tables.
        label4 = QLabel("Tabulky a listy:", self)
        label4.setGeometry(15, self.layout_yPosition, 280, 20)
        label4 = QLabel("Počet záznamů v listu:", self)
        label4.setGeometry(370, self.layout_yPosition, 500, 20)
        self.layout_yPosition += 35

        self.list_button2 = []  # Index colide with table name.
        self.list_label5 = []
        for i1 in range(len(self.list_Tables_Layout)):
            label3 = QLabel(self.list_Tables_Layout[i1][0].thisList.tableName[:2] + ":", self)
            button2 = QPushButton(self.list_Tables_Layout[i1][0].thisList.tableName[3:], self)
            self.list_button2.append(button2)

            if i1 == 4:
                label3.setGeometry(-300, self.layout_yPosition, 30, 20)
                button2.setGeometry(-300, self.layout_yPosition, 180, 22)
            else:
                label3.setGeometry(40, self.layout_yPosition, 30, 20)
                button2.setGeometry(100, self.layout_yPosition, 180, 22)

            label5 = QLabel("-", self)
            self.list_label5.append(label5)
            if i1 == 0 or i1 == 4 or i1 == 8 or i1 == 9:
                label5.setGeometry(-300, self.layout_yPosition, 30, 20)
            else:
                label5.setGeometry(370, self.layout_yPosition, 30, 20)

            if i1 != 4:
                self.layout_yPosition += 35

        self.layout_yPosition += 15


        # QGroupBox - titled border - frame with label.
        myWi = QWidget()

        layout_yPosition_intern = 2

        label8 = QLabel("Stav: ", myWi)
        label8_font = QFont()
        label8_font.setBold(True)
        label8.setFont(label8_font)
        label8.setGeometry(15, layout_yPosition_intern, 80, 20)
        self.label9 = QLabel("-", myWi)
        label9_font = QFont()
        label9_font.setBold(True)
        self.label9.setFont(label9_font)
        self.label9.setGeometry(100, layout_yPosition_intern, 1000, 20)
        layout_yPosition_intern += 35

        self.button4 = QPushButton("Aktualizovat tabulky", myWi)
        self.button4.setGeometry(100, layout_yPosition_intern, 180, 22)
        layout_yPosition_intern += 35

        self.button5 = QPushButton("Nastavit výchozí hodnoty vkládacích políček", myWi)
        self.button5.setGeometry(100, layout_yPosition_intern, 300, 22)
        layout_yPosition_intern += 35

        self.checkBox1 = QCheckBox("Řadit výsledky podle času a korekce sestupně (otočit řazení).", myWi)
        self.checkBox1.setChecked(False)
        self.checkBox1.setGeometry(15, layout_yPosition_intern, 1000, 22)
        layout_yPosition_intern += 35

        label6 = QLabel("Odstranit data z listu číslo:", myWi)
        label6.setGeometry(15, layout_yPosition_intern, 340, 20)

        self.editText1 = QLineEdit(myWi)
        self.editText1.setGeometry(400, layout_yPosition_intern, 80, 20)

        self.button6 = QPushButton("Odstranit data", myWi)
        self.button6.setGeometry(500, layout_yPosition_intern, 180, 22)
        layout_yPosition_intern += 35

        label7 = QLabel("Odstranit data ze všech listů:", myWi)
        label7.setGeometry(15, layout_yPosition_intern, 480, 20)

        self.button7 = QPushButton("Odstranit data", myWi)
        self.button7.setGeometry(500, layout_yPosition_intern, 180, 22)
        layout_yPosition_intern += 35


        myStWi2 = QStackedWidget(self)
        myStWi2.addWidget(myWi)

        radioButtonsGroup1 = QVBoxLayout()
        radioButtonsGroup1.addWidget(myStWi2)

        qgroupbox1 = QGroupBox("Funkce k tabulkám obecně: ")
        qgroupbox1.setLayout(radioButtonsGroup1)

        myStWi = QStackedWidget(self)
        myStWi.addWidget(qgroupbox1)

        myStWi.setGeometry(15, self.layout_yPosition, 1085, layout_yPosition_intern + 30)
        self.layout_yPosition += layout_yPosition_intern + 60

        self.layout_yPosition += 5


    def refresh(self):
        for i1 in range(len(self.list_label5)):
            self.list_label5[i1].setText(str(self.lists.listsOfAllLists[0][self.list_Tables_Layout[i1][0].thisList.baseListNumber].sumOfRows))



class MainHome_Layout(QWidget):

    def __init__(self, received_lists, received_list_Tables_Layout, *args, **kwargs):
        super(MainHome_Layout, self).__init__(*args, **kwargs)
        """
        This class perform scrolling screen. I do not know better solution. This should be only one row.
        """

        self.mainWidget = MainWidget(received_lists, received_list_Tables_Layout)
        self.mainWidget.setMinimumWidth(1125)
        self.mainWidget.setMinimumHeight(self.mainWidget.layout_yPosition)

        myLayout = QStackedWidget()
        myLayout.addWidget(self.mainWidget)

        scroll = QScrollArea(self)
        scroll.setWidget(myLayout)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(622)
        scroll.setFixedWidth(1152)
        scroll.setGeometry(-1, -1, 622, 1152)
