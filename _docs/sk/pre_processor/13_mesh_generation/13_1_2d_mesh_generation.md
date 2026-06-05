---
lang: sk
title: "13.1. Generovanie 2D siete"
---

# 13.1. Generovanie 2D siete

  
13.1.1. Generovanie siete v riadenom režime

13.1.2. Generovanie siete v expertnom režime

13.1.3. Nástroje na generovanie sietí v režime Expert

  * Import Mesh

  * Uložiť sieť

  * Skontrolujte sieťovinu

  * Plocha a objem

  * Odstrániť sieť

  * Zobraziť sieť

  * Manuálne odstraňovanie nečistôt

  * Predvolené nastavenie

13.1.4. Všeobecné nastavenia

13.1.5. Váhové faktory siete

13.1.6. Okná hustoty siete

13.1.7. Povrchová úprava

13.1.8. Kritériá na opravu

13.1.9. Rozšírené nastavenia

13.1.10. Sieť definovaná používateľom

## Generovanie siete v riadenom režime

Na nasledujúcom obr. 13.1.1. sú zobrazené možnosti generovania siete v režime Guided (![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }})).

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image001.jpg' | relative_url }})

Okno nastavení siete v režime Guided

**Počet prvkov:******Počet prvkov, ktoré sa majú vygenerovať pre objekt, možno určiť jednoduchým nastavením posuvníka a výberom vhodnej hodnoty pre aktuálnu simuláciu.

**Generovať sieť** ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) : Sieť môžete vygenerovať kliknutím na tlačidlo Generovať sieť.

**Odstrániť sieť** ![]({{ '/assets/icons/pre_icons/mo_delete_button.jpg' | relative_url }}) : Táto funkcia odstráni vytvorenú sieť.

## Generovanie siete v režime Expert

Na ovládanie parametrov siete, ako je veľkosť, tvar, hustota, typ prvku atď..., musí používateľ prepnúť do expertného režimu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) pre pokročilejšie možnosti siete. Na nasledujúcom obr. 13.1.2. sú zobrazené možnosti siete dostupné z režimu Expert.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image002.jpg' | relative_url }})

Okno nastavení siete v režime Expert

## Nástroje na generovanie sietí v režime Expert

**Importovanie siete** ![]({{ '/assets/icons/pre_icons/mo_import_mesh_button.jpg' | relative_url }}) : Sieť možno do preprocesora importovať zo súboru s kľúčovými slovami, databázového súboru alebo z ľubovoľného podporovaného formátu siete (.DB, .Key file a . ANS).

**Uloženie siete** ![]({{ '/assets/icons/pre_icons/mo_save_mesh_button.jpg' | relative_url }}) : Táto funkcia uloží aktuálne vytvorenú sieť do súboru.

**Check Mesh** ![]({{ '/assets/icons/pre_icons/mo_check_mesh_button.jpg' | relative_url }}) : Pomocou funkcie Check Mesh (Skontrolovať sieť) možno skontrolovať, či nie sú v sieti problémy. Pri dokonalej sieti sa zobrazí vyskakovacie okno, ako je znázornené na obr. 13.1.3., keď používateľ klikne na možnosť![]({{ '/assets/icons/pre_icons/mo_check_mesh_button.jpg' | relative_url }}).

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image003.jpg' | relative_url }})

Kontrola vyskakovacieho okna siete

**Plocha a objem** ![]({{ '/assets/icons/pre_icons/mo_area_volume.jpg' | relative_url }}) : Táto funkcia poskytuje informácie o ploche oka a objeme objektu. (Pozri obr. 13.1.4.)

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image004.jpg' | relative_url }})

Vyskakovacie okno Plocha a objem siete

**Delete Mesh** ![]({{ '/assets/icons/pre_icons/mo_delete_mesh_button.jpg' | relative_url }}) : Odstráni sieť vytvorenú pre objekt.

  
**Zobraziť sieť**![]({{ '/assets/icons/pre_icons/mo_show_mesh_button.jpg' | relative_url }}) : Keď používateľ klikne na Zobraziť sieť, v okne zobrazenia sa zobrazí vygenerovaná sieť. Tlačidlo Zobraziť sieť prepína medzi zobrazením siete a geometrie objektu.

**Ručné prepracovanie** ![]({{ '/assets/icons/pre_icons/mo_manual_remesh_button.jpg' | relative_url }}) : Ak simulácia pokračuje z predtým spustenej simulácie, odporúčané tlačidlo, na ktoré treba kliknúť, je Ručné prepracovanie. Tým sa automaticky vykoná extrakcia hraníc a používateľ bude vyzvaný na interpoláciu okrajových podmienok.

