---
lang: sk
title: "12.2. Úprava údajov 2D geometrie"
---

# 12.2. Úprava údajov 2D geometrie

12.2.1. Nástroje na úpravu 2D geometrie

12.2.2. Zobrazenie alebo zobrazenie možností úprav

12.2.3. Možnosti vlastností 2D editora geometrie

12.2.4. Importovanie viacerých hraničných geometrií

12.2.5. Definovanie a úprava viacerých hraničných geometrií

Editor 2D geometrie sa používa na vytvorenie geometrie objektu alebo na úpravu existujúcej geometrie. Importovanú geometriu možno upraviť v okne Upraviť geometriu. Táto možnosť je prístupná zo stránky Geometria kliknutím na štítok ![](../../../assets/Icons/Pre_icons/MO_Edit_lable.jpg), ako je znázornené na obr. 12.2.1.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image001.jpg)

Možnosť 2D Geometry Editor

Pozrite si dostupné možnosti na vytvorenie a úpravu geometrie, ako je znázornené na nasledujúcom obr. 12.2.2.

  
![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image002.jpg)

Okno na úpravu geometrie

## Nástroje na úpravu 2D geometrie

Nižšie sú vysvetlené rôzne možnosti úprav 2D geometrie,

**Výber**![](../../../assets/Icons/Pre_icons/MO_Click_Select.jpg) :**** Nástroj Výber sa používa na výber vrcholu alebo hrany geometrie. Pomocou tohto vertexu alebo hrany je možné polohovať ich ťahaním a púšťaním.

**Výber oblasti** ![](../../../assets/Icons/Pre_icons/MO_Area select.jpg) : Nástroj Výber oblasti sa používa na výber geometrie viac ako jednej entity v rámci poľa.

**Vytvorenie slučky** ![](../../../assets/Icons/Pre_icons/MO_Create_loop.jpg) : Nástroj Create Loop (Vytvoriť slučku) sa používa na vytvorenie geometrickej slučky vytvorením bodov a ich spojením. Jednoduchá geometria, ako je znázornená na obr, sa vytvorí pomocou funkcie create loop v 7 krokoch, ako je znázornené na obr. 12.2. 3.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image003.jpg)

Jednoduchá uzavretá slučka s tabuľkou geometrických súradníc

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image004.jpg)

Kroky na vytvorenie jednoduchej geometrie pomocou nástroja Create Loop

Ak používateľ nie je schopný zistiť súradnice vrcholov pomocou mriežkových čiar alebo mriežkových bodov (pozri obr. 12.2.4.), potom súradnice geometrických bodov môže priamo zadať alebo zmeniť z geometrickej tabuľky v pravej dolnej časti v záložke geometria (pozri obr. 12.2.4.). Línie mriežky možno upraviť na požadovaný rozmer zadaním vzdialenosti medzi chamtivými líniami/bodmi do poľa vedľa výberu línií mriežky.

**Pridanie bodu do slučky** ![](../../../assets/Icons/Pre_icons/MO_Add_points_to_loop.jpg) : Nástroj na pridanie bodu do slučky sa používa na pridanie nových bodov do existujúcej slučky. Po pridaní skontrolujte a zaistite súradnice pridaných bodov na karte geometrie. Ak sú súradnice bodov nepresné, používateľ ich musí opraviť dvojitým kliknutím na príslušnú bunku na karte geometrie. Typický príklad pridávania bodov pred zavedením kružnice je uvedený na obr. 12.2.5.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image005.jpg)

Pridanie bodov do existujúcej slučky

**Odstránenie bodu** ![](../../../assets/Icons/Pre_icons/MO_Delete point.jpg) : Nástroj na odstránenie bodu sa používa na odstránenie bodu v slučke. Pre jednoduchý príklad, ako je znázornené na obr. 12.2.6.

  
![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image006.jpg)

Odstránenie bodu zo slučky

**Krúhly roh**![](../../../assets/Icons/Pre_icons/MO_Round_corner.jpg) : Nástroj Okrúhly roh sa používa na vytvorenie filetovania vo vybranom bode. Keď používateľ vyberie roh, systém zobrazí pole na zadanie polomeru, ako je znázornené na obr. 12.2.7.

  
![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image007.jpg)

Vytvorenie okrúhleho rohu pre geometriu

**Nastavenie uhla** ![](../../../assets/Icons/Pre_icons/MO_Set_angle.jpg) : Nástroj Nastavenie uhla sa používa na zmenu uhla hrany. Keď používateľ vyberie hranu (Krok-1), systém zobrazí aktuálny uhol hrany, kliknutím na zobrazenie uhla pre hranu sa v okne zobrazenia zobrazí pole Uhol modrou farbou (Krok-2), potom zmeňte aktuálny uhol (Krok-3) a stlačením tlačidla ENTER použite, ako je znázornené na obr. 12.2.8.

  
![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image008.jpg)

