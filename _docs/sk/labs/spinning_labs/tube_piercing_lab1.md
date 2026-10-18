---
lang: sk
title: "Laboratórium piercingu trubice1"
---

# Tube Piercing Lab1

1.1. Vytvorenie nového problému

1.2. Stránka procesu

1.3. Nastavenie simulácie

1.4. Stránka objektu

1.5. Obrobok

1.5.1. Stránka 2D prierezu obrobku

1.5.2. Stránka 3D geometrie

1.5.3. Sieťovina obrobku strana

1.5.4. Materiálová strana

1.5.5. Hraničné podmienky obrobku

1.6. Strana vretena

1.6.1. Import 2D geometrie vretena - prierez

1.6.2. Vygenerovať 3D geometriu vretena

1.7. Zrolujte 1 stranu

1.7.1. Importovanie strany 2D prierezu valca

1.7.2. Vygenerovať 3D geometriu vretena

1.7.3. Roll 1 Orientačná stránka

1.8. Stránka posunovača

1.8.1. Stránka 3D geometrie posunovača

1.8.2. Stránka pohybu posunovača

1.9. Topánka 1 strana

1.9.1. Stránka 3D geometrie topánky 1

1.10. Stránka s ovládacími prvkami

1.11. Kontaktná stránka

1.12. Stránka Zastavenie ovládacích prvkov

1.13. Stránka s ovládacími prvkami simulácie

1.14. Generovať databázu

1.15. Simulácia chodu

1.16. Po spracovaní

V tomto laboratóriu nastavíme jednoduchý proces prepichovania skúmaviek s modelom ale a implicitným riešiteľom.

## Vytvorenie nového problému

Na ** zariadení so systémom Windows ** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), zvoľte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * vxx.xx. Zobrazí SA hlavné okno Deform GUI.

Vytvorte nový problém buď výberom * * Súbor * *![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 3DTPL1.1. Pomocou prepínača v poli jednotky vyberte prepínač „** Integrovaný výrobný proces **“ a systém jednotiek ako „** SI * *“. Definujte názov problému ako "** TubePiercingLab1 * * " a uistite sa, že je zapnuté začiarkavacie políčko "Zobraziť dialóg možností" (ak nezapneme začiarkavacie políčko "**Zobraziť dialóg možností ** ", potom nedostaneme dialógové okno Nový projekt v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

Nový problém

V dialógovom okne Nový projekt sa otvorí sprievodca viacerými operáciami, v tomto bode sa používateľovi zobrazí výzva na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**TubePiercingLab1 * * “. Operáciu 3D Spinning je možné pridať aj v dialógovom okne „Nový projekt“ alebo z Prieskumníka. Ak chcete pridať 3D Spinning z dialógového okna „Nový projekt“, vyberte 3D Spinning zo zoznamu operácií a začiarknite políčko „* * Prvá operácia * * “. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otvorení operácie.

Ak operácia 3D Spinning nie je pridaná z „New Project“ (Nový projekt), operáciu je možné pridať zo zoznamu Explorer Operations (Operácie prieskumníka). Pridajte operáciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ktoré je k dispozícii vedľa 3D Spinning, alebo používateľ môže tiež pridať presunutím myšou do editora operácií (pozri obr. 3DTPL1.2.). Proces prepichnutia trubice je modelovaný s osou pozdĺž osi Y, preto ak je aktuálny smer obrazovky smerom nahor „Z“, objaví sa vyskakovacie okno, ktoré naznačuje zmenu smeru obrazovky smerom nahor na „+Y“. V laboratóriu použijeme os „+Y“ ako smer obrazovky smerom nahor, preto kliknite na tlačidlo „YES-Change“ v kontextovom okne „Change screen upward axis“ (Zmeniť obrazovku smerom nahor). Teraz sa predvolene otvorí okno nastavení procesu, ako je znázornené na obr. 3DTPL1.3.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0002.jpg' | relative_url }})

Zobrazenie vyskakovacieho okna smeru nahor

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0003.jpg' | relative_url }})

Otvorená operácia 3D odstreďovania

## Stránka procesu

Na stránke Process zvoľte "**Tube piercing** " a definujte rýchlosť otáčania vretena * * ako * * -300 * *** rpm * *, ako je znázornené na obr. 3DTPL1.4. Táto rýchlosť sa vzťahuje aj na chvost a hlavu, ak sa používa. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku nastavenia simulácie.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0004.jpg' | relative_url }})

Stránka procesu

## Nastavenie simulácie

V nastavení simulácie je v predvolenom nastavení vybraná metóda riešenia "* * ale * * " a typ riešiteľa je "* * Implicitné * * ", ktoré sú v súčasnosti k dispozícii iba možnosti. Keďže nás teplotný profil nezaujíma, vyberieme typ „**Konštantná teplota (izotermická)** “ Tepelný výpočet a pre 3D model zvolíme typ * **** symetria ** a symetrické číslo nastavíme ako * * 2 * *, čo znamená polovičnú symetriu (pozri obr. 3DTPL1.5.). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na objekty.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0005.jpg' | relative_url }})

Stránka nastavenia simulácie

## Stránka objektu

V tomto laboratóriu na piercing trubiek budeme používať obrobok, tŕň, posunovač, jednu rolovaciu a 2 podporné topánky. V zozname Objekty sa predvolene začiarkne a vypne políčko Obrobok a tŕň, pretože tieto objekty sú pre tento proces povinné. Začiarknite políčko **Posúvač * *, pretože ho budeme používať. V časti Rolls and Discs vyberte možnosť „* * 1 Roll + 2 Support shoes * * “, pretože na vedenie pohybu obrobku budeme používať podporné topánky, pozri obr. 3DTPL1.6. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na obrobok.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0006.jpg' | relative_url }})

Stránka objektov

## Obrobok

Na stránke Obrobok ponechajte názov objektu ako * * Obrobok * *, definujte * * objekt * * ** teplotu * * ako * * 1250 * ** °C ** a typ objektu ako * * Plast * *, ako je znázornené na obr. 3DTPL1.7. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 2D Geometry.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0007.jpg' | relative_url }})

Stránka obrobku

### Stránka 2D prierezu obrobku

Na vytvorenie geometrie obrobku použijeme špecializovanú možnosť primitívnej geometrie, ako je znázornené na obr. 3DTPL1.8. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a definujte **Polomer(R)** ako **100** a **Dĺžku(L)** ako **900** na základnej stránke geometrie. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) vytvoríte geometriu a zatvoríte primitívnu stránku geometrie (pozri obr. 3DTPL1.8.). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0008.jpg' | relative_url }})

Primitívna stránka geometrie obrobku

### Stránka 3D geometrie

Na stránke 3D geometrie definujte **počty otáčaných rezov* ***ako* ***100** a v predvolenom nastavení bude uhol otáčania 180, pretože sme vybrali číslo symetrie ako 2. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}) vygenerujete 3D geometriu.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0009.jpg' | relative_url }})

