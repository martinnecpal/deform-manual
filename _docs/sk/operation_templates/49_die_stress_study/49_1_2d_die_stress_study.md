---
lang: sk
title: "49.1. Štúdia napätí v 2D čipe"
---

# 49.1. 2D analýza napätí v polotovare

49.1.1. Ako pridať analýzu napätia v matrici pre 2D konfiguráciu

49.1.2. Výber kroku

49.1.3. Okno „Objekty“

49.1.4. Typy objektov

49.1.5. Matrice

49.1.5.1. Všeobecné informácie

49.1.5.2. Geometria

49.1.5.3. Sieť objektu

49.1.5.4. Materiál predmetu

49.1.5.5. Okrajové podmienky objektu

49.1.5.6. Inicializácia

49.1.5.7. Interpolácia sily

49.1.5.8. Príslušenstvo

49.1.6. Ovládacie prvky

49.1.7. Kontakt

49.1.8. Ovládacie prvky simulácie

49.1.9. Vytvorenie databázy

## Ako pridať analýzu napätia v lisovacej forme pre 2D konfiguráciu

Po dokončení operácie 2D tvárnenia je možné v sprievodcovi MO pridať analýzu napätia v matrici z ponuky, ktorá sa zobrazí po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) v ľavom hornom rohu (pozri obr. 49.1.1. a obr. 49.1.2.). Po pridaní analýzy napätia v lisovacej forme sa pridá nová karta a operácia analýzy napätia v lisovacej forme sa automaticky pridá do editora operácií na tejto novej karte. Používateľ môže do jedného projektu MO v rôznych krokoch pridať aj viacero kariet s analýzou napätia v lisovacej forme. Projekt MO v rôznych krokoch.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0001.jpg' | relative_url }})

Pridanie analýzy napätia v matrici

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0002.jpg' | relative_url }})

Po pridaní analýzy napätia v matrici

## Výber kroku

V okne výberu kroku môže používateľ zvoliť číslo kroku, v ktorom sa má vykonať analýza napätia v matrici. Okno výberu kroku zobrazuje číslo kroku spolu s počtom simulácií, časom simulácie a zdvihom matrice. Používateľ môže nastaviť analýzu napätia v lisovacej forme pre akýkoľvek krok vybraný v okne výberu kroku, pozri obr. 49.1.3. a obr. 49.1.4.

  1. **Jeden krok** – Túto možnosť je potrebné zvoliť, ak chce používateľ simulovať analýzu napätia formy v jednom zvolenom kroku, pozri obr. 49.1.3.

     1. **Použiť vybraný krok** – Používateľ môže túto možnosť zapnúť pri analýze napätia v lisovacej forme s jedným krokom, aby sa použil aktuálny krok načítaný z databázy. Číslo aktuálneho vybraného kroku sa zobrazí v zátvorkách.

     2. **Načítať krok z databázy** – Používateľ môže túto možnosť zapnúť pri analýze napätia v matrici s jedným krokom, aby načítal z nominálnej databázy iný krok, ako je aktuálne načítaný. Po výbere tejto možnosti sa otvorí okno na výber kroku s krokmi uloženými v nominálnej databáze, kde si používateľ môže vybrať jeden z uvedených krokov.

  1. **Viac krokov** – Túto možnosť je potrebné zvoliť v prípade, ak chce používateľ simulovať analýzu napätia v lisovacej forme pre viacero vybraných krokov jednej operácie, pozri obr. 49.1.4. V súčasnosti program DEFORM® podporuje analýzu napätia v lisovacej forme vo viacerých krokoch iba pre kroky vybrané v rámci jednej operácie. Používatelia môžu pre každú operáciu nezávisle pridať ďalšie operácie analýzy napätia v lisovacej forme. Pri použití možnosti viacerých krokov nastavíme analýzu napätia v lisovacej forme pre prvý krok z vybraných krokov a pre nasledujúce kroky analýzy napätia v lisovacej forme naplánujeme interpoláciu síl pôsobiacich na obrobok. Údaje o objekte, ovládacie prvky simulácie a ďalšie nastavenia sa prenesú z prvého kroku analýzy napätia v lisovacej forme. 

     1. **Použiť vybraný krok** – Používateľ môže túto možnosť zapnúť, aby pri nastavení analýzy napätia v matrici použil aktuálny krok načítaný z databázy. Číslo aktuálneho vybraného kroku sa zobrazí v zátvorkách.

     2. **Načítať krok z databázy** – Používateľ môže túto možnosť zapnúť, aby mohol vybrať iné kroky z nominálnej databázy, ako je aktuálne načítaný krok. Po zvolení tejto možnosti sa otvorí okno na výber krokov s krokmi uloženými v nominálnej databáze, kde si používateľ môže vybrať iné kroky zo zoznamu. Výber krokov je možné vykonať pomocou možností výberu zobrazených na obr. 49.1.4.

        1. **Auto** – Použite kroky, ktoré systém vyberie automaticky.

        2. **Žiadne** – Zrušenie výberu všetkých vybraných krokov, aby sme mohli vybrať nové.

        3. **Všetko** – Ak chcete vybrať všetky kroky v databáze, majte na pamäti, že program DEFORM® v súčasnosti podporuje analýzu napätia pri viacerých krokoch len pre kroky vybrané v rámci jednej operácie.

        4. **Definované používateľom** – Vyberte kroky podľa požiadaviek používateľa; používateľ môže na výber krokov použiť buď možnosť „Inkrement“, alebo „Počet krokov z rozsahu“.

  * **Krok** \- na výber krokov na základe zadejanej hodnoty kroku.

  * **Počet krokov** – Systém vyberie definovaný počet krokov tak, aby boli rovnomerne rozložené.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0021.jpg' | relative_url }})

