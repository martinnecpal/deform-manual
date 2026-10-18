---
lang: sk
title: "Laboratórne cvičenie na 2D tvárnenie v režime Expert"
---

# Laboratórne cvičenie: 2D tvárnenie v režime Expert

  
V tomto laboratórnom cvičení si ukážeme, ako nastaviť typickú operáciu tvárnenia po ohreve v peci v expertnom režime viacerých operácií (MO). Operácia tvárnenia je otvorené prostredie, v ktorom môže používateľ nastaviť akýkoľvek problém týkajúci sa deformácie, prenosu tepla, difúzie a tepelného spracovania, avšak pre nových používateľov je k dispozícii režim s návodom, ktorý ich prevedie jednoduchými a základnými funkciami ovládania simulácie, generovania siete, zastavenia a ovládania krokov. Po oboznámení sa s programom DEFORM môže používateľ pre podrobnejšie štúdium využiť pokročilé funkcie v režime expert.

V rámci tohto cvičenia sa pokúsime preskúmať niekoľko funkcií systému v režime pre pokročilých.

## Vytvorenie nového problému a pridanie operácií

### Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno „Nový problém“

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. 2DFEL1.1. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Názov úlohy zadajte ako „**Forming_Operation_in_expert_Mode**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

Otvorí sa sprievodca viacerými operáciami, v tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**Forming_Operation_in_expert_Mode**“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie. Otvorí sa sprievodca MO (pozri obr. 2DFEL1.2.). Ako prvú operáciu vyberte 2D operáciu prenosu tepla a zaškrtnite políčko na pridanie operácie prenosu tepla ako prvej operácie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste pokračovali v otváraní operácie.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0002.jpg' | relative_url }})

Okno na otvorenie nového projektu v nástroji MO Wizard

###  Pridanie operácie tvarovania

Sprievodca viacerými operáciami otvorí nový projekt s 2D operáciou prenosu tepla. Pridajte jednu operáciu tvarovania pre tvarovanie kužeľa po prenose tepla vzduchom po dobu 5 sekúnd z pece do foriem pomocou zoznamu operácií v prehliadači kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ako je znázornené na obr. 2DFEL1.3.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0003.jpg' | relative_url }})

Pridanie formovacej operácie

## Úloha 1: Nastavenie vykurovacieho systému pre prenos tepla

Pri prvom procese prenosu tepla zmeňte názov procesu na „**Prenos vzduchom**“ dvojitým kliknutím na názov procesu v okne Editoru procesov, ako je znázornené na obr. 2DFEL1.4, a po úprave stlačte klávesu **Enter** na klávesnici.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0004.jpg' | relative_url }})

Prvú operáciu nazvite „Letecký transfer“

### Výber typu geometrie

V tomto laboratórnom cvičení používame osovo symetrické geometrie, preto v okne typu geometrie zaškrtnite políčko **2D osovo symetrické**, ako je znázornené na obr. 2DFEL1.3., a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

### Výber typu prenosu tepla

Ako typ prenosu tepla pre prevádzku „Prenos vzduchom“ vyberte možnosť „**Prenos vzduchom**“, ako je znázornené na obr. 2DFEL1.5. Tým sa nastavia predvolené nastavenia prenosu tepla pre režim kúrenia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0005.jpg' | relative_url }})

Výber typu prenosu tepla pre prenos vzduchom

### Nastavenie podmienok spracovania

Nastavte **čas prenosu** na **5** sekúnd pri teplote okolia 68 °F a predvolený koeficient konvekcie podľa obr. 2DFEL1.6. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0006.jpg' | relative_url }})

Nastavenia prevádzkových podmienok pre prenos vzduchu

### Vyberte ovládacie prvky simulácie pre prenos vzduchu

V okne ovládacích prvkov simulácie bude aktivovaný expertný režim (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) (pozri [Fig. 2DFEL1.7.]()); kliknutím na ikonu na karte „Nástroje“ si môžete prezrieť možnosti ovládania simulácie v expertnom režime.

