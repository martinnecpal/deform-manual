---
lang: sk
title: "Lab01 Kovanie blokov"
---

# Lab01 Kovanie blokov

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0000.jpg' | relative_url }})

  
1.1. Vytvorenie nového problému

1.2. Ovládacie prvky simulácie

1.3. Nastavenie vlastností materiálu

1.4. Načítanie údajov o objektoch

1.4.1. Obrobok (blok)

1.4.2. Horná matrica

1.4.3. Spodná matrica

1.5. Polohovanie

1.6. Vzťahy medzi objektmi

1.7. Nastavenie ovládacích prvkov krokov

1.8. Vytvorenie databázy

1.9. Spustenie simulácie

1.10. Následné spracovanie výsledkov

1.11. Ukončenie sprievodcu MO

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main, ako je znázornené nižšie na obr. 3DL1.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno grafického rozhrania DEFORM

Novú úlohu vytvoríte buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nová úloha**, alebo kliknutím na ikonu Nová úloha ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. 3DL1.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Názov úlohy zadajte ako „******Block**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „Zobraziť dialógové okno s možnosťami“, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili novú úlohu s použitím integrovaného výrobného procesu Deform.

.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt (pozri obr. 3DL1.3.), kde bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**Block**“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0003.jpg' | relative_url }})

Okno na výber typu problému

Používateľ môže tiež zmeniť systém jednotiek (systém jednotiek vybraný v ponuke Súbor sa nastaví ako predvolený) a pridať **3D tvárniacu operáciu** výberom z roletového zoznamu **Prvá****operácia** a **zaškrtnutím políčka** (pozri obr. 3DL1.4.). Pomocou možnosti **Kopírovať existujúci projekt** môžeme importovať predtým uložené projekty ako nový projekt. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0004.jpg' | relative_url }})

Priradenie názvu problému

Otvorí sa sprievodca viacerými operáciami (MO Wizard) (pozri obr. 3DL1.5.). Sprievodca MO Wizard je rozdelený do niekoľkých samostatných častí – konkrétne na okno DISPLAY, grafické nástroje, strom operácií, editor vlastností, editor operácií, prehliadač a grafické okno.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0005.jpg' | relative_url }})

Okno sprievodcu MO

## Ovládacie prvky simulácie

V tejto operácii nastavujeme jednoduchý izotermický režim, preto na stránke „Simulation control“ v záložke „Sim Mode“ **vypnite** začiarkavacie políčko **„Heat transfer mode“** (pozri obr. 3DL1.6.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0006.jpg' | relative_url }})

Stránka ovládacích prvkov simulácie

## Nastavenie vlastností materiálu

Pri nastavení simulácie je potrebné pre objekty špecifikovať vlastnosti materiálu. Obrobku bol priradený typ materiálu „Plast“, preto je potrebné definovať napätie pri plastickom tečení. Okrem toho, ak by simulácia bola neizotermická (teplota sa mení v čase), boli by potrebné aj tepelné vlastnosti. Vlastnosti materiálu lisovacích foriem nie je potrebné špecifikovať, pretože ich typ objektu je „Pevný“ (a simulácia je izotermická), a preto pri zaťažení nedochádza k ich deformácii.

Kliknutím na ikonu materiálu ![]({{ '/assets/icons/pre_icons/mo_material_icon.jpg' | relative_url }}) na karte prehliadača sa zobrazí zoznam materiálov rozdelených do rôznych kategórií. Pre túto simuláciu musíme pre obrobok definovať materiál **AISI-1035,****COLD**. Preto je potrebné vybrať kategóriu **Oceľ**, aby sa zobrazili všetky oceľové materiály. Existujú dva rôzne materiály AISI-1035 – jeden pre tvárnenie za studena a druhý pre kovanie za tepla. Keďže táto simulácia je nastavená na izbovú teplotu, vyberte materiál „AISI-1035, COLD“.

Po výbere materiálu zo zoznamu kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať), čím pridáte vybraný materiál do úlohy.

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) si môžete zobraziť vlastnosti pridaného materiálu (pozri obr. 3DL1.7. a obr. 3DL1.8.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku objektu.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0007.jpg' | relative_url }})

Stránka so zoznamom materiálov

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0008.jpg' | relative_url }})

Stránka s vlastnosťami materiálov

## Načítavanie údajov o objekte

Ak tam ešte nie sú tri objekty, pridajte ich kliknutím na tlačidlo „Vložiť objekt“ ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}); tri objekty budú pomenované ako „Obrobok“, „Horná forma“ a „Spodná forma“. Obrobok bude pridaný ako plastový objekt, zatiaľ čo Horná forma a Spodná forma budú pridané ako tuhé objekty (pozri obr. 3DL1.9.). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Obrobok.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0009.jpg' | relative_url }})