V priebehu simulácie DEFORM môže rozsiahla deformácia plastických alebo pórovitých objektov spôsobiť, že prvky v sieťach týchto objektov budú natoľko deformované, že sieť už nebude použiteľná (záporný Jakobsonov koeficient). Ak nastane tento stav, simulácia sa preruší a do súboru ProblemID.MSG sa zapíše chybové hlásenie. Ak chcete pokračovať v simulácii po tom, ako sa sieť stala nepoužiteľnou, objekt sa musí znovu vyrezať. Remeshing je proces nahradenia deformovanej siete novou nedeformovanou sieťou a interpolácie premenných poľa (deformácia, rýchlosť, poškodenie a teplota atď.) zo starej siete do novej siete.

Vo väčšine prípadov sa remeshing a interpolácia vykonávajú automaticky bez zásahu používateľa.

Sieť na objekte je možné regenerovať aj ručne a interpolovať údaje zo starej siete. Postup na vykonanie manuálneho remeshingu je nasledujúci:

**Postup**

  * Otvorte predprocesor.
  * Vyberte krok z databázy, v ktorom sa má vykonať remeshing, a načítajte ho do preprocesora. Ak sa objekt v poslednom kroku neremešuje, môže byť potrebné vykonať remešovanie v skoršom kroku.
  * Vyberte objekt, ktorý chcete opraviť.
  * V okne Objekty vyberte možnosť Manual Remeshing (Ručné premazávanie).

  * Ak je potrebné upraviť geometriu dielu (napríklad orezanie blesku alebo vyrazenie pásu, možno to urobiť v tomto bode pomocou editora geometrie).

  * Podľa potreby upravte okná siete alebo iné parametre siete.
  * Vygenerujte novú sieť.
  * Interpolujte údaje zo starej siete do novej siete kliknutím na tlačidlo OK.
  * Interpolujte okrajové podmienky zo starej siete do novej siete, pokiaľ:

  * Súčasne s výmenou dielu sa vymieňajú aj lisovacie nástroje
  * Sieť sa pri remeshovaní viditeľne deformuje.
  * Pri opätovnom spustení problému sa okamžite vyskytne záporná chyba Jakobiánu.

  * Vygenerujte databázu a spustite simuláciu.

Ak sa sieť po remeshovaní viditeľne deformuje alebo ak súčasne meníte matrice, regenerujte sieť a interpolujte údaje, ale nie okrajové podmienky. Ak okrajové podmienky nie sú interpolované, je potrebné znovu vytvoriť všetky okrajové podmienky rýchlosti, prenosu tepla, medzi objektmi alebo iné okrajové podmienky. Ak nedošlo k žiadnym zmenám geometrie (napríklad orezanie súčiastky), potom stačí kliknúť na ![]({{ '/assets/icons/pre_icons/mo_manual_remesh_button.jpg' | relative_url }}), čím sa extrahuje ohraničenie a zobrazí sa dialógové okno generovania siete. Po vytvorení siete sa pri výstupe vykoná interpolácia stavových premenných a okrajových podmienok.

**Východiskové nastavenie** ![]({{ '/assets/icons/pre_icons/mo_default_settings_button.jpg' | relative_url }}): Keď používateľ klikne na záložku Default settings (Východiskové nastavenia), všetky nastavenia sa zmenia na východiskové hodnoty, v predvolenom nastavení bude okno Mesh v sivom režime, pretože nie sú definované žiadne okná mesh. Ak chce používateľ aktivovať okno mesh, musí zmeniť váhový faktor pre hustotu mesh zvýšením hodnoty posuvníka na 1.

## Všeobecné nastavenia

Okno Generovanie siete (pozri obr. 13.1.2.) umožňuje používateľovi generovať sieť pre aktuálny objekt. Hustotu siete možno riadiť buď systémom na základe nastavení, alebo môže používateľ priamo priradiť veľkosť prvku.

  * **Metóda nastavenia systému** využíva systém váh a priradených okien na riadenie veľkosti prvkov počas počiatočného generovania siete a následného automatického obnovovania siete.
  * **Užívateľsky definované** umožňuje používateľovi špecifikovať určité oblasti na objekte, ktoré majú mať vyššiu hustotu prvkov v porovnaní s inými oblasťami objektu len počas počiatočného generovania siete (na túto špecifikáciu hustoty sa neodkazuje počas automatického remeshingu).