Príklad nastavenia uhla pre hranu

**Presun**![](../../../assets/Icons/Pre_icons/MO_Move.jpg) : Nástroj Presun sa používa na zmenu polohy bodu jeho pretiahnutím na iné miesto. Ak chcete presunúť akúkoľvek hranu alebo oblasť, používateľ musí najprv vybrať hranu/oblasť (krok 1), potom výberom nástroja Move (Presun) kliknutím na vybranú hranu/oblasť sa v okne zobrazenia zobrazí pole súradníc X,Y modrou farbou (krok 2). Je potrebné zadať požadovanú vzdialenosť presunu v smere X a Y (Krok-3) a stlačiť tlačidlo klávesnice ENTER, aby sa použil postup zobrazený na obr. 12.2.9.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image009.jpg)

Príklad na presun okraja alebo oblasti

**Presun na stredovú čiaru** ![](../../../assets/Icons/Pre_icons/MO_Move_to_centerline.jpg) : Pomocou tohto nástroja môže používateľ presunúť najbližšie a rovnako vzdialené body slučky na stredovú čiaru, ako je znázornené na obr. 12.2.10. Používateľ jednoducho musí vybrať nástroj Presun na os, ako je znázornené na obr. 12.2.10.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image010.jpg)

Príklad na presunutie slučky na os

**Offset** ![](../../../assets/Icons/Pre_icons/MO_Offset.jpg) : Nástroj Offset sa používa na zmenu veľkosti geometrickej slučky. Používateľ môže zmenšiť alebo zväčšiť veľkosť zadaním kladnej, resp. zápornej vzdialenosti posunu, ako je znázornené na obr. 12.2.11.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image011.jpg)

Príklad na vyrovnanie slučky

**Urobiť prvý bod** ![](../../../assets/Icons/Pre_icons/MO_Make_first_point.jpg) : Nástroj Urobiť prvý bod sa používa na vytvorenie vybraného bodu ako prvého bodu v slučke, použije sa pre uzavretú slučku, ako prvý bod nemôžeme vybrať stredový bod oblúka, ako je znázornené na obr. 12.2.12.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image012.jpg)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image013.jpg)

Príklad na vyjadrenie prvého bodu

**Opatočný smer** ![](../../../assets/Icons/Pre_icons/MO_Reverse_direction.jpg) : Opatočný smer sa používa na zmenu smeru slučky, aby sa zmenila orientácia geometrie. Geometria by mala byť vytvorená v protismere hodinových ručičiek, ak je geometria vytvorená v smere hodinových ručičiek, pomocou tejto možnosti môžeme zmeniť smer slučky (pozri obr. 12.2.13.).

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image015.jpg)

Príklad na zobrazenie opačného smeru

**Zatvorenie slučky**![](../../../assets/Icons/Pre_icons/MO_Close_loop.jpg) : Nástroj na uzavretie slučky sa používa na uzavretie otvorenej slučky, ako je znázornené na obr. 12.2.14.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image014.jpg)

Príklad na zobrazenie uzavretej slučky

**Rozdeliť slučku**![](../../../assets/Icons/Pre_icons/MO_Split_loop.jpg) : Nástroj Rozdeliť slučku sa používa na rozdelenie slučky vo vybranom bode (pozri obr. 12.2.15.).

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image016.jpg)

Príklad na znázornenie skĺznej slučky

**Sub loop**![](../../../assets/Icons/Pre_icons/MO_Sub_loop.jpg) : Nástroj Sub loop sa používa na výber vnútornej slučky ako sub loop v prípade topológie viacerých slučiek, výberom tohto nástroja môžeme priradiť materiál pre geometriu viacerých slučiek (pozri obr. 12.2.16.).

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image017.jpg)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image018.jpg)

Príklad na zobrazenie čiastkovej slučky

**Spojenie slučiek** ![](../../../assets/Icons/Pre_icons/MO_Join_loop.jpg) : možnosť spojiť slučky sa používa na spojenie 2 slučiek výberom slučiek, ktoré sa majú spojiť, koncový bod prvej slučky sa spojí s prvým bodom druhej slučky (pozri obr. 12.2.17.).

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image019.jpg)

Príklad na zobrazenie slučkových slučiek

**Spojenie všetkých slučiek** ![](../../../assets/Icons/Pre_icons/MO_Join_all_loops.jpg) : Nástroj na spojenie všetkých slučiek sa používa na spojenie všetkých slučiek. Príklad pre Join all loops je uvedený na obr. 12.2.18.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image020.jpg)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image021.jpg)

