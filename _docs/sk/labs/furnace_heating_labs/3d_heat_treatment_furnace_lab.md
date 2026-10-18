---
lang: sk
title: "Laboratórium s 3D pecou na tepelné spracovanie"
---

# Šablóna laboratória pre 3D pec na dávkové tepelné spracovanie

## Zhrnutie problému

Šablóna „Pec na tepelné spracovanie v dávkach“ v novej funkcii MO (Multiple Operations) je praktický nástroj na nastavenie procesu s viacerými operáciami, ktorý slúži na modelovanie ohrevu viacerých obrobkov a upínacích prípravkov v dávkovej peci podľa predpísaných časových a teplotných bodov (tepelného plánu).

V rámci tohto cvičenia si ukážeme, ako pomocou tejto šablóny pripraviť simuláciu ohrevu v peci s kruhovým nákladom pozostávajúcim zo 6 oceľových dielov. Toto cvičenie môže používateľom pomôcť pochopiť možnosti nového MO.

## Začiatok úlohy s viacerými operáciami

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek zvoľte prepínač „**Anglický**“, ako je znázornené na obr. 3FHL1.1. Názov úlohy zadajte ako „****DrillBit****“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt (pozri obr. 3FHL1.2.), v tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**DrillBit**“, systém jednotiek **anglický** a klikneme na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) na vytvorenie projektu.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0002.jpg' | relative_url }})

DEFORM – Nová operácia „Multiple“ – Hlavné okno

V položke „Umiestnenie“ sa vytvorí nový projekt a jeho priečinok, ako je znázornené na obrázku [Fig. 3FHL1.3.]({{ '/docs/sk/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/' | relative_url }}#Fig_3DMBL1_3_Added_multiple_blow_forging_operation_into_operation_editor)

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0003.jpg' | relative_url }})

Nová zložka projektu „DrillBit“

## Pridať do projektu modul dávkovej pece na tepelné spracovanie

Ak chcete do MO pridať proces „Kúrenie pecou“, presuňte kurzor myši do ľavej časti hlavného okna MO a umiestnite ho na záložku „Explorer“. Zobrazí sa okno „Explorer“, ktoré sa rozbalí zľava doprava, pozri [Fig. 3FHL1.4.]()

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0004.jpg' | relative_url }})

Pridanie procesu vykurovania pecou do projektu MO

V okne „Explorer“ kliknite na „**Tepelné spracovanie (3)**“, potom na „**Jednotlivé**“ a v kategórii „**Jednotlivé**“ kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) (Pridať) vpravo od položky „**[3D] Ohrievanie v peci**“, ako je znázornené na obr. 3FHL1.4. V tomto laboratórnom cvičení si totiž ukážeme, ako pomocou nového MO pripraviť simuláciu ohrievania viacerých oceľových dielov v peci so špecifickým rozložením zaťaženia. Týmto sa do projektu pridá trojrozmerný proces ohrevu v peci na tepelné spracovanie; ako dôkaz bola do „Editoru operácií“ vložená grafická položka, ktorú je možné vidieť na obr. 3FHL1.5. Kliknutím na položku ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/oprn_editor_oprn.jpg' | relative_url }}) sa stromová štruktúra, ktorú predstavuje okno „Navigátor“ na pravej strane hlavného okna modulu MO, prebuduje na základe preddefinovaného typu šablóny, pozri obr. 3FHL1.5.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0005.jpg' | relative_url }})

Okná MO; (a) Okno prehliadača (b) Okno editora operácií (c) Okno stromu operácií

Stromová štruktúra v okne „Operačný strom“ zobrazuje položky, ktoré bude potrebné nakonfigurovať pre simuláciu „Kúrenie v peci“. Kliknutím na ľubovoľnú položku prejdete do príslušného konfiguračného okna, alebo kliknutím na tlačidlá ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) v pravom dolnom rohu môžete prechádzať medzi rôznymi konfiguračnými oknami.

V nasledujúcich kapitolách si prejdeme jednotlivé konfiguračné okná.

## Nastavenie procesu

