---
lang: sk
title: "37.2. Sprievodca 3D tepelným spracovaním"
---

# 37.2. Sprievodca 3D tepelným spracovaním

37.2.1. Ako pridať operáciu 3D tepelného spracovania

37.2.2. Výber procesu

37.2.3. Inicializácia

37.2.4. Výber materiálu

37.2.5. Objekty

  * Obrobok / Objekt – všeobecné informácie

  * Geometria objektu

  * Sieť objektu

  * Materiál predmetu

  * Okrajová podmienka objektu

  * Vlastnosti objektu

  * Inicializovať

37.2.6. Podrobnosti o médiu

37.2.7. Harmonogram

37.2.8. Ovládacie prvky

37.2.9. Ovládacie prvky na zastavenie

37.2.10. Ovládacie prvky simulácie

37.2.11. Databáza generácií

## Ako pridať operáciu 3D tepelného spracovania

Operáciu tepelného spracovania je možné nastaviť v prostredí MO, do ktorého sa dostanete z hlavného okna grafického rozhrania. Novú úlohu vytvoríte buď výberom položky Súbor ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Nová úloha, alebo kliknutím na ikonu Nová úloha ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Vyberte možnosť „Integrated Manufacturing Process“ a systém jednotiek. Otvorí sa okno MO s vyskakovacím oknom „New Project“. V tomto okne definujte názov projektu, titul a systém jednotiek (štandardne sa vyberie systém jednotiek zvolený v ponuke „File“). Tiež môžeme pridať operáciu 3D HT Wizard výberom z roletového zoznamu Prvá operácia a zaškrtnutím políčka na pridanie operácie ako Operácia 1 do nového projektu (ako je znázornené na obr. 37.2.1.). Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) v okne „Nový projekt“; otvorí sa sprievodca MO a v editore operácií uvidíte, že do editora operácií bol pridaný sprievodca 3D tepelného spracovania (ako je znázornené na obr. 37.2.2.). Pomocou možnosti „Kopírovať existujúci projekt“ môžete importovať predtým uložené projekty ako nový projekt. 

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image001.jpg' | relative_url }})

V okne „Nový projekt“ zadajte názov projektu a vyberte prvú operáciu

  
Operáciu 3D HT Wizard môžeme pridať aj z karty „Explorer“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie 3D HT Wizard (ako je znázornené na obr. 37.2.2.) alebo presunutím operácie 3D HT Wizard do okna editora operácií metódou drag and drop. Štandardne sa v oblasti úpravy nastavení vlastností otvorí stránka výberu procesu.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image002.jpg' | relative_url }})

Pridanie operácie zo zoznamu operácií v Průzkumníku

## Výber procesu

Na stránke „Process“ môže používateľ vybrať režim simulácie: fázovú transformáciu, difúziu, deformáciu alebo ich kombináciu. Ak má používateľ záujem iba o simuláciu fázových transformácií počas tepelného spracovania, môže zapnúť len fázovú transformáciu; ak však chce simulovať vplyv zmien spôsobených fázovou transformáciou na geometriu, mal by zapnúť ako fázovú transformáciu, tak aj deformáciu. Ak chce používateľ simulovať iba proces difúzie uhlíka, môže zapnúť iba difúziu, avšak ak chce simulovať vplyv difúzie na geometriu, mal by zapnúť difúziu aj deformáciu.

  
Na tejto stránke môže používateľ nastaviť parametre trvania kroku (pozri obr. 37.2.3.). Definícia kroku môže byť buď v režime „User“ (Používateľ), alebo „Auto“ (Automaticky). Ak je definícia kroku nastavená na režim „User“, používateľ musí určiť čas na jeden krok spolu s krokom prírastku, aby sa krok zapísal do databázy.

  
Ak je definícia kroku nastavená na režim „Auto“, musí používateľ uviesť maximálnu povolenú zmenu teploty na jeden krok spolu s minimálnou a maximálnou dĺžkou trvania procesu na jeden krok, ako aj veľkosť kroku, aby sa daný krok mohol zapísať do databázy.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image003.jpg' | relative_url }})

Stránka procesu

## Inicializácia

