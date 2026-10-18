---
lang: sk
title: "Laboratórne cvičenie: 2D tvárnenie v riadenom režime"
---

# Laboratórium 2D tvárnenia v riadenom režime

V tomto laboratórnom cvičení si ukážeme, ako nastaviť typickú operáciu tvárnenia po ohreve v peci v režime vedeného postupu s viacerými operáciami (MO). Operácia tvárnenia je otvorené prostredie, v ktorom môže používateľ nastaviť akúkoľvek úlohu týkajúcu sa deformácie, prenosu tepla, difúzie a tepelného spracovania, avšak pre nových používateľov bude režim s návodom slúžiť ako sprievodca s jednoduchými a základnými funkciami pre ovládanie simulácie, generovanie siete, zastavenie a ovládanie krokov. Po zoznámení sa s programom DEFORM môže používateľ pre podrobnejšie štúdium využiť pokročilé funkcie v režime pre expertov.

V rámci tohto laboratórneho cvičenia sa pokúsime poukázať na rôzne vlastnosti systému v režime s vedením, ktoré môže používateľ využiť pri počiatočných štúdiách.

1.1. Vytvorenie novej úlohy a pridanie operácií

1.2. Operácia 1: Nastavenie vykurovania s prenosom tepla

1.3. Operácia 2: Tvarovanie

1.4. Spustenie simulácie

1.5. Následné spracovanie

## Vytvorenie nového problému a pridanie operácií

### Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Hlavné okno grafického rozhrania DEFORM

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte systém jednotiek pomocou prepínača „**Anglický**“, ako je znázornené na obr. 2DFGL1.1. Nastavte názov úlohy na „**Forming_Operation_in_Guided_Mode** “ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu deformácie.

Spustí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt, v ktorom bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**Forming_Operation_in_Guided_Mode**“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie. Otvorí sa sprievodca MO (pozri obr. 2DFGL1.2.). Ako prvú operáciu vyberte 2D operáciu prenosu tepla a zaškrtnite políčko na pridanie operácie prenosu tepla ako prvej operácie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste pokračovali v otváraní operácie.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0002.jpg' | relative_url }})

Okno na otvorenie nového projektu v nástroji MO Wizard

### Pridanie operácie tvarovania

Sprievodca viacerými operáciami otvorí nový projekt s jednou 2D operáciou prenosu tepla. Pridajte jednu operáciu tvarovania na tvarovanie kužeľa po prenose tepla vzduchom po dobu 5 sekúnd z pece do foriem zo zoznamu operácií v prehliadači kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ako je znázornené na obr. 2DFGL1.3.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0003.jpg' | relative_url }})

Pridanie formovacej operácie

## Operácia 1: Nastavenie vykurovania pri prenose tepla

Pri prvom procese prenosu tepla zmeňte názov procesu na „**Prenos vzduchom**“ dvojitým kliknutím na položku „Názov procesu“ v okne „Editor procesov“, ako je znázornené na obr. 2DFGL1.4, a po úprave stlačte klávesu **Enter** na klávesnici.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0004.jpg' | relative_url }})

Prvú operáciu nazvite „Letecký transfer“

### Výber typu geometrie

V tomto laboratórnom cvičení používame osovo symetrické geometrie, preto v okne typu geometrie zaškrtnite políčko **2D osovo symetrické**, ako je znázornené na obr. 2DFGL1.3., a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

### Výber typu prenosu tepla

Ako typ prenosu tepla pre prevádzku „Prenos vzduchom“ vyberte možnosť „**Prenos vzduchom**“, ako je znázornené na obr. 2DFGL1.5. Týmto sa nastavia predvolené nastavenia prenosu tepla pre režim kúrenia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0005.jpg' | relative_url }})

Výber typu prenosu tepla pre prenos vzduchom

### Nastavenie podmienok spracovania

Nastavte čas prenosu na 5 sekúnd pri teplote okolia 68 °F a predvolený koeficient konvekcie podľa obr. 2DFGL1.6. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0006.jpg' | relative_url }})