Stránka na pridávanie objektov

### Obrobok (blok)

Po otvorení stránky „Obrobok“ zmeňte názov objektu na **Blok** a uistite sa, že typ objektu je nastavený na **Plast**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku geometrie, a kliknite na možnosť ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) „Načítať geometriu z knižnice“. (Pozri obr. 3DL1.10.)

Najbežnejším typom súboru na import geometrie do programu DEFORM-3D je súbor formátu stereolitografie (.STL). Geometria bloku sa nachádza v súbore **Block_Billet.STL** v inštalačnom priečinku programu DEFORM, v adresári \3D\LABS. Po vyhľadaní a výbere tohto súboru kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}), čím sa geometria naimportuje do programu DEFORM. Geometria obdĺžnikového bloku by sa teraz mala zobraziť v okne DISPLAY. Keďže je geometria bloku už definovaná, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím prejdete na stránku so sieťou.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0010.jpg' | relative_url }})

Stránka s definíciami z geometrie

Na stránke siete v **režime s návodom** vidíme možnosti nastavenia siete, ako je cieľový počet prvkov, náhľad a generovanie siete. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_preview_mesh_button.jpg' | relative_url }}), aby ste videli, ako vyzerá sieť povrchu pri použití predvolených nastavení siete. Vytvorená sieť povrchu vyzerá dobre, preto kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), aby ste dokončili proces vytvárania siete. Keď sa zobrazí otázka „Chcete priradiť predvolené okrajové podmienky?“, kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). Po dokončení vytvárania siete môžeme vidieť počet prvkov v strome objektov alebo v časti „Summary“ (Súhrn) ovládacích prvkov vytvárania siete (pozri obr. 3DL1.11 a obr. 3DL1.12). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku materiálov objektov.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0011.jpg' | relative_url }})

Stránka na generovanie sietí

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0012.jpg' | relative_url }})

Pred a po vytvorení siete

Opäť vidíme materiál objektu a kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_edit_material_button.jpg' | relative_url }}) môžeme upravovať vlastnosti materiálu. Vyberte materiál zo zoznamu, aby ste ho pridali k objektu, ako je znázornené na obr. 3DL1.13. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Okrajové podmienky“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0013.jpg' | relative_url }})

Stránka o materiáloch objektu

V prípade objektu BCC budú predvolené okrajové podmienky definované samotným sprievodcom MO. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku s pohybmi.

Pokiaľ ide o pohyb, keďže obrobok nemá žiadny počiatočný pohyb, nedefinujeme preň žiadny pohyb. Pokračujte až k hornej matrici kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Horná matrica

Pri vstupe na stránku „Top die“ sa uistite, že pre hornú matricu je vybraný typ objektu **rigid**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Top die geometry“ (Geometria hornej matrice), kliknite na možnosť „load geometry from library“ (načítať geometriu z knižnice) ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a importujte geometriu **Block_TopDie.STL** z inštalačnej zložky programu DEFORM v adresári \3D\LABS. Geometria obdĺžnikového bloku by teraz mala byť viditeľná v grafickom okne. Odporúča sa skontrolovať geometriu objektu po jeho importe do programu DEFORM, aby ste sa uistili, že neobsahuje žiadne chyby. Na kontrolu geometrie kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Zobrazí sa okno „GEOMETRY CHECKING“, ktoré obsahuje prehľad geometrie objektu (pozri obr. 3DL1.14.). V prípade objektu s uzavretým objemom by mala byť 1 plocha, 0 voľných hrán a 0 neplatných entít. Objekty, ktoré sú importované ako plochy a nie ako telesa, budú mať voľnú hranu, ale aj tak by mali mať len 1 plochu.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0014.jpg' | relative_url }})

