---
lang: sk
title: "Laboratórium 2D operácií prenosu tepla"
---

# Laboratórium 2D prevádzky prenosu tepla

V tomto laboratórnom cvičení si ukážeme, ako nastaviť typickú simuláciu viacerých operácií zahŕňajúcu rôzne operácie prenosu tepla a kovania. Počas tohto cvičenia sa tiež pokúsime poukázať na rôzne funkcie systému, ktoré môže používateľ využiť v iných typoch situácií s viacerými operáciami. Tieto operácie môžu predstavovať súbor operácií s tepelným odpočinkom (pozri obr. 2DHTRL1.1.), súbor deformačných operácií s výmenou foriem medzi jednotlivými operáciami alebo kombináciu operácií prenosu tepla a deformačných operácií (pozri obr. 2DHTRL1.1.). Model je 2D osovo symetrický a nasledujúce 3D obrázky slúžia iba na ilustračné účely.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0001.jpg' | relative_url }})

3D znázornenie procesov tepelného odpočinku a tvarovania

V tomto laboratóriu sme nastavili model so štyrmi operáciami, ktorý zahŕňa jednu operáciu „ohrev v peci“, „prenos tepla“, „odpočinok v teple“, jednu operáciu „deformácia“ a operáciu „udržanie tepla“. Súčiastka je valcovitý obrobok, ktorý najprv prejde operáciou ohrevu v peci po dobu jednej hodiny pri teplote 2000 F, na čo nadväzuje operácia prenosu tepla trvajúca 15 sekúnd počas presunu z pece do formovacej stanice. Po tejto operácii nasleduje operácia tepelného odpočinku, pri ktorej obrobok odpočíva na tvárniacich maticiach po dobu 4 sekúnd pred operáciou deformácie. Operácia deformácie prebieha počas špecifického zdvihu (7,25”) hornej matice. Na záver nasleduje fáza udržiavania teploty trvajúca 4 sekundy. Celú sekvenciu je možné nastaviť pomocou tohto systému a všetky operácie je možné simulovať bez zásahu používateľa v dávkovom režime.

1.1. Vytvorenie novej úlohy a pridanie operácií

1.2. Operácia 1: Nastavenie ohrevu pece

1.3. Operácia 2: Preprava vzduchu

1.4. Operácia 3: Tepelné odležanie

1.5. Operácia 4: Tvarovanie

1.6. Operácia 5: Teplo v obydlí

1.7. Simulácia problému

1.8. Následné spracovanie

## Vytvorenie nového problému a pridanie operácií

### Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2.) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main. 

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. 2DHTRL1.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Anglický**“. Názov úlohy zadajte ako „******Heat_Transfer_Operations**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Vyskakovacie okno s novým problémom

Otvorí sa sprievodca MO spolu s oknom na zadanie názvu projektu (pozri obr. 2DHTRL1.3.), pričom definovaný názov úlohy sa aktualizuje na „**Heat_Transfer_Operations**“ ako názov projektu a aktualizuje sa aj vybraný systém jednotiek. Používateľ môže tiež zmeniť systém jednotiek a pridať operáciu výberom z roletového zoznamu Prvá operácia a zaškrtnutím príslušného políčka (pozri obr. 2DHTRL1.3.). Pomocou možnosti Kopírovať existujúci projekt môžeme importovať predtým uložené projekty ako nový projekt. Vyberte **F****irst operation** ako operáciu **2D Heat transfer** a zaškrtnite políčko, aby ste pridali operáciu prenosu tepla ako prvú operáciu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0003.jpg' | relative_url }})

Okno na otvorenie nového projektu v nástroji MO Wizard

### Pridávanie ďalších operácií

Sprievodca viacerými operáciami otvorí nový projekt s jednou 2D operáciou prenosu tepla. Pridajte ďalšie dve operácie prenosu tepla pre prenos vzduchu a odpočinok, jednu operáciu tvarovania a operáciu prenosu tepla pre zotrvanie po tvarovaní zo zoznamu operácií v Průzkumníku kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ako je znázornené na obr. 2DHTRL1.4.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0004.jpg' | relative_url }})

