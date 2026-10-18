---
lang: sk
title: "Laboratórium pre experimenty s prenosom tepla v 3D"
---

# Laboratórne cvičenie z prenosu tepla v 3D

V tomto laboratórnom cvičení si ukážeme, ako nastaviť typickú simuláciu viacerých operácií zahŕňajúcu rôzne operácie prenosu tepla a kovania. Počas tohto cvičenia sa tiež pokúsime poukázať na rôzne funkcie systému, ktoré môže používateľ využiť v iných typoch situácií s viacerými operáciami. Tieto operácie môžu pozostávať zo súboru operácií tepelného odpočinku (pozri [Fig. 3DHTRL1.1.]()), súboru deformačných operácií s výmenou foriem medzi jednotlivými operáciami alebo kombinácie operácií prenosu tepla a deformačných operácií (pozri obr. 3DHTRL1.1.). 3D model vysvetlený v tomto laboratórnom cvičení je kompletný model a nasledujúce 3D obrázky slúžia iba na ilustračné účely.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0001.jpg' | relative_url }})

3D znázornenie procesov tepelného odpočinku a tvárnenia

V tomto laboratóriu sme nastavili model so štyrmi operáciami, ktorý zahŕňa jednu operáciu „ohrev v peci“, „prenos tepla“, „odpočinok v teple“, jednu operáciu „deformácia“ a operáciu „udržanie tepla“. Súčiastka je valcovitý obrobok, ktorý najprv prejde operáciou ohrevu v peci po dobu jednej hodiny pri teplote 2000 F, po čom nasleduje operácia prenosu tepla trvajúca 15 sekúnd počas presunu z pece do formovacej stanice. Po tejto operácii nasleduje operácia tepelného odpočinku, pri ktorej obrobok odpočíva na tvárniacich maticiach po dobu 4 sekúnd pred operáciou deformácie. Operácia deformácie prebieha počas špecifického zdvihu (7,25”) hornej matice. Na záver nasleduje fáza udržiavania teploty trvajúca 4 sekundy. Celú sekvenciu je možné nastaviť pomocou tohto systému a všetky operácie je možné simulovať bez zásahu používateľa v dávkovom režime.

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

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2.) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main. 

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. 3DHTRL1.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Zadajte názov úlohy ako „**3D_****Heat_Transfer_Operations**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno „Nový problém“

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt, ako je znázornené na obr. 3DHTRL1.3. V tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**3D_Heat_Transfer_Operations**“. Ako prvú operáciu vyberte **3D Heat transfer operation** a **zaškrtnite** políčko, aby ste operáciu prenosu tepla pridali ako prvú operáciu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0003.jpg' | relative_url }})

Okno na otvorenie nového projektu v nástroji MO Wizard

### Pridávanie ďalších operácií

Sprievodca viacerými operáciami otvorí nový projekt s jednou operáciou 3D prenosu tepla. **Pridajte****ďalšie dve operácie prenosu tepla** pre prenos vzduchom a odpočinok, jednu operáciu tvárnenia a operáciu prenosu tepla pre zotrvanie po tvárnení zo zoznamu operácií v Průzkumníku kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ako je znázornené na obr. 3DHTRL1.4.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0004.jpg' | relative_url }})

Pridávanie operácií

## Operácia 1: Nastavenie vykurovania pece

Pre prvú operáciu prenosu tepla zmeňte názov operácie na „**Ohrev v peci**“ dvojitým kliknutím na názov operácie v okne Editor operácií, ako je znázornené na obr. 3DHTRL1.5, a stlačte klávesu Enter na klávesnici.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0005.jpg' | relative_url }})

Prvú operáciu nazvite „Vyhrievanie v peci“

### Výber typu prenosu tepla pre vykurovanie pece

V položke „Typ prenosu tepla v peci“ pre režim kúrenia v peci vyberte možnosť „Heat“, ako je znázornené na obr. 3DHTRL1.6. Tým sa nastavia predvolené nastavenia prenosu tepla pre režim kúrenia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0006.jpg' | relative_url }})

Výber typu prenosu tepla pre vykurovanie pece

### Nastavenie prevádzkových podmienok pre ohrev v peci