Generovať 3D geometriu

  
Piercing trubice používa tehlovú sieť, preto musíme definovať nastavenia týkajúce sa tehlovej siete na úrovni geometrie na stránke 3D geometrie. ![]({{ '/assets/icons/pre_icons/mo_setup_brick_mesh_label.jpg' | relative_url }}) odkaz je povolený po vygenerovaní 3D geometrie. Kliknutím na tento odkaz prejdete na stránku nastavenia tehlovej siete a vyberiete prepínač * * Otočiť * *. Pri otáčaní musíme zvoliť prepínač **Čiastočné otáčanie **, pretože objekty sú objektom symetrie a potom pridať počiatočný povrch a koncový povrch, ako je znázornené na obr. 3DTPL1.10. Kliknutím na tlačidlo Sprievodca ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) vypočítate os otáčania, referenčnú os, počiatočný uhol a uhol otáčania na základe vybraných povrchov. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) potvrďte nastavenie a potom kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0010.jpg' | relative_url }})

Nastaviť stránku s mriežkou z tehál

### Stránka sieťoviny obrobku

"Tehlová sieť" je predvolene vybraná ako typ siete, definujte sieť prierezu **T*****arg** et počet prvkov** ako **300**. Definujte parametre 3D povrchovej siete **Počet otočených sekcií ako 40.** Definujeme jemnejšiu sieťovinu pozdĺž kontaktnej oblasti s **uhlom 15°** a ** pomerom veľkosti 4**. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}) vygenerujete 3D povrchovú sieť. 3D povrchová sieť sa vygeneruje so 14640 prvkami a 17958 uzlami, ako je znázornené na obr. 3DTPL1.11. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku materiálu.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0011.jpg' | relative_url }})

Mriežka obrobku strana

### Stránka materiálu

Na stránke Materiál kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (importovať údaje o materiáli z knižnice) a načítajte materiál **AISI 52100[70-2200F (20-1200C)]** z knižnice materiálov, ako je znázornené na obr. 3DTPL1.12.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0012.jpg' | relative_url }})

Priradenie materiálu obrobku

### Hraničné podmienky obrobku

Na stránke Boundary conditions overte predvolené BCC vygenerované pre rotačnú symetriu počas generovania povrchovej siete. Skontrolujte podriadené a hlavné uzly, rotačnú os a uhol otáčania, na tejto stránke nie je potrebné nastavovať nič, pretože všetky údaje sa v predvolenom nastavení získavajú na základe predchádzajúcich nastavení z geometrie a povrchovej siete, preto kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku vretena.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0013.jpg' | relative_url }})

