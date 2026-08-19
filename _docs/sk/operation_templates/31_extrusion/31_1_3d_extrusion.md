---
lang: sk
title: "31.1. 3D extrudovanie"
---

# 31.1. 3D extrudovanie

31.1.1. Ako pridať operáciu 3D extruzného tvarovania

31.1.2. Nastavenie simulácie

31.1.3. Stránka so zoznamom materiálov

31.1.4. Definovanie extruznej matrice

31.1.5. Stránka objektu „Die“

  * Geometria

  * Symetria

  * Stránka so sieťami na lisovacie formy

  * Výber materiálu

  * Stránka BCC

  * Pohyb

  * Oporná plocha

  * Kontrolné body ložiska

31.1.6. Definícia výliskového polotovaru

  * Stránka „Geometria obrobku“

  * Typ generovania siete obrobku

  * Stránka BCC pre obrobok

  * Nehnuteľnosť

  * Inicializovať

  * B.I. Flownet

31.1.7. Ovládacie prvky

31.1.8. Kontakt

31.1.9. Ovládacie prvky krokov

31.1.10. Vytvorenie databázy

## Ako pridať operáciu 3D extruzného vytvorenia

Operáciu extrudovania je možné nastaviť v prostredí integrovaného výrobného procesu, ku ktorému sa dostanete z hlavnej obrazovky grafického používateľského rozhrania. Používateľ môže vytvoriť nový problém buď výberom položky Súbor ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Nový problém, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}), výberom prepínača 3D extrudovanie v časti Typ problému a Systém jednotiek a následným kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), ako je znázornené na obr. 31.1.1. Otvorí sa sprievodca integrovaným výrobným procesom a v editore operácií uvidíme, že bola pridaná operácia 3D extrúzia.

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image001.jpg' | relative_url }})

Pridanie operácie extrudovania pomocou hlavného okna grafického rozhrania

  
Operáciu extrudovania môžeme do prostredia Integrovaného výrobného procesu pridať aj z kontextového menu „Nový projekt“, keď sa v tomto prostredí otvorí nová úloha, ako je znázornené na obr. 31.1.2. Pomocou možnosti „Kopírovať existujúci projekt“ môžeme z kontextového menu „Nový projekt“ importovať predtým uložené projekty ako nové projekty.

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image002.jpg' | relative_url }})

V okne „Nový projekt“ zadajte názov projektu a vyberte prvú operáciu

  
Operáciu „Extrúzia“ môžeme do editora operácií pridať aj z karty „Explorer“ v prostredí „Integrated Manufacturing Process“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie „Extrúzia“, ako je znázornené na obr. 31.1.3., alebo presunutím operácie „Extrúzia“ do okna editora operácií metódou drag-and-drop.   
Po pridaní operácie „Extrúzia“ do editora operácií sa v okne na úpravu nastavení vlastností otvorí stránka výberu nastavení simulácie.

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image003.jpg' | relative_url }})

Pridanie operácie zo zoznamu operácií v Průzkumníku

## Nastavenie simulácie

### Simulačná metóda

