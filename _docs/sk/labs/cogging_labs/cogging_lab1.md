---
lang: sk
title: "Laboratórna úloha č. 1 – Cogging"
---

# Cogging – laboratórna práca č. 1

1.1. Úvod

1.2. Formulácia problému

1.3. Definovanie nastavení procesu

1.4. Definícia tabuľky prechodov

1.5. Naloženie materiálu

1.6. Definícia objektu

1.7. Definícia objektu „Billet“

1.8. Definícia hornej matrice

1.9. Definovanie údajov manipulátora

1.10. Polohovanie objektov

1.11. Plánované umiestnenie

1.12. Definícia vzťahu medzi objektmi

1.13. Náhľad simulácie

1.14. Ovládacie prvky simulácie

1.15. Vytvorenie databázy

1.16. Spustenie simulácie

1.17. Následné spracovanie

## Úvod

Sprievodca coggingom ponúka možnosti, ako sú tabuľka priechodov, ovládacie prvky pohybu, možnosti opätovného ohrevu a základné prvky pre lisovacie formy, sochty a manipulátory; vďaka týmto možnostiam môže používateľ ľahko nastaviť typický proces coggingu. K coggingu sa dostanete cez sprievodcu DEFORM MO, ktorý je dostupný z hlavného okna grafického rozhrania DEFORM. 

## Zadanie úlohy

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. 3DCGL1.1. Vyberte volič „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte volič „**Angličtina**“. Názov úlohy zadajte ako „**Coglab**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), čím otvoríte nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu problému

Spustí sa sprievodca viacerými operáciami s dialógovým oknom „Nový projekt“. V tejto lekcii použijeme ako názov projektu „**Coglab**“. Operáciu 3D Cogging je možné pridať aj v dialógovom okne „Nový projekt“, v tomto laboratórnom cvičení však pridáme operáciu Cogging zo zoznamu operácií v Průzkumníku, preto v dialógovom okne „Nový projekt“ nezaškrtávajte políčko „Prvá operácia“ ani operáciu „Cogging“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otvorení operácie. Otvorí sa sprievodca MO (pozri obr. 3DCGL1.2.).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0002.jpg' | relative_url }})

Priradenie názvu problému

Pridajte operáciu 3D Cogging zo zoznamu operácií v prehliadači. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky 3D Cogging alebo ju môžete pridať aj pretiahnutím do editora operácií (pozri obr. 3DCGL1.3.). Po pridaní operácie Cogging sa štandardne otvorí okno procesu.

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0003.jpg' | relative_url }})

Operácia Explorer

## Nastavenia procesu

V okne „Process“ vyberte prepínač **Hot – Calculate temp in Bille****t****and****dies** a zaškrtnite políčko **Heat transfer per bite**, keďže budeme nastavovať neizotermický proces. Nastavte **Dĺžku cyklu** na **5** sekúnd a **Dĺžku zdržania** na **1** sekundu, ako je znázornené na obr. 3DCGL1.4.

Na stránke „Proces“ si používateľ môže pre simuláciu vybrať 2 alebo 4 matrice a tiež sa rozhodnúť, či na pridržanie sochoru použije manipulátory (alebo či na sochor použije priamu technológiu BCC). V prípade dutých polotovarov môže používateľ použiť trn, ako je to v prípade procesu lisovania. Toto okno obsahuje aj možnosti na nastavenie kritérií opätovného ohrevu pomocou funkcie Adaptive Reheating. V tomto laboratórnom cvičení použijeme 2 matrice a manipulátory; kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na ďalšiu tabuľku.

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0004.jpg' | relative_url }})

Okno procesu

## Definícia tabuľky prechodov

V okne „Tabuľka priechodov“ nastavíme axiálny posuv na jeden záber, hrúbku priečneho rezu, smer pohybu, otáčanie na jeden záber (°) a otáčanie na jeden priechod (°).

V tomto konkrétnom laboratórnom cvičení definujeme dva priechody a použijeme výpočet Auto Bite. Stačí teda pridať ešte jeden priechod pomocou ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a potom kliknúť na „Pass 1“. (Pozri obr. 3DCGL1.5.)

**Tip:**