Na karte „Main“ nechajte zaškrtnutý iba režim „Heat Transfer“, pretože sa modeluje iba prenos tepla, ako je znázornené na obr. 2DFEL1.7. K dispozícii sú aj ďalšie pokročilé funkcie, ako napríklad krok, zastavenie, riešiteľ, procesné podmienky atď. Niektoré z týchto funkcií použijeme pri vytváraní siete, zastavovaní a riadení krokov v neskoršej fáze nastavenia. Ďalšie informácie o možnostiach ovládania simulácie nájdete v [Simulation Controls]({{ '/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte ďalej.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0007.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre vykurovanie pece v expertnom režime

### Import materiálu pre obrobok

V okne „Material“ načítajte materiál **AISI-4120** z knižnice materiálov DEFORM, z kategórie **Steel**, pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To je možné vykonať tak, ako je znázornené na obr. 2DFEL1.8, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Materiál je možné načítať aj zo zoznamu materiálov v Průzkumníku. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre okno Materiál a objekt, keďže v prípade prevádzky s prenosom tepla vzduchom nás zaujíma iba prenos tepla obrobku vo vzduchu.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0008.jpg' | relative_url }})

Import materiálu obrobku z knižnice DEFORM

### Definícia obrobku

V okne „Objekt obrobku“ ponechajte typ objektu ako „**Plast**“ a zadajte teplotu obrobku **1750** °F (pozri obr. 2DFEL1.9.). Pomocou možnosti „Importovať objekt zo súboru“ ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) môžete importovať údaje o objekte zo súboru kľúčových slov alebo z databázy a pomocou možnosti „Importovať objekt z knižnice“ môžete importovať údaje o objekte zo súboru kľúčových slov. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali a importovali geometriu obrobku.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0009.jpg' | relative_url }})

Definícia objektu obrobku

### Vytvorenie geometrie obrobku

Na stránke „Geometria“ kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) (pozri obr. 2DFEL1.10.) a vytvorte **valec** s polomerom **0,4** " a výškou **2,7** ", ako je znázornené na obr. 2DFEL1.11.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0010.jpg' | relative_url }})

Okno s definíciou geometrie

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0011.jpg' | relative_url }})

Vytvorenie geometrie valca pre obrobok

### Vytvorenie siete obrobku

V expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) je k dispozícii kompletná škála možností vytvárania sietí; pre prevádzku s prenosom vzduchu vytvorte sieť s použitím **1000** prvkov a **pomero veľkostí** **3**, ako je znázornené na obr. 2DFEL1.12. V ďalšom kroku použijeme iné okno hustoty siete a možnosti opätovného vytvorenia siete. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali. Ďalšie informácie o možnostiach siete v expertnom režime nájdete v [13.1. 2D Mesh Generation]({{ '/docs/sk/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/' | relative_url }}).

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0012.jpg' | relative_url }})

Vytvorenie siete pre obrobok

### Priradiť materiál obrobku

Ak chcete obrobku priradiť materiál, vyberte v okne materiálov materiál „**AISI****-4120**“. Postupujte podľa obrázku 2DFEL1.13. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0013.jpg' | relative_url }})

Priradenie materiálu k obrobku

### Definovanie okrajových podmienok obrobku

Na stránke BCC skontrolujte predvolené nastavenie „Výmena tepla s prostredím“ (BCC) pre celý vonkajší povrch polotovaru (čo nezahŕňa os, keďže tieto uzly sa nachádzajú vnútri objektu) kliknutím na položku „Definované“ v časti „Výmena tepla s prostredím“. Predvolené BCC sa priradia automaticky na základe výberu typu úlohy ako osovo symetrickej a simulačného režimu ako prenos tepla. (pozri obr. 2DFEL1.14.)

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0014.jpg' | relative_url }})

Definícia okrajových podmienok pre obrobok

Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezatvorí okno ovládacích prvkov, keďže nie je potrebné nastavovať polohu objektu.

### Kontrola brzdových ovládačov

V okne „Zastavovacie riadenie“ v expertnom režime môžeme vidieť, že čas prenosu **5** sekúnd, definovaný v okne „Podmienky procesu“ na začiatku nastavenia, sa tu odráža ako „Trvanie procesu“ v zastavovacom riadení, ako je znázornené na obr. 2DFEL1.15. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0015.jpg' | relative_url }})

Ovládanie zastavenia prevádzky leteckej prepravy

### Definovanie ovládacích prvkov krokov

Nastavte typ definície kroku na **časový prírastok** s konštantnou hodnotou **0,1** s na karte „Prírastok kroku“, ako je znázornené na obr. 2DFEL1.16.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0016.jpg' | relative_url }})