Nastavenia prevádzkových podmienok pre prenos vzduchu

### Vyberte ovládacie prvky simulácie pre prenos vzduchu

Je zaškrtnutá iba možnosť „Udržať iba režim prenosu tepla“, keďže sa modeluje iba prenos tepla, ako je znázornené na obr. 2DFGL1.7. Keď sa používateľ nachádza v okne ovládacích prvkov simulácie, aktivuje sa expertný režim (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) (pozri obr. 2DFGL1.7.), ktorý môže používateľ využiť na pokročilé funkcie. Keďže v tomto laboratórnom cvičení žiadne takéto funkcie nepoužívame, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0007.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre prenos vzduchu v riadenom režime

### Import materiálu pre obrobok

V okne „Material“ načítajte materiál **AISI-4120** z knižnice materiálov DEFORM, z kategórie **Steel**, pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To je možné vykonať tak, ako je znázornené na obr. 2DFGL1.8., kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Materiál je možné načítať aj zo zoznamu materiálov v Průzkumníku. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre otvorenie okien Materiál a Objekt.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0008.jpg' | relative_url }})

Import materiálu obrobku z knižnice DEFORM

### Definícia obrobku

V okne „Objekt obrobku“ ponechajte typ objektu ako „**Plast**“ a zadajte teplotu obrobku 1750 °F (pozri obr. 2DFGL1.9.). Pomocou možnosti „Importovať objekt zo súboru“ môžeme importovať údaje o objekte z kľúčového súboru alebo databázy a pomocou možnosti „Importovať objekt z knižnice“ môžeme importovať údaje o objekte z kľúčového súboru. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0009.jpg' | relative_url }})

Definícia objektu obrobku

### Vytvorenie geometrie obrobku

Na stránke „Geometria“ kliknite na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) (pozri [Fig. 2DFGL1.10.]()) a vytvorte **valec** s **polomerom****0,4** a **výškou****2,7**, ako je znázornené na obr. 2DFGL1.11. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0010.jpg' | relative_url }})

Okno s definíciami geometrie

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0011.jpg' | relative_url }})

Vytvorenie geometrie valca pre obrobok

### Vytvorenie siete obrobku

Vytvorte sieť s 1000 prvkami pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) (pozri obr. 2DFGL1.12.). V expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) je k dispozícii kompletná škála možností vytvárania sietí, ak potrebujete mať väčšiu kontrolu nad vytvorenou sieťou. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0012.jpg' | relative_url }})

Vytvorenie siete pre obrobok

###  Nastavenie materiálu obrobku

Ak chcete obrobku priradiť materiál, vyberte z okna materiálov materiál „**AISI-4120**“. Postupujte podľa obrázku 2DFGL1.13. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0013.jpg' | relative_url }})

Priradenie materiálu k obrobku

### Definovanie okrajových podmienok obrobku

Na stránke BCC skontrolujte, či je pre celý vonkajší povrch polotovaru predvolene priradená voľba „Výmena tepla s prostredím“ (ktorá nezahŕňa os, keďže tieto uzly sa nachádzajú vnútri objektu), a to kliknutím na položku „Definované“ v časti „Výmena tepla s prostredím“. Predvolené BCC sa priradia automaticky na základe výberu typu úlohy ako osovo symetrickej a simulačného režimu ako prenos tepla. (pozri obr. 2DFGL1.14.)

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0014.jpg' | relative_url }})

Definícia okrajových podmienok pre obrobok

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí okno „Ovládacie prvky krokov“, keďže nie je potrebné definovať ovládacie prvky pre polohovanie objektu ani pre teplotné zastavenie.

### Definovanie ovládacích prvkov krokov

Nastavte **počet simulačných krokov** na **50** s dĺžkou každého kroku **0,1** s a ukladajte **každých****5** krokov (pozri obr. 2DFGL1.15.). Nastavenia pokročilých ovládacích prvkov simulácie sú k dispozícii v expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do fázy generovania databázy.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0015.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre prenos vzduchu