Šablóna „Extrúzia“ obsahuje tri rôzne typy extrúzie. Ide o extrúziu ALE, extrúziu v ustálenom stave a Lagrangeovú extrúziu (inkrementálnu).   
**Extrúzia ALE:** Pri type extrúzie ALE (Augmented Lagrangian Eulerian) je počiatočný obrobok modelovaný približne tak, aby sa viac približoval konečnému tvaru. Simulácie ALE je možné zastaviť po dosiahnutí ustáleného stavu na základe kritérií zastavenia ALE; počet krokov potrebných na dosiahnutie ustáleného stavu závisí od toho, do akej miery dokážeme modelovať počiatočné podmienky obrobku tak, aby sa priblížili podmienkam ustáleného stavu. Simulácie ALE zvyčajne trvajú kratšie a pomáhajú rýchlo vizualizovať výsledok procesu extrudovania. Pri extrudovaní metódou ALE sa materiál môže posúvať kolmo na smer extrudovania.  
**Extrúzia v ustálenom stave:** Pri type simulácie „Extrúzia v ustálenom stave“ modelujeme systém na základe podmienok ustáleného stavu a simulujeme ho počas niekoľkých krokov, aby sa riešenie stabilizovalo. Simulácia trvá veľmi krátko, keďže hľadáme stabilizované konvergentné riešenie, a dá sa použiť na predpovedanie výstupných stavových premenných. Pri extrudovaní v ustálenom stave sa materiál môže posúvať kolmo na smer extrudovania.  
**Lagrangeovská extrúzia:** Pri Lagrangeovskom type extrúzie sa počiatočný tvar obrobku modeluje rovnako ako skutočný obrobok a počas simulácie sa obrobok postupne posúva (deformuje) vo všetkých smeroch na základe výsledkov inkrementálnych rovníc, pričom sa aktualizujú hodnoty stavových premenných. Dokončenie simulácie trvá dlhšie, pretože simulácia musí pokračovať, kým obrobok neprejde cez matricu, aby bolo možné vizualizovať výsledok procesu extrudovania; okrem toho sa výtlak počíta vo všetkých smeroch a aktualizuje.

### Tepelný výpočet

Na karte „Tepelné výpočty“ (pozri obr. 31.1.4.) sú k dispozícii možnosti na výber typov objektov, na ktorých sa majú vykonať tepelné výpočty. 

  * **Konštantná teplota (izotermická)**: Ak používateľ zvolí túto možnosť, simulácia nevykonáva žiadne tepelné výpočty. Túto možnosť môže používateľ využiť v prípade, že zmena teploty v procese je zanedbateľná.

  * **Iba obrobok (neizotermické)**: Ak používateľ zvolí túto možnosť, simulácia vykoná tepelný výpočet iba pre obrobok; táto možnosť je užitočná vo väčšine prípadov, keď používateľa zaujíma iba zmena teploty obrobku.

  * **Obrobok a formy (neizotermické)**: Túto možnosť je možné použiť v prípade, že je potrebné vykonať tepelné výpočty tak pre obrobok, ako aj pre formy, s cieľom sledovať zmeny teploty týchto objektov.

### Typ lisovacej formy

V položke „Typ modelu“ máme na výber možnosti „Úplný model“ alebo „So symetrickými podmienkami“ v závislosti od symetrie geometrie, ktorú chceme v nastavení modelovať.

###   
Zrýchlenie 

Možnosti zrýchlenia sú k dispozícii iba pre extrudovanie v ustálenom stave a metódou ALE. Zrýchlenie možno použiť na urýchlenie aktualizácie stavových premenných, čo zvýši rýchlosť a skráti čas simulácie v prípade metód extrudovania ALE a v ustálenom stave. Pri Lagrangeovej metóde extruzie nie je možnosť zrýchlenia aktívna, ako je znázornené na obr. 31.1.4. Obr. 31.1.5. znázorňuje vplyv zrýchlenia stavových premenných na čas simulácie.

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image004.jpg' | relative_url }})

Stránka s nastaveniami simulácie

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image005.jpg' | relative_url }})

Účinok zrýchlenia

## Stránka so zoznamom materiálov

Na stránke materiálov môže používateľ pridať materiály do zoznamu pomocou možnosti „Načítať z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (ako je znázornené na obr. 31.1.6.). Ak požadovaný materiál nie je v zozname k dispozícii, môže ho používateľ načítať na stránke materiálov objektu pomocou funkcie „Importovať údaje o materiáli zo súboru“ ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}). Ak materiál nie je k dispozícii v knižnici DEFORM, môže ho používateľ vytvoriť pomocou ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Používateľ môže materiál zo zoznamu odstrániť pomocou ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) alebo údaje o materiáli upraviť pomocou ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}). Upravený alebo novo definovaný materiál je možné uložiť pomocou ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}). 

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image006.jpg' | relative_url }})