Pridávanie operácií

## Operácia 1: Nastavenie vykurovania pece

Pre prvú operáciu prenosu tepla zmeňte názov operácie na „**Ohrev v peci**“ dvojitým kliknutím na názov operácie v okne Editor operácií, ako je znázornené na obr. 2DHTRL1.5, a stlačte klávesu **Enter** na klávesnici.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0005.jpg' | relative_url }})

Prvú operáciu nazvite „Vyhrievanie v peci“

### Vyberte typ geometrie

V tomto laboratórnom cvičení používame osovo symetrické geometrie, preto v okne typu geometrie zaškrtnite políčko **2D osovo symetrické**, ako je znázornené na obr. 2DHTRL1.4., a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

### Výber typu prenosu tepla pre vykurovanie pece

Pre režim kúrenia v peci vyberte typ prenosu tepla **Teplo v peci**, ako je znázornené na obr. 2DHTRL1.6. Tým sa nastavia predvolené nastavenia prenosu tepla pre režim kúrenia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0006.jpg' | relative_url }})

Výber typu prenosu tepla pre vykurovanie pece

### Nastavenie prevádzkových podmienok pre ohrev v peci

Nastavte dobu ohrevu na **3600** sekúnd (jedna hodina ohrevu) pri teplote pece alebo okolitej teplote **2000** °F, ako je znázornené na obr. 2DHTRL1.7, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0007.jpg' | relative_url }})

Nastavenia prevádzkových podmienok pre ohrev v peci

### Výber ovládacích prvkov simulácie pre ohrev pece

Nechajte zaškrtnutý len režim „Heat Transfer“, pretože sa modeluje iba prenos tepla, ako je znázornené na obr. 2DHTRL1.8, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0008.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre vykurovanie pece

### Import materiálu obrobku

V okne „Material“ načítajte materiál **AISI-8620** z knižnice materiálov DEFORM v kategórii **Steel** pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To môžete urobiť tak, ako je znázornené na obr. 2DHTRL1.9, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Materiál je možné načítať aj zo zoznamu materiálov v prehliadači. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na stránku so zoznamom materiálov.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0009.jpg' | relative_url }})

Import materiálu obrobku z knižnice DEFORM

### Skontrolujte vlastnosti materiálu

Na stránke materiálu **AISI-8620**, kde chcete skontrolovať tepelné vlastnosti materiálu, vyberte kartu **Thermal** (pozri obr. 2DHTRL1.10.) a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Definovať) vedľa položky Tepelná vodivosť, aby ste mohli sledovať priebeh tepelnej vodivosti v závislosti od teploty, ako je znázornené na obr. 2DHTRL1.11.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0010.jpg' | relative_url }})

Okno na definovanie vlastností materiálu pre AISI-8620

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0011.jpg' | relative_url }})

Funkcia tepelnej vodivosti na základe údajov o teplote pre materiál AISI-8620

Podobne kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Definovať) vedľa položky „Teplotná kapacita“ a prezrite si údaje o funkcii, ako je znázornené na obr. 2DHTRL1.12.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0012.jpg' | relative_url }})

Funkcia tepelnej kapacity na základe údajov o teplote pre materiál AISI-8620

Pre emisivitu a hustotu hmoty je definovaná konštantná hodnota, ako je znázornené na obr. 2DHTRL1.10. Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre okno „Vlastnosti materiálu“ a „Objekt“, keďže na operáciu ohrevu stačí iba objekt „Obrobok“.

### Definícia obrobku

V okne „Objekt obrobku“ ponechajte typ objektu ako „**Plast**“ (pozri obr. 2DHTRL1.13.). V tejto fáze môže používateľ tiež zadať počiatočnú teplotu obrobku ako **68°** F. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte a načítajte geometriu obrobku.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0013.jpg' | relative_url }})

Definícia objektu obrobku

### Import geometrie obrobku