Hustota siete sa vzťahuje na veľkosť prvkov, ktoré sa vytvoria v rámci hranice objektu. Hustota siete je primárne založená na zadanom celkovom počte prvkov a na ovládacích prvkoch hustoty siete "Point" (Bod) alebo "Parameter" (Parameter). Rozlíšenie mriežky vzorky a tolerancie kritických bodov tiež ovplyvňujú hustotu siete, ale v menšej miere ako ostatné parametre.

Hustota siete je definovaná počtom uzlov na jednotku dĺžky, spravidla pozdĺž okraja objektu. Hodnoty hustoty siete určujú pomer hustoty siete medzi dvoma oblasťami v objekte. Nevzťahujú sa na absolútny počet uzlov. Musia sa teda špecifikovať aspoň dve oblasti s rôznou hustotou.

Vyššia hustota siete (viac prvkov na jednotku plochy/objemu) ponúka zvýšenú presnosť a rozlíšenie geometrie a premenných polí, ako sú deformácia, teplota a poškodenie. Vo všeobecnosti však platí, že s rastúcim počtom uzlov sa zvyšuje čas potrebný na vyriešenie problému počítačom. Preto je žiaduce mať veľký počet malých prvkov (vysoká hustota) v oblastiach, kde sa vyskytujú veľké gradienty hodnôt deformácie, teploty alebo poškodenia. Naopak, aby sa šetrili výpočtové zdroje, je žiaduce mať malý počet relatívne veľkých prvkov v oblastiach, kde dochádza k veľmi malej deformácii alebo kde sú gradienty veľmi malé.

Ďalšie problémy súvisiace s generovaním sietí:

  * Príliš hrubá sieť v rohoch môže spôsobiť degradáciu siete a problémy s remeshingom.
  * Príliš hrubá sieť v oblastiach s lokalizovanými povrchovými efektmi (t. j. vysoké poškodenie pozdĺž povrchu) môže spôsobiť pokles špičkových hodnôt v dôsledku chýb interpolácie počas remeshingu.

**Nastavenie systému:**

  * ******Počet prvkov (MGNELM)**

Počet prvkov siete predstavuje približný počet prvkov, ktoré systém vytvorí. Automatický generátor siete (AMG) prevezme hodnotu pre [MGNELM](/docs/sk/keyword_documentation/m/mgnelm/) a vygeneruje sieť, ktorá bude obsahovať približne rovnaký počet prvkov.

Chyba medzi počtom zadaných prvkov a počtom vygenerovaných prvkov je zvyčajne približne desať percent. Pri generovaní siete sa zadaný celkový počet prvkov používa v spojení s ovládacími prvkami "Point" (Bod) a "Parameter" (Parameter) na určenie hustoty siete.

  * **Počet prvkov hrúbky (MGTELM)**

Pomer maximálnej hrúbky je jedným z viacerých spôsobov riadenia hustoty siete počas automatického generovania siete (AMG). Počet prvkov v smere hrúbky predstavuje približný počet prvkov, ktoré systém vygeneruje v smere hrúbky ľubovoľnej oblasti súčiastky. Automatický generátor siete (AMG) vezme hodnotu pre [MGTELM](/docs/sk/keyword_documentation/m/mgtelm/) a vygeneruje sieť, ktorá bude mať tento počet prvkov naprieč najtenšou časťou. Ak je napríklad hodnota [MGTELM](/docs/sk/keyword_documentation/m/mgtelm/) nastavená na 4, AMG sa pokúsi mať 4 prvky naprieč hrúbkou geometrie.

Smer hrúbky objektu je kolmý na rozvetvenú os stredovej čiary pre každú oblasť dielu. Celkový počet prvkov, ktoré sa majú vytvoriť v sieti, sa riadi hodnotou počtu prvkov v kľúčovom slove [MGNELM](/docs/sk/keyword_documentation/m/mgnelm/) . Ak by hodnota hrúbky prvkov viedla k sieti, ktorá by obsahovala viac prvkov, ako je hodnota uvedená v slove [MGNELM](/docs/sk/keyword_documentation/m/mgnelm/), hodnota [MGNELM](/docs/sk/keyword_documentation/m/mgnelm/) by sa zmenšila tak, aby sieť obsahovala približne [MGNELM](/docs/sk/keyword_documentation/m/mgnelm/) prvkov. Ak hodnota [MGTELM](/docs/sk/keyword_documentation/m/mgtelm/) vedie k sieti, ktorá obsahuje menej ako [MGNELM](/docs/sk/keyword_documentation/m/mgnelm/) prvkov, zostávajúce prvky sa rozdelia na iné používateľom zadané ovládacie prvky hustoty siete (zakrivenie, deformácia, miera deformácie a teplota).

  * **Pomer veľkosti prvkov (MGSIZR)**