Na stránke „Inicializácia“ môže používateľ aktivovať simulačný režim a tiež importovať údaje o prostredí a naplánované údaje zo súboru sprievodcu HT (.HTWZ) zo starších verzií projektu pomocou možnosti „Importovať súbor sprievodcu“ (pozri obr. 37.2.4.).

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image020.jpg' | relative_url }})

Úvodná stránka

## Výber materiálu

Materiály potrebné pre tento proces je možné načítať buď z knižnice pomocou ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), alebo z databázy či súboru kľúčov pomocou ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), ako je znázornené na obr. 37.2.5. Používateľ môže tiež pridať nový materiál a definovať požadované údaje na príslušnej karte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). Ďalšie informácie o definícii údajov o materiáloch nájdete v [Material data](/docs/en/pre_processor/10_material_data/10_material_data/).

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image003.jpg' | relative_url }})

Import materiálu z knižnice

## Objekty

Ak chce používateľ spolu so sochou zahrnúť aj upínacie prípravky a iné objekty, na stránke „Objekty“ pridá počet objektov potrebných pre operáciu tepelného spracovania kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Predvolene sa do operácie pridá jeden objekt, ako je znázornené na obr. 37.2.6.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image006.jpg' | relative_url }})

Okno „Objekty“

### Všeobecné informácie o obrobku/predmete

Na stránke „Všeobecné nastavenia objektu“ (pozri obr. 37.2.7.) môže používateľ vybrať typ objektu kliknutím na príslušné začiarkavacie políčko. Ďalšie informácie o typoch objektov nájdete v príslušnej časti. Predvolený typ objektu pre obrobok je nastavený na „Plast“. Používateľ môže nastaviť počiatočnú teplotu objektu zadaním hodnoty do poľa „Teplota objektu“. Používateľ môže tiež importovať objekt z iných databáz alebo súborov kľúčov pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a vyhľadaním príslušného súboru.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image004.jpg' | relative_url }})

Stránka „Všeobecné informácie o objekte“

### Geometria objektu

Používateľ môže definovať jednoduché geometrie pomocou základných možností; geometrie je možné tiež importovať pomocou možnosti „Importovať geometriu zo súboru“ (![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})) alebo z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (pozri obr. 37.2.8.). Ďalšie informácie o rôznych možnostiach na stránke geometrie nájdete v časti [12.3. 3D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/).

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image005.jpg' | relative_url }})

Stránka „Geometria objektu“

### Sieť objektu

Na stránke „Mesh“ budú obe možnosti režimu – „Guided ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }})“ aj „Expert ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})“ – v aktívnom režime; v režime „Guided“ stačí na vytvorenie siete definovať iba počet prvkov. V režime „Guided“ môže používateľ zmeniť počet prvkov siete a vygenerovať sieť s ostatnými predvolenými nastaveniami, ako je znázornené na obr. 37.2.9. Ďalšie možnosti na ovládanie hustoty siete sú k dispozícii po prepnutí do režimu „Expert“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}). Možnosti siete v režime Expert sú znázornené na obr. 37.2.10. Podrobný popis týchto nastavení siete v režime Expert nájdete v časti [13.2. 3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/).

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image006.jpg' | relative_url }})

Režim s navádzaním – možnosť „Mesh“

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image007.jpg' | relative_url }})

Možnosť vytvorenia siete v expertnom režime

### Materiál objektu

Na stránke materiálov sa zobrazujú všetky materiály pridané do zoznamu materiálov (ako je znázornené na obr. 37.2.11.) a používateľ si môže zo zoznamu materiálov vybrať požadovaný materiál a priradiť ho k príslušnému objektu. Užívateľ môže materiál na stránke Materiál objektu načítať aj pomocou funkcie Importovať údaje o materiáli zo súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) alebo pomocou možnosti Načítať z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). 

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image008.jpg' | relative_url }})

Okno výberu materiálu

### Okrajová podmienka objektu

Systém automaticky priradí tepelné a difúzne BCC v závislosti od zvoleného procesu a podmienok symetrie na základe typu geometrie. Používateľ si môže tieto BCC skontrolovať a môže tiež priradiť požadované BCC v závislosti od procesu (pozri obr. 37.2.12).