Zoznam materiálov – Strana

## Definovanie extruznej matrice 

Používateľ môže pridať matrice kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}) vedľa poľa „Počet matríc“ a ak chce matrice odstrániť, musí kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_icon.jpg' | relative_url }}), ako je znázornené na obr. 31.1.7.

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image007.jpg' | relative_url }})

Stránka s matrikami

## Stránka objektu „Die“

Používateľ môže definovať názov, dočasnú premennú objektu a typ objektu (pozri obr. 31.1.8.). Typ objektu „Rigid“ je predvolene vybraný. Používateľ môže importovať objekty z iných databáz alebo súborov kľúčov pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) alebo uložiť údaje o objektoch pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}). Používateľ môže vidieť zaškrtávacie políčko „**Priradiť opornú plochu**“, ak je vybraný typ simulácie ALE alebo Steady-state; toto políčko môže zaškrtnúť pre formu, ktorá má otvor, aby definoval a upravil opornú plochu. 

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image008.jpg' | relative_url }})

Stránka objektu „Die“

###   
3D geometria

Geometriu môžeme vytvoriť pomocou funkcie „Definovať primitív“ alebo ju môžeme importovať zo súboru pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). Užívateľ môže údaje o geometrii uložiť pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}). Ďalšie informácie o ostatných možnostiach geometrie nájdete v časti 3D geometria. (Pozri obr. 31.1.9.)

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image009.jpg' | relative_url }})

Stránka o geometrii

### Symetria

Stránka symetrie je dostupná len vtedy, ak na stránke nastavení simulácie vyberieme model formy so symetrickou podmienkou. Na tejto stránke môžeme pomocou možností výberu určiť symetrickú plochu na formách a obrobku. Po výbere symetrickej plochy kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), ako je znázornené na obr. 31.1.10. Ak chce používateľ odstrániť údaje o niektorej z definovaných symetrických plôch, vyberie príslušné údaje o ploche a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_symmetry_icon.jpg' | relative_url }}). Ak chce používateľ odstrániť všetky údaje o symetrii, klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image010.jpg' | relative_url }})

Stránka o symetrii

### Stránka so sieťami na lisovacie formy

Sieť pre lisovacie formy môžeme vytvoriť tak, že v riadenom režime zadáme počet prvkov, ako je znázornené na obr. 31.1.11. K pokročilým nastaveniam na riadenie vytvárania 3D siete sa dostanete pomocou prepínača „expertný režim“ na paneli nástrojov.   
Ďalšie informácie o pokročilých možnostiach siete v režime pre pokročilých nájdete v časti Nastavenia 3D siete. 

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image011.jpg' | relative_url }})

Stránka so sieťou matíc

###   
Výber materiálu

Na stránke materiálov sa zobrazujú všetky materiály pridané do zoznamu materiálov (ako je znázornené na obr. 31.1.12.). Používateľ môže vybrať požadovaný materiál a priradiť ho k príslušnému objektu. Ak požadovaný materiál nie je v zozname k dispozícii, môže ho používateľ načítať na stránke materiálov objektu pomocou funkcie Importovať údaje o materiáli zo súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) alebo pomocou možnosti Načítať z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). Ak materiál nie je k dispozícii v knižnici DEFORM, môže ho používateľ vytvoriť pomocou ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Používateľ môže materiál zo zoznamu odstrániť pomocou ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) alebo údaje o materiáli upraviť pomocou ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}). Upravený alebo novo definovaný materiál je možné uložiť pomocou ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image012.jpg' | relative_url }})

Priradenie materiálu

###   
Stránka BCC