Okno „Proces“ obsahuje predovšetkým zoznam niekoľkých parametrov (Vlastnosti) a predstavuje prehľad informácií o projekte, ako je znázornené na obr. 3FHL1.6. Niektoré ovládacie prvky je možné rýchlo upraviť bez nutnosti prechádzať jednotlivými konfiguračnými oknami.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0006.jpg' | relative_url }})

Stránka procesu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste vybrali objekty.

## Definícia obrobku

V tomto laboratórnom cvičení sa používa iba obrobok, preto nechajte zaškrtnuté rádio tlačidlo **1 obrobok** (pozri obr. 3FHL1.7.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali obrobok.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0007.jpg' | relative_url }})

Okno na výber objektov

### Pomenujte objekt

Ako názov objektu zadajte „**Vrták**“, ostatné nastavenia ponechajte v predvolenom stave, ako je znázornené na obr. 3FHL1.8. Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku definície „Geometria“, ako je znázornené na obr. 3FHL1.9.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0008.jpg' | relative_url }})

Okno definície objektu obrobku

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0009.jpg' | relative_url }})

Okno na definovanie geometrie obrobku

### Vytvorenie geometrie

Na stránke „Geometria“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), v nasledujúcom okne vyberte „**Cylinder**“ a zadajte **9,8** palca ako **priemer** a **24** palcov ako **výšku**, ako je znázornené na obr. 3FHL1.10. Geometria objektu sa zároveň zobrazí v náhľade v strednej časti grafického okna. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) potvrďte všetky zmeny a systém sa vráti do definície „Geometria“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Mriežka“, pozri obr. 3FHL1.11.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0010.jpg' | relative_url }})

Nastavenia geometrických primitív na vytvorenie dielu „Vrták“

### Vytvoriť sieť objektu

V tejto šablóne je možné vygenerovať iba „Tetrahedrálnu sieť“; do poľa „Cieľový počet prvkov“ zadajte hodnotu **5000** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Ikona myši na obrazovke sa zmení na ikonu „zaneprázdnená“ a potom sa vráti do normálneho stavu, čo znamená, že sieť bola vygenerovaná; výsledky sa tiež zobrazia v centrálnej grafickej oblasti, pozri obr. 3FHL1.11. Používateľ si môže sieť predbežne prezrieť kliknutím na ![]({{ '/assets/icons/pre_icons/mo_preview_mesh_button2.jpg' | relative_url }}); keďže sa tým vygeneruje len povrchová sieť, bude to rýchle. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), prejdite na stránku „Material“ (Materiál), pozri obr. 3FHL1.12.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0011.jpg' | relative_url }})

Vytváranie sietí

### Načítanie a priradenie materiálu

V okne výberu objektu „Materiál“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať materiál zo súboru) „**4340.key**“ zo zložky **\3d\LABS\Furnace_Material** v inštalačnej ceste, ako je znázornené na obr. 3FHL1.12. Systém automaticky priradí načítaný materiál k obrobku. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste otvorili okno „Načítanie vzoru“.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0012.jpg' | relative_url }})

Načítať a priradiť materiál z knižnice

## Definovanie vzoru zaťaženia

Modelovanie dávky viacerých dielov zahrievaných v dávkovej peci s cieľom definovať rozloženie dávky. Vytvorí sa kruhový vzor s 6 dielmi, preto zvoľte typ vzoru „Kruhový“, do stĺpca „Rad“ zadajte hodnotu 6, vzdialenosť medzi obrobkami je 17 palcov a ponechajte zaškrtnutú možnosť „Stredová symetria“, pozri obr. 3FHL1.13. Dokončite definíciu rozloženia nákladu; rozloženie si môžete predbežne prezrieť kliknutím na tlačidlo, výsledok sa zobrazí v strednej časti grafického okna, pozri obr. 3FHL1.13.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0013.jpg' | relative_url }})

Návrh rozloženia zaťaženia dielov; okno na definovanie rozloženia zaťaženia a náhľad rozloženia zaťaženia