### Vytvoriť databázu

V etape vytvárania databázy môže používateľ skontrolovať údaje potrebné na analýzu a pokračovať vo vytváraní databázy (pozri obr. 2DFGL1.16.). Pred vykonaním akejkoľvek z viacerých operácií je používateľ povinný vytvoriť databázu. Pre všetky nasledujúce operácie stačí nastaviť len procesné údaje a parametre simulácie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k ďalšej operácii „**Tvarovanie kužeľa**“.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0016.jpg' | relative_url }})

Okno na vytvorenie databázy pre prvú operáciu

## Operácia 2: Tvarovanie

Operácia tvarovania prebieha dovtedy, kým vzdialenosť medzi maticami nedosiahne hodnotu 0,025". Keďže obrobok prichádza z operácie vzduchového prenosu so svojou teplotnou históriou, vytvorte obrobok podľa údajov z objektu v databáze a pridajte ďalšie tri objekty pre razník, spodnú maticu a vyhadzovač, aby ste nastavili operáciu tvarovania kužeľa.

Pomenujte operáciu ako „**Tvorba kužeľa**“ dvojitým kliknutím na položku Názov operácie v editore operácií a stlačením klávesy Enter na klávesnici operáciu zatvorte. Potvrďte typ geometrie 2D osovo symetrická a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

### Vyberte nastavenia ovládacích prvkov simulácie pre tvarovanie kužeľa

V nastaveniach simulácie zaškrtnite oba simulačné režimy – „Deformácia“ aj „Prenos tepla“ – ako je znázornené na obr. 2DFGL1.17. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0017.jpg' | relative_url }})

Nastavenia riadenia simulácie pri tvarovaní kužeľa

### Materiál na výrobu foriem

V okne materiálov naimportujte materiál **AISI-H13** pre lisovacie formy z knižnice DEFORM v kategórii ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Die_material**, ako je znázornené na obr. 2DFGL1.18. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa otvorí okno objektov, a pridajte objekty.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0018.jpg' | relative_url }})

Import materiálu výsekových foriem z knižnice DEFORM

### Pridať objekty s kockami

V okne „Object“ pridajte 4 objekty tak, ako je znázornené na obr. 2DFGL1.19, keďže na operáciu tvarovania kužeľa budeme používať všetky tri matrice pri teplote **300°** F. Teraz vidíme, že strom objektov je rozbalený a obsahuje matrice, ktorých podrobnosti budeme teraz definovať. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0019.jpg' | relative_url }})

Pridávanie objektov na vytvorenie kužeľa

### Definícia obrobku

V okne definície obrobku vyberte typ objektu „**Načítať z databázy**“, ako je znázornené na obr. 2DFGL1.20. Kliknite na položku „Horná matrica“ v strome operácií, aby ste definovali matrice.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0020.jpg' | relative_url }})

Okno definície obrobku pri tvárnení kužeľa

### Definícia hornej matrice

V okne definície Top die nastavte typ objektu na „rigid“ a zadajte počiatočnú teplotu 300 °F, ako je znázornené na obr. 2DFGL1.21. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0021.jpg' | relative_url }})

Okno s definíciou hornej matrice pri tvárnení kužeľa

### Import a úprava geometrie hornej matrice

V okne „Top die Geometry“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a importujte súbor „**StubShaft_ConeTools.igs**“ z knižnice geometrií DEFORM v priečinku /2D/LABS/. Keďže táto geometria obsahuje viacero hraníc, systém zobrazí upozornenie týkajúce sa úpravy geometrie. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) otvoríte okno na úpravu importovanej geometrie, ako je znázornené na obr. 2DFGL1.22.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0022.jpg' | relative_url }})

Import geometrie s viacerými hranicami pre hornú matricu

Vyberte druhú slučku a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}), čím odstránite slučku 2, ako je znázornené na obr. 2DFGL1.23. Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), čím zatvoríte editor geometrie. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0023.jpg' | relative_url }})

Úprava geometrie hornej matrice

### Sieťovanie hornej matrice

