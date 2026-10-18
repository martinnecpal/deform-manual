---
lang: sk
title: "Laboratórium Lab07 pre nosič prevodoviek"
---

# Laboratórna práca č. 07 – Laboratórna práca s nosičom ozubených kolies

## Úvod

Toto je druhé laboratórne cvičenie založené na skutočnom priemyselnom diele z porovnávacieho testu Nemeckého združenia kováčskeho priemyslu z roku 1999. Tento diel poslúži na ilustráciu reálnej úlohy. V závislosti od hardvéru a nastavení systému bude riešenie tejto úlohy trvať od niekoľkých hodín až po jeden deň.

V predchádzajúcom laboratórnom cvičení [Lab04: Steering Link]({{ '/docs/sk/labs/basic_labs/3d_labs/lab04_steering_link/' | relative_url }}) sme podrobne vysvetlili nastavenia siete, ktoré slúžia na optimalizáciu času spracovania a riešenie úlohy.

## Postup: Kovanie na mechanickom lise

Geometria nástrojov a polotovaru uvedená pre prierez 1/12 (300)

**Billet:**

Rozmery: priemer 31,5 mm × výška 67 mm

Materiál: DIN C35

Predohrev: 1230 °C

**Nástroj:** Teplota: 80 °C 

**Čas prenosu z pece:** 7 sekúnd

**Doba zotrvania na čipe:** 0,7 sekundy

**Prvá operácia:** Ploché valcovanie na 9,5 mm 

**Prechod na druhý nástroj:** 3 sekundy

**Druhý krok:** Tvarovanie v kováčskej dielni

## Plánovanie simulácie

Ide o dvojfázový proces kovania s pomerne dlhým časom odpočinku medzi pecou a lisom. Prvá fáza je jednoduchá a pravdepodobne nespôsobí žiadne ťažkosti. Druhá fáza je zložitejšia a jej výsledky sa oveľa ťažšie predpovedajú, čo zvyšuje užitočnosť simulácie. Existujú tri možné prístupy k simulácii tohto procesu:

  1. Simulujte celý proces v 3D, vrátane prenosu tepla, lisovania a dokončovacieho spracovania. Simulácia sa ľahko spúšťa a presne zachytáva rozloženie teploty a deformácie v obrobku.

  2. Simulujte zúženie v 2D, preneste údaje do 3D a simulujte vytláčanie v 3D. 2D operáciu je jednoduchšie nastaviť a prebieha veľmi rýchlo. Prevod do 3D si vyžaduje použitie nástroja na konverziu z 2D do 3D, ktorý je k dispozícii v programe DEFORM®. Rovnako ako celá 3D simulácia, aj tento prístup presne zachytáva rozloženie teploty a deformácie v obrobku.

  3. Vytvorte geometriu zúženej časti v CAD modeli a simulujte len druhú operáciu. Táto metóda je rýchla a vyžaduje menej úsilia ako spustenie úplnej simulácie, avšak rozloženie teploty a deformácie nebude správne a tieto odchýlky ovplyvnia výpočty zaťaženia a v niektorých prípadoch môžu ovplyvniť aj správanie sa materiálu pri tečení.

V rámci tejto úlohy spustíme celú simuláciu v 3D (pozri obr. 3DL7.1.). Všetky operácie nastavíme v dávkovom režime.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image001.jpg' | relative_url }})

3D CAD model výstupu z procesu zhutňovania a dokončovacieho kovania

## Nastavenie simulácie

### Vytvorenie nového problému a pridanie prvej operácie prenosu tepla

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main, ako je znázornené na obr. 3DL7.2.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image002.jpg' | relative_url }})

Hlavné okno grafického používateľského rozhrania

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image003.jpg' | relative_url }})

Vyskočilo nové hlásenie o probléme

Vytvorte nový problém buď výberom položky **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 3DL7.3. Vyberte prepínač „Integrovaný výrobný proces“ a v poli Jednotky vyberte systém jednotiek pomocou prepínača „**SI**“. Názov úlohy zadajte ako „**Gear_Carrier**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „Zobraziť dialógové okno s možnosťami“, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.  
  
Otvorí sa šablóna MO (Multiple operation) a v tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**Gear_Carrier**“. Ako prvú operáciu vyberte operáciu 3D prenosu tepla a zaškrtnite políčko „Prvá operácia“, čím pridáte operáciu prenosu tepla ako prvú operáciu. Vyberte prepínač **SI** jednotiek a kliknutím otvoríte operáciu.

### Operácia 1: Letecká preprava

V rámci tohto procesu sme nastavili operáciu prenosu tepla (vzduchová fáza procesu), pri ktorej sa diel počas 7 sekúnd prenáša z pece do formovacej stanice. Počas tejto doby sa diel, ktorého teplota je približne 2000 °F, čiastočne ochladzuje na teplotu okolitého vzduchu.

#### Definovať názov operácie

Pomenujte operáciu ako „**Air Transfer**“ dvojitým kliknutím na položku „Názov operácie“ v editore operácií a stlačením klávesy Enter na klávesnici potvrďte zmenu, ako je znázornené na obr. 3DL7.4. 

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image004.jpg' | relative_url }})

Zmena názvu operácie v editore operácií.

