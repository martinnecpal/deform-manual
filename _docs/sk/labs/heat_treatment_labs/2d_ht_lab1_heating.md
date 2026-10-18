---
lang: sk
title: "2D HT Laboratórium 1 – Kúrenie"
---

# 2D HT Lab1: Modelovanie procesu ohrevu s fázovou premenou

  
1.1. Vytvorenie nového problému

1.2. Otvorte operáciu a vyberte geometriu

1.3. Načítanie vlastností materiálu

1.4. Pridávanie objektov

1.5. Vytvorenie objektu 1

1.6. Vytvorenie objektu 2

1.7. Definícia vzťahov medzi objektmi

1.8. Nastavenie ovládacích prvkov simulácie

1.9. Vytvorenie databázy

1.10. Spustenie simulácie

1.11. Následné spracovanie výsledkov

1.12. Ukončenie sprievodcu MO

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené nižšie (obr. 2DHTML1.1.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno programu DEFORM GUI

Vytvorte nový problém buď výberom položky **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem**, alebo kliknutím na ikonu New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Problem Setup, ako je znázornené na obr. 2DHTML1.2. Zvoľte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**SI**“ pomocou prepínača. Zadajte názov úlohy ako „**Gear_Blank**“ a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoríte novú úlohu s použitím integrovaného výrobného procesu.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image014.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa sprievodca MO spolu s oknom na zadanie názvu projektu; predvolený názov problému sa aktualizuje na „**Gear_Blank**“ ako názov projektu a aktualizuje sa aj zvolený systém jednotiek. Vyberte **Prvú****operáciu** ako **[2D]** **Tvarovanie**, ako je znázornené na obr. 2DHTML1.3, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste pridali projekt.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0003.jpg' | relative_url }})

Sprievodca MO – Nový projekt

## Otvoriť operáciu a vybrať typ geometrie

Keďže sme pri pridávaní projektu vybrali prvú operáciu, táto sa otvorí automaticky. V tomto cvičení používame geometrie s rovinným deformovaním, preto na stránke typu geometrie vyberte voľbu **2D Plane strain**, ako je znázornené na obr. 2DHTML1.4., a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). 

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0004.jpg' | relative_url }})

Do editora operácií bola pridaná operácia 2D tvárnenia a typ geometrie s rovinným deformovaním

V režime riadenia simulácie na karte „Sim Mode“ zapnite možnosti **Deformácia**, **Prenos tepla** a **Transformácia**, ako je znázornené na obr. 2DHTML1.5. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0005.jpg' | relative_url }})

Ovládacie prvky simulácie v režime s návodom

## Načítanie vlastností materiálu

V okne „Zoznam materiálov“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), aby ste načítali údaje o materiáloch z knižnice, vyberte kategóriu **Oceľ** a načítate materiál „J**IS-S45C (tepelné spracovanie)**“. Tento materiál je zmesový materiál s tromi zložkami (fázami): austenit, perlit a martenzit. Tieto zložky sa kombinujú na určenie vlastností zmesového materiálu pomocou pravidla váženého priemeru zmesi na základe objemových podielov jednotlivých zložiek. Preto sú pre každú fázu definované údaje o pružnosti, plasticite a tepelných vlastnostiach. Aby používatelia lepšie pochopili požiadavky na údaje o materiáloch, odporúčame im preveriť aspoň údaje o tečivom napätí, Youngovom module a tepelnej vodivosti každej fázy. (Pozri obr. 2DHTML1.6.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0006.jpg' | relative_url }})

Okno definície materiálu

Vzťahy medzi týmito fázami sa definujú v dialógovom okne „Fázová transformácia“, ktoré otvoríte kliknutím na tlačidlo „Transformácia“. Pre každý vzťah existuje kinetický model na určenie rýchlosti fázovej transformácie. Medzi súvisiace vlastnosti patria latentné teplo, zmena objemu atď. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Objekt“.

## Pridávanie objektov

Teraz sa do zoznamu objektov štandardne pridajú 3 objekty. Odstráňte teda posledné objekty kliknutím na tlačidlo na odstránenie objektu ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) – ide o dva objekty v zozname s názvami „Workpiece“ a „Top die“, ako je znázornené na obr. 2DHTML1.7. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Workpiece“.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0007.jpg' | relative_url }})