## Definícia dávkovej pece

V tejto časti bude predstavená definícia pece. Kliknutím na stromovú štruktúru a trojuholníkové tlačidlo vedľa položky ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/fold_list.jpg' | relative_url }}) rozbalíte položku definície **„Batch Furnace“**, pod ktorou sa nachádza niekoľko podpolí, ktoré je potrebné nakonfigurovať.

  * ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/general_settings.jpg' | relative_url }})Základné informácie o peci, ako napríklad tvar, rozmery, zdroj tepla atď.

  * ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/wall.jpg' | relative_url }}) Informácie o stenách pece, vrátane materiálu, počtu vrstiev a hrúbky.

  * ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/cooling_system.jpg' | relative_url }})Parametre súvisiace s chladením, napríklad prietok chladiacej vody, vstupná a výstupná teplota vody.

  * ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/fan_system.jpg' | relative_url }})Nastavenia recirkulačného ventilátora, veľkosť ventilátora, materiál, rýchlosť atď.

  * ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/accesory.jpg' | relative_url }})Informácie o príslušenstve: tento nástroj je určený na odhad tepla absorbovaného akýmikoľvek malými časťami pece, ktoré nie je potrebné zahrnúť do siete, za predpokladu, že ich teplota je rovnomerná a zhodná s teplotou pece.

Kliknutím na položku v stromovej štruktúre s názvom „Definícia pece“ (![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/batch_furnace_lable.jpg' | relative_url }})) sa otvorí hlavné okno „Dávková pec“, ako je znázornené na obr. 3FHL1.14.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0014.jpg' | relative_url }})

Hlavné okno s definíciami dávkovej pece