Okno s výsledkami kontroly geometrie

Okrem kontroly, či importovaná geometria neobsahuje chyby, je potrebné skontrolovať aj jej orientáciu. Ak ide o uzavretý objem, správna orientácia je daná vtedy, keď normály plôch smerujú von z objektu. Ak geometria nie je uzavretý objem, ale len povrch, správna orientácia je definovaná tak, že normály smerujú k obrobku. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_show_geometry_normal_vectors_option.jpg' | relative_url }}) si môžete zobraziť normály povrchu a ak normály povrchu nesmerujú správne von z objektu, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_reverse_label.jpg' | relative_url }}). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) sa vrátite na stránku s pohybmi hornej matrice.

**Pohyb hornej matrice**

Ak sa niektorá z foriem pohybuje, je potrebné tento pohyb definovať. V tejto simulácii sa horná forma bude pohybovať smerom nadol, aby stlačila blok.

Matrica sa bude pohybovať smerom nadol **konštantnou****rýchlosťou** **1** palca za sekundu. Na stránke „Pohyb“ prejdite na kartu „Posun“ a ako typ pohybu vyberte „Rýchlosť“. V poli **Rýchlosť** nastavte konštantnú hodnotu **1** palec/sek. Predvolený smer –**Z** je pre túto simuláciu správny. Pokračujte až k spodnej matrici kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Spodná matrica

Keď sa dostanete na stránku „Bottom die“, uistite sa, že pre spodnú matricu je vybraný typ „rigid object“. Kliknutím na tlačidlo „Next“ prejdite na stránku „Bop die geometry“, kliknite na možnosť „Load geometry from library“ a vyberte ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), potom importujte súbor s geometriou **Block_BottomDie.STL** z inštalačnej zložky DEFORM v adresári \3D\LABS. Pomocou tlačidiel ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_show_geometry_normal_vectors_option.jpg' | relative_url }}) skontrolujte, či geometria neobsahuje žiadne chyby a či normály plôch správne smerujú von z objektu. 

V tomto momente by mali byť všetky tri objekty viditeľné v okne DISPLAY.

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s nastavením polohy.

## Polohovanie

###  Automatické polohovanie

V prípade jednoduchého usporiadania s tromi objektmi, kde je horná matrica primárnou matricou, ak klikneme na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}), spodná matrica prejde procesom polohovania s ohľadom na kolízie s obrobkom v smere +Z a horná matrica prejde procesom polohovania s ohľadom na kolízie s obrobkom v smere -Z. (Pozri obr. 3DL1.15.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0015.jpg' | relative_url }})

Automatické polohovanie

### Umiestňovanie objektov

Okno „Umiestňovanie objektov“ otvoríte kliknutím na tlačidlo „Umiestniť objekty“ (pozri obr. 3DL1.16.). V programe DEFORM-3D sú k dispozícii nasledujúce metódy umiestňovania:

![]({{ '/assets/icons/pre_icons/mo_drag_radio_button.jpg' | relative_url }}) |  Objekty je možné umiestňovať tak, že ich pomocou myši presúvate v okne DISPLAY.  
---|---  
![]({{ '/assets/icons/pre_icons/mo_drop_radio_button.jpg' | relative_url }}) |  Objekty je možné upustiť v stanovenom smere a môžu sa posúvať a otáčať, kým sa nezastavia (nedosiahnu rovnovážny stav) v kontakte s ostatnými objektmi. Umístenie pri upustení je obzvlášť užitočné v prípadoch, keď je počiatočná poloha objektu nejasne definovaná, napríklad pri nepravidelne tvarovanej surovici, ktorá sa usadzuje v dutine.  
![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }}) |  Objekty je možné presunúť o definovanú vzdialenosť buď zadaním vektora vzdialenosti, alebo zadaním počiatočného a koncového bodu presunu.  
![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) |  Pri polohovaní metódou interferencie sa polohovaný objekt posúva tak, aby sa veľmi mierne prekrýval s referenčným objektom. Objekty je možné otáčať o definovaný uhol okolo ľubovoľnej osi.  
![]({{ '/assets/icons/pre_icons/mo_rotational_radio_button.jpg' | relative_url }}) |  Objekty je možné otočiť o definovaný uhol okolo ľubovoľnej osi.  
  