Na stránke Geometria kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a importujte súbor „**Disk_wkp****.****igs**“, ako je znázornené na obr. 2DHTRL1.14. Ďalšie možnosti dostupné v tejto fáze sú definovanie obrobku z primitívnej geometrie a 2D geometrického editora pomocou možností ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}). Ak systém požiada o zadanie umiestnenia 2D\LABS\ ako umiestnenia knižnice, kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0014.jpg' | relative_url }})

Importovať geometriu z knižnice DEFORM

Po importovaní geometrie kliknite na možnosť ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste importovanú geometriu skontrolovali a v prípade potreby opravili (pozri obr. 2DHTRL1.15.). V závislosti od typu importovanej geometrie sa po kliknutí na „Skontrolovať a opraviť geometriu“ uistite, že značka ohraničenia objektu (tieňovaná oblasť vedľa ohraničenia) zostáva vnútri ohraničenia. Ak sa systému nepodarí geometriu opraviť, vyberte jednu z možností „Systém zistil“, „Uzavreté“ a „Otvorené“, aby ste geometriu opravili.

Ak orientácia geometrie nie je správna, systém sa pokúsi túto chybu opraviť počas fázy vytvárania siete, odporúča sa však skontrolovať a opraviť geometriu objektu už pri jej importe. Tento postup zostáva rovnaký vždy, keď potrebujeme importovať geometriu objektu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0015.jpg' | relative_url }})

Kontrola a oprava geometrie

### Vytvorenie siete obrobku

Vytvorte sieť s použitím 2000 prvkov (pozri obr. 2DHTRL1.16.). V expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) je k dispozícii aj kompletná škála možností vytvárania sietí, ak potrebujete mať väčšiu kontrolu nad vytvorenou sieťou. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0016.jpg' | relative_url }})

Okno na generovanie siete

### Priradiť materiál obrobku

Ak chcete obrobku priradiť materiál, vyberte v okne materiálov materiál „**AISI****-8620**“. Postupujte podľa obrázku 2DHTRL1.17. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0017.jpg' | relative_url }})

Okno na výber materiálu objektu

### Definovanie okrajových podmienok obrobku

Na stránke BCC skontrolujte, či je pre celý vonkajší povrch polotovaru predvolene priradená voľba „Výmena tepla s prostredím“ (ktorá nezahŕňa os, keďže tieto uzly sa nachádzajú vnútri objektu), a to kliknutím na položku „Definované“ v časti „Výmena tepla s prostredím“. Predvolené BCC sa priradia automaticky na základe výberu typu úlohy ako osovo symetrickej (pozri obr. 2DHTRL1.18.).

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0018.jpg' | relative_url }})

Definícia okrajových podmienok pre ohrev v peci

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí okno „Ovládacie prvky krokov“, keďže nie je definované polohovanie objektov a je potrebné definovať ovládacie prvky tepelného zastavenia.

### Nastavenie krokových regulátorov pre vykurovanie pece

Nastavte **počet simulačných krokov** na **100**, pričom dĺžka každého kroku je **36** sekúnd, a ukladajte výsledky každých **10** **krokov** (pozri obr. 2DHTRL1.19.). Nastavenia pokročilých ovládacích prvkov simulácie sú k dispozícii v expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do fázy generovania databázy.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0019.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre vykurovanie pece

### Vytvoriť databázu

V etape vytvárania databázy môže používateľ skontrolovať údaje potrebné na analýzu a pokračovať vo vytváraní databázy (pozri obr. 2DHTRL1.20.). Ako prvú z viacerých operácií musí používateľ vytvoriť databázu. Pre všetky nasledujúce operácie stačí len nastaviť procesné údaje a parametre simulácie. V tejto fáze má používateľ tiež možnosť importovať súbor kľúčových slov, čo je obzvlášť užitočné pre neskoršie operácie. Funkčnosť tejto funkcie „Pridať používateľsky definovaný súbor kľúčových slov“ bude rozoberaná v neskorších častiach tohto laboratórneho cvičenia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}), aby ste prešli k ďalšej operácii „Air Transfer“.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0020.jpg' | relative_url }})

