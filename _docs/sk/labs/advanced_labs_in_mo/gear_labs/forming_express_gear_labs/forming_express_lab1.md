---
lang: sk
title: "Vytvorenie Express Lab1"
---

# Laboratórna úloha č. 1. Laboratórna úloha s 2D ozubenými kolesami

### Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. L1.1. Vyberte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek vyberte „**Anglický**“ pomocou prepínača. Názov úlohy zadajte ako „**FE_Gear**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na zadanie úlohy

Spustí sa grafické rozhranie MO spolu s oknom „Nový projekt“. Zadajte názov projektu ako **FE_Gear**, skontrolujte, či je zaškrtnuté políčko **Prvá****operácia**, a zo zoznamu vyberte operáciu **[2D] Forming Express** zo zoznamu a použite predvolený (domovský) adresár, ako je znázornené na obr. L1.2. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pridajte projekt. Na tento laboratórny cvičebný projekt sa bude odkazovať v budúcich laboratórnych cvičeniach, preto je dôležité použiť vyššie uvedený názov.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0002.jpg' | relative_url }})

Okno nového projektu MO

### Otvoriť preprocesor

Zmeňte predvolený názov operácie z „Forming“ na „**Upset**“ dvojitým kliknutím na názov v dlaždici operácie. V prípade potreby môžete na priblíženie tejto dlaždice operácie použiť koliesko myši. Stlačením klávesy **Enter** potvrďte nový názov.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0003.jpg' | relative_url }})

Zmena názvu operácie na „Upset“

### Typ procesu

Overte, či je typ geometrie nastavený na **2D osovo symetrický**, a nastavte typ procesu na **kovanie za tepla**.

Operácie Forming Express využívajú posuvníky „Zložitosť“ a „Presnosť“ na nastavenie parametrov siete a časových krokov pre simuláciu. Čím vyššie sú nastavené hodnoty „Zložitosť“ a „Presnosť“, tým viac prvkov a menších časových krokov sa v analýze použije.

Vo všeobecnosti platí, že medzi rozlíšením a dĺžkou výpočtu existuje kompromis. Ak posuvníky nastavíte úplne doľava (Jednoduché/Rýchle), dosiahnete kratšiu dobu výpočtu, avšak vzhľadom na väčšie prvky sa zvyšuje pravdepodobnosť, že vám uniknú dôležité geometrické detaily alebo chyby.

V rámci tohto cvičenia nechajte posuvník **Zložitosť** nastavený na hodnotu **Stredná** a posuvník **Presnosť** nastavte na hodnotu **Rýchla**, ako je znázornené na obr. L1.4. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0004.jpg' | relative_url }})

Okno procesu

### Tepelná analýza

V tomto prvom laboratórnom cvičení nebudeme brať do úvahy zmeny teploty, ku ktorým dochádza počas tvarovania, preto nastavte výpočet teploty na **Konštantná teplota (izotermická)**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Nastavenie počtu objektov

Simulovaná operácia kovania vyžaduje obrobok a hornú a dolnú matricu. Budeme teda mať **1 obrobok + 2 matrice**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Definovanie všeobecných údajov o obrobku

Potvrďte predvolený názov objektu „Workpiece“ a teplotu **2******2** 50**°F. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). 

**Poznámka:** Tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_object.._button.jpg' | relative_url }}) slúži na import údajov z iného kľúčového slova úlohy DEFORM alebo z inej databázy. Vo väčšine prípadov budete používať možnosť Import Geometry ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) na nasledujúcej stránke.

### Vytvorenie geometrie obrobku z primitívu

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) vytvoríte geometriu v programe DEFORM. Modelovaný obrobok má priemer 5 in. a výšku 7,48 in., pričom polomery rohov sú **0,1** in. Osovo-symetrické simulácie modelujú radiálny rez dielu, preto vyberte **Cylinder**, nastavte polomer na **2,5** palca, **výšku** na **7,48** palca a R1 a R2 na hodnotu **0,1** palca (pozri obr. L1.5.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) potvrďte tieto rozmery dielu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0005.jpg' | relative_url }})

Geometria obrobku – okno „Primitívy“

_**Manipulácia s displejom**_

Funkcie na manipuláciu s oknom DISPLAY (napríklad Posun, Zväčšenie, Zväčšenie obrazu a Otočenie) je možné aktivovať pomocou ikon v hornej časti okna Pre-processor. Tieto funkcie majú tiež jednoduché klávesové skratky, ktoré vám umožňujú rýchlo ich vykonať. Akonáhle sa s týmito funkciami oboznámite, neváhajte ich použiť na úpravu zobrazenia polotovaru v okne DISPLAY.