![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0016.jpg' | relative_url }})

Okno na umiestňovanie objektov

### Polohovanie pomocou ťahania

Kliknite na možnosť ![]({{ '/assets/icons/pre_icons/mo_drag_radio_button.jpg' | relative_url }}) a ako polohovací objekt vyberte **Blok**. V okne DISPLAY kliknite na šípku +Z a pretiahnite blok nahor tak, aby sa už nedotýkal spodnej formy. Zmeňte polohovací objekt na **hornú matricu** a pomocou šípky +Z ju posuňte nahor tak, aby sa už nedotýkala bloku, a potom pomocou šípky -Y ju umiestnite do polohy znázornenej nižšie. (Pozri obr. 3DL1.17.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0017.jpg' | relative_url }})

Polohovanie ťahaním

### Umiestnenie kvapiek

Ako príklad umiestnenia pomocou funkcie „Drop“ umiestnime blok na spodnú formu.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_drop_radio_button.jpg' | relative_url }}) a nastavte objekt na polohovanie na „Blok“. Zmeňte smer na -Z a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) vykonajte presun. (Pozri obr. 3DL1.18.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0018.jpg' | relative_url }})

Polohovanie kvapky

### Polohovanie s posunom

Ako príklad posunutia polohy posuňme **hornú formu** tak, aby ležala priamo na spodnej forme.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }}) a zmeňte polohovací objekt na „Top Die“. Existujú dva spôsoby polohovania pomocou posunu: 1) zadanie vektora vzdialenosti alebo 2) zadanie počiatočného a koncového bodu pohybu. Pri oboch týchto možnostiach môžete na definovanie parametrov vzdialenosti použiť myš.

Najjednoduchší spôsob, ako umiestniť hornú maticu na spodnú maticu, je použiť možnosť „Dva body“. Vyberte túto možnosť a ako počiatočný a koncový bod presunu vyberte body znázornené nižšie. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) vykonajte presun. (Pozri obr. 3DL1.19.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0019.jpg' | relative_url }})

Polohovanie s posunom

### Určovanie polohy na základe interferencie

Horná forma by teraz mala ležať priamo na spodnej forme. Použime polohovanie pomocou interferencie, aby sme hornú formu vrátili späť do správnej polohy na vrchole bloku.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). V dialógovom okne pre polohovanie by objektom polohovania už mal byť **Top Die**. Zmeňte referenčný bod na Block, ak tak ešte nebolo urobené. Keďže sa Top Die musí pohybovať smerom nadol, aby sa dotkol hornej časti Blocku, zmeňte smer priblíženia na **-Z**. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) na umiestnenie hornej matrice. (Pozrite obr. 3DL1.20. a obr. 3DL1.21.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0021.jpg' | relative_url }})

Okno na umiestňovanie objektov

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0020.jpg' | relative_url }})

Rušenie objektov

Po dokončení tohto nastavovania polohy kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste opustili okno OBJECT POSITIONING.

Pokračujte na stránku s kontaktnými údajmi kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

**Poznámka:**

Kedykoľvek v okne [Object Positioning]({{ '/docs/sk/pre_processor/19_object_positioning/19_object_positioning/' | relative_url }}) môžete pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_cancel_button.jpg' | relative_url }}) alebo ![]({{ '/assets/icons/pre_icons/mo_reset_button.jpg' | relative_url }}) vrátiť objekty do polôh, v ktorých sa nachádzali pred otvorením okna „Umiestnenie objektov“.

## Vzťahy medzi objektmi

Na stránke „Kontakt“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) – pridajú sa dva vzťahy. Vzťahy v programe DEFORM sú definované vo vzťahu k objektom typu „Master“ a „Slave“. V tejto simulácii dochádza k deformácii obrobku medzi dvoma tuhými formami. Tuhé formy sú definované ako hlavné objekty a deformovaný obrobok je definovaný ako podriadený objekt.

