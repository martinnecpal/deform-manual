---
lang: sk
title: "13.2. Generovanie 3D Tet Mesh"
---

# 13.2. Generovanie 3D Tet Mesh

13.2.1. Generovanie 3D siete v riadenom režime
13.2.2. Generovanie 3D siete v expertnom režime

13.2.3. Nástroje na generovanie 3D sietí v režime Expert

  * Import Mesh

  * Uložiť sieť

  * Skontrolujte sieťovinu

  * Plocha a objem

  * Odstrániť sieť

  * Povrchová sieť

  * Pevná sieť

  * Manuálne odstraňovanie nečistôt

  * Zobraziť 3D

  * Zobraziť 2D prierez

  * Predvolené nastavenie

13.2.4. Všeobecné nastavenia pre sieť Tetrahehdral (Tet)

13.2.5. Váhové faktory siete

13.2.6. Okná hustoty siete

13.2.7. Povlaková sieť

13.2.8. Kritériá na opravu

13.2.9. Zabudované vo Flownete

## Generovanie 3D siete v riadenom režime

Na nasledujúcom obr. 13.2.1. sú zobrazené možnosti generovania siete v režime s riadením (![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }})). Na stránke siete v riadenom režime môžeme generovať len tetraedrický typ siete.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image001.jpg' | relative_url }})

Okno 3D Mesh s riadeným režimom

**Počet prvkov :** Počet prvkov, ktoré sa majú vygenerovať pre objekt, možno určiť jednoduchým nastavením posuvníka a výberom vhodnej hodnoty pre aktuálnu simuláciu.

**Preview![]({{ '/assets/icons/pre_icons/mo_mesh_preview_button.jpg' | relative_url }}) :**Táto funkcia umožňuje používateľovi zobraziť náhľad povrchovej siete objektu.

******Generovanie siete![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) : **Keď je používateľ spokojný s náhľadom povrchovej siete, sieť možno vygenerovať na objekte kliknutím na tlačidlo Generate Mesh (Generovať sieť).

**Delete**![]({{ '/assets/icons/pre_icons/mo_delete_button.jpg' | relative_url }}) : Táto funkcia odstráni vytvorenú sieť.

Na ovládanie parametrov siete, ako je veľkosť, tvar, hustota, typ prvkov atď..., musí používateľ prepnúť do expertného režimu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) pre pokročilejšie možnosti siete. Na nasledujúcom obr. 13.2.2. sú zobrazené možnosti siete dostupné z expertného režimu.

## Generovanie 3D siete v režime Expert

Na nasledujúcom Obr. 13.2.2. sú zobrazené možnosti generovania siete v režime Expert.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image002.jpg' | relative_url }})

Okno 3D Mesh v režime Expert

## Nástroje na generovanie 3D sietí v režime Expert

**Importovanie siete** ![]({{ '/assets/icons/pre_icons/mo_import_mesh_button.jpg' | relative_url }}) : Sieť možno do sprievodcu MO importovať zo súboru s kľúčovými slovami, databázového súboru alebo z ľubovoľného podporovaného formátu siete (PDA alebo univerzálny súbor).

**Uloženie siete** ![]({{ '/assets/icons/pre_icons/mo_save_mesh_button.jpg' | relative_url }}) : Táto funkcia uloží aktuálne vytvorenú sieť do súboru.

**Check Mesh** ![]({{ '/assets/icons/pre_icons/mo_check_mesh_button.jpg' | relative_url }}) : Pomocou funkcie Check Mesh (Skontrolovať sieť) možno skontrolovať, či nie sú v sieti problémy. Pri dokonalej sieti sa zobrazí vyskakovacie okno, ako je znázornené na obr. 13.2.3., keď používateľ klikne na možnosť check mesh (skontrolovať sieť).

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image004.jpg' | relative_url }})

Kontrola vyskakovacieho okna Mesh

**Plocha a objem** ![]({{ '/assets/icons/pre_icons/mo_area_volume.jpg' | relative_url }}) : Táto funkcia poskytuje informácie o ploche oka a objeme objektu. (Pozri obr. 13.2.4. )

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image005.jpg' | relative_url }})

Vyskakovacie okno Plocha a objem siete

**Generovať sieť** ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) : Sieť môžete vygenerovať kliknutím na tlačidlo Generovať sieť.

