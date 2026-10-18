---
lang: sk
title: "Laboratórne cvičenie na 3D tvárnenie v režime s vedením"
---

# 3D tvarovanie v režime s vedením

V tomto laboratórnom cvičení si ukážeme, ako nastaviť typickú operáciu tvárnenia obrobku po vyhrevaní v peci v režime vedeného viacerých operácií (MO). Operácia tvárnenia je otvorené prostredie, v ktorom môže používateľ nastaviť akúkoľvek úlohu týkajúcu sa deformácie, prenosu tepla, difúzie a tepelného spracovania, avšak pre nových používateľov bude režim s návodom slúžiť ako sprievodca s jednoduchými a základnými funkciami pre ovládanie simulácie, generovanie sietí, zastavenie a riadenie krokov. Po zoznámení sa s programom DEFORM môže používateľ pre podrobnejšie štúdium využiť pokročilé funkcie v režime pre expertov.

V rámci tohto laboratórneho cvičenia sa pokúsime poukázať na rôzne vlastnosti systému v režime s vedením, ktoré môže používateľ využiť pri počiatočných štúdiách.

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

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte systém jednotiek „**SI**“, ako je znázornené na obrázku [Fig. 3DFGL1.1.](). Zadajte názov úlohy ako „**3D_Forming_Operation_in_Guided_Mode** “ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu deformácie.

Otvorí sa sprievodca viacerými operáciami, v tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**3D_Forming_Operation_in_Guided_Mode**“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie. Otvorí sa sprievodca MO (pozri obr. 3DFGL1.2.). Vyberte **prvú operáciu** ako operáciu **3D** **tepelného** **prenosu** a **zaškrtnite políčko**, aby ste operáciu tepelného prenosu pridali ako prvú operáciu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste pokračovali v otváraní operácie.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0002.jpg' | relative_url }})

Okno na otvorenie nového projektu v nástroji MO Wizard

### Pridanie operácie tvarovania

Sprievodca MO otvorí nový projekt s jednou 3D operáciou prenosu tepla. Pridajte **jednu** **tvarovaciu** **operáciu** pre „riadiaci čap“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ako je znázornené na obr. 3DFGL1.3.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0003.jpg' | relative_url }})

Pridanie formovacej operácie

## Úloha 1: Nastavenie vykurovacieho systému pre prenos tepla

Pre prvú operáciu prenosu tepla zmeňte názov operácie na „**Prenos vzduchu**“ dvojitým kliknutím na názov operácie v okne Editor operácií, ako je znázornené na obr. 3DFGL1.4, a stlačte klávesu Enter na klávesnici.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0004.jpg' | relative_url }})

Prvú operáciu nazvite „Letecký transfer“

### Výber typu prenosu tepla

Pre prevádzku s prenosom vzduchom vyberte typ prenosu tepla „**Prenos vzduchom**“, ako je znázornené na obr. 3DFGL1.3. Tým sa nastavia predvolené nastavenia prenosu tepla pre režim kúrenia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

### Nastavenie podmienok spracovania

Nastavte čas prenosu na 4 s pri teplote okolia **20** °C a predvolený koeficient konvekcie podľa obr. 3DFGL1.5. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0005.jpg' | relative_url }})

Nastavenia prevádzkových podmienok pre prenos vzduchu

### Vyberte ovládacie prvky simulácie pre prenos vzduchu