Možnosť ![]({{ '/assets/icons/pre_icons/mo_auto_velocity_bcc_button.jpg' | relative_url }}) umožňuje používateľovi automaticky priradiť rýchlosť BCC na základe geometrie, aby sa obrobok počas simulácie nepohyboval nepredvídateľne (pozri obr. 37.2.13.).

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image009.jpg' | relative_url }})

Priradená symetria BCC

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image010.jpg' | relative_url }})

Používateľom priradené BCC typu „Velocity“

### Vlastnosť objektu

V okne „Vlastnosti objektu“ sa zadávajú rôzne parametre objektu, ktoré ovplyvňujú buď termomechanické správanie objektu, alebo správanie numerického riešenia. (Pozri obr. 37.2.14.) Ďalšie informácie nájdete v [16\. Object properties](/docs/en/pre_processor/16_object_properties/16_object_properties/).

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image011.jpg' | relative_url }})

Okno vlastností objektu

### Inicializácia

Na stránke „Initialize“ má používateľ k dispozícii možnosti na inicializáciu hodnôt teploty, deformácie, napätia, poškodenia, rýchlosti, posunutia, veľkosti zŕn, objemového podielu rekryštalizácie a hustoty (pozri obr. 37.2.15.).

  
Používateľ môže pre objekt tiež definovať hodnotu priemernej rýchlosti deformácie a limitnej rýchlosti deformácie. Ak ide o plastický objekt, limitná rýchlosť deformácie určuje limitnú hodnotu efektívnej rýchlosti deformácie, pod ktorou sa plastický materiál považuje za tuhý. Priemerná rýchlosť deformácie je charakteristická priemerná hodnota efektívnej rýchlosti deformácie. Na začiatku simulácie by sa mala zadať aproximácia tejto hodnoty. Program DEFORM automaticky udržiava pomer medzi priemernou rýchlosťou deformácie a limitnou rýchlosťou deformácie. Všeobecne by hodnota limitnej rýchlosti deformácie mala byť 0,01. 

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image012.jpg' | relative_url }})

Načítanie stránky

Ak sa simuluje difúzny proces, používateľ by mal na úrovni uzlov nastaviť počiatočné percentuálne podiely atómov pre difúziu. V prípade tepelného spracovania by mal používateľ inicializovať objemový podiel každej fázy existujúcej na začiatku na úrovni prvku, pričom súčet objemových podielov všetkých fáz by mal byť rovný 1. Hodnoty uzlov sú dostupné kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}) na paneli nástrojov a inicializáciu je možné vykonať pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). Podobne je možné zobraziť hodnoty prvkov kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) na paneli nástrojov a inicializáciu je možné vykonať pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). Možnosti pre uzlové a prvkové údaje sú znázornené na obr. 37.2.16 a obr. 37.2.17.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image013.jpg' | relative_url }})

Okno s uzlovými údajmi

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image014.jpg' | relative_url }})

Okno s údajmi o prvkoch

## Podrobnosti o médiu

Na stránke „Podrobnosti o médiu“ môže používateľ definovať médium a jeho koeficienty prenosu tepla spolu so zónami priradenými k danému médiu (pozri obr. 37.2.18.)

****

**Médiá** – Tu je možné definovať rôzne typy médií používaných v procese tepelného spracovania; pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}) je možné médiá pridať a pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_delete_icon.jpg' | relative_url }}) je možné definované médiá odstrániť. Médiá je možné premenovať pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_rename_button.jpg' | relative_url }}).  
**Zóny** – Zóny sú plochy obrobku, ktoré sú priradené k médiám vybraným na karte „Médiá“; štandardne je jedna zóna definovaná ako „Predvolená“, ktorú nie je možné odstrániť. Každá zóna môže mať priradené rôzne koeficienty prenosu tepla, pričom tieto koeficienty môžu byť konštantné, alebo môžu byť funkciou teploty či času. Na ostatné povrchy, pre ktoré nie je definovaná žiadna zóna, sa uplatňujú podmienky definované pre zónu „Predvolená“. Hodnoty koeficientov prenosu tepla pre každú zónu je možné uložiť pomocou tlačidla a opätovne načítať pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}).

**Žiarenie** – Ak je potrebné pre príslušné médium aktivovať žiarenie, používateľ môže zaškrtnúť políčko „Žiarenie“.