_**Ikony na displeji**_

_**Ikona**_ |  _**Funkcia**_ |  _**Popis**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_pan_icon.jpg' | relative_url }}) |  Posúvanie |  Objekty v okne DISPLAY je možné dynamicky posúvať nahor, nadol, doľava alebo doprava pohybom myši pri stlačenom ľavom tlačidle myši. (Klávesová skratka: Shift + ľavé tlačidlo myši)  
![]({{ '/assets/icons/pre_icons/mo_zoom_icon.jpg' | relative_url }}) |  Zväčšenie/zmenšenie |  Okno DISPLAY je možné dynamicky zväčšiť alebo zmenšiť tak, že podržíte ľavé tlačidlo myši a pohybujete myšou nahor alebo nadol. (Klávesová skratka: Alt + ľavé tlačidlo myši)  
![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) |  Zväčšiť |  Časť okna DISPLAY je možné zväčšiť tak, že kliknete a podržíte ľavé tlačidlo myši v jednom rohu rámčeka na zväčšenie a potiahnutím kurzora vytvoríte okno, ktoré ohraničuje oblasť zväčšenia. (Klávesová skratka: Ctrl + Alt + ľavé tlačidlo myši)  
  
_**Výber bodu**_

Súradnice bodov a vzdialenosti medzi bodmi je možné získať z aktuálneho zobrazenia.

**Ikony na výber bodov**

_**Ikona**_ |  _**Funkcia**_ |  _**Popis**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) |  Meranie |  Vzdialenosti medzi ľubovoľnými dvoma bodmi je možné zmerať kliknutím na prvý bod a následným kliknutím na druhý bod. Meracie čiary zostanú na obrazovke, kým nekliknete na tlačidlo Obnoviť.  
![]({{ '/assets/icons/pre_icons/mo_select_icon.jpg' | relative_url }}) |  Vybrať |  Toto je predvolený režim zobrazenia, ktorý slúži na výber uzlov a plôch prvkov a na získanie informácií o nich. Tento režim sa používa aj pri meraní.  
  
Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujete sieť obrobku.

### Stránka „Vytvoriť sieť obrobku“

Predvolený cieľový počet prvkov je **2000** pri aktuálnom nastavení posuvníka. Táto hodnota je neaktívna, keďže sieť je nastavená na „Systém“. Používatelia môžu túto hodnotu zmeniť alebo využiť niektoré pokročilé možnosti vytvárania siete pomocou metódy „Definované používateľom“. Potvrďte toto nastavenie **Systém** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vygenerujte sieť obrobku. Vygenerovaná sieť obrobku je znázornená na obr. L1.6.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0006.jpg' | relative_url }})

Okno so sieťou obrobkov

**Ikony na grafickom displeji**

_**Ikona**_ |  _**Funkcia**_ |  _**Popis**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}) |  Zobraziť tieňované objekty |  Zobrazí všetky objekty, ktoré sú tieňované bez siete  
![]({{ '/assets/icons/pre_icons/mo_wirefrane_mode_icon.jpg' | relative_url }}) |  Zobraziť len sieť |  Zobrazí všetky objekty bez tieňovania, iba so sieťou  
![]({{ '/assets/icons/pre_icons/mo_shade_wireframe_icon.jpg' | relative_url }}) |  Zobraziť tieňovanú sieť |  Zobrazí všetky objekty tieňované pomocou siete  
![]({{ '/assets/icons/pre_icons/mo_feature_line_mode_icon.jpg' | relative_url }}) |  Zobraziť povrchovú náplasť |  Zobrazujú sa iba charakteristické čiary objektov  
![]({{ '/assets/icons/pre_icons/mo_refresh_icon.jpg' | relative_url }}) |  Obnoviť |  Obnoví okno DISPLAY a vymaže predchádzajúce meracie čiary  
![]({{ '/assets/icons/pre_icons/mo_fit_all_icon.jpg' | relative_url }}) |  Zobrazenie prispôsobenia |  Všetky objekty sa zmestia do okna DISPLAY  
![]({{ '/assets/icons/pre_icons/mo_capture_screen_image_to_file_icon.jpg' | relative_url }}) |  Zachytiť obrázok |  Zachytí okno DISPLAY a uloží ho do súboru  
![]({{ '/assets/icons/pre_icons/mo_capture_screen_to_clip_board_icon.jpg' | relative_url }}) |  Zaznamenanie obrázku do schránky |  Zaznamená okno DISPLAY a uloží ho do pamäťovej schránky  
  
Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste obrobku priradili materiál.