V okne na generovanie siete vytvorte sieť hornej formy s 1000 prvkami pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obr. 2DFGL1.24. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0024.jpg' | relative_url }})

Vytvorenie siete pre lisovaciu formu

### Priradiť materiál k hornej matrici

V okne „Materiál hornej matrice“ vyberte materiál **AISI-H13**, ktorý chcete priradiť k hornej matrici, ako je znázornené na obr. 2DFGL1.25. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0025.jpg' | relative_url }})

Priradenie materiálu pre horný obrobok

### Priradenie BCC pre hornú maticu

V okne „Definovať BCC“ sa BCC „Výmena tepla s prostredím“ automaticky priradí ku všetkým hranám okrem osovej hrany. Kliknite na vetvu „Definované“ pod BCC „Výmena tepla s prostredím“, aby ste potvrdili definíciu BCC (pozri obr. 2DFGL1.26.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0026.jpg' | relative_url }})

Nastavenie okrajových podmienok pre hornú formu

### Priradenie ovládacích prvkov pohybu pre hornú matricu

V ovládacích prvkoch pohybu hornej matrice definujte **hydraulický****lis** s hydraulickou rýchlosťou ako funkciou času a s definíciou obmedzenia sily v smere **-Y**, ako je znázornené na obr. 2DFGL1.27.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0027.jpg' | relative_url }})

Definícia hydraulického pohybu hornej matrice

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_function.._button.jpg' | relative_url }}) vedľa položky „rýchlosť“ a nastavte tak, aby v rozmedzí od 0 do 0,025 s bola rýchlosť zdvihového piestu 10 in/s a v rozmedzí od 0,02501 do 0,06 s bola rýchlosť zdvihového piestu 8 in/s, ako je znázornené na obr. 2DFGL1.28. V predvolenom nastavení sa pri viacerých operáciách pre definície funkcie času zohľadňuje miestny čas, takže v tejto funkcii sa čas od 0 do 0,06 sekundy vzťahuje na operáciu formovania kužeľa. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste definíciu uzavreli.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0028.jpg' | relative_url }})

Hydraulická rýchlosť definovaná ako funkcia miestneho času

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}) vedľa položky „limit výkonu“, aby ste definovali krivku limitu výkonu, ako je znázornené na obr. 2DFGL1.29. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste definíciu uzavreli, a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno definície spodnej matrice.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0029.jpg' | relative_url }})

Definícia výkonového limitu pre hydraulický lis

### Definícia spodnej matrice

V okne definície spodnej matrice nastavte typ objektu na „tuhý“ a zadajte počiatočnú teplotu 300 °F, ako je znázornené na obr. 2DFGL1.30. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0030.jpg' | relative_url }})

Okno na definovanie spodnej matrice

### Import a úprava geometrie spodnej matrice

V okne „Geometria spodnej matrice“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a importujte súbor „**StubShaft_ConeTools.igs**“ z knižnice geometrií DEFORM v priečinku /2D/LABS/. Keďže táto geometria obsahuje viacero hraníc, systém zobrazí okno s otázkou, či chcete geometriu upraviť. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) otvoríte okno na úpravu importovanej geometrie, ako je znázornené na obr. 2DFGL1.31.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0031.jpg' | relative_url }})

Import geometrie s viacerými hranicami pre spodnú matricu

Vyberte prvú slučku a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}), aby ste odstránili slučku 1, ako je znázornené na obr. 2DFGL1.32. Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili editor geometrie. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0032.jpg' | relative_url }})

Úprava geometrie spodnej matrice

### Sieťová spodná forma

V okne na generovanie siete vytvorte sieť spodnej formy s 1000 prvkami pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obr. 2DFGL1.33. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0033.jpg' | relative_url }})

Vytvorenie siete pre spodnú formu

### Priradiť materiál k spodnej matrici

V okne „Materiál spodnej formy“ vyberte materiál **AISI-H13**, aby ste ho priradili k spodnej forme, ako je znázornené na obr. 2DFGL1.25. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

