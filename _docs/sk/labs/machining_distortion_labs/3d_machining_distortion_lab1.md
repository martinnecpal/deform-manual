---
lang: sk
title: "Laboratórium deformácií pri 3D obrábaní 1"
---

# Laboratórium deformácií pri 3D obrábaní 1

1.1. Vytvorenie nového problému

1.2. Operácia sčítania

1.3. Okno objektu

1.4. Obrobok

1.5. Inštalácia svietidiel

1.6. Definovanie počiatočného obrábacieho cyklu

1.7. Okno ovládacích prvkov:

1.8. Plánované umiestnenie

1.9. Kontakt

1.10. Náhľad simulácie

1.11. Riadenie simulácie

1.12. Vytvorenie databázy

1.13. Spustenie simulácie

1.14. Následné spracovanie výsledkov

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené na obrázku [Fig. 3DMDL1.1.]({{ '/docs/sk/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/' | relative_url }}#Fig_3DHTWL1_1_DEFORM_GUI_main_window)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno programu DEFORM GUI

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 3DMDL1.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte systém jednotiek pomocou prepínača „**Anglický**“. Názov úlohy zadajte ako „******3D_Machining_Distortion******“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „Zobraziť dialógové okno s možnosťami“, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém pomocou integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa okno „Integrated Manufacturing Process“. V tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**3D_Machining_Distortion**“ (pozri obr. 3DMDL1.3.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0003.jpg' | relative_url }})

Okno nového projektu

## Pridávanie operácie

Otvorí sa sprievodca viacerými operáciami. Zoznamu operácií v prehliadači pridajte 3D operáciu **Deformácia pri obrábaní**. Operáciu je možné pridať kliknutím na tlačidlo 3D operácie Deformácia pri obrábaní ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo ju môžete pridať aj pretiahnutím do editora operácií (pozri obr. 3DMDL1.4.).

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0004.jpg' | relative_url }})

Zohľadnenie deformácie pri 3D obrábaní

## Okno objektu

V okne objektov je pre toto laboratórne cvičenie potrebné okrem obrobku aj 4 upínacie prípravky a 1 priechod. Nastavte teda **počet upínacích prípravkov** na **4** a počet priechodov **na** 1 a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) pridajte objekty „Fixtures“ a „Pass“ (pozri obr. 3DMDL1.5.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte ďalej.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0005.jpg' | relative_url }})

Okno objektu

## Obrobok

Na stránke obrobku načítajte informácie o objekte výberom možnosti ![]({{ '/assets/icons/pre_icons/mo_import_object.._button.jpg' | relative_url }}). Používateľ môže vyhľadať súbor databázy. Načítajte súbor „**CoolingModel.DB**“ z inštalačnej zložky Deform \3d\**LABS** \**Machining_Distortion** a vyberte príslušné číslo kroku (posledný krok pre toto cvičenie) a objekt (tento model má len jeden objekt) (pozri obr. 3DMDL1.6.). Pre toto cvičenie sú k dispozícii dva súbory. Jeden súbor kľúčových slov a jeden databázový súbor pre typickú simuláciu chladenia. Uvedený súbor kľúčových slov bol spustený na vytvorenie databázového súboru.

Po načítaní objektu môže používateľ zmeniť jeho názov a zapnúť funkciu „init displacement“, aby bolo možné správne zaznamenať deformáciu spôsobenú výlučne odoberaním materiálu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0006.jpg' | relative_url }})

Okno na importovanie obrobkov

V okne „Hraničné podmienky“ zvoľte vo všetkých smeroch „Fixed Velocity BCC“ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

V okne „Initialize“ sú k dispozícii na inicializáciu niektoré bežne používané stavové premenné, ako napríklad teplota, deformácia, napätie, poškodenie, rýchlosť, posunutie atď. Používateľ môže hodnoty týchto stavových premenných inicializovať tak, že zadá hodnotu do vstupného poľa a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). V tomto laboratórnom cvičení nebudeme inicializovať žiadne údaje. Použite teda predvolené hodnoty zo simulovanej databázy a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0007.jpg' | relative_url }})

Inicializovať okno

## Inštalácia svietidiel

V okne „Objekt“ je počet svietidiel nastavený na štyri; v tomto laboratórnom cvičení sa využívajú všetky štyri svietidlá. Dve sa nachádzajú v blízkosti osi a dve na vzdialenejšom konci. Je možné ich načítať (alebo definovať) v ľubovoľnom poradí. Po načítaní môže používateľ skontrolovať geometriu a v prípade potreby ju upraviť.

### Zápas č. 1

V okne „Fixture 1“ zadajte názov upínacieho prípravku (ak sa má líšiť od predvoleného) a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) načítajte alebo definujte geometriu upínacieho prípravku. (pozri obr. 3DMDL1.8.) Geometriu upínacieho prípravku je možné definovať pomocou základných tvarov (ktoré je v prípade potreby možné aj interaktívne upravovať) alebo načítať existujúci súbor s geometriou. Pre toto laboratórne cvičenie (pozri obr. 3DMDL1.9.) načítajeme upínací prípravok 1 ako ten vľavo dole **(lb_fixture.GEO**) z inštalačnej cesty \3d\LABS\Machining_Distortion.

