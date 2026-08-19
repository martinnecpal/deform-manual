---
lang: sk
title: "30.2. Nastavenie napätia v 3D čipe"
---

# 30.2. Príručka k 3D napätiu čipu

30.2.1. Ako pridať operáciu „3D napätie v lisovacej forme“

30.2.2. Okno „Objekty“

30.2.3. Typy objektov

30.2.4. Obrobok

30.2.5. Matrice

  * Všeobecné informácie

  * Geometria

  * Sieť objektu

  * Vynútená interpolácia

  * Materiál predmetu

  * Okrajové podmienky objektu

  * Tepelné zúženie

  * Inicializovať

  * Zápas

30.2.6. Polohovanie

30.2.7. Plánované polohovanie

30.2.8. Vzťahy medzi objektmi

30.2.9. Riadenie simulácie

30.2.10. Vytvorenie databázy

## Ako pridať 3D operáciu „Die stress“

Po dokončení operácie 3D tvárnenia je možné v sprievodcovi MO na karte Explorer pridať operáciu „Die stress 3D“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky „Die Stress 3D“ na karte Explorer, alebo môžeme operáciu „Die stress“ pridať ako naplánovanú operáciu spolu s nastavením operácie tvárnenia, Používateľ môže operáciu pridať aj pretiahnutím a umiestnením do editora operácií, ako je znázornené na obr. 30.2.1. Ak je operácia „Die stress“ nastavená ako naplánovaná, v čase nastavenia nie je možné vygenerovať databázu (DB); tá sa vygeneruje automaticky po dokončení operácie tvárnenia a vykonaní analýzy napätia v lisovacej forme. Ak je operácia „Die stress“ naplánovaná pred dokončením simulácie tvárnenia, musí používateľ definovať naplánované polohovanie pohyblivých lisovacích foriem, aby sa určila presná poloha pre interpoláciu síl.

  
![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image001.jpg' | relative_url }})

Pridanie 3D operácie „Die stress“ do editora operácií

## Okno „Objekty“

  
Používateľ môže pridať požadovaný počet ďalších objektov pre simuláciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Obr. 30.2.2. znázorňuje tri objekty, ktoré prešli z predchádzajúcej operácie tvárnenia do operácie namáhania lisovacej formy. Používateľ môže na základe nastavenia pridať potrebné upínacie prvky a ďalšie komponenty. 

![]({{ '/assets/images/operation_templates/30_die_stress/30_1_2d_die_stress_setup/image002.jpg' | relative_url }})

Okno „Objekty“

## Typy objektov

**Obrobok:** Obrobok je typ plastového objektu, ktorý sa považuje za načítaný z databázy, keďže údaje o ňom sa čítajú z predchádzajúcej operácie. Používateľ môže tiež importovať objekt pomocou možnosti „Importovať objekt“, ktorá je k dispozícii na stránke „Všeobecné nastavenia objektu“ pre nové objekty pridané v tejto operácii.

**Poznámka**: Používateľ má možnosť importovať objekty aj pre obrobky, ktoré sa v skutočnosti načítajú z databázy; preto sa používateľovi odporúča, aby neobrovoval objekty pre tento typ obrobku, keďže tieto budú pri generovaní databázy odstránené a nebudú zohľadnené pri analýze.

  
**Formy**: Objekty definované ako formy sa budú považovať za pružné objekty. Tieto objekty budú pokryté sieťou a sily sa interpolujú z obrobku.

  
**Fixture**: Objekty definované ako „fixtures“ sa budú považovať za tuhé a pre tieto objekty nie je potrebná žiadna sieť, pokiaľ sa nemajú vykonávať výpočty prenosu tepla.

## **Obrobok**

Keďže obrobok nepotrebujeme na analýzu napätia v lisovacej forme, bude počas generovania DB odstránený, a tento objekt sa v režime postprocesora nezobrazí. Používateľ môže obrobok vynechať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (pozri obr. 30.2.3.). 

![]({{ '/assets/images/operation_templates/30_die_stress/30_1_2d_die_stress_setup/image003.jpg' | relative_url }})

Okno obrobku

## Matrice

**Všeobecné informácie**

V tomto okne môže používateľ nastaviť teplotu objektu a vybrať typ objektu, ako je znázornené na obr. 30.2.4. V prípade foriem je ako predvolený typ objektu nastavený typ „Elastic“.

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image002.jpg' | relative_url }})

Okienko hornej matrice

  
**Geometria**

Používateľ môže definovať novú geometriu pomocou možností v okne geometrie. Režim s návodom ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) ponúka základné možnosti na definovanie geometrie (pozri obr. 30.2.5.). Ak používateľ potrebuje ďalšie pokročilé možnosti, musí prejsť do expertného režimu kliknutím na ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}). Odborný režim ponúka rôzne možnosti, ako napríklad konverziu 2D na 3D, vyhľadanie osí, nastavenie mriežky blokov, symetrické roviny a kontrolu (pozri obr. 30.2.6.). Geometriu je možné importovať aj pomocou možnosti Importovať geometriu zo súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) alebo pomocou možnosti Importovať z knižnice. Používateľ môže tiež importovať geometrie v iných formátoch, ako sú .key, .DB, .STL, .PDA, .NAS a .UNV. Na jednoduché definovanie základných geometrických tvarov sú k dispozícii primitívy. Ďalšie informácie o vytváraní a úprave 3D geometrií nájdete v časti [12\. 3. 3D Geometry Data Defining.](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/)

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image003.jpg' | relative_url }})