Nastavte „Názov pece“ na „**Linderburg426**“ a počiatočnú „Teplotu pece“ na **1260** F. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavenie potvrdili, a prejdite do okna „Všeobecné nastavenia“ (![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/general_settings.jpg' | relative_url }})).

*Upozorňujeme, že „Scaling“ je mierka modelu; jeho použitie sa neodporúča, pretože si vyžaduje nastavenie špeciálnych okrajových podmienok, preto ho nechajte na hodnote 1.

### Všeobecné nastavenia

Tvar telesa dávkovej pece Linderburg426 je „**vertikálny valec**“, jej celkové rozmery sú **99,6** palca v priemere a **72** palcov na výšku. Ide o elektrickú pec s pripojeným tepelným príkonom **113,727** Btu/s.

Dokončite všetky nastavenia (pozri obr. 3FHL1.15.), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste ich potvrdili, a prejdite do okna definície „Wall“ (![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/wall.jpg' | relative_url }})).

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0015.jpg' | relative_url }})

Všeobecné nastavenia

### Stena

Na stránke s definíciami „Steny“ bude potrebné zadať tri skupiny informácií: „Strecha“, „Bočná stena“ a „Dno“. 

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0016.jpg' | relative_url }})

Nakladanie a rozmiestňovanie materiálu na stenu

Predvolenou hodnotou sú údaje pre „Strechu“; nastavte počet **vrstiev** na **1** a **hrúbku** na **10** palcov, pozri obr. 3FHL1.16.

Ak chcete priradiť materiál vrstve, kliknite na roletové menu „**Materiál**“ pri položke „**Vrstva 1**“, ako je znázornené na obr. 3FHL1.17. Presuňte kurzor myši na položku „**Prehľadávať...**“ “ a vyberte súbor s kľúčovými slovami materiálu **„CF_Veneen_2800F.key** “ zo zložky \3d\LAB\Furnace_Material v inštalačnej ceste. V dôsledku toho sa „CF_Veneen_2800F“ pridá do tohto roletového zoznamu a zvolí sa ako aktuálny materiál pre vrstvu 1. Okrem toho je k dispozícii aj pre „Bočnú stenu“ a „Dno“. Medzitým je podporovaná aj metóda „Drag and Drop“ (ťahaj a pusť); týmto spôsobom pretiahnite názov materiálu z prehliadača „Material“ (obr. 3FHL1.17.) a umiestnite ho do roletového zoznamu materiálov.

Všimnite si tlačidlo ![]({{ '/assets/icons/pre_icons/mo_material_icon.jpg' | relative_url }}) vedľa názvu materiálu ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/cf_veneen_2800f_mat_list.jpg' | relative_url }}); kliknutím na toto tlačidlo sa dostanete na stránku „Editor materiálov“ (obr. 3FHL1. obr. 3FHL1.17.). Je možné vykonávať zmeny na aktuálne priradenom materiáli.

Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_side_wall_button.jpg' | relative_url }}), nastavte počet **vrstiev** na **1** a **hrúbku** na **9** palcov, pozri obr. 3FHL1.17.. Z roletového zoznamu materiálov vyberte „**CF_Veneen_2800F**“ a priraďte ho k vrstve 1 bočnej steny.

Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_bottom_button.jpg' | relative_url }}), nastavte počet vrstiev na 1 a **hrúbku** na **9** palcov, pozri obr. 3FHL1.17. Z roletového zoznamu materiálov vyberte „**CF_Veneen_2800F**“ a priraďte ho k vrstve 1 spodnej steny.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0017.jpg' | relative_url }})

Definícia steny

Dokončite všetky nastavenia, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste ich potvrdili, a prejdite do okna definície „Chladiaci systém“ (![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/cooling_system.jpg' | relative_url }})).

### Chladiaci systém

V tomto cvičení nechajte všetky polia nastavené na nulu, pozri obr. 3FHL1.18. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite do okna definície „Fan System“ (![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/fan_system.jpg' | relative_url }})).

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0018.jpg' | relative_url }})

Definícia chladiaceho systému

### Systém ventilátorov

Ide o vákuovú pec, preto zaškrtnite políčko „Bez atmosféry“ ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/non_atmosphere.jpg' | relative_url }}), ako je znázornené na obr. 3FHL1.19.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0019.jpg' | relative_url }})

Definícia ventilátorového systému

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a potom prejdite na definíciu „Príslušenstvo“ (![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/accesory.jpg' | relative_url }})).

### Príslušenstvo

Celková hmotnosť vykurovacích prvkov modelu Linderburg426 je **50** libier, sú vyrobené z grafitu. Okrem toho je potrebné pri odhade tepelného zaťaženia zohľadniť aj celkovú hmotnosť **1200** libier nosných konštrukcií zo zliatiny.

Na stránke „Príslušenstvo“ nastavte počet príslušenstiev na 2 (pozri obr. 3FHL1.20.) a následne priraďte materiál k príslušným častiam pece.

V tomto laboratórnom cvičení nastavte príslušenstvo 1 ako vykurovacie prvky; keďže súbor s kľúčovými slovami pre grafit je už pripravený, stačí vybrať ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/graphite_list.jpg' | relative_url }}) z adresára **\3d\LABS\Furnace_Material\Wall\GRAPHITE.Zadajte **KĽÚČ** v inštalačnej ceste do okna „Accessory“ v súbore ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/material_list_1.jpg' | relative_url }}).

Potom nastavte príslušenstvo 2 ako podpery; podobne prejdite z adresára **\3d\LABS\Furnace_Material\Accessory\Alloy.KEY** v inštalačnej ceste do okna „Accessory“ v programe ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/material_list_2.jpg' | relative_url }}).

V tomto laboratórnom cvičení nastavte príslušenstvo 1 ako vykurovacie prvky; keďže súbor s kľúčovými slovami pre grafit je už pripravený, stačí v inštalačnej zložke vyhľadať súbor ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/alloy_list.jpg' | relative_url }}) z adresára **\3d\LABS\Furnace_Material\Wall\GRAPHITE.KEY** a vložiť ho do okna „Príslušenstvo“.

Potom nastavte príslušenstvo 2 ako podpery; podobne prejdite z adresára **\3d\LABS\Furnace_Material\Accessory\alloy.KEY** v inštalačnej zložke do okna „Príslušenstvo“.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0020.jpg' | relative_url }})

Priradiť materiál k príslušenstvu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste potvrdili zmeny. Týmto je definícia pece dokončená, pec Linderburg426 bola úspešne vytvorená a nakonfigurovaná.

*Všimnite si, že na hlavnej stránke s definíciami „Batch Furnace“ (obr. 3FHL1.15) sa nachádzajú štyri nastavenia týkajúce sa materiálu pece,

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/fuel_list.jpg' | relative_url }})

\- podadresár „plyn/palivo“

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/wall_list.jpg' | relative_url }})

\- materiál vrstvy steny pece

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/atm_list.jpg' | relative_url }})

\- atmosféra v peci

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/accs_list.jpg' | relative_url }})

\- doplnkový materiál

Tieto nastavenia určujú predvolenú podzložku materiálu, v ktorej sa nachádzajú príslušné súbory s kľúčovými slovami pre materiály, takže každý súbor s kľúčovými slovami pre materiály nachádzajúci sa v týchto zložkách sa zobrazí v príslušnom roletovom menu materiálov, ako je vidieť na obr. 3FHL1.15.

## Tepelný harmonogram a PID regulácia

### Termínový harmonogram

Tepelný plán predstavuje nastavené hodnoty času a teploty. Ak ho chcete definovať, kliknite v stromovej štruktúre na položku „Tepelný plán“ ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/thermal_schedule_list.jpg' | relative_url }}).

V nasledujúcom okne na definovanie „tepelného plánu“, ako je znázornené na obr. 3FHL1.21, vyberte ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/function_of_time_radio_button.jpg' | relative_url }}) a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}).

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0021.jpg' | relative_url }})

Definícia tepelného harmonogramu

Následne sa v strednej časti okna zobrazí okno s definíciou funkcie „Teplota okolia“; do tabuľky zadajte nasledujúce páry údajov „čas (s)/teplota (F)“: „0/1260“, „13500/1260“, „13620/1220“, „22860/1220“, „24000/1600“ a „54000/1600“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_button2.jpg' | relative_url }}) si môžete prezrieť funkciu vo forme krivky, ako je znázornené na obr. 3FHL1.22.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0022.jpg' | relative_url }})