**Odstrániť sieť** ![]({{ '/assets/icons/pre_icons/mo_delete_mesh_button.jpg' | relative_url }}) : Táto funkcia odstráni vytvorenú sieť. Keď používateľ klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_mesh_button.jpg' | relative_url }}), zobrazí sa vyskakovacie okno, ako je znázornené na ( obr. 13.2.5.). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) je možné sieť vymazať.

  
![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image003.jpg' | relative_url }})

Odstránenie vyskakovacieho okna siete

**Povrchová sieť**![]({{ '/assets/icons/pre_icons/mo_surface_mesh_button.jpg' | relative_url }}) : Po nastavení všetkých parametrov siete je možné kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_surface_mesh_button.jpg' | relative_url }}) vytvoriť povrchovú sieť. Keď sa vygeneruje nová sieť pre objekt, ktorý má v súčasnosti sieť, stará sieť sa vymaže a nahradí sa novou sieťou. Ak dôjde k zlyhaniu pri generovaní povrchovej siete, pozrite si časť [Trouble shooting](/docs/sk/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/).

**Tvrdá sieť** ![]({{ '/assets/icons/pre_icons/mo_solid_mesh_button.jpg' | relative_url }}) : Po vygenerovaní povrchovej siete by mal používateľ skontrolovať sieť pred generovaním pevnej siete. Venujte osobitnú pozornosť primeranej hustote siete v oblastiach so zložitou geometriou. Po vygenerovaní prijateľnej povrchovej siete sa môže vygenerovať pevná sieť kliknutím na tlačidlo Generate Solid Mesh (Generovať pevnú sieť). Ak je povrchová sieť importovaná ako geometria, používateľ môže upustiť od generovania povrchovej siete a priamo umiestniť pevnú sieť na povrchovú sieť. Ak generovanie pevnej siete zlyhá, pozrite si časť [Trouble shooting](/docs/sk/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/).

**Ručné prepracovanie** ![]({{ '/assets/icons/pre_icons/mo_manual_remesh_button.jpg' | relative_url }}) : Ak simulácia pokračuje z predtým spustenej simulácie, odporúčané tlačidlo, na ktoré treba kliknúť, je Ručné prepracovanie. Tým sa automaticky vykoná extrakcia hraníc a používateľ bude vyzvaný na interpoláciu okrajových podmienok.

V priebehu simulácie DEFORM môže rozsiahla deformácia plastických alebo pórovitých objektov spôsobiť, že prvky v sieťach týchto objektov budú natoľko deformované, že sieť už nebude použiteľná (záporný Jakobsonov koeficient). Ak nastane tento stav, simulácia sa preruší a do súboru ProblemID.MSG sa zapíše chybové hlásenie. Ak chcete pokračovať v simulácii po tom, ako sa sieť stala nepoužiteľnou, objekt sa musí znovu vyrezať. Remeshing je proces nahradenia deformovanej siete novou nedeformovanou sieťou a interpolácie premenných poľa (deformácia, rýchlosť, poškodenie a teplota atď.) zo starej siete do novej siete.

V prípade šesťstennej (tehlovej) siete 3D v súčasnosti nedokáže vytvoriť tehlovú sieť, takže ak sa vyžaduje opätovné vytvorenie siete pre elastoplastickú tehlovú sieť, používateľ musí vytvoriť novú sieť mimo programu DEFORM a interpolovať stavové premenné a znovu aplikovať okrajové podmienky na novú sieť.

Vo väčšine prípadov prebieha remeshing a interpolácia automaticky bez zásahu používateľa.

Sieť na objekte je možné regenerovať aj ručne a interpolovať údaje zo starej siete. Postup na vykonanie manuálneho remeshingu je nasledujúci:

**Postup:**

  * Otvorte predprocesor.

  * Vyberte krok z databázy, v ktorom sa má vykonať remeshing, a načítajte ho do preprocesora. Ak sa objekt nebude remeshovať v poslednom kroku, môže byť potrebné remeshovať v skoršom kroku.

  * Vyberte objekt, ktorý chcete opraviť.
  * V okne Objekty vyberte možnosť Manual Remeshing (Ručné premazávanie).

  * Ak je potrebné upraviť geometriu dielu (napríklad orezanie blesku alebo vyrazenie pásu, možno to urobiť v tomto bode pomocou editora geometrie).

  * Podľa potreby upravte okná siete alebo iné parametre siete.
  * Vygenerujte novú sieť povrchu.
  * Vygenerujte novú pevnú sieť.
  * Interpolujte údaje zo starej siete do novej siete kliknutím na tlačidlo OK.
  * Interpolujte okrajové podmienky zo starej siete do novej siete, pokiaľ:

  * Súčasne s výmenou dielu sa vymieňajú aj lisovacie nástroje
  * Sieť sa pri remeshovaní viditeľne deformuje.
  * Pri opätovnom spustení problému sa okamžite vyskytne záporná chyba Jakobiánu.

  * Vygenerujte databázu a spustite simuláciu.

Ak sa sieť po remeshovaní viditeľne deformuje alebo ak súčasne meníte matrice, regenerujte sieť a interpolujte údaje, ale nie okrajové podmienky. Ak okrajové podmienky nie sú interpolované, je potrebné znovu vytvoriť všetky okrajové podmienky rýchlosti, prenosu tepla, medzi objektmi alebo iné okrajové podmienky. Ak nedošlo k žiadnym zmenám geometrie (napríklad orezanie súčiastky), potom stačí kliknúť na , čím sa vyťaží ohraničenie a zobrazí sa dialógové okno generovania siete. Po vytvorení siete sa pri výstupe vykoná interpolácia stavových premenných a okrajových podmienok.

**Východiskové nastavenie** ![]({{ '/assets/icons/pre_icons/mo_default_settings_button.jpg' | relative_url }}) : Keď používateľ klikne na záložku Default settings (Východiskové nastavenia), všetky nastavenia sa zmenia na východiskové hodnoty, v predvolenom nastavení bude okno Mesh (Sieť) v sivom režime, pretože nie sú definované žiadne okná mesh. Ak chce používateľ aktivovať okno mesh, musí zmeniť váhový faktor pre hustotu mesh zvýšením hodnoty posuvníka na 1.

**Zobraziť 3D**

Výberom tejto možnosti môže používateľ zobraziť 3D objekt v okne Display. Táto možnosť je užitočnejšia pre možnosť brick mesh.

**Zobraziť 2D prierez**

Výberom tejto možnosti môže používateľ zobraziť objekt 2D prierezu v okne Zobrazenie. Táto možnosť je užitočnejšia pre možnosť brick mesh (tehlová sieť).

**Typ siete** :

  * **Tetraedrická sieť** : Pomocou tejto možnosti môže používateľ vygenerovať tetraedrickú (tet) sieť s existujúcimi nastaveniami siete pre objekt. V predvolenom nastavení v DEFORM sa vyberie tetraherdická sieť.

  * **Brick mesh :** Pomocou tejto možnosti môže používateľ vygenerovať brick mesh s existujúcimi nastaveniami mesh pre objekt. Možnosti brick mesh nájdete v kapitole 13.3. Generovanie tehlovej siete

## **Všeobecné nastavenia pre sieť Tetrahehdral (Tet)**

V rámci programu DEFORM možno pre 3D objekty generovať dva rôzne typy sietí.

  * **Relatívna sieť**

Pomocou nastavenia relatívnej siete používateľ určí počet pevných prvkov, ktoré sa majú vygenerovať. Bez ohľadu na to, aký zložitý tvar bude mať diel, počet prvkov zostane v podstate konštantný. ( Obr. 13.2.6.)

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image006.jpg' | relative_url }})

Možnosti okna relatívnej siete

  * **Absolútna sieť**

Pomocou nastavenia absolútnej siete používateľ zadá veľkosť prvkov a systém určí celkový počet potrebných prvkov na základe veľkosti zadaného prvku a geometrie. S rastúcou zložitosťou súčiastky má počet prvkov tendenciu rásť. ( Obr. 13.2.7.)

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image007.jpg' | relative_url }})

Možnosti okna s absolútnou sieťou

  * **Povrchové prvky**

Počet povrchových prvkov (MGNELS) predstavuje približný počet povrchových prvkov, ktoré vygeneruje generátor siete. Automatický generátor siete (AMG) prevezme hodnotu MGNELS a vygeneruje sieť, ktorá bude obsahovať približne rovnaký počet prvkov. Táto hodnota sa ignoruje, ak sa používajú okná siete s definíciou absolútnej hustoty siete.

  * **Pomer veľkosti prvku**([MGSIZR](/docs/sk/keyword_documentation/m/mgsizr/))

Pomer maximálnej veľkosti medzi prvkami je jedným z viacerých spôsobov riadenia hustoty siete počas automatického generovania siete (AMG) určením pomeru hustoty uzlov.

  
Pri hodnote 3 pre [MGSIZR](/docs/sk/keyword_documentation/m/mgsizr/) bude najväčšia hrana prvku na objekte približne 3-krát väčšia ako najmenšia hrana prvku na tom istom objekte. Ak sa požadujú rovnako veľké prvky, potom je pomer veľkosti = 1. Ak je Size Ratio = 0, pomer veľkosti prvkov nebude faktorom pri rozdelení hustoty siete.

  * **Vnútorná jemnejšia sieť**

Táto funkcia definuje jemnú vnútornú sieť pre objekt pri sieťovaní. Táto funkcia je aktívna pre DEFORM-3D.Bolo pridané zaškrtávacie políčko, ktoré umožňuje používateľovi vytvoriť jemnejšiu vnútornú sieť. Túto funkciu možno použiť, keď chce používateľ vidieť viac pevných prvkov v celej hrúbke súčiastky. Upozorňujeme, že pri použití tejto možnosti sa môže výrazne zvýšiť celkový počet prvkov. Porovnanie s jemnejšou vnútornou sieťou a bez nej je vidieť na obr. 13.2.8..

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image008.jpg' | relative_url }})

Porovnanie siete s 10000 prvkami zadanými pri generovaní; a) vnútorná sieť bez jemnejšej vnútornej siete b) vnútorná sieť s jemnejšou vnútornou sieťou