### Zápas č. 2

Podobne ako v prípade Fixture 1, aj pre Fixture 2 načítajte súbor v ľavom hornom rohu (**lu_fixture.GEO**) z inštalačnej zložky \3d\LABS\Machining_Distortion.

### Zápas č. 3

Podobne ako v prípade prípravku 1, aj v prípade prípravku 3 načítajte spodný súbor (**rb_fixture.GEO**) z inštalačnej zložky \3d\LABS\Machining_Distortion.

### Zápas č. 4

Podobne ako v prípade Fixture 1, aj pre Fixture 4 načítajte súbor v pravom hornom rohu (**ru_fixture.GEO**) z inštalačnej cesty \3d\LABS\Machining_Distortion.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0008.jpg' | relative_url }})

Okno zápasu č. 1

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0009.jpg' | relative_url }})

Okno Geometria

## Definovanie počiatočného obrábacieho cyklu

Z hľadiska modelu sú informácie o obrábacom priechode tiež geometrickými údajmi. Ak sa geometria priechodu prekrýva so surovcom, určuje polohu a rozsah materiálu určeného na odstránenie. Ide teda tiež o geometrické údaje, ktoré je možné definovať/načítať rovnakým spôsobom ako upínacie prípravky v predchádzajúcom kroku. Pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Import geometrie) (obr. 3DMDL1.11.) načítajte súbor „**pass1.GEO**“ z inštalačnej cesty \3d\LABS\Machining_Distortion. Používateľ si môže túto geometriu skontrolovať.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0010.jpg' | relative_url }})

Okno prechodu

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0011.jpg' | relative_url }})

Okno Geometria

## Okno ovládacích prvkov

V tejto operácii umiestňujeme upínacie prvky vo vzťahu k polotovaru. Zvoľte možnosť ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}), aby ste otvorili dialógové okno „Umiestňovanie objektov“. Tu zvoľte režim umiestňovania „Interferencia“. Zo zoznamu objektov vyberte „Polotovar“ ako referenčný objekt a postupne vyberte upínacie prvky 1 až 4 na umiestnenie. (Obr. 3DMDL1.13.) Pre každú dvojicu je potrebné zvoliť správny smer priblíženia na polohovanie. Smer priblíženia pre spodné upínacie prvky by mal byť „Z“ a pre horné upínacie prvky „-Z“. Používateľ môže použiť predvolenú hodnotu kolízie a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) vykonať polohovanie každého upínacieho prvku.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0012.jpg' | relative_url }})

Okno ovládacích prvkov

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0013.jpg' | relative_url }})

Okno „Poloha objektu“

## Plánované polohovanie

Plánované umiestňovanie umožňuje používateľovi definovať umiestnenie objektov v nastavení MO pre nasledujúce operácie, pre ktoré sa nevytvára databáza. Týmto spôsobom sa objekty umiestnia ešte pred vytvorením databázy počas spustenia simulácie v dávkovom režime. V tomto laboratórnom cvičení nepoužívame plánované umiestňovanie.

## Kontakt