Nastavte dobu ohrevu na **3600** sekúnd (jedna hodina ohrevu) pri teplote pece alebo okolitej teplote **2000F**, ako je znázornené na obr. 3DHTRL1.7, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0007.jpg' | relative_url }})

Nastavenia prevádzkových podmienok pre ohrev v peci

### Výber ovládacích prvkov simulácie pre vykurovanie pece

Nechajte zaškrtnutý iba **režim** **Heat****Transfer**, pretože sa modeluje iba prenos tepla, ako je znázornené na obr. 3DHTRL1.8, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0008.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre vykurovanie pece

### Import materiálu obrobku

V okne „Materiál“ načítajte materiál **AISI-8620** z knižnice materiálov DEFORM v kategórii „Oceľ“ pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To je možné vykonať tak, ako je znázornené na obr. 3DHTRL1.9, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Materiál je možné načítať aj zo zoznamu materiálov v Průzkumníku.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0009.jpg' | relative_url }})

Import materiálu obrobku z knižnice DEFORM

### Skontrolujte vlastnosti materiálu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste skontrolovali tepelné vlastnosti materiálu. Vyberte kartu „Thermal“ (pozri obr. 3DHTRL1.10.) a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Definovať) vedľa položky **Tepelná vodivosť**, aby ste mohli sledovať priebeh tepelnej vodivosti v závislosti od teploty, ako je znázornené na obr. 3DHTRL1.11.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0010.jpg' | relative_url }})

Okno na definovanie vlastností materiálu pre AISI-8620

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0011.jpg' | relative_url }})

Funkcia tepelnej vodivosti na základe údajov o teplote pre materiál AISI-8620

Podobne kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Definovať) vedľa položky **Teplotná kapacita** a prezrite si údaje o funkcii, ako je znázornené na obr. 3DHTRL1.12.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0012.jpg' | relative_url }})

Funkcia tepelnej kapacity na základe údajov o teplote pre materiál AISI-8620

Pre emisivitu a hmotnostnú hustotu sa definuje konštantná hodnota tak, ako je znázornené na obr. 3DHTRL1.10. Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre okno „Vlastnosti materiálu“ a „Objekt“, keďže na prevádzku vyhrevnej pece stačí iba objekt „Obrobok“.

### Definícia obrobku

V okne „Objekt obrobku“ ponechajte typ objektu ako „**Plast**“ (pozri obr. 3DHTRL1.13.). V tejto fáze môže používateľ tiež zadať počiatočnú teplotu obrobku ako **68** °F. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte a načítajte geometriu obrobku.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0013.jpg' | relative_url }})

Definícia objektu obrobku

### Premena geometrie z 2D na 3D pre obrobok

V tomto laboratórnom cvičení sa 3D geometria vytvára rotáciou 2D geometrie, preto zaškrtnite políčko „**Použiť priečny rez**“, aby sa 2D geometria previedla na 3D geometriu, ako je znázornené na obr. 3DHTRL1.14.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0014.jpg' | relative_url }})

Výber konverzie geometrie z 2D na 3D v okne 3D geometrie

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a v okne 2D geometrie kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice), aby ste načítali **Disk_wkp.igs** z inštalačného adresára programu DEFORM 2D\LABS\, ako je znázornené na obr. 3DHTRL1.15. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_no_button.jpg' | relative_url }}), ak systém požiada o uloženie adresára 2D\LABS\ ako umiestnenia knižnice.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0015.jpg' | relative_url }})

Import 2D geometrie z knižnice 2D geometrie DEFORM pre obrobok

Ďalšie možnosti, ktoré sú v tejto fáze k dispozícii, sú definovanie obrobku z primitívnej geometrie a import 3D geometrie pomocou možností „Definovať primitív“ a „Importovať 3D geometriu“.