## Váhové faktory siete

Váhové faktory alebo parametre (systémovo definovaná hustota siete) pre hraničné zakrivenie, teplotu, deformáciu a mieru deformácie určujú relatívne váhy hustoty siete, ktoré sa majú priradiť príslušnému parametru. (Pozri obr. 13.2.9.)

Hustoty teploty, deformácie a rýchlosti deformácie sú priradené na základe gradientov týchto parametrov, nie na základe absolútnych hodnôt parametrov. To znamená, že oblasť s rýchlou zmenou teploty v určitom smere dostane viac prvkov ako oblasť s rovnomerne vysokou teplotou.

Hodnoty zo všetkých kľúčových slov hustoty siete sa počas procesu generovania siete kombinujú, aby sa vytvorilo rozloženie hustoty siete v rámci geometrickej hranice.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image009.jpg' | relative_url }})

Okno 3D Mesh Weighting Factors

  * **Váhový faktor založený na zakrivení povrchu** (MGWCUV)

Váha zakrivenia povrchu ([MGWCUV](/docs/sk/keyword_documentation/m/mgwcuv/)) použije vyššiu hustotu siete v oblastiach, kde sú dĺžky hrán geometrie menšie. Účelom je použiť jemnejšiu sieť v oblastiach, kde sa používajú menšie hrany, aby sa v oblasti malých prvkov vytvorila jemnejšia sieť. Ak je hodnota [MGWCUV](/docs/sk/keyword_documentation/m/mgwcuv/) väčšia ako 0, hraničná oblasť s krivkami dostane v tejto oblasti vyššiu hustotu siete. Ak je hodnota [MGWCUV](/docs/sk/keyword_documentation/m/mgwcuv/) nastavená na 0, toto váhové kritérium sa ignoruje.

  * **Váhový faktor založený na teplote** (MGWTMP)