**Koeficient difúznej povrchovej reakcie** \- V prípade potreby je možné tu definovať hodnoty koeficientu difúznej povrchovej reakcie súvisiace s médiom; tieto hodnoty môžu byť konštantné, alebo môžu byť funkciou teploty či percentuálneho podielu atómov.****

**Emisivita –** Ak sa má pre určitú zónu modelovať žiarenie, môže používateľ zaškrtnúť políčko „Žiarenie“ a pre túto zónu definovať hodnotu emisivity. Emisivitu je možné definovať ako konštantu, funkciu teploty alebo funkciu času.**  
**

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image015.jpg' | relative_url }})

Stredná stránka

## Rozvrh

Na stránke s plánom môže používateľ naplánovať procesy žíhania, normalizácie a kalenia tak, že zadá ich trvanie, použitý materiál, teplotu prostredia a obsah atómov, ako je znázornené na obr. 37.2.19.

  * Používateľ môže pridať operáciu pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_button.jpg' | relative_url }}).

  * Používateľ môže vymazať definovanú operáciu pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_delete_button.jpg' | relative_url }}).

  * Používateľ môže pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_delete_all_button.jpg' | relative_url }}) naraz vymazať všetky definované operácie.

  * Používateľ môže pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_insert_button.jpg' | relative_url }}) vložiť operáciu medzi dve operácie.

  * Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_display_button.jpg' | relative_url }}) sa zobrazí graf teplotného priebehu v závislosti od času pre všetky operácie, ako je znázornené na obr. 37.2.21.

  * Používateľ môže tiež nastaviť konkrétne podmienky prostredia pomocou pokročilej možnosti pre každú operáciu samostatne kliknutím na ![]({{ '/assets/icons/pre_icons/mo_define.._button.jpg' | relative_url }}).

  
**Pokročilé nastavenia:**

Používateľ môže definovať teplotu prostredia a obsah atómov v závislosti od času, ako je znázornené na obr. 37.2.20.  
**Používať miestny čas pre funkcie** – Ak používateľ zapne túto možnosť, pri výpočte hodnôt funkcií sa zohľadňuje miestny čas operácie; v opačnom prípade sa štandardne používa globálny čas. Globálny čas predstavuje súčet procesného času všetkých operácií, zatiaľ čo miestny čas začína v okamihu spustenia operácie a končí jej ukončením.  
**Spustiť inkubáciu transformácie** – Používateľ môže spustiť inkubáciu transformácie zaškrtnutím tohto políčka.  
**.KEY používateľa** – používateľ môže v týchto poliach zadať cestu k súboru .KEY, ktorý je možné použiť spolu s existujúcou definíciou.  
**Aktívne transformácie** – Tu sa zobrazujú všetky transformácie definované v súbore materiálu a používateľ môže aktivovať transformácie, ktoré sa majú použiť pri danej operácii, zaškrtnutím políčok vedľa príslušných transformácií.  
Používateľ sa môže vrátiť na stránku s rozvrhom kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_cancel_button.jpg' | relative_url }}) môže opustiť stránku bez uloženia zmien definovaných iba v danej relácii. 

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image016.jpg' | relative_url }})

Stránka s rozvrhom

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image021.jpg' | relative_url }})

Rozvrh – Pokročilé nastavenia

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image017.jpg' | relative_url }})

Graf harmonogramu

## Polohovanie

Používateľ môže objekty umiestniť pomocou tlačidla „Umiestniť objekty“. Na umiestnenie objektov sú k dispozícii rôzne možnosti (pozri obr. 37.2.22.); ďalšie informácie o týchto možnostiach nájdete v [19\. Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/).

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image018.jpg' | relative_url }})

Možnosti umiestnenia objektu

## Ovládacie prvky na zastavenie

Ovládacie prvky tepelného zastavenia umožňujú zastaviť simuláciu pri vopred definovaných podmienkach (pozri obr. 37.2.23.), napríklad pri dosiahnutí zvolenej teploty vo všetkých uzloch, čím je možné odhadnúť dobu ohrevu. Uplatňujú sa na objekt vybraný z roletového zoznamu objektov.