Okno „Vytvorenie databázy“ pre prvú operáciu

## Operácia 2: Letecký transport

V rámci tohto pracovného kroku sme nastavili fázu odvodu tepla do ovzdušia, pri ktorej trvá presun dielu z pece do formovacej stanice 15 sekúnd. Počas tejto doby sa diel, ktorého teplota je približne 2000 °F, čiastočne ochladí na teplotu okolitého vzduchu.

### Výber typu prenosu tepla pri prenose vzduchom

Pomenujte operáciu ako „**Air Transfer**“ dvojitým kliknutím na položku „Názov operácie“ v editore operácií a stlačením klávesy Enter na klávesnici operáciu zatvorte. Vyberte typ prenosu tepla „**Transfer through air**“, ako je znázornené na obr. 2DHTRL1.21, a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0021.jpg' | relative_url }})

Výber typu prenosu tepla pre prenos vzduchom

### Nastavenie prevádzkových podmienok pre prepravu vzduchu

Nastavte podmienky procesu na **doba prenosu** **15** sekúnd v prostredí s teplotou **68** °F s použitím predvoleného koeficientu konvekcie, ako je znázornené na obr. 2DHTRL1.22.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0022.jpg' | relative_url }})

Nastavenia prevádzkových podmienok pre vzduchový transport

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno „Objekt obrobku“, a potvrďte typ objektu ako „Načítať z databázy“ (pozri obr. 2DHTRL1.23.). To znamená, že teplotná história obrobku z operácie ohrevu v peci bude k dispozícii ako vstupné údaje pre túto operáciu. Kliknite na vetvu „Ovládanie krokov“ v strome operácií.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0023.jpg' | relative_url }})

Načítanie výberu objektu z databázy pre obrobok

### Nastavenie definície kroku pre vzduchový prenos

V okne „Step Controls“ nastavte **15** krokov s krokom **1** sekunda a ukladajte každých **5** krokov (pozri obr. 2DHTRL1.24.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0024.jpg' | relative_url }})

Krok: Nastavenia pre funkciu Air Transfer

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) otvoríte operáciu „Heat resting“ (pozri obr. 2DHTRL1.25.), ktorú databáza vygeneruje pre nasledujúce operácie počas simulácie v dávkovom režime.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0025.jpg' | relative_url }})

Okno na vytvorenie databázy pre následné operácie v dávkovom režime

**Poznámka**:

V tejto fáze má používateľ možnosť pridať ďalšie údaje o objektoch alebo simuláciách výberom možnosti „Pridať súbor s používateľsky definovanými kľúčovými slovami“ (pozri obr. 2DHTRL1.22.). Upozorňujeme, že ak bude toto kľúčové slovo definované, systém ho načíta pred vytvorením databázy pre druhú operáciu. V tejto fáze sa však nebude vykonávať žiadna kontrola údajov definovaných používateľom z tohto súboru kľúčových slov.

## Operácia 3: Odpočinok pri teple

V tomto pracovnom kroku nastavujeme prenos tepla tak, že obrobok spočíva na tvárniacich maticiach po dobu 4 sekúnd pred samotnou deformáciou.

### Výber typu prenosu tepla pri tepelnej stabilizácii

Pomenujte operáciu ako „**Teplotné odležanie**“ dvojitým kliknutím na názov operácie v editore operácií a stlačením klávesy Enter na klávesnici operáciu zatvorte. Vyberte typ prenosu tepla „**Odležanie na matrici**“, ako je znázornené na obr. 2DHTRL1.26, a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0026.jpg' | relative_url }})

Výber typu prenosu tepla pre prevádzku s tepelným odpočinkom

### Nastavenie podmienok procesu pre tepelné odležanie

Nastavte podmienku procesu na **doba odpočinku****** v trvaní **4** sekúnd v prostredí s teplotou 68°F s použitím predvoleného konvekčného koeficientu, ako je znázornené na obr. 2DHTRL1.27. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0027.jpg' | relative_url }})