Tento váhový faktor ([MGWTMP](/docs/sk/keyword_documentation/m/mgwtmp/)) sa môže použiť na určenie jemných prvkov v oblastiach s vysokým teplotným gradientom.

  * **Vážiaci faktor základne napätia** (MGWSTN)

Na zachovanie jemnej siete v oblastiach s vysokým napätím možno tento váhový faktor ([MGWSTN](/docs/sk/keyword_documentation/m/mgwstn/)) upraviť.

  * **Váhový faktor založený na rýchlosti ťahu** (MGWSTR)

Ak sa na deformujúcom sa objekte nachádzajú oblasti s vysokou rýchlosťou deformácie a lokalizovanou deformáciou, potom sa použitím váhového faktora ([MGWSTR](/docs/sk/keyword_documentation/m/mgwstr/)) vytvorí jemná sieť v oblastiach s vysokým gradientom rýchlosti deformácie.

  * **Váhový faktor sieťových okien** (MGWUSR)

Váhový faktor okien definovaný používateľom ([MGWUSR](/docs/sk/keyword_documentation/m/mgwusr/)) sa používa v spojení s oknami Mesh Density. Užívateľom definované váhové rozdelenie použije vyššiu hustotu siete na oblasti so zadaným oknom hustoty. Ak je tento parameter nastavený na 0, okná siete sa počas automatického remeshovania ignorujú.

  * **Dodatočný váhový koeficient**