### Priradenie BCC pre spodnú matricu

V okne „Definovať BCC“ sa všetkým stranám automaticky priradí BCC „Výmena tepla s okolím“. Kliknutím na vetvu „Definované“ pod BCC „Výmena tepla s okolím“ potvrďte definíciu BCC (pozri obr. 2DFGL1.34.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí okno definície objektu 4.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0034.jpg' | relative_url }})

Nastavenie okrajových podmienok pre spodnú formu

### Definícia vyhadzovača

V okne definície objektu 4 zmeňte názov objektu na „**Ejector**“ a zadajte počiatočnú teplotu 300 °F. Potvrďte typ objektu ako tuhý a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte. (pozri obr. 2DFGL1.35.)

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0035.jpg' | relative_url }})

Okno na definovanie vyhadzovacej matrice

###  Vytvorenie geometrie vyhadzovača

V okne „Geometria vyhadzovača“ kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}), aby ste definovali geometrické body v tabuľke geometrie, ako je znázornené na obr. 2DFGL1.36. Po dokončení definície geometrie kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), čím zatvoríte editor geometrie, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0036.jpg' | relative_url }})

Import geometrie s viacerými hranicami pre vyhadzovaciu maticu

### Vytváranie siete vyhadzovača

V okne na generovanie siete vytvorte sieť ejektora s 1000 prvkami pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obr. 2DFGL1.37. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0037.jpg' | relative_url }})

Vytvorenie siete pre vyhadzovaciu formu

### Priradiť materiál k vyhadzovacej matrici

V okne „Materiál vyhadzovača“ vyberte materiál AISI-H13, aby ste ho priradili k vyhadzovaču, ako je znázornené na obr. 2DFGL1.25. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

### Priradenie BCC pre vyhadzovaciu matricu

V okne „Definovať BCC“ sa BCC „Výmena tepla s prostredím“ automaticky priradí k hranám s výnimkou osovej hrany. Kliknite na vetvu „Definované“ pod BCC „Výmena tepla s prostredím“, aby ste potvrdili definíciu BCC (pozri obr. 2DFGL1.38.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno s kontaktmi, keďže všetky objekty sú štandardne správne umiestnené.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0038.jpg' | relative_url }})

Nastavenie okrajových podmienok pre vyhadzovaciu maticu

### Definovanie vzťahov medzi objektmi

Vyberte typ kontaktu „užívateľ“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) (pozri obr. 2DFGL1.40.). Tým sa pridá vzťah medzi polotovarom, hornou maticou, spodnou maticou a vyhadzovačom. Keďže matrice sú tuhé a polotovar je plastický, horná, spodná a vyhadzovacia matrica sa považujú za hlavné a polotovar za podriadený. S cieľom predpovedať ohyb počas deformácie sa polotovaru priradí vlastný kontakt.

Vyberte vzťah **Horná matrica – obrobok** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) upravte podmienky kontaktu. Na karte „Trenie“ (pozri obr. 2DBL1.39.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné procesy tvárnenia.

Keďže ide o simuláciu tepelného tvárnenia a formy sú oceľové, použite roletové menu a zo zoznamu vyberte možnosť **tepelné tvárnenie**. Hodnota trenia **0,25** sa nastaví automaticky. Na karte „Thermal“ je predvolene nastavený koeficient prenosu tepla 0,004, čo je pre tvárnenie v poriadku.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0039.jpg' | relative_url }})

Okno na definovanie koeficientu trenia medzi objektmi

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna „Inter-Object“; keďže podmienky trenia sú rovnaké pre všetky páry objektov, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu na všetky ostatné. Po vykonaní tejto operácie budú mať všetky vzťahy trenie 0,25 a koeficient prenosu tepla 0,004, ako je znázornené na obr. 2DFGL1.40. Keďže sa kontakt inicializuje a vygeneruje počas vytvárania databázy, zaškrtnite políčka „inicializovať“ a „vygenerovať“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0040.jpg' | relative_url }})

Definícia vzťahov medzi objektmi pri formovaní kužeľa

### Definovanie ovládacích prvkov zastavenia

V okne riadenia zastavenia zaškrtnite políčko „Vzdialenosť medzi objektmi pri riadení zastavenia“ a nastavte ju na hodnotu 0,025". Následne v okne zobrazenia vyberte bod na spodnom okraji hornej matrice a na hornom okraji spodnej matrice a ako smer vyberte os Y, ako je znázornené na obr. 2DFGL1.41. Po výbere bodov na formách je možné pozorovať vzdialenosť medzi formami, v tomto prípade je to približne **0,5**". Pokiaľ ide o pokročilé možnosti zastavenia, pozrite si režim Expert (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})); keďže ho v tomto laboratórnom cvičení nepoužívame, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0041.jpg' | relative_url }})