Okno „Geometria“ v režime s návodom

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image004.jpg' | relative_url }})

Okno Geometria v režime Expert

  
**Sieť objektu**

Stránka „Mesh“ ponúka možnosti vytvorenia siete pre objekt. Režim „Guided ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }})“ umožňuje nastaviť počet prvkov pomocou posuvníka na vytvorenie siete. Ak je geometria objektu zložitá alebo ak chce používateľ ovládať hustotu siete na celom objekte, musí prejsť do expertného režimu kliknutím na ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}). Odborný režim ponúka rôzne možnosti, ako sú váhové faktory, okná siete a režim definovaný používateľom, ktoré slúžia na riadenie hustoty siete. Možnosti vytvárania siete dostupné v odbornom režime a v režime „Guided“ sú znázornené na obr. 30.2.7 a obr. 30.2.8. Podrobnejší popis týchto možností nájdete v časti [13.2. 3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/).

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image005.jpg' | relative_url }})

Okno „Mesh“ v režime s navádzaním

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image006.jpg' | relative_url }})

Okno „Mesh“ v expertnom režime

  
**Vynútená interpolácia**

Na interpoláciu sily zo surového materiálu (referenčného objektu) na lisovacie formy musí používateľ zaškrtnúť políčko „Interpolovať silu“ a zadať hodnotu tolerancie chyby. Tieto interpolované sily zvyčajne nebudú presne rovnaké. Tolerancia chyby to do určitej miery reguluje. Zadanie vyššej tolerancie spôsobí interpoláciu síl z väčšieho počtu povrchových uzlov polotovaru, čím sa zvýšia sily interpolované na lisovacie formy. Pokiaľ sú sily pre polotovar a lisovaciu formu pomerne blízke, interpolácia sa považuje za úspešnú. V interaktívnom režime vyberte ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}), v dávkovom režime zaškrtnite políčko Interpolovať, aby sa interpolácia síl na lisovacie formy naplánovala automaticky pred generovaním databázy (pozri obr. 30.2.9.). Interpolované sily sú zobrazené na obr. 30.2.10.

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image007.jpg' | relative_url }})

Vynútiť okno interpolácie

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image009.jpg' | relative_url }})

Interpolované sily

**Materiál objektu**

V okne „Materiál“ sa zobrazia všetky materiály zdedené z predchádzajúcej operácie (pozri obr. 30.2.11.), pričom používateľ môže materiál potrebný pre túto operáciu načítať do okna „Materiál objektu“ pomocou možnosti „Importovať údaje o materiáli zo súboru“ (![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})) alebo pomocou možnosti „Načítať z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})).

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image008.jpg' | relative_url }})

Okno s materiálmi

**Okrajové podmienky objektu**

Keď interpolujeme sily pôsobiace na polotovar, tieto sily pôsobia na lisovacie formy, čo spôsobuje ich nepravidelný posun počas simulácie. Aby sa zabránilo nepravidelnému posunu lisovacích foriem, je potrebné priradiť vhodné okrajové podmienky. Na zastavenie posunu lisovacích foriem možno použiť okrajovú podmienku rýchlosti (pozri obr. 30.2.12.). Priradenie okrajových podmienok rýchlosti na horný okraj matrice je znázornené na obr. 30.2.13.

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image010.jpg' | relative_url }})

Okno s okrajovými podmienkami

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image011.jpg' | relative_url }})

Okrajové podmienky rýchlosti priradené v smere Z

**Tepelné sťahovanie**

3D model BCC s tepelne zmrštiteľným uložením, ktorý sa používa na analýzu napätia v matrici; podmienky tepelne zmrštiteľného uloženia sú definované medzi vložkou matrice a zmrštiteľným krúžkom. To je možné definovať nasledujúcimi krokmi:

**V prípade valcovej metódy,**

  * Zadanie hodnoty rušenia.

  * Výber smeru (smer kolmý na vnútornú plochu zmršťovacieho krúžku alebo vonkajšiu plochu vložky matrice)

  * Výber vnútornej plochy zmršťovacieho krúžku alebo vonkajšej plochy vložky matrice (plochy, ktorá prichádza do styku s matricou)

**V prípade metódy „kolmo na povrch“,**

Používateľ musí zadať hodnotu interferencie; Deform automaticky vyberie smer kolmý na povrch.

  * Zadanie hodnoty rušenia.

  * Výber vnútornej plochy zmršťovacieho krúžku alebo vonkajšej plochy vložky matrice (plochy, ktorá prichádza do styku s matricou)

Ak sa zúženie uplatňuje na vnútorný objekt, hodnota by mala byť záporná, a ak sa zúženie uplatňuje na vonkajší objekt, hodnota by mala byť kladná.  
Ďalšie informácie o montáži s tepelne zmrštiteľným obalom nájdete v dokumente [3D Die Stress Analysis](/docs/en/operation_templates/30_die_stress/3d_die_stress_analysis_theory/).   
Na obr. 30.2.14 a obr. 30.2.15 je znázornené tesné uloženie pomocou zmršťovacieho krúžku.

  
![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image012.jpg' | relative_url }})

Okno BCC s termoplastickým upevnením

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image013.jpg' | relative_url }})

Priradené okrajové podmienky pre zúženie

**Inicializovať**

V okne „Initialize“ sú na inicializáciu k dispozícii niektoré bežne používané stavové premenné, ako napríklad teplota, deformácia, napätie, poškodenie, rýchlosť, posun atď.

  
Používateľ môže inicializovať hodnoty týchto stavových premenných kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). Obr. 30.2.16 znázorňuje rôzne stavové premenné, ktoré sú k dispozícii v okne „Initialize“. V závislosti od typu stavovej premennej ich môže používateľ inicializovať aj z dátových okien „Node“ a „Element“. Ďalšie informácie o tom, ako inicializovať stavové premenné v oknách „Node“ a „Element“, nájdete v [17.1. Node Data Window](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) a [17.2. Element Data Window](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/).

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image014.jpg' | relative_url }})

Inicializovať okno

  
**Zápasy**

V tejto operácii je možné definovať upínacie prípravky, ktoré držia formy. Upínacie prípravky sa v tejto operácii považujú za tuhé objekty. Definícia a úprava geometrie týchto objektov je podobná ako v prípade foriem. Ak sú zapnuté tepelné výpočty, je potrebné pre tieto objekty definovať sieť, kryštálovú mriežku (BCC) a materiál; tieto premenné je možné definovať podobným spôsobom ako v prípade foriem.

## Polohovanie

Na obr. 30.2.17 je zobrazené okno na umiestňovanie, v ktorom môže používateľ umiestňovať upínacie prvky a objekty lisovacej formy pridané pomocou tlačidla „Umiestniť objekty“. Na umiestnenie objektov sú k dispozícii rôzne možnosti, ako je znázornené na obr. 30.2.18.  
Ďalšie informácie o týchto možnostiach nájdete v dokumente [19\. Object Positioning.](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

![]({{ '/assets/images/operation_templates/30_die_stress/30_1_2d_die_stress_setup/image017.jpg' | relative_url }})

Okno na nastavenie polohy

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image015.jpg' | relative_url }})

Okno na umiestňovanie objektov

## Plánované polohovanie

Ak si používateľ nie je istý polohou objektu – ako je to v prípade objektov typu „Read From DB“ – a operácia analýzy napätia je pridaná v dávkovom režime, naplánované polohovanie pomôže objekty presne umiestniť.

Funkcia „Schedule positioning“ umožňuje používateľovi definovať umiestnenie objektov v nastaveniach MO pre nasledujúce operácie, pre ktoré sa nevytvára databáza (DB), tak, aby boli objekty umiestnené ešte pred vytvorením databázy počas spustenia simulácie v dávkovom režime (pozri obr. 30.2.19.)

![]({{ '/assets/images/operation_templates/30_die_stress/30_1_2d_die_stress_setup/image019.jpg' | relative_url }})

Plánované časové okno na umiestnenie

## Vzťahy medzi objektmi

  
Účelom vzťahov medzi objektmi je definovať, ako rôzne objekty v simulácii vzájomne interagujú.

  
V okne „Kontakt“ budú obe možnosti režimu – „Guided ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }})“ aj „Expert ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})“ – v aktívnom režime; v režime „Guided“ sú všetky možné vzťahy už uvedené v zozname (pozri obr. 30.2.20.). Používateľ musí pre objekty, ktoré sú v kontakte, definovať typ vzťahu a hodnotu trenia pre vybraný vzťah. Pri nastavovaní analýzy napätia v lisovacej forme v dávkovom režime môže používateľ naplánovať generovanie kontaktov pomocou možností režimu Expert ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}).

  
V režime Expert tabuľka vzťahov zobrazuje aktuálne vzťahy medzi objektmi, ktoré boli definované tak, ako je znázornené na obr. 30.2.21. Všetky objekty, ktoré môžu prísť do kontaktu v priebehu simulácie, musia mať definovaný kontaktný vzťah.