Poznámka:

Keď sa objekt deformuje, okno siete definované používateľom sa bude pohybovať podľa zložky rýchlosti priradenej tomuto oknu. Toto okno bude so sebou počas celej simulácie niesť váhu hustoty siete.

## Okná hustoty siete pre sieť Tet

Koncepcia okna Hustota siete (pozri obr. 13.2.10.) je podobná koncepcii hustoty siete definovanej používateľom. Hustota siete zadaná pre dané okno sa aplikuje na akýkoľvek geometrický bod (uzol alebo vrchol STL) vo vnútri okna. Okno hustoty siete sa však používa počas remeshingu aj počiatočného generovania siete, zatiaľ čo hustoty siete definované používateľom sa používajú len počas počiatočného generovania. Môže jej byť tiež priradená rýchlosť alebo môže sledovať pohyb iného objektu a môže byť definovaná v oblasti, cez ktorú ešte nebol obrobok deformovaný.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image012.jpg' | relative_url }})

Okno 3D Mesh Density

Hustota siete je definovaná počtom povrchových uzlov na jednotku dĺžky. Hodnoty hustoty siete môžu špecifikovať pomer hustoty siete medzi dvoma oblasťami v objekte alebo absolútnu dĺžku hrany prvku v oblasti na povrchu. V prípade relatívnej hustoty siete medzi jednou alebo viacerými oblasťami sa nezadaným oblastiam priradí globálna hodnota. V prípade absolútnej hustoty siete nezadané oblasti tiež nadobudnú globálnu hodnotu. V prípade špecifikácie absolútnej hustoty siete by si mal používateľ dať pozor na to, akú hodnotu hustoty použije.

Používateľ môže tiež importovať ľubovoľnú používateľom definovanú geometriu (vo formáte GEO) ako okno hustoty siete (pozri obr. 13.2.11.) na presnejšiu kontrolu hustoty siete na určitých oblastiach na objekte počas počiatočného generovania siete (pozri obr. 13.2.12.), ako aj remeshingu.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image011.jpg' | relative_url }})

Špecifikácia okna siete pomocou geometrie

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image010.jpg' | relative_url }})

Sieť vytvorená pomocou geometricky definovaného povrchu siete

**Definovanie okien hustoty siete** : Okno hustoty siete je možné definovať pomocou nižšie uvedených krokov,

  1. Vyberte číslo okna v záhlaví okna hustoty oka. Môžete definovať až 20 rôznych okien. Okrem základných dostupných typov okien siete môže používateľ definovať aj ľubovoľný tvar okna hustoty siete, ktorým môže byť akýkoľvek platný 3D GEO súbor vygenerovaný zo systému DEFORM.

  * Kliknite na tlačidlo Add bounding point (Pridať ohraničujúci bod) a kliknite na časť, aby sa vytvorilo okno hustoty siete.
  * Ťahaním okna upravte veľkosť a umiestnenie okna hustoty oka.
  * Po definovaní okna sa jeho hustota zadá do poľa v záhlaví Parametre.

  1. Rýchlosť pre okno siete možno definovať aj v smere x a/alebo y. Tieto hodnoty sa tiež nachádzajú v záhlaví Parameters (Parametre).
  2. Ak je potrebné okno otočiť, používateľ môže použiť tlačidlá na otáčanie v okne zobrazenia.
  3. Po aplikácii okna v polohe, ktorú si používateľ želá, sa stlačením tlačidla Zobraziť v okne zobrazenia zvýraznia uzly povrchu, ktoré sú uzavreté oknom siete. Stlačením tlačidla Hide (Skryť) sa zruší zvýraznenie uzlov, ktoré sú obsiahnuté oknom hustoty siete.