Stránka hraničných podmienok obrobku

## Stránka vretena

Na stránke Mandrel General ponechajte predvolené hodnoty pre name ako * *Mandrel** a teplotu ako **20** °C. Kliknite na stránku prierezu ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na geometriu 2D.

### Import 2D geometrie vretena - prierez

Importujte 2D geometriu „**Mandrel_2D.geo** “ z priečinka „3D/Labs/Spinning“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a potom kliknite na Skontrolovať a opraviť geometriu vo vyskakovacom okne na overenie geometrie. Geometria sa opraví z hľadiska jej orientácie, kliknite na tlačidlo ok v kontextovom okne správy a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) na zatvorenie okna overenia geometrie. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0014.jpg' | relative_url }})

Importovanie 2D prierezu vretena

### Generovať 3D geometriu vretena

Použitím predvolenej hodnoty **100** ako „**Počet otočných sekcií** “ vygenerujte 3D geometriu kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}) (pozri obr. 3DTPL1.15.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) spustite 1 stranu.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0015.jpg' | relative_url }})

Stránka 3D geometrie vretena

## Roll 1 strana

Na stránke Roll 1 General ponechajte predvolené hodnoty pre name ako * * Roll * *** 1 * * a teplotu ako **20°C**. Kliknite na stránku prierezu ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na geometriu 2D.

### Importovanie stránky 2D prierezu valca

Importujte 2D geometriu „**Roll 1_2D.geo** “ z priečinka „**3D/Labs/Spinning** “. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) vo vyskakovacom okne na overenie geometrie. Geometria sa opraví z hľadiska jej orientácie, kliknite na tlačidlo ok v kontextovom okne správy a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) na zatvorenie okna overenia geometrie. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0016.jpg' | relative_url }})

Importovanie 2D prierezu valca 1

### Generovať 3D geometriu vretena

Použitím predvolenej hodnoty **100** ako „**Počet otočných sekcií** “ vygenerujte 3D geometriu kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}) (pozri obr. 3DTPL1.17.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zrolujte orientačnú stránku 1.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0017.jpg' | relative_url }})

Roll 1 3D geometria page

### Roll 1 Orientačná stránka

Na stránke Orientácia nastavte ** Uhol osi valca ** ![]({{ '/assets/equations/pre_processor/10_material_data/degree_icon.jpg' | relative_url }}) na **6** * stupňov * * a * * Uhol osi valca ** ![]({{ '/assets/equations/pre_processor/10_material_data/alpha_icon.jpg' | relative_url }}) na **0****stupňov**, ako je znázornené na obr. 3DTPL1.18. Rotačná os a smer valca sú zobrazené v oblasti zobrazenia, ako je znázornené na obr. 3DTPL1.19. Polohovanie na základe týchto dvoch uhlov sa na tejto orientačnej stránke nepoužije, ale použije sa počas „Automatického polohovania“ na stránke „Polohovanie“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre posunutie stránky.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0018.jpg' | relative_url }})

Hodiť 1 orientačnú stránku

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0019.jpg' | relative_url }})

Orientačná os valca 1

## Stránka posunovača

Na stránke Pusher General ponechajte predvolené hodnoty pre name ako **Pusher** a teplotu ako **20** °C. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry.

### Stránka 3D geometrie posunovača

Pri vstupe na stránku 3D geometrie posunovača sa posunovač generuje automaticky na základe geometrie obrobku. **Šírka** je nastavená na **240** mm, ktorá sa vypočíta na základe existujúcej veľkosti obrobku. V prípade potreby môže používateľ upraviť hodnotu šírky a kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) posuniete stránku pohybu.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0020.jpg' | relative_url }})

Stránka 3D geometrie posunovača

### Stránka pohybu posunovača

V tomto nastavení vyberte typ pohybu ako **Rýchlosť**. Vyberte **Funkcia času** z rozbaľovacieho poľa a definujte rýchlosť ako funkciu času, ako je znázornené na obr. 3DTPL1.21. Definujte ovládanie rýchlosti, ako je znázornené na obr. 3DTPL1.22. a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button2.jpg' | relative_url }}) a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Shoe 1.

  
Pre konštantnú rýchlosť je možné použiť tlačidlo sprievodcu ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) na odhad odporúčanej rýchlosti pre posunovač. Rýchlosť sa odhaduje na základe rýchlosti otáčania a orientačných uhlov. Hodnota, ktorú tu získame, môže byť použitá ako referencia, avšak v procese prepichnutia trubice zvyčajne nastavujeme rýchlosť ako funkciu času tak, aby sa posunovač zastavil po úplnom zasunutí tyče(obrobku) so zátkou(tŕňom) a predtým, ako narazí do valca.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0021.jpg' | relative_url }})