### Priradiť materiál obrobku

Kliknite na ikonu (Načítať materiál z knižnice) ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a prejdite do kategórie **Oceľ**. Prejdite zoznamom materiálov a vyhľadajte položku **AISI-8620[1550-2200F(850 -1200C)]** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}), čím priradíte tento materiál k obrobku. Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) môžu používatelia zobraziť alebo upraviť údaje o materiáli. V tomto laboratórnom cvičení nie sú potrebné žiadne zmeny, preto kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku s okrajovými podmienkami.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0007.jpg' | relative_url }})

Okno Knižnica materiálov

### Overiť okrajové podmienky obrobku

Keďže typ geometrie je „Axisymmetric“, pozdĺž stredovej osi obrobku bola automaticky priradená okrajová podmienka rýchlosti typu „X, Fixed“. Kliknutím na položku „**X, Fixed**“ v strome okrajových podmienok si môžete overiť, ktoré uzly sú obmedzené tak, aby sa nepohybovali v smere X. (Pozri obr. L1.8.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0008.jpg' | relative_url }})

Okno BCC obrobku

Ak potrebuje používateľ pridať ďalšie okrajové podmienky, môže v strome okrajových podmienok označiť položku „Rýchlosť“ a následne pomocou nástrojov na ľavom okraji obrazovky ![]({{ '/assets/icons/pre_icons/mo_2d_picking_option.jpg' | relative_url }}) vybrať príslušné uzly, na ktoré sa má obmedzenie vzťahovať.

V tomto laboratórnom cvičení potrebujeme iba predvolenú okrajovú podmienku „X, Fixed“ na stredovej osi, preto kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a začnite definovať hornú matricu.

### Hlavné údaje o generálnom objekte Die

Teplotu je potrebné nastaviť na **300** °F a typ objektu bude **Rigid**, ako je znázornené na obr. L1.9. Ide o predvolené nastavenia pre lisovaciu formu a my budeme používať práve tieto nastavenia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku s geometriou hornej lisovacej formy.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0009.jpg' | relative_url }})

Hlavné okno „Die General“

### Import a úprava geometrie hornej matrice

Načítajte geometriu matrice s plochým vrchom zo súboru IGS. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) otvorí (načíta) súbor „**flat top die.****igs**“. Geometria hornej matrice sa nachádza v inštalačnej zložke programu DEFORM v adresári \Tutorials.

Poznámka: Dajte pozor, aby ste nevybrali súbor FlatTopDieSI.igs.

Vždy je dobré skontrolovať geometriu, aby ste sa uistili, že je v súlade s predpismi. 

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), čím otvoríte ponuku „Skontrolovať a opraviť geometriu“. Zmeňte typ otvorenia/zatvorenia/automatického nastavenia geometrie na „otvoriť“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}). Malo by sa zobraziť hlásenie, že geometria je správna, ako je znázornené na obr. L1.10. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) opustíte ponuku.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0010.jpg' | relative_url }})

Okno na kontrolu a opravu geometrie hornej matrice

Nástroj na kontrolu geometrie by ste mali použiť na každú 2D geometriu, ktorú importujete do programu DEFORM, aj keď sa táto geometria javí ako správna.

Keďže ide o izotermickú simuláciu, nie je potrebné vytvárať sieť ani priraďovať materiál pre hornú matricu. Tieto možnosti sa preto nezobrazujú v strome operácií na stránke „Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre pohyb hornej matrice“.

### Priradiť pohyb hornej matrice

V tomto laboratórnom cvičení sa pre hornú maticu použije konštantná rýchlosť. Skontrolujte, či je zvolená možnosť „Speed“ (Rýchlosť) a smer nastavený na **–Y**. Nastavte rýchlosť na **3** **in**/s, ako je znázornené na obr. L1.11. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre dolnú maticu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0011.jpg' | relative_url }})

Okienko pre pohyb hornej matrice

### Všeobecné údaje o spodnej matrici

Teplotu je potrebné nastaviť na **300** °F a typ objektu bude **Tuhý**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou.

### Stránka o geometrii spodnej matrice

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste v editore geometrie definovali geometriu spodnej matrice. Uistite sa, že v tabuľke geometrie je vybraný formát XYR. Na definovanie geometrie zadajte geometrické body do tabuľky tak, ako je znázornené na obr. L1.12.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0012.jpg' | relative_url }})

Okno „Upraviť geometriu spodnej matrice“