Okno na výber krokov v rámci štúdie namáhania pri jednokrokovom lisovaní.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0003.jpg' | relative_url }})

Okno na výber krokov v štúdii namáhania matice s viacerými krokmi.

## Okno „Objekty“

Používateľ môže pridať požadovaný počet ďalších objektov pre simuláciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Obr. 49.1.5. znázorňuje objekty, ktoré prešli z nominálnej prevádzky do prevádzky s namáhaním formy. Používateľ môže na základe nastavenia pridať potrebné upínacie prvky a ďalšie komponenty.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0004.jpg' | relative_url }})

Okno „Objekty“

## Typy objektov

Štúdia zaťaženia podporuje typy objektov „Rigid“ a „Elastic“.

  
Objekty, pre ktoré je potrebný výstup napätia, sa považujú za pružné objekty. Tieto objekty budú rozdelené na sieť a sily sa interpolujú z obrobku.

  
Upevňovacie prvky, pri ktorých nie je potrebné vypočítať napätie, sa považujú za tuhé objekty. Tieto objekty nevyžadujú vytvorenie siete, pokiaľ nie je potrebné vykonať výpočty prenosu tepla.

## Matrice

### Okno „Všeobecné vlastnosti objektu“

V tomto okne môže používateľ nastaviť teplotu objektu a vybrať typ objektu, ako je znázornené na obr. 49.1.6. V prípade foriem prevzatých z nominálneho nastavenia je typ objektu predvolene nastavený na „Elastic“ (Pružný). Ak používateľ nechce vypočítať napätia na objekte, môže zvoliť typ objektu „Rigid“ (Tuhý). Od verzie v13.1.1 boli na stránke objektu zavedené dve nové možnosti na umiestnenie foriem v budúcich krokoch, pozri obr. 49.1.6.  
Umiestnenie formy v nasledujúcich krokoch pri viacstupňovej analýze napätia formy:  
V prípade viackrokového posudzovania napätia v lisovacej forme, ak objekt vyžaduje polohovanie, musí používateľ určiť, ako má byť objekt v nasledujúcich krokoch polohovaný, a to zaškrtnutím políčka „Potreba polohovania“ na stránke objektu, ako je znázornené na obr. 49.1.6. 

  * Ak je objekt súčasťou nominálnej konfigurácie a vyžaduje polohovanie, musí používateľ zaškrtnúť políčko „Vyžaduje polohovanie“ a z nominálnej konfigurácie vybrať príslušný objekt ako „Nasledujúci objekt“.

  * Ak objekt nie je súčasťou nominálnej konfigurácie, ale nachádza sa v ohraničujúcom obdĺžniku objektu nominálnej konfigurácie a vyžaduje polohovanie, musí používateľ zaškrtnúť políčko „Vyžaduje polohovanie“ a z nominálnej konfigurácie vybrať príslušný objekt, v ktorého ohraničujúcom obdĺžniku sa aktuálny objekt nachádza, ako „Nasledujúci objekt“. Zaškrtávacie políčko „Nie je pôvodný objekt“ by sme nemali zaškrtnúť, aby bolo možné na aktuálny objekt použiť interpoláciu síl z nominálnej konfigurácie.

  * Ak objekt nie je súčasťou nominálnej konfigurácie a nenachádza sa v ohraničujúcom obdĺžniku žiadneho z objektov nominálnej konfigurácie a vyžaduje polohovanie, musí používateľ zaškrtnúť políčko „Vyžaduje polohovanie“ a vybrať objekt z nominálnej konfigurácie, s ktorým sa aktuálny objekt dotýka, alebo ho označiť ako „Nasledujúci objekt“. Mali by sme tiež zaškrtnúť políčko „Nie je pôvodný objekt“. Ak používateľ zaškrtne políčko „Nie je pôvodný objekt“ pre daný objekt, na tento objekt sa nebude vykonávať interpolácia síl.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0005.jpg' | relative_url }})