Po importe 2D geometrie kliknite na ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) a potom na tlačidlo **2D -> 3D konverzia** ![]({{ '/assets/icons/pre_icons/mo_settings..._button.jpg' | relative_url }}). V okne nastavení vyberte typ konverzie Revolve a uistite sa, že uhol otáčania je 360° a os otáčania je Z, ostatné nastavenia ponechajte na predvolených hodnotách (pozri obr. 3DHTRL1.16.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_3d__label.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili okno nastavení konverzie.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0016.jpg' | relative_url }})

Importovať geometriu z knižnice DEFORM

Ak sa pre objekt importuje akákoľvek 3D geometria, použite akciu ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) na kontrolu geometrie; dokonalá geometria musí mať iba jednu plochu a nesmie obsahovať žiadne voľné hrany ani neplatné hrany a orientácie polygónov. Ak geometria nie je dokonalá, kliknite na možnosť geometrie ![]({{ '/assets/icons/pre_icons/mo_fix_label.jpg' | relative_url }}), aby ste tieto problémy odstránili. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno „Mesh“.

### Vytvorenie siete obrobku

Vytvorte sieť s použitím predvoleného počtu **32 000** prvkov (pozri obr. 3DHTRL1.17.). V expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) je k dispozícii aj kompletná škála možností vytvárania sietí, ak potrebujete mať väčšiu kontrolu nad vytvorenou sieťou. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0017.jpg' | relative_url }})

Okno na generovanie siete

### Priradiť materiál obrobku

Ak chcete obrobku priradiť materiál, vyberte v okne materiálov materiál „**AISI****-8620**“. Postupujte podľa obrázku 3DHTRL1.18. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0018.jpg' | relative_url }})

Okno na výber materiálu objektu

### Definovanie okrajových podmienok obrobku

Na stránke BCC skontrolujte, či je predvolene priradená výmena tepla s prostredím BCC k celému vonkajšiemu povrchu polotovaru kliknutím na položku „Defined“ v časti „Heat exchange with Environment“. Predvolené hodnoty BCC sa priraďujú automaticky. (Pozri obr. 3DHTRL1.19.)

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0019.jpg' | relative_url }})

Okno s okrajovými podmienkami

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí okno „Step controls“, keďže nie je potrebné definovať ovládacie prvky pre polohovanie objektu a teplotné zastavenie.

### Nastavenie krokových regulátorov pre vykurovanie pece

Nastavte **počet simulačných krokov** na **100**, pričom dĺžka každého kroku je **36** sekúnd, a ukladajte výsledky každých **10** krokov (pozri obr. 3DHTRL1.20.). Nastavenia pokročilých ovládacích prvkov simulácie sú k dispozícii v expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do fázy vytvárania databázy.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0020.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre vykurovanie pece

### Vytvoriť databázu

Na stránke na vytvorenie databázy môže používateľ skontrolovať údaje potrebné na analýzu a pokračovať vo vytvorení databázy (pozri obr. 3DHTRL1.21.). Pri prvej z viacerých operácií je používateľ povinný vytvoriť databázu. Pre všetky nasledujúce operácie stačí len nastaviť procesné údaje a parametre simulácie. V tejto fáze má používateľ tiež možnosť importovať súbor kľúčových slov, čo je obzvlášť užitočné pre neskoršie operácie. Funkčnosť tejto funkcie „Pridať súbor kľúčových slov definovaných používateľom“ bude rozoberaná v neskorších častiach tohto laboratórneho cvičenia. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k ďalšej operácii „Air Transfer“.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0021.jpg' | relative_url }})

Okno „Vytvorenie databázy“ pre prvú operáciu

## Operácia 2: Letecký transport

V rámci tohto procesu sme nastavili operáciu prenosu tepla (vzduchová fáza procesu), pri ktorej sa diel na 15 sekúnd prenáša z pece do formovacej stanice. Počas tejto doby sa diel, ktorého teplota je približne 2000F, čiastočne ochladí na teplotu okolitého vzduchu.

### Výber typu prenosu tepla pri prenose vzduchom

Pomenujte operáciu ako „**Air Transfer**“ dvojitým kliknutím na položku „Názov operácie“ v editore operácií a stlačením klávesy Enter na klávesnici operáciu zatvorte. Vyberte typ prenosu tepla „**Transfer through air**“, ako je znázornené na obr. 3DHTRL1.22, a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0022.jpg' | relative_url }})

Výber typu prenosu tepla pre prenos vzduchom