Tieto body vymedzia geometriu v smere proti smeru hodinových ručičiek, aby sa zabezpečilo, že orientácia geometrie bude smerovať dovnútra geometrie, ako je znázornené na obr. L1.12. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) uzavrite definíciu geometrie a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Positioning“ (Polohovanie).

### Polohovanie

Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) nastavte polohu nástrojov tak, aby boli v kontakte s obrobkom (vo vertikálnom smere tvárnenia). Uistite sa, že obrobok je umiestnený na spodnej matrici a že horná matrica prilieha k obrobku, ako je znázornené na obr. L1.13. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na stránku kontaktu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0013.jpg' | relative_url }})

Po umiestnení objektov pomocou možnosti „Automatické umiestnenie“

### Vzťahy medzi objektmi – vytváranie trenia a kontaktu

DEFORM automaticky vytvorí vzájomné vzťahy medzi obrobkom a lisovacími formami. Nastavenia trenia sa určujú automaticky na základe **typu procesu** definovaného v hornej časti stromu procesov. Keďže sme túto simuláciu definovali ako ****kovanie za tepla****, koeficient trenia bol nastavený na hodnotu ****0,3**** pre ****šmyk****, ktorú ****systém**** sám ****definoval****, ako je znázornené na obr. L1.14.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0014.jpg' | relative_url }})

Kontaktné okno

V prípade potreby môžu používatelia prepnúť na možnosť „User-defined“ (Definované používateľom) a nastaviť rôzne hodnoty trenia. Ďalej je potrebné vytvoriť kontakt medzi objektmi. Použite predvolenú toleranciu kontaktu „Definované systémom“ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}). Na uzloch obrobku, kde bol vytvorený kontakt, by sa mal kontakt zvýrazniť. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Ovládacie prvky zastavenia“.

### Definícia primárneho zdvihu matrice

Pole „Primárny zdvih matrice“ predstavuje odhad celkového pohybu hornej matrice počas procesu tvárnenia. Celkový primárny zdvih matrice sa používa na stanovenie veľkosti časového kroku a ďalších parametrov riadenia. Ak nie je známy presný zdvih, treba použiť najpravdepodobnejšiu hodnotu. V tomto prípade sa horná matrica posunie presne o 6 palcov. Nastavte **Celkový****primárny****zdvih****matrice** na **6** palcov a zaškrtnite políčko **Presná hodnota**, ako je znázornené na obr. L1.15. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre primárny zdvih matrice.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0015.jpg' | relative_url }})

Okno počiatočného pohybu matrice

### Priradiť ovládacie prvky zastavenia

V dialógovom okne „Ovládacie prvky zastavenia“ sa nastavujú presné kritériá používané na zastavenie simulácie. Pre túto operáciu zastavte analýzu, keď **Maximálny zdvih matrice** **dosiahne** hodnotu **6** palcov. Zaškrtnite políčko **Maximálny zdvih matrice** a zadajte hodnotu **6** palcov, ako je znázornené na obr. L1.16. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku ovládacích prvkov simulácie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0016.jpg' | relative_url }})

Okno ovládacích prvkov na zastavenie

### Priradiť ovládacie prvky simulácie

Na vykonanie tejto operácie sa musí nástroj posunúť o 6 palcov, aby sa dosiahol požadovaný tvar. Na takéto jednoduché vyťahovanie by mal stačiť **počet krokov** približne **100**. Ide o predvolenú hodnotu počtu krokov pre nastavenia posúvača definované v tejto úlohe.

Zmeňte hodnotu **Krok** na **5**. To znamená, že každý piaty krok simulácie sa uloží do databázy a výsledky v týchto krokoch budú viditeľné v postprocesore.

Všimnite si, že ak sa používa iná metóda zastavenia, ako je to v tomto prípade, počet krokov nemusí byť presný.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0017.jpg' | relative_url }})

Okno ovládacích prvkov simulácie

### Potvrdiť pohyb

Kliknite na položku **Pohyb** pod položkou „Horná matica“ v strome operácií, aby ste si prezreli náhľad pohybu. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_preview_icon.jpg' | relative_url }}) (Náhľad pohybu objektu) v pravom dolnom rohu obrazovky (pozri obr. L1.11.). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_movement_play_button.jpg' | relative_url }}) (prehrávanie) (pozri obr. L1.18.) a sledujte, ako sa horná matica pohybuje cez obrobok. Tento nástroj potvrdí, že sa váš nástroj pohybuje správnym smerom a že máte dostatok krokov na dokončenie zdvihu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0018.jpg' | relative_url }})

