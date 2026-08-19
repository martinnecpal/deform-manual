---
lang: sk
title: "49.2. 3D analýza napätí v čipe"
---

# 49.2. 3D analýza napätia v polovodičovej matici 

49.2.1. Ako pridať analýzu napätí v lisovacej forme pre 3D konfiguráciu

49.2.2. Výber kroku

49.2.3. Okno „Objekty“

49.2.4. Typy objektov

49.2.5. Matrice

49.2.5.1. Všeobecné informácie

49.2.5.2. Geometria

49.2.5.3. Sieť objektu

49.2.5.4. Materiál objektu

49.2.5.5. Okrajové podmienky objektu

49.2.5.6. Inicializácia

49.2.5.7. Interpolácia sily

49.2.5.8. Príslušenstvo

49.2.6. Ovládacie prvky

49.2.7. Kontakt

49.2.8. Ovládacie prvky simulácie

49.2.9. Vytvorenie databázy

## Ako pridať analýzu napätia v lisovacej forme pre 3D nastavenie

Štúdiu napätia v matrici je možné pridať v sprievodcovi MO z ponuky, ktorá sa zobrazí po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) v ľavom hornom rohu (pozri obr. 49.2.1.), Po pridaní analýzy napätia v matrici sa pridá nová karta a operácia analýzy napätia v matrici sa automaticky pridá do editora operácií na novej karte, pozri obr. 49.2.2. Používateľ môže do jedného projektu MO pridať aj viacero kariet analýzy napätia v matrici v rôznych krokoch. 

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0001.jpg' | relative_url }})

Pridanie analýzy napätia v matrici

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0002.jpg' | relative_url }})

Po pridaní analýzy napätia v matrici

## Výber kroku

V okne výberu kroku môže používateľ vybrať číslo kroku, v ktorom sa má vykonať analýza napätia v matrici. Okno výberu kroku zobrazuje číslo kroku spolu s počtom simulácií, časom simulácie a zdvihom matrice. Používateľ môže nastaviť analýzu napätia v lisovacej forme pre ľubovoľný krok vybraný v okne výberu kroku, pozri obr. 49.2.3. a obr. 49.2.4.

  1. **Jeden krok** – Túto možnosť je potrebné zvoliť v prípade, ak chce používateľ simulovať analýzu napätí v lisovacej forme v jednom vybranom kroku, pozri obr. 49.2.3.

     1. **Použiť vybraný krok** – Používateľ môže túto možnosť zapnúť pri analýze napätia v lisovacej forme v jednom kroku, aby sa použil aktuálny krok načítaný z databázy. Číslo aktuálneho vybraného kroku sa zobrazí v zátvorkách.

     2. **Načítať krok z databázy** – Používateľ môže túto možnosť aktivovať pri analýze napätia v lisovacej matrici s jedným krokom, aby z nominálnej databázy načítal iný krok, ako je aktuálne načítaný. Po výbere tejto možnosti sa otvorí okno na výber kroku s krokmi uloženými v nominálnej databáze, kde si používateľ môže vybrať jeden z uvedených krokov.

  1. **Viac krokov** – Túto možnosť je potrebné zvoliť v prípade, ak chce používateľ simulovať analýzu napätia v lisovacej forme pre viacero vybraných krokov jednej operácie, pozri obr. 49.2.4. V súčasnosti program DEFORM® podporuje analýzu napätí v lisovacej forme vo viacerých krokoch iba pre kroky vybrané z jednej operácie. Používatelia môžu pre každú operáciu nezávisle pridať ďalšie operácie analýzy napätí v lisovacej forme. Pri použití možnosti viacerých krokov nastavíme analýzu napätia v lisovacej forme pre prvý z vybraných krokov a pre nasledujúce kroky analýzy napätia v lisovacej forme naplánujeme interpoláciu síl pôsobiacich na obrobok. Údaje o objektoch, ovládacie prvky simulácie a ďalšie nastavenia sa prenesú z prvého kroku analýzy napätia v lisovacej forme. 

     1. **Použiť vybraný krok** – Používateľ môže túto možnosť zapnúť, aby pri nastavení analýzy napätia v lisovacej forme použil aktuálny krok načítaný z databázy. Číslo aktuálneho vybraného kroku sa zobrazí v zátvorkách.

     2. **Načítať krok z databázy** – Používateľ môže túto možnosť zapnúť, aby mohol z nominálnej databázy vybrať iné kroky, ako je aktuálne načítaný krok. Po zvolení tejto možnosti sa otvorí okno na výber krokov s krokmi uloženými v nominálnej databáze, z ktorých môže používateľ vybrať iné kroky zo zoznamu. Výber krokov je možné vykonať pomocou volieb zobrazených na obr. 49.2.4.

        1. **Auto** – Použite kroky, ktoré systém vyberie automaticky.

        2. **Žiadne** – Zrušenie výberu všetkých vybraných krokov, aby sme mohli vybrať nové.

        3. **Všetko** – Ak chcete vybrať všetky kroky v databáze, majte na pamäti, že program DEFORM® v súčasnosti podporuje analýzu napätia pri viacerých krokoch len pre kroky vybrané v rámci jednej operácie.

        4. **Definované používateľom** – Vyberte kroky na základe požiadaviek používateľa; používateľ môže na výber krokov použiť buď možnosť „Inkrement“, alebo „Počet krokov z rozsahu“.

  * **Krok** \- na výber krokov na základe definovanej hodnoty kroku.

  * **Počet krokov** – Systém vyberie definovaný počet krokov tak, aby boli rovnomerne rozložené.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0021.jpg' | relative_url }})