### Nastavenie prevádzkových podmienok pre prečerpávanie vzduchu

Definujte prevádzkové podmienky ako dobu prenosu **15** sekúnd v prostredí s teplotou **68** F s použitím predvoleného konvekčného koeficientu, ako je znázornené na obr. 3DHTRL1.23\. 

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0023.jpg' | relative_url }})

Nastavenia prevádzkových podmienok pre vzduchový prenos

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno objektu obrobku, a potvrďte typ objektu ako „Načítať z databázy“ (pozri obr. 3DHTRL1.24.). To znamená, že údaje o obrobku z operácie ohrevu v peci budú k dispozícii ako počiatočné údaje pre túto operáciu. Kliknite na vetvu „Ovládanie krokov“ v strome operácií.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0024.jpg' | relative_url }})

Načítanie výberu objektu z databázy pre obrobok

### Nastavenie definície kroku pre vzduchový prenos

V okne „Step Controls“ nastavte **15****krokov** s **1 sekundovým** **krokom** a ukladaním **každých** **5** krokov (pozri obr. 3DHTRL1.25.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0025.jpg' | relative_url }})

Krok určuje nastavenia prevádzky s prenosom vzduchu

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) otvoríte operáciu „Heat resting“, ktorú databáza vygeneruje pre nasledujúce operácie počas simulácie v dávkovom režime (pozri obr. 3DHTRL1.26.).

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0026.jpg' | relative_url }})

Okno na vytvorenie databázy pre následné operácie v dávkovom režime

**Poznámka:**

V tejto fáze má používateľ možnosť pridať ďalšie údaje o objektoch alebo simuláciách výberom možnosti „Pridať súbor s používateľsky definovanými kľúčovými slovami“ (pozri obr. HTransL1.26.). Upozorňujeme, že ak bude toto kľúčové slovo definované, systém ho načíta pred vytvorením databázy pre druhú operáciu. V tejto fáze sa však nebude vykonávať žiadna kontrola údajov definovaných používateľom z tohto súboru kľúčových slov.

## Operácia 3: Odpočinok pri teple

V rámci tejto operácie sme nastavili operáciu tepelného odpočinku, pri ktorej obrobok pred operáciou deformácie spočíva na tvárniacich maticiach po dobu 4 sekúnd.

### Výber typu prenosu tepla pre tepelné odpočinutie

Pomenujte operáciu ako „**Teplotné odležanie**“ dvojitým kliknutím na názov operácie v editore operácií a stlačením klávesy Enter na klávesnici operáciu zatvorte. Vyberte typ prenosu tepla „**Odležanie na matrici**“, ako je znázornené na obr. 3DHTRL1.27, a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0027.jpg' | relative_url }})

Výber typu prenosu tepla pre prevádzku s tepelným odpočinkom

### Nastavenie podmienok procesu pre tepelné odležanie

Nastavte podmienku procesu na **doba odpočinku****** v trvaní **4** sekúnd v prostredí s teplotou **68F** s použitím predvoleného koeficientu konvekcie, ako je znázornené na obr. 3DHTRL1.28. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0028.jpg' | relative_url }})

Nastavenia prevádzkových podmienok pre operáciu tepelného odležania

### Pridať objekty s kockami

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno „Objekt“, a potvrďte predvolený počet objektov 3.

### Definícia hornej matrice

Kliknite na položku „Top Die“ v strome operácií. Potvrďte teplotu hornej matrice **300** °F a typ objektu **Rigid**, ako je znázornené na obr. 3DHTRL1.29. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0029.jpg' | relative_url }})

Okno definície hornej formy pre operáciu tepelného odpočinku

### Premena 2D geometrie na 3D pre hornú matricu

Podobne ako pri vytváraní geometrie obrobku, prevediete 2D geometriu pre hornú matricu. Zapnite teda začiarkavacie políčko „**Použiť priečny rez**“ (pozri obr. 3DHTRL1.14.) a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do okna 2D geometrie, kde pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) naimportujte súbor „**Disk_top****.igs'** z inštalačnej cesty /2D/LABS/, ako je znázornené na obr. 3DHTRL1.30.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0030.jpg' | relative_url }})