Pomer maximálnej veľkosti medzi prvkami je jedným z viacerých spôsobov riadenia hustoty siete počas automatického generovania siete (AMG) určením pomeru hustoty uzlov.

Pri hodnote 3 pre [MGSIZR](/docs/sk/keyword_documentation/m/mgsizr/) bude najväčšia hrana prvku na objekte približne 3-krát väčšia ako najmenšia hrana prvku na tom istom objekte. Ak sa požadujú rovnako veľké prvky, potom je pomer veľkosti = 1. Ak je Size Ratio = 0, pomer veľkosti prvkov nebude faktorom pri rozdelení hustoty siete.

  * **Relatívny typ siete**

Pomocou nastavenia relatívneho typu siete používateľ určí počet prvkov, ktoré sa majú generovať, s pomerom hrúbky prvkov a veľkosti prvkov. (Pozri obr. 13.1.5.)

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image005.jpg' | relative_url }})

Možnosť absolútneho typu oka

  * Sieť absolútneho typu

Pomocou nastavenia absolútneho typu siete používateľ zadá veľkosť prvkov a systém určí celkový počet prvkov, ktoré sú potrebné, na základe veľkosti zadaného prvku, pomeru veľkosti, hrúbky prvku a geometrie. S rastúcou zložitosťou súčiastky má počet prvkov tendenciu rásť. (Pozri obr. 13.1.6.)

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image006.jpg' | relative_url }})

Možnosť absolútneho typu oka

  * **Generovanie mapovej siete**

Mapované sieťovanie sa môže použiť v počiatočných fázach procesu tvárnenia. Keďže geometria obrobku nadobúda počas tvárnenia zložitý tvar, sieť je vystavená niekoľkým preriešeniam a mapované sieťovanie nemusí byť schopné prežiť takéto zmeny geometrie a preriešenie môže zlyhať. Generovanie mapovanej siete je vidieť na obr. 13.1.7.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image007.jpg' | relative_url }})

Možnosť typu mapovanej siete

  * **Zohľadnenie kontaktu s hlavnými objektmi**

## Váhové faktory siete

Váhové faktory alebo parametre (systémovo definovaná hustota siete) pre hraničné zakrivenie, teplotu, deformáciu a mieru deformácie určujú relatívne váhy hustoty siete, ktoré sa majú priradiť k príslušnému parametru. (Pozri obr. 13.1.8.)

Hustoty teploty, deformácie a rýchlosti deformácie sú priradené na základe gradientov týchto parametrov, nie na základe absolútnych hodnôt parametrov. To znamená, že oblasť s rýchlou zmenou teploty v určitom smere dostane viac prvkov ako oblasť s rovnomerne vysokou teplotou.

Hodnoty zo všetkých kľúčových slov hustoty siete sa počas procesu generovania siete kombinujú, aby sa vytvorilo rozloženie hustoty siete v rámci geometrickej hranice.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image008.jpg' | relative_url }})

Okno váhových faktorov siete pre 2D

  * **Váhový faktor založený na hraničnej krivosti (MGWCUV)**

Váha hraničnej krivosti použije vyššiu hustotu siete na krivky na hranici objektov. Ak je hodnota [MGWCUV](/docs/sk/keyword_documentation/m/mgwcuv/) väčšia ako 0, hraničná oblasť s krivkami dostane v tejto oblasti vyššiu hustotu siete. Ak je hodnota [MGNELM](/docs/sk/keyword_documentation/m/mgnelm/) nastavená na 0, toto kritérium váženia sa ignoruje.

Hodnoty zo všetkých kľúčových slov hustoty siete sa počas procesu generovania siete kombinujú, aby sa vytvorilo rozloženie hustoty siete v rámci geometrickej hranice.

  * **Váhový faktor základne napätia (MGWSTN)**

Na zachovanie jemnej siete v oblastiach s vysokým napätím možno tento váhový faktor ([MGWSTN](/docs/sk/keyword_documentation/m/mgwstn/)) upraviť. Od verzie 12 pridaná možnosť Use Gradient (Použiť gradient) pre váhový faktor základne deformácie

  * **Váhový faktor založený na rýchlosti ťahu (MGWSTR)**