V tejto fáze definujeme „4“ páry objektov typu „master-slave“. V dialógovom okne „Inter Object“ (obr. 3DMDL1.14.) vyberte typ kontaktu „user“ a štyrikrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), čím definujete štyri páry vzťahov medzi objektmi. Pre každý pár postupne vyberte jedno upínacie zariadenie ako hlavný objekt a polotovar ako podriadený objekt. alebo

Používateľ môže priamo kliknúť na ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}), aby pridal všetky predvolené vzťahy, a pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určiť vhodnú toleranciu kontaktu

V tomto laboratórnom cvičení nedefinujeme žiadne podmienky trenia. (V prípade potreby môže používateľ zvoliť možnosť ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Upraviť) a definovať podmienky trenia.) Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vygenerujete podmienky kontaktu. V tejto fáze sa kontaktné uzly zvýraznia v zobrazovacej oblasti. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0014.jpg' | relative_url }})

Kontaktný formulár

## Náhľad simulácie

Náhľad simulácie poskytuje prehľad o operácii, ktorá sa má vykonať, na základe definície procesu a cyklu. Pre 3D objekt máme k dispozícii dve boolovské metódy,

  * **Na základe geometrie (nová metóda)**: Ak pri vykonávaní booleovskej operácie použijeme možnosť „Na základe geometrie“, program najprv vykoná booleovskú operáciu a následne vykoná lokálne prečlenenie novej plochy, ktorá vznikla po booleovskej operácii, podľa definovaných nastavení prečlenenia. Týmto spôsobom sa vytvorí hladká sieť, ako je znázornené na obr. 3DMDL1.15.

  * **Na základe pevnej siete (starý spôsob)**: Ak pri použití metódy pevnej siete vykonáme boolovskú operáciu, vykoná sa boolovská operácia na objekte a následne sa vygeneruje nová sieť pre nový povrch; nový povrch nemusí byť hladký, a preto ani vygenerovaná sieť nebude vyzerať hladko, ako je znázornené na obr. 3DMDL1.15.

V tomto laboratórnom cvičení použijeme metódu založenú na geometrii pre booleovskú operáciu s predvolenými nastaveniami lokálneho prečlenenia, preto vyberte voľbu **Geometry based (new method)** a sledujte náhľad simulácie. V okne Náhľad simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) spustíte animáciu, ktorá zobrazí objekt, ktorý bol po prechode odstránený (pozri obr. 3DMDL1.16.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0015.jpg' | relative_url }})

Výstup 3D booleovských metód

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0016.jpg' | relative_url }})

Okno náhľadu simulácie

## Riadenie simulácie

Posledným krokom pri generovaní údajov pre model je nastavenie parametrov simulácie, kde definujeme počiatočný krok ako „-1“, počet krokov ako „2“ s ukladaním každého kroku a čas na jeden krok ako „1 sekunda“, ako je znázornené na obr. 3DMDL1.17. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku generovania databázy.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0017.jpg' | relative_url }})

Okno riadenia simulácie

## Vytvorenie databázy

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vygenerovali databázu. Keď program dokončí zapisovanie databázy, prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

## Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“ – otvorí sa dialógové okno „Možnosti spustenia“. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Po dokončení simulácie môžeme vidieť, že na koniec súboru Message bola pridaná nasledujúca správa:

******Správa*******

Simulácia bola dokončená a zastavená v časovom kroku určenom používateľom.

## Následné spracovanie výsledkov

Po dokončení simulácie môže používateľ zadať ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), aby si prezrel výsledky modelu. Bežný postup spočíva v tom, že najskôr sa vyberie číslo kroku a potom stavové premenné, ktoré sa majú zobraziť. Niektoré dôležité stavové premenné je možné vybrať priamo z post-procesorov a k ostatným sa dá dostať prostredníctvom tabuľky ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) (výberom). Obr. 3DMDL1.18 znázorňuje rozloženie efektívneho napätia po obrábacom cykle a obr. 3DMDL1.19 znázorňuje rozloženie maximálneho hlavného napätia po obrábacom cykle.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0018.jpg' | relative_url }})

Rozloženie efektívneho napätia a deformácia polotovaru po obrábacom cykle

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0019.jpg' | relative_url }})

Rozloženie maximálneho hlavného napätia a deformovaný polotovar po obrábacom cykle
