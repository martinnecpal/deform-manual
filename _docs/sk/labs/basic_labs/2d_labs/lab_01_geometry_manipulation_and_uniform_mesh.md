---
lang: sk
title: "Laboratórium 01: Manipulácia s geometriou a jednotná sieť"
---

# Laboratórium 01: Manipulácia s geometriou a rovnomerná sieť

  
1.1. Vytvorenie nového problému

1.2. Pridanie operácie tvarovania

1.3. Výber typu geometrie

1.4. Pridanie objektu

1.5. Obrobok

1.6. Vytvorenie geometrie obrobku

1.7. Stránka so sieťou obrobku

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main, ako je znázornené nižšie. (Pozri obr. L1.1.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno grafického rozhrania programu DEFORM

Novú úlohu vytvoríte buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nová úloha**, alebo kliknutím na ikonu Nová úloha ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. L1.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Názov úlohy zadajte ako „**Mesh**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa sprievodca hromadnými operáciami s dialógovým oknom Nový projekt (pozri obr. L1.3.), kde bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**Mesh**“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0003.jpg' | relative_url }})

Sprievodca MO – Nový projekt

Používateľ môže tiež zmeniť systém jednotiek a pridať operáciu výberom z roletového zoznamu „Prvá operácia“ a zaškrtnutím príslušného políčka (pozri obr. L1.4.). Pomocou možnosti „Kopírovať existujúci projekt“ môžeme importovať predtým uložené projekty ako nové projekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie. 

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0004.jpg' | relative_url }})

Nastavenia okna nového projektu

## Pridanie operácie tvarovania

Sprievodca viacerými operáciami otvorí nový projekt. Pridajte operáciu 2D tvárnenia zo zoznamu operácií v Průzkumníku. Operáciu je možné pridať kliknutím na tlačidlo operácie 2D tvárnenia ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) (pozri obr. L1.5.) alebo ju môžete pridať aj pretiahnutím do Editoru operácií.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0005.jpg' | relative_url }})

Do editora operácií bola pridaná operácia 2D tvárnenia

## Výber typu geometrie

V tomto cvičení používame osovo symetrické geometrie, preto na stránke s typom geometrie zaškrtnite políčko „2D Axisymmetric“ a potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Object“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0006.jpg' | relative_url }})

Výber typu osovo symetrickej geometrie

## Pridanie objektu

V tomto laboratórnom cvičení potrebujeme len jeden objekt. Ak sa v zozname objektov už nachádzajú tri objekty, odstráňte posledné dva objekty kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) a v zozname ponechajte len objekt „Workpiece“ (pozri obr. L1.7.), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0007.jpg' | relative_url }})

Okno na pridávanie objektov

## Obrobok

V okne „Workpiece“ (Obrobok) zmeňte názov objektu na **Billet** a ako typ objektu vyberte **Plastic**, ako je znázornené na obr. L1.8. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0008.jpg' | relative_url }})

Objekt „Billet“ – Okno

## Vytvorenie geometrie obrobku

V programe DEFORM-2D sa definícia povrchu objektu označuje ako jeho geometria. Geometriu objektu je možné vytvoriť priamo v programe DEFORM alebo ju importovať ako súbor vo formáte .dxf alebo .igs. V tomto cvičení sa geometria polotovaru vytvorí priamo v programe DEFORM.

Na stránke „Geometria“ kliknite na označenie ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a prezrite si dostupné možnosti na vytvorenie a úpravu geometrie (pozri obr. L1.9.),

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0009.jpg' | relative_url }})

Okno „Upraviť geometriu“

**Vybrať**![]({{ '/assets/icons/pre_icons/mo_click_select.jpg' | relative_url }}) :**** Nástroj „Vybrať“ slúži na výber vrcholu alebo hrany geometrie. Pomocou tohto nástroja je možné vrchol alebo hranu umiestniť ťahaním a púšťaním.

**Výber oblasti** ![]({{ '/assets/icons/pre_icons/mo_area select.jpg' | relative_url }}): Nástroj „Výber oblasti“ slúži na výber geometrie viacerých prvkov v rámci obdĺžnika.