Na stránke „Okrajové podmienky“ môže používateľ objektu priradiť rôzne okrajové obmedzenia. Okrajové podmienky určujú, ako okraj objektu interaguje s ostatnými objektmi a s prostredím. Bežne používanými okrajovými podmienkami sú výmena tepla s prostredím pre simulácie zahŕňajúce prenos tepla a symetria BCC pre symetrický model. BCC „Výmena tepla s prostredím“ sa pridáva štandardne po vytvorení siete, ako je znázornené na obr. 31.1.13.

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image013.jpg' | relative_url }})

Stránka BCC

###   
Pohyb

Ak ide o zdvihovú maticu, používateľ môže definovať jej pohyb na základe rýchlosti alebo sily ako konštanty, ako funkcie času alebo ako funkcie zdvihu, ako je znázornené na obr. 31.1.14.

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image014.jpg' | relative_url }})

Stránka hnutia Die

###   
Stránka o oporných plochách (pre ALE a extrudovanie v ustálenom stave)

Na stránke **Oporná plocha** budeme definovať oporné plochy a pridávať ich do zoznamu oporných plôch. Na definovanie opornej plochy môže používateľ **vybrať** všetky výplne súvisiace s opornou plochou a kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}). Pri definovaní prvej opornej plochy sa do zoznamu pridá zvýraznená oporná plocha s **ID <1>**. Potom môže používateľ pokračovať a definovať ďalšie oporné plochy podobným spôsobom, ako je znázornené na obr. 31.1.15. Každá oporná plocha dostane pridelené jedinečné ID a v zobrazení geometrie lisovacej formy bude zvýraznená inou farbou.  
Zaškrtávacie políčko **Zobraziť vnútro** slúži na zobrazenie vnútornej geometrie s cieľom vybrať opornú plochu.

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image015.jpg' | relative_url }})

Bol pridaný zoznam ložiskových plôch

### Kontrolné body ložiska (pre ALE a extrudovanie v ustálenom stave)

Pri extrudovaní sú ohyby, skrútenia a zvlnenia profilov spôsobené hlavne nerovnomerným tokom materiálu. Ohyby okrajových profilov je teda možné znížiť nastavením dĺžky opory, a to definovaním kontrolných bodov opory (pozri obr. 31.1.16.). Po definovaní opornej plochy môže používateľ definovať kontrolné body opory pozdĺž vstupnej hrany opornej plochy. Používateľ môže kontrolné body opory uložiť do súboru pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) a môže tiež importovať uložené kontrolné body opory zo súboru pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_open_icon.jpg' | relative_url }}). Ako je znázornené na obr. 31.1.17, po definovaní kontrolných bodov sa zmení tvar a dĺžka opory pre plochy.

  
Používateľ môže vymazať vybraný kontrolný bod ložiska pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_delete_current_row_icon.jpg' | relative_url }}).   
Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}) môže používateľ odstrániť všetky kontrolné body opornej plochy.  
**Zobraziť pôvodnú geometriu ![]({{ '/assets/icons/pre_icons/mo_show_org_geo_button.jpg' | relative_url }})**: Pomocou tejto možnosti si môžeme prezrieť pôvodnú geometriu matrice bez uplatnenia upravených hodnôt dĺžky ložiska.  
**Zobraziť upravenú geometriu** ![]({{ '/assets/icons/pre_icons/mo_show_mod_geo_button.jpg' | relative_url }}): Pomocou tejto možnosti môžeme zobraziť upravenú geometriu matrice po uplatnení upravených hodnôt dĺžky ložiska, pozri obr. 31.1.18.  
**Zobraziť oporné plochy** ![]({{ '/assets/icons/pre_icons/mo_show_bearing_surf_button.jpg' | relative_url }}): Pomocou tejto možnosti môžeme zobraziť iba definované oporné plochy.

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image016.jpg' | relative_url }})

Stránka s kontrolnými bodmi ložísk

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image017.jpg' | relative_url }})

Nastavenie kontrolných bodov nosnej plochy

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image018.jpg' | relative_url }})