Definícia environmentálnej funkcie

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste potvrdili hodnoty.

### PID regulácia

Späť na stránku s definíciou „Tepelného harmonogramu“, ako je znázornené na obr. 3FHL1.23.

Zapnite PID reguláciu kliknutím na ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/on_radio_bitton.jpg' | relative_url }}). Potom nastavte „Spain“ na **2400** F, „Proportional Gain“ na **10**, „Integral Gain“ na **0,000833333** 1/s a „Damping“ nechajte na nule.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0023.jpg' | relative_url }})

Definícia PID regulácie

Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste potvrdili nastavenia PID, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre otvorenie okna ovládacích prvkov polohovania a zastavenia, keďže polohovanie nie je potrebné a ovládacie prvky zastavenia na základe trvania procesu budú definované v simulácii času ohrevu, ako je znázornené na obr. 3FHL1.24.

## Riadenie simulácie

Zaškrtnite políčko **Zobraziť****faktor**, aby ste aktivovali žiarenie, zadajte **Čas****kúrenia** ako **54000** sekúnd a vyberte prepínač **Auto** pre definíciu krokov, čím nastavíte definíciu krokov na základe teploty. Nechajte predvolené hodnoty definície krokov, t. j. zmena teploty na krok 5 °F, minimálny a maximálny čas na krok 0,001, resp. 10 sekúnd.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0024.jpg' | relative_url }})

Riadenie simulácie

## Vytvoriť databázu

Na stránke „Generate DB“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), ako je znázornené na obr. 3FHL1.25. V oblasti okna „Message“ sa zobrazí správa, že databáza bola úspešne vygenerovaná.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0025.jpg' | relative_url }})

Okno „Vytvoriť databázu“

## Spustiť simuláciu

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 3FHL1.26. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0026.jpg' | relative_url }})

Spustiť simuláciu