**Vytvoriť slučku** ![]({{ '/assets/icons/pre_icons/mo_create_loop.jpg' | relative_url }}): Nástroj „Vytvoriť slučku“ slúži na vytvorenie geometrickej slučky tak, že sa vytvoria body a spojia sa. 

**Pridať bod do slučky** ![]({{ '/assets/icons/pre_icons/mo_add_points_to_loop.jpg' | relative_url }}): Nástroj „Pridať bod do slučky“ slúži na pridávanie nových bodov do existujúcej slučky.

**Odstrániť bod** ![]({{ '/assets/icons/pre_icons/mo_delete point.jpg' | relative_url }}): Nástroj „Odstrániť bod“ slúži na odstránenie bodu zo slučky.

**Zaoblený roh**![]({{ '/assets/icons/pre_icons/mo_round_corner.jpg' | relative_url }}) : Nástroj „Zaoblený roh“ slúži na vytvorenie zaoblenia vo vybranom bode.

**Nastavenie uhla** ![]({{ '/assets/icons/pre_icons/mo_set_angle.jpg' | relative_url }}): slúži na zmenu uhla hrany.

**Presun**![]({{ '/assets/icons/pre_icons/mo_move.jpg' | relative_url }}): slúži na presun bodu.

**Presunúť na stredovú čiaru ![]({{ '/assets/icons/pre_icons/mo_move_to_centerline.jpg' | relative_url }}) **: slúži na presun bodu najbližšieho k slučke na stredovú čiaru

**Posun** ![]({{ '/assets/icons/pre_icons/mo_offset.jpg' | relative_url }}): Nástroj „Posun“ slúži na zmenu veľkosti geometrickej slučky.

**Nastaviť prvý bod** ![]({{ '/assets/icons/pre_icons/mo_make_first_point.jpg' | relative_url }}): Nástroj „Nastaviť prvý bod“ slúži na to, aby sa vybraný bod stal prvým bodom v slučke; táto funkcia sa používa pri uzavretých slučkách a ako prvý bod nemožno nastaviť stred oblúka.

**Zmena smeru** ![]({{ '/assets/icons/pre_icons/mo_reverse_direction.jpg' | relative_url }}): Funkcia „Zmena smeru“ slúži na zmenu smeru slučky s cieľom zmeniť orientáciu geometrie. Geometria by mala byť vytvorená proti smeru hodinových ručičiek; ak je vytvorená v smere hodinových ručičiek, pomocou tejto možnosti môžeme zmeniť smer slučky.

**Uzavretá slučka**![]({{ '/assets/icons/pre_icons/mo_close_loop.jpg' | relative_url }}) : Nástroj na uzavretie slučky sa používa na uzavretie otvorenej slučky

**Rozdelenie slučky**![]({{ '/assets/icons/pre_icons/mo_split_loop.jpg' | relative_url }}) : Nástroj na rozdelenie slučky slúži na rozdelenie slučky vo vybranom bode

**Podslučka**![]({{ '/assets/icons/pre_icons/mo_sub_loop.jpg' | relative_url }}): Nástroj „Podslučka“ slúži na výber vnútornej slučky ako podslučky v prípade topológie s viacerými slučkami; jej výberom môžeme priradiť materiál k geometrii s viacerými slučkami

**Spojenie slučiek** ![]({{ '/assets/icons/pre_icons/mo_join_loop.jpg' | relative_url }}): Funkcia „Spojenie slučiek“ slúži na zlúčenie dvoch slučiek výberom slučiek, ktoré sa majú spojiť; koncový bod prvej slučky sa spojí s prvým bodom druhej slučky

**Spojiť všetky slučky** ![]({{ '/assets/icons/pre_icons/mo_join_all_loops.jpg' | relative_url }}): Nástroj „Spojiť všetky slučky“ slúži na zlúčenie všetkých slučiek.

**Odstrániť vybrané** ![]({{ '/assets/icons/pre_icons/mo_delete_selected.jpg' | relative_url }}): Funkcia „Odstrániť vybrané“ slúži na odstránenie vybraných slučiek alebo hrán.

**Odstrániť nevybrané** ![]({{ '/assets/icons/pre_icons/mo_delete_unselected.jpg' | relative_url }}) : Funkcia „Odstrániť nevybrané“ slúži na odstránenie nevybraných hrán slučiek.