Pre každý z týchto vzťahov je možné definovať niekoľko vlastností rozhrania (hlavne trenie a koeficient prenosu tepla). Keďže táto simulácia nebude zohľadňovať žiadny prenos tepla, jedinou vlastnosťou rozhrania, ktorú je potrebné definovať, je trenie. (Pozri obr. 3DL1.22.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0022.jpg' | relative_url }})

Kontaktný formulár

Keď je zvýraznený prvý vzťah, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}), aby ste vzťah upravili. V časti obrazovky venovanej treniu sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné procesy tvárnenia. Keďže táto simulácia prebieha pri izbovej teplote a lisovacie formy sú oceľové, použite roletové menu a zo zoznamu vyberte možnosť „Tvarovanie za studena (oceľové lisovacie formy)“ (pozri obr. 3DL1.23.). Automaticky sa vyberie hodnota trenia 0,12. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite na hlavnú stránku kontaktu.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0023.jpg' | relative_url }})

Okno definície údajov medzi objektmi

Teraz, keď bol definovaný vzťah medzi hornou maticou a blokom, je potrebné definovať vzťah medzi spodnou maticou a blokom. Keďže podmienky trenia sú rovnaké medzi obrobkom a oboma maticami, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) je možné skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných. Po vykonaní tejto operácie budú mať oba vzťahy definované trenie 0,12. (Pozri obr. 3DL1.24.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0024.jpg' | relative_url }})

Kontaktné okno

Po definovaní vzťahov je potrebné vytvoriť kontakt medzi objektmi. Pri vytvorení kontaktu sa všetky uzly na deformujúcom sa objekte (Slave), ktoré sa nachádzajú v rámci špecifikovanej tolerancie voči forme (Master), premiestnia na povrch formy.

Pred vytvorením kontaktu musíme určiť primeranú hodnotu tolerancie. Príliš veľká tolerancia spôsobí, že sa príliš veľa uzlov dostane do kontaktu s povrchom formy, čo môže viesť k deformácii siete obrobku. Príliš malá tolerancia bude znamenať, že v kontaktnom páse sa nachádza príliš málo uzlov a vygeneruje sa len veľmi malý kontakt. Kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) v sekcii Tolerancia program DEFORM určí primeranú hodnotu tolerancie. Vypočíta sa tolerancia 0,0046" a automaticky sa zadá do programu.

Po nastavení tejto tolerancie kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}), čím sa vytvorí kontakt medzi objektmi. Kontakt sa vytvorí medzi blokom a oboma maticami a tento kontakt sa v okne DISPLAY zobrazí ako farebné bodky na hornej a spodnej ploche bloku.

**Poznámka:**

Ak sa pri generovaní kontaktu použije príliš veľká tolerancia a dôjde k deformácii siete obrobku, je možné pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_restore_mesh_button.jpg' | relative_url }}) vrátiť späť generovanie kontaktu.

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Krok“.

## Nastavenie ovládacích prvkov krokov

Na stránke „Step“ nastavte **Počet****simulačných****krokov** na **20**. Pokiaľ sa simulácia nezastaví predčasne, prebehne 20 krokov. Nastavte **Krok****prirastania** na **Uložiť** na hodnotu **2**. Každý druhý krok simulácie sa zapíše do databázy. Všimnite si, že v tomto okne sa zobrazuje aj primárna matrica. Nastavte primárnu matricu na hornú matricu, práve táto matrica sa bude používať ako ovládací prvok pre mnohé ovládacie prvky krokovania a zastavenia (pozri obr. 3DL1.25).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0025.jpg' | relative_url }})

