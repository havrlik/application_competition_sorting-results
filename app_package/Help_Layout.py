from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QStackedWidget, QScrollArea



class MainWidget(QWidget):

    def __init__(self, received_lists, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)

        self.lists = received_lists

        font_h1 = self.font()
        font_h1.setPointSize(14)
        font_h2 = self.font()
        font_h2.setPointSize(11)

        self.button1 = QPushButton("<- Zpět", self)
        self.button1.setGeometry(15, 12, 120, 22)

        label1 = QLabel("Help", self)
        label1.setFont(font_h1)
        label1.setGeometry(170, 10, 930, 24)

        self.layout_yPosition = 55
        yStep_text = 28

        # label2 = QLabel("Obecné", self)
        # label2.setFont(font_h2)
        # label2.setGeometry(15, self.layout_yPosition, 980, 22)
        # self.layout_yPosition += 30

        paragraph1 = [
            "Popis aplikace, obecné použití",
            [
                "Aplikace umožňuje řazení výsledků z menších závodů nebo soutěží. Primárně zaměřeno na běžecké a podobné soutěže.",
                "Lze zadat různé 'závody' a ty rozdělit do 'kategorií'. Po zadání výdledků se zobrazí umístění účastníka jak v závodě, tak v kategorii. K zadání výsledků do aplikace stačí znát informace ",
                "          z cíle - startovní nebo jiné identifikační číslo soutěžícího, čas, a dále jen název daného závodu. Pro společný start více závodů (různé délky tratě, věkové kategorie, pohlaví atd) lze použít ",
                "          stejnou sadu startovních čísel, aplikace pak sama rozpozná ke kterému závodu výsledek soutěžícího patří a správně ho zařadí.",
                "Prakticky prabíhá práce s aplikací tak, že v první fázi před startem lze zadat údaje o závodech, kategoriích a soutěžících, ve druhé fázi po závodě doplnit časy k jednotlivým soutěžícím. ",
                "          Výsledky se seřadí a uživatel uvidí jednotlivé soutěžící roztříděné podle kategoriích a seřazené podle výsledku. Výsledky i surová data lze exportovat do formátu .txt nebo univerzálního ",
                "          tabulkového .csv.",
                "Výsledky se zadávají v běžném formátu času v šedesátkové soustavě, možnost až na milisekundy, a maximálně na 999 hodin (ale kód aplikace lze upravit), dále lze zadat dodatečnou korekci ",
                "          stejných časů (hodnoty celých čísel 0 až 999) a lze také účastníka zapsat s časem ale nezařadit do výsledných umístění. Řazení lze otočit, aby delší čal byl ten lepší. Ale jiné hodnoty ",
                "          výsledku než čas aplikace zatím neumí (například zadávat vzdálenost v metrech).",
            ],

            "Jak jsou data uchovávána a zobrazována v aplikaci",
            [
                "Je tu 8 uživatelských tabulek. Do šesti tabulek se zadávají data, další dvě jen zobrazují užitečné informace poskládáním dat. Jsou očíslovány od 0 do 9, tabulka číslo 4 je vynechána. Tolik tabulek ",
                "          je potřeba kvůli povaze dat a univerzálnímu použití pro různé požadavky - hlavně z důvodu přiřazení umístění v jednotlivých kategoriích a možné potřebě jedné sady startovních čísel ",
                "          pro skupinu více závodů při společném startu. Uživatel může vhodně seskládat kategorie pro konkrétní požadavky soutěže.",
                "V aplikaci jsou dvě sady tabulek. Jedna sada s daty, které se zadávají do aplikace, a druhá sada, která je určena pro čtení dat uživatelem - aplikace poskládá data z první sady tak, ",
                "          aby se pohodlněji četli uživatelem. Například v tabulce s výsledky aplikace potřebuje znát jen ID účastníka a čas, ale uživatel navíc uvidí i jméno učastníka, jméno závodu a tak podobně. ",
                "          Tabulky z první sady jsou nazývány 'listy' (anglicky lists) nebo zkráceně 'L' s doplněným číslem listu. Tabulky z druhé uživatelské sady jsou 'tabulky' (tables), zkráceně 'T', také s číslem ",
                "          tabulky. Jak to použít: Na domovském layoutu (česky obrazovce) jsou tlačítka, kterými se můžete proklikat na další layouty, které obsahují jednotlivé tabulky. Tyto layouty jsou shodně ",
                "          očíslovány s tabulkami, které zobrazují. Například layout 'T1' zobrazuje tabulku 'T1' a také vkládácí políčka do listu 'L1'. Po stisknutí tlačítka 'Aktualizovat' (nachází se na domovském ",
                "          layoutu i na layoutech jednotlivých tabulek) se data přepíšou z listů do tabulek. 'Tabulky' jsou tedy spíše virtuální náhled do 'listů', ale uživatel zde vidí to co potřebuje. Ve druhé sadě ",
                "          tabulek určených pro uživatele je více tabulek ze stejného důvodu. Je tam o dvě víc (T8 a T9), aby se daly pohodlně odečíst hodnoty, které jsou cílem pro tuto aplikace. Obsahují ",
                "          jména i výsledky účastníků a další užitečné informace. Uživatelské tabulky jsou takto řešený kvůli omezení duplicity dat v listech, viz databáze SQL atp. Hodnoty, které se načítají ",
                "          z jiných listů, budeme říkat 'relační', protože musí již existovat v dotyčném listu.",
                "Záznamy, nebo-li řádky v listech (slovo list si pro zjednodušení můžete představit jako synonymum pro slovo tabulka) jsou očíslovány, tomuto číslu se říká 'ID'. Aplikace ho přiřazuje ",
                "          automaticky a v daném listu je vždy unikátní - každý záznam má jiné ID. Číslování ID začíná od nuly. Pokud se všimnete, že ID na sebe nenavazují, tak to neni chyba, může se to stát ",
                "          třeba při smazání záznamů.",
                "Záznamy uživatelských tabulek jsou seřazeny. V tabulce T1 a T2 je to podle čísla priority ve čtvrtém sloupci, můžeme tím ovlivnit, jak chceme záznamy seřadit i v dalších tabulce T3 a v tabulce ",
                "          s výsledky jednotlivých skupin T8. Dále třeba T5 účastníci jsou řazeny podle roku narození, pohlaví a jména. V tabulce T7 je řazení jen podle ID. V tabulce T8 jsou záznamy seřazeny ",
                "          podle kategorií a místění účastníků, kategorie jsou navíc odděleny a nadepsány informacemi o nich.",
            ],

            "Jak zvolit závody a kategorie, jak zadávat soutěžící a jejich výsledky",
            [
                "V závodě s rozlišováním výsledků mužů a žen vytvořte dva 'L1 Závody', i kdyby soutěžili společně na stejné trati. Dva různé závody budou mít každý vlastní seřazení výsledků - při soutěžích, ",
                "          kdy jsou mezi pohlavími rozdílné výsledky je to lepší než to řešit přes kategorie v jediném závodě. V případě nejistoty při rozhodování o kategoriích je tedy lépe vytvořit více závodů, ",
                "          než více kategorií v jednom závodě. Jednotlivé závody můžete dále rozdělit na 'L2 Kategorie', třeba věkové, které budou mít opět vlastní seřazení výsledků. Jednu vytvořenou ",
                "          kategorii můžete přiřadit k více závodům, pokud se to bude hodit, pokud jsou například věkové rozdělení mužů i žen stejné - a pokud vyhovuje další popis kategorie požadavkům. ",
                "          Co se týče 'Názvů' závodů, kategorií, skupin závod-kategorie a skupin společných startovních čísel, musí být unikátní jak pro svůj sloupec, tak mezi těmito čtyřmi sloupci.",
                "Každý závod má svou sadu startovních čísel, startovní čísla nemohou být dvě stejná v jednom závodě. Startovní číslo může být alfanumerické - může obsahovat i písmena nebo další znaky. ",
                "          V případě společných závodů (myšleno závod zapsaný podle systému této aplikace) kdy výce závodů má společný start, nebo cíl, a hlavně pokud v cíli nerozlišují závodníky jednotlivých ",
                "          závodů, tito závodníci musejí mít jedinečná startovní čísla. Lze to zajistit zapsáním do listu 'L1 Závody' do páté kolonky 'Skupina společných startovních čísel' stejného názvu / zkratky ",
                "          k daným 'závodům'. Později při zadávání výsledků do listu 'L7 Všechny výsledky' stačí zadat jakýkoli název závodu a aplikace dohledá ten správný ze společné skupiny. Pokud naopak ",
                "          chcete pro jednotlivé kategorie i nové sady startovních čísel, raději vytvořte nové závody, nebo to obejít a pro každou kategorii připsat ke startovnímu číslu také nějaký identifikační znak.",
                "Kategorie přiřadíte k závodů v listu 'L3 Skupiny závod-kategorie'. Každý závod tedy musí mít alespoň jednu kategorii.",
                "V listu 'L5 Účastníci' se zadají informace o účastnících. V listu 'L6 Přiřazení účastník - skupina' se k účastníkovi přiřadí startovní číslo a závod - přesněji záznam z listu 'L3 Skupiny závod-kategorie'. ",
                "          V layoutu L5/T5 lze navíc v kolonkách 'ID skupiny (bude přepsáno do L6)', 'Název skupiny (bude přepsáno do L6)' a 'Startovní číslo (bude přepsáno do L6)' obstarat vložení záznamu ",
                "          i do listu 'L6 Přiřazení účastník - skupina'. Pokud vložení do listu L5 proběhne v pořádku, ale do listu L6 nikoli, je potřeba přejít do layoutu L6/T6 a opakovat vložení. Pokud ",
                "          potřebujete účastníka zařadit do více různých závodů, můžete v layoutu L6/T6 (ale z layoutu L5/T5 jde pouze jeden takový záznam - při opětovném vložení hodnot jména, ",
                "          příjmení atd. se totiž vytvoří nový účastník s jedinečným ID). Při editaci (opravě / přepsání) záznamu L5 nelze použít funkci vložení záznamu do L6.",
            ],

            "Konkrétní příklad jednoduché soutěže",
            [
                "Rozdělení závodů a kategorií: všichni účastníci všech závodů i kategorií běží najednou a mají jedinečná startovní čísla, může ale nemusí být společný start nebo cíl a trasa také nemusí ",
                "          být totožná: 'Závody': Pro obě pohlaví zvolte dva závody, pokud se bude lišit trasa pro ruzné závodníky stejného pohlaví tak i pro každou trasu vytvořte speciální závod. ",
                "          'Kategorie': Pokud chcete několik kategorií v jednom závodě, vytvořte je. I pro závod bez více kategorií je potřeba jednu vytvořit. Pokud si nejste jistí, jak je potřeba vytvořit ",
                "          tyto závody a kategorie, obecně je asi lepší vytvořit další závod, než další kategorii do společného závodu. Společná startovní čísla zajistíte v listu L1 v pátém sloupci vepsáním ",
                "          stejné (náhodné) zkratky do všech požadovaných závodů. Dále pokračujete vytvořením záznamů soutěžících a přiřazení startovních čísel a závodu, kterého se účastní. Po závodě ",
                "          do listu L7 zapisujete časy a startovní čísla a také jméno závodu - v případě společných startovních čísel je jedno který závod vložíte, protože aplikace sama rozpozná, kam ",
                "          startovní číslo patří.",
                "Pokud chcete zaznamenávat i juniorní nebo dětské závody, také je můžete výtvořit. Většinou asi bude mít každá věková kategorie i jinou trasu, proto vytvořte pro každou trasu nový 'závod' ",
                "          i 'kategorii', 'závody' ale dvojmo pro obě pohlaví ('kategorie' být dvojmo nemusí pokud mají společné údaje o věku atd.). Při zadávání výsledků opět stačí znát nazev závodu, ",
                "          startovní číslo a čas.",
            ],

            "Zadávání hodnot do aplikace",
            [
                "Pro zadání záznamu do aplikace přejděte na potřebný layout, hodnoty vpište do kolonek pod nadpisem 'Přidat nový'. Jsou tu dva typy kolonek, můžete si vybrat, obě vloží záznam totožně, ",
                "          jen vypadají jinak. Tlačítko vloží hodnoty jen z kolonek u kterých se nachází, pochopitelně nekombinuje ty horní se spodními. Záznamy lze upravovat: mazat, nebo upravit stávající záznam. ",
                "          Při těchto úpravách musíte znát ID chtěného záznamu, tedy číslo z prvního sloupce stejného listu. Při úpravě stávajícího záznamu se hodnoty načtou do vkládacích políček, hodnoty ",
                "          opravte a potvrďte tlačítkem. Sledujte nápis 'Stav', zda nedošlo k chybě, případně vkládejte jiné hodnoty, dokud to hlásí problem. Pokud se to nedaří nebo jste si to rozmysleli, ",
                "          přepsání lze zrušit tlačítkem 'Vyčistit', původní záznam zůstane nezměněn.",
                "Aplikace kontroluje zadané hodnoty. Kontroluje zda, neni požadováno číslo, jedinečnost hodnot, existenci relačních hodnot v jiných tabulkách a správnost formátu (v kolonkách pohlaví, ",
                "          čas a korekce). V případě zjištěného nedostatku se zobrazí hláška o problému a vložení neproběhne. Dále do kolonek nesmíte zadávat středníky ';'. Bílé znaky, jako je třeba mezera ( ), ",
                "          na začátku a na konci se umaže.",
                "Názvy 'závodů', 'kategorií', 'skupin závod-kategorie' a 'skupin společných startovních čísel' zadávejte nejlépe jako zkratky. Doporučujeme krátce, jednoznačně, písmena jen malá a bez mezer. ",
                "          Určitě se s nimi bude dále pracovat (pokud nechcete používat ID) a tímto se sníží chybovost.",
                "V běžeckých a podobných soutěžích se budou účastníci zařazovat do kategorií nejspíše podle věku. Aplikace ale věk a kategorii nekontroluje, na to se musí dát pozor při přiřazování daných ",
                "          záznamů. Na druhou stranu to umožňuje korekce - třeba zařazení juniorů mezi seniory, nebo univerzální použití i jinde, kde se konkrétně věk nebere v potaz.",
                "Do listu L5, kolonky 'pohlaví', můžete zadávat tyto hodnoty: 'm, M, f, F, z, Z, ž, Ž' Aplikace je přepíše na 'M' nebo 'F', zkratky znamenají male a female.",
                "List L7, kolonka 'čas': možnost zadat v tomto formátu '000:00:00.000' klasicky v šedesátkové soustavě. Můžete vynechat nuly na začátku nebo milisekundy na konci, ale například na začátku ",
                "          nesmí být dvojtečka - to vrátí upozornění, zda jste na něco nezapomněli, apt. Lze zapnout funkci na odříznutí milisekund při zadávání a zároveň i při zobrazení v uživatelských ",
                "          tabulkách. Pokud ale stávající hodnoty již milisekundy obsahovaly, při zapnutí funkce se neodříznou (odříznou se pouze u nově přidaných), jen nebudou vidět, ale při seřazení budou ",
                "          brány v potaz stejně jako doposud - na to pozor. Dále při zadávání času místo dvojteček můžete zadávat pomlčky (-).",
                "List L7, kolonka 'korekce': v případě stejných časů lze výsledek korigovat touto hodnotou. Může nabývat celých čísel od 0 do 999. Při seřazení kvůli přidání pořadí aplikace tuto hodnotu ",
                "          použije jako další desetinná místa, a to i při opačném řazení.",
                "List L7, kolonka 'zařadit': pokud chcete, aby nějaký účastník byl v tabulce se svým časem, ale nechcete ho započítat do pořadí (například: neodpovídá kategorii, mimo soutěž, diskvalifikace), ",
                "          vložte do této kolonky číslici '0', jinak nevyplňujte a nebo vložte jakoukoli jinou numerickou hodnotu, automaticky bude přepsána na '1'. Při sežazení výsleků se těm nezařazeným ",
                "          přiřadí pořadí počínající 100 001, takže můžete porovnávat mezi sebou i tyto nezařazené výsledky.",
                "Aplikace používá jako desetiný oddělovač tečku (.) po zvyklostech v anglicky hovořících státech a v programovacích jazycích. U hodnoty času ale můžete vložit i čárku (,) a aplikace ji přepíše.",
                "Jakmile začnete vkládat záznamy do listů L5, již by se neměli mazat nebo přepisovat záznamy předchozích listů, protože na ně může být odkazovano relačními hodnotami. Některé chyby však ",
                "          aplikace odhalí a vypíše problém do popisku 'Stav' na domovském layoutu.",
            ],

            "Paralelní rychlejší zadávání na více počítačích",
            [
                "Výsledky lze vkládat i na více offline počítačích, exportovaná data pak přenést do jednoho počítače a ručně je překopírovat do jediného souboru. Pozor ale na jedinečnost ID, kterou ",
                "          aktuálně nelze v aplikaci editovat - možná by chtělo tuto funkci dopsat. V praxi se to ale dá obejít. Napřed v jednom počítači vytvoříte všechny závody, kategorie a tak (později ",
                "          na dalších počítačích se budou zadávat jen účastníci a / nebo jejich výsledky). Potom pro každý počítač ručně upravíte exportovaný soubor s jediným dočasným účastníkem (který později ",
                "          smažete nebo nezařadíte), musí mít i přiřazení ke skupině a zapsaný výsledek. V každém ze souboru ručně přepíšete ID v záznamu tohoto účastníka pro všechny tři listy L5, L6 a L7. ",
                "          ID bude pro každý počítač jiné, například 0, 1 000, 2 000, 3 000 atd. Při načtení souboru do aplikace se totiž nové ID daného listu nastaví na nejvyšší (+ 1), jaký načtený list obsahuje, ",
                "          a pokud v každém počítači vložíte méně než zmíněných 1 000 záznamů, nedojde ke kolizi čísel ID.",
                "Během načtení souboru do aplikace se ale většina požadavků, na které můžete narazit při vkládání záznamů, nekontroluje (z důvodu složitosti a komplikovaných reportů možných nedostatků), ",
                "          proto při ruční editaci souborů dbejte obezřetnosti.",
            ],

            "About",
            [
                "Vytvořil: Matouš Havrlík.",
                "Vytvořeno v roce 2018. Poslední aktualizace: 2018.  --> https://github.com/havrlik/application_competition_sorting-results <--",
                "Aplikace vznikla v rámci studia programování, a pokud má sloužit v běžném provozu, tak nejspíše pro malé zájmové neziskové akce.",
                "Aplikace neni otestovaná na úplně všechy kombinace případů z důvodu náročnosti a častého upravování. Nedostatky se mohou projevit spadnutím aplikace, takže doporučujeme časté ukládání ",
                "          dat. Při standartních úkonech by však problémy neměli nastat.",

            # "",
            #     "          ",
            ],
                    ]

        for i1 in paragraph1:
            if type(i1) == str:
                labelHx = QLabel(i1, self)
                labelHx.setFont(font_h2)
                labelHx.setGeometry(15, self.layout_yPosition, 980, 22)
                self.layout_yPosition += 30
            else:
                for i2 in i1:
                    if i2[0] == " ":
                        self.layout_yPosition -= 8
                    labelx = QLabel(i2, self)
                    labelx.setGeometry(30, self.layout_yPosition, 1070, 20)
                    self.layout_yPosition += yStep_text
                self.layout_yPosition += 20

        self.layout_yPosition += 35



class Help_Layout(QWidget):

    def __init__(self, received_lists, *args, **kwargs):
        super(Help_Layout, self).__init__(*args, **kwargs)
        """
        This class perform scrolling screen. I do not know better solution. This should be only one row.
        """

        self.mainWidget = MainWidget(received_lists)
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