**Zobraziť vrcholy** ![]({{ '/assets/icons/pre_icons/mo_show_vertex.jpg' | relative_url }}): slúži na zobrazenie vrcholov geometrie.

**Zobraziť čísla vrcholov** ![]({{ '/assets/icons/pre_icons/mo_show_vertex_numbers_icon.jpg' | relative_url }}) : slúži na zobrazenie čísel vrcholov geometrie.

**Zobraziť vnútro**![]({{ '/assets/icons/pre_icons/mo_show_inside.jpg' | relative_url }}): slúži na zobrazenie orientácie geometrie.

**Zobraziť smer hrany** ![]({{ '/assets/icons/pre_icons/mo_show_edge_direction.jpg' | relative_url }}) : slúži na znázornenie smeru vytvorenej slučky.

**Zobraziť materiál** ![]({{ '/assets/icons/pre_icons/mo_material_icon.jpg' | relative_url }}): slúži na načítanie a priradenie materiálu k oblasti geometrie.

**Mriežkové čiary**: V okne zobrazenia sa zobrazujú mriežkové čiary v horizontálnom aj vertikálnom smere. 

**Body mriežky**: V okne zobrazenia sa zobrazujú body mriežky v horizontálnom a vertikálnom smere.

**Mriežka: žiadna**: Ak je táto možnosť zvolená, body mriežky a čiary mriežky v horizontálnom a vertikálnom smere sa v okne zobrazenia nezobrazujú.

Na karte **Objekty** môžeme vybrať objekt zo zoznamu, čím sa v grafickom okne skryje geometria vybraného objektu.

Na karte **Geometria** môžeme zadávať alebo upravovať geometrické prvky. Geometrické prvky je možné zadávať dvoma spôsobmi: metódou „Čiara-oblouk“ a metódou „XYR“.

Na karte **l****oop** môžeme načítať materiál a priradiť ho k vybraným slučkám. Okrem toho si môžeme pozrieť priradený materiál v podrobnostiach príslušnej slučky.

V tomto cvičení vytvoríme geometriu tak, že do tabuľky 1 zadáme nasledujúce hodnoty súradníc XYR (pozri obr. L1.10) a klikneme na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

X |  Y |  R  
---|---|---  
0 |  0 |  0  
1,5 |  0 |  0,12  
1,5 |  4 |  0,12  
0 |  4 |  0  
  
Hodnota súradníc XYR v geometrii

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0010.jpg' | relative_url }})

Stránka „Úprava 2D geometrie“

Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), použite predvolené parametre kontroly a kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}), ako je znázornené na obr. L1.11. Zobrazí sa správa: „Geometria je správna“. Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0011.jpg' | relative_url }})

Okno „Skontrolovať a opraviť geometriu“

## Stránka so sieťou obrobku

Prepnite do režimu pre pokročilých kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Prepnúť do režimu pre pokročilých). Režim pre pokročilých ponúka viac možností pre podrobné nastavenia.

### Vytvorenie siete pri predvolených nastaveniach

Pri použití predvolených nastavení siete (pomer veľkostí 3 a počet prvkov 1000) vygenerujte sieť kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obr. L1.12.

Pomer veľkostí určuje rozdiel medzi najmenším a najväčším prvkom. Pri pomere 3 je najmenší prvok veľký 1/3 najväčšieho prvku. Váhovacie faktory určujú, kde sa v objekte umiestnia malé a veľké prvky.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0012.jpg' | relative_url }})

Sieť vygenerovaná pre pomer veľkostí 3

### Vytvorenie rovnomernej siete

Ak chcete na objekte vytvoriť jednotnú sieť, v ktorej majú všetky prvky rovnakú veľkosť, nastavte pomer veľkostí (Size Ratio) na hodnotu 1 a opäť kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). (Pozri obr. L1.13.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0013.jpg' | relative_url }})

Sieť vygenerovaná pre pomer veľkostí 1

**Poznámka**: Je dôležité vedieť, že pri vytvorení novej siete sa všetky informácie o starej sieti stratia.

**Súvisiace témy:**

[12.2. 2D Geometry Data Editing]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/' | relative_url }})