Import geometrie hornej matrice z knižnice geometrií DEFORM

Po importe 2D geometrie kliknite na ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) a vyberte možnosť **2D -> 3D konverzia** ![]({{ '/assets/icons/pre_icons/mo_settings..._button.jpg' | relative_url }}); otočte 2D geometriu o 360° okolo osi Z, ako je znázornené na obr. 3DHTRL1.31. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_3d__label.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), čím zatvoríte okno nastavení konverzie.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0031.jpg' | relative_url }})

Nastavenia pre konverziu geometrie z 2D do 3D pre hornú matricu

### Vytvoriť sieť hornej matrice

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vytvorte sieť s použitím predvoleného počtu **32 000** prvkov, ako je znázornené na obr. 3DHTRL1.32.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0032.jpg' | relative_url }})

Vytvorenie siete pre hornú maticu

### Materiál na výrobu foriem

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a načítajte materiál **AISI-H13** z knižnice materiálov DEFORM, z kategórie **Die_material**, pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice), ako je znázornené na obr. 3DHTRL1.33. Vyberte načítaný materiál a priraďte ho k hornej matrici. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0033.jpg' | relative_url }})

Načítavanie materiálu formy z knižnice DEFORM

### Definícia hornej matrice BCC

V okne „Definovať BCC“ sa všetkým povrchom automaticky priradí BCC „Výmena tepla s okolím“. Kliknite na vetvu „Definované“ pod BCC „Výmena tepla s okolím“, aby ste potvrdili definíciu BCC (pozri obr. 3DHTRL1.34.). Kliknite na vetvu „Spodná forma“ v strome operácií, aby ste definovali spodnú formu.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0034.jpg' | relative_url }})

Výmena tepla s prostredím BCC pre hornú matricu

### Definícia spodnej matrice

Pre spodnú formu tiež zadajte teplotu objektu **300F** a typ objektu **Rigid**, ako je znázornené na obr. 3DHTRL1.29. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

### Premena 2D geometrie na 3D pre spodnú formu

V okne „Geometria spodnej matrice“ zaškrtnite políčko **„Použiť prierez“** (pozri obr. 3DHTRL1.14.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli do okna 2D geometrie, kde pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) naimportujte súbory „**Disk_btm****.igs“** z inštalačnej cesty /2D/LABS/, ako je znázornené na obr. 3DHTRL1.35.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0035.jpg' | relative_url }})

Načítanie geometrie spodnej matrice z knižnice DEFORM

Po importe 2D geometrie kliknite na ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) a vyberte možnosť **2D -> 3D konverzia ![]({{ '/assets/icons/pre_icons/mo_settings..._button.jpg' | relative_url }})**, potom otočte 2D geometriu o 360° okolo osi Z, ako je znázornené na obr. 3DHTRL1.36. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_3d__label.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), čím zatvoríte okno nastavení konverzie.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0036.jpg' | relative_url }})

Nastavenia pre konverziu geometrie z 2D do 3D pre hornú formu

### Vytvorenie siete spodnej formy

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vytvorte sieť s **32 000** prvkami, ako je znázornené na obr. 3DHTRL1.37.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0037.jpg' | relative_url }})

Vytvorenie siete pre spodnú formu

### Priradiť materiál pre spodnú formu

Zoznamu materiálov vyberte materiál **AISI-H13** a priraďte ho k spodnej matrici.

### Definícia spodnej matrice BCC

Potvrďte automaticky priradenú výmenu tepla s prostredím BCC pre všetky povrchy kliknutím na položku „Definované“ v časti „Výmena tepla s prostredím BCC“, ako je znázornené na obr. 3DHTRL1.38. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0038.jpg' | relative_url }})

Výmena tepla s prostredím BCC pre spodnú formu

### Poloha hornej matrice

Teraz v časti „Ovládacie prvky“ prejdite do ponuky „Poloha“, kde najskôr posunieme hornú matricu ďalej od obrobku, aby teplo z tepelného odpočinku zohľadňovalo prenos tepla medzi obrobkom a spodnou matricou.

