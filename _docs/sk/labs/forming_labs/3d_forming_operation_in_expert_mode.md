---
lang: sk
title: "Operácia 3D tvarovania v laboratóriu v režime Expert"
---

# 3D tvarovanie v režime Expert

V tomto laboratórnom cvičení si ukážeme, ako nastaviť typickú operáciu tvárnenia obrobku po vyhrevaní v peci v expertnom režime viacerých operácií (MO). Operácia tvárnenia je otvorené prostredie, v ktorom môže používateľ nastaviť akýkoľvek problém týkajúci sa deformácie, prenosu tepla, difúzie a tepelného spracovania, avšak pre nových používateľov je k dispozícii režim s návodom, ktorý ich prevedie jednoduchými a základnými funkciami pre ovládanie simulácie, generovanie siete, zastavenie a ovládanie krokov. Po oboznámení sa s programom DEFORM môže používateľ pre podrobné štúdium využiť pokročilé funkcie v režime expert.

V rámci tohto cvičenia sa pokúsime predstaviť niekoľko funkcií systému v režime pre pokročilých, aby sme používateľa motivovali k využívaniu tohto režimu na podrobné štúdium.

1.1. Vytvorenie novej úlohy a pridanie operácií

1.2. Operácia 1: Nastavenie vykurovania s prenosom tepla

1.3. Operácia 2: Tvarovanie

1.4. Spustenie simulácie

1.5. Následné spracovanie

## Vytvorenie nového problému a pridanie operácií

### Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

Vyskakovacie okno „Nový problém“

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte systém jednotiek pomocou prepínača „**SI**“, ako je znázornené na obr. 3DFEL1.1. Názov úlohy definujte ako „****3D_Forming_Operation_in_Expert_Mode**** “ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu deformácie.

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom „Nový projekt“, ako je znázornené na obrázku [Fig. 3DFEL1.2](). Používateľ bude vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „****3D_Forming_Operation_in_Expert_Mode****“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie. Otvorí sa sprievodca MO (pozri obrázok [Fig. 3DFEL1.2.]()). Ako **prvú operáciu** vyberte operáciu **3D** **tepelný** **prenos** a **zaškrtnite políčko**, aby ste operáciu tepelného prenosu pridali ako prvú operáciu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste pokračovali v otváraní operácie.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0002.jpg' | relative_url }})

Okno na otvorenie nového projektu v nástroji MO Wizard

### Pridanie operácie tvarovania

Sprievodca viacerými operáciami otvorí nový projekt s jednou 3D operáciou prenosu tepla. Pridajte jednu operáciu tvárnenia pre „riadiaci čap“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ako je znázornené na obr. 3DFEL1.3.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0003.jpg' | relative_url }})

Pridanie formovacej operácie

## Operácia 1: Nastavenie vykurovacieho systému na prenos tepla

Pre prvú operáciu prenosu tepla zmeňte názov operácie na „**Prenos vzduchu**“ dvojitým kliknutím na názov operácie v okne Editor operácií, ako je znázornené na obr. 3DFEL1.4, a stlačte klávesu Enter na klávesnici.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0004.jpg' | relative_url }})

Prvú operáciu nazvite „Letecký transfer“

### Výber typu prenosu tepla

Pre prevádzku s prenosom vzduchom vyberte typ prenosu tepla „**Prenos vzduchom**“, ako je znázornené na obr. 3DFEL1.3. Tým sa nastavia predvolené nastavenia prenosu tepla pre režim kúrenia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

### Nastavenie podmienok spracovania

Nastavte **čas prenosu** na **4** s pri teplote okolia **20** °C a predvolený koeficient konvekcie tak, ako je znázornené na obr. 3DFEL1.5, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0005.jpg' | relative_url }})

Nastavenia prevádzkových podmienok pre prenos vzduchu

### Vyberte ovládacie prvky simulácie pre prenos vzduchu

V okne ovládacích prvkov simulácie sa aktivuje expertný režim (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) (pozri obr. 3DFEL1.6.); kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) na karte „Nástroje“ si môžete prezrieť funkcie ovládania simulácie v expertnom režime.