Definícia krokového prírastku pre prenos vzduchu

Na karte „Simulačné kroky“ nastavte **počet simulačných krokov** na hodnotu **50** a ukladanie každých **5** krokov, ako je znázornené na obr. 2DFEL1.17. V expertnom režime ovládania krokov (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) sú k dispozícii aj rôzne pokročilé nastavenia ovládacích prvkov simulácie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do fázy generovania databázy.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0017.jpg' | relative_url }})

Definícia simulačných krokov pre prenos vzduchu

### Vytvoriť databázu

V etape vytvárania databázy môže používateľ skontrolovať údaje potrebné na analýzu a pokračovať vo vytváraní databázy (pozri obr. 2DFEL1.18.). Pred prvou operáciou z akéhokoľvek súboru viacerých operácií je používateľ povinný vytvoriť databázu. Pre všetky nasledujúce operácie stačí nastaviť len procesné údaje a parametre simulácie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k ďalšej operácii „**Tvarovanie kužeľa**“.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0018.jpg' | relative_url }})

Okno na vytvorenie databázy pre prvú operáciu

## Operácia 2: Tvarovanie

Operácia tvárnenia prebieha dovtedy, kým vzdialenosť medzi maticami nedosiahne hodnotu 0,025". Keďže obrobok prichádza z operácie vzduchového prenosu so svojou teplotnou históriou, vytvorte obrobok podľa údajov z objektu v databáze a pridajte ďalšie tri objekty pre razník, spodnú maticu a vyhadzovač, aby ste nastavili operáciu tvárnenia kužeľa.

Pomenujte operáciu ako „**Tvarovanie kužeľa**“ dvojitým kliknutím na položku Názov operácie v editore operácií a stlačením klávesy Enter na klávesnici operáciu zatvorte. Potvrďte osovo-symetrický typ geometrie a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

### Vyberte nastavenia ovládacích prvkov simulácie pre tvarovanie kužeľa

V nastaveniach simulácie zaškrtnite oba simulačné režimy **Deformácia** a **Prenos tepla**, ako je znázornené na obr. 2DFEL1.19. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0019.jpg' | relative_url }})

Nastavenia riadenia simulácie pri tvarovaní kužeľa

### Materiál na výrobu foriem

V okne materiálov naimportujte materiál **AISI-H13** pre lisovacie formy z **knižnice DEFORM** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) v kategórii **Die_material**, ako je znázornené na obr. 2DFEL1.20. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa otvorí okno objektov, a pridajte objekty.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0020.jpg' | relative_url }})

Import materiálu výsekových foriem z knižnice DEFORM

### Pridať objekty s kockami

V okne „Object“ pridajte 4 objekty tak, ako je znázornené na obr. 2DFEL1.21., keďže na operáciu tvarovania kužeľa budeme používať všetky tri matrice pri teplote **300** °F. Teraz vidíme, že strom objektov je rozbalený a obsahuje matrice, ktorých podrobnosti teraz definujeme. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0021.jpg' | relative_url }})

Pridávanie objektov na vytvorenie kužeľa

### Definícia obrobku

V okne definície obrobku vyberte typ objektu „**Načítať z databázy**“, ako je znázornené na obr. 2DFEL1.22. Po definovaní foriem nastavíme v okne hustoty siete pre obrobok vnútorný roh hornej časti spodnej formy pre tvarovanie kužeľa, preto kliknite na položku „Top Die“ (Horná forma) v strome operácií, aby ste definovali formy.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0022.jpg' | relative_url }})

Okno definície obrobku pri tvárnení kužeľa

### Definícia hornej matrice

V okne definície „Top die“ nastavte typ objektu na „rigid“ a zadajte počiatočnú teplotu **300** °F, ako je znázornené na obr. 2DFEL1.23. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0023.jpg' | relative_url }})

Okno definície hornej matrice pri tvárnení kužeľa

### Import a úprava geometrie hornej matrice