Nastavenia prevádzkových podmienok pre operáciu tepelného odležania

### Pridať objekty s kockami

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno „Object“, a potvrďte hodnotu „Number of Objects“ ako 3 (celkový počet objektov), keďže pre operáciu odležania budeme vkladať obe formy pri teplote 300°F. Teraz vidíme, že strom objektov je rozbalený a obsahuje obe matrice, ktorých podrobnosti budeme teraz definovať.

### Definícia hornej matrice

Kliknite na položku „Top Die“ v strome operácií, aby ste definovali lisovacie formy. Potvrďte teplotu hornej lisovacej formy 300 °F a typ objektu „rigid“, ako je znázornené na obr. 2DHTRL1.28. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0028.jpg' | relative_url }})

Okno definície hornej matrice pre operáciu tepelného odpočinku

### Import geometrie hornej matrice

V okne „Top die Geometry“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a načítajte súbor „**Disk_top****.igs**“, ako je znázornené na obr. 2DHTRL1.29.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0029.jpg' | relative_url }})

Import geometrie hornej matrice z knižnice DEFORM

### Vytvoriť sieť hornej formy

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vytvorte sieť s 600 prvkami, ako je znázornené na obr. 2DHTRL1.30. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s materiálmi.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0030.jpg' | relative_url }})

Vytvorenie siete pre hornú matricu

### Materiál na výrobu foriem

Načítajte materiál **AISI-H13** z knižnice materiálov DEFORM, z kategórie **Die_material**, pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice), ako je znázornené na obr. 2DHTRL1.31. Vyberte načítaný materiál a priraďte ho k hornej matrici.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0031.jpg' | relative_url }})

Načítavanie materiálu formy z knižnice DEFORM

### Definícia hornej matrice BCC

V okne „Definovať BCC“ sa BCC „Výmena tepla s okolím“ automaticky priradí ku všetkým stranám okrem strany osi. Kliknutím na vetvu „Definované“ pod BCC „Výmena tepla s okolím“ potvrďte definíciu BCC (pozri obr. 2DHTRL1.32.). Kliknite na vetvu „Spodná matrica“ v prevádzkovom strome, aby ste spustili matricu.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0032.jpg' | relative_url }})

Výmena tepla s prostredím BCC pre hornú matricu

### Definícia spodnej matrice

Pre spodnú formu je povolená aj teplota objektu 300°F a typ tuhého objektu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

### Import geometrie spodnej matrice

V okne „Geometria spodnej formy“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a načítajte súbor „**Disk_btm****.igs**“, ako je znázornené na obr. 2DHTRL1.33. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku vytvorenia siete.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0033.jpg' | relative_url }})

Načítanie geometrie spodnej matrice z knižnice DEFORM

### Vytvorenie siete spodnej formy

Vytvorte sieť s použitím 600 prvkov, ako je znázornené na obr. 2DHTRL1.34.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0034.jpg' | relative_url }})

Vytvorenie siete pre spodnú formu

### Priradiť materiál pre spodnú formu

Zoznamu materiálov vyberte materiál **AISI-H13** a priraďte ho k spodnej matrici. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na okrajové podmienky.

### Definícia spodnej matrice BCC

Potvrďte automaticky priradenú výmenu tepla s prostredím BCC na všetkých stranách okrem strany osi kliknutím na položku „Definované“ v časti „Výmena tepla s prostredím BCC“, ako je znázornené na obr. 2DHTRL1.35. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s nastavením polohy.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0035.jpg' | relative_url }})

Výmena tepla s prostredím BCC pre spodnú formu

### Poloha hornej matrice

Teraz z položky „Polohovanie“ prejdite do ponuky „Polohovanie objektov“, kde najskôr posunieme hornú matricu ďalej od obrobku, aby teplo z tepelného odpočinku zohľadňovalo prenos tepla medzi obrobkom a spodnou matricou.