Okienko hornej matrice

### Geometria

Používateľ môže definovať novú geometriu alebo upraviť existujúcu geometriu pomocou možností v okne geometrie. Okno geometrie ponúka základné možnosti na definovanie geometrie (pozri obr. 49.1.7.). Geometriu je možné importovať aj pomocou možnosti „Importovať geometriu zo súboru“ (![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})) alebo pomocou možnosti „Importovať z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})). Používateľ môže tiež importovať geometrie v iných formátoch, ako sú napríklad .DXF a .IGES. Na jednoduché definovanie základných geometrických tvarov sú k dispozícii primitívy. Ďalšie informácie o vytváraní a úprave 2D geometrií nájdete v [12.1. 2D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/) a [12.2. 2D Geometry Data Editing.](/docs/en/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/)

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0006.jpg' | relative_url }})

Okno Geometria

### Sieť objektu

Stránka „Mesh“ ponúka možnosti vytvorenia siete pre objekt. Všetky formy, na ktorých je potrebné vypočítať napätia, by mali byť pokryté sieťou. Stránka „Mesh“ umožňuje používateľovi nastaviť počet prvkov pomocou posuvníka alebo ručným zadávaním na účely vytvorenia siete, pozri obr. 49.1.8. Používatelia môžu využiť expertný režim na definovanie požadovanej siete; ďalšie informácie týkajúce sa expertných možností vytvárania sietí nájdete v [13.1. 2D Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/). 

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0007.jpg' | relative_url }})

Okno so sieťkou

### Materiál objektu

V okne „Materiál“ sa zobrazujú všetky materiály zdedené z nominálnej operácie; používatelia môžu tiež načítať materiál potrebný pre túto operáciu v okne „Materiál objektu“ pomocou funkcie „Importovať údaje o materiáli zo súboru“ (![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})) alebo pomocou možnosti „Načítať z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})), pozri obr. 49.1.9.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0008.jpg' | relative_url }})

Okno s materiálmi

### Okrajové podmienky objektu