Upravená geometria matrice po nastavení dĺžky ložiska

Ďalšie informácie nájdete v dokumente [steady state extrusion lab.](/docs/en/labs/extrusion_labs/steady_state_extrusion_lab1/)

## Definícia extruzného polotovaru

Používateľ môže zvoliť názov a dočasný objekt. Typ objektu bude štandardne plast, ako je znázornené na obr. 31.1.19.

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image019.jpg' | relative_url }})

Stránka objektu obrobku

### Stránka „Geometria obrobku“

Geometria obrobku sa vytvára pomocou funkcie „Definovať primitív“ alebo ju môžeme importovať pomocou možností importu. V prípade nastavenia simulácie typu ALE je možné geometriu obrobku vytvoriť pomocou booleovského štítku po vytvorení geometrie foriem. Ďalšie informácie o ostatných možnostiach na stránke „Geometria“ nájdete v [12.3. 3D Geometry Data Defining.](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/).

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image020.jpg' | relative_url }})

Stránka „Geometria obrobku“

###   
Typ generovania siete obrobku

V šablóne „Extrúzia“ môže používateľ vytvoriť pravidelnú tetraedrickú sieť pre obrobok pomocou metódy „Pravidelné vytváranie siete“ alebo špeciálnu sieť pomocou nástroja „Nástroj na extrudovanie siete“ – pozri obr. 31.1.21.

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image021.jpg' | relative_url }})

Typy generovania sietí

  * **Nástroj na extrudovanie siete obrobku**

Nástroj „Mesh Extruding“ je špeciálny typ vytvárania siete, ktorý sa používa v operácii „Extrusion“ na rýchlejšie vytvorenie siete. Pri tejto metóde vytvárania siete sa obrobok rozdelí do 3 oblastí, 

  * **Oblasť kontajnera** – Táto oblasť zahŕňa materiál vnútri kontajnera, ktorý nevykazuje výrazné deformácie.

  * **Deformačná oblasť** \- Ide o oblasť bližšie k otvoru formy, kde dochádza k výraznej deformácii materiálu. Táto oblasť zahŕňa otvor formy a čiastočne aj vstup a výstup materiálu cez tento otvor.

  * **Oblasť extrudátu** – Táto oblasť zahŕňa materiál, ktorý už prešiel otvorom matrice a nedochádza v nej k výraznej deformácii.

  
Systém automaticky identifikuje zóny na základe geometrie lisovacej formy. Používateľ však môže zóny upraviť ťahaním príslušných hraníc zón na reprezentatívnom obrázku v okne nástroja na vytláčanie siete (pozri obr. 31.1.22) alebo pomocou kontrolných bodov v zobrazovacej oblasti. Prechod siete môže používateľ ovládať pomocou nastavení v okne „Nástroj na vytláčanie siete“.

  
Pri tejto metóde sa v deformovanej oblasti vytvorí tetraedrická sieť, ktorá sa následne vytiahne do kontajnerovej oblasti a oblasti extrudátu, pozri obr. 31.1.23. Používateľ môže v každej oblasti vytvoriť viacero zón a pre každú zónu definovať pomer veľkostí/počet vrstiev, čím ovplyvní prechod siete. V oblasti deformácie je možné sieť vygenerovať pomocou,

  * **Relatívna**: Pri tejto metóde môže používateľ určiť počet prvkov potrebných na vytvorenie relatívnej siete a definovať pomer veľkostí v jednotlivých zónach, čím ovplyvní prechod medzi sieťami.

  * **Absolútna**: Pri tejto metóde môže používateľ určiť minimálnu hodnotu veľkosti prvku a nastaviť veľkosť prvkov v jednotlivých zónach, čím ovplyvní prechod siete.

**Náhľad**: Keď používateľ klikne na akciu „**Náhľad**“, vygeneruje sa tetrahedrálna sieť pre deformovanú oblasť a zobrazí sa.