Na karte „Hlavné nastavenia“ nechajte zaškrtnutý iba režim „Prenos tepla“, keďže sa modeluje iba prenos tepla. Názov operácie, ktorý bol zmenený na „Prenos vzduchu“, sa tu zobrazuje tak, ako je to vidieť na obr. 3DFEL1.6. K dispozícii sú tu aj ďalšie pokročilé funkcie, ako napríklad krok, zastavenie, riešiteľ, podmienky procesu atď. Niektoré z týchto funkcií použijeme v neskoršej fáze nastavenia pri ovládaní siete, zastavovania a krokov. Ďalšie informácie o možnostiach ovládania simulácie nájdete v [Simulation Controls]({{ '/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0006.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre prenos vzduchu v expertnom režime

### Import materiálu pre obrobok

V okne „Material“ načítajte materiál „**DIN-41Cr4[1450-2200F(800-1200)]**“ z knižnice materiálov DEFORM, z kategórie **Steel**, pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To je možné vykonať tak, ako je znázornené na obr. 3DFEL1.7, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Materiál je možné načítať aj zo zoznamu materiálov v Průzkumníku. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno Obrobok.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0007.jpg' | relative_url }})

Import materiálu obrobku z knižnice DEFORM

### Definícia obrobku

V okne „Objekt obrobku“ ponechajte typ objektu ako „**Plast**“ a zadajte teplotu obrobku **1300** °C (pozri obr. 3DFEL1.8.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali a naimportovali geometriu obrobku.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0008.jpg' | relative_url }})

Definícia objektu obrobku

### Vytvorenie geometrie obrobku

Na stránke „Geometria“ pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) načítajte súbor „**ids_link_billet.stl**“ z inštalačnej zložky **/3D/LABS/**, ako je znázornené na obr. 3DFEL1.9. V tejto fáze je k dispozícii aj možnosť vytvorenia primitívnej geometrie.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0009.jpg' | relative_url }})

Import geometrie obrobku

Po importe akejkoľvek geometrie kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste geometriu skontrolovali; zobrazí sa okno na kontrolu geometrie, ktoré obsahuje prehľad geometrie objektu (pozri obr. 3DFEL1.10.). Objekt s uzavretým objemom by mal mať 1 plochu, 0 voľných hrán a 0 neplatných entít. Objekty, ktoré sú importované ako plochy a nie ako telesa, budú mať voľnú hranu, ale aj tak by mali mať len 1 plochu.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0010.jpg' | relative_url }})

Kontrola importovanej 3D geometrie

### Vytvorenie siete obrobku

V expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) je k dispozícii kompletná škála možností vytvárania sietí; pre prevádzku s prenosom vzduchu vytvorte sieť pomocou typu generovania **Absolute** **sieť** s minimálnou veľkosťou prvku 1,3333 mm a **pomerom veľkostí** **3**, ako je znázornené na obr. 3DFEL1.11. V ďalšom kroku použijeme iné okno hustoty siete a možnosti vynúteného prečlenenia. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) a v rozbaľovacom okne „Východiskové okrajové podmienky“, ktoré sa zobrazí s otázkou, či chcete priradiť východiskové okrajové podmienky, vyberte možnosť ![]({{ '/assets/icons/pre_icons/mo_no_button.jpg' | relative_url }}), pretože nechceme priradiť okrajovú podmienku „Výmena tepla s okolím“ (bcc) na všetky povrchy. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a pokračujte. Ďalšie informácie o možnostiach siete v expertnom režime nájdete v [3D Mesh]({{ '/docs/sk/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/' | relative_url }}).

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0011.jpg' | relative_url }})

Vytvorenie siete pre obrobok

### Priradiť materiál obrobku

Na priradenie materiálu k obrobku vyberte v okne materiálov materiál **„DIN-41Cr4[1450-2200F(800-1200)]**“. Postupujte podľa obrázku 3DFEL1.12. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0012.jpg' | relative_url }})

Priradenie materiálu k obrobku

### Definovanie okrajových podmienok obrobku

Keďže modelujeme polovicu riadiaceho ramena, musíme na zachovanie symetrie definovať okrajovú podmienku symetrickej roviny na konci dielu v smere +X a okrajovú podmienku výmeny tepla s okolím na všetkých povrchoch s výnimkou konca dielu v smere +X.

Pridajte **symetriu BCC** k koncovej rovine **+X** dielu tak, že vyberiete rovinu pomocou voľieb výberu na ľavej strane panela nástrojov BCC a kliknete na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) (Pridať BCC). Po pridaní sa pod položkou „Symmetry Planar“ zobrazia vektory symetrickej roviny, ako je znázornené na obr. 3DFEL1.13, čím sa zabezpečí správne definovanie BCC.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0013.jpg' | relative_url }})

Definícia okrajovej podmienky symetrie pre obrobok

Následne pridajte výmenu tepla s prostredím BCC tak, že vyberiete symetrickú rovinu pomocou možností výberu na ľavej strane panela nástrojov BCC a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) (Pridať BCC). Vyberte vetvu „Defined“, aby ste potvrdili definíciu BCC, ako je znázornené na obr. 3DFEL1.14.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0014.jpg' | relative_url }})

Definícia okrajových podmienok pre obrobok

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí okno „Ovládacie prvky zastavenia“, keďže nie je definované polohovanie objektu a je potrebné definovať ovládacie prvky tepelného zastavenia.

### Kontrola brzdových ovládačov

V okne riadenia zastavenia v expertnom režime môžeme vidieť, že čas prenosu 4 sekundy, ktorý bol definovaný v okne Podmienky procesu na začiatku nastavenia, sa tu premieta ako riadenie zastavenia na základe trvania procesu, ako je znázornené na obr. 3DFEL1.15. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0015.jpg' | relative_url }})

Ovládanie zastavenia prevádzky leteckej prepravy

### Definovanie ovládacích prvkov krokov

Nastavte typ definície kroku na **časový prírastok** s konštantnou hodnotou **0,1** s na karte **prírastok kroku**, ako je znázornené na obr. 3DFEL1.16.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0016.jpg' | relative_url }})

Definícia krokového prírastku pre prenos vzduchu

Vyberte kartu **simulačné kroky** a nastavte **počet simulačných krokov** na **50** s dĺžkou **0,1** sekundy na každý krok a ukladajte **každých** **5** krokov, ako je znázornené na obr. 3DFEL1.17. Ako bolo uvedené v definícii ovládacích prvkov simulácie, rôzne pokročilé nastavenia ovládacích prvkov simulácie sú k dispozícii aj v expertnom režime ovládania krokov (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli do fázy generovania databázy.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0017.jpg' | relative_url }})

Definícia krokov simulácie pre prenos vzduchu

### Vytvoriť databázu

V etape vytvárania databázy môže používateľ skontrolovať údaje potrebné na analýzu a pokračovať vo vytváraní databázy (pozri obr. 3DFEL1.18.). Ako prvú z viacerých operácií musí používateľ vytvoriť databázu. Pre všetky nasledujúce operácie stačí len nastaviť procesné údaje a parametre simulácie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k ďalšej operácii „**Riadenie****prepojenie**“.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0018.jpg' | relative_url }})

Okno na vytvorenie databázy pre prvú operáciu

## Operácia 2: Tvarovanie riadiaceho ramena

Operácia tvárnenia prebieha dovtedy, kým vzdialenosť medzi maticami nedosiahne hodnotu 400,8 mm. Keďže obrobok prichádza z operácie vzduchového prenosu so svojou teplotnou históriou, vytvorte obrobok podľa údajov z objektu v databáze a pridajte ďalšie dva objekty pre hornú a spodnú maticu, aby ste nastavili operáciu tvárnenia pomocou riadiaceho ramena.

Pomenujte operáciu ako „**Riadiaca tyč**“ dvojitým kliknutím na položku „Názov operácie“ v editore operácií a stlačením klávesy Enter na klávesnici operáciu zatvorte.

### Vyberte nastavenia ovládacích prvkov simulácie pre tvarovanie

V nastaveniach simulácie zaškrtnite oba simulačné režimy **Deformácia** a **Prenos tepla**, ako je znázornené na obr. 3DFEL1.19. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0019.jpg' | relative_url }})

Nastavenia riadenia simulácie pre tvárnenie

### Pridať objekty s kockami

V okne „Object“ pridajte 3 objekty, ako je znázornené na obr. 3DFEL1.20., keďže na operáciu tvárnenia použijeme obe matrice pri teplote 90 °C. Teraz vidíme, že strom objektov je rozbalený a obsahuje matrice, ktorých podrobnosti budeme teraz definovať. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0020.jpg' | relative_url }})

Pridávanie objektov na tvarovanie

### Definícia obrobku

V okne definície obrobku vyberte typ objektu „**Načítať z databázy**“, ako je znázornené na obr. 3DFEL1.21. Po definovaní foriem nastavíme hustotu siete pre obrobok na širšom konci symetrického riadiaceho ramena, preto kliknite na položku „Top Die“ v strome operácií, aby ste definovali formy.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0021.jpg' | relative_url }})

Okno definície obrobku v procese tvárnenia

### Definícia hornej matrice

V okne definície Top die nastavte typ objektu na **rigid** a zadajte počiatočnú teplotu **90** °C, ako je znázornené na obr. 3DFEL1.22. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0022.jpg' | relative_url }})

Okno s definíciou hornej matrice pri tvárnení

### Import geometrie hornej matrice

V okne „Top die Geometry“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a importujte súbor „**Ids_link_top****.stl'** z cesty ku knižnici geometrií DEFORM **/3D/LABS/** (pozri obr. 3DFEL1.23.). Skontrolujte importovanú geometriu tak, ako bolo vysvetlené skôr v prípade geometrie obrobku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno pohybu hornej matrice.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0023.jpg' | relative_url }})

Import geometrie s viacerými hranicami pre hornú matricu

### Priradenie ovládacích prvkov pohybu pre hornú matricu

V ovládacích prvkoch pohybu hornej matrice definujte **hydraulický lis** s hydraulickou **rýchlosťou** ako **funkciu času** (miestneho času) v smere **-Z**, ako je znázornené na obr. 3DFEL1.24.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0024.jpg' | relative_url }})

Definícia hydraulického pohybu hornej matrice

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_function..._button2.jpg' | relative_url }}) vedľa položky „rýchlosť“ a nastavte tak, aby v rozmedzí od 0 do 2,04 s lis bežal rýchlosťou 10 mm/s a v rozmedzí od 2,0401 do 4 s rýchlosťou 8 mm/s, keďže táto operácia začína po 4 sekundách prevádzky vzduchového prenosu; ak chce používateľ zachovať globálny čas pre definíciu funkcie, v ovládacích prvkoch simulácie musí byť pre definíciu funkcie zvolený globálny čas. V tomto laboratórnom cvičení teda definujeme funkciu rýchlosti globálneho času tak, ako je znázornené na obr. 3DFEL1.25. To znamená, že v rozmedzí od 4 do 6,04 s lis beží rýchlosťou 10 mm/s a v rozmedzí od 6,0401 do 8,0 s lis beží rýchlosťou 8 mm/s. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste uzavreli definíciu, a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno definície spodnej matrice.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0025.jpg' | relative_url }})

Hydraulická rýchlosť definovaná ako funkcia miestneho času

### Definícia spodnej matrice

V okne definície spodnej formy nastavte typ objektu na **tuhý** a zadajte počiatočnú **teplotu** **90** °C, ako je znázornené na obr. 3DFEL1.26. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0026.jpg' | relative_url }})

Okno na definovanie spodnej matrice

### Import geometrie spodnej matrice

V okne „Geometria spodnej formy“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a importujte súbor „**ids_link_bottom.stl**“ z cesty knižnice geometrií DEFORM /3D/LABS/ (pozri obr. 3DFEL1.27). Skontrolujte importovanú geometriu podľa pokynov uvedených vyššie pre geometriu obrobku. Kliknite na vetvu **obrobok** v strome operácií, aby ste otvorili okno pre definovanie siete obrobku.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0027.jpg' | relative_url }})

Import geometrie s viacerými hranicami pre spodnú matricu

### Definovanie siete obrobku pre operáciu tvárnenia

Na väčšom konci symetrického riadiaceho ramena pridáme okno hustoty siete, aby sme presnejšie zachytili stavovú premennú a tok kovu. Takisto nastavíme vynútené prečlenenie siete každých 50 krokov, aby sme sieť pravidelne spresňovali. Na definovanie nastavení siete zaškrtnite políčko „**Definovať nastavenia siete**“ na stránke Sieť obrobku a zaškrtnite tiež políčko „**Vykonávať prečlenenie pred touto operáciou**“, aby ste mali od začiatku operácie tvárnenia odlišnú sieť. Vyberte kartu „**Váhovacie faktory**“, aktivujte okná hustoty siete nastavením váhového faktora na 0,2 pre okná siete a nastavte váhový faktor zakrivenia hranice na 0,4, váhový faktor rozloženia deformácie na 0,2 a váhový faktor rozloženia rýchlosti deformácie na 0,2, ako je znázornené na obr. 3DFEL1.28.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0028.jpg' | relative_url }})

Nastavenia váhových koeficientov pre okná siete

Po nastavení váhového koeficientu pre okná siete sa aktivuje karta „Mesh windows“, ako je znázornené na obr. 3DFEL1.28. Teraz vyberte kartu „Mesh windows“, aby ste mohli pridať okná siete a definovať ich nastavenia. Na umiestnenie okien siete potrebujeme spodnú matricu spolu s obrobkom, preto vyberte spodnú matricu a obrobok, ktoré sa majú zobraziť, pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}) (režim definovaný používateľom) pod stromom objektov. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) na karte „Mesh windows“ (Okná siete), aby ste pridali nové okno siete, z typov okien siete vyberte typ „Hollow mesh density“ (Hustota dutej siete) a umiestnite okno nad stredom veľkého konca spodnej matrice, ako je znázornené na obr. 3DFEL1.29, a určte veľkosť prvkov v rámci okna na hodnotu 2,0 v porovnaní s prvkami mimo okna.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0029.jpg' | relative_url }})

Pridanie okna pre nastavenie hustoty siete pre obrobok pri operácii tvárnenia

Znovu kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}) (režim definovaný používateľom), aby ste zapli zobrazenie hornej matrice spolu s obrobkom a spodnou matricou, a potom pretiahnite okno nahor tak, aby pokrývalo celú výšku obrobku, ako je znázornené na obr. 3DFEL1.30.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0030.jpg' | relative_url }})

Umiestnenie okna s hustotou siete

Vyberte kartu **kritériá premenovania siete**** a nastavte **maximálny** **prírastok kroku** na hodnotu **50**, aby simulácia prebiehala po každých 50 krokoch pri operácii tvarovania kužeľa, ako je znázornené na obr. 3DFEL1.31. Kliknite na položku „Plánované polohovanie“ v strome operácií, aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0031.jpg' | relative_url }})

Kritériá núteného prepočítania siete používané pri tvarovaní

### Definícia plánovaného polohovania

Matrice sú štandardne v správnej polohe. Ak sa chcete uistiť, že sú správne umiestnené, definujte plánovanú polohu hornej a dolnej matrice vo vzťahu k obrobku metódou kolízie v smere -Z, resp. +Z, ako je znázornené na obr. 3DFEL1.32. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0032.jpg' | relative_url }})

Plánované polohovanie hornej a spodnej matrice

### Definovanie vzťahov medzi objektmi

Vyberte typ kontaktu „užívateľ“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) (pozri obr. 3DFEL1.35.). Tým sa pridá vzťah medzi sochárom, hornou matricou a spodnou matricou. Keďže matrice sú tuhé a sochár je plastický, horná a spodná matrica sa považujú za hlavné a sochár za podriadený.

Zvýraznite vzťah medzi hornou matricou a obrobkom a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) upravte podmienky kontaktu. Na karte „Trenie“ (pozri obr. 3DFEL1.33.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné tvárniace procesy.

Keďže ide o simuláciu tvárnenia za tepla a formy sú z ocele, použite roletové menu a zo zoznamu vyberte možnosť **Tvárnenie za tepla (s mazáním)**. Hodnota trenia **0,3** sa nastaví automaticky.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0033.jpg' | relative_url }})

Definícia koeficientu trenia medzi objektmi pri horúcom kovaniu

Na karte **tepelná** vyberte z roletového menu možnosť „Typ tvárnenia“; tým sa pridá predvolená hodnota koeficientu prenosu tepla **5** pre tvárnenie, ako je znázornené na obr. 3DFEL1.34.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0034.jpg' | relative_url }})

Definícia koeficientu prenosu tepla medzi objektmi pri tvárnení

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna „Inter-Object“; keďže podmienky trenia a prenos tepla medzi objektmi sú rovnaké pre všetky páry objektov, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných. Po vykonaní tejto operácie budú mať všetky vzťahy koeficient trenia **0,3** a koeficient prenosu tepla **5**, ako je znázornené na obr. 3DFEL1.35. Keďže sa kontakt inicializuje a vygeneruje počas vytvárania databázy, zaškrtnite políčka „Initialize“ a „Generate“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0035.jpg' | relative_url }})

Definícia vzťahu medzi objektmi pre tvorbu

### Definovanie ovládacích prvkov zastavenia

V okne riadenia zastavenia vyberte kartu **Vzdialenosť medzi formami**, aby ste nastavili, kedy má vzdialenosť medzi formami dosiahnuť hodnotu 11,0 mm. Zadajte teda vzdialenosť **11,0**, vyberte smer **Z** a potom v zobrazenom okne vyberte bod na veľkom konci, v strede hornej a dolnej dutiny matrice, ako je znázornené na obr. 3DFEL1.36. Po výbere bodov na maticiach je možné sledovať vzdialenosť medzi maticami, v tomto prípade je to približne 51,8. Ako riadiace prvky zastavenia možno použiť aj parametre procesu, ako sú maximálne zaťaženie primárnej matice, minimálna rýchlosť a maximálny zdvih, maximálne napätie v prvku a trvanie procesu; k dispozícii je aj riadiaci prvok zastavenia na rovine, ktorý sa bežne používa pri valcovacích operáciách. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0036.jpg' | relative_url }})

Riadenie zastavenia matíc na základe vzdialenosti pri tvárnení

### Nastavenie ovládacích prvkov krokov

Na karte **Krok** **Prírastok** vyberte definíciu kroku ako **Posun matrice** **0,2** mm, ako je znázornené na obr. 3DFEL1.37.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0037.jpg' | relative_url }})

Krok určuje nastavenia pre operáciu tvárnenia

Vyberte kartu **simulačné** **kroky** a nastavte **počet** **krokov** na **500** a **krok** **inkrementu** **na** **10** pre posun primárnej matrice (t. j. hornej matrice, objekt č. 2 v tejto simulácii), ako je znázornené na obr. 3DFEL1.38.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0038.jpg' | relative_url }})

Definícia krokov simulácie tvárnenia

Vyberte kartu **Pokročilé** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Premenné**, aby ste mohli zvoliť **globálny** čas, ktorý sa má použiť pre údaje funkcie (pozri obr. 3DFEL1.39.), keďže sme globálny čas použili pri definícii funkcie rýchlosti hydraulického lisu.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0039.jpg' | relative_url }})

Výber globálneho času pre údaje o funkcii pri tvárnení kužeľov

Kliknite na kartu **Kritériá** **pregenerovania siete**, aby ste si prezreli kritériá pregenerovania siete obrobku definované v okne siete obrobku, ako je znázornené na obr. 3DFEL1.40.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0040.jpg' | relative_url }})

Kritériá pre vytvorenie novej siete pri operácii tvarovania definované pre obrobok

Keďže sa počas simulácie vytvorí databáza pre operáciu tvarovania kužeľa, týmto je nastavenie viacerých tvarovacích operácií v režime MO – Expert dokončené. Na simuláciu problému prejdite na kartu „Simulácia“ nad stromom objektov. (Pozri obr. 3DFEL1.42.)

## Spustenie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 3DFEL1.41.Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0041.jpg' | relative_url }})

Vyskočiace okno „Spustiť simuláciu“

Sledujte priebeh simulácie na kartách „Simulation Graphics“, „Simulation Message“ a „Simulation Log“ a uistite sa, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). (Pozri obr. 3DFEL1.42.)

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0042.jpg' | relative_url }})

Simulačný režim zobrazujúci aktuálny stav formovania

Po dokončení všetkých viacnásobných operácií sa v súbore protokolu simulácie zobrazí správa „MULTIPLE OPERATION COMPLETED.“; následne prejdite na kartu „Post“, kde si môžete prezrieť výsledky simulácie.

## Následné spracovanie

V postprocesore sa v zozname krokov pod grafickou oblasťou zobrazujú čísla krokov dostupné z rôznych simulovaných operácií. Na kontrolu odozvy modelu je možné použiť súbor stavových premenných dostupných v ponuke „Post“. Upozorňujeme, že pre prvú operáciu sú k dispozícii iba tepelné údaje o obrobku. Výsledky deformácie sú viditeľné pri operácii tvárnenia riadiaceho ramena (pozri obr. 3DFEL1.43.). Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_zoom_icon.jpg' | relative_url }}) (zväčšenie podľa okna) zväčšite kužeľovú časť obrobku, ako je znázornené na obr. 3DFEL1.43.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0043.jpg' | relative_url }})

Deformačne efektívny variabilný obrys pri kužeľovom tvare obrobku

Niektoré dôležité stavové premenné je možné vybrať priamo z okna „Post Tools“ a k ostatným sa dostanete cez dialógové okno „State Variable“ kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}).

Kliknite na ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) **Graf** (zaťaženie – zdvih) a vytvorte graf času (s) v závislosti od zaťaženia (klb) a tiež graf času (s) v závislosti od rýchlosti (in/s) pre hornú matricu. Všimnite si zmenu rýchlosti po deformácii o 20,4 mm z 10 in/sec na 8 in/sec, ako je znázornené na obr. 3DFEL1.44.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0044.jpg' | relative_url }})

Grafy „Čas vs. zaťaženie“ a „Čas vs. rýchlosť“ pre primárnu matricu (horná matrica)