Na to najprv kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}). Vyberte hornú frézu, metódu ![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }}) a vektor vzdialenosti (x=0, y=0, z=4). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) posuniete hornú frézu ďalej od obrobku. (Pozri obr. 3DHTRL1.39.)

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte okno „Polohovanie objektu“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) nastavíte plánovanú polohu spodnej matrice.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0039.jpg' | relative_url }})

Polohovanie hornej matrice v kľudovom režime

### Poloha spodnej matrice v rozvrhu

Spodnú formu musíme umiestniť vzhľadom na objekt „Workpiece“ z databázy, preto musíme jej polohu naplánovať už pri generovaní databázy. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať) a vyberte „Polohovací objekt“ ako spodnú maticu, metódu „Interferencia“ vo vzťahu k „Obrobku“ v smere +Z (pozri obr. 3DHTRL1.40.). Upozorňujeme, že podrobnosti polohovania pridané v naplánovanom polohovaní sa zohľadnia pred generovaním údajov o interakcii medzi objektmi pre túto operáciu. V tomto bode nebude viditeľný žiadny fyzický pohyb foriem. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0040.jpg' | relative_url }})

Plánované nastavenie polohy spodnej formy vo vzťahu k obrobku

### Naplánovanie vzťahov medzi objektmi pre tepelné odležanie

Vyberte typ kontaktu „užívateľ“, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať vzťah) a vyberte „Spodná forma“ ako hlavný prvok a „Obrobok“ ako podriadený prvok, ako je znázornené na obr. 3DHTRL1.41.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0041.jpg' | relative_url }})

Vzťah medzi obrobkom a spodnou matricou

Kliknite na tlačidlo vzťahu ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) (Upraviť) a v sekcii „Teplo“ vyberte z roletového menu možnosť „**F******r** ee Resting**“, čím definujete koeficient prenosu tepla medzi objektmi, ako je znázornené na obr. 3DHTRL1.42. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno úprav. Tým sa počas simulácie vytvorí kontakt medzi objektmi na začiatku operácie odpočinku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno ovládania krokov.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0042.jpg' | relative_url }})

Výber koeficientu prenosu tepla medzi objektmi v pokojovom stave

### Nastavenie krokov pre tepelné odležanie

V okne „Step Controls“ nastavte **počet krokov** na **10**, **krok prírastku** na 2 a definíciu kroku riešenia pre každý krok na **0,4** s, ako je znázornené na obr. 3DHTRL1.43. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli do okna Generate DB. V okne Database generation kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}), aby ste otvorili operáciu Forming.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0043.jpg' | relative_url }})

Ovládacie prvky pre režim tepelného odpočinku

## Operácia 4: Tvarovanie

Operácia tvárnenia prebieha počas konkrétneho zdvihu (7,25”) hornej matrice. Keďže všetky objekty vyrábame podľa údajov z databázy, údaje o objektoch pochádzajú z predchádzajúcich operácií vrátane tepelnej histórie. Preto všetky objekty z operácie tepelného odpočinku prejdú do operácie tvárnenia, ako je znázornené na obr. 3DHTRL1.44.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0044.jpg' | relative_url }})

Odovzdávanie objektov na čítanie z databázy

### Výber simulačných režimov pre tvárnenie

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby sa otvorilo okno „Typ geometrie“, a potvrďte predvolené režimy simulácie vybrané v časti „Ovládacie prvky simulácie“ (Deformácia a Prenos tepla), ako je znázornené na obr. 3DHTRL1.45. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno objektu.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0045.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre operáciu tvárnenia

Na stránke objektov overte, či je typ údajov všetkých objektov nastavený na „Načítanie z databázy“ a či nie je definovaný žiadny pohyb. V strome objektov kliknite na **vetvu „Horná forma – pohyb“**, aby ste definovali ovládacie prvky pohybu hornej formy.

### Definovanie ovládacích prvkov pre pohyb hornej matrice

Pre hornú matricu nastavte konštantný pohyb matrice o hodnotu **1** palca za sekundu v zápornom smere osi „Z“, ako je znázornené na obr. 3DHTRL1.46. (Ak je definovaný krok, kliknutím na ikonu náhľadu pohybu objektu si môžete prezrieť pohyb hornej matrice.)

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0046.jpg' | relative_url }})