Na to najprv kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}). Vyberte hornú maticu, metódu „**Offset**“ a vektor vzdialenosti (x=0, y=4). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) sa horná matrica posunie ďalej od obrobku. (pozri obr. 2DHTRL1.36.)

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte okno „Polohovanie objektu“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) nastavíte plánovanú polohu spodnej matrice.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0036.jpg' | relative_url }})

Polohovanie hornej matrice v kľudovom režime

### Poloha spodnej matrice v rozvrhu

Spodnú formu musíme umiestniť vzhľadom na objekt „Workpiece“ z databázy, preto musíme jej polohu naplánovať už pri generovaní databázy. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať) a vyberte „Polohovací objekt“ ako spodnú maticu, metódu „Interferencia“ vo vzťahu k „Obrobku“ v smere **+Y** (pozri obr. 2DHTRL1.37.). Upozorňujeme, že podrobnosti polohovania pridané v naplánovanom polohovaní sa zohľadnia pred generovaním údajov o vzájomných vzťahoch medzi objektmi pre túto operáciu. V tomto bode nebude viditeľný žiadny fyzický pohyb foriem. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0037.jpg' | relative_url }})

Plánované polohovanie spodnej formy vo vzťahu k obrobku

### Naplánovanie vzťahov medzi objektmi pre tepelné odležanie

Vyberte kontakt typu **Používateľ**, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať vzťah) a vyberte „Spodná forma“ ako hlavný prvok a „Obrobok“ ako podriadený prvok, ako je znázornené na obr. 2DHTRL1.38.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0038.jpg' | relative_url }})

Vzťah medzi obrobkom a spodnou matricou

Kliknite na tlačidlo vzťahu ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) (Upraviť) a v sekcii „Teplo“ vyberte z roletového menu možnosť „**Voľný pokojový stav**“, čím definujete koeficient prenosu tepla medzi objektmi, ako je znázornené na obr. 2DHTRL1.39. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno úprav. Tým sa počas simulácie vytvorí kontakt medzi objektmi na začiatku fázy voľného stavu. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno ovládania krokov.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0039.jpg' | relative_url }})

Výber koeficientu prenosu tepla medzi objektmi v pokojovom stave

### Nastavenie krokov pre tepelné odležanie

V okne „Step Controls“ nastavte **počet krokov** na **10**, pričom každý krok trvá **0,4** s a každý **druhý** krok sa uloží (pozri obr. 2DHTRL1.40.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) v okne Generate DB a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) v okne Database generation, aby ste pokračovali v definovaní operácie tvárnenia.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0040.jpg' | relative_url }})

Ovládacie prvky krokov pre prevádzku s tepelným odpočinkom

## Operácia 4: Tvarovanie

Operácia tvárnenia prebieha počas konkrétneho zdvihu (7,25”) hornej matrice. Keďže všetky objekty vyrábame podľa údajov z databázy, údaje o objektoch pochádzajú z predchádzajúcich operácií vrátane tepelnej histórie. Preto všetky objekty z operácie tepelného odpočinku prejdú do operácie tvárnenia, ako je znázornené na obr. 2DHTRL1.41.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0041.jpg' | relative_url }})

Odovzdávanie objektov na čítanie z databázy

### Výber simulačných režimov pre tvárnenie

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím otvoríte okno „Typ geometrie“, a potvrďte predvolené režimy simulácie vybrané v časti „Ovládacie prvky simulácie“ (Deformácia a Prenos tepla), ako je znázornené na obr. 2DHTRL1.42. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno s objektom.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0042.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre operáciu tvárnenia

Na stránke objektov overte, či je typ údajov všetkých objektov nastavený na „Načítané z databázy“ a či nie je definovaný žiadny pohyb; kliknite na vetvu „Horná matrica – pohyb“ v rámci operácie, aby ste definovali ovládacie prvky pohybu hornej matrice.

### Definovanie ovládacích prvkov pre pohyb hornej matrice

Hornému valcu priraďte konštantný pohyb **1** palca za sekundu v zápornom smere osi „Y“, ako je znázornené na obr. 2DHTRL1.43. (Ak je definovaný krok, kliknutím na ikonu náhľadu pohybu objektu si môžete prezrieť pohyb horného valca).

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0043.jpg' | relative_url }})