Aby ste ušetrili čas pri nastavovaní údajov pre každý priechod, stačí definovať len prvý priechod a potom pridať ďalší. Všetky údaje z prvého priechodu sa tak skopírujú do ďalšieho.

Zaškrtnite políčko **Automatický výpočet počtu rezov**, aby systém automaticky vypočítal počet rezov potrebných na jeden priechod na základe dĺžky polotovaru alebo podmienok uvedených v počiatočnej a koncovej polohe matrice.

**Axiálny posuv na jeden záber** je **10** palcov,

**Hrúbka priečneho rezu** je **18** palcov a

**Smer pohybu** sa pre figúrky označuje ako **–X**.

Pre druhý priechod môžete zmeniť **rotáciu na priechod** (°) na **90**, pričom všetky ostatné parametre ponechajte rovnaké ako v 1. priechode. Ostatné hodnoty ponechajte na predvolených hodnotách a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím prejdete na stránku „Materiál“.

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0005.jpg' | relative_url }})

Okno s tabuľkou priechodov

## Načítanie materiálu

V tomto laboratórnom cvičení budeme používať materiál zo súboru **USER_HT.KEY**, ktorý je k dispozícii v inštalačnom adresári Labs Directory. V okne so zoznamom materiálov vyberte možnosť „Importovať údaje o materiáli zo súboru“ (![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})) a otvorí sa dialógové okno. V ňom vyhľadajte súbor USER_HT.KEY v adresári Labs Directory a otvorte ho. Otvorí sa dialógové okno na výber materiálu, vyberte **TITANIUM 6Al-4V** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste materiál importovali. Zopakujte rovnaký postup na import materiálu formy **AISI D3**, ktorý je k dispozícii v súbore USER_HT.KEY. (pozri obr. 3DCGL1.6.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0006.jpg' | relative_url }})

Okno s materiálmi

Po kliknutí na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) sa zobrazia vlastnosti materiálov načítaných na stránku so zoznamom materiálov, ktoré je možné upravovať (pozri obr. 3DCGL1.7.). V tomto cvičení budeme používať predvolené hodnoty, preto klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s objektom.

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0007.jpg' | relative_url }})

Stránka „Vlastnosti materiálu“

## Definícia objektu 