Stránka na ovládanie krokov

Teraz je potrebné určiť vhodnú veľkosť kroku pre simuláciu. Pri väčšine simulácií by sa dĺžka zdvihu matrice na jeden krok mala nastaviť na približne 1/3 typickej dĺžky hrany prvku. Na určenie tejto hodnoty možno použiť nástroj „Measure ![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }})“. Kliknite na ikonu a potom zmerajte ľubovoľnú dĺžku hrany na bloku (možno budete musieť kliknúť na ![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}), aby sa zobrazila tieňovaná sieť). Typická dĺžka hrany je približne 0,4". Jedna tretina z 0,4" je približne 0,13". V časti „Definícia krokov riešenia“ vyberte rádio tlačidlo „S konštantným posunom matrice“ a zadajte hodnotu **0,13**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Vytvorenie databázy“.

## Vytvorenie databázy

Po úplnom nastavení úlohy je posledným krokom vytvorenie databázového súboru. Modul FEM (časť programu DEFORM®, ktorá vypočítava riešenie) používa databázový súbor na ukladanie riešení úlohy metódou konečných prvkov. Pri generovaní databázy v preprocesore DEFORM sa všetky informácie definované v preprocesore (napríklad vlastnosti materiálov, riadenie pohybov, geometrie objektov atď.) prenesú do databázového súboru.

Na stránke „Generation DB“. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) spustíte kontrolu programu, či sa pri nastavení úlohy na niečo nezabudlo. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch). 

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}). 

## Spustenie simulácie

Kliknite na označenie akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“ (pozri obr. 3DL1.26). Otvorí sa dialógové okno „Možnosti spustenia“, ako je znázornené na obr. 3DL1.27. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0032.jpg' | relative_url }})

Možnosti simulácie

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0027.jpg' | relative_url }})

Spustiť okno simulácie

Priebeh simulácie je možné počas jej vykonávania sledovať prostredníctvom okien „Simulation Message“ a „Process Monitor“ v režime simulácie. Kliknutím na kartu „Simulation Message“ zobrazíte súbor správ. Pokiaľ je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}), čo je predvolené nastavenie, súbor správ sa bude aktualizovať každých pár sekúnd.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Po ukončení simulácie sa na koniec súboru správ pridá nasledujúca správa: NORMAL STOP: Pridelené kroky boli dokončené, ako je znázornené na (pozri obr. 3DL1.28.).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0028.jpg' | relative_url }})

Karta „Simulačné správy“

## Následné spracovanie výsledkov

Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), čím sa otvorí postprocesor MO. (Pozri obr. 3DL1.29.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0029.jpg' | relative_url }})

Okno postprocesora MO

### Nástroje pre kroky a výber krokov

Na výber kroku, ktorý chcete zobraziť, slúži stránka prehliadača krokov. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) v prehliadači krokov; keď kliknete na tlačidlo „Všetko“, v prehliadači krokov sa zobrazia všetky uložené kroky. Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_step_list.jpg' | relative_url }}) môžete otvoriť okno ZOZNAM KROKOV, ktoré umožňuje používateľovi definovať podrobnejšie nastavenia krokov.

### Premenné stavu

Niektoré z najčastejšie používaných stavových premenných si môžete pozrieť na stránke nástrojov príspevku. (Pozri obr. 3DL1.30.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0030.jpg' | relative_url }})

Stránka Nástroje príspevkov

Zvoľte možnosť „Strain-Effective“ v položke „Post-Tolls“, aby ste zistili mieru deformácie, ktorú obrobok utrpel. Kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) otvoríte okno STATE VARIABLE (Premenná stavu) a ako možnosť Scaling (Mierka) vyberte ![]({{ '/assets/icons/post_icons/mo_local_scaling_radio_button.jpg' | relative_url }}). Táto možnosť použije lokálne minimálne a maximálne efektívne deformácie ako krajné hodnoty na farebnej lište. Prejdite jednotlivými krokmi simulácie a sledujte akumuláciu deformácie.