**Definícia okna** : Pomocou týchto možností je možné vytvoriť a upraviť rôzne okná 3D siete, ako je vysvetlené nižšie,

  * Na definovanie okna siete sa používajú možnosti **Box![]({{ '/assets/icons/pre_icons/mo_box_window_icon.jpg' | relative_url }})** , **Cylinder![]({{ '/assets/icons/pre_icons/mo_cylinder_window_icon.jpg' | relative_url }})** , **Ring![]({{ '/assets/icons/pre_icons/mo_hollow_cylinder_icon.jpg' | relative_url }}) **a **Polygon![]({{ '/assets/icons/pre_icons/mo_polygon_window_icon.jpg' | relative_url }}) **.
  * **Zmenšenie veľkosti, presun a otočenie okna** : používateľ môže zmeniť veľkosť okna pomocou možnosti Veľkosť riadiaceho bodu, používateľ môže presunúť okno pomocou možnosti Osová šípka a používateľ môže otočiť okno pomocou možnosti Osová rotácia.

  * **Šípka osi** : pomocou tejto možnosti môže používateľ posúvať okno v smere vybranej osi pozdĺž globálnej osi. Používateľ musí vybrať šípku osi, ktorej smerom sa má pohybovať, a potom potiahnuť šípku osi, okno interaktívne zmení svoju polohu, keď potiahneme šípku osi.

  * **Rotačná šípka** : pomocou tejto možnosti môže používateľ otáčať okno v smere zvolenej osi pozdĺž globálnej osi. Používateľ musí vybrať os, ktorej smerom sa má pohybovať, a potom otáčať rotačnou šípkou, okno sa bude interaktívne otáčať, keď budeme otáčať rotačnou šípkou.

  * **Ovládací bod veľkosti** : veľkosť okna možno ovládať pomocou ovládacích bodov veľkosti na základe miestneho súradnicového systému okna. Používateľ môže pozorovať možnosť nastavenia veľkosti na základe typu okna. Používateľ môže ťahaním riadiacich bodov veľkosti interaktívne meniť veľkosť pozdĺž osi v smere ťahania.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image015.jpg' | relative_url }})

  * **Modify**![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}) : pomocou tejto možnosti môže používateľ upraviť predtým definované okno.
  * **Duplikovať okno**![]({{ '/assets/icons/pre_icons/mo_duplicate_window_button.jpg' | relative_url }}) : pomocou tejto možnosti môže používateľ duplikovať existujúce okno a môže zmeniť polohu alebo veľkosť duplikovaného okna.
  * **Preview**![]({{ '/assets/icons/pre_icons/mo_preview_icon.jpg' | relative_url }}) : pomocou tejto možnosti môže používateľ zobraziť náhľad okna siete na objekte.

**Body** : Body predstavujú celkový počet bodov, ktoré tvoria okno hustoty siete.

**Hustota** : Hustota je požadovaná hodnota hustoty pre dané okno.

**Veľkosť** : Velocity je rýchlosť okna. Umožňuje, aby sa okno pohybovalo spolu s matricami. V prípadoch, keď nie je známa rýchlosť razníka, ako napríklad pri kovaní kladivom alebo pri lisovaní s riadeným zaťažením, by sa mal urobiť najlepší odhad konštantnej rýchlosti.

**Miestne okno na opätovné nastavenie: **

Poznámka:

Ak je oknu priradená rýchlosť, pred vykonaním druhej alebo tretej operácie by sa mala podľa potreby zmeniť jeho poloha.

**Dôležité aspekty pri definovaní okna hustoty siete:**

  * Musí existovať len jedno okno hustoty oka. Globálne hodnoty hustoty sa použijú pre každú oblasť, ktorá nie je vnútri okna.
  * Dávajte pozor na veľké pomery hustoty oka. Pomer hustoty 5:1 je veľký a pomer 10:1 je extrémny. Extrémne veľké pomery hustoty môžu viesť k problémom pri generovaní siete vrátane oveľa dlhšieho času potrebného na generovanie siete.
  * Absolútna hustota siete je mocný nástroj, pretože umožňuje definovať špecifické rozlíšenie v rôznych oblastiach súčiastky. Zoberme si prvok s hrúbkou 0,5''. Ak chcete zachovať 3 prvky v celej hrúbke prvku, zadajte v tejto oblasti absolútnu hustotu siete 6 prvkov/palec. Keď sa do tejto oblasti dostane viac materiálu, celkový počet prvkov sa zvýši podľa potreby, aby sa zachovalo požadované rozlíšenie.
  * Ak sa použije absolútna hustota, používateľ musí byť opatrný pri zadávaní hodnôt, pretože nie je stanovená horná hranica počtu prvkov.