Okno na výber krokov v štúdii namáhania s jednokrokovou matricou.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0003.jpg' | relative_url }})

Okno výberu krokov v štúdii o namáhaní foriem s viacerými krokmi

## Okno „Objekty“

Používateľ môže pridať požadovaný počet ďalších objektov pre simuláciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Obr. 49.2.5. znázorňuje objekty, ktoré prešli z nominálnej prevádzky do prevádzky s namáhaním matrice. Používateľ môže na základe nastavenia pridať potrebné upínacie prvky a ďalšie komponenty.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0004.jpg' | relative_url }})

Okno „Objekty“

## Typy objektov

Štúdia o namáhaní podporuje typy objektov „Rigid“ (tuhý) a „Elastic“ (pružný).

  
Objekty, pre ktoré sa vyžaduje výstup napätia, sa považujú za pružné objekty. Tieto objekty budú rozdelené na sieť a sily sa interpolujú z obrobku.

  
Upevňovacie prvky, pri ktorých nie je potrebný výstup napätia, sa považujú za tuhé prvky. Tieto prvky nevyžadujú vytvorenie siete, pokiaľ sa nemajú vykonávať výpočty prenosu tepla.

## Matrice

### Okno „Všeobecné nastavenia objektu“

V tomto okne môže používateľ nastaviť teplotu objektu a vybrať typ objektu, ako je znázornené na obr. 49.2.6. V prípade foriem prevzatých z nominálneho nastavenia je typ objektu predvolene nastavený na „Elastic“ (Pružný). Ak používateľ nechce vypočítať napätia v objekte, môže zvoliť typ objektu „Rigid“ (Tuhý). Od verzie v13.1.1 boli na stránke objektu zavedené dve nové možnosti na umiestnenie foriem v nasledujúcich krokoch, pozri obr. 49.2.6.

  
**Umiestnenie formy v nasledujúcich krokoch viacstupňovej analýzy napätia formy:**

  
V prípade viackrokového posúdenia napätia v lisovacej forme, ak objekt vyžaduje polohovanie, musí používateľ určiť, ako má byť objekt v nasledujúcich krokoch polohovaný, a to zaškrtnutím políčka „Potreba polohovania“ na stránke objektu, ako je znázornené na obr. 49.2.6.

  * Ak je objekt súčasťou nominálnej konfigurácie a vyžaduje polohovanie, musí používateľ zaškrtnúť políčko „Vyžaduje polohovanie“ a z nominálnej konfigurácie vybrať príslušný objekt ako „Nasledujúci objekt“.

  * Ak objekt nie je súčasťou nominálnej konfigurácie, ale nachádza sa v ohraničujúcom obdĺžniku objektu nominálnej konfigurácie a vyžaduje polohovanie, musí používateľ zaškrtnúť políčko „Potrebuje polohovanie“ a z nominálnej konfigurácie vybrať príslušný objekt, v ktorého ohraničujúcom obdĺžniku sa aktuálny objekt nachádza, ako „Nasledujúci objekt“. Zaškrtávacie políčko „Nie je pôvodný objekt“ by sme nemali zaškrtávať, aby bolo možné na aktuálny objekt aplikovať interpoláciu síl z nominálnej konfigurácie.

  * Ak objekt nie je súčasťou nominálnej konfigurácie, nenachádza sa v ohraničujúcom obdĺžniku žiadneho z objektov nominálnej konfigurácie a vyžaduje polohovanie, musí používateľ zaškrtnúť políčko „Vyžaduje polohovanie“ a vybrať objekt z nominálnej konfigurácie, s ktorým prichádza aktuálny objekt do styku, alebo ho nastaviť ako „Nasledujúci objekt“. Mali by sme tiež zaškrtnúť políčko „Nie je pôvodný objekt“. Ak používateľ zaškrtne políčko „Nie je pôvodný objekt“ pre daný objekt, na tento objekt sa nebude vykonávať interpolácia síl.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0005.jpg' | relative_url }})