Nechajte zaškrtnutý len režim „Heat Transfer“, pretože sa modeluje iba prenos tepla, ako je znázornené na obr. 3DFGL1.6. Pre pokročilé funkcie môže používateľ využiť expertný režim ovládacích prvkov simulácie (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Keďže v tomto cvičení žiadne takéto funkcie nepoužívame, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0006.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre prenos vzduchu v riadenom režime

### Import materiálu pre obrobok

V okne „Material“ načítajte materiál „**DIN-41Cr4[1450-2200F(800-1200)]**“ z knižnice materiálov DEFORM, z kategórie **Steel**, pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To je možné vykonať tak, ako je znázornené na obr. 3DFGL1.7, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Materiál je možné načítať aj zo zoznamu materiálov v Průzkumníku. Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre okno Materiál a objekt, keďže v prípade prevádzky s prenosom tepla vzduchom nás zaujíma iba prenos tepla obrobku vo vzduchu.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0007.jpg' | relative_url }})

Import materiálu obrobku z knižnice DEFORM

### Definícia obrobku

V okne „Objekt obrobku“ ponechajte typ objektu ako „**Plast**“ a zadajte teplotu obrobku **1300** °C (pozri obr. 3DFGL1.8.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali a naimportovali geometriu obrobku.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0008.jpg' | relative_url }})

Definícia objektu obrobku

### Vytvorenie geometrie obrobku

Na stránke Geometria pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) naimportujte súbor „**ids_link_billet.stl**“ z inštalačnej zložky /3D/LABS/, ako je znázornené na obr. 3DFGL1.9. V tejto fáze je k dispozícii aj možnosť vytvorenia primitívnej geometrie.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0009.jpg' | relative_url }})

Import geometrie obrobku

Po importe akejkoľvek geometrie kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste geometriu skontrolovali; zobrazí sa okno na kontrolu geometrie, ktoré obsahuje prehľad geometrie objektu (pozri obr. 3DFGL1.10.). Objekt s uzavretým objemom by mal mať 1 plochu, 0 voľných hrán a 0 neplatných entít. Objekty, ktoré sú importované ako plochy a nie ako telesa, budú mať voľnú hranu, ale aj tak by mali mať len 1 plochu.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0010.jpg' | relative_url }})

Kontrola importovanej 3D geometrie

### Vytvorenie siete obrobku

Vytvorte sieť s použitím 32 000 prvkov (pozri obr. 3DFGL1.11.). V expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) je k dispozícii aj kompletná škála možností vytvárania sietí, ak potrebujete mať väčšiu kontrolu nad vytvorenou sieťou. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0011.jpg' | relative_url }})

Vytvorenie siete pre obrobok

### Priradiť materiál obrobku

Na priradenie materiálu k obrobku vyberte v okne materiálov materiál „**DIN****-41Cr4[1450-2200F(800-1200)]**“. Postupujte podľa obrázku 3DFGL1.12. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0012.jpg' | relative_url }})

Priradenie materiálu k obrobku

### Definovanie okrajových podmienok obrobku

Na stránke BCC skontrolujte predvolenú hraničnú podmienku „Výmena tepla s okolím“ (Heat exchange with Environment BCC), ktorá je priradená k celému vonkajšiemu povrchu polotovaru, avšak v tomto laboratórnom cvičení modelujeme iba polovicu riadiaceho ramienka. Aby sme teda zabezpečili symetriu, musíme definovať okrajovú podmienku symetrickej roviny na konci súčiastky v smere +X a okrajovú podmienku výmeny tepla s prostredím na všetkých povrchoch okrem konca súčiastky v smere +X.

Pridajte **symetriu** **BCC** k koncovej rovine **+X** dielu tak, že vyberiete rovinu pomocou možností výberu na ľavej strane panela nástrojov BCC a kliknete na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) (Pridať BCC). Po pridaní sa vektory symetrickej roviny zobrazia pod položkou Symetrická rovina, ako je znázornené na obr. 3DFGL1.13. Aby ste zaistili správne definovanie BCC.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0013.jpg' | relative_url }})

Definícia okrajovej podmienky symetrie pre obrobok

Odstráňte automaticky definovanú výmenu tepla s okolím (BCC) tak, že v časti „Výmena tepla s okolím“ vyberiete vetvu „Definované“ a kliknete na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_bcc_button.jpg' | relative_url }}) (Odstrániť BCC). Následne pre výmenu tepla s prostredím BCC vyberte celú časť objektu s výnimkou roviny symetrie pomocou možností výberu na ľavej strane panela nástrojov BCC a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) (Pridať BCC). Vyberte vetvu „Definované“, aby ste potvrdili definíciu BCC, ako je znázornené na obr. 3DFGL1.14.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0014.jpg' | relative_url }})