Ovládanie pohybu hornej matrice

### Poloha hornej matrice podľa plánu

Kliknite na vetvu „Plánované polohovanie“ v prevádzkovom strome, aby ste definovali polohu hornej matrice. Teraz kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať) a ako „Polohovací objekt“ vyberte hornú matricu, ako metódu „Interferencia“ vo vzťahu k „Obrobku“ v smere -Y (pozri obr. 2DHTRL1.44.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0044.jpg' | relative_url }})

Plánované polohovanie hornej matrice pri tvárnení

### Naplánovanie vzťahov medzi objektmi na účely formovania

Vyberte typ kontaktu „užívateľ“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi polotovarom, hornou maticou a spodnou maticou (pozri obr. 2DHTRL1.46.). Keďže matrice sú tuhé a polotovar je plastický, horná a spodná matrica sa považujú za hlavné a polotovar za podriadený. S cieľom predpovedať ohyb počas deformácie sa polotovaru priradí vlastný kontakt.

Zvýraznite vzťah **Horná matrica – polotovar** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) upravte podmienky kontaktu. V časti obrazovky venovanej treniu (pozri obr. 2DHTRL1.45.) sa nachádza roletové menu, ktoré umožňuje používateľovi vybrať vhodné podmienky trenia pre bežné procesy tvárnenia.

Keďže ide o simuláciu tvárnenia za tepla a formy sú z ocele, použite roletové menu a zo zoznamu vyberte možnosť **Tvárnenie za tepla (s mazaním)**. Hodnota trenia **0,3** sa nastaví automaticky.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0045.jpg' | relative_url }})

Okno na definovanie koeficientu trenia medzi objektmi

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna „Inter-Object“. Keďže podmienky trenia sú rovnaké pre všetky páry objektov, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných. Po vykonaní tejto operácie budú mať všetky vzťahy trenie 0,3, ako je znázornené na obr. 2DHTRL1.46. Keďže sa kontakt inicializuje a vygeneruje počas vytvárania databázy, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0046.jpg' | relative_url }})

Definícia vzťahu medzi objektmi pre formovaciu operáciu

### Definovanie riadenia zastavenia pri tvárnení

V okne riadenia zastavenia zaškrtnite políčko „Max. zdvih matrice“ a nastavte **primárny posun matrice** na hodnotu (0,7,25), ako je znázornené na obr. 2DHTRL1.47. Pokročilé možnosti zastavenia sú k dispozícii v režime Expert (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili krokové ovládanie.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0047.jpg' | relative_url }})

Ovládanie zastavenia zdvihu lisovacej matice pri tvárnení

### Definovanie ovládacích prvkov krokov pre formovanie

V okne nastavenia krokov nastavte **počet krokov** na **100** , pri **0,0725** ” na jeden krok pohybu matrice uložte krok pre primárnu matricu (ktorá je v tejto simulácii objektom číslo 2) na hodnotu **10**, ako je znázornené na obr. 2DHTRL1.48.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0048.jpg' | relative_url }})

Krok určuje nastavenia pre operáciu tvárnenia

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}), aby ste pokračovali v definovaní operácie „Heat Dwelling“.

## Operácia 5: Otepľovanie obydlia

Teplotné držanie nie je nič iné ako udržanie tepla po deformácii počas určitého času, pričom tento čas sa nazýva doba teplotného držania alebo jednoducho doba držania.

### Vyberte typ prenosu tepla pre zadržanie tepla

Operáciu nazvite **Heat Dwelling** a vyberte prepínač typu prenosu tepla **Dwell on die**, ako je znázornené na obr. 2DHTRL1.49.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0049.jpg' | relative_url }})

Typ prenosu tepla pre prevádzku v režime „Heat Dwelling“

### Nastavenie podmienok spracovania pre dobu zdržania v ohrievacom priestore

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a potvrďte **doba zdržania****** **4** sekundy pri teplote okolia **68** °F a predvolenom koeficiente konvekcie, ako je znázornené na obr. 2DHTRL1.50.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0050.jpg' | relative_url }})