#### Určenie typu prenosu tepla

Ako typ prenosu tepla vyberte „**Prenos****vzduchom**“, ako je znázornené na obr. 3DL7.5, a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image005.jpg' | relative_url }})

Výber typu prenosu tepla pre prevádzku s prenosom vzduchom.

#### Stanovenie podmienok procesu 

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a nastavte „**Čas prenosu**“ na hodnotu **7** sekúnd a „**Teplotu prostredia**“ na hodnotu **20** °C a ponechajte predvolený **koeficient konvekcie** **0,02** N/s/mm/°C, ako je znázornené na obr. 3DL7.6.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image006.jpg' | relative_url }})

Nastavenia prevádzkových podmienok pre prevádzku s prívodom vzduchu.

#### Definovanie ovládacích prvkov simulácie 

Nechajte zaškrtnutý iba režim „Heat Transfer“ (Prenos tepla), ako je znázornené na obr. 3DL7.7, keďže sa modeluje iba prenos tepla. Pre pokročilé funkcie môže používateľ využiť expertný režim (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})); pre pokračovanie kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image007.jpg' | relative_url }})

Stránka riadenia simulácie pre prevádzku vzduchového prenosu.

#### Import materiálu pre obrobok

V okne „Material“ načítajte materiál „**DIN-C15[20-2200F(20-1200C)]**“ z knižnice materiálov DEFORM pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). Postupujte podľa obrázku 3DL7.8. Materiál je možné načítať aj zo zoznamu materiálov v Průzkumníku. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na stránku Objekty.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image008.jpg' | relative_url }})

Import materiálu pre obrobok z knižnice DEFORM.

#### Definovanie obrobku

##### Nastavenie objektu obrobku

V okne „Objekt obrobku“ ponechajte typ objektu ako „**Plast**“ a nastavte teplotu obrobku na **1230** °C (pozri obr. 3DL7.9.). Ďalšou možnosťou, ktorá je v tejto fáze k dispozícii, je „Importovať objekt“ z iného súboru kľúčových slov alebo databázy. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali a importovali geometriu obrobku.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image009.jpg' | relative_url }})

Definícia objektu obrobku.

##### Import geometrie obrobku