Stránka objektu

### Geometria

Používateľ môže definovať novú geometriu pomocou možností v okne geometrie. Okno geometrie ponúka základné možnosti na definovanie geometrie (pozri obr. 49.2.7.). Geometriu je možné importovať aj pomocou možnosti „Importovať geometriu zo súboru“ (![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})) alebo pomocou možnosti „Importovať z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})). Používateľ môže tiež importovať geometrie v iných formátoch, ako sú .key, .DB, .STL, .PDA, .NAS a .UNV. Na jednoduché definovanie základných geometrických tvarov sú k dispozícii primitívy. Ďalšie informácie o vytváraní a úpravách 3D geometrií nájdete v [12.3. 3D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/).

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0006.jpg' | relative_url }})

Okno Geometria

### Sieť objektu

Stránka „Mesh“ ponúka možnosti vytvorenia siete pre objekt. Všetky formy, na ktorých je potrebné vypočítať napätia, by mali byť pokryté sieťou. Stránka „Mesh“ umožňuje nastaviť počet prvkov pomocou posuvníka na vytvorenie siete. Možnosti vytvárania siete dostupné v okne „Mesh“ v režime „Guided“ sú zobrazené na obr. 49.2.8. Ďalšie informácie týkajúce sa možnosti vytvorenia siete v režime Expert nájdete v dokumentácii [13.2. 3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/) a [13.3. 3D Brick Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/).

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0007.jpg' | relative_url }})

Okno so sieťkou

**Cieľový počet prvkov**: Počet prvkov, ktoré sa majú pre daný objekt vygenerovať, je možné určiť jednoduchým posunutím posuvníka a výberom vhodnej hodnoty pre aktuálnu simuláciu.

**Vytvorenie siete**: Sieť je možné vytvoriť kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

**Odstrániť sieť:** Táto funkcia odstráni vygenerovanú sieť.

### Materiál objektu

V okne „Materiál“ sa zobrazujú všetky materiály zdedené z nominálnej operácie; používatelia môžu materiál potrebný pre túto operáciu načítať aj v okne „Materiál objektu“ pomocou funkcie „Importovať údaje o materiáli zo súboru“ (![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})) alebo pomocou možnosti „Načítať z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})), pozri obr. 49.2.9.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0008.jpg' | relative_url }})

Okno s materiálmi

### Okrajové podmienky objektu

Keď interpolujeme sily pôsobiace na polotovar, pôsobia tieto sily na lisovacie formy, čo spôsobuje, že sa formy počas simulácie pohybujú nepravidelne.