Definícia okrajovej podmienky pre obrobok

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí okno „Ovládacie prvky krokov“, keďže nie je potrebné definovať ovládacie prvky pre polohovanie objektu a teplotné zastavenie.

### Definovanie ovládacích prvkov krokov

Nastavte **počet simulačných krokov** na **50**, pričom dĺžka každého kroku je **0,1** s a **uloženie sa vykonáva každých** **5** krokov (pozri obr. 3DFGL1.15.). Nastavenia pokročilých ovládacích prvkov simulácie sú k dispozícii v expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do fázy generovania databázy.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0015.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre prenos vzduchu

### Vytvoriť databázu

V etape vytvárania databázy môže používateľ skontrolovať údaje potrebné na analýzu a pokračovať vo vytváraní databázy (pozri obr. 3DFGL1.16.). Ako prvú z viacerých operácií musí používateľ vytvoriť databázu. Pre všetky nasledujúce operácie stačí len nastaviť procesné údaje a parametre simulácie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k ďalšej operácii „Tvarovanie kužeľa“.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0016.jpg' | relative_url }})

Okno na vytvorenie databázy pre prvú operáciu

## Operácia 2: Tvarovanie riadiaceho ramena

Operácia tvárnenia prebieha dovtedy, kým vzdialenosť medzi maticami nedosiahne hodnotu 400,8 mm. Keďže obrobok prichádza z operácie vzduchového prenosu so svojou teplotnou históriou, vytvorte obrobok podľa údajov z objektu v databáze a pridajte ďalšie dva objekty pre hornú a spodnú maticu, aby ste nastavili operáciu tvárnenia pomocou riadiaceho ramena.

Pomenujte operáciu ako „**Riadiaca tyč**“ dvojitým kliknutím na položku „Názov operácie“ v editore operácií a stlačením klávesy Enter na klávesnici operáciu zatvorte.

### Vyberte nastavenia ovládacích prvkov simulácie pre tvarovanie

V nastaveniach simulácie zaškrtnite oba simulačné režimy – „Deformácia“ aj „Prenos tepla“ – ako je znázornené na obr. 3DFGL1.17. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno s objektmi, a pridajte objekty, keďže nebudeme simulovať tepelné výpočty formy a nie je potrebné definovať žiadny materiál pre formy.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0017.jpg' | relative_url }})

Nastavenia riadenia simulácie pre tvárnenie

### Pridať objekty s kockami

V okne „Object“ pridajte 3 objekty, ako je znázornené na obr. 3DFGL1.18., keďže na operáciu tvárnenia použijeme obe matrice pri teplote 90 °C. Teraz vidíme, že strom objektov je rozbalený a obsahuje matrice, ktorých podrobnosti budeme teraz definovať. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0018.jpg' | relative_url }})

Pridávanie objektov na tvarovanie

### Definícia obrobku

V okne definície obrobku vyberte typ objektu „**Načítať z databázy**“, ako je znázornené na obr. 3DFGL1.19. Kliknite na položku „Horná matrica“ v strome operácií, aby ste definovali matrice.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0019.jpg' | relative_url }})

Okno definície obrobku v procese tvárnenia

### Definícia hornej matrice

V okne definície Top die nastavte typ objektu na **rigid** a zadajte počiatočnú teplotu **90** °C, ako je znázornené na obr. 3DFGL1.20. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0020.jpg' | relative_url }})

Okno s definíciou hornej matrice pri tvárnení

### Import geometrie hornej matrice

V okne „Top die Geometry“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a načítajte súbor „**Ids_link_top****.stl**“ z adresára knižnice geometrií DEFORM /3D/LABS/ (pozri obr. 3DFGL1.21.). Skontrolujte importovanú geometriu tak, ako bolo vysvetlené skôr v prípade geometrie obrobku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno pohybu hornej matrice.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0021.jpg' | relative_url }})

Import geometrie s viacerými hranicami pre hornú matricu

### Priradenie ovládacích prvkov pohybu pre hornú matricu