V okne „Top die Geometry“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a importujte súbor „**StubShaft_ConeTools****.igs**“ z knižnice geometrií DEFORM v adresári **/2D/LABS/**. Keďže táto geometria obsahuje viacero hraníc, systém zobrazí okno s upozornením týkajúce sa úpravy geometrie. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}), aby sa otvorilo okno na úpravu importovanej geometrie, ako je znázornené na obr. 2DFEL1.24.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0024.jpg' | relative_url }})

Import geometrie s viacerými hranicami pre hornú matricu

Vyberte druhú slučku a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}), aby ste odstránili **slučku 2**, ako je znázornené na obr. 2DFEL1.25. Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), čím zatvoríte editor geometrie. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0025.jpg' | relative_url }})

Úprava geometrie hornej matrice

### Sieťovanie hornej matrice

V okne na generovanie siete vytvorte sieť hornej formy s predvoleným počtom 1000 prvkov a pomerom rozmerov 3 pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obr. 2DFEL1.26. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0026.jpg' | relative_url }})

Vytvorenie siete pre lisovaciu formu

### Priradiť materiál k hornej matrici

V okne „Materiál hornej matrice“ vyberte materiál **AISI-H13**, ktorý chcete priradiť k hornej matrici, ako je znázornené na obr. 2DFEL1.27. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0027.jpg' | relative_url }})

Priradenie materiálu pre horný obrobok

### Priradenie BCC pre hornú matricu

V okne „Definovať BCC“ sa BCC typu „Výmena tepla s prostredím“ automaticky priradí ku všetkým hranám okrem osovej hrany. Kliknite na vetvu „Definované“ pod BCC typu „Výmena tepla s prostredím“, aby ste potvrdili definíciu BCC (pozri obr. 2DFEL1.28.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0028.jpg' | relative_url }})

Nastavenie okrajových podmienok pre hornú formu

### Priradenie ovládacích prvkov pohybu pre hornú matricu

V ovládacích prvkoch pohybu hornej matrice definujte hydraulický lis s hydraulickou rýchlosťou ako funkciu času a s definíciou obmedzenia sily v smere **-Y**, ako je znázornené na obr. 2DFEL1.29.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0029.jpg' | relative_url }})

Definícia hydraulického pohybu hornej formy

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_function..._button2.jpg' | relative_url }}) vedľa položky „rýchlosť“ a nastavte ho tak, aby sa ram v rozmedzí od 0 do 0,025 s pohyboval rýchlosťou 10 in/s a v rozmedzí od 0,02501 do 0,06 s rýchlosťou 8 in/s, keďže táto operácia začína po 5 sekundách prevádzky vzduchového prenosu; ak chce používateľ zachovať globálny čas pre definíciu funkcie, v ovládacích prvkoch simulácie musí byť pre definíciu funkcie zvolený globálny čas. Preto v tomto laboratórnom cvičení definujeme rýchlosť ako funkciu globálneho času, ako je znázornené na obr. 2DFEL1.30. T. j. v čase od 5 do 5,025 s sa ram pohybuje rýchlosťou 10 in/s a v čase od 5,02501 do 5,06 s sa ram pohybuje rýchlosťou 8 in/s. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) uzavrite definíciu.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0030.jpg' | relative_url }})

Funkcia definovania hydraulickej rýchlosti v globálnom čase

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}) vedľa položky „limit výkonu“, aby ste definovali krivku limitu výkonu, ako je znázornené na obr. 2DFEL1.31. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste definíciu uzavreli, a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno definície spodnej matrice.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0031.jpg' | relative_url }})

Definícia výkonového limitu pre hydraulický lis

### Definícia spodnej matrice

V okne definície spodnej formy nastavte typ objektu na **Rigid** a zadajte počiatočnú teplotu **300°** F, ako je znázornené na obr. 2DFEL1.32. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0032.jpg' | relative_url }})

Okno na definovanie spodnej matrice

### Import a úprava geometrie spodnej matrice

V okne „Geometria spodnej matrice“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a importujte súbor „**StubShaft_ConeTools****.igs**“ z cesty knižnice geometrií DEFORM **/2D/LABS/**. Keďže táto geometria obsahuje viacero hraníc, systém zobrazí okno s upozornením týkajúce sa úpravy geometrie. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}), aby sa otvorilo okno na úpravu importovanej geometrie, ako je znázornené na obr. 2DFEL1.33.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0033.jpg' | relative_url }})

Import geometrie s viacerými hranicami pre spodnú matricu

Vyberte prvú slučku a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}), aby ste vymazali slučku 1, ako je znázornené na obr. 2DFEL1.34. Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste uzavreli editor geometrie. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0034.jpg' | relative_url }})

Úprava geometrie spodnej matrice

### Sieťová spodná forma

V okne na generovanie siete vytvorte sieť spodnej formy s 1000 prvkami pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obr. 2DFEL1.35. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0035.jpg' | relative_url }})

Vytvorenie siete pre spodnú formu

### Priradiť materiál k spodnej matrici

V okne „Materiál spodnej formy“ vyberte materiál **AISI-H13**, aby ste ho priradili k spodnej forme, ako je znázornené na obr. 2DFEL1.27. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

### Priradenie BCC pre spodnú matricu

V okne „Definovať BCC“ sa všetkým hranám automaticky priradí BCC typu „Výmena tepla s prostredím“. Kliknutím na vetvu „Definované“ pod BCC typu „Výmena tepla s prostredím“ potvrďte definíciu BCC (pozri obr. 2DFEL1.36.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí okno definície objektu 4.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0036.jpg' | relative_url }})

Nastavenie okrajových podmienok pre spodnú formu

### Definícia vyhadzovača

V okne definície objektu 4 zmeňte názov objektu na „**Ejector**“ a zadajte počiatočnú teplotu **300** °F. Potvrďte typ objektu ako **tuhý** a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte. (pozri obr. 2DFEL1.37.)

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0037.jpg' | relative_url }})

Okno na definovanie vyhadzovacej matrice

### Vytvorenie geometrie vyhadzovača

V okne „Ejector die Geometry“ kliknite na popis akcie ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}), aby ste definovali geometrické body v tabuľke geometrie, ako je znázornené na obr. 2DFEL1.38. Po dokončení definície geometrických bodov kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zavreli editor geometrie, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0038.jpg' | relative_url }})

Import geometrie s viacerými hranicami pre vyhadzovaciu matricu

### Vytváranie siete vyhadzovača

V okne na generovanie siete vytvorte sieť ejektora s 1000 prvkami pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obr. 2DFEL1.39. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0039.jpg' | relative_url }})

Vytvorenie siete pre vyhadzovaciu formu

### Priradiť materiál k vyhadzovacej matrici

V okne „Materiál vyhadzovača“ vyberte materiál **AISI-H13**, aby ste ho priradili k vyhadzovaču, ako je znázornené na obr. 2DFEL1.27. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

### Priradenie BCC pre vyhadzovaciu matricu

V okne „Definovať BCC“ sa BCC typu „Výmena tepla s prostredím“ automaticky priradí ku všetkým hranám okrem osovej hrany. Kliknutím na vetvu „Definované“ pod BCC typu „Výmena tepla s prostredím“ potvrďte definíciu BCC (pozri obr. 2DFEL1.40.). Kliknite na vetvu **Sieť obrobku** v strome operácií, aby ste definovali sieť pre tvarovanie kužeľa.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0040.jpg' | relative_url }})

Nastavenie okrajových podmienok pre vyhadzovaciu maticu

### Definovanie siete obrobku pre tvarovanie kužeľa

V blízkosti vnútorného rohu medzi spodnou a hornou matricou pridáme okno hustoty siete, aby sme presnejšie zachytili stavovú premennú, a tiež nastavíme vynútené **prekreslenie siete** každých **20 krokov** s cieľom spresniť sieť. Zaškrtnite teda políčko „**Definovať nastavenia siete**“, aby sa zmeny uplatnili v momente, keď simulácia dosiahne bod prerobovania siete, a zaškrtnite tiež políčko „**Vykonávať prerobovanie siete pred touto operáciou**“, aby nové nastavenia siete platili od začiatku operácie tvárnenia. Vyberte kartu „**Váhovacie faktory**“, aby ste aktivovali okná hustoty siete tak, že oknám siete priradíte váhu 0,2 a nastavíte krivku hranice na 0,4, rozloženie deformácie na 0,2 a rozloženie rýchlosti deformácie na 0,2, ako je znázornené na obr. 2DFEL1.41.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0041.jpg' | relative_url }})

Nastavenie váhového koeficientu pre okná siete

Po nastavení váhy pre okná siete sa aktivuje záložka „Mesh windows“, ako je znázornené na obr. 2DFEL1.41. Teraz vyberte záložku „Mesh windows“, aby ste pridali okno hustoty siete, a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) na pridanie okna siete. Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) (zväčšenie podľa okna) alebo ![]({{ '/assets/icons/pre_icons/mo_zoom_icon.jpg' | relative_url }}) (dynamické zväčšenie) zväčšite spodný vnútorný roh formy v blízkosti miesta, kde potrebujeme pridať okno na obrobku. Pomocou nástrojov na definovanie okna (mnohouholník alebo obdĺžnik) definujte okno tak, ako je znázornené na obr. 2DFEL1.42. Definujte relatívnu veľkosť prvkov siete pre okno na hodnotu 0,00001 v porovnaní s prvkami mimo okna.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0042.jpg' | relative_url }})

Nastavenie okna hustoty siete pre obrobok pri tvárnení kužeľa

Vyberte kartu „Kritériá pregenerovania siete“ a nastavte **Maximálny prírastok kroku** na hodnotu **20**, aby sa počas operácie tvarovania kužeľa simulácia pregenerovala po každých 20 krokoch, ako je znázornené na obr. 2DFEL1.43. Kliknite na položku **Kontakt** v strome operácií, aby ste definovali vzťahy medzi objektmi.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0043.jpg' | relative_url }})

Kritériá núteného prepočítania siete používané pri tvarovaní kužeľa

### Definovanie vzťahov medzi objektmi

Vyberte typ kontaktu „užívateľ“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) (pozri obr. 2DFEL1.45.). Tým sa pridá vzťah medzi polotovarom, hornou matricou, spodnou matricou a vyhadzovačom. Keďže matrice sú tuhé a polotovar je plastický, horná, spodná a vyhadzovacia matrica sa považujú za hlavné a polotovar za podriadený. S cieľom predpovedať ohyb počas deformácie sa polotovaru priradí vlastný kontakt.

Vyberte vzťah **Horná matrica – Obrobok** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) upravte podmienky kontaktu. Na karte „Trenie“ (pozri obr. 2DFEL1.44.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné procesy tvárnenia.

Keďže ide o simuláciu tepelného tvárnenia a lisovacie formy sú z ocele, použite roletové menu a zo zoznamu vyberte možnosť „tepelné tvárnenie“. Hodnota trenia 0,25 sa nastaví automaticky. Na karte „Tepelné vlastnosti“ je predvolene nastavený koeficient prenosu tepla 0,004, čo je pre tvárnenie v poriadku.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0044.jpg' | relative_url }})

Okno na definovanie koeficientu trenia medzi objektmi

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna „Inter-Object“, keďže podmienky trenia sú pre všetky páry objektov rovnaké, Tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete použiť na skopírovanie vlastností rozhrania z prvých vzťahov, ktoré budú mať hodnotu trenia 0,25 a hodnotu koeficientu prenosu tepla 0,0004, ako je znázornené na obr. 2DFEL1.45. Keďže sa kontakt inicializuje a vygeneruje počas vytvárania databázy, zaškrtnite políčka „inicializovať“ a „vygenerovať“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0045.jpg' | relative_url }})

Definícia vzťahov medzi objektmi pri formovaní kužeľa

### Definovanie ovládacích prvkov zastavenia

V okne riadenia zastavenia vyberte kartu „Die Distance“ (Vzdialenosť medzi formami), aby ste nastavili hrúbku prebytku; simulácia sa zastaví, keď vzdialenosť medzi formami dosiahne hodnotu 0,025". Zadajte teda vzdialenosť **0,025**, vyberte smer Y a potom v zobrazenom okne vyberte bod na spodnom okraji hornej matrice a na hornom okraji spodnej matrice, ako je znázornené na obr. 2DFEL1.46. Po výbere bodov na maticiach je možné sledovať vzdialenosť medzi maticami, v tomto prípade je to približne 0,5". Ako riadiace prvky zastavenia možno použiť aj parametre procesu, ako sú maximálne zaťaženie primárnej matice, minimálna rýchlosť a maximálny zdvih, maximálne napätie v prvku a trvanie procesu; k dispozícii je tiež riadiaci prvok zastavenia na rovine, ktorý sa bežne používa pri valcovaní. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0046.jpg' | relative_url }})

Riadenie zastavenia matíc na základe vzdialenosti pri tvarovaní kužeľa

###  Nastavenie ovládacích prvkov kroku

Na karte „Krok“ vyberte definíciu kroku ako **Posun matrice** s hodnotou **0,005** ", ako je znázornené na obr. 2DFEL1.47.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0047.jpg' | relative_url }})

Krok určuje nastavenia pre operáciu tvarovania kužeľa

Vyberte kartu **simulačné kroky** a nastavte **počet krokov** na **100** a **krok pre ukladanie** nastavte na **10** pre posun primárnej matrice (t. j. hornej matrice, objekt č. 2 v tejto simulácii), ako je znázornené na obr. 2DFEL1.48.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0048.jpg' | relative_url }})

Definícia krokov simulácie tvarovania kužeľa

Vyberte kartu **Pokročilé**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Premenné**, aby ste pri aplikácii údajov funkcie mohli použiť globálny čas (pozri obr. 2DFEL1.49.), keďže sme globálny čas použili pri definícii funkcie rýchlosti hydraulického lisu.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0049.jpg' | relative_url }})

Výber globálneho času pre údaje o funkcii pri tvárnení kužeľov

Kliknite na kartu „Kritériá pre vytváranie novej siete“, aby ste si prezreli kritériá pre vytváranie novej siete obrobku definované v okne „Sieť obrobku“, ako je znázornené na obr. 2DFEL1.50.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0050.jpg' | relative_url }})

Kritériá pre vytvorenie novej siete pri operácii tvarovania kužeľa definované pre obrobok

Týmto je nastavenie operácie viacnásobného tvarovania v režime MO – Expert dokončené, keďže databáza pre operáciu tvarovania kužeľa sa vygeneruje počas simulácie. Na simuláciu úlohy prejdite na kartu Simulácia nad stromom objektov kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}). 

## Spustenie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 2DFEL1.51. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0054.jpg' | relative_url }})

Vyskočiace okno „Spustiť simuláciu“

Sledujte priebeh simulácie na kartách „Simulation Graphics“, „Simulation Message“ a „Simulation Log“ a uistite sa, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). (pozri obr. 2DFEL1.52.) Počas priebehu simulácie sledujte vplyv hustoty siete počas operácie tvarovania kužeľa, ako je znázornené na obr. 2DFEL1.52.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0051.jpg' | relative_url }})

Simulačný režim zobrazujúci priebeh formovania kužeľa

Po dokončení všetkých operácií sa v súbore protokolu simulácie zobrazí správa „MULTIPLE OPERATION COMPLETED.“; následne prejdite na kartu „Post“, kde si môžete prezrieť výsledky simulácie.

## Následné spracovanie

V zozname krokov postprocesora pod grafickou oblasťou sú uvedené čísla krokov dostupné z rôznych simulovaných operácií. Na kontrolu odozvy modelu je možné použiť súbor stavových premenných dostupných v ponuke „Post“. Upozorňujeme, že pre prvú operáciu sú k dispozícii iba tepelné údaje o obrobku. Výsledky deformácie sú viditeľné pri operácii tvarovania kužeľa. Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) (zväčšenie podľa okna) môžete zväčšiť kužeľovú časť obrobku, ako je znázornené na obr. 2DFEL1.53. Vďaka definícii okna hustoty siete je tiež viditeľná jemná sieť pre obrobok v spodnom vnútornom rohu hornej matrice.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0052.jpg' | relative_url }})

Postprocesor MO s variabilným obrysom zohľadňujúcim deformáciu pri kužeľovom tvare obrobku

Niektoré dôležité stavové premenné je možné vybrať priamo z okna „Post Tools“ a k ostatným sa dostanete cez dialógové okno „State Variable“ kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}).

Kliknite na graf ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) (zaťaženie – zdvih) a vyneste graf času (s) v závislosti od zaťaženia (klb), ako aj graf času (s) v závislosti od rýchlosti (in/s) pre hornú matricu. Sledujte zmenu rýchlosti v momente, keď zaťaženie prekročí krivku výkonového limitu; rýchlosť sa zmení z 10 in/sec na 8 in/sec, ako je znázornené na obr. 2DFEL1.54.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0053.jpg' | relative_url }})

Grafy „Čas vs. zaťaženie“ a „Čas vs. rýchlosť“ pre primárnu matricu (horná matrica)