**Vytvoriť**: Používateľ môže kliknúť na akčnú položku „**Vytvoriť**“, aby vytvoril sieť.

**Predvolené nastavenie** ![]({{ '/assets/icons/pre_icons/mo_default_settings_button.jpg' | relative_url }}): Keď používateľ klikne na toto tlačidlo, zóny a ich hodnoty sa vrátia na predvolené hodnoty.

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image022.jpg' | relative_url }})

Stránka s nástrojom na extrudovanie sietí

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image023.jpg' | relative_url }})

Sieť vytvorená pomocou nastavení nástroja na extrudovanie siete

  * **Pravidelné zapojenie obrobku**

V nastavení pravidelnej siete môže používateľ ovládať sieť definovaním pokročilých nastavení, ako sú váhové faktory, okná siete, pomer veľkostí a kritériá pregenerovania siete. Používateľ môže kliknúť na „![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }})“ na vygenerovanie siete; sieť vygenerovaná pomocou pravidelného vytvárania sietí vyzerá tak, ako je znázornené na obr. 31.1.24.  
Ďalšie informácie o nastaveniach siete pri bežnom vytváraní sietí nájdete v časti „Nastavenia siete v expertnom režime“ v [13.2.2. Expert mode 3D mesh generation](../../pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation.htm#13.2.2._Expert_Mode_3D_Mesh_Generation)

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image024.jpg' | relative_url }})

Stránka s pravidelným sieťovaním

###   
Stránka BCC pre obrobok

Na stránke „Okrajové podmienky“ môže používateľ objektu priradiť rôzne okrajové obmedzenia. Okrajové podmienky určujú, ako okraj objektu interaguje s ostatnými objektmi a s prostredím. Systém po vytvorení siete automaticky priradí obrobku so symetrickým modelom symetrickú rovinu BCC (pozri obr. 31.1.25.).

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image025.jpg' | relative_url }})

Symetria BCC obrobku

**Metódy simulácie BCC pre ALE a extrúziu v ustálenom stave**

V prípade simulačných metód ALE a ustáleného stavu musí používateľ definovať voľnú hladinu. Voľná hladina je hladina na výstupnom konci extrudátu. V dialógovom okne Hraničné podmienky kliknite v stromovej štruktúre na položku Voľná hladina, vyberte spodnú hladinu a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}), aby ste pridali hraničnú podmienku voľnej hladiny (pozri obr. 31.1.26.).

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image026.jpg' | relative_url }})

BCC s voľným povrchom obrobku

### Nehnuteľnosť

V okne „Vlastnosti objektu“ sa zadávajú rôzne parametre objektu, ktoré ovplyvňujú buď termomechanické správanie objektu, alebo správanie numerického riešenia. (Pozri obr. 31.1.27.) Objemová kompenzácia je jedným z dôležitých parametrov, ktoré je potrebné nastaviť pri simulácii extrudovania typu Lagrange. Je možné ju aktivovať výberom jednej z možností v časti „Cieľový objem“ a výpočtom aktuálneho objemu objektu pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}). Ďalšie informácie o možnostiach na stránke „**Vlastnosti**“ nájdete v [16\. Object properties.](/docs/en/pre_processor/16_object_properties/16_object_properties/)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image036.jpg' | relative_url }})

Stránka nehnuteľnosti

### Inicializácia

V okne „Initialize“ sú na inicializáciu k dispozícii niektoré bežne používané stavové premenné, ako napríklad teplota, deformácia, napätie, poškodenie, rýchlosť, posunutie, hustota, veľkosť zŕn mikrostruktúry a veľkosť častíc.  
Používateľ môže inicializovať hodnoty týchto stavových premenných tak, že ich zadá do príslušného poľa a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). Obr. 31.1.28. znázorňuje rôzne stavové premenné, ktoré sú k dispozícii v okne „Initialize“. V závislosti od typu stavovej premennej ich môže používateľ inicializovať aj z dátových okien „Node“ a „Element“. Ďalšie informácie o tom, ako inicializovať stavové premenné v oknách „Node“ a „Element“, nájdete v [Object node variables](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) a [Object element variables](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/).

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image027.jpg' | relative_url }})