*Poznámka: Uistite sa, prosím, že používate len jeden procesor; tento model pece zatiaľ nepodporuje viacjadrové procesory.

Kliknite na ponuku „Simulácia“ > „Monitor procesov“; otvorí sa okno „Monitor procesov“, ako je znázornené na obr. 3FHL1.27. Informácie o spustenej databáze „DrillBit“ sú uvedené v zozname pod položkou „Spustené úlohy“.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0027.jpg' | relative_url }})

Monitor procesov

V okne „Správa“ je vidieť, že informácie o prebiehajúcej úlohe sa tiež často aktualizujú.

## Následné spracovanie

Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), aby ste spustili postprocesor pre databázu. Okrem premenných popisujúcich stav deformácie, ako je napríklad teplota obrobkov, budú k dispozícii aj informácie týkajúce sa spotreby energie pece.

#### Spotreba energie

Ako je vidieť na obr. 3FHL1.28., v postprocesore kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_summary_icon.jpg' | relative_url }}) (Súhrn), aby ste si zobrazili súhrn simulácie. V okne „Súhrn“ kliknite na **Tepelné spracovanie** a potom na ![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/furnace_lable.jpg' | relative_url }}).

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0028.jpg' | relative_url }})

Krivka spotreby energie pece

Ako je znázornené na obr. 3FHL1.28, na prehľadovej stránke „Pec“ sa nachádza niekoľko premenných týkajúcich sa spotreby energie v peci,

  * Hrubý energetický príkon – hodnota energie dodanej počas prevádzky v závislosti od času.

  * Teplo na náplň – teplo absorbované všetkými obrobkami počas prevádzky.

  * Teplo akumulované v peci – teplo absorbované všetkými stenami pece počas prevádzky.

  * Vodné chladenie – teplo vznikajúce počas prevádzky je odvádzané chladiacou vodou.

  * Straty cez steny – straty žiarenia počas prevádzky cez horúce steny.

  * Straty cez otvory – straty žiarenia počas prevádzky cez akékoľvek otvorené miesta, ako sú otvory v stene pece.

  * Chladenie ventilátorom – počas prevádzky sa teplo odvádza do systému chladiacej vody recirkulačného ventilátora.

  * Teplo generované ventilátorom – teplo vznikajúce počas prevádzky recirkulačného ventilátora pri jeho chode.

  * Teplota pece – simulovaná teplota pece.

  * Nastavená hodnota – teplotný program.

Po výbere akejkoľvek premennej kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}); v grafickom okne sa zobrazí príslušná krivka spotreby energie, ktorá znázorňuje vzťah medzi hodnotou tepla v priebehu času a časom, ako je vidieť na obr. 3FHL1.28.

#### Sledovanie teploty v rôznych miestach

Sledovanie bodov je veľmi užitočný nástroj na kontrolu rozloženia teploty v rámci rozloženia nákladu.

Ako je vidieť na obr. 3FHL1.29, vyberte dva body – jeden ako rohový a druhý ako stredový –, označte všetky kroky a potom sledujte priebeh teploty; výsledky sú znázornené na obr. 3FHL1.29.

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0029.jpg' | relative_url }})

Body sledovania

Z obr. 3FHL1.30 vyplýva, že roh a stred obrobku sa zahrievajú takmer rovnakou rýchlosťou, takže teplotný rozdiel je relatívne menší, čo výrazne pomáha pri kontrole kvality tepelného spracovania. (Údaje sú exportované z grafu sledovania bodov a súhrnného grafu nastavenej hodnoty a teploty pece.)

![]({{ '/assets/images/labs/furnace_heating_labs/3d_heat_treatment_furnace_lab/image0030.jpg' | relative_url }})

Teplotný profil

**Súvisiace témy:**

[6.2. Integrated Manufacturing Process Simulation layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/' | relative_url }})

[6.3. Integrated Manufacturing Process Post layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/' | relative_url }})

[Heat Treatment Operation]({{ '/docs/sk/operation_templates/37_heat_treatment/37_introduction_to_heat_treatment/' | relative_url }})