Pridávanie objektov

## Vytvorenie objektu 1

Po otvorení stránky **Obrobok** zmeňte názov objektu na **Ozubené koleso** a ako typ objektu vyberte **Elastoplastický**, ako je znázornené na obr. 2DHTML1.8. Nastavte teplotu objektu na 20 °C. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0008.jpg' | relative_url }})

Definícia objektu obrobku

### Import geometrie

Na stránke „Geometria“ kliknite na možnosť „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **TOOTH.IGS** z adresára **\2d\LABS** v inštalačnej zložke programu DEFORM, ako je znázornené na obr. 2DHTML1.9. Použite akciu ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) na overenie správnosti geometrie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na stránku „Mesh“ (Sieť).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0009.jpg' | relative_url }})

Import súboru s geometriou

### Vytvorenie siete objektu

Prepnite do režimu Expert kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Prepnúť do režimu Expert) na paneli nástrojov. Režim Expert ponúka viac možností pre podrobné nastavenia.

Na stránke „Mesh“ vyberte kartu „Weighing factors“ a nastavte **váhový faktor** pre zakrivenie hranice na hodnotu **1,0**, pričom ostatné váhové faktory ponechajte nezmenené, ako je znázornené na obr. 2DHTML1.10.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0010.jpg' | relative_url }})

Okno „Váha faktora“

Vyberte kartu **Všeobecné**, nastavte **Cieľový počet prvkov** na **500**, nastavte počet **prvkov hrúbky** na **4** a **pomer veľkostí** medzi prvkami na **3**. Po zmene týchto nastavení kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s materiálmi objektu.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0011.jpg' | relative_url }})

Definovanie a generovanie siete

Opäť vidíme materiál objektu a kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_edit_material_button.jpg' | relative_url }}) môžeme upravovať vlastnosti materiálu. Vyberte materiál zo zoznamu, aby ste ho pridali k objektu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Okrajové podmienky“.

### Priradenie okrajových podmienok

Zvoľte okrajovú podmienku rýchlosti **Vy=0** na spodnej ploche ozubeného kolesa, ako je znázornené na obr. 2DHTML1.12.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0012.jpg' | relative_url }})

Prerez zubom ozubeného kolesa s okrajovými podmienkami s nulovou zvislou rýchlosťou

Nastavte tepelné okrajové podmienky na „Výmena tepla s okolím“ pre vonkajšiu časť zuba a vnútornú časť (vrt), ako je znázornené na obr. 2DHTML1.13.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0013.jpg' | relative_url }})

Prerez ozubeného kolesa s výmenou tepla BCC

Kliknite na tlačidlo **Objekt****uzly**![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}); otvorí sa okno s údajmi o uzloch. V tomto dialógovom okne kliknite na kartu **Tepelné** a skontrolujte, či je teplota nastavená na 20 °C. Okrem toho kliknite na kartu **Diffusion** a inicializujte ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) **Atom****Percentage** všetkých uzlov na hodnotu **0,14**, ako je znázornené na obr. 2DHTML1.14. Kliknite na tlačidlo **Zobraziť premennú** ![]({{ '/assets/icons/pre_icons/mo_plot_icon.jpg' | relative_url }}), aby ste potvrdili stavové premenné, ktoré ste práve inicializovali. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte dialógové okno.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0014.jpg' | relative_url }})

Definícia údajov o percentuálnom podiele difúznych atómov v okne „Údaje o uzle“

Kliknite na ikonu **Object****Element![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }})**. Otvorí sa dialógové okno s údajmi o prvku. V tomto dialógovom okne kliknite na položku **Mikrostruktúra**, potom vyberte kartu **Fázová transformácia** a nastavte **Curr. objemový podiel** **perlitu** na hodnotu **1,0** pre všetky prvky, ako je znázornené na obr. 2DHTML1.15. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte dialógové okno.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0015.jpg' | relative_url }})

Definícia údajov o fázovej transformácii v okne „Údaje prvku“