Okno s náhľadom pohybu hornej matrice

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste opustili ponuku, a v strome operácií kliknite na **Generate****DB**, čím spustíte generovanie databázy.

### Kontrola údajov a vytvorenie databázy

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}). Program DEFORM skontroluje všetky vstupné údaje a overí, či sú definované všetky potrebné údaje. V okne Správy by sa mali zobraziť nasledujúce správy.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0001.jpg' | relative_url }})

Červené označenia signalizujú chýbajúce alebo nesprávne údaje, ktoré zabránia spusteniu simulácie. Pred vytvorením databázy je potrebné chybu opraviť.

Žlté značky označujú údaje, ktoré môžu byť pochybné a mali by sa skontrolovať. Tieto údaje by sa mali dôkladne preskúmať, pretože môžu viesť k nestabilite systému alebo k chybným (nesprávnym) výsledkom.

Preverte informácie o kontrole údajov. Ak sa nezobrazujú žiadne žlté ani červené značky, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

V okne Správy by ste mali hľadať nasledujúce správy.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0002.jpg' | relative_url }})

Keď sa zobrazí táto správa, znamená to, že nastavenia simulácie boli uložené do databázy a simulácia je pripravená na spustenie.

Kliknutím na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustíte simuláciu.

### Spustenie a sledovanie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spúšťaní) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. (Pozri obr. L1.19.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0019.jpg' | relative_url }})

Spustenie simulácie z režimu simulácie MO

V pravom hornom rohu sa aktualizuje pole „Stav“, ktoré vás informuje o tom, že simulácia práve prebieha na konkrétnom počítači.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0003.jpg' | relative_url }})

Karty „Simulačná správa“ a „Simulačný protokol“ v pravom dolnom rohu vám poskytnú informácie o priebehu simulácie.

Priebeh simulácie je možné sledovať v grafickom okne počas jej behu. V predvolenom nastavení sa grafika aktualizuje vždy, keď sa do databázy uloží nový krok. 

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0004.jpg' | relative_url }})

Ak chcete, aby sa grafika aktualizovala častejšie, môžete v roletovom menu „Update“ (v pravom dolnom rohu grafického okna) zmeniť nastavenie na „Current Step“. V 2D simuláciách to zvyčajne nie je potrebné, keďže prebiehajú veľmi rýchlo.

Osvedčeným postupom je sledovať prvých niekoľko krokov simulácie v grafickom režime simulácie, aby sa overilo, či sa pohyby nástroja a deformácia obrobku vyvíjajú podľa očakávaní.

Po dokončení simulácie sa obraz v grafickom okne prestane meniť a zobrazí sa konečný deformovaný tvar súčiastky. Posledné riadky na karte **Simulačné správy** budú signalizovať, že simulácia bola dokončená.

"******Správa*******

Simulácia bola dokončená a zastavená v časovom kroku zadanom používateľom „“.

### Výsledky kontroly v režime príspevku

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Zoznam krokov a ovládacie prvky prehrávania

V grafickom okne sa zobrazujú výsledky simulácie. Uložené kroky sú uvedené v prehliadači krokov v spodnej časti grafického okna, ako je znázornené na obr. L1.20.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0020.jpg' | relative_url }})

Krokový prehliadač pre prevádzku v núdzovom režime

Ovládacie prvky hry slúžia na:

![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) **Prehrávanie dopredu**: Zobrazuje kroky jeden po druhom, až kým sa od aktuálne vybraného kroku nezobrazí posledný krok.

![]({{ '/assets/icons/pre_icons/mo_preview_stop_button.jpg' | relative_url }}) **Stop** : Zastaví prehrávanie (dopredu alebo dozadu) krokov.

**![]({{ '/assets/icons/pre_icons/mo_preview_one step_forward_button.jpg' | relative_url }})Jeden krok vpred** : Prejsť na ďalší uložený krok v zozname krokov.

![]({{ '/assets/icons/pre_icons/mo_preview_last_step_button.jpg' | relative_url }}) **Preskočiť na koniec** : Preskočí na posledný uložený krok v zozname krokov.

![]({{ '/assets/icons/pre_icons/mo_preview_play_back_button.jpg' | relative_url }}) **Prehrávať spätne**: Zobrazuje kroky jeden po druhom v opačnom poradí, až kým sa od aktuálneho vybraného kroku nezobrazí prvý krok.

![]({{ '/assets/icons/pre_icons/mo_preview_one_step_back_button.jpg' | relative_url }}) **Jeden krok späť**: Posuňte zoznam krokov späť o jeden uložený krok.

