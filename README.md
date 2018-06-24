# application_competition_sorting-results
Application ability to sort participants and their results in race or competition. Czech user language.

Application, where you can insert races and categories, and participans with race numbers. After inserting results it automatically sort in each category.
User's language is czech. For right understanding to this code and application performance rather use also czech language, because user labels are actually only in czech language.


So in description I will continue in czech language:

Popis aplikace, obecné použití:

Aplikace umožňuje řazení výsledků z menších závodů nebo soutěží. Primárně zaměřeno na běžecké a podobné soutěže.
Lze zadat různé 'závody' a ty rozdělit do 'kategorií'. Po zadání výdledků se zobrazí umístění účastníka jak v závodě, tak v kategorii. K zadání výsledků do aplikace stačí znát informace z cíle - startovní nebo jiné identifikační číslo soutěžícího, čas, a dále jen název daného závodu. Pro společný start více závodů (různé délky tratě, věkové kategorie, pohlaví atd) lze použít stejnou sadu startovních čísel, aplikace pak sama rozpozná ke kterému závodu výsledek soutěžícího patří a správně ho zařadí.

Prakticky prabíhá práce s aplikací tak, že v první fázi před startem lze zadat údaje o závodech, kategoriích a soutěžících, ve druhé fázi po závodě doplnit časy k jednotlivým soutěžícím. Výsledky se seřadí a uživatel uvidí jednotlivé soutěžící roztříděné podle kategoriích a seřazené podle výsledku. Výsledky i surová data lze exportovat do formátu .txt nebo univerzálního tabulkového .csv.

Výsledky se zadávají v běžném formátu času v šedesátkové soustavě, možnost až na milisekundy, a maximálně na 999 hodin (ale kód aplikace lze upravit), dále lze zadat dodatečnou korekci stejných časů (hodnoty celých čísel 0 až 999) a lze také účastníka zapsat s časem ale nezařadit do výsledných umístění. Řazení lze otočit, aby delší čal byl ten lepší. Ale jiné hodnoty výsledku než čas aplikace zatím neumí (například zadávat vzdálenost v metrech).