Pomocou ikony ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) je možné otvoriť všetky možnosti stavových premenných.

### Sledovanie bodov

V programe DEFORM je možné počas simulácie sledovať body v objekte. Sledovať sa dá nielen poloha bodov, ale aj stavové premenné v týchto miestach. Okno „Point Tracking“ otvoríte kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }}).

Chceme určiť niekoľko bodov na nedeformovanej geometrii a sledovať, kam sa posúvajú pri deformácii dielu. Ak chcete zobraziť nedeformovanú geometriu, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_preview_first_step_icon.jpg' | relative_url }}), čím sa zobrazí prvý krok simulácie. Teraz kliknite na tri miesta na obrobku (pozri obr. 3DL1.31), potvrďte predvolenú možnosť Sledovanie a kliknite na ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0031.jpg' | relative_url }})

Body sledovania

Keď sa z roletového menu „State Variable“ vyberie stavová premenná, v okne DISPLAY sa zobrazí graf sledovania polohy týchto troch bodov.

Kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) spustíte prehrávanie jednotlivých krokov. Zistíte, že pri zmene krokov sa na grafe sledovania bodov zvýrazní aj príslušný krok. Kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_preview_stop_button.jpg' | relative_url }}) zastavíte prehrávanie krokov. Teraz kliknite kdekoľvek na grafe sledovania bodov – vybraný krok zobrazený v okne DISPLAY by sa mal zmeniť tak, aby zodpovedal polohe vybranej na grafe. (Pozri obr. 3DL1.32.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0032.jpg' | relative_url }})

Graf sledovania bodov

### Krájanie objektov

V programe DEFORM je možné objekt rozrezať a následne zobraziť rôzne stavové premenné v rámci objektu. Najprv skryjeme graf „Point Tracking“ tak, že klikneme pravým tlačidlom myši na položku „Point Tracking“ v stromovej štruktúre objektov a vyberieme možnosť „Hide Point Tracking graph“ (pozri obr. 3DL1.33).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0033.jpg' | relative_url }})

Možnosť sledovania bodov RMB v strome objektov

Kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_slice.jpg' | relative_url }}) otvoríte okno „Slicing“. Objekty je možné rozrezať viacerými spôsobmi. Objekty v okne „DISPLAY“ sú ohraničené žltým obdĺžnikovým rámčekom. Kliknutím na vertikálny okraj rámčeka vytvoríte horizontálnu rovinu rezu. Kliknutím na horizontálny okraj rámčeka vytvoríte vertikálnu rovinu rezu. Kliknite na žltý rámček na viacerých miestach a vyskúšajte si túto možnosť rezania. (Pozri obr. 3DL1.34.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0034.jpg' | relative_url }})

Rezanie objektov

Rezné roviny sú definované bodom na rovine a smerom normály k tejto rovine. V okne SLICING sú označené písmenami P (Point – bod) a N (Normal – normála). 

Objekty je možné rozrezať aj tak, že vyberiete súradnicu X, Y alebo Z bodu a potom pomocou posuvníka túto súradnicu potiahnete nahor alebo nadol. Pri pohybe posuvníka sa objekty budú dynamicky rozrezávať. Kliknite na súradnicu X bodu, ako je znázornené na obr. 3DL1.35, a potom posúvajte posuvník dopredu a dozadu, aby ste objekty rozrezali.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0035.jpg' | relative_url }})

Okno na krájanie 

Na určenie spôsobu zobrazenia rezaných plôch je k dispozícii niekoľko možností. (Pozri obr. 3DL1.36.) Po dokončení rezania kliknite na tlačidlo „OK“ na stránke rezania.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0036.jpg' | relative_url }})

Rezacie plochy

## Ukončenie sprievodcu MO

Keď skončíte, ukončite postprocesor MO kliknutím na ikonu zatvorenia ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }}).