**Poznámka**: Súčet všetkých objemových podielov fáz musí byť pre každý prvok rovný jednici. V opačnom prípade dialógové okno neprijme zadané hodnoty.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top Die“.

## Vytvorenie objektu 2

Keď otvoríte stránku „Top Die“, premenujte tento objekt na **Plane** a uistite sa, že typ objektu je **Rigid**. (Pozri obr. 2DHTML1.16.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0016.jpg' | relative_url }})

Okienko „Top Die“

### Import geometrie

Na stránke „Geometria“ kliknite na možnosť „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **PLANE.IGS** z adresára **\2d\LABS** v inštalačnom priečinku programu DEFORM, ako je znázornené na obr. 2DHTML1.17. Použite akciu ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že geometria je správna.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0017.jpg' | relative_url }})

Import geometrie

Účelom tohto objektu je slúžiť ako rovina symetrie, ktorú nesmie žiadny materiál prekročiť. Kľúčom k tomu, aby táto rovina fungovala ako skutočná rovina symetrie, je nastaviť prenos tepla na rozhraní na nulu, trenie na nulu a medzi oboma objektmi nastaviť kritérium „bez oddelenia“. Tieto parametre budú stanovené neskôr.

Keďže sú objekty prednastavené, klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka „Kontakt“.

## Vzťahy medzi objektmi

Vyberte typ kontaktu **Používateľ** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Nastavte vzťah podriadený/nadriadený medzi **Lietadlom** a **Prevodovkou**, ako je znázornené na obr. 2DHTML1.18.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0018.jpg' | relative_url }})

Okno medzi objektmi

Vyberte vzťah **Rovina** a **Ozubené koleso** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) upravte podmienky kontaktu. Na karte **Kontakt** nastavte kritérium oddelenia na **Absolútny****tlak** a nastavte hodnotu na **1e+07**, ako je znázornené na obr. 2DHTML1.19. Tým sa zabráni strate kontaktu zuba ozubeného kolesa so symetrickou rovinou. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno Definícia údajov medzi objektmi. 

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0019.jpg' | relative_url }})

Okno na definovanie údajov o deformácii medzi objektmi

Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určte vhodnú toleranciu kontaktu (vypočíta sa hodnota približne 0,00126"), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktu.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Step“.

## Nastavenie ovládacích prvkov simulácie

Vyberte kartu ![]({{ '/assets/icons/pre_icons/mo_main_setting.jpg' | relative_url }}) **Hlavná** a zmeňte **Názov operácie** na **Kúrenie**, ako je znázornené na obr. 2DHTML1.20.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0020.jpg' | relative_url }})

Ovládacie prvky simulácie – hlavná záložka v expertnom režime

Vyberte kartu **Simulačné kroky** ![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }}) a zadajte **počet simulačných krokov** na hodnotu **10 000**. **Interval ukladania** nastavte na každých **10** krokov, ako je znázornené na obr. 2DHTML1.21.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0021.jpg' | relative_url }})

Definovanie krokov simulácie