Aby sa zabránilo nepravidelnému posunu foriem, je potrebné nastaviť vhodné okrajové podmienky. Na zastavenie posunu foriem možno použiť rýchlostnú BCC, pozri obr. 49.2.10. Rýchlostná BCC je nastavená na hornom okraji formy, ako je znázornené na obr. 49.2.11. 

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0009.jpg' | relative_url }})

Okno s okrajovými podmienkami

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0010.jpg' | relative_url }})

Okrajové podmienky rýchlosti priradené v smere Z

**Tepelné zúženie:**  
3D model BCC s tepelne zmrštiteľným spojom, ktorý sa používa na analýzu napätia v matrici; podmienky tepelne zmrštiteľného spoja sú definované medzi vložkou matrice a zmrštiteľným krúžkom. To je možné definovať nasledujúcimi krokmi:

**V prípade valcovej metódy,**

  * Zadanie hodnoty rušenia.

  * Voľba smeru (smer kolmý na vnútornú plochu zmršťovacieho krúžku alebo vonkajšiu plochu vložky lisovacej formy)

  * Výber vnútornej plochy zmršťovacieho krúžku alebo vonkajšej plochy vložky matrice (plochy, ktorá prichádza do styku s matricou)

**V prípade metódy „kolmo na povrch“,**

  * Používateľ musí zadať hodnotu interferencie; Deform automaticky vyberie smer kolmý na povrch.

  * Zadanie hodnoty rušenia.

  * Výber vnútornej plochy zmršťovacieho krúžku alebo vonkajšej plochy vložky matrice (plochy, ktorá prichádza do styku s matricou)

Ak sa zúženie aplikuje na vnútorný objekt, hodnota by mala byť záporná, a ak sa zúženie aplikuje na vonkajší objekt, hodnota by mala byť kladná.

Ďalšie informácie o montáži s tepelne zmrštiteľným spojom nájdete v dokumente [3D Die Stress Analysis.](/docs/en/operation_templates/30_die_stress/3d_die_stress_analysis_theory/) na obr. 49.2.12. a obr. 49.2.13. znázorňujú montáž s tepelne zmrštiteľným spojom BCC na zmrštiteľnom krúžku.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0011.jpg' | relative_url }})

Okno BCC s termoplastickým upevnením

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0012.jpg' | relative_url }})

Priradené okrajové podmienky pre zúženie

### Inicializácia

V okne „Initialize“ sú k dispozícii na inicializáciu niektoré bežne používané stavové premenné, ako napríklad teplota, deformácia, napätie, poškodenie, rýchlosť, posunutie atď.

Používateľ môže inicializovať hodnoty týchto stavových premenných kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). Obr. 49.2.14 znázorňuje rôzne stavové premenné, ktoré sú k dispozícii v okne „Initialize“. V závislosti od typu stavovej premennej ich môže používateľ inicializovať aj z dátových okien uzlov a prvkov. Ďalšie informácie o tom, ako inicializovať stavové premenné v oknách „Node“ a „Element“, nájdete v [17.1. Node Data Window](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) a [17.2. Element Data Window](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/).

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0013.jpg' | relative_url }})

Inicializovať okno

###  Interpolácia s vynútením

Na interpoláciu síl z objektu obrobku do foriem musí používateľ kliknúť na ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) v okne „Interpolácia síl“; používateľ môže tiež odstrániť interpolovanú silu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_delete_interpolate_force_button.jpg' | relative_url }}) (pozri obr. 49.2.15. a obr. 49.2.16.).

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0014.jpg' | relative_url }})

Okno „Interpolácia sily“

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0015.jpg' | relative_url }})

Interpolované sily

### Rozpis zápasov

V tejto operácii je možné definovať upínacie prípravky, ktoré držia formy. Upínacie prípravky sa v tejto operácii považujú za tuhé objekty. Definícia a úprava geometrie týchto objektov je podobná ako v prípade foriem. Ak sú zapnuté tepelné výpočty, je potrebné pre tieto objekty definovať sieť, mriežku BCC a materiál; tieto premenné je možné definovať podobným spôsobom ako v prípade foriem.