**Spôsob zastavenia:**

  * **Žiadne** : Neaplikuje žiadne opatrenia na obmedzenie prehriatia

  * **Ľubovoľný uzol**: Simulácia sa zastaví, keď ktorýkoľvek uzol v sochore dosiahne zadanú hodnotu.

  * **Všetky uzly**: Simulácia sa zastaví, keď všetky uzly v sochárskej surovine dosiahnu zadanú hodnotu.

  * **Vybraný uzol**: Simulácia sa zastaví, keď zadaný uzol v sochore dosiahne zadanú hodnotu.

  * **Priemer všetkých uzlov**: Simulácia sa zastaví, keď priemerná teplota všetkých uzlov v sochore dosiahne zadanú hodnotu.

  * **Priemerná teplota povrchu + maximálna teplota**: Simulácia sa zastaví, keď priemerná teplota všetkých uzlov na povrchu sochory + maximálna teplota v sochore dosiahne zadanú hodnotu.

**Teplotný rozsah:**

Okrem jednej hodnoty je možné na zastavenie simulácie použiť aj teplotný rozsah.

  * **Zastaviť, ak teplota je mimo rozsahu**: Simulácia sa zastaví, ak hodnota teploty prekročí stanovený rozsah.

  * **Zastaviť, keď je teplota v rozsahu** : Simulácia sa zastaví, keď sa hodnota teploty nachádza v zadanom rozsahu.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image024.jpg' | relative_url }})

Ovládacie prvky na obmedzenie prehriatia

## Ovládacie prvky simulácie

Na stránke „Ovládacie prvky simulácie“ (pozri obr. 37.2.24.) môže používateľ nastaviť typ kroku na „Používateľský“ alebo „Automatický“ výberom príslušného prepínača.

  
**Auto** – Ak používateľ zvolí možnosť „Auto“, systém bude automaticky riadiť hodnotu časového kroku na základe zadaných podmienok. Podmienky používané na riadenie časového kroku sú:

  * **Zmena teploty na jeden krok** – Maximálna povolená zmena teploty na jeden krok; ak táto hodnota prekročí stanovenú hranicu, časový krok sa skráti, a ak je nižšia ako táto hodnota, časový krok sa predĺži.

  * **Minimálna/maximálna dĺžka časového kroku** – Určuje rozsah časového kroku, v rámci ktorého môže systém meniť hodnotu časového kroku. Tu je možné nastaviť minimálnu povolenú hodnotu časového kroku a maximálnu povolenú hodnotu časového kroku.

  * **Počet krokov na uloženie** – Hodnota „počet krokov na uloženie“ (STPINC) určuje počet krokov, ktoré systém uloží do databázy. Pri spustení simulácie sa musí vypočítať každý krok, ale nie je nutné, aby sa všetky kroky uložili do databázy. Uložením väčšieho počtu krokov sa zachová viac informácií o procese, čo však bude vyžadovať viac úložného priestoru.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image025.jpg' | relative_url }})

Ovládacie prvky simulácie

## Databáza generácií

Po úplnom nastavení úlohy je posledným krokom vytvorenie databázového súboru. Modul FEM (časť programu DEFORM®, ktorá vypočítava riešenie) používa databázový súbor na ukladanie riešení úlohy metódou konečných prvkov. Pri generovaní databázy v preprocesore DEFORM MO sa všetky informácie definované v preprocesore (napríklad vlastnosti materiálov, obmedzenia pohybu, geometrie objektov atď.) prenesú do databázového súboru.

Na stránke „Generate DB“ (pozri obr. 37.2.25). Od verzie 12.0.2 je možné zobraziť súhrn nastavení simulácie prevádzky. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) spustíte kontrolu programu, či v nastavení úlohy niečo nechýba. Počas kontroly červené správy označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch). 

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

**Pridať súbor s kľúčom**

Akékoľvek informácie, ktoré nie sú definované v sprievodcovi, ale napriek tomu sa vzťahujú na daný proces, je možné načítať ako súbor s príponou .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt – tieto hodnoty je možné definovať v súbore s príponou .key, následne stačí zmeniť len tento súbor a simuláciu je možné odoslať znovu.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_2_3d_heat_treatment_wizard/image019.jpg' | relative_url }})

Vytvoriť databázu

**Súvisiace témy:**

[6.1. Integrated Manufacturing Process Pre- Processor Layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

[6.2. Integrated Manufacturing Process.Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Proces Post - Processor layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[3D Heat Treatment wizard Lab](/docs/en/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/)