Keď interpolujeme sily pôsobiace zo sochoru, pôsobia sily na matrice, čo spôsobuje, že sa matrice počas simulácie posúvajú nepravidelne. Aby sa zabránilo nepravidelnému posunu matríc, je potrebné priradiť vhodné okrajové podmienky. Na zastavenie posunu foriem možno použiť rýchlostné okrajové podmienky (BCC), pozri obr. 49.1.10. Rýchlostné okrajové podmienky sú priradené k hornému okraju formy, ako je znázornené na obr. 49.1.11.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0009.jpg' | relative_url }})

Okno „Okrajové podmienky“

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0010.jpg' | relative_url }})

Okrajové podmienky rýchlosti priradené v smere Y

**Tepelné sťahovanie**

Funkciu „Shrink Fit BCC“ je možné použiť na definovanie podmienok teplovzťahového spojenia medzi vložkou matrice a teplovzťahovým krúžkom. V prípade 2D objektov je teraz možné definovať teplovzťahové spojenie pomocou možností „Auto“ a „User“.

  * **Auto** – Systém automaticky určí toleranciu medzi zvolenou hranou aktuálneho objektu a najbližším objektom.

  * **Používateľ** – Používateľ musí hodnotu rušenia zadať ručne, a to

    * Pri výbere smeru zvoľte smer kolmý na vnútornú plochu zmršťovacieho krúžku alebo vonkajšiu plochu vložky matrice.

    * Výber vnútornej plochy zmršťovacieho krúžku alebo vonkajšej plochy vložky matrice, teda plochy, ktorá prichádza do styku s matricou.

    * Nastavenie hodnoty zúženého uloženia – Ak sa zúžené uloženie uplatňuje na vnútorný objekt, hodnota by mala byť záporná, a ak sa zúžené uloženie uplatňuje na vonkajší objekt, hodnota by mala byť kladná.

Na obr. 49.1.12 a obr. 49.1.13 je znázornené použitie BCC s tepelne zmrštiteľným spojom na zmrštiteľnom krúžku. Ďalšie informácie o tepelne zmrštiteľných spojoch nájdete v dokumente [2D Die Stress Analysis - Theory.]().

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0011.jpg' | relative_url }})

Okno BCC s termoplastickým upevnením

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0012.jpg' | relative_url }})

Priradené okrajové podmienky pre tepelné zmrštenie

### Inicializácia

V okne „Initialize“ sú na inicializáciu k dispozícii niektoré bežne používané stavové premenné, ako napríklad teplota, deformácia, napätie, poškodenie, rýchlosť, posun atď.

Používateľ môže inicializovať hodnoty týchto stavových premenných kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). Obr. 49.1.14 znázorňuje rôzne stavové premenné, ktoré sú k dispozícii v okne „Initialize“. V závislosti od typu stavovej premennej ich môže používateľ inicializovať aj z dátových okien uzlov a prvkov. Ďalšie informácie o tom, ako inicializovať stavové premenné v oknách „Node“ a „Element“, nájdete v [17.1. Node Data Window](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) a [17.2. Element Data Window](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/).

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0013.jpg' | relative_url }})

Inicializovať okno

### Interpolácia s vynútením

Na interpoláciu síl z objektu obrobku na lisovacie formy musí používateľ v okne „Interpolácia síl“ vybrať možnosť ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}); používateľ môže tiež odstrániť interpolovanú silu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_delete_interpolate_force_button.jpg' | relative_url }}) (pozri obr. 49.1.15. a obr. 49.1.16.).

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0014.jpg' | relative_url }})

Okno „Vynútiť interpoláciu“

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0015.jpg' | relative_url }})

Interpolované sily

###  Zápasy

V tejto operácii je možné definovať upínacie prípravky, ktoré držia formy. Upínacie prípravky sa v tejto operácii považujú za tuhé objekty. Definícia a úprava geometrie týchto objektov je podobná ako v prípade foriem. Ak sú zapnuté tepelné výpočty, je potrebné pre tieto objekty definovať sieť, kryštálovú mriežku BCC a materiál; tieto premenné je možné definovať podobným spôsobom ako v prípade foriem.

## Ovládacie prvky