Na stránke „Geometria“ pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) načítajte súbor „**IDS_GC_Billet****.stl**“ z inštalačnej zložky **/3D/LABS/**, ako je znázornené na obr. 3DL7.10. V tejto fáze je k dispozícii aj možnosť vytvorenia základnej geometrie na vytvorenie geometrie.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0010.jpg' | relative_url }})

Import geometrie pre obrobok.

Po importe akejkoľvek geometrie kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste geometriu skontrolovali. Zobrazí sa okno na kontrolu geometrie, ktoré obsahuje prehľad geometrie objektu (pozri obr. 3DL7.11.).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0011.jpg' | relative_url }})

Výstup kontroly geometrie obrobku.

  
Roviny symetrie je možné definovať pomocou položky „Symmetry Planes“ na stránke geometrie. Kliknite na ****![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }})**** a vyberte **symetrické****plochy** polotovaru, ako je znázornené na obr. 3DL7.12. Definícia symetrických plôch sa prenesie do BCC, ak to bude počas generovania siete povolené. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku Sieť.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0012.jpg' | relative_url }})

Definícia rovín symetrie pre obrobok.

##### Vytvorenie siete obrobku

Sieť vygenerujeme tak, že pomocou ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) prejdeme do expertného režimu, vyberieme **absolútnu****sieť**, nastavíme **Veľkosť******3** a nastavíme **minimálnu veľkosť prvku** na **0,33** mm (pozri obr. 3DL7.13.). Nastavíme **váhové koeficienty** pre **krivost povrchu** na **0,9**, pre **teplotu** na **0,0**, **distribúciu deformačného napätia** na **0,1** a **distribúciu rýchlosti deformácie** na **0,1** (pozri obr. 3DL7.14.). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) na vytvorenie siete. Počas generovania siete sa zobrazí okno s predvolenými okrajovými podmienkami, ako je znázornené na obr. 3DL7.15. Pokiaľ ide o prenesenie podmienok symetrie z geometrie do BCC, kliknite na „**Áno**“, aby sa podmienky symetrie preniesli z geometrie do siete. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}), aby ste sa vrátili do režimu s návodom. Po dokončení generovania siete (pozri obr. 3DL7.16.) kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0013.jpg' | relative_url }})

Nastavenia siete obrobku.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0014.jpg' | relative_url }})

Nastavenie váhových koeficientov siete pre obrobok.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0015.jpg' | relative_url }})

Pri generovaní siete sa zobrazí okno s predvolenými okrajovými podmienkami.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0016.jpg' | relative_url }})

Vytvorená sieť pre obrobok.

##### Priradenie materiálu obrobku

Na priradenie materiálu k obrobku vyberte v okne materiálov materiál „**DIN****-C15[70-2200F(20-1200C)]**“; postupujte podľa obr. 3DL7.17. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0017.jpg' | relative_url }})

Priradenie materiálu k obrobku.

##### Definovanie okrajových podmienok obrobku

Na stránke BCC skontrolujte definované roviny symetrie a predvolené nastavenie výmeny tepla s prostredím BCC pre celý vonkajší povrch sochory s výnimkou rovín, ako je znázornené na obr. 3DL7.18. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku Step.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0018.jpg' | relative_url }})

BCC pre obrobok

##### Definovanie ovládacích prvkov krokov

Nastavte **počet simulačných krokov** na **14** s dĺžkou každého kroku **0,5** sekundy a ukladajte výsledky každých **2** kroky (pozri obr. 3DL7.19.). Nastavenia pokročilých ovládacích prvkov simulácie sú k dispozícii v expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do fázy generovania databázy.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0019.jpg' | relative_url }})

Stránka riadenia krokov pre prevádzku vzduchového prenosu.

##### Vytvorenie databázy

V etape vytvárania databázy môže používateľ skontrolovať údaje potrebné na analýzu a pokračovať vo vytváraní databázy (pozri obr. 3DL7.20.). Pred vykonaním akejkoľvek z viacerých operácií je používateľ povinný vytvoriť databázu. Pre všetky nasledujúce operácie stačí len nastaviť procesné údaje a parametre simulácie.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0020.jpg' | relative_url }})

Vytvorenie databázy pre prvú operáciu – letecký prevoz.

### Operácia 2: Odpočinok na kockách

#### Pridanie druhej operácie prenosu tepla

Po vytvorení databázy prvej operácie pridajte ďalšiu 3D operáciu prenosu tepla kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ako je znázornené na obr. 3DL7.21. Operáciu pomenujte „**Rest on Die**“ dvojitým kliknutím na názov operácie v editore operácií a stlačením klávesy Enter na klávesnici operáciu zatvorte.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0021.jpg' | relative_url }})

Pridanie ďalšej operácie 3D prenosu tepla na nastavenie operácie „Rest on Die“.

#### Určenie typu prenosu tepla

Ako typ prenosu tepla vyberte „**Rest on die**“, ako je znázornené na obr. 3DL7.22, a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte v nastavovaní prevádzky.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0022.jpg' | relative_url }})

Výber typu prenosu tepla pre prevádzku typu „Rest on die“.

#### Stanovenie podmienok procesu 

Nastavte „**Doba odpočinku******“ na hodnotu **0,7** s a „**Teplota okolia******“ na **20** °C a ponechajte predvolený ****konvekčný koeficient**** na hodnote **0,02** N/s/mm/°C, ako je znázornené na obr. 3DL7.23. V tejto operácii klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Objekt.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0024.jpg' | relative_url }})

Nastavenia procesných podmienok pre operáciu „Rest on Die“.

#### Definovanie ovládacích prvkov simulácie 

Nechajte zaškrtnutý iba režim „Heat Transfer“, pretože sa modeluje iba prenos tepla, ako je znázornené na obr. 3DL7.24, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0023.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre operáciu „Odpočinok na matrici“.

#### Pridať objekty s kockami

Aby sme mohli pokračovať v operácii s maticou, potrebujeme objekt „**Bottom********Die**“, preto odstráňte objekt hornej matice podľa obrázku 3DL7.25. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s objektom obrobku.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0025.jpg' | relative_url }})

Objekty určené na operáciu „Odpočinok na kocke“.

#### Definovanie typu objektu „obrobok“

Na stránke objektu obrobku ponecháme predvolený výber typu objektu ako „**Načítať****z databázy**“ (pozri obr. 3DL7.26.), čo znamená, že údaje o obrobku z operácie „Prenos vzduchom“ budú k dispozícii ako východiskové údaje pre túto operáciu. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka objektu „Spodná forma“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0026.jpg' | relative_url }})

Stránka objektu obrobku.

#### Definícia spodnej formy

##### Nastavenie objektu spodnej matrice

V okne „Bottom die object“ ponechajte typ objektu ako „**Rigid**“ a zadajte teplotu **80** °C (pozri obr. 3DL7.27.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali a importovali geometriu spodnej formy.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0027.jpg' | relative_url }})

Stránka objektu „Spodná matrica“.

##### Import geometrie spodnej matrice

Na stránke Geometria pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) naimportujte súbor „**IDS_GC_Upset_Bot****.****stl**“ z inštalačnej cesty **/3D/LABS/**, ako je znázornené na obr. 3DL7.28. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Mesh“ (Sieť).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0028.jpg' | relative_url }})

Import geometrie spodnej matrice.

##### Vytvorenie mriežky spodnej formy

Vytvoríme sieť pre spodnú matricu s použitím **32 000** prvkov, ako je znázornené na obr. 3DL7.29. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Materiál“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0029.jpg' | relative_url }})

Vytvorenie siete pre spodnú formu.

##### Import materiálu pre lisovacie formy

Načítame materiál **AISI-H13** z knižnice materiálov DEFORM ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) v kategórii **Die_material** pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice), ako je znázornené na obr. 3DL7.30. Vyberte načítaný materiál a priraďte ho k spodnej matrici.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0030.jpg' | relative_url }})

Načítavanie materiálu formy zo knižnice DEFORM pre spodnú formu.

##### Definícia spodnej matrice BCC

Potvrďte automaticky priradenú položku „Výmena tepla s prostredím BCC“ pre všetky plochy kliknutím na „**Definované**“ v položke „Výmena tepla s prostredím BCC“, ako je znázornené na obr. 3DL7.31. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Polohovanie“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0031.jpg' | relative_url }})

Výmena tepla s okolitým prostredím BCC pre spodnú formu.

#### Nastavenie polohy spodnej formy

Definujte polohu spodnej formy kliknutím na popisok „**Plán********Polohovanie**“ a následne pridajte akciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať), vyberte „**Polohovanie****objekt**“ ako **spodná forma**, metódu ako „**interferencia**“ vo vzťahu k „**obrobku**“ v smere **Z** (pozri obr. 3DL7.32.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0032.jpg' | relative_url }})

Plánované nastavenie polohy spodnej formy v režime „Rest on Die“.

#### Plánovanie vytvárania kontaktov

Na stránke „Kontakt“ vyberte kontakt typu **User****type** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Zvýraznite vzťah **Spodná forma** – **Obrobok** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}), aby ste upravili podmienky kontaktu (pozri obr. 3DL7.33.). Na karte „Thermal“ vyberte z roletového menu položku „**Free Resting**“, čím definujete koeficient prenosu tepla medzi objektmi na hodnotu **1** N/s/mm/°C, ako je znázornené na obr. 3DL7.34. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno úprav.  
  
Uistite sa, že v časti „Naplánovať kontakt“ sú zaškrtnuté políčka „Inicializovať“ a „Generovať“ (pozri obr. 3DL7.33.), aby systém vygeneroval kontakt medzi objektmi počas vytvárania databázy v rámci druhej operácie. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno s ovládacími prvkami krokov.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0033.jpg' | relative_url }})

Vzťah kontaktu medzi objektmi pre operáciu „Opieranie o formu“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0034.jpg' | relative_url }})

Kontakt medzi objektmi (HTC) pri operácii „Rest on Die“.

#### Nastavenie ovládacích prvkov krokov

Nastavte počet simulačných krokov na 7, každý s dĺžkou 0,1 s, a uložte každý krok (pozri obr. 3DL7.35.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do fázy generovania databázy. Skontrolujte, či na stránke Generovanie databázy nie sú žiadne chyby. Databázu nebudeme generovať, pretože nastavujeme druhú operáciu v dávkovom režime a databáza sa vygeneruje počas behu programu po dokončení simulácie predchádzajúcej operácie.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0035.jpg' | relative_url }})

Definícia krokového riadenia pre operáciu „Odpočinok na matrici“.

### Nastavenie 3. operácie: Operácia s deformáciou

#### Pridanie prvej tvarovacej operácie

Po nastavení druhej operácie pridáme prvú tvarovaciu operáciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ako je znázornené na obr. 3DL7.36. Operáciu pomenujte „**Upsetting**“ dvojitým kliknutím na položku „Názov operácie“ v editore operácií a stlačením klávesy Enter na klávesnici operáciu zatvorte.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0036.jpg' | relative_url }})

Pridanie operácie tvarovania na nastavenie operácie lisovania.

#### Vyberte ovládacie prvky simulácie pre lisovanie

Pre túto operáciu musíme zaškrtnúť oba režimy – Deformácia aj Prenos tepla –, keďže budeme simulovať ako deformáciu, tak aj prenos tepla (pozri obr. 3DL7.37). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Objekt.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0037.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre proces lisovania.

#### Predmety určené na deformáciu stlačením

Na stránke objektov môžeme vidieť, že sa tu nachádzajú tri objekty. Obrobok a spodná matrica sú načítané z databázy a nový tuhý objekt – horná matrica – sa automaticky pridá ako objekt č. 2 (pozri obr. 3DL7.38.). Obrobok a spodná forma sú objektov typu „Načítané z databázy“, čo znamená, že údaje o objektoch sa načítajú z posledného kroku simulácie predchádzajúcej operácie.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0038.jpg' | relative_url }})

Predmety určené na operáciu lisovania.

#### Definovanie kompenzácie objemu pre objekt „Obrobok“

Keďže obrobok je objektu typu „Read from DB“, definujeme preň iba údaje súvisiace s kompenzáciou objemu. Kliknite na Vlastnosti obrobku v stromovej štruktúre objektov, otvorí sa stránka Vlastnosti. Zaškrtnite políčko „**Predefinovať**: **Cieľový****objem**“ a vyberte Cieľový objem ako **Aktívny v FEM + vytváranie siete**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}) na výpočet objemu obrobku; zobrazí sa vyskakovacie okno s informáciami o objeme siete a geometrie. Ako cieľový objem použijeme objem geometrie, preto v kontextovom menu kliknite na **Áno** v okne, ako je znázornené na obr. 3DL7.39, a nastavte ho ako objem, ktorý sa má kompenzovať počas opätovného vytvárania siete. V stromovej štruktúre objektov vyberte objekt *Horná matrica*.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0039.jpg' | relative_url }})

Nastavenie kompenzácie objemu pre obrobok.

#### Definovanie hornej matrice

##### Nastavenie objektu „Top Die“

Keď v stromovej štruktúre objektov vyberieme objekt „Top Die“, otvorí sa stránka objektu „Top Die“. Na stránke objektu Top Die ponechajte typ objektu ako „**Rigid**“ a zadajte teplotu **80** °C a zaškrtnite políčko „**Primary****die**“, ako je znázornené na obr. 3DL7.40. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte a importujte geometriu hornej matrice.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0040.jpg' | relative_url }})

Operácia „Upsetting“ – Definícia objektu hornej matrice

##### Import geometrie hornej matrice

Na stránke Geometria pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) načítajte súbor „**IDS_GC_Upset_Top****.****stl**“ z inštalačnej zložky /3D/LABS/, ako je znázornené na obr. 3DL7.41. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) na kontrolu geometrie. Zobrazí sa okno kontroly geometrie, ktoré obsahuje prehľad geometrie objektu. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na stránku „Mesh“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0041.jpg' | relative_url }})

Import geometrie pre hornú matricu pri operácii zhutňovania.

##### Vytvorenie siete pre hornú matricu

Vytvoríme sieť s predvoleným počtom 32 000 prvkov, ako je znázornené na obr. 3DL7.42. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Material“ (Materiál).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0042.jpg' | relative_url }})

Vytvorenie siete pre hornú matricu pri operácii zhutňovania.

##### Priradenie materiálu pre hornú matricu

Zoznamu materiálov, ktorý bol načítaný už v predchádzajúcej operácii (pozri 7.4.3.7.4.), vyberte materiál AISI-H13 a priraďte ho k hornej matrici. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku BCC.

##### Definícia hornej matrice BCC

Na stránke „Definovať BCC“ môžeme vidieť, že BCC „Výmena tepla s okolím“ je automaticky priradená ku všetkým povrchom. Kliknutím na vetvu **Definované** pod BCC „Výmena tepla s okolím“ potvrdíme definíciu BCC (pozri obr. 3DL7.43.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Pohyb“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0043.jpg' | relative_url }})

Výmena tepla s prostredím BCC pre hornú matricu.

##### Definovanie pohybu hornej matrice

Vyberte typ pohybu ako **Mechanický****lis**, nastavte **Celkový****zdvih** na **270** mm, **závit** **kovania** na **92,5** mm a **Cyklus/s** na **1,4** (pozri obr. 3DL7.44.). Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Polohovanie.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0044.jpg' | relative_url }})

Definícia pohybu hornej matrice pri operácii lisovania.

#### Definovanie plánovaného umiestnenia

Musíme umiestniť hornú matricu nad obrobok; na tento účel použijeme plánované polohovanie, keďže aktuálna operácia prebieha v dávkovom režime. Kliknite na odkaz **Plánované polohovanie** a pridajte akciu na naplánovanie polohy hornej matrice vo vzťahu k obrobku metódou kolízie v smere -Z, ako je znázornené na obr. 3DL7.45. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Kontakt“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0045.jpg' | relative_url }})

Nastavenie polohy hornej matrice pre operáciu lisovania.

#### Plánovanie generovania kontaktov

Na stránke „Kontakt“ vyberte kontakt typu **Typ používateľa** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi obrobkom, hornou maticou a spodnou maticou, ako je znázornené na obr. 3DL7.46. Keďže matrice sú tuhé a obrobok je plastický, horná a spodná matrica sa považujú za hlavné objekty a obrobok za podriadený objekt. Uistite sa, že sú zaškrtnuté políčka Inicializovať a Generovať v časti Naplánovať kontakt (pozri obr. 3DL7.46), aby systém vygeneroval kontakt medzi objektmi počas generovania databázy druhej operácie. 

Zvýraznite vzťah **Horná matrica** – **obrobok** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}), aby ste upravili podmienky kontaktu. Na karte „Trenie“ sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné procesy tvárnenia. Keďže ide o simuláciu tvárnenia za tepla a matrice sú oceľové, použite roletové menu a zo zoznamu vyberte možnosť **Tvárnenie za tepla (mazané)** (pozri obr. 3DL7.47.). Automaticky sa vyberie hodnota trenia 0,3. 

Tepelné údaje je potrebné upraviť tak, aby sa použil koeficient prenosu tepla pre „tvarovanie“. Kliknite na kartu **Thermal** a v roletovom menu vyberte položku **Forming**, ako je znázornené na obr. 3DL7.48.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0046.jpg' | relative_url }})

Definícia vzťahu medzi objektmi pre operáciu lisovania.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0047.jpg' | relative_url }})

Okno s definíciou koeficientu trenia medzi objektmi.

  
![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0048.jpg' | relative_url }})

Okno s definíciou medziobjektovej HTC.

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite na stránku „Kontakt“, keďže podmienky trenia sú rovnaké pre všetky páry objektov, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných. Po vykonaní tejto operácie budú mať všetky vzťahy trenie 0,3, ako je znázornené na obr. 3DL7.49. Keďže sa kontakt inicializuje a vygeneruje počas vytvárania databázy, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Stopping controls“ (Ovládacie prvky zastavenia).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0049.jpg' | relative_url }})

Definícia vzťahu medzi objektmi pre operáciu lisovania.

#### Definovanie zastavovacích prvkov pre tvárenie

Na stránke „Ovládacie prvky zastavenia“ zaškrtnite políčko „Ovládací prvok zastavenia pri maximálnom zdvihu matrice“ a nastavte primárny posun matrice na (**0,0,270**), ako je znázornené na obr. 3DL7.50. Pokročilé možnosti zastavenia sú k dispozícii v režime Expert (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) nastavte ovládacie prvky krokovania.

  
![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0050.jpg' | relative_url }})

Ovládanie zastavenia zdvihu matrice pri operácii zhutňovania.

#### Definovanie ovládacích prvkov krokov pre zúženie

Na stránke „Step“ nastavte počet krokov na 120 pri posuve formy 0,5 mm/krok a krok prírastku na 10 pre primárnu formu. Uistite sa, že je ako primárna forma vybraná horná forma, ako je znázornené na obr. 3DL7.51. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „DB Generation“ (Vytvorenie databázy). Databázu nebudeme vytvárať, pretože sa vytvorí počas behu programu po dokončení simulácie predchádzajúcej operácie.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0051.jpg' | relative_url }})

Krok určuje nastavenia pre operáciu lisovania.

### Nastavenie 4. operácie: Prechod na druhý nástroj

#### Pridanie tretej operácie prenosu tepla

Po nastavení operácie tvárnenia pridajte ďalšiu operáciu prenosu tepla kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ako je znázornené na obr. 3DL7.52. Operáciu pomenujte ako „**Transfer 2**“ dvojitým kliknutím na položku „Názov operácie“ v editore operácií a stlačením klávesy Enter na klávesnici operáciu zatvorte.

#### Vyberte typ prenosu tepla 

Ako typ prenosu tepla vyberte „**Prenos vzduchom**“, ako je znázornené na obr. 3DL7.52, a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0052.jpg' | relative_url }})

Výber typu prenosu tepla pre prevod do druhého pracovného cyklu nástroja.

#### Nastavenie prevádzkových podmienok pre prevádzku s prenosom tepla

Na stránke „Stav procesu“ nastavte **čas prenosu** na **3** s pri **20** °C **okolitej teplote** s použitím predvoleného **konvekčného koeficientu** **0,02** N/s/mm/°C, ako je znázornené na obr. 3DL7.53. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Objekt“.

  
![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0053.jpg' | relative_url }})

Nastavenia podmienok spracovania pre prechod na druhú operáciu s nástrojom.

#### Odstrániť objekty typu „Die“

V tejto operácii využívame prenos vzduchom, preto musíme odstrániť oba objekty „Top die“ a „Bottom Die“. Stránka „Object“ by mala vyzerať tak, ako je znázornené na obr. 3DL7.54. Typ objektu „Workpiece“ ponecháme ako „Read from DB“, pretože ako počiatočné údaje pre túto operáciu potrebujeme načítat údaje objektu z posledného kroku predchádzajúcej simulácie. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Step“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0054.jpg' | relative_url }})

Stránka objektu týkajúca sa presunu do druhého nástroja. 

#### Definovanie ovládacích prvkov krokov 

Na stránke „Step“ nastavte počet krokov na 6, krok na 1 a definíciu kroku riešenia pre každý krok na 0,5 s. (Pozri obr. 3DL7.55.) Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Vytvorenie databázy“; databázu nebudeme vytvárať, pretože sa vytvorí počas behu programu po dokončení simulácie predchádzajúcej operácie. 

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0055.jpg' | relative_url }})

Ovládacie prvky krokov na prechod k druhej operácii s nástrojom.

### Nastavenie piateho pracovného kroku: Dokončenie kovania

#### Pridanie druhej formovacej operácie

Do laboratórneho cvičenia na nosiči ozubeného kolesa pridáme operáciu dokončovacieho kovania. Na karte Explorer v ľavej časti používateľského rozhrania prejdite na položku **Forming![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Single** a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky **[3D] Formovanie**, ako je znázornené na obr. 3DL7.56. Operáciu pomenujte „**Dokončovacie kovanie**“ dvojitým kliknutím na položku Názov operácie v editore operácií a stlačením klávesy Enter na klávesnici operáciu zatvorte.

  
![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0056.jpg' | relative_url }})

Pridanie operácie 3D tvarovania do nastavenia operácie konečného kovania.

#### Vyberte ovládacie prvky simulácie pre operáciu „Dokončenie“

V tejto operácii, podobne ako pri operácii „Upsetting“, ponecháme zaškrtnuté oba režimy – „Deformation“ aj „Heat Transfer“ – ako je znázornené na obr. 3DL7.57. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s objektom.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0057.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre operáciu „Dokončenie kovania“.

#### Definovanie objektov pre dokončenie kovania 

Na stránke objektov sa uistite, že boli pridané tri objekty, pričom pre objekt „obrobok“ je nastavený typ „Načítať z databázy“ a pre objekty „Horná forma“ a „Spodná forma“ je nastavený typ „**Pevný**“. Pozrite obr. 3DL7.58. Kliknite na objekt „Horná forma“ v stromovej štruktúre objektov. 

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0058.jpg' | relative_url }})

Stránka objektu „Dokončenie kováčskej operácie“.

#### Definovanie objektu hornej matrice

##### Nastavenie objektu hornej matrice

Na stránke objektu „Top Die“ ponechajte typ objektu ako „**Rigid**“ a zadajte teplotu **80** °C (pozri obr. 3DL7.59.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali a importovali geometriu „Top Die“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0059.jpg' | relative_url }})

Dokončite definíciu objektu hornej formy.

##### Definovanie geometrie hornej matrice na dokončovacie kovanie

Na stránke Geometria pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) načítajte súbor „**IDS_GC_Finish_Top****.stl**“ z inštalačnej zložky /3D/LABS/, ako je znázornené na obr. 3DL7.60. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) skontrolujte geometriu. Zobrazí sa okno kontroly geometrie, ktoré obsahuje prehľad geometrie objektu.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0060.jpg' | relative_url }})

Import geometrie hornej matrice pre kovanie metódou Finish.

Keďže importovaná geometria má rez 1/12, musíme definovať symetrické roviny. Symetrické roviny je možné definovať pomocou položky „Symetrické roviny“ na stránke geometrie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}) a vyberte symetrické plochy hornej matrice, ako je znázornené na obr. 3DL7.61. Definícia symetrických plôch sa prenesie do BCC počas generovania siete, ak to bude počas generovania siete povolené. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Mesh“ (Sieť).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0061.jpg' | relative_url }})

Určenie rovín symetrie pre hornú formu pri finálnom kovaní.

##### Vytvoriť sieť s najvyššou hustotou

Sieť vytvoríme s použitím predvoleného počtu 32 000 prvkov, ako je znázornené na obr. 3DL7.62. Počas vytvárania siete kliknite na „**Áno**“ v rozbaľovacom okne „Predvolené okrajové podmienky“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Materiál.

  
![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0062.jpg' | relative_url }})

Vytvorenie siete pre hornú maticu kováčskej formy.

##### Priradiť materiál pre hornú matricu

Zoznamu materiálov, ktorý bol načítaný už v predchádzajúcej operácii (pozri 7.4.3.7.4.), vyberte materiál **AISI-H13** a priraďte ho k hornej matrici. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku BCC.

##### Definovanie okrajových podmienok hornej formy

Na stránke BCC skontrolujte definované roviny symetrie a predvolené priradenie výmeny tepla s prostredím BCC na celý vonkajší povrch hornej matrice s výnimkou rovín symetrie, ako je znázornené na obr. 3DL7.63. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali pohyb.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0063.jpg' | relative_url }})

BCC pre finálne kovanie hornej matrice.

##### Nastavenie pohybu hornej matrice

Vyberte typ mechanického pohybu, nastavte **Celkový****zdvih** na hodnotu **270** mm, **Kovacie****zdvih** na hodnotu **24,6** mm a **Cyklus/s** na hodnotu **1,4** (pozri obr. 3DL7.64.). Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Spodná matrica.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0064.jpg' | relative_url }})

Dokončiť stránku s definíciami pohybov hornej matrice pri kovaní.

#### Definovanie typu objektu „spodná matrica“

##### Definovanie typu objektu „spodná matrica“

V okne objektu „Bottom Die“ ponechajte typ objektu ako „**Rigid**“ a nastavte teplotu na **80** °C (pozri obr. 3DL7.65.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali a importovali geometriu spodnej formy.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0065.jpg' | relative_url }})

Dokončiť tvorbu stránky objektu „Spodná matica“.

##### Definovanie geometrie spodnej matrice na dokončovacie kovanie

Na stránke Geometria pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) naimportujte súbor „**IDS_GC_Finish_Bot****.****stl**“ z inštalačnej cesty **/3D/LABS/**, ako je znázornené na obr. 3DL7.66. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) skontrolujte geometriu; zobrazí sa okno na kontrolu geometrie, ktoré obsahuje prehľad geometrie objektu.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0066.jpg' | relative_url }})

Import geometrie pre spodnú matricu kováčskeho nástroja Finish.

Keďže importovaná geometria má prierez 1/12, musíme definovať roviny symetrie. Roviny symetrie je možné definovať pomocou položky „Symmetry planes“ na stránke geometrie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}) a vyberte symetrické plochy spodnej matrice, ako je znázornené na obr. 3DL7.67. Definícia symetrických plôch sa prenesie do BCC počas generovania siete, ak to bude počas generovania siete povolené. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Mesh“ (Sieť).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0067.jpg' | relative_url }})

Určenie symetrických rovín pre spodnú formu na kovanie.

##### Vytvoriť sieť spodnej formy

Sieť vytvoríme s použitím predvoleného počtu 32 000 prvkov, ako je znázornené na obr. 3DL7.68. Počas vytvárania siete kliknite v rozbaľovacom okne „Predvolené okrajové podmienky“ na „**Áno**“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Materiál“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0068.jpg' | relative_url }})

Vytvorenie siete pre spodnú formu na kovanie metódou Finish.

##### Priradiť materiál pre spodnú matricu

Zoznamu materiálov, ktorý bol načítaný už v predchádzajúcej operácii (pozri 7.4.3.7.4), vyberte materiál **AISI-H13** a priraďte ho k spodnej matrici. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku BCC.

##### Definovanie okrajových podmienok spodnej formy

Na stránke BCC skontrolujte definované roviny symetrie a predvolene priradenú výmenu tepla s prostredím BCC pre celý vonkajší povrch spodnej matrice s výnimkou rovín symetrie, pozri obr. 3DL7.69.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0069.jpg' | relative_url }})

BCC pre dokončenie kovania spodnej matrice.

#### Definícia plánovaného umiestnenia

V operácii „Dokončenie kovania“ nie sú objekty v správnej polohe. Na ich správne umiestnenie použijeme funkciu „Plánované polohovanie“, keďže aktuálna operácia prebieha v dávkovom režime. Kliknite na odkaz **Plánované polohovanie** a pridajte akciu na plánované polohovanie spodnej matrice vo vzťahu k obrobku metódou kolízie v smere +Z, ako je znázornené na obr. 3DL7.70. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na stránku Kontakt.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0070.jpg' | relative_url }})

Naplánujte umiestnenie spodnej matrice pri záverečnej fáze kovania.

#### Naplánovanie generovania kontaktov pre operáciu „Dokončenie kovania“

Vyberte kontakt typu **užívateľ** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi obrobkom, hornou maticou a spodnou maticou (pozri obr. 3DL7.71.). Keďže matrice sú tuhé a obrobok je plastický, horná a spodná matrica sa považujú za hlavné objekty a obrobok za podriadený objekt. Uistite sa, že sú zaškrtnuté políčka Initialize a Generate v časti Schedule contact (pozri obr. 3DL7.71.), aby systém počas generovania databázy druhej operácie vytvoril vzájomný kontakt medzi objektmi. 

Zvýraznite vzťah medzi **hornou maticou** a **obrobkom** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) upravte podmienky kontaktu. Na karte „Trenie“ sa nachádza roletové menu, ktoré umožňuje používateľovi vybrať vhodné podmienky trenia pre bežné procesy tvárnenia. Keďže ide o simuláciu tvárnenia za tepla a matrice sú oceľové, použite roletové menu a zo zoznamu vyberte položku **Tvárnenie za tepla (mazané)**. Automaticky sa vyberie hodnota trenia **0,3**.

  
Podobne je potrebné upraviť tepelné údaje tak, aby sa použil koeficient prenosu tepla pre „tvarovanie“. Kliknite na kartu **Tepelné** a v roletovom menu vyberte položku **Tvarovanie**.

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite na stránku Kontakt. Keďže podmienky trenia sú rovnaké pre všetky páry objektov, tlačidlom ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných vzťahov. Po vykonaní tejto operácie budú mať všetky vzťahy trenie 0,3, ako je znázornené na obr. 3DL7.71. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

  
![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0071.jpg' | relative_url }})

Definícia vzťahu medzi objektmi v rámci operácie „Dokončenie kovania“.

#### Definovanie riadenia zastavenia

Na stránke „Stopping controls“ nastavte hodnotu **Max****load** na **1,0e6** N, ako je znázornené na obr. 3DL7.72. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Step“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0072.jpg' | relative_url }})

Ovládacie prvky na zastavenie operácie dokončovania kovania.

#### Definovanie ovládacích prvkov krokov 

V okne „Step Controls“ nastavte **počet krokov** na **200**, **Krok****prírastok** na **10** a **Riešenie****krok****definícia** pre každý krok na **0,5** s. (Pozri obr. 3DL7.73.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do okna Generate DB. 

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0073.jpg' | relative_url }})

Definícia krokového riadenia pre operáciu dokončovacieho kovania.

### Simulácia problému

Simuláciu spustíte kliknutím na popisok ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }})action a výberom možnosti „**Pokračovať v behu**“. (Pozri obr. 3DL7.74.)

  
![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0074.jpg' | relative_url }})

Otvorí sa okno „Spustiť simuláciu“.

  
  
Sledujte priebeh simulácie na kartách „Simulation Graphics“, „Simulation Message“ a „Simulation Log“ a uistite sa, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). (Pozri obr. 3DL7.75.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0075.jpg' | relative_url }})

Simulačný režim zobrazujúci simuláciu prenosu tepla v peci.

Po dokončení všetkých viacnásobných operácií sa v súbore protokolu simulácie zobrazí správa „MULTIPLE OPERATION COMPLETED.“; následne prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), kde si môžete prezrieť výsledky simulácie.

### Následné spracovanie

V postprocesore vykreslite stavovú premennú **Teplota** a prehrajte jednotlivé kroky od prvej operácie, aby ste mohli sledovať prenos tepla v obrobku a formách od vzduchového prenosu až po druhú tvárniacu operáciu. Rozloženie teploty v obrobku v poslednom kroku každej operácie je znázornené na obr. 3DL7.76.

  
![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0076.jpg' | relative_url }})

Rozloženie teploty v obrobku v poslednom kroku každej operácie od prenosu vzduchom až po finálne kovanie.

Kliknite na ikonu Zrkadlová symetria ![]({{ '/assets/icons/pre_icons/mo_mirror_merge_icon.jpg' | relative_url }}) a potom klikajte na symetrické plochy, kým neuvidíte celý diel. Bude to vyžadovať 11 kliknutí a celý diel sa v poslednom kroku simulácie zobrazí tak, ako je znázornené na obr. 3DL7.77.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab07_gear_carrier_lab/image0077.jpg' | relative_url }})

Zrkadlenie symetrických plôch obrobku v postprocesore.