Nastavenia prevádzkových podmienok pre režim udržiavania tepla

Pre všetky objekty sú nastavené predvolené údaje načítané z databázy (pochádzajúce z predchádzajúcich operácií spolu s teplotnou históriou). Potvrďte predvolené podmienky pre objekty a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali až do okna „Kontakt“ (Kontakt medzi objektmi).

### Naplánovanie vzťahov medzi objektmi z hľadiska zadržiavania tepla

Vyberte typ kontaktu **užívateľ** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Zvýraznite vzťah **Horná matrica – polotovar** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}), aby ste upravili podmienky kontaktu. V sekcii tepelnej analýzy vyberte z roletového menu možnosť „**Free Resting**“, aby ste definovali koeficient prenosu tepla medzi objektmi, ako je znázornené na obr. 2DHTRL1.37.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), čím zatvoríte okno úprav (pozri obr. 2DHTRL1.51.). Tým sa počas vytvárania databázy vygeneruje kontakt medzi objektmi. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno s ovládacími prvkami krokov.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0051.jpg' | relative_url }})

Vzťah medzi objektmi v rámci prevádzky vykurovania obytných priestorov

### Definovanie ovládacích prvkov krokov pre dobu pôsobenia tepla

V okne „Step Controls“ nastavte počet krokov na **10**, pričom každý krok trvá **0,4** s a každý **druhý** krok sa uloží (pozri obr. 2DHTRL1.52.). Týmto je nastavenie viacerých operácií vrátane všetkých operácií prenosu tepla dokončené, takže na simuláciu problému prejdite na kartu „Simulation“ nad stromom objektov.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0052.jpg' | relative_url }})

Ovládacie prvky pre prevádzku v režime vykurovania

## Simulácia problému

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 2DHTRL1.53. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“ (od kroku -1), potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0053.jpg' | relative_url }})

Vyskočné okno „Spustiť simuláciu“

Sledujte priebeh simulácie na kartách „Simulation Graphics“, „Simulation Message“ a „Simulation Log“ a uistite sa, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). (pozri obr. 2DHTRL1.54.)

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0054.jpg' | relative_url }})

Simulačný režim zobrazujúci stav prevádzky ohrevu pece

Po dokončení všetkých viacnásobných operácií sa v súbore protokolu simulácie zobrazí správa „MULTIPLE OPERATION COMPLETED.“. Následne prejdite na kartu „Post“, kde si môžete prezrieť výsledky simulácie.

## Následné spracovanie

V zozname krokov postprocesora pod grafickou oblasťou sú uvedené čísla krokov, ktoré sú k dispozícii z rôznych simulovaných operácií. Na kontrolu odozvy modelu je možné použiť súbor stavových premenných dostupných v ponuke „Post“. Upozorňujeme, že pre prvé dve operácie sú k dispozícii iba tepelné údaje o obrobku, keďže lisovacie formy sa zavádzajú až od tretej operácie. Výsledky deformácie sú viditeľné pri operácii „Deformácia“ (pozri obr. 2DHTRL1.55).

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0055.jpg' | relative_url }})

Postprocesor MO po simulácii všetkých operácií

Niektoré dôležité stavové premenné je možné vybrať priamo z položky „Post“, k ostatným sa dostanete cez dialógové okno „State Variable“ kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}). (pozri obr. 2DHTRL1.56.)

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0056.jpg' | relative_url }})

Graf teplôt všetkých objektov na konci viacerých operácií

Zaznačte stavovú premennú **Teplota** a prehrajte jednotlivé kroky od prvej operácie, aby ste mohli pozorovať prenos tepla v obrobku a formách od fázy ohrevu v peci až po fázu udržovania teploty, ako je znázornené na obr. 2DHTRL1.57.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0057.jpg' | relative_url }})

Prenos tepla v objektoch z vykurovania pecí do prevádzky vykurovania obytných priestorov