Obr. 49.1.17. znázorňuje okno Ovládacie prvky, v ktorom môže používateľ umiestniť upínacie prvky a objekty matice pridané pomocou tlačidla „Umiestniť objekty“ ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}). Toto umiestnenie sa uplatní iba pre aktuálne vybraný krok a v nasledujúcich krokoch sa nebude používať. Na umiestnenie objektov sú k dispozícii rôzne možnosti umiestnenia (pozri obr. 49.1.18.). Ďalšie informácie o týchto možnostiach nájdete v [16.Object Positioning](/docs/en/pre_processor/16_object_properties/16_object_properties/).

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0016.jpg' | relative_url }})

Okno ovládacích prvkov

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0017.jpg' | relative_url }})

Okno „Polohovanie objektu“

## Kontakt

Účelom vzťahov medzi objektmi je definovať, ako rôzne objekty v simulácii vzájomne interagujú. V okne „Inter-object“ sú všetky možné vzťahy už uvedené v zozname (pozri obr. 49.1.19.). Používateľ musí pre objekty, ktoré sú v kontakte v rámci zvoleného vzťahu, definovať typ vzťahu a hodnotu trenia.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0018.jpg' | relative_url }})

Okno „Inter Object“ (režim s návodom)

## Riadenie simulácie

**Počet simulačných krokov:** Ak sa analýza napätí vykonáva len na jednom nástroji, na získanie presných hodnôt napätí stačí simulácia v jednom kroku. Ak sa analýza napätí vykonáva na zostavách lisovacích nástrojov, kde dochádza k interakcii medzi nástrojmi, zvyčajne je potrebných viac ako jeden krok, aby sa sústava nástrojov dostala do rovnovážneho stavu pri pôsobiacom zaťažení.

Používateľ môže aktivovať tepelný výpočet tak, že v expertnom režime zapne režim prenosu tepla a v nastaveniach BCC objektu zadá príslušné tepelné BCC a v okne medzi objektmi zadá hodnoty koeficientov prenosu tepla.

**Počet krokov na uloženie:** Počet krokov na uloženie do databázy určuje, koľko krokov systém uloží do databázy. Pri spustení simulácie sa musí vypočítať každý krok, ale nie je nutné, aby sa všetky kroky uložili do databázy. Keďže počet krokov, ktoré sa budú simulovať pri analýze napätia v liatej forme, je nižší, používateľ môže uložiť každý krok.

**Riadenie veľkosti kroku:** Veľkosť kroku riešenia sa riadi časovým krokom. Maximálny čas trvania procesu na jeden krok možno pre operácie analýzy napätia v matrici nastaviť na 1 sekundu. Obr. 49.1.20. znázorňuje okno „Simulation Controls“ (Ovládacie prvky simulácie).

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0019.jpg' | relative_url }})

Okno riadenia simulácie

Ďalšie informácie a popis možností v časti „Ovládacie prvky simulácie“ nájdete v dokumente [9\. Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/).

## Vytvoriť databázu

**Kontrola údajov** ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}): Týmto sa vykonáva kontrola údajov. Ak sú údaje správne, môžeme vygenerovať databázu. Ak sa však počas kontroly údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vygenerovaním databázy. Chyby zabránia vygenerovaniu databázy, zatiaľ čo varovania vygenerovanie databázy neumožnia.

**Vytvorenie databázy:** Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) sa vytvorí databáza pre inštaláciu. (Pozri obr. 49.1.21.)

**Pridať súbor .key:** Akékoľvek informácie, ktoré nie sú definované v sprievodcovi, ale stále sa vzťahujú na daný proces, je možné načítať ako súbor .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt – tieto hodnoty je možné definovať v súbore .key, potom stačí zmeniť len tento súbor a simuláciu je možné odoslať znova.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0020.jpg' | relative_url }})

Okno na generovanie databázy

**Súvisiace témy:**

[49\. Introduction to Die Stress Study](/docs/en/operation_templates/49_die_stress_study/49_introduction_to_die_stress_study/)

[49.2. 3D Die Stress Study](/docs/en/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/)