Príklad na zobrazenie spojenia všetkých slučiek

**Odstrániť vybrané** ![](../../../assets/Icons/Pre_icons/MO_Delete_selected.jpg) : Odstrániť vybrané slúži na odstránenie vybraných slučiek alebo hrán.

**Odstrániť nevyznačené** ![](../../../assets/Icons/Pre_icons/MO_Delete_Unselected.jpg) : Odstrániť nevyznačené sa používa na odstránenie nevyznačených hrán slučiek.

## Možnosti zobrazenia alebo zobrazenia úprav

**Zobraziť vrchol** ![](../../../assets/Icons/Pre_icons/MO_Show_vertex.jpg) : slúži na zobrazenie vrcholov geometrie.

**Zobraziť čísla vrcholov** ![](../../../assets/Icons/Pre_icons/Mo_Show_Vertex_numbers_icon.jpg) : slúži na zobrazenie čísla vrcholov geometrie.

**Zobraziť vnútro**![](../../../assets/Icons/Pre_icons/MO_Show_inside.jpg) : slúži na zobrazenie orientácie geometrie.

**Zobraziť smer hrany** ![](../../../assets/Icons/Pre_icons/MO_Show_Edge_direction.jpg) : slúži na vykreslenie smeru vytvorenej slučky.

**Zobraziť materiál** ![](../../../assets/Icons/Pre_icons/MO_Material_icon.jpg) : slúži na načítanie a priradenie materiálu k oblasti geometrie.

**Sieťové línie** : Zobrazuje mriežkové čiary v horizontálnom a vertikálnom smere v okne zobrazenia. (Pozri obr. 12.2.19.)

**Sieťové body** : Zobrazuje body mriežky v horizontálnom a vertikálnom smere v okne zobrazenia (pozri obr. 12.2.19).

**Mriežka žiadna** : Keď je táto možnosť vybratá, body mriežky a línie mriežky v horizontálnom a vertikálnom smere sa v okne Zobrazenie nezobrazujú. (Pozri obr. 12.2.19.)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image022.jpg)

Okno definície mriežky

**Zobraziť os**![](../../../assets/Icons/Pre_icons/MO_Show_Axis.jpg) : Zobrazí os v okne displeja

**Zobraziť stredovú čiaru**![](../../../assets/Icons/Pre_icons/MO_Show_centreline.jpg) :Zobrazí stredovú čiaru v okne displeja

**Vmestiť všetko** ![](../../../assets/Icons/Pre_icons/MO_Fit_All_icon.jpg) : Vmestí všetky zobrazené entity do aktuálneho zobrazovacieho priestoru.

**Zväčšenie okna** ![](../../../assets/Icons/Pre_icons/Mo_Box_Zoom_Icon.jpg) : Funkcia zväčšenia okna umožňuje detailnú kontrolu malej oblasti aktuálne definovaných entít. Oblasť priblíženia sa vyberie podržaním klávesov Ctrl + Alt a kliknutím ľavého tlačidla myši, pričom potiahnutím myši sa vybraná oblasť uzavrie zobrazeným rámčekom. Po uvoľnení tlačidla myši vybraná oblasť vyplní zobrazovacie okno.

**Zoom** ![](../../../assets/Icons/Pre_icons/MO_Zoom_icon.jpg) : Priblíženie dynamicky mení veľkosť oblasti objektu, ktorá vypĺňa aktívny port zobrazenia. Veľkosť zobrazenia možno zmeniť podržaním klávesu Alt a kliknutím ľavého tlačidla myši v aktívnom porte zobrazenia a posunutím myši dozadu alebo dopredu, čím sa zväčší alebo zmenší veľkosť objektu v okne zobrazenia.

**Paning**![](../../../assets/Icons/Pre_icons/MO_Pan_icon.jpg) : Pan upravuje oblasť vypĺňajúcu aktívne zobrazovacie pole bez zmeny veľkosti zobrazeného objektu.

**Uložiť**![](../../../assets/Icons/Pre_icons/MO_Save_icon.jpg) :Uloží problémové nastavenie vo formáte súboru .key. Túto funkciu možno tiež otvoriť z ponuky File Tools (Nástroje súboru).

## Možnosti vlastností editora 2D geometrie

**Záložka Geometria :** V záložke Geometria môžeme zadávať alebo upravovať geometrické entity. Geometrické entity možno zadávať dvoma spôsobmi, metódou Line-Arc a metódou XYR.