**![]({{ '/assets/icons/pre_icons/mo_preview_last_step_button.jpg' | relative_url }})Preskočiť na začiatok** : Vráťte zoznam krokov späť na prvý uložený krok.

_**Graf zaťaženia a zdvihu**_

Kliknite na ikonu ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) (zaťaženie – zdvih) v nástrojoch stĺpika. Vykreslite graf závislosti zaťaženia Y (os Y) od zdvihu (os X) pre hornú matricu výberom tlačidla ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) (pozri obr. L1.21.). Graf zobrazuje zaťaženie počas celej simulácie. Zvislá lišta označujúca krok udáva aktuálny krok.

Kliknutím na ľubovoľný bod na grafe zaťaženia a zdvihu (alebo na akýkoľvek graf v programe DEFORM) sa zobrazia výsledky v danom kroku. Prípadne je možné vybrať ľubovoľný krok zo zoznamu krokov a vertikálny ukazovateľ krokov preskočí na tento bod v simulácii. Graf je možné odstrániť kliknutím pravým tlačidlom myši na graf a výberom možnosti **Odstrániť**.

Poznámka: Grafy sa štandardne otvárajú v tom istom grafickom okne ako simulácia. Ak chcete dosiahnuť podobný vzhľad ako na obrázku nižšie, prejdite do nastavení „Options ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})“ a v časti „Graph Display“ zaškrtnite políčko vedľa položky „New window“ a potom stlačte . Znovu vykreslite graf, aby ste videli zmeny.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0021.jpg' | relative_url }})

Graf zdvihu hornej matrice

_**Grafy stavových premenných**_

  * **Graf rýchlosti**

Vyberte krok 75 (alebo akýkoľvek iný medzistupeň na lište výberu krokov). Kliknite na ikonu stavovej premennej ![]({{ '/assets/icons/post_icons/mo_vel_sv_icon.jpg' | relative_url }}) (Celková rýchlosť) v nástrojoch Post – Stavové premenné. Kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) otvoríte dialógové okno s vlastnosťami stavovej premennej. Zvoľte typ zobrazenia ![]({{ '/assets/icons/post_icons/mo_vector_plot_button.jpg' | relative_url }}). Okamžité rýchlosti sa zobrazujú ako vektory v zvolenom časovom kroku. Farby šípok označujú veľkosť rýchlosti. (Pozri obr. L1.22.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0022.jpg' | relative_url }})

Graf rýchlostného vektora s grafom zdvihu zaťaženia pre hornú maticu

  * **Graf efektívneho napätia**

V dialógovom okne „State Variable“ vyberte **Deformácia**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Efektívna**. Nastavte mierku na **Globálnu** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Efektívna deformácia predstavuje mieru deformácie počas simulovaného procesu. Pri tvárnení za studena to súvisí s pracovným spevnením.

Prejdite si simuláciu a sledujte, ako sa napätie mení v priebehu tvarovania dielu. Pri **globálnom** škálovaní farebná lišta znázorňuje maximálny rozsah premennej kdekoľvek v obrobku.

Nastavte mierku na **Lokálnu** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Spustite simuláciu. V každom kroku sa stavové premenné preškálujú na maximálnu hodnotu v danom kroku.

Vyberte zobrazenie ![]({{ '/assets/icons/post_icons/mo_solid_plot_button.jpg' | relative_url }}) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Okraje kontúr sa zmenia na ostré hrany (pozri obr. L1.23.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0023.jpg' | relative_url }})

Kontúra efektívnej premennej deformácie v miestnom aj globálnom meradle

Keď dokončíte prezeranie výsledkov, kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste opustili okno „State variable“. Mierku a typ grafu môžete zmeniť aj pomocou možností, ktoré sa zobrazia po kliknutí pravým tlačidlom myši na lištu s vrstevnicami.

Kliknite na tlačidlo režimu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) MO, aby ste prešli do režimu Pre a mohli pokračovať v ďalšom laboratórnom cvičení.

### Ukončiť operáciu v kováčskej dielni

#### Vložiť novú operáciu

K plochému dielu pridáme operáciu dokončovacieho kovania. Na karte Explorer v ľavej časti používateľského rozhrania prejdite na položku **Forming**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Single a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky **[2D] Forming Express**, ako je znázornené na obr. L1.24.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0024.jpg' | relative_url }})

Pridanie operácie z Průzkumníka

V editore operácií bude pridaná nová dlaždica operácie (pozri obr. L1.25.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0025.jpg' | relative_url }})

Pridaná operácia rýchleho tvarovania 

Kliknite na dlaždicu **Forming**. Zobrazí sa vám vyskakovacie okno s výzvou na výber medzi interaktívnym a dávkovým nastavením. Interaktívne nastavenie umožňuje priamejšiu kontrolu nad vstupnými údajmi. Dávkové nastavenie však zaručuje, že bude možné zálohovať a znovu spustiť celý projekt od začiatku bez prerušenia. _Pre takmer všetky projekty poskytuje dávkové nastavenie väčšiu flexibilitu._

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0026.jpg' | relative_url }})

Vyskakovacie okno s typom nastavenia pre operáciu 2D tvárnenia

V tomto dialógovom okne kliknite na ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}), ako je znázornené na obr. L1.26. V stromovej štruktúre procesov sa otvorí druhá operácia. Všimnite si, ako sú objekty v prvej operácii teraz prepojené s druhou operáciou a zobrazujú sa ako „Read from DB“. Všetky objekty sa v druhej operácii zobrazujú červenou farbou, čo znamená, že sa načítajú z predchádzajúcej operácie v databáze.