Načítanie stránky

### B.I. Flownet

V databáze s veľkým počtom krokov bude vykreslenie siete Flownet trvať veľmi dlho; používateľ môže tento problém vyriešiť využitím vstavanej siete Flownet. Ak používateľ využije vstavanú sieť Flownet, táto sa vykreslí priebežne počas simulácie problému. (Pozri obr. 31.1.29.)  
Ďalšie informácie o definovaní v rámci systému Flownet nájdete v dokumente [13.2.9. Built in Flownet](../../pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation.htm#13_2_9_Built_In_Flownet)

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image016.jpg' | relative_url }})

Vstavaná stránka Flownet

## Ovládacie prvky

Používateľ môže umiestňovať objekty pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}). K dispozícii sú rôzne možnosti umiestňovania objektov, ako je znázornené na obr. 31.1.30. Ďalšie informácie o týchto možnostiach nájdete v časti [19\. Object positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/).

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image028.jpg' | relative_url }})

Ovládacie prvky na nastavenie polohy objektu

## Kontakt

V šablóne extrudovania bola implementovaná špeciálna metóda kontaktu, ktorá v prípade simulačných metód ALE a Steady-state generuje úplný kontakt s polotovarom, čím sa skracuje čas potrebný na dosiahnutie ustáleného stavu. Keď používateľ navštívi stránku kontaktu, zobrazí sa mu vyskakovacie okno „Vytvorenie úplného kontaktu“, ako je znázornené na obr. 31.1.31. Ak sa použije vytvorenie úplného kontaktu, systém automaticky vypočíta toleranciu kontaktu so susednými objektmi a následne vytvorí kontakt.   
V prípade simulačnej metódy lagrangovského typu môže používateľ odhadnúť toleranciu pomocou ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) a následne vygenerovať kontakty.

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image029.jpg' | relative_url }})