## Ovládacie prvky

Obr. 49.2.17. znázorňuje okno „Ovládacie prvky“, v ktorom môže používateľ umiestňovať upínacie prvky a objekty foriem pridané pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}). Toto umiestnenie sa uplatní iba pre aktuálne vybraný krok a v nasledujúcich krokoch sa nebude používať. Na umiestnenie objektov sú k dispozícii rôzne možnosti umiestnenia (pozri obr. 49.2.18.). Ďalšie informácie o týchto možnostiach nájdete v [19.Object Positioning.](/docs/en/pre_processor/19_object_positioning/19_object_positioning/).

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0016.jpg' | relative_url }})

Okno ovládacích prvkov

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0017.jpg' | relative_url }})

Okno „Polohovanie objektu“

## Kontakt

Účelom vzťahov medzi objektmi je definovať, ako rôzne objekty v simulácii vzájomne interagujú.

V okne „Medzi objektmi“ sú už v zozname uvedené všetky možné vzťahy (pozri obr. 49.2.19.). Používateľ musí pre objekty, ktoré sú v kontakte, definovať typ vzťahu a hodnotu trenia pre vybraný vzťah. Ďalšie informácie týkajúce sa stránky „Kontakt“ v expertnom režime nájdete v [20\. Inter-Object Data Definition](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/).

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0018.jpg' | relative_url }})

Okno „Vzťahy medzi objektmi“

## Riadenie simulácie

**Počet simulačných krokov:** Ak sa analýza napätí vykonáva len na jednom nástroji, na získanie presných hodnôt napätí stačí simulácia v jednom kroku. Ak sa analýza napätí vykonáva na zostavách lisovacích nástrojov, kde dochádza k interakcii medzi nástrojmi, zvyčajne je potrebných viac ako jeden krok, aby sa sústava nástrojov dostala do rovnovážneho stavu pri pôsobiacom zaťažení.

Používateľ môže aktivovať tepelný výpočet tak, že v režime Expert zapne režim prenosu tepla a v nastaveniach BCC objektu definuje príslušné tepelné BCC a v okne medzi objektmi nastaví hodnoty koeficientov prenosu tepla.

**Počet krokov na uloženie:** Počet krokov na uloženie do databázy určuje, koľko krokov systém uloží do databázy. Pri spustení simulácie sa musí vypočítať každý krok, ale nie je nutné, aby bol každý krok uložený do databázy. Keďže počet krokov, ktoré sa budú simulovať pri analýze napätia v lisovacej forme, je nižší, používateľ môže uložiť každý krok.

**Riadenie veľkosti kroku:** Veľkosť kroku riešenia sa riadi časovým krokom. Maximálny čas, ktorý môže uplynúť na jeden krok, možno pre operácie analýzy napätia v matrici nastaviť na 1 sekundu. 

Na obr. 49.2.20 je zobrazené okno „Simulation Controls“.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0019.jpg' | relative_url }})

Okno riadenia simulácie

Ďalšie informácie a popis možností v ovládacích prvkoch simulácie nájdete v [9\. Simulation Controls.](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

## Vytvoriť databázu

**Kontrola údajov ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}):** Táto kontrola overuje údaje. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvorenie databázy:** Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) sa vytvorí databáza pre inštaláciu (pozri obr. 49.2.21.).

**Pridať súbor .key:** Akékoľvek informácie, ktoré nie sú definované v sprievodcovi, ale stále sa vzťahujú na daný proces, je možné načítať ako súbor .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt – tieto hodnoty je možné definovať v súbore .key, následne stačí zmeniť len tento súbor a simuláciu je možné odoslať znova.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0020.jpg' | relative_url }})

Okno na generovanie databázy

**Súvisiace témy:**

[49\. Introduction to Die Stress Study](/docs/en/operation_templates/49_die_stress_study/49_introduction_to_die_stress_study/)

[49.1. 2D Die Stress Study](/docs/en/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/)