Ovládanie pohybu hornej matrice

### Poloha hornej matrice podľa plánu

Kliknite na vetvu „Plánované polohovanie“ v strome objektov, aby ste definovali polohovanie hornej matrice. Teraz kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať) a vyberte „Polohovací objekt“ ako **T******o** p die,** metódu „**Interference**“ vo vzťahu k „**Workpiece**“ v smere -Z (pozri obr. 3DHTRL1.47.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0047.jpg' | relative_url }})

Plánované polohovanie hornej matrice pri tvárnení

### Naplánovanie vzťahov medzi objektmi na účely formovania

Vyberte typ kontaktu „užívateľ“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi polotovarom, hornou matricou a spodnou matricou (pozri obr. 3DHTRL1.49.). Keďže matrice sú tuhé a polotovar je plastický, horná a spodná matrica sa považujú za hlavné a polotovar za podriadený. S cieľom predpovedať ohyb počas deformácie sa polotovaru priradí vlastný kontakt.

Zvýraznite vzťah medzi hornou matricou a polotovarom a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) upravte podmienky kontaktu. V časti obrazovky venovanej treniu (pozri obr. 3DHTRL1.48.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné procesy tvárnenia.

Keďže ide o simuláciu tvárnenia za tepla a formy sú z ocele, použite roletové menu a zo zoznamu vyberte možnosť **Tvárnenie za tepla (s mazáním)**. Hodnota trenia 0,3 sa nastaví automaticky.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0048.jpg' | relative_url }})

Okno na definovanie koeficientu trenia medzi objektmi

Tepelné údaje je potrebné upraviť tak, aby sa namiesto koeficientu prenosu tepla „Voľný pokojový stav“, ktorý sa používal v predchádzajúcej operácii, použil koeficient „Tvarovanie“. Kliknite na kartu **Tepelné** a v roletovom menu vyberte položku **Tvarovanie**, ako je znázornené na obr. 3DHTRL1.49.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0049.jpg' | relative_url }})

Okno na definovanie koeficientu trenia medzi objektmi

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna „Inter-Object“. Keďže podmienky trenia sú rovnaké pre všetky páry objektov, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu na všetky ostatné. Po vykonaní tejto operácie budú mať všetky vzťahy trenie 0,3, ako je znázornené na obr. 3DHTRL1.50. Keďže kontakt sa inicializuje a vygeneruje počas vytvárania databázy, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0050.jpg' | relative_url }})

Definícia vzťahu medzi objektmi pre formovaciu operáciu

### Definovanie riadenia zastavenia pri tvárnení

V okne riadenia zastavenia zaškrtnite políčko „Max. zdvih matrice“ a nastavte primárny posun matrice na (0,0,7,25), ako je znázornené na obr. 3DHTRL1.51. Pokročilé možnosti zastavenia sú k dispozícii v režime Expert (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili krokové ovládanie.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0051.jpg' | relative_url }})

Ovládanie zastavenia zdvihu matice pri formovaní

### Definovanie ovládacích prvkov krokov pre formovanie

V okne nastavenia krokov nastavte **počet krokov** na **100** pri **0,0725** ” na jeden krok pohybu formy, **krok** **prírastok****na****uloženie** na hodnotu **10** pre primárnu maticu (ktorá je v tejto simulácii objektom číslo 2), ako je znázornené na obr. 3DHTRL1.52.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0052.jpg' | relative_url }})

Krok určuje nastavenia pre operáciu tvárnenia

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}), čím otvoríte operáciu „Heat Dwelling“.

## Operácia 5: Otepľovanie obydlia

Teplotné držanie nie je nič iné ako udržanie tepla po deformačnom procese počas určitého času, pričom tento čas sa nazýva doba teplotného držania alebo jednoducho doba držania.

### Vyberte typ prenosu tepla pre zadržanie tepla

Pomenujte operáciu ako „heat Dwelling“ a vyberte prepínač typu prenosu tepla „Dwell on die“, ako je znázornené na obr. 3DHTRL1.53.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0053.jpg' | relative_url }})

Typ prenosu tepla pre prevádzku v režime „Heat Dwelling“