Na karte **Krok** ![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}) vyberte možnosť **Krok** a v časti Definícia kroku nastavte hodnotu **Teplota** na Konštantná. Zadajte počiatočný/minimálny časový krok na 0,1 sekundy na krok a maximálnu zmenu teploty na krok nastavte na 5 °C. Maximálny časový krok pre zmenu teploty nastavte na 20 sekúnd na krok. (pozri obr. 2DHTML1.22.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0022.jpg' | relative_url }})

Okno s definíciou kroku

Vyberte kartu **Ovládacie prvky zastavenia** ![]({{ '/assets/icons/pre_icons/mo_stopping_criteria.jpg' | relative_url }}) a nastavte **Trvanie procesu** na **3600** sekúnd. (pozri obr. 2DHTML1.23.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0023.jpg' | relative_url }})

Okno s ovládacími prvkami na zastavenie

V časti **Procesné podmienky** ![]({{ '/assets/icons/pre_icons/mo_process_conditions.jpg' | relative_url }}) nastavte **teplotu prostredia** na **850** °C a zmeňte **konvekčný koeficient** na **0,1**. Tento konvekčný koeficient je podobný konvekčnému koeficientu určitých druhov chladiacich olejov. (pozri obr. 2DHTML1.24.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na stránku generovania databázy.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0024.jpg' | relative_url }})

Okno „Podmienky procesu“ 

## Vytvoriť databázu

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení úlohy niečo nechýba. Počas kontroly červené správy označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch). Ak sa nezobrazujú žiadne chyby, databázu je možné vygenerovať.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu (pozri obr. 2DHTML1.25.). Keď program dokončí zapisovanie databázy, prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0025.jpg' | relative_url }})

Okno „Vytvoriť databázu“

## Spustenie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 2DHTML1.26. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0026.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať prostredníctvom okien „Simulation Message“ a „Process Monitor“ v režime simulácie. Kliknutím na kartu „Simulation Message“ zobrazíte súbor správ. Súbor správ sa aktualizuje každých pár sekúnd.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha. (Pozri obr. 2DHTML1.27.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0027.jpg' | relative_url }})

Simulačná správa

##  Následné spracovanie výsledkov

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), kde si môžete prezrieť výsledky; otvorí sa postprocesor MO.

Kľúčovou stavovou premennou, ktorú treba skúmať, je fázový objemový podiel. Kliknutím na tlačidlo „State Variables ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }})“ otvoríte dialógové okno so stavovými premennými. Na karte „Microstructure“ otvorte premennú „Volume Fraction“. Vyberte zložku „Pearlite“ a vyneste premennú ako tieňovanú kontúru. Používateľ by mal vidieť, že premenná má spočiatku hodnotu 1,0 (čo znamená, že 100 % štruktúry tvorí perlit) a nakoniec klesne na 0,0 (čo znamená, že 0 % materiálu tvorí perlit). Používateľ by mal znázorniť aj ostatné objemové podiely, aby určil, na ktorú zložku sa objem premenil (pozri obr. 2DHTML1.28.). Kliknite na tlačidlo **Stav****Premenné**![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) a vykreslite **Teplotu**![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) (pozri obr. 2DHTML1.29.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0028.jpg' | relative_url }})

Graf objemového podielu a perlitov

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0029.jpg' | relative_url }})

Graf teploty

Okrem toho by sa používateľ mal pozrieť na zmenu objemu objektu v závislosti od času. Kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_summary_icon.jpg' | relative_url }}) **Súhrn** otvoríte dialógové okno Súhrn. Vykreslite objem. Mal by sa zobraziť graf objemu objektu v závislosti od času, ako je znázornené na obr. 2DHTML1.30. Treba poznamenať, že bez fázovej transformácie by sa objem objektu v dôsledku tepelnej rozťažnosti monotónne zvyšoval s teplotou. Pri transformácii dochádza počas transformácie k poklesu objemu. Je to preto, lebo austenit má štruktúru FCC, zatiaľ čo perlit pozostáva z feritu (štruktúra BCC) a cementitu (ortorombická štruktúra). FCC je hustá štruktúra, a preto má menší objem ako BCC alebo akákoľvek ortorombická štruktúra, čo spôsobuje, že premena austenitu na perlit vedie k zníženiu objemu.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab1_heating/image0030.jpg' | relative_url }})

Okno súhrnu – Graf objemu

## Ukončenie sprievodcu MO

Keď skončíte, ukončite postprocesor MO kliknutím na ikonu zatvorenia ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }}); zobrazí sa vyskakovacie okno s možnosťou uložiť zmeny. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) v tomto okne a sprievodca MO sa zatvorí. 

(Alebo)

Ak chce používateľ pokračovať v nastavení, môže priamo prejsť do režimu „pre“ a pokračovať v nastavení pridaním operácie.

Súvisiace témy:

[2D HT Lab2 Carburization]({{ '/docs/sk/labs/heat_treatment_labs/2d_ht_lab2_carburization/' | relative_url }})

[2D HT Lab3 Diffusion]({{ '/docs/sk/labs/heat_treatment_labs/2d_ht_lab_3_diffusion/' | relative_url }})

[2D HT Lab4 Quenching ]({{ '/docs/sk/labs/heat_treatment_labs/2d_ht_lab4_quenching/' | relative_url }})