Vyskakovacie okno „Full Contact Generation“

  
**Systém**: Ak je zaškrtnuté toto políčko, systém priradí predvolené vzťahy medzi objektmi. Okrem toho môže používateľ v prípade potreby pridať mazivá tak, že z roletového menu vyberie možnosť „Pridať nové“ a klikne na tlačidlo „Upraviť“, alebo môže na účely simulácie načítať požadované mazivá z knižnice.  
**Používateľ**: Pri operácii „Extrúzia“ je štandardne vybrané rádio tlačidlo „Používateľ“. Používateľ môže pridať vzťahy kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}), ako je znázornené na obr. 31.1.32. Používateľ môže zmeniť hodnotu každého vzťahu tak, že ho vyberie a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môže používateľ priradiť rovnaké hodnoty všetkým vzťahom. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) môže používateľ vypočítať toleranciu kontaktu. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) môže používateľ vygenerovať kontaktný vzťah medzi objektmi, pre ktoré sú definované kontaktné vzťahy. Zaškrtnutím políčka vedľa kontaktného vzťahu môže používateľ definovať priliehavý kontakt.  
Ďalšie informácie o dialógovom okne s kontaktnými údajmi nájdete v [20.Inter-Object Relations.](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image030.jpg' | relative_url }})

Stránka s kontaktnými údajmi

## Ovládacie prvky krokov

V ovládacích prvkoch krokov môže používateľ definovať počet krokov, veľkosť kroku a čas/zdvih na krok, čím riadi kroky simulácie, ako je znázornené na obr. 31.1.33. Ovládacie prvky krokov, ktoré je potrebné definovať, sú k dispozícii v režime s návodom, zatiaľ čo pokročilejšie nastavenia je možné definovať v režime Expert.

### REŽIM S VEDENÍM:

Počet krokov:**Tu je možné zadať počet krokov, ktoré sa majú simulovať. Ak sa** simulácia ukončí skôr na základe kritérií ukončenia, nasledujúci krok spúšťajúci operáciu bude pokračovaním predchádzajúcej operácie.

**Počet krokov**: Počet krokov ([STPINC](/docs/en/keyword_documentation/s/stpinc/)), ktoré sa majú uložiť do databázy, určuje, koľko krokov systém v databáze uloží. Pri spustení simulácie sa musí vypočítať každý krok, ale nie je nutné, aby sa všetky kroky uložili do databázy. Uložením väčšieho počtu krokov sa zachová viac informácií o procese, čo však bude vyžadovať väčší úložný priestor.

**Čas na jeden krok:** Ak je zadaný čas na jeden krok, použije sa časový interval na jeden krok. Posun formy na jeden krok bude rovný časovému kroku vynásobenému rýchlosťou formy.  
Posun na krok: Ak je nastavený posun na krok, primárny valec sa v každom časovom kroku posunie o zadanú hodnotu. Celkový posun primárneho valca bude rovný posunu na krok vynásobenému celkovým počtom krokov.

**Primárny lisovací nástroj:** Primárny lisovací nástroj ([PDIE](/docs/en/keyword_documentation/p/pdie/)) je objekt, pre ktorý je definovaných mnoho kritérií zastavenia a krokovania. Napríklad vzdialenosť zastavenia založená na zdvihu primárneho lisovacieho nástroja. Keď zdvih objektu definovaného ako primárny lisovací nástroj dosiahne hodnotu posunu primárneho lisovacieho nástroja, simulácia sa zastaví, aj keď bolo špecifikovaných viac krokov. Funkcia „Krok podľa zdvihu“ určuje veľkosť kroku na základe pohybu primárneho lisovacieho nástroja.

Primárna forma sa zvyčajne priraďuje k objektu, ktorý je strojom najviac riadený. Napríklad forma pripevnená k piestu hydraulického lisu by bola označená ako primárny objekt.

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image031.jpg' | relative_url }})

Ovládacie prvky krokov v režime GUIDED

###   
REŽIM PRE ODBORNÍKOV

Používateľ môže definovať údaje pre riadenie krokov pomocou ovládacích prvkov simulácie v expertnom režime, ako je znázornené na obr. 31.1.34. Ďalšie informácie a popis možností ovládacích prvkov simulácie v expertnom režime nájdete v [9\. Simulation Controls.](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

![]({{ '/assets/images/operation_templates/31_extrusion/31_1_3d_extrusion/image032.jpg' | relative_url }})

Ovládacie prvky krokov v režime EXPERT

## Vytvoriť databázu

**Overiť údaje**![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})****

Systém skontroluje údaje. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvoriť databázu ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})**

Kliknutím na toto tlačidlo sa vygenerovala databáza pre nastavenie. (Pozri obr. 31.1.35.)

**Pridať súbor s kľúčom**

Akékoľvek informácie, ktoré nie sú definované v sprievodcovi, ale stále sa vzťahujú na daný proces, je možné načítať ako súbor s príponou .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt – tieto hodnoty je možné definovať v súbore s príponou .key, následne stačí zmeniť len tento súbor a simuláciu je možné odoslať znovu.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image048.jpg' | relative_url }})

Vytvoriť stránku databázy

**Súvisiace témy:**

[9\. Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

[16\. Object Properties](/docs/en/pre_processor/16_object_properties/16_object_properties/)

[19\. Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

[20\. Inter-Object Data Definition](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[Steady State Extrusion Lab](/docs/en/labs/extrusion_labs/steady_state_extrusion_lab1/)

[ALE Extrusion Lab](/docs/en/labs/extrusion_labs/ale_extrusion_lab1/)

[Lagrangian Extrusion Lab](/docs/en/labs/extrusion_labs/lagrangian_extrusion_lab1/)