Ak sa na deformujúcom sa objekte nachádzajú oblasti s vysokou rýchlosťou deformácie ([MGWSTR](/docs/sk/keyword_documentation/m/mgwstr/)) a lokalizovanou deformáciou, potom použitie tohto váhového faktora spôsobí, že v oblastiach s vysokým gradientom rýchlosti deformácie sa vytvorí jemná sieť. Od verzie 12 pridaná možnosť Use Gradient (Použiť gradient) pre základný váhový faktor miery deformácie

  * **Váhový faktor založený na teplote (MGWTMP)**

Tento váhový faktor ([MGWTMP](/docs/sk/keyword_documentation/m/mgwtmp/)) sa môže použiť na určenie jemných prvkov v oblastiach s vysokým teplotným gradientom.

  * **Váhový faktor sieťových okien (MGWUSR)**

Váhový faktor okien definovaný používateľom sa používa v spojení s oknami Mesh Density ([MGWUSR](/docs/sk/keyword_documentation/m/mgwusr/)). Užívateľom definované váhové rozdelenie použije vyššiu hustotu siete na oblasti so zadaným oknom hustoty. Ak je tento parameter nastavený na 0, okná siete sa počas automatického remeshovania ignorujú.

Poznámka:

Keď sa objekt deformuje, okno siete definované používateľom sa bude pohybovať podľa zložky rýchlosti priradenej tomuto oknu. Toto okno bude so sebou počas celej simulácie niesť váhu hustoty siete.

## Okná s hustotou siete

Koncept okna Hustota siete (pozri obr. 13.1.9.) je podobný konceptu hustoty siete definovanej používateľom. Hustota siete zadaná pre dané okno sa aplikuje na akýkoľvek geometrický bod (uzol alebo vrchol STL) vo vnútri okna. Okno hustoty siete sa však používa počas opätovného sieťovania aj počiatočného generovania siete, zatiaľ čo hustoty siete definované používateľom sa používajú len počas počiatočného generovania. Môže jej byť tiež priradená rýchlosť alebo môže sledovať pohyb iného objektu a môže byť definovaná v oblasti, cez ktorú ešte nebol obrobok deformovaný.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image009.jpg' | relative_url }})

Okná hustoty siete pre 2D

Okno hustoty siete určuje oblasť v priestore, ktorá sa bude pohybovať s objektom počas deformácie. Na túto oblasť sa aplikuje definícia hustoty oka a spôsobí, že oblasť bude mať príslušnú hustotu oka. (Pozri obr. 13.1.9.)

Dôležité skutočnosti, ktoré je potrebné poznamenať:

Okno hustoty siete musí pretínať hranicu objektu.

**Definovanie okien hustoty siete** : Okno hustoty siete je možné definovať pomocou nižšie uvedených krokov,

  * Vyberte číslo okna v záhlaví okna hustoty oka.
  * Pridať body, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_2d_add_point_button.jpg' | relative_url }}) pre pridanie bodov. Vytvorte okno definovaním 3 alebo viacerých bodov v požadovanej oblasti výberom ![]({{ '/assets/icons/pre_icons/mo_2d_polygon_window_icon.jpg' | relative_url }}) .
  * Po definovaní okna sa jeho relatívna hustota siete alebo veľkosť prvku zadá do poľa v záhlaví Parameters (Parametre).
  * Rýchlosť pre okno siete možno definovať aj v smere x a/alebo y.
  * Tieto hodnoty sa nachádzajú aj v záhlaví Parameters.
  * Nezabudnite nastaviť váhu oblastí definovaných používateľom na nenulovú hodnotu v rámci váhových faktorov.

**Definícia okna [2D]** : Pomocou týchto možností možno vytvoriť a upraviť rôzne 2d okná siete, ako je vysvetlené nižšie,

Na definovanie okna Mesh sú používateľovi k dispozícii možnosti **Polygon**![]({{ '/assets/icons/pre_icons/mo_2d_polygon_window_icon.jpg' | relative_url }}) , **Rectangle**![]({{ '/assets/icons/pre_icons/mo_2d_rectangle_window_icon.jpg' | relative_url }}) a **Circle**![]({{ '/assets/icons/pre_icons/mo_2d_circle_window_icon.jpg' | relative_url }}).

**Add****a****point**![]({{ '/assets/icons/pre_icons/mo_2d_add_point_button.jpg' | relative_url }}) : Pomocou tejto možnosti môže používateľ pridať body na definovanie okna siete.

**Delete****a****point**![]({{ '/assets/icons/pre_icons/mo_2d_delete_point_button.jpg' | relative_url }}) : Pomocou tejto možnosti môže používateľ odstrániť body definovaného okna siete.