**Systém**: Po výbere tohto prepínača systém priradí predvolené vzťahy medzi objektmi. V prípade potreby môže používateľ pridať mazivá výberom možnosti „Pridať nové“ z roletového menu a kliknutím na tlačidlo „Upraviť“, alebo môže na účely simulácie načítať požadované mazivá z knižnice.

**Používateľ**: V predvolenom nastavení bude zaškrtnuté políčko „Používateľ“. Používateľ môže pridať vzťahy kliknutím na tlačidlo.

  
![]({{ '/assets/images/operation_templates/30_die_stress/30_1_2d_die_stress_setup/image020.jpg' | relative_url }})

Okno medzi objektmi v režime s navádzaním

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image016.jpg' | relative_url }})

Okno medzi objektmi v režime Expert

## Riadenie simulácie

**Počet simulačných krokov**

Ak sa analýza napätí vykonáva len na jednom nástroji, na získanie presných hodnôt napätí stačí jednokroková simulácia. Ak sa analýza napätí vykonáva na zostavách foriem, kde dochádza k interakcii medzi nástrojmi, zvyčajne je potrebných viac ako jeden krok, aby sa sústava foriem dostala do rovnovážneho stavu pri pôsobiacom zaťažení.

Používateľ môže aktivovať tepelný výpočet tak, že v expertnom režime zapne režim prenosu tepla a v nastaveniach BCC objektu definuje príslušné tepelné BCC a v okne medzi objektmi nastaví hodnoty koeficientov prenosu tepla.  
****

**Krok pri ukladaní**

Hodnota krokového prírastku (STPINC), ktorá sa má uložiť do databázy, určuje počet krokov, ktoré systém uloží do databázy. Pri spustení simulácie sa musí vypočítať každý krok, ale nemusí sa nutne uložiť do databázy. Keďže počet krokov, ktoré sa vykonajú pri analýze napätia v čipe, je nižší, používateľ môže uložiť každý krok.

**Ovládanie krokového posunu**

Veľkosť kroku riešenia je riadená časovým krokom. Maximálny čas trvania procesu na jeden krok možno pre operácie analýzy napätia v matrici nastaviť na 1 sekundu.  
Na obr. 30.2.22 sú zobrazené ovládacie prvky simulácie v režime s navádzaním.  
Na obr. 30.2.23 sú zobrazené ovládacie prvky simulácie v režime Expert.

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image017.jpg' | relative_url }})

Riadenie simulácie v režime „Guided“

![]({{ '/assets/images/operation_templates/30_die_stress/30_2_3d_die_stress_setup/image018.jpg' | relative_url }})

Ovládanie simulácie v režime Expert

Ďalšie informácie a popis možností v časti „Ovládacie prvky simulácie“ nájdete v [9\. Simulation Controls.](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/).

## Vytvoriť databázu

****

**Skontrolujte údaje ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})**  
Systém skontroluje údaje. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvoriť databázu ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})**

****

Kliknutím na toto tlačidlo sa vygeneruje databáza potrebná na nastavenie. (Pozri obr. 30.2.24.)

  
**Pridať súbor s kľúčmi**

Akékoľvek informácie, ktoré nie sú definované v sprievodcovi, ale napriek tomu sa vzťahujú na daný proces, je možné načítať ako súbor s príponou .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt – tieto hodnoty je možné definovať v súbore s príponou .key, následne stačí zmeniť len tento súbor a simuláciu je možné odoslať znovu.

![]({{ '/assets/images/operation_templates/30_die_stress/30_1_2d_die_stress_setup/image024.jpg' | relative_url }})

Okno na generovanie databázy

**Súvisiace témy:**

[6.1. Integrated Manufacturing Process Pre- Processor Layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

[6.2. Integrated Manufacturing Process.Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Process Post - Processor layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[Die stress study labs](/docs/en/labs/die_stess_study_labs/die_stess_labs_across_single_steps_main_pg/)

[30\. Introduction to Die Stress](/docs/en/operation_templates/30_die_stress/30_introduction_to_die_stress/)

[30.1. 2D Die stress setup](/docs/en/operation_templates/30_die_stress/30_1_2d_die_stress_setup/)