Stránka pohybu posunovača

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0022.jpg' | relative_url }})

Funkcia definície času

## Topánka 1 strana

Na stránke Shoe 1 general ponechajte predvolené hodnoty pre name ako * * Shoe * * 1 a teplotu ako **20°C**. V strome objektov je zobrazený iba jeden predmet topánky, v procese prepichnutia trubice sa ľavá a pravá topánka považujú za topánky s rovnakou geometriou. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry.

### Stránka 3D geometrie topánky 1

Na stránke 3D geometrie máme špecializované primitívne 2D prierezy na definovanie geometrie obuvi, z ktorej sa 3D geometria generuje pretláčaním. Definujte **polomer ako 102 mm** , **výšku ako 120 mm** , **šírku ako 50 mm* *, * * dĺžku vytláčania ako 500 mm * * a * *vzdialenosť k počiatku ako 101,9 mm** a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}) (pozri obr. 3DTPL1.23.). Ľavá aj pravá obuv sa generujú po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre ovládanie stránky.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0023.jpg' | relative_url }})

Stránka 3D geometrie topánky 1

## Stránka ovládacích prvkov

Na stránke Ovládacie prvky kliknite na odkaz **Automatické polohovanie**, ako je znázornené na obr. 3DTPL1.24. Na stránke Automatické polohovanie definujte **H** až **90 mm** a **D** až **60 mm** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), ako je znázornené na obr. 3DTPL1.25. Nasledujúce akcie sa vykonávajú počas automatického polohovania,

Prevaľovať

* Rotačné polohovanie na základe dvoch orientačných uhlov

* Posun polohovania používa parameter H pozdĺž smeru y

Priebojník

* Posun polohovania používa parameter D pozdĺž smeru x

* Obrobok

* Interferenčné polohovanie s valcom

Pusher

* Interferenčné polohovanie s obrobkom

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pre zatvorenie stránky automatického polohovania a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre kontaktovanie stránky.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0024.jpg' | relative_url }})

Stránka s ovládacími prvkami

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0025.jpg' | relative_url }})

Stránka automatického polohovania

Kontakty

Na stránke Kontakt vyberte typ „**User * * “ a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}), v tabuľke budeme pozorovať pridávanie predvolených vzťahov. Teraz definujte ** hodnotu trenia ** pre každý vzťah, ako je znázornené na obr. 3DTPL1.26. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) vypočítate predvolenú hodnotu tolerancie kontaktu a vytvoríte kontakt kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Zastavenie ovládacích prvkov.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0026.jpg' | relative_url }})

stránka s kontaktnými informáciami

## Stránka Zastavenie ovládacích prvkov

Definujte **Proces****Trvanie** ako **2,7** s, ako je znázornené na obr. 3DTPL1.27. Kliknite na stránku ovládacích prvkov simulácie ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0027.jpg' | relative_url }})

Stránka Zastavenie ovládacích prvkov

## Stránka ovládacích prvkov simulácie

Zadajte **Počet krokov** ako * *20000 * * , * *Krok * ***prírastok * ***na * ***ušetriť * ***ako * ** 100 * * a * *Čas na krok ako 0,0005** sek na stránke Ovládacie prvky simulácie, ako je znázornené na obr. 3DTPL1.28. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujete stránku DB.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0028.jpg' | relative_url }})

Stránka ovládacích prvkov simulácie

Všeobecné

Na stránke Generate DB kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) a vygenerujte databázu. Sledujte správy na karte Správa, ktoré informujú o stave generovania databázy alebo o tom, či ide o chyby.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0029.jpg' | relative_url }})

Generovať stránku DB

## Simulácia behu

Po vygenerovaní databázy prepnite do režimu simulácie výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. 3DTPL1.30. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať z posledného kroku** “ a potom vyberte režim simulácie ako **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0030.jpg' | relative_url }})

Okno Spustiť simuláciu

  
Sledujte priebeh simulácie tak, že sa pozriete na kartu Simulačná správa a Simulačný protokol, uistite sa, že je začiarknutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Používateľ môže zobraziť proces prepichnutia trubice, keď simulácia pokračuje podľa zadaných kritérií zastavenia zo simulačnej grafiky.

Postprocessing

Po dokončení simulácie skontrolujte výsledky prepnutím do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov simulácie.

Prehrajte si kroky simulácie a pozrite sa, ako sa tvorí časť obrobku počas procesu prepichnutia rúrky.

![]({{ '/assets/images/labs/spinning_labs/tube_piercing_lab/image0031.jpg' | relative_url }})

Výstup postprocesora prepichnutia rúrky