## Povlak Mesh

Používateľ môže pomocou tejto možnosti pridať vrstvy povlaku a vygenerovať pre ne sieť. Povlaková sieť je tenká vrstva prvkov pozdĺž hranice objektu so špecifickými vlastnosťami. Pre pridané povlakové vrstvy môže používateľ priradiť materiál. (Pozri obr. 13.2.13.) Ďalšie informácie o používaní povlakovej siete nájdete v dokumente [Appendix XI](/docs/sk/appendices/appendix_xi__near_surface_mesh_functions/).

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image013.jpg' | relative_url }})

Okno z náterovej sieťoviny

**Zachovať premenlivý stav a okrajové podmienky** :

## Kritériá na opravu

Kritériá remeshingu (Autoremesh) sú najvhodnejším spôsobom, ako zvládnuť remeshing objektov, ktoré prechádzajú veľkou plastickou deformáciou. Okno Remeshing Criteria (Kritériá opätovného remeshovania) (pozri obr. 13.2.14. ) obsahuje skupinu parametrov, ktoré riadia, kedy a ako často sa bude sieť na objekte s okom regenerovať na základe priradenia určitých spúšťačov. Existujú štyri kľúčové slová, ktoré riadia spustenie postupu remeshingu pre objekt, sú to Hĺbka zásahu (RMDPTH), Max. Time Increment (RMTIME), Max. Step Increment (RMSTEP) a Max. Stroke Increment (RMSTRK). Keď sa splnia kritériá remeshovania podľa niektorého z týchto kľúčových slov alebo sa sieť stane nepoužiteľnou (záporný jakobián), objekt sa remeshuje. Ak objekt počas simulácie splní niektoré z kritérií remeshingu, vygeneruje sa nová sieť, informácie o riešení zo starej siete sa interpolujú na novú sieť a simulácia pokračuje.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image014.jpg' | relative_url }})

Okno nastavenia kritérií na opravu