V ovládacích prvkoch pohybu hornej matrice definujte **hydraulický** **lis** s hydraulickou **rýchlosťou** ako **funkciu času** (miestneho času) v smere **-Z**, ako je znázornené na obr. 3DFGL1.22.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0022.jpg' | relative_url }})

Definícia hydraulického pohybu hornej matrice

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_function..._button2.jpg' | relative_url }}) vedľa položky „rýchlosť“ a nastavte tak, aby v rozmedzí od 0 do 2,04 s lis bežal rýchlosťou 10 mm/s a v rozmedzí od 2,0401 do 4 s rýchlosťou 8 mm/s, ako je znázornené na obr. 3DFGL1.23. V predvolenom nastavení sa pri viacerých operáciách v definíciách funkcie času zohľadňuje miestny čas, takže v tejto funkcii sa čas od 0 do 4 sekúnd vzťahuje na operáciu tvárnenia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste uzavreli definíciu, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno definície spodnej matrice.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0023.jpg' | relative_url }})

Hydraulická rýchlosť definovaná ako funkcia miestneho času

### Definícia spodnej matrice

V okne definície spodnej formy nastavte typ objektu na **tuhý** a zadajte počiatočnú teplotu **90** °C, ako je znázornené na obr. 3DFGL1.24. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0024.jpg' | relative_url }})

Okno na definovanie spodnej matrice

### Import geometrie spodnej matrice

V okne „Geometria spodnej matrice“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a importujte súbor „**ids_link_bottom.stl**“ z knižnice geometrií DEFORM v adresári /3D/LABS/ (pozri obr. 3DFGL1.25.). Skontrolujte importovanú geometriu tak, ako bolo vysvetlené v predchádzajúcom popise geometrie obrobku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno plánovaného polohovania.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0025.jpg' | relative_url }})

Import geometrie s viacerými hranicami pre spodnú matricu

### Definícia plánovaného polohovania

Matrice sú štandardne v správnej polohe. Ak sa chcete uistiť, že sú správne umiestnené, definujte plánovanú polohu hornej a dolnej matrice vo vzťahu k obrobku metódou kolízie v smere -Z, resp. +Z, ako je znázornené na obr. 3DFGL1.26. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0026.jpg' | relative_url }})

Plánované polohovanie hornej a spodnej matrice

### Definovanie vzťahov medzi objektmi

Vyberte kontakt typu **užívateľ** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) (pozri obr. 3DFGL1.29.). Tým sa pridá vzťah medzi polotovarom, hornou maticou a spodnou maticou. Keďže matice sú tuhé a polotovar je plastický, horná a spodná matica sa považujú za hlavné a polotovar za podriadený.

Zvýraznite vzťah **Horná forma – obrobok** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) upravte podmienky kontaktu. Na karte „Trenie“ (pozri obr. 3DFGL1.27.) sa nachádza roletové menu, ktoré umožňuje používateľovi vybrať vhodné podmienky trenia pre bežné tvárniace procesy.

Keďže ide o simuláciu tvárnenia za tepla a formy sú z ocele, použite rozbaľovacie menu a zo zoznamu vyberte možnosť **Tvárnenie za tepla**. Hodnota trenia **0******.** 3** sa vyberie automaticky.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0027.jpg' | relative_url }})

Definícia koeficientu trenia medzi objektmi pri horúcom kovaniu

Na **kartu „Tepelné vlastnosti“** vyberte z roletového menu možnosť typu **Tvarovanie**; tým sa pridá predvolená hodnota koeficientu prenosu tepla **5** pre tvarovanie, ako je znázornené na obr. 3DFGL1.28.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0028.jpg' | relative_url }})

Definícia koeficientu prenosu tepla medzi objektmi pri tvárnení

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna „Inter-Object“; keďže podmienky trenia a prenos tepla medzi objektmi sú rovnaké pre všetky páry objektov, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných. Po vykonaní tejto operácie budú mať všetky vzťahy koeficient trenia 0,3 a koeficient prenosu tepla 5, ako je znázornené na obr. 3DFGL1.29. Keďže sa kontakt inicializuje a vygeneruje počas vytvárania databázy, zaškrtnite políčka „Initialize“ a „Generate“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0029.jpg' | relative_url }})