**Metóda XYR** : Formát **XYR** ([DIEGEO](/docs/sk/Keyword_Documentation/D/DIEGEO/)) pozostáva z definovania súradnice X, súradnice Y a polomeru pre každý bod geometrie definujúci objekt. Nakreslí sa oblúk so zadaným polomerom spájajúci čiary, ktoré by sa pretínali v bode definovanom súradnicou X a Y. (Pozri obr. 12.2.20.)

  
Tabuľka XYR sa zobrazí priamo v okne Geometria. Táto tabuľka umožňuje špecifikovať a/alebo upravovať geometriu objektu prostredníctvom množstva bodov vo formáte XYR. X a Y sú súradnice x a y bodu a R je polomer bodu (ak má definovať zakrivenú čiaru).

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image023.jpg)

2D editor geometrie s typom XYR Geo

**Metóda líniového oblúka :** Formát líniového oblúka ([DIEGEO](/docs/sk/Keyword_Documentation/D/DIEGEO/)) je podobný formátu XYR v tom, že môže definovať oblúky, ale je viac orientovaný na entity. Formát XYR definuje spojovacie body a typ spojenia, ale formát Line-Arc definuje čiary a oblúky, ktoré tvoria objekt, nie spojenia. Hlavným dôvodom, prečo sa používa formát Line-Arc, je skutočnosť, že súbory IGES sú formátované v schéme Line-Arc. (Pozri obr. 12.2.21.)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image024.jpg)

2D editor geometrie s typom Geo Line-Arc

**Pridanie slučky** ![](../../../assets/Icons/Pre_icons/MO_Add_Loop_button.jpg) : Kliknutím na toto tlačidlo sa pridá nová slučka, táto možnosť je potrebná na definovanie topológie pre viachraničné objekty (pozri obr. 12.2.22).

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image025.jpg)

Príklad na zobrazenie Add loop

**Delete Loop** ![](../../../assets/Icons/Pre_icons/MO_Delete_Loop_button.jpg) : Kliknutím na toto tlačidlo sa odstráni existujúca slučka (pozri obr. 12.2.23.).

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image026.jpg)

Príklad na znázornenie slučky Delete Loop

**Pridanie vrcholu**![](../../../assets/Icons/Pre_icons/MO_Add_Vertex_button.jpg) : Kliknutím na toto tlačidlo sa pridá nový vrchol do slučky (pozri obr. 12.2.24).

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image027.jpg)

Príklad na ukážku Pridanie vrcholu do slučky

**Delete Vertex** ![](../../../assets/Icons/Pre_icons/MO_Delete_Vertex_button.jpg): Kliknutím na toto tlačidlo sa odstráni existujúci vrchol v slučke. (Pozri obr. 12.2.25.)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image028.jpg)

Príklad na zobrazenie vymazania vrcholu v slučke

**Priradiť k![](../../../assets/Icons/Pre_icons/MO_Assign_to_pull_down_button.jpg) :**

Ak je k dispozícii viacero hraničných geometrií (viacero slučiek), používateľ môže priradiť každú geometriu slučky k iným objektom, ako je znázornené na obr. 12.2.26.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image029.jpg)

Príklad na zobrazenie možnosti Priradiť k

Karta **Objekty** : V záložke Objekty môžeme vybrať objekt v zozname, aby sa geometria vybraného objektu skryla v okne grafického zobrazenia, ak je zobrazených viac ako jeden objekt. (Pozri obr. 12.2.27.)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image030.jpg)

Okno objektov 2D editora geometrie

Karta **Opáčky** : Na karte Loops môžeme načítať a priradiť materiál pre vybrané slučky. Taktiež môžeme vidieť zobrazenie priradeného materiálu k príslušnej slučke (pozri obr. 12.2.28).

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image031.jpg)

Okno materiálov 2D editora geometrie

## Importovanie viacerých hraničných geometrií

V MO môže používateľ importovať viacero hraničných geometrií, ako je znázornené na obr. 12.2.29.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image032.jpg)

Príklad na zobrazenie viacerých hraničných geometrií

## Definovanie a úprava viacerých hraničných geometrií

Používateľ môže vytvoriť viacero hraničných geometrií. Na obr. 12.2.30. je znázornené definovanie viacerých hraničných geometrií a úprava definovanej geometrie.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image033.jpg)![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_2_2D_Geometry_Editing/12_2_Image034.jpg)

Príklad na ukážku úpravy a definovania viacerých hraničných geometrií

[12\. Geometry Modelling](/docs/sk/pre_processor/12_geometry_modelling/12_geometry_modelling/)

[12.1. 2D Geometry Data Defining](/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/)

[12.3. 3D Geometry Data Defining](/docs/sk/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/)

[12.4. 3D Geometry Editing (GEO TOOL)](/docs/sk/pre_processor/12_geometry_modelling/12_4_3d_geometry_data_Editing_geo_toolL/)