Podrobnosti o maximálnej hĺbke zásahu (RMDPTH), maximálnom prírastku zdvihu (RMSTRK), maximálnom prírastku času (RMTIME), maximálnom prírastku kroku (RMSTEP) a účele kritérií nájdete v časti [13.1.8. Remeshing criteria](13_1_2d_mesh_generation.htm#13.1.8._Remeshing_criteria)

**Vzdialenosť prieniku** (**absolútna**) : Ak je zadané kladné číslo (v jednotke dĺžky), program vykoná kontrolu na každej hrane povrchu, ktorá má na každom konci kontaktný uzol. Vypočíta sa vzdialenosť od stredu hrany k povrchu matrice. Ak maximálna hĺbka prieniku prekročí zadanú hranicu, spustí sa opätovné meranie.

**Vzdialenosť prieniku** (**relatívna**) : Ak je zadané záporné číslo (zlomok), program vykoná kontrolu na každej hrane povrchu, ktorá má na každom konci kontaktný uzol. Vypočíta sa vzdialenosť od stredu hrany k povrchu matrice a vydelí sa pôvodnou dĺžkou hrany. Ak tento pomer prekročí veľkosť zadanej hodnoty, spustí sa opätovné obťahovanie.

**Východisková hodnota :** Preprocesor má teraz východiskovú hodnotu 0,7 s relatívnym nastavením.

**Možnosti globálneho a lokálneho odstránenia:**

Pre DEFORM-3D bolo generovanie sietí rozšírené o funkciu lokálneho sieťovania.  
Predvolené nastavenia poukazujú na existujúce globálne postupy remeshingu, pri ktorých sa každý prvok starej siete nahradí novým prvkom siete, po ktorom nasleduje interpolácia.   
V aktuálnej verzii sú všetky lokálne nastavenia súvisiace so sieťovaním uložené v lokálnych súboroch, nie v databáze.

To znamená, že keď používateľ skopíruje súbor databázy z jedného priečinka do druhého, miestne nastavenia remesh sa neprenesú, pokiaľ sa všetky súbory neskopírujú do pracovného priečinka.

**Lokálny povrch:** Pomocou tejto metódy lokálneho remeshovania môžeme remeshovať iba zlú sieť prvkov na povrchu podľa definovanej úrovne uzlov. Lokálny typ siete povrchu je rýchlejší ako typ siete plného telesa.

**Lokálne teleso:** Funkcia lokálneho vytvárania siete telesa umožňuje niekoľko možností kontroly veľkosti a kvality prvkov. Lokálne remeshing má tiež možnosti, aby sieťovanie bolo skutočne lokálne, aby sa minimalizovali chyby súvisiace s interpoláciou.

  
**Vnútorné prvky**

  * **Kontrola veľkosti**

  * **Priemer susedov** : O veľkosti prvku sa rozhoduje na základe priemernej veľkosti okolitých prvkov deformovanej siete.
  * **Škálovací faktor** : Veľkosť prvku bude zmenšená na základe menovacieho faktora uvedeného pre každú vrstvu smerom dovnútra.
  * **Prvky s dobrým tvarom** : Prvky, ktoré majú dobrý tvar, budú z remeshingu vynechané.
  * **Preskočte dobrý povrchový prvok** : Prvky, ktoré sú dobré na povrchu, budú vynechané z remeshingu.

## **Vstavaný vo Flownete**

V DB s veľkým počtom krokov bude vykresľovanie Flownetu trvať dlho, používateľ môže tento problém prekonať použitím vstavaného Flownetu. Keď používateľ použije vstavaný Flownet, Flownet sa vykresľuje počas simulácie problému.

**Postup nastavenia vstavaného systému Flownet:**

1\. Pre objekt obrobku po vygenerovaní geometrie a siete vyberte stránku Built-in Flownet. (Pozri obr. 13.2.15.)

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image016.jpg' | relative_url }})

Zabudované okno Flownet pre obrobok

2\. Vytvorte vstavaný flownet pomocou dostupných možností "Generate by Offset" alebo "Define Primitive" a po vytvorení flownetu ho môžete škálovať alebo polohovať pomocou možností "Scale" a "Positioning".

  
Zobrazí sa možnosť Generate by Offset (Generovať podľa posunu), ktorá požaduje zadanie veľkosti posunu, ktorým sa má sieť posunúť, aby sa vygeneroval vstavaný flownet, kliknite na tlačidlo OK a prijmite generovanie flownetu. Ak vygenerovaná vzdialenosť posunu nie je v poriadku, potom opäť vyberte možnosť "Generate by Offest" (Generovať podľa posunu) a zadajte novú veľkosť posunu a akceptujte, ako je znázornené na obr. 13.2.16.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image017.jpg' | relative_url }})

Integrovaná možnosť generovania Flownetu pomocou posunu

Možnosť Primitive geometry (Primitívna geometria) možno použiť aj na použitie primitívnej geometrie ako zabudovaného flownetu Po vytvorení primitív bude potrebné polohovanie na lokalizáciu alebo môže byť potrebné škálovanie na zmenu veľkosti vytvoreného primitívu, aby sa mohol použiť ako zabudovaný flownet, ako je znázornené na obr. 13.2.17.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image018.jpg' | relative_url }})

Zabudované generovanie siete Flownet pomocou možnosti definovať primitívne

3\. Po vygenerovaní vstavaného flownetu použite možnosť slicing a nakrájajte objekt na plátky, aby ste lepšie vizualizovali vygenerovaný vstavaný flownet, ako je znázornené na obr. 13.2.18. Používateľ môže tiež pozorovať len vstavaný flownet zaškrtnutím políčka "Show built-in flownet only" (Zobraziť len vstavaný flownet).

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_2_3d_tet_mesh_generation/13_2_image019.jpg' | relative_url }})

Zabudovaná aplikácia Flownet s nakrájaným objektom

Pre zabudovaný flownet remesh sú k dispozícii možnosti, ktoré umožňujú vykonať remeshovanie zabudovaného flownetu alebo remeshovať zabudovaný flownet každých niekoľko krokov simulácie.

  
K dispozícii sú aj ďalšie možnosti na uloženie vygenerovaného vstavaného flownetu, import súboru geometrie pre vstavaný flownet a možnosti na odstránenie vstavaného flownetu.

  
**Import zabudovaného systému Flownet** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}): Importuje zabudovaný systém Flownet

**Uloženie zabudovaného Flownetu do súboru s geometriou** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) : Uloží zabudovaný Flownet do súboru s geometriou (iba vo formáte GEO).

**Odstránenie vstavaného systému Flownet**![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}) : Odstráni vstavaný systém Flownet

**Súvisiace témy:**

[13\. Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/)

[13.1. 2D Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/)

[13.3. 3D Brick Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/)