Riadenie zastavenia matíc na základe vzdialenosti pri tvarovaní kužeľa

### Nastavenie ovládacích prvkov krokov

V okne nastavenia krokov nastavte **počet krokov** na **100** a **0,005** ” na jeden krok pohybu matrice, **krok prírastku na uloženie** nastavte na **10** pre primárnu matricu (ktorá je v tejto simulácii objektom číslo 2), ako je znázornené na obr. 2DFGL1.42. Pokročilé funkcie ovládania krokov a simulácie sú k dispozícii v režime Expert (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}))

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0042.jpg' | relative_url }})

Krok: Nastavenia pre tvarovanie kužeľa

Týmto je nastavenie viacerých tvárniacich operácií v režime MO – Guided dokončené, keďže databáza pre operáciu tvárnenia kužeľa sa vygeneruje počas simulácie. Na simuláciu úlohy prejdite na kartu „Simulácia“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}).

## Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 2DFGL1.43. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“ (od kroku -1), potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0043.jpg' | relative_url }})

Vyskočiace okno „Spustiť simuláciu“

Sledujte priebeh simulácie na kartách „Simulation Graphics“, „Simulation Message“ a „Simulation Log“ a uistite sa, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). (pozri obr. 2DFGL1.44.)

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0044.jpg' | relative_url }})

Simulačný režim zobrazujúci priebeh formovania kužeľa

Po dokončení všetkých operácií sa v súbore protokolu simulácie zobrazí správa „MULTIPLE OPERATION COMPLETED.“ a následne sa prejde na kartu „Post“, kde si môžete prezrieť výsledky simulácie.

## Následné spracovanie

V zozname krokov postprocesora pod grafickou oblasťou sú uvedené čísla krokov dostupné z rôznych simulovaných operácií. Na kontrolu odozvy modelu je možné použiť súbor stavových premenných dostupných v ponuke „Post“. Upozorňujeme, že pre prvú operáciu sú k dispozícii iba tepelné údaje o obrobku. Výsledky deformácie sú viditeľné pri operácii tvarovania kužeľa (pozri obr. 2DFGL1.45.). Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) (zväčšenie podľa okna) zväčšite časť obrobku v tvare kužeľa, ako je znázornené na obr. 2DFGL1.45.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0045.jpg' | relative_url }})

Postprocesor MO s variabilným obrysom zohľadňujúcim deformáciu pri kužeľovom tvare obrobku

Niektoré dôležité stavové premenné je možné vybrať priamo z okna „Post Tools“, k ostatným sa dostanete cez dialógové okno „State Variable“ kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}).

Kliknite na graf ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) (zaťaženie – zdvih) a vyneste graf času (s) v závislosti od zaťaženia (klb), ako aj graf času (s) v závislosti od rýchlosti (in/s) pre hornú maticu. Sledujte zmenu rýchlosti v momente, keď zaťaženie prekročí krivku výkonového limitu; rýchlosť sa zmení z 10 in/sec na 8 in/sec, ako je znázornené na obr. 2DFGL1.46.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0046.jpg' | relative_url }})

Grafy „Čas vs. zaťaženie“ a „Čas vs. rýchlosť“ pre primárnu matricu (horná matrica)