**Premiestniť****bod**![]({{ '/assets/icons/pre_icons/mo_2d_relocate_point_button.jpg' | relative_url }}) : Pomocou tejto možnosti môže používateľ premiestniť body definovaného okna siete.

**Modify**![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}) : Pomocou tejto možnosti môže používateľ upraviť predtým definované okno siete.

**Duplikovať**![]({{ '/assets/icons/pre_icons/mo_duplicate_window_button.jpg' | relative_url }}) : Pomocou tejto možnosti môže používateľ duplikovať existujúce okno a môže premiestniť body duplikovaného okna.

K oknám s hustotou siete sú priradené tieto údaje:

**Body**

Body predstavujú celkový počet bodov, ktoré tvoria okno hustoty siete.

**Hustota**

Hustota je požadovaná hodnota hustoty pre dané okno.

Ako vybrať hustotu oka: Určite požadovanú najjemnejšiu hustotu oka na základe predpokladaného zakrivenia, rohov výlisku, veľkosti defektu atď. Napríklad pre polomer 0,125 by sme chceli mať prvky o niečo menšie (možno 0,100"). To by zodpovedalo absolútnej hustote siete 10 (1 / 0,100). Teraz určte globálnu hustotu tak, že zoberiete 1/3 tejto hodnoty, takže do poľa globálnej hustoty v okne Mesh Density Windows zadajte 3.

**Rýchlosť**

Rýchlosť je rýchlosť okna. Umožňuje, aby sa okno pohybovalo spolu s matricami. Rýchlosť môže byť v smere X, v smere Y alebo ich kombinácia.

Pohyb okna s hustotou pletiva: Oknu hustoty siete možno priradiť konštantnú rýchlosť. To je užitočné v situáciách, keď je potrebné definovať vyššiu hustotu okolo pohybujúceho sa objektu, napríklad úderníka. Oknu by mala byť pridelená rovnaká rýchlosť a smer ako dierovaniu. V prípadoch, keď nie je známa rýchlosť razníka, napríklad pri kovaní kladivom alebo pri lisovaní s riadeným zaťažením, by sa mal urobiť najlepší odhad konštantnej rýchlosti.

Poznámka:

Ak je oknu priradená rýchlosť, pred vykonaním druhej alebo tretej operácie by sa mala podľa potreby zmeniť jeho poloha.

## Povlak

Používateľ môže pomocou tejto možnosti pridať vrstvy povlaku a vygenerovať pre ne sieť. Pre pridaný povlakový materiál môže používateľ priradiť materiál. (Pozri obr. 13.1.10.) Ďalšie informácie o používaní okien povlakovania nájdete v dokumente [Appendix XI](/docs/sk/appendices/appendix_xi__near_surface_mesh_functions/).

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image010.jpg' | relative_url }})

Povlak Okno Mesh

## Kritériá na opravu

Kritériá remeshingu (Autoremesh) sú najvhodnejším spôsobom, ako zvládnuť remeshing objektov, ktoré prechádzajú veľkou plastickou deformáciou. Okno Remeshing Criteria (Kritériá opätovného remeshovania) (pozri obr. 13.1.11.) obsahuje skupinu parametrov, ktoré riadia, kedy a ako často sa bude sieť na objekte s okom regenerovať na základe priradenia určitých spúšťačov. Existujú štyri kľúčové slová, ktoré riadia spustenie postupu remeshingu pre objekt, sú to Hĺbka zásahu ([RMDPTH](/docs/sk/keyword_documentation/r/rmdpth/)),Max. Time Increment ([RMTIME](/docs/sk/keyword_documentation/r/rmtime/)), Max. Step Increment ([RMSTEP](/docs/sk/keyword_documentation/r/rmstep/)) a Max. Prírastok zdvihu ([RMSTRK](/docs/sk/keyword_documentation/r/rmstrk/)). Keď sa splnia kritériá remeshovania podľa niektorého z týchto kľúčových slov alebo sa sieť stane nepoužiteľnou (záporný jakobián), objekt sa remeshuje. Ak objekt počas simulácie splní niektoré z kritérií remeshingu, vygeneruje sa nová sieť, informácie o riešení zo starej siete sa interpolujú na novú sieť a simulácia pokračuje.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image011.jpg' | relative_url }})

Okno Kritériá na opravu

****

**Maximálna hĺbka interferencie (RMDPTH)**
Maximálna hĺbka interferencie ([RMDPTH](/docs/sk/keyword_documentation/r/rmdpth/)) sa používa na spustenie postupu remeshingu. Ak akákoľvek časť hlavného objektu prenikne do podriadeného objektu nad hĺbku uvedenú v položke [RMDPTH](/docs/sk/keyword_documentation/r/rmdpth/), spustí sa opätovné vymazanie.

Hĺbka interferencie riadi spustenie postupu remeshingu na základe hĺbky interferencie medzi podriadeným objektom a hlavným objektom. Hĺbka interferencie je hĺbka, v ktorej hrana prvku podriadeného objektu pretína povrch hlavného objektu. Objekt, ktorý sa má remeshovať, musí byť podriadený objekt.

Parameter hĺbky zásahu by sa mal používať pri extrémne ostrých rohoch, kde je polomer rohu takmer rovnako veľký ako dĺžka hrany priľahlého prvku. Hĺbka sieťovania by mala byť nastavená približne na polovicu dĺžky hrany prvku. Príliš veľká hĺbka zásahu môže spôsobiť nadmernú stratu objemu. Príliš malá hodnota môže spôsobiť príliš veľa remeshovaní, čo vedie k pomalému času behu a nadmernej chybe interpolácie.

Ak dochádza k prenikaniu oka, prvým krokom by malo byť použitie ovládacích prvkov hustoty oka na umiestnenie menšieho oka do oblasti, v ktorej dochádza k prenikaniu oka. Ak sa problémy stále vyskytujú, je možné použiť hĺbku zásahu.

**Maximálny prírastok zdvihu (RMSTRK)**
Vždy, keď je maximálny prírastok zdvihu ([RMSTRK](/docs/sk/keyword_documentation/r/rmstrk/)) prekročený o prírastok zdvihu primárnej matrice od posledného kroku opätovného oddeľovania, spustí sa nový krok opätovného oddeľovania.

**Maximálny prírastok času (RMTIME)**
Kedykoľvek uplynie maximálny časový prírastok ([RMTIME](/docs/sk/keyword_documentation/r/rmtime/)) (hodnota uplynulého času) od posledného kroku opätovného merania, spustí sa nový krok opätovného merania. Kľúčové slovo [RMTIME](/docs/sk/keyword_documentation/r/rmtime/) riadi iniciovanie postupu remeshovania na základe času procesu meraného od posledného remeshovania. Je to hodnota času procesu, ktorý môže uplynúť medzi remeshovaním objektu. Pri hodnote 10 pre [RMTIME](/docs/sk/keyword_documentation/r/rmtime/) sa bude objekt remeshovať najmenej každých 10 sekúnd. To je užitočné, keď sa simulácia predčasne zastaví z dôvodu zápornej jacobovej chyby. Skôr ako sa sieť stane nepoužiteľnou, objekt sa môže remeshovať. Uplynulý čas procesu medzi remeshovaním sa nepoužije na určenie, kedy sa objekt remeshuje.

**Maximálny prírastok kroku (RMSTEP)**
Kedykoľvek od posledného kroku remeshingu dôjde k maximálnemu prírastku kroku (počet krokov), spustí sa nový krok remeshingu. Kľúčové slovo [RMSTEP](/docs/sk/keyword_documentation/r/rmstep/) riadi začatie postupu remeshingu na základe počtu simulačných krokov meraných od posledného remeshingu. Je to hodnota simulačných krokov, ktoré môžu uplynúť medzi remeshovaním objektu. Pri hodnote 15 pre [RMSTEP](/docs/sk/keyword_documentation/r/rmstep/) sa bude objekt remešovať najmenej každých 15 krokov. To je užitočné, keď sa simulácia predčasne zastaví z dôvodu zápornej jacobovej chyby. Skôr ako sa sieť stane nepoužiteľnou, objekt sa môže remeshovať.

**Účel kritérií**

Keď ostrá hrana nástroja alebo matrice narazí na obrobok, môže dôjsť k hlbokému prieniku ostrej hrany do hrany prvku. Ak je táto hĺbka veľká, môže dôjsť k roztiahnutiu prvkov a opätovné zapracovanie môže byť ťažké. Pred dosiahnutím tejto hĺbky sa remeshing s umiestnením uzlov okolo hrany a umožní simulácii pokračovať bez prekážok.

****

## Rozšírené nastavenia

Na nasledujúcom Obr. 13.1.12. je zobrazené okno Rozšírené nastavenia.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image012.jpg' | relative_url }})

Okno pokročilých nastavení siete

**Rozlíšenie siete**(**MGGRID**)

Keď je objekt vynesený do 2D siete, na diskretizáciu hustoty siete v celej východiskovej geometrii je potrebná vzorkovacia sieť. Rozlíšenie mriežky ([MGGRID](/docs/sk/keyword_documentation/m/mggrid/)) určuje rozstupy vzorkovacích mriežok, ktoré sa používajú na vzorkovanie hustoty siete. Zvýšenie hodnoty delenia X alebo delenia Y bude mať za následok ostrejšie gradienty medzi oblasťami s rôznou hustotou siete. V prípade zaslepenia, keď sa vyžaduje veľmi vysoký gradient siete v úzkej oblasti, môže byť potrebné tieto hodnoty zvýšiť, aby sa zachytili veľké zmeny gradientu siete na krátkych vzdialenostiach.

**Parametre pridávania uzlov** (**MGERR**)
Parametre pridávania uzlov ([MGERR](/docs/sk/keyword_documentation/m/mgerr/)) určujú maximálnu povolenú chybu vzdialenosti a uhla medzi hranicou objektu a jeho pridruženou stranou prvku mriežky. Tolerancie vzdialenosti a uhla sa používajú na zachytenie kritickej geometrie hraníc, ktorá by sa inak mohla stratiť pri generovaní siete. Ak sa vyžaduje, aby objekt zachytil veľmi malé prvky, maximálna vzdialenosť sa môže znížiť, alebo ak je potrebné umiestniť uzol na malom uhle, môže sa znížiť aj chyba uhla. Len zriedkakedy bude musieť používateľ tieto hodnoty meniť. V prípade dielov, ktoré sú veľmi malé, je hodnota 0,01 % ohraničenia objektu dobrým východiskovým číslom, ktoré možno použiť pre [MGERR](/docs/sk/keyword_documentation/m/mgerr/) na lepšiu manipuláciu s rozlíšením siete.

## Sieť definovaná používateľom

Nastavenia siete definované používateľom umožňujú používateľovi určiť, aby určité oblasti na objekte mali vyššiu hustotu prvkov v porovnaní s inými oblasťami objektu len počas počiatočného generovania povrchovej siete (na túto špecifikáciu hustoty sa neodkazuje počas automatického obnovovania siete).

Keď je zvolená hustota siete definovaná používateľom, hodnoty hustoty sa nastavujú prostredníctvom okna zobrazenia. Výberom hustoty siete definovanej používateľom sa aktivuje tlačidlo definície relatívnej hustoty siete. Po kliknutí na toto tlačidlo sa používateľovi zobrazí okno Display Window (Okno zobrazenia), prostredníctvom ktorého je možné nastaviť hustoty siete. Hodnota hustoty sa používa na určenie váhy, ktorá sa má priradiť oblasti. Všimnite si, že skutočné číslo má význam len vo vzťahu k inému bodu hustoty. Napríklad bod s váhou 4 bude mať sieť dvakrát hustejšiu ako bod s váhou 2. Možno si tiež vybrať medzi nastavením hodnôt hustoty ako hraničných alebo vnútorných bodov. Ak sa urobí chyba, funkcia Delete (Odstrániť) vymaže aktuálny bod (zobrazený červenou farbou) a funkcia Delete All (Odstrániť všetko) vymaže všetky nastavené hodnoty hustoty. (Pozri obr. 13.1.13.)

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image013.jpg' | relative_url }})

Okno definované používateľom pre 2D

**Hustota hraníc**
Špecifikácia hraničnej hustoty sa používa na umiestnenie hodnoty hustoty na hranicu objektu. Zadajte požadovanú hustotu do poľa Hustota v okne Zobrazenie. Teraz vyberte tlačidlo Pridať body a kliknite na hranicu objektu. Teraz by sa mal zobraziť zelený bod s hodnotou hustoty zobrazenou vedľa neho. Ak chcete hodnotu odstrániť, vyberte tlačidlo Delete Points (Odstrániť body) a kliknite na bod, ktorý chcete odstrániť.

**Vnútorná hustota**
Špecifikácia vnútornej hustoty sa používa na nastavenie hodnoty hustoty pre sieť vnútri hranice objektu. Stačí kliknúť na tlačidlo Špecifikácia vnútornej hustoty a zadať požadovanú hodnotu hustoty. Teraz kliknite na tlačidlo Add Points (Pridať body) a kliknutím vo vnútri objektu umiestnite hodnoty hustoty. Mal by sa objaviť žltý bod s hodnotou hustoty vedľa neho. Ak chcete odstrániť vnútorné hustoty, kliknite na tlačidlo Odstrániť body a vyberte body, ktoré chcete odstrániť.

**Súvisiace témy:**

[13\. Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/)

[13.2. 3D Tet Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/)

[13.3. 3D Brick Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/)
