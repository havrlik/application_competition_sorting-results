from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFileDialog, QMessageBox, QLineEdit
from PyQt5.QtGui import QFont
from app_package import ImportExport



class ImportExport_Layout(QWidget):

    def __init__(self, received_lists, received_setDefaultValuesOfInsertingFields, *args, **kwargs):
        super(ImportExport_Layout, self).__init__(*args, **kwargs)

        self.lists = received_lists
        self.listener_setDefaultValuesOfInsertingFields = received_setDefaultValuesOfInsertingFields
        self.importExport = ImportExport.ImportExport(self.lists)

        font_h1 = self.font()
        font_h1.setPointSize(14)
        font_h2 = self.font()
        font_h2.setPointSize(11)


        self.button1 = QPushButton("<- Zpět", self)
        self.button1.setGeometry(15, 12, 120, 22)

        label1 = QLabel("Import a export hodnot do souborů", self)
        label1.setFont(font_h1)
        label1.setGeometry(170, 10, 930, 24)

        self.layout_yPosition = 45

        label2 = QLabel("Import dat ve formátu tohoto programu:", self)
        label2.setGeometry(15, self.layout_yPosition, 480, 20)

        self.button4 = QPushButton("Import", self)
        self.button4.setGeometry(500, self.layout_yPosition, 180, 22)
        self.button4.clicked.connect(self.importData)
        self.layout_yPosition += 35

        label3 = QLabel("Export dat ve formátu tohoto programu:", self)
        label3.setGeometry(15, self.layout_yPosition, 480, 20)

        self.button5 = QPushButton("Export", self)
        self.button5.setGeometry(500, self.layout_yPosition, 180, 22)
        self.button5.clicked.connect(self.exportData_all)
        self.layout_yPosition += 35

        label9 = QLabel("Export výsledků z tabulky T8 ve formátu CSV:", self)
        label9.setGeometry(15, self.layout_yPosition, 480, 20)

        self.button6 = QPushButton("Export T8 - výsledky", self)
        self.button6.setGeometry(500, self.layout_yPosition, 180, 22)
        self.button6.clicked.connect(self.exportData_T8)
        self.layout_yPosition += 35

        label4 = QLabel("Stav: ", self)
        label4_font = QFont()
        label4_font.setBold(True)
        label4.setFont(label4_font)
        label4.setGeometry(15, self.layout_yPosition, 80, 20)
        self.label5 = QLabel("-", self)
        label5_font = QFont()
        label5_font.setBold(True)
        self.label5.setFont(label5_font)
        self.label5.setGeometry(100, self.layout_yPosition, 1000, 20)
        self.layout_yPosition += 50

        yStep_text = 22

        label6 = QLabel("Návod", self)
        label6.setFont(font_h2)
        label6.setGeometry(15, self.layout_yPosition, 980, 22)
        self.layout_yPosition += 30

        paragraph1 = [
            "Export provádějte s aktualizovanými tabulkami. Po aktualizaci raději zkontrolujte správnost údajů a také koukněte, zda na domovském layoutu ('Home') u nápisu 'Stav' není zpráva ",
            "          o nenalezených realčních hodnotách.",
            "Při exportu dat aplikace vyhodí člověkem čitelný soubor s příponou '.txt'. Můžete ale doplnit příponu '.csv', a poté soubor otevírat v tabulkových editorech.",
            "Pro export výsledků soutěže použijte funkci export tabulky T8. Soubor zapíše příponu '.csv', a nebo můžete zvolit i '.txt'. Při exportu se vypíší data tak, jak je vidíte v tabulce T8, proto ",
            "          nezapomeňte aktualizovat tabulky. Formát '.csv' je univerzální a půjde otevřít v libovolném tabulkovém editoru.",
        ]

        for i1 in range(len(paragraph1)):
            labelX = QLabel(paragraph1[i1], self)
            labelX.setGeometry(30, self.layout_yPosition, 1070, 20)
            self.layout_yPosition += yStep_text
        self.layout_yPosition += 15

        label7 = QLabel("Pokročilý uživatel", self)
        label7.setFont(font_h2)
        label7.setGeometry(15, self.layout_yPosition, 980, 22)
        self.layout_yPosition += 30

        paragraph2 = [
            "Import souboru: první řádek musí obsahovat frázi: '" + self.importExport.idMark + "'. Dále před každou tabulkou musí být řádek s nadpisem 'L' a číslem tabulky.",
            "Řádky s daty listů musejí začínat číslicí, ostatní řádky nesmějí (!) začínat číslicí - tedy první znak řádku nesmí být numerický (například označení tabulek nebo názvy kolonek). Můžete se podívat ",
            "          na strukturu exportovaného souboru. Při editaci exportovaných souborů buďte obezřetní, protože hodnoty nejsou při importu kontrolovány - například relační hodnoty nebo unikátnost hodnot.",
        ]

        for i1 in range(len(paragraph2)):
            labelX = QLabel(paragraph2[i1], self)
            labelX.setGeometry(30, self.layout_yPosition, 1070, 20)
            self.layout_yPosition += yStep_text
        self.layout_yPosition += 10


    def importData(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filePath, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Text Files (*.txt)", options = options)
        if filePath:
            message = self.importExport.importData(filePath)
            if type(message) == str and len(message) > 0:
                self.label5.setText(str(message))
            self.listener_setDefaultValuesOfInsertingFields()


    def exportData_all(self):
        """
        Write data from lists into file.
        First row in file contains identification mark, second date and time of created.
        Before every table datas is describing and identification rows of any table.
        List data must begin by numeric character, other rows must not.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filePath, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "Text Files (*.txt);;All files (*)", options = options)
        if filePath:
            message = self.importExport.exportData_all(filePath)
            if type(message) == str and len(message) > 0:
                self.label5.setText(str(message))


    def exportData_T8(self):
        """
        Write data from table T8 into file.
        This table should be actualized by user before export.
        Prefer is CSV file.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filePath, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "CSV Table Files (*.csv);;All files (*)", options = options)
        if filePath:
            message = self.importExport.exportData_T8(filePath)
            if type(message) == str and len(message) > 0:
                self.label5.setText(str(message))