Táto operácia preberá vlastnosti predchádzajúcej operácie, takže aj táto operácia bude izotermickým procesom tepelného kovania.

#### Importovacie matrice

Pre túto operáciu sa budú importovať nové formy, takže formy sa naozaj nebudú načítať z databázy tak ako obrobok. Toto sa dá ľahko zmeniť. Pri importe nižšie uvedených foriem nezabudnite, že geometrie sa nachádzajú v inštalačnom priečinku DEFORM v adresári \Tutorials.

#### Horná matrica

Kliknite na položku „Top Die“ v strome operácií. Zmeňte typ objektu na **Define**, ako je znázornené na obr. L1.27. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Geometry“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0027.jpg' | relative_url }})

Okienko hornej matrice

#### Geometria hornej matrice

Načítajte geometriu „**gear top die.****IGS**“. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) otvorte (načítajte) súbor „gear top die.IGS“. Geometria hornej matrice sa nachádza v inštalačnej zložke DEFORM v adresári \Tutorials. Pomocou ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) skontrolujte geometriu a upravte tieňovanie tak, aby bolo správne na vnútornej strane dielu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Top die Movement (Pohyb hornej matrice).

V ďalšej časti tohto nastavenia definujeme kritérium zastavenia na základe vzdialenosti medzi maticami v medzere na odrezávanie. Na tento účel musíme na maticiach určiť referenčné body.

V pravom dolnom rohu stránky s geometriou kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}), aby sa tlačidlo zmenilo na modré.

Pomocou myši vyberte výstupok na hornej forme, ktorý zodpovedá ploche pre výstupok, ako je znázornené na obr. L1.28.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0028.jpg' | relative_url }})

Určenie referenčného bodu pre geometriu hornej matrice

#### Priradiť pohyb hornej matrice

Rýchlosť **3** palcov za sekundu je už definovaná z predchádzajúcej operácie, takže nie sú potrebné žiadne zmeny. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Spodná matrica“.

#### Spodná matrica

Zmeňte typ objektu na **Definovať**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Geometria.

#### Geometria spodnej matrice

Načítajte geometriu „**gear bottom die.****IGS**“. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) otvorte (načítajte) súbor „gear bottom die.IGS“. Geometria spodnej matrice sa nachádza v inštalačnej zložke DEFORM v adresári \Tutorials. Použite ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) na kontrolu geometrie a opravte tieňovanie tak, aby bolo správne na vnútornej strane dielu. V pravom dolnom rohu stránky s geometriou kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}), aby sa tlačidlo zmenilo na modré. Pomocou myši vyberte a označte bod uvedený nižšie na odlievacej ploche spodnej matrice, ako je znázornené na obr. L1.29.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0029.jpg' | relative_url }})

Určenie referenčného bodu pre geometriu spodnej matrice

#### Plánované polohovanie

Keďže sa obrobok načítava z databázy po predchádzajúcej operácii tvarovania, jeho rozmery a tvar sa môžu zmeniť, ak sa projekt spustí od začiatku. Z tohto dôvodu je lepšie umožniť flexibilné polohovanie nástrojov vo vzťahu k obrobku, ako im nastaviť pevnú polohu.

V programe DEFORM existuje operácia nazývaná „Plánované polohovanie“, ktorá umožňuje presunúť nástroje do kontaktu s obrobkom ľubovoľného tvaru vždy, keď sa obrobok načíta z predchádzajúcej operácie. 

V strome procesov prejdite na položku **Plánované polohovanie** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridajte operáciu polohovania. 

Najprv nastavíme, aby sa spodná forma posunula smerom k obrobku. 