### Nastavenie podmienok spracovania pre dobu zdržania v ohrievacom priestore

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a potvrďte **doba zdržania****** **4** sekundy pri teplote okolia **68F** a predvolenom koeficiente konvekcie, ako je znázornené na obr. 3DHTRL1.54.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0054.jpg' | relative_url }})

Nastavenia prevádzkových podmienok pre režim udržiavania tepla

Pre všetky objekty sú nastavené predvolené údaje načítané z databázy (pochádzajúce z predchádzajúcich operácií spolu s teplotnou históriou). Potvrďte predvolené podmienky pre objekty a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte až do okna „Kontakt“ (Kontakt medzi objektmi).

### Naplánovanie vzájomných kontaktných vzťahov medzi objektmi pre akumuláciu tepla

Vyberte kontakt typu **user****type** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Zvýraznite vzťah „Top Die – Billet“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}), aby ste upravili podmienky kontaktu. V sekcii tepelnej analýzy vyberte z roletového menu možnosť „**Voľný pokoj**“, čím definujete koeficient prenosu tepla medzi objektmi, ako je znázornené na obr. 3DHTRL1.42.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), čím zatvoríte okno úprav (pozri obr. 3DHTRL1.55.). Tým sa počas vytvárania databázy vygeneruje kontakt medzi objektmi. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno s ovládacími prvkami krokov.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0055.jpg' | relative_url }})

Vzťah medzi objektmi v rámci prevádzky vykurovania obytných priestorov

### Definovanie ovládacích prvkov krokov pre dobu pôsobenia tepla

V okne „Step Controls“ nastavte **počet krokov** na **10**, **krok****prírastok** na **2** a definíciu kroku riešenia pre každý krok na **0,4** s. (Pozri obr. 3DHTRL1.56.) Týmto je nastavenie viacerých operácií vrátane všetkých operácií prenosu tepla dokončené. Prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a simulujte úlohu.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0056.jpg' | relative_url }})

Ovládacie prvky pre prevádzku v režime vykurovania

## Simulácia problému

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 3DHTRL1.57. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0057.jpg' | relative_url }})

Vyskočiace okno „Spustiť simuláciu“

Sledujte priebeh simulácie na kartách „Simulation Graphics“, „Simulation Message“ a „Simulation Log“ a uistite sa, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). (Pozri obr. 3DHTRL1.58.)

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0058.jpg' | relative_url }})

Simulačný režim zobrazujúci prevádzkový stav ohrevu pece

Po dokončení všetkých viacnásobných operácií sa v súbore protokolu simulácie zobrazí správa „MULTIPLE OPERATION COMPLETED.“; následne prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), kde si môžete prezrieť výsledky simulácie.

## Následné spracovanie

V postprocesore zoznam krokov pod grafickou oblasťou uvádza čísla krokov dostupných z rôznych simulovaných operácií. Na kontrolu odozvy modelu je možné použiť súbor stavových premenných dostupných v ponuke „Post“. Upozorňujeme, že pri prvých dvoch operáciách sú k dispozícii iba tepelné údaje obrobku, keďže lisovacie formy sa zavádzajú až od tretej operácie. Výsledky deformácie je možné zobraziť v operácii „Deformácia“ (pozri obr. 3DHTRL1.59).

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0059.jpg' | relative_url }})

Postprocesor MO po simulácii všetkých operácií

Niektoré dôležité stavové premenné je možné vybrať priamo z okna „Post Tools“, k ostatným sa dostanete cez dialógové okno „State Variable“ kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}). (Pozri obr. 3DHTRL1.60.)

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0060.jpg' | relative_url }})

Graf teplôt všetkých objektov na konci viacerých operácií

Zobrazte stavovú premennú „Teplota“ a prehrávajte jednotlivé kroky od prvej operácie, aby ste mohli pozorovať prenos tepla v obrobku a formách od fázy ohrevu v peci až po fázu udržovania teploty, ako je znázornené na obr. 3DHTRL1.61.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/3d_heat_transfer_operation_lab/image0061.jpg' | relative_url }})

Prenos tepla v objektoch z vykurovania pecí do prevádzky vykurovania obytných priestorov