V okne objektu sú k dispozícii možnosti na zachovanie veľkosti siete na sochore počas simulácie, a to buď pomocou pomeru strán, alebo veľkosti prvku. Podrobný popis týchto možností nájdete v [Cogging Manual]({{ '/docs/sk/operation_templates/29_cogging/29_1_cogging_setup/' | relative_url }}). Používateľ má tiež možnosť vykonať vyrovnanie sochora medzi jednotlivými priechodmi alebo medzi jednotlivými zábermi. Vyrovnávanie sochoru je operácia manipulácie s geometriou, ktorá sa vykonáva s cieľom zabrániť nadmernému ohybu spôsobenému miernymi chybami polohovania, ktoré sa nahromadili počas viacerých priechodov. V rámci tohto laboratórneho cvičenia nebudeme vykonávať žiadne vyrovnávanie sochoru (pozri obr. 3DCGL1.8.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0008.jpg' | relative_url }})

Okno objektu

## Definícia objektu „Billet“

V okne „Billet“ zmeňte hodnotu **teploty objektu** z 68 °F na **1500** °F (pozri obr. 3DCGL1.9.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0009.jpg' | relative_url }})

Okienko na polotovar

### Definovanie geometrie polotovaru 

V okne „Geometria polotovaru“ vyberte možnosť ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), keďže geometriu polotovaru budeme vytvárať z primitív. V okne „Primitív“ vyberte ako prierez **obdĺžnik** so zaoblenými rohmi a zadajte **výšku/šírku** **20** , **dĺžku** **60** a **polomer rohu** **2** (pozri obr. 3DCGL1.11.). Po vytvorení geometrie z primitívu sa uistite, že na stránke Geometria je zaškrtnuté políčko „Použiť prierez“ v možnostiach konverzie 2D => 3D. Operácia Cogging používa 2D prierez na generovanie mriežky blokov a prierez sa počas simulácie aktualizuje, preto by políčko „Použiť prierez“ v možnostiach konverzie 2D => 3D malo byť pri operácii Cogging vždy zaškrtnuté. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

Zobrazí sa 2D priečny rez geometrie, ako je znázornené na obrázku. V prípade potreby je možné 2D priečny rez upraviť pomocou možností dostupných na stránke 2D priečny rez (pozri obr. 3DCGL1.12.). V tomto laboratórnom cvičení sa 2D priečny rez nebude upravovať, preto kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0010.jpg' | relative_url }})

Okno Geometria

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0011.jpg' | relative_url }})

Primitívne okno typu „Billet“

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0012.jpg' | relative_url }})

Okno 2D geometrie

### Definícia siete z polotovarov 

Na stránke „Mesh“ zadajte **100** ako počet prvkov siete pre 2D priečny rez a **size****ratio** ako **1**. Zadajte **14** ako **počet****vrstiev** v axiálnom smere. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) a v rozbaľovacom okne „Predvolené okrajové podmienky“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). Zadajte hodnotu 25000 pre počet prvkov pri opätovnom vytvorení siete. Toto číslo sa použije na generovanie tetraedrickej siete v prípade, že opätovné vytvorenie brickovej siete zlyhá kvôli príliš veľkému skresleniu (pozri obr. 3DCGL1.13.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0013.jpg' | relative_url }})

Okienko zo sieťoviny z hliníkového bloku

### Priradiť materiál na výkovok

Na stránke „Materiál polotovaru“ vyberte materiál **TITANIUM 6Al-4V** pre polotovar, ktorý bol importovaný skôr (pozri obr. 3DCGL1.14.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0014.jpg' | relative_url }})

Okno s materiálmi

### Definícia okrajovej podmienky

V závislosti od zvolených procesných podmienok systém automaticky vygeneruje BCC pre tepelné a symetrické podmienky. V tomto cvičení nepoužívame symetriu, preto sa automaticky generujú iba tepelné BCC, ako je znázornené na obr. 3DCGL1.15. Pre toto cvičenie ponecháme predvolené vygenerované BCC. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0015.jpg' | relative_url }})

Okno BCC z hliníkového bloku

### Vlastnosti polotovarov 

Rôzne parametre objektu, ktoré ovplyvňujú buď termomechanické správanie objektu, alebo správanie numerického riešenia, sa zadávajú v okne „Object-Properties“ (pozri obr. 3DCGL1.16.). V rámci tohto laboratórneho cvičenia nie je potrebné vykonávať žiadne zmeny v okne vlastností. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top die“.

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0016.jpg' | relative_url }})

Okno s vlastnosťami polotovaru

## Definícia hornej matrice

V okne „Top die Window“ zmeňte teplotu objektu z **68°** F na **200°** F (pozri obr. 3DCGL1.17.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0017.jpg' | relative_url }})

Okienko na hornej matrici

### Definovanie geometrie hornej matrice

Na definovanie geometrie výseku použijeme možnosti primitívnej geometrie, ktoré ponúka sprievodca; vyberte teda možnosť ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a v okne „Primitive“ zadajte **výšku/šírku** **15** , **dĺžku** **25** a **polomer rohu** **2** (pozri obr. 3DCGL1.18.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

V tomto cvičení sa 2D priečny rez nebude upravovať, preto kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0018.jpg' | relative_url }})

Okno „Geometria hornej matrice“

### Definovanie mriežky hornej matrice

Na stránke „Mesh“ zadajte **100** ako počet prvkov 2D priečnych sietí a **veľkosť****pomer** ako **1**. V axiálnom smere budeme mať **7** **vrstiev** (pozri obr. 3DCGL1.19.). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) na vytvorenie siete pre matricu a v rozbaľovacom okne „Predvolené okrajové podmienky“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). Geometria a sieť matrice sa duplikujú aj pre ostatné matrice. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0020.jpg' | relative_url }})

Okno s mriežkou v hornej časti formy

### Určenie materiálu hornej matrice

Na stránke „Materiál hornej formy“ vyberte pre hornú formu materiál **AISI D3** (pozri obr. 3DCGL1.20.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0021.jpg' | relative_url }})

Okno s materiálom hornej matrice

### Definícia pohybu hornej matrice

Na stránke „Top die movement“ (Pohyb hornej matrice) nastavte pre toto laboratórne cvičenie **rýchlosť** matrice na **1** palec/sekundu (pozri obr. 3DCGL1.21.). Používateľ má tiež možnosť použiť mechanický lis a iné typy ovládania pohybu, ako napríklad skrutkový lis, v rámci pokročilých nastavení v závislosti od požiadaviek procesu. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka manipulátora.

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0019.jpg' | relative_url }})

Okienko pre pohyb hornej matrice

## Definovanie údajov manipulátora 

V okne manipulátora zmeňte **vzdialenosť odovzdávania vľavo** na **10** palcov a **vzdialenosť odovzdávania vpravo** na **10** palcov. Vzdialenosť odovzdania pomáha pri uvoľnení jednej sady manipulátorov, zatiaľ čo druhá sada preberá činnosť. Pri týchto nastaveniach sa sada manipulátorov uvoľní, keď sa formy nachádzajú vo vzdialenosti do 10 palcov od sady manipulátorov. Podmienky tlmenia pre pružinové manipulátory je možné nastaviť podľa obr. 3DCGL1.22. Od verzie DEFORM V12 bola na stránke „Manipulátory“ pridaná možnosť „Generovať BCC manipulátora“. Ak používateľ zaškrtne toto políčko, vygeneruje sa kontaktná BCC s manipulátorom pre všetky uzly povrchu (kontaktná oblasť manipulátora) v rámci okna trenia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0022.jpg' | relative_url }})

Okno manipulátora

### Definícia objektu ľavého manipulátora

V ľavom okne manipulátora zmeňte teplotu objektu z 68**°******F na **200°** F (pozri obr. 3DCGL1.23.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0023.jpg' | relative_url }})

Okno ľavého manipulátora

### Definovanie geometrie ľavého manipulátora

Na stránke „Geometria ľavého manipulátora“ vyberte možnosť ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) na definovanie geometrie manipulátora z primitív. V okne „Primitív“ zadajte rozmery podľa obr. 3DCGL1.24, vytvorte geometriu a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

V tomto laboratórnom cvičení sa 2D priečny rez nebude upravovať, preto klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka so sieťou. 

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0024.jpg' | relative_url }})

Okno s primitívami manipulátora

### Definovanie siete ľavého manipulátora

Na stránke „Mesh“ zadajte **50** ako počet prvkov 2D priečnych sietí a **veľkosť****pomer** ako **2**. V axiálnom smere budeme mať **5** **vrstiev**. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) na vytvorenie siete pre manipulátor a v rozbaľovacom okne „Predvolené okrajové podmienky“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). Geometria a sieť manipulátora sa duplikujú aj pre ostatné manipulátory (pozri obr. 3DCGL1.25.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0025.jpg' | relative_url }})

Okno so sieťou na ľavom manipulátore

### Definícia materiálu ľavého manipulátora

Na stránke s materiálmi pre ľavý manipulátor vyberte ako materiál pre ľavý manipulátor **AISI D3** (pozri obr. 3DCGL1.26.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s polohovaním. 

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0021.jpg' | relative_url }})

Okno „Priradenie materiálu“

## Umiestňovanie objektov 

Umiestnenie objektov riadi systém automaticky na základe údajov o prechode nastavených v tabuľke prechodov. Preto nie je potrebné vykonávať žiadne umiestňovanie – kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Plánované umiestňovanie“. 

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0027.jpg' | relative_url }})

Okno na nastavenie polohy

## Plánované polohovanie

Keďže nie je potrebné vykonávať žiadne polohovanie, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) aj na stránke „Naplánované polohovanie“.

## Definícia vzťahu medzi objektmi

Systém automaticky vygeneruje kontaktné vzťahy medzi objektmi; ak by používateľ chcel definovať akúkoľvek inú podmienku okrem predvolených, mal by zvoliť používateľskú voľbu. V tomto laboratórnom cvičení použijeme kontaktné podmienky generované **systémom**, vyberieme typ definície kontaktu **Systém**, zaškrtneme políčka „Inicializovať“ a „Generovať“ pre naplánovaný kontakt a zadáme malú hodnotu tolerancie kontaktu **0,0001**, ako je znázornené na obr. 3DCGL1.28. Koeficienty prenosu tepla medzi objektmi a koeficient trenia je možné nastaviť na stránke ovládacích prvkov simulácie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0028.jpg' | relative_url }})

Okno medzi objektmi

## Náhľad simulácie

Náhľad simulácie poskytuje prehľad operácií, ako sú deformácia, výdrž, opätovné zahrievanie atď., ktoré sa majú vykonať na základe definície procesu vo forme animácie. Ponúka tiež náhľad nastavenia pri každej operácii. V okne náhľadu simulácie sa kliknutím na tlačidlá prehrávania spustí animácia (pozri obr. 3DCGL1.29.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0029.jpg' | relative_url }})

Okno náhľadu simulácie

## Ovládacie prvky simulácie

V okne riadenia simulácie nastavte **počet krokov** pre simuláciu deformácie na hodnotu **10**, **krok na uloženie** na hodnotu **500**, aby sa pri každom zábere uložil len jeden krok, a hodnotu zdvihu na jeden krok na **0,1** palca/krok.

**Prenos tepla****počet krokov** a **krok** nastavte na hodnotu **10**, aby sa pri operáciách prenosu tepla, ako je napríklad zdržanie, ukladal len 1 krok. Keďže sa pred dokončením simulácie coggingu vykoná viacero operácií, veľkosť databázy sa reguluje ukladaním obmedzeného počtu krokov do databázy. Všetky ostatné hodnoty ponechajte na predvolených hodnotách a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). Od verzie v11.0 je pre simulácie coggingu k dispozícii explicitný riešiteľ, avšak v tomto laboratórnom cvičení budeme používať implicitný riešiteľ (pozri obr. 3DCGL1.30.).

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0030.jpg' | relative_url }})

Okno riadenia simulácie

## Vytvorenie databázy

Na stránke na generovanie databázy kliknite na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Databázu vygenerujte kliknutím na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Po kliknutí na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) sa vygeneruje súbor ProblemID.MST spolu s databázou.

## Spustenie simulácie

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 3DCGL1.31. Použite predvolenú možnosť **Pokračovať v spustení**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“ (od kroku -1), potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0031.jpg' | relative_url }})

Vyskakovacie okno „Spustiť simuláciu“

Priebeh simulácie môžete sledovať v okne „Simulation graphics“ a na kartách „Simulation Message“ a „Simulation Log“ (pozri obr. 3DCGL1.32.). Súbory správ a protokolov sa automaticky aktualizujú, čo umožňuje sledovať priebeh simulácie. Pomocou možností na paneli nástrojov „Simulačná grafika“ je možné počas simulácie problému znázorniť základné stavové veličiny objektov, ako sú teplota, deformácia a kontakt. Teraz môžeme využiť aj možnosti „Súhrn“, „Zaťaženie – zdvih“, „Zrkadlenie“, „Rozrezávanie“ a „Meranie“, ktoré boli pridané do zoznamu nástrojov.

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0032.jpg' | relative_url }})

Simulačný režim MO

Pri simulácii coggingu sa všetky simulačné údaje o coggingu počas behu zapíšu do súboru ProblemID.MST. Súbor ProblemID.MST umožňuje postupné vykonávanie simulácie coggingu, pričom každá operácia deformácie zubov a prenosu tepla prebieha ako samostatná operácia na základe nastavení na stránke procesu a v tabuľke priechodov. Súbor ProblemID.MST riadi spustenie a zastavenie každej operácie. Pre všetky operácie sa správy o spustení a zastavení zobrazujú v súbore správ. Po dokončení všetkých operácií sa v súbore protokolu simulácie zobrazí správa „MULTIPLE OPERATION COMPLETED“ (Viacnásobná operácia dokončená).

## Následné spracovanie

Po dokončení simulácie si môže používateľ prezrieť výsledky prepnutím do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). (Pozri obr. 3DCGL1.33.)

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0033.jpg' | relative_url }})

Režim MO Post

Prejdite jednotlivými krokmi a pozrite si rozloženie teploty a rozloženie deformácie pomocou grafického znázornenia stavových premenných teploty a efektívnej deformácie (pozri obr. 3DCGL1.34).

Zmenu teploty v lisovacích formách je možné pozorovať aj na obr. 3DCGL1.35.

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0034.jpg' | relative_url }})

Rozloženie napätia

![]({{ '/assets/images/labs/cogging_labs/cogging_lab1/image0035.jpg' | relative_url }})

Rozloženie teploty