Definícia vzťahu medzi objektmi pre tvorbu

### Definovanie ovládacích prvkov zastavenia

V okne riadenia zastavenia skontrolujte ovládací prvok **Vzdialenosť medzi maticami** a nastavte hodnotu vzdialenosti na **11,0** mm. Následne v okne zobrazenia vyberte body v strede dutín hornej a dolnej matice na strane veľkého konca a vyberte smer **Z**, ako je znázornené na obr. 3DFGL1.30. Po výbere bodov na formách je možné pozorovať vzdialenosť medzi formami, v tomto prípade je to približne 51,8. Pokiaľ ide o pokročilé možnosti zastavenia, pozrite si režim Expert (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})); keďže ho v tomto laboratórnom cvičení nepoužívame, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a pokračujte.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0030.jpg' | relative_url }})

Riadenie zastavenia matíc na základe vzdialenosti pri tvárnení

### Nastavenie ovládacích prvkov krokov

V okne nastavenia krokov nastavte **počet krokov** na **500**, s krokom **0,2** mm pre **maticu** **pohybu**, **krok** **prirastku** **na****uloženie** nastavte na **10** pre primárnu maticu (ktorá je v tejto simulácii objektom číslo 2), ako je znázornené na obr. 3DFGL1.31. Pokročilé funkcie ovládania krokov a simulácie sú k dispozícii v režime Expert (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})).

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0031.jpg' | relative_url }})

Krok: Nastavenia pre formovanie

Keďže sa počas simulácie vytvorí databáza pre operáciu tvarovania kužeľa, týmto sa dokončí nastavenie viacerých tvarovacích operácií v režime MO – Guided. Na simuláciu úlohy kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov (pozri obr. 3DFGL1.33.).

## Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 3DFGL1.32. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. 

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0032.jpg' | relative_url }})

Vyskočiace okno „Spustiť simuláciu“

Priebeh simulácie sledujte na kartách „Simulation Graphics“, „Simulation Message“ a „Simulation Log“, pričom sa uistite, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). (Pozri obr. 3DFGL1.33.)

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0033.jpg' | relative_url }})

Simulačný režim zobrazujúci aktuálny stav formovania

Po dokončení všetkých operácií sa v súbore protokolu simulácie zobrazí správa „MULTIPLE OPERATION COMPLETED.“, potom prejdite na kartu „Post“ kliknutím na ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), aby ste si prezreli výsledky simulácie.

## Následné spracovanie

V postprocesore sa v zozname krokov pod grafickou oblasťou zobrazujú čísla krokov dostupných z rôznych simulovaných operácií. Na kontrolu reakcie modelu je možné použiť súbor stavových premenných dostupných v ponuke „Post“. Upozorňujeme, že pre prvú operáciu sú k dispozícii iba tepelné údaje o obrobku. Výsledky deformácie je možné vidieť pri operácii tvárnenia riadiaceho ramena (pozri obr. 3DFGL1.34). Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) (zväčšenie podľa okna) zväčšite kužeľovú časť obrobku, ako je znázornené na obr. 3DFGL1.34.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0034.jpg' | relative_url }})

Deformačne efektívny variabilný obrys pri kužeľovom tvare obrobku

Niektoré dôležité stavové premenné je možné vybrať priamo z okna „Post Tools“ a k ostatným sa dostanete cez dialógové okno „State Variable“ kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}).

Kliknite na graf ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) (zaťaženie – zdvih) a vyneste graf času (s) v závislosti od zaťaženia (klb), ako aj graf času (s) v závislosti od rýchlosti (in/s) pre hornú maticu. Všimnite si zmenu rýchlosti po deformácii o 20,4 mm z 10 in/sec na 8 in/sec, ako je znázornené na obr. 3DFGL1.35.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0035.jpg' | relative_url }})

Grafy „Čas vs. zaťaženie“ a „Čas vs. rýchlosť“ pre primárnu matricu (horná matrica)