Vyberte **Interferencia** a ako **Polohovací****objekt** zvoľte **Spodná****matrica** a ako **Referenčný****objekt** zvoľte **Obrobok**. Nastavte smer priblíženia na **Y** (hore). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). 

Upozorňujeme, že nástroj sa v tomto momente nepohybuje, ale jeho polohovanie sa vykoná pri generovaní databázy pre túto operáciu.

Kliknite opäť na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), aby ste naplánovali druhé polohovanie. Vyberte možnosť **Interferencia** a nastavte polohu **hornej** **matrice** smerom nadol (**-Y**) voči **obrobku**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). (Pozri obr. L1.30.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na stránku Kontakt

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0030.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

#### Vzťahy medzi objektmi

V dialógovom okne „Kontakt“ sa ako prvá operácia použije ten istý **systémom** **definovaný** kontakt so šmykom **0,3**. Nie sú teda potrebné žiadne zmeny. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Primárny zdvih matrice“.

#### Zdvih primárneho valca

Pri definovaní uvedených kritérií zastavenia sme zistili, že medzera medzi maticami bola približne **1,75** palca (pred naplánovaným polohovaním). Dobrý odhad toho, o koľko sa horná matrica počas tejto operácie posunie, je približne 1,5 palca. Nastavte celkový primárny zdvih matrice na 1,5 palca. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím prejdete na stránku Ovládacie prvky zastavenia (pozri obr. L1.31.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0031.jpg' | relative_url }})

Okno primárneho zdvihu matrice

#### Ovládacie prvky na zastavenie

Na rozdiel od merania vzdialenosti pohybu nástroja, ako sme to robili v prvej operácii, tento proces ukončíme pri pevne stanovenej vzdialenosti medzi nástrojmi. V tomto prípade nastavíme hrúbku prebytku na 0,2 in.

Vzdialenosť blesku sa meria v referenčných bodoch určených na hornej a dolnej matrici.

V stromovej štruktúre procesu kliknite na položku „Ovládacie prvky zastavenia“. Zaškrtnite políčko **Vzdialenosť****medzi****objektmi** a nastavte hodnotu na **0,2** palca. Vyberte objekt 1 ako **hornú****matricu** a objekt 2 ako **spodnú****matricu** a vyberte smer **Y**. Po dokončení nastavení sa v grafickom okne zobrazia referenčné body a aktuálna vzdialenosť (pozri obr. L1.32.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku Simulačné ovládacie prvky.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0032.jpg' | relative_url }})

Okno s ovládacími prvkami na zastavenie 

#### Ovládacie prvky simulácie

Kliknite na položku „Simulation controls“ (Ovládacie prvky simulácie). Chceme prejsť vzdialenosť približne 1,5 in. v 100 krokoch, takže použijeme krokový prírastok 0,015 in/krok. NECHCE sa však stať, aby simulácii došli kroky, keďže je nastavené ďalšie kritérium zastavenia (vzdialenosť medzi maticami). Keďže chceme mať pri opätovnom spustení tohto prípadu flexibilitu, nastavíme počet krokov simulácie na 1000, nie na 100. Tým sa zabezpečí, že ak projekt spustíme znovu s inými nastaveniami, nebudeme sa musieť obávať vyčerpania počtu krokov. Ukončenie simulácie bude vždy riadiť vzdialenosť medzi nástrojmi.

Zmeňte časový krok zo „System“ na **User**. Zmeňte **Počet krokov** na **1000** a **Krok** na **5** a nastavte **konštantný****posun** na hodnotu **0,015** in (pozri obr. L1.33.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0033.jpg' | relative_url }})

Okno ovládacích prvkov simulácie

#### Vytvoriť databázu

Systém sa na krátko pozastaví, kým vykoná naplánované polohovanie a vytvorenie kontaktu. Farba obrobku sa zmení z červenej (Načítané z databázy) na žltú (Plastový objekt).

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Kliknutím na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustíte simuláciu.

#### Spustiť a sledovať simuláciu

Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) a potom zrušte zaškrtnutie políčka „Odoslať úlohu do simulačnej fronty“. Zrušením zaškrtnutia tejto možnosti sa úloha spustí na lokálnom počítači. Použite predvolenú možnosť **Začať od posledného záporného kroku**. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) spustíte simuláciu.

#### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

Prejdite všetky kroky. Všimnite si, že diel úplne nevyplňuje dutinu formy (pozri obr. L1.34.). 

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0034.jpg' | relative_url }})

Tvar obrobku v poslednom kroku druhej operácie
