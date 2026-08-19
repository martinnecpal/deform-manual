---
lang: sk
title: "36.1. 2D Heat Transfer Express"
---

# 36.1. 2D Heat Transfer Express

36.1.1. Ako pridať operáciu „2D Heat Transfer Express“

36.1.2. Definícia nastavení procesu

36.1.3. Nastavenie režimu kúrenia

  * Objekt – základná definícia

  * Definícia geometrie objektu

  * Definícia sieťového modelu objektu

  * Definícia materiálu

  * Definícia okrajových podmienok

  * Definícia teplotných podmienok

  * Definícia ovládacích prvkov na zastavenie

  * Definícia ovládacích prvkov simulácie

  * Vytvoriť databázu

36.1.4. Definícia prevodovej operácie

  * Výber objektov

  * Umiestňovanie objektov a vytváranie vzťahov medzi objektmi

  * Definícia tepelného stavu

36.1.5. Definovanie operácie „Odpočinok na kocke“

  * Definovať tepelné výpočty

  * Výber objektov

  * Polohovanie

  * Plánovanie umiestnenia

  * Generovanie kontaktov medzi objektmi

  * Definícia teplotných podmienok

36.1.6. Pokračovanie v definovaní tvárniacich operácií

36.1.7. Definovanie operácie „Dwell on die“

  * Definícia teplotných podmienok

## Ako pridať operáciu „2D Heat Transfer Express“

Operácia „Heat Transfer Express“ je dostupná cez sprievodcu MO Wizard, ktorý je možné otvoriť z hlavného grafického rozhrania. Operáciu „Heat Transfer Express“ je možné pridať v sprievodcovi MO Wizard na karte „Explorer“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky „2D Heat Transfer Express“. Používateľ ju môže pridať aj pomocou funkcie drag and drop do editora operácií, ako je znázornené na obr. 36.1.1. Operáciu Heat Transfer Express je možné pridať aj interaktívne po operáciách prenosu tepla po simulácii predchádzajúcich operácií alebo v dávkovom/naplánovanom režime.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image001.jpg' | relative_url }})

Do editora operácií bola pridaná operácia „2D Heat Transfer Express“

## Definícia nastavení procesu

V okne „Process“ je potrebné pre operáciu prenosu tepla nastaviť simulačné režimy, ako sú „Geometry Type“, „Heating Type“, „Shape Complexity“ a „Accuracy“, ako je znázornené na obr. 36.1.1.

**Typ geometrie**

V nástroji Forming je možné nastaviť iba dva geometrické modely, a to „Axisymmetric“ a „Plane Strain“.

Axisymetrické modely predstavujú priečny rez vzhľadom na stredovú os. Model preto vyžaduje, aby deformujúca sa geometria bola osovo symetrická a nachádzala sa v prvom a štvrtom kvadrante (t. j. X > 0). Systém navyše predpokladá, že prúdenie v každej radiálnej rovine je identické. (Pozri [Fig. 9.1.2.](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Fig._9.1.2._Example_for_types_of_geometry_model))

Pri rovinnom deformovaní sa predpokladá, že geometria má jednotkovú hĺbku a že predná aj zadná plocha sú fixované. Simulácia vychádza z predpokladu, že objekty sa budú správať rovnako v akomkoľvek priereze naprieč šírkou a výškou objektu. (Pozri [Fig. 9.1.2.](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Fig._9.1.2._Example_for_types_of_geometry_model))

Ďalšie typy geometrie – „Rovinné napätie“ a „Krútenie“ – sú k dispozícii iba v rámci 2D operácie tvárnenia. Ďalšie informácie o týchto typoch geometrie nájdete v [9.1.2. Geometry type (GEOTYP](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\]).

  
**Typ vykurovania**

V režime Heat Transfer Express sú v 2D aj 3D k dispozícii štyri typy ohrevu alebo procesov prenosu tepla, a to (pozri obr. 36.1.1.):

  * Kúrenie

  * Prevod

  * Odpočinok na kocke a

  * Doba zdržania na čipe

Ohrievanie obrobku, prenos tepla pri presúvaní obrobku z pece do lisu, odloženie obrobku na formu (pred tvárnením) a zotrvanie obrobku na forme po tvárnení je možné jednoducho nastaviť pomocou príslušného typu ohrevu. Podrobnejšie informácie o týchto typoch ohrevu sú uvedené v dokumente [36\. Introduction to Heat transfer express operation](/docs/en/operation_templates/36_heat_transfer_express/36_introduction_to_heat_transfer_express_operations/), pozri časť „Typy ohrevu“.

V režimoch „Odpočinok“ a „Prevádzka“ sa aktivuje okno pre tepelný výpočet, ktoré ponúka možnosti výberu, či sa má počítať prenos tepla cez matrice, alebo nie. Tieto možnosti budú podrobnejšie vysvetlené v popisoch príslušných režimov.

**Zložitosť tvaru a presnosť**

Posuvníky pre zložitosť tvaru a presnosť simulácie (pozri obr. 36.1.1.) ovplyvňujú nastavenia siete a počet časových krokov použitých v simulácii. To zase ovplyvňuje dĺžku behu a úroveň detailov dostupnú v simulácii.

**Zložitosť tvaru:**

  * **Jednoduché**: Geometria objektov je svojou povahou jednoduchá. Vyžadujú si minimálny počet prvkov, ich riešenie je jednoduchšie a trvá kratšie.

  * **Stredná**: Geometria objektov je stredne zložitá (nie príliš zložitá).

  * **Zložité**: Geometria objektov má zložitý charakter.

**Presnosť tvaru:**

  * **Rýchly**: Vhodný na rýchle vyhodnotenie procesu. Výmenou za rýchlejšie časy spustenia však existuje vyššie riziko, že sa prehliadnu dôležité detaily.

  * **Stredná**: Simulácia používa nastavenia, ktoré sa snažia dosiahnuť rovnováhu medzi výpočtovým časom a presnosťou.

  * **Presné**: Vykonáva sa veľmi podrobná analýza procesu, ktorá zvyčajne zachytí aj tie najmenšie detaily. Čas potrebný na výpočet a požiadavky na úložný priestor sú vyššie.

## Definícia režimu kúrenia

Pri prevádzke v režime ohrevu alebo v režime pece sa modeluje ohrev sochory v peci. Po výbere nastavení procesu systém zobrazí prispôsobené okná pre operáciu ohrevu, ktoré používateľa prevedú nastavením tejto operácie. Pre túto operáciu je povolený len jeden objekt (pozri obr. 36.1.2.) a tento objekt sa pridá automaticky. Pridajú sa predvolené nastavenia procesu vhodné pre operáciu ohrevu.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image002.jpg' | relative_url }})

Okno na definovanie objektu vykurovacieho režimu

### Základná definícia objektu

Základná definícia objektu zahŕňa názov objektu, typ a teplotu. Okrem toho je možné pomocou tlačidla „Advanced“ inicializovať hodnoty premenných stavu objektu a údaje o objekte, ako sú geometria, sieť, okrajové podmienky a materiál, je možné importovať zo súboru DEFORM .DB /.Key. (Pozri obr. 36.1.3.)

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image003.jpg' | relative_url }})

Okno obrobku

**Názov objektu**: Používateľ môže definovať názov všetkých objektov dostupných v danej operácii.

**Typ objektu**: Typ objektu (OBJTYP) určuje, či a ako sa modeluje deformácia pre každý jednotlivý objekt v úlohe typu DEFORM. V operácii Forming Express sú k dispozícii len dva typy objektov, a to plastický a tuhý, ktoré sú automaticky preddefinované podľa čísla objektu, takže obrobok bude plastický a formy budú tuhé. V operácii Forming je k dispozícii viac typov objektov, podrobnosti nájdete v [11.4. Object Type](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type).

  
**Plast**: Plastové objekty sa modelujú ako tuho-plastický alebo tuho-viskoplastický materiál v závislosti od vlastností materiálov. Model predpokladá, že napätie v materiáli lineárne rastie s rýchlosťou deformácie až do prahovej hodnoty rýchlosti deformácie, označovanej ako limitná rýchlosť deformácie ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)). Po prekročení medznej rýchlosti deformácie sa materiál deformuje plasticky. Plastické správanie materiálu objektu sa špecifikuje pomocou funkcie tokového napätia materiálu alebo údajov o tokovom napätí ([FSTRES](/docs/en/keyword_documentation/f/fstres/)). V programe Heat Transfer Express sa obrobok automaticky priradí k typu objektu „Plast“.  
**Tuhé**: Tuhé objekty sa modelujú ako nedeformovateľné materiály. V analýze deformácie je objekt reprezentovaný geometrickým profilom ([DIEGEO](/docs/en/keyword_documentation/d/diegeo/)). Údaje o riešení deformácie dostupné pre tuhé objekty zahŕňajú zdvih objektu, zaťaženie a rýchlosť. Sieť pre tuhý objekt sa používa iba na výpočty tepelného prenosu, transformácie a difúzie. V programe Heat Transfer Express sú lisovacie formy alebo nástroje automaticky priradené k kategórii „Tuhé“, keďže ide o nedeformovateľné objekty.

**Poznámka:**

Je potrebné poznamenať, že typ objektu je v operácii programu Heat Transfer Express preddefinovaný číslom objektu. Prvý objekt bude z plastu a pri ďalšom pridávaní sa budú pridávať iba tuhé objekty.  
Na stránke „Objekt“ sa nachádza tlačidlo „Importovať objekt“. Slúži na import kompletných údajov o objekte z iného súboru DEFORM.

**Teplota objektu**: Používateľ môže nastaviť teplotu objektu v poli „Teplota“ v príslušnom okne objektu, ako je znázornené na obr. 36.1.3.

Pokročilé nastavenia objektu: Pokročilé nastavenia v časti „Možnosti inicializácie“ (pozri obr. 36.1.4.) sa zídu v prípade, ak používateľ importuje objekt z predtým spusteného projektu alebo úlohy, alebo ak sa operácia „express“ pridá až po niekoľkých iných operáciách a je potrebné inicializovať niekoľko dôležitých stavových premenných.

  
Pomocou pokročilých nastavení môže používateľ zadať teplotu, deformáciu, rýchlosť, poškodenie a posun, ku ktorým došlo v deformovateľnom objekte. (Pozri obr. 36.1.4.)

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image004.jpg' | relative_url }})

Pokročilé nastavenia objektov

V operácii „Forming“ je možné inicializovať ďalšie premenné; podrobnosti nájdete v operácii [35\. 2D Heat Transfer](/docs/en/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/) a [Initialize](../35_heat_transfer/35_1_2d_heat_transfer_operation.htm#Initialize).

Priemerná rýchlosť deformácie ([AVGSTR](/docs/en/keyword_documentation/a/avgstr/)) je charakteristická priemerná hodnota efektívnej rýchlosti deformácie. Na začiatku simulácie by sa mala zadať aproximácia tejto hodnoty.

Medzná rýchlosť deformácie ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)) definuje medznú hodnotu efektívnej rýchlosti deformácie, pod ktorou sa plastický alebo porézny materiál považuje za tuhý a správa sa ako materiál s newtonovskými vlastnosťami.

![]({{ '/assets/icons/pre_icons/mo_reset_button.jpg' | relative_url }}): Pomocou tejto funkcie môže používateľ obnoviť hodnoty premenných v počiatočnom stave.

Ďalšie možnosti vlastností objektu deformácie, ktoré sú k dispozícii v operácii tvarovania, nájdete v [16.1. Deformation Properties.](/docs/en/pre_processor/16_object_properties/16_1_deformation_properties/)

### **Definícia geometrie objektu**

Okno „Geometria“ slúži na vytvorenie geometrie objektu, ako je znázornené na obr. 36.1.5. Pred vytvorením geometrie sú k dispozícii iba možnosti „Definovať primitív“ a „Upraviť geometriu“, avšak po vytvorení geometrie sa aktivujú možnosti „Skontrolovať“, „Zmenšiť“ a „Obrátiť geometriu“ a po vygenerovaní siete sa aktivuje možnosť „Extrahovať okraj“.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image005.jpg' | relative_url }})

Okno s definíciou geometrie

**Definovať primitív ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }})**

  * **Pre osovo symetrický typ**: Na stránke s geometrickými primitívami je k dispozícii päť základných tvarov, ktoré možno použiť na vytvorenie geometrií, ako je znázornené na obr. 36.1.6. V každom prípade musí používateľ prispôsobiť rozmery tak, aby zodpovedali danej úlohe.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image011.jpg' | relative_url }})

Okno s geometrickými primitívami pre typ geometrie „Osovo symetrická“

  * **Pre typ rovinného deformovania**: Na stránke geometrických primitív sa nachádzajú tri základné tvary, ktoré možno použiť na vytvorenie geometrií, ako je znázornené na obr. 36.1.7. V každom prípade musí používateľ prispôsobiť rozmery tak, aby zodpovedali danej úlohe.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image012.jpg' | relative_url }})

Okno s geometrickými primitívami pre typ geometrie „Rovinné deformácie“

**Skontrolujte**![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})

Po vytvorení geometrie objektu sa aktivuje tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Je potrebné skontrolovať orientáciu geometrie. To je možné urobiť kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Zobrazí sa okno „Skontrolujte a opravte geometriu“, ako je znázornené na obr. 36.1.8 nižšie. Geometria sa opraví, ak obsahuje nejaké chyby, po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}). Po oprave geometrie alebo ak geometria neobsahuje žiadne chyby, zobrazí sa správa „Geometria je správna“ a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Ďalšie informácie nájdete v časti [12.1. 2D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/) [Check Geometry](../../pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining.htm#Check_Geometry). 

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image006.jpg' | relative_url }})

Okno „Skontroluj a oprav geometriu“

**Veľkosť**![]({{ '/assets/icons/pre_icons/mo_scale_label.jpg' | relative_url }})

Geometriu je možné pri tvárnení zmeniť tak, aby zohľadňovala teplotnú rozťažnosť, a to stanovením zväčšovacieho koeficientu. (Pozri obr. 36.1.9.) Zväčšovací koeficient je možné vypočítať na základe teplotného rozdielu a údajov o materiáli závislých od teploty. Upravenú geometriu je možné uložiť v rôznych formátoch na ukladanie geometrie.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image014.jpg' | relative_url }})

Okno „Scale Geo“

**Reverse![]({{ '/assets/icons/pre_icons/mo_reverse_label.jpg' | relative_url }})**

Táto funkcia obráti orientáciu geometrie. Pri geometrii s jedným okruhom musí byť orientácia 2D geometrie vždy smerom dovnútra; pri geometrii s viacerými okruhmi môže mať okruh, ktorý sa nachádza v oboch oblastiach, orientáciu na ktorúkoľvek stranu, avšak topológia musí byť definovaná.

**Výňatok Border![]({{ '/assets/icons/pre_icons/mo_extract_border_button.jpg' | relative_url }})**

Táto funkcia extrahuje geometrické údaje z aktuálneho objektu s mriežkou v databáze pre všetky typy objektov s výnimkou tuhého objektu.

**Edit![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) **

Možnosť „Editácia geometrie“ slúži na vytvorenie geometrie objektu alebo na úpravu existujúcej geometrie. Importovanú geometriu je možné upravovať v okne „Editácia geometrie“. Na stránke „Geometria“ kliknite na označenie ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a prezrite si dostupné možnosti na vytvorenie a úpravu geometrie, ako je znázornené na obr. 36.1.10.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image007.jpg' | relative_url }})

Okno „Upraviť geometriu“

Geometriu je možné vytvoriť pomocou nástroja na vytváranie slučiek alebo zadaním súradníc geometrie do tabuľky editora geometrie v pravom dolnom rohu okna, ako je znázornené na obr. 36.1.10, a to buď v režime XYR, alebo v režime Čiara-oblouk. Podrobnejšie informácie o 2D editore geometrie nájdete v kapitole [12.2. 2D Geometry Data Editing](/docs/en/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/).

**Ďalšie možnosti geometrie:**

**Zobraziť geometriu vnútri značky:** Zaškrtnutím tejto možnosti sa aktivuje zobrazenie orientácie geometrie.

**Určiť referenčný bod**: Používateľ môže vybrať referenčný bod geometrie kliknutím na toto tlačidlo v okne zobrazenia. Tento referenčný bod je potrebný na určenie vzdialenosti medzi objektmi pomocou ovládacích prvkov na zastavenie.

**Import geometrie zo súboru** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}): Importuje geometriu zo súboru  
**Načítať geometriu z knižnice** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}): Importuje geometriu z knižnice  
**Uloženie geometrie do súboru** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) : Uloží geometriu do súboru.  
**Uložiť geometriu do knižnice** ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ uložiť geometriu do knižnice.  
**Odstrániť geometriu** ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}): používateľ môže odstrániť geometriu.

### Definícia objektovej siete

Okno „Vytvorenie siete“ umožňuje používateľovi vytvoriť sieť pre aktuálny objekt. Na obr. 36.1.11. je zobrazené okno „Vytvorenie siete“ v systémovom režime. V tomto režime systém automaticky nastaví počet prvkov siete na základe zložitosti tvaru a výberu nastavenia presnosti v pracovnom okne.

**Systém****Režim**: Pri použití ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) musí používateľ vytvoriť sieť pre objekty a po vytvorení siete sa aktivuje tlačidlo **![]({{ '/assets/icons/pre_icons/mo_delete_button.jpg' | relative_url }})** „Mesh“, ktoré slúži na odstránenie aktuálnej siete objektu.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image008.jpg' | relative_url }})

Okno nastavení siete v režime Systém

**Režim definovaný používateľom**: Možnosť režimu siete definovaného používateľom je znázornená na obr. 36.1.12. V tomto režime môže používateľ meniť počet prvkov pomocou posuvníka a využívať pokročilé možnosti na úpravu pomeru veľkostí, hrúbky prvkov, váhového faktora a kritérií pregenerovania siete.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image009.jpg' | relative_url }})

Nastavenia siete v užívateľsky definovanom režime

**Počet prvkov (MGNELM)**

Počet prvkov siete predstavuje približný počet prvkov, ktoré systém vygeneruje. Automatický generátor siete (AMG) použije hodnotu pre [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) a vygeneruje sieť, ktorá bude obsahovať približne rovnaký počet prvkov.

Chyba medzi počtom zadaných prvkov a počtom vygenerovaných prvkov sa zvyčajne pohybuje okolo desiatich percent. Pri generovaní siete sa na určenie hustoty siete používa zadaný celkový počet prvkov v kombinácii s ovládacími prvkami „Bod“ a „Parameter“.

**Pokročilé nastavenia siete**

**Všeobecné nastavenia**

Okrem počtu prvkov môže používateľ zvoliť aj hrúbku prvkov a hodnoty pomeru veľkostí, aby dosiahol požadovanú sieť.

  * **Počet prvkov hrúbky (MGTELM)**

Pomer maximálnej hrúbky je jedným z viacerých spôsobov, ako regulovať hustotu siete počas automatického generovania siete (AMG). Počet prvkov v smere hrúbky predstavuje približný počet prvkov, ktoré systém vygeneruje v smere hrúbky v akejkoľvek oblasti dielu. Automatický generátor siete (AMG) použije hodnotu pre [MGTELM](/docs/en/keyword_documentation/m/mgtelm/) a vygeneruje sieť, ktorá bude mať tento počet prvkov v najtenšej časti. Napríklad, ak je [MGTELM](/docs/en/keyword_documentation/m/mgtelm/) nastavené na 4, AMG sa pokúsi vytvoriť 4 prvky v smere hrúbky geometrie.

Smer hrúbky objektu je kolmý na os rozvetvenej stredovej čiary pre každú oblasť dielu. Celkový počet prvkov, ktoré sa majú vygenerovať v sieti, sa riadi hodnotou počtu prvkov v kľúčovom slove [MGNELM](/docs/en/keyword_documentation/m/mgnelm/). Ak hodnota prvkov hrúbky vedie k sieti, ktorá obsahuje viac prvkov, ako je hodnota špecifikovaná v [MGNELM](/docs/en/keyword_documentation/m/mgnelm/), hodnota [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) sa zníži tak, aby sieť obsahovala približne [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) prvkov. Ak hodnota [MGTELM](/docs/en/keyword_documentation/m/mgtelm/) vedie k sieti, ktorá obsahuje menej ako [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) prvkov, zostávajúce prvky budú rozdelené medzi ostatné užívateľom špecifikované parametre hustoty siete (krivost, deformácia, rýchlosť deformácie a teplota).

  * **Pomer veľkostí prvkov (MGSIZR)**

Maximálny pomer veľkostí medzi prvkami je jedným z viacerých spôsobov, ako regulovať hustotu siete počas automatického vytvárania siete (AMG) prostredníctvom zadania pomeru hustôt uzlov.

Pri hodnote 3 pre [MGSIZR](/docs/en/keyword_documentation/m/mgsizr/) bude najväčšia hrana prvku na objekte približne trojnásobkom veľkosti najmenšej hrany prvku na tom istom objekte. Ak sa požadujú prvky rovnakej veľkosti, pomer veľkostí je 1. Ak je pomer veľkostí 0, pomer veľkostí prvkov nebude mať vplyv na rozloženie hustoty siete.

**Faktory, ktoré sa zohľadňujú**

Váhovacie faktory alebo parametre (systémom definovaná hustota siete) pre zakrivenie hranice, teplotu, deformáciu a rýchlosť deformácie určujú relatívne váhy hustoty siete, ktoré sa majú priradiť k príslušnému parametru. (Pozri obr. 36.1.13.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image018.jpg' | relative_url }})

Okno nastavení váhových koeficientov

Hustoty teploty, deformácie a rýchlosti deformácie sa prideľujú na základe gradientov týchto parametrov, nie na základe ich absolútnych hodnôt. To znamená, že oblasť s rýchlou zmenou teploty v určitom smere bude obsahovať viac prvkov ako oblasť s rovnomernou vysokou teplotou.

Hodnoty zo všetkých kľúčových slov týkajúcich sa hustoty siete sa počas procesu generovania siete kombinujú, čím sa vytvorí rozloženie hustoty siete v rámci geometrických hraníc. 

Operácia tvarovania obsahuje ďalší váhový faktor, a to možnosti v okne „Mesh Density“ (Hustota siete), pomocou ktorých môže používateľ definovať konkrétnu oblasť v priestore, ktorá sa bude počas deformácie pohybovať spolu s ostatnými objektmi s príslušnou hustotou siete. Pozrite si [13.1.5. Mesh Weighting factors.](../../pre_processor/13_mesh_generation/13_1_2d_mesh_generation.htm#13.1.5._Mesh_weighting_factors).

**Kritériá pre generovanie novej siete**

Kritériá pregenerovania siete (Autoremesh) predstavujú najpohodlnejší spôsob, ako riešiť pregenerovanie siete objektov, ktoré podliehajú veľkej plastickej deformácii, preto sa to v prípade výpočtov prenosu tepla nedá použiť.

**Pokročilé nastavenia**

Na obr. 36.1.14. je zobrazené okno „Pokročilé nastavenia“.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image020.jpg' | relative_url }})

Okno s pokročilými nastaveniami siete

  * **Rozlíšenie mriežky (MGGRID)**

Pri vytváraní 2D siete objektu je potrebná vzorkovacia mriežka na diskretizáciu hustoty siete v celej počiatočnej geometrii. Rozlíšenie mriežky (MGGRID) určuje rozstup vzorkovacích mriežok, ktoré sa používajú na vzorkovanie hustôt siete. Zvýšenie hodnoty X division alebo Y division bude mať za následok ostrejšie prechody medzi oblasťami s odlišnou hustotou siete. V prípade vyrezávania, kde je potrebný veľmi vysoký gradient siete v úzkej oblasti, môže byť potrebné tieto hodnoty zvýšiť, aby sa zachytili veľké zmeny gradientu siete na krátkych vzdialenostiach.

  * **Parametre pridávania uzlov (MGERR)**

Parametre pridávania uzlov (MGERR) určujú maximálnu povolenú vzdialenosť a uhlovú chybu medzi hranicou objektu a stranou príslušného prvku mriežky. Tolerancie vzdialenosti a uhla sa používajú na zachytenie kritickej geometrie hraníc, ktorá by inak mohla byť stratená pri generovaní siete. Ak sa od objektu vyžaduje zachytenie veľmi malých detailov, maximálnu vzdialenosť je možné znížiť, alebo ak je potrebné umiestniť uzol pod malým uhlom, je možné znížiť aj uhlovú chybu. Používateľ bude musieť tieto hodnoty meniť len zriedka. Pre veľmi malé diely je hodnota 0,01 % ohraničujúceho obdĺžnika objektu dobrým východiskovým číslom, ktoré možno použiť pre MGERR na lepšie zvládnutie rozlíšenia siete.

**Skontrolujte Mesh![]({{ '/assets/icons/pre_icons/mo_check_mesh_button.jpg' | relative_url }}) **

Sieť je možné skontrolovať z hľadiska prípadných problémov pomocou funkcie „Check Mesh“. Ak je sieť bezchybná, po kliknutí na možnosť „Check Mesh“ sa zobrazí okno znázornené na obr. 36.1.15. 

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image003.jpg' | relative_url }})

Skontrolujte vyskakovacie okno so sieťou

**Odstrániť sieť** ![]({{ '/assets/icons/pre_icons/mo_delete_mesh_button.jpg' | relative_url }})

Odstráni sieť vytvorenú pre daný objekt.

**Zobraziť sieť ![]({{ '/assets/icons/pre_icons/mo_show_mesh_button.jpg' | relative_url }}) **

Keď používateľ klikne na tlačidlo „Zobraziť sieť“, v okne zobrazenia sa zobrazí vygenerovaná sieť. Tlačidlo „Zobraziť sieť“ prepína medzi zobrazením siete a geometrie objektu.

**Predvolené nastavenie** ![]({{ '/assets/icons/pre_icons/mo_default_settings_button.jpg' | relative_url }})  
Keď používateľ klikne na kartu „Predvolené nastavenia“, všetky nastavenia sa zmenia na predvolené hodnoty. Okno „Mesh“ bude štandardne neaktívne, keďže nie sú definované žiadne okná typu „Mesh“. Ak chce používateľ aktivovať okno „Mesh“, musí zmeniť váhový faktor hustoty siete tak, že posuvník nastaví na hodnotu 1.

Ďalšie možnosti sietí sú k dispozícii v operáciách tvarovania a v predspracovateľovi – pozri [13.1. 2D Mesh Generation.](/docs/en/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/)

### Definícia materiálu

Na obr. 36.1.16. je zobrazené okno s materiálmi. Používateľ môže pridať alebo importovať materiál zo súboru kľúčových slov alebo ho načítať z knižnice materiálov DEFORM.

  
Po načítaní systém automaticky priradí načítaný materiál k objektu. Používateľ môže vlastnosti materiálu upravovať aj pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image010.jpg' | relative_url }})

Okno s materiálmi

Po pridaní materiálu kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) – otvorí sa okno s materiálom, ako je znázornené na obr. 36.1.17.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image022.jpg' | relative_url }})

Okno na úpravu materiálu

Požadované vlastnosti závisia od fyzikálnych javov simulovaných v programe DEFORM. Vlastnosti materiálu, ktoré musí používateľ zadať, závisia od typov materiálov, ktoré používateľ v simulácii využíva. V operácii „Tvarovanie“ má používateľ prístup ku všetkým vlastnostiam materiálu; ďalšie informácie nájdete v [10\. Material Data.](/docs/en/pre_processor/10_material_data/10_material_data/).

### Definícia okrajových podmienok

V okne „Okrajové podmienky“ v programe Heat Transfer Express môže používateľ pre objekt priradiť iba tepelnú výmenu s okolím a teplotné okrajové obmedzenia. Okrajové podmienky určujú, ako hranica objektu interaguje s inými objektmi a s okolím. Najčastejšie používanými okrajovými podmienkami sú tepelná výmena s okolím pri simuláciách zahŕňajúcich prenos tepla. Obr. 36.1.18. znázorňuje rôzne okrajové podmienky (BCC), ktoré je možné priradiť k objektu.

V predvolenom nastavení sa výmena tepla s okolím priradí ku všetkým povrchom s výnimkou symetrického povrchu (t. j. stredovej čiary) v osovo symetrickom modeli a k celému vonkajšiemu povrchu v modeli s rovinným deformovaním, ako je znázornené na obr. 36.1.18.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image011.jpg' | relative_url }})

Pre obrobok bola nastavená okrajová podmienka symetrie

Definované BCC je možné najskôr inicializovať výberom typu BCC v strome a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_button.jpg' | relative_url }}). Konkrétne definované BCC je možné tiež odstrániť výberom definovanej vetvy zo stromu BCC a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_bcc_button.jpg' | relative_url }}). Teplotu okolia je možné meniť v okne „Heat condition“ (Teplotné podmienky). Okná okolia nie sú povolené pre výmenu tepla s BCC okolia v režime prenosu tepla, sú však k dispozícii v režime tvárnenia; ďalšie podrobnosti nájdete v časti „Thermal“ (Tepelné vlastnosti) pod [14.3 Thermal Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/).

V predspracovateľovi a pri operácii tvarovania sú k dispozícii ďalšie možnosti tepelného BCC a rôzne kategórie BCC, ako napríklad [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/), [Thermal](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/), [Diffusion](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/) a [Heating](/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/). Ďalšie informácie o týchto BCC nájdete v [14\. Boundary Conditions.](../../pre_processor/14_boundary_conditions).

### Definícia tepelného stavu

V tomto okne je potrebné definovať tepelné podmienky, ako sú doba ohrevu (trvanie procesu), teplota okolia a konvekčný koeficient, ako je znázornené na obr. 36.1.19. Pre všetky typy ohrevu systém štandardne definuje podmienky ohrevu; na zmenu týchto predvolených nastavení je potrebné zadať údaje o nastaveniach procesu.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image012.jpg' | relative_url }})

Okno nastavení teplotných podmienok

### Definícia ovládacích prvkov na zastavenie

Iba v režime kúrenia poskytuje funkcia prenosu tepla ovládacie prvky na zastavenie simulácie, keď sa všetky uzly obrobku nachádzajú v stanovenom rozsahu stupňov od nastavenej teploty alebo teploty okolia, ako je znázornené v [Fig. 36.1.20.](). V [Fig. 36.1.20.]() sa simulácia zastaví, ak sú teploty všetkých uzlov v rozmedzí 1199,5 °C až 1200,5 °C.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image013.jpg' | relative_url }})

Okno na ovládanie vypnutia kúrenia

### Definícia ovládacích prvkov simulácie

Systém DEFORM rieši časovo závislé nelineárne úlohy generovaním série riešení metódou konečných prvkov (FEM) v diskrétnych časových krokoch. V každom časovom kroku sa na základe okrajových podmienok, termomechanických vlastností materiálov obrobku a prípadne riešení z predchádzajúcich krokov určujú rýchlosti, teploty a ďalšie kľúčové premenné každého uzla v sieti konečných prvkov. Ostatné stavové premenné sa odvodzujú z týchto kľúčových hodnôt a aktualizujú sa pri každom časovom kroku. Dĺžka tohto časového kroku a počet simulovaných krokov sa určujú na základe informácií zadaných v ponuke nastavení krokov. Obr. 36.1.21. znázorňuje možnosti ovládania simulácie.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image014.jpg' | relative_url }})

Okno ovládacích prvkov simulácie v definícii systému

Používateľ musí určiť čas na jeden krok (definícia kroku), celkový počet krokov a veľkosť kroku, ktoré sa majú uložiť v definícii kroku používateľa a systému. V programe Heat Transfer Express sú k dispozícii tri typy definícií krokov: systémová, používateľská a automatická.

Typ systému (pozri obr. 36.1.21.) – automatický výpočet definície kroku na základe zadaného času ohrevu a zvolených nastavení presnosti a zložitosti. V závislosti od rôznych nastavení presnosti a zložitosti systém upraví prvky siete objektu a veľkosť kroku zmenou počtu krokov. Ak používateľ potrebuje upraviť automaticky vypočítanú definíciu kroku, možnosť „Ručné zadanie“ umožňuje zmeniť definíciu kroku.

V rámci typu používateľa bude mať používateľ oprávnenie na úpravu definícií krokov podľa potreby, ako je znázornené na obr. 36.1.22.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image015.jpg' | relative_url }})

Ovládacie prvky pre definíciu krokov používateľa

Typ „Auto“ predstavuje krokové riadenie založené na teplote; nastavenia ([DTPMAX)](/docs/en/keyword_documentation/d/dtpmax/)) určujú dĺžku časového kroku. Účelom týchto nastavení je určiť dĺžku časového kroku simulácie, ktorá je riadená deformáciou vyvolanou teplotou. Používateľ musí zadať počiatočný časový krok (čas na krok), maximálnu zmenu teploty na krok, minimálny čas na krok a maximálny čas na krok, ako je znázornené na obr. 36.1.23.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image016.jpg' | relative_url }})

Pokročilé ovládacie prvky na definovanie krokov

**Zmena teploty na jeden krok**(([DTPMAX](/docs/en/keyword_documentation/d/dtpmax/))  
Maximálny prírastok zmeny teploty obmedzuje rozsah, o ktorý sa môže teplota ktoréhokoľvek uzla zmeniť počas jedného časového kroku. Ak je priradená hodnota odlišná od nuly, spustí sa nový podkrok, keď zmena teploty v ktoromkoľvek uzle dosiahne hodnotu ([DTPMAX](/docs/en/keyword_documentation/d/dtpmax/). Maximálny/minimálny časový krok predstavuje najväčší a najmenší časový krok povolený pri podkrokovaní založenom na teplote.

### Vytvoriť databázu

**Overiť údaje**![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})****

Systém skontroluje údaje. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvoriť databázu ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})**

Kliknutím na toto tlačidlo sa vytvorila databáza pre nastavenie. (Pozri obr. 36.1.24.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image050.jpg' | relative_url }})

Okno „Vytvoriť databázu“

## Definovanie operácie prenosu

Operácia „Prenos tepla“ sa používa na nastavenie konvekčného prúdenia vzduchu, zvyčajne počas presunu obrobku z pece do lisu. Používateľ môže túto operáciu pridať po operácii ohrevu alebo začať samotným prenosom tepla na ohriaty obrobok ako prvou operáciou. V operácii „Transfer“ bude používateľ vedený nastavovacími oknami rovnako ako v operácii „Heating“, s výnimkou ovládacích prvkov na zastavenie ohrevu, ako je znázornené na obr. 36.1.25. Podrobnosti o základnej definícii objektu, geometrii, sieti, materiáli a okrajových podmienkach nájdete v časti Definovanie operácie ohrevu. Okrem možností operácie ohrevu môže používateľ pridať viac ako jeden objekt, čím sa pridávajú možnosti polohovania objektov a definície vzťahov medzi objektmi. Tieto možnosti sú popísané v tejto časti.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image017.jpg' | relative_url }})

Po ohreve v peci pridať operáciu prenosu tepla

### Výber objektov

V operácii „Prenos tepla“ je povolené použiť viac ako jeden objekt. V závislosti od nastavenia procesu si môže používateľ v tomto okne vybrať počet objektov potrebných na vykonanie operácie (pozri obr. 36.1.26.). Používateľ musí mať na pamäti, že v simulácii môže byť len jeden plastový objekt. Je možné pridať maximálne 100 foriem.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image018.jpg' | relative_url }})

Nastavenia výberu objektov pri operácii presunu

### Umiestňovanie objektov a vytváranie vzťahov medzi objektmi

Ak používateľ vyberie viac ako jeden objekt, systém za objektmi pridá ovládacie prvky (polohovanie) a okná plánovaného polohovania a kontaktu, aby sa objekty správne umiestnili a aby sa v prípade potreby v nastavení vytvoril kontakt medzi objektmi. Ďalšie podrobnosti o týchto možnostiach nájdete v časti „Definovanie operácie odpočinku na matrici“ v kapitole „Polohovanie a plánované polohovanie“.

### Definícia pojmu „tepelné podmienky“

V tomto okne je potrebné definovať podmienky ohrevu, ako sú doba prenosu (trvanie procesu), teplota okolia a koeficient konvekcie, ako je znázornené na obr. 36.1.27. Pre všetky typy ohrevu systém štandardne definuje podmienky ohrevu; používateľ musí zadať údaje o nastaveniach procesu zmenou predvolených hodnôt.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image019.jpg' | relative_url }})

Teplotné podmienky pri prevádzke prenosu

Po nastavení teplotných podmienok musí používateľ definovať ovládacie prvky simulácie; podrobnosti o nastavení ovládacích prvkov simulácie nájdete v časti Definícia ovládacích prvkov simulácie.

  
Databáza sa musí vygenerovať v prípade interaktívneho nastavenia alebo ak je operácia prenosu prvou operáciou; v opačnom prípade sa databáza vygeneruje automaticky počas simulácie. Ďalšie informácie o ovládacích prvkoch simulácie a generovaní databázy nájdete v častiach „Definícia ovládacích prvkov simulácie“ a „Generovanie databázy“.

## Definícia operácie „Odpočinok na kocke“

Operácia „Odpočinok na forme“ alebo „Odpočinok“ slúži na nastavenie prenosu tepla z horúceho obrobku do okolia a do formy, na ktorej leží pred tvarovaním. Používateľ môže túto operáciu pridať po operácii prenosu tepla alebo môže začať priamo operáciou odpočinku zahriateho obrobku ako prvou operáciou. V operácii odpočinku bude používateľ vedený nastavovacími oknami rovnako ako v operácii ohrevu, s výnimkou ovládacích prvkov na zastavenie ohrevu, ako je znázornené na obr. 36.1.28. Okrem možností operácie ohrevu môže používateľ pridať viac ako jeden objekt, čím sa pridávajú možnosti tepelného výpočtu, polohovania objektov a definície vzťahov medzi objektmi. Tieto možnosti sú rozoberané v tejto časti.

Systém štandardne pridá dva objekty čipov a voľba pre výpočet tepelného správania sa zobrazí za oknom procesu, ako je znázornené na obr. 36.1.28.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image020.jpg' | relative_url }})

Pridanie operácie odpočinku po operácii prenosu tepla

### Definícia tepelných výpočtov

Okno „Výpočet teploty“ (pozri obr. 36.1.29.) ponúka možnosti v sekcii „Neizotermické“, kde je možné zvoliť výpočet teploty iba v obrobku alebo v obrobku aj v lisovacích formách.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image021.jpg' | relative_url }})

Okno na výber typu výpočtu teploty

**Neizotermický**: Proces, pri ktorom teplota systému nie je konštantná. Zahrnutie výpočtov teploty zlepší predpovede toku materiálu a predpovede zaťaženia, najmä v procesoch, kde dochádza k výrazným zmenám teploty. Výpočet teploty v nástrojoch ďalej zlepšuje výpočet teploty obrobku, pretože zmena teploty nástroja ovplyvňuje únik tepla z obrobku.

### Výber objektov

V tomto okne si môže používateľ v závislosti od nastavenia procesu vybrať počet objektov potrebných na vykonanie operácie (pozri obr. 36.1.30.). Používateľ musí mať na pamäti, že v simulácii môže byť len jeden plastový objekt. Je možné pridať maximálne 100 foriem.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image022.jpg' | relative_url }})

Okno na výber objektov

Podrobnosti o základnej definícii objektu, geometrii, sieti, materiáli a okrajových podmienkach nájdete v kapitole 36.1.3. Definovanie operácie ohrevu.

### Polohovanie

Ak sa objekty nečítajú z databázy, ako je znázornené na obr. 36.1.31, musí používateľ kliknúť na tlačidlo „Umiestniť objekty“, aby objekty umiestnil podľa požiadaviek nastavenia. Ďalšie informácie o možnostiach umiestňovania nájdete v [19.Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/). Ak sa objekty čítajú z databázy, ich umiestňovanie musí byť naplánované.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image023.jpg' | relative_url }})

Nastavenia okna „Positioning Objects“ pre typ „Read from DB“ a ďalšie typy objektov

### Plánovanie polohy

Ak si používateľ nie je istý polohou objektu, ako je to v prípade objektov typu „Read From DB“, naplánované umiestňovanie pomôže objekty presne umiestniť.

Funkcia „Schedule positioning“ umožňuje používateľovi definovať umiestnenie objektov v nastavení MO pre nasledujúce operácie, pre ktoré sa nevytvára databáza (DB), tak, aby sa objekty umiestnili ešte pred vytvorením databázy počas spustenia simulácie v dávkovom režime. (Pozri [Fig. 36.1.32.]())

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image024.jpg' | relative_url }})

V rozvrhu umiestnite objekty do po sebe nasledujúcich operácií

### Generovanie kontaktov medzi objektmi

Účelom vzťahov medzi objektmi je definovať, ako rôzne objekty v simulácii vzájomne interagujú. Všetky objekty, ktoré sa v priebehu simulácie môžu navzájom dotýkať, musia mať definovaný kontaktný vzťah. V systéme Heat Transfer Express sa automaticky definuje vzťah medzi obrobkom a formami a vlastný kontakt pre obrobok, potom sa vygeneruje kontakt, keď používateľ klikne na tlačidlo, ako je znázornené na obr. 36.1.33. Správa o vygenerovaných kontaktoch sa zobrazí na karte Správy pod grafickým oknom.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image025.jpg' | relative_url }})

Nastavenia okna na generovanie kontaktov medzi objektmi v dávkovom režime

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image026.jpg' | relative_url }})

Nastavenia okna na generovanie kontaktov medzi objektmi v interaktívnom režime (alebo pri prvom spustení)

V prípade, že expresný výpočet prenosu tepla prebieha postupne, systém v dávkovom režime naplánuje definovanie a generovanie kontaktov tak, že počas behu inicializuje predchádzajúce kontakty; preto nie je možné generovať a inicializovať kontaktné uzly ani obnoviť nastavenia siete, ako je znázornené na obr. 36.1.34. Používateľ môže zvoliť hodnotu tolerancie pre generovanie kontaktov výberom prepínača „Definované používateľom“.

  
Hodnotu koeficientu prenosu tepla vedením si môže užívateľ nastaviť sám; systém zároveň ponúka aj typické hodnoty, a to (pozri obr. 36.1.33.)  
(1 N/s/mm/°C alebo 0,0003 Btu/s/in²/°F) pre stav voľného pokoja  
(1 N/s/mm/°C alebo 0,0003 Btu/s/in²/°F) pre obytné priestory  
(11 N/s/mm/°C alebo 0,004 Btu/s/in²/°F) pri tvárnení

### Definícia tepelného stavu

V tomto okne je potrebné definovať tepelné podmienky, ako sú doba odpočinku (trvanie procesu), teplota okolia a konvekčný koeficient, ako je znázornené na obr. 36.1.35. Pre všetky typy ohrevu systém štandardne definuje podmienky ohrevu; používateľ musí zadať údaje o nastaveniach procesu zmenou predvolených hodnôt.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image027.jpg' | relative_url }})

Okno nastavení teplotných podmienok

Po nastavení teplotných podmienok musí používateľ definovať ovládacie prvky simulácie; podrobnosti o nastavení ovládacích prvkov simulácie nájdete v časti Definícia ovládacích prvkov simulácie.

  
Databáza „Next“ sa musí vygenerovať v prípade interaktívneho nastavenia alebo ak ide o prvú operáciu prenosu; v opačnom prípade sa databáza vygeneruje automaticky počas simulácie. Ďalšie informácie o ovládacích prvkoch simulácie a generovaní databázy nájdete v článkoch „Simulation_controls_Definition“ a „Generate Database“.

## Pokračovanie v definovaní tvárniacich operácií

Po operáciách rýchleho prenosu tepla môže používateľ pridať operácie tvárnenia (pozri obr. 36.1.36.) a pokračovať v nastavení neizotermickej deformácie. Operácie prenosu tepla je možné pridať aj medzi operácie tvárnenia, najmä po operácii tvárnenia s prispôsobeným typom ohrevu „Heat Dwelling“, ktorý je k dispozícii pre simuláciu zdržania a je vysvetlený v nasledujúcej časti 36.1.7. Definovanie operácie zdržania na matrici. Ďalšie informácie o nastavení operácií tvárnenia nájdete v [33.1. 2D Forming Setup](/docs/en/operation_templates/33_forming/33_1_2d_forming_setup/) alebo [34.1. 2D Forming Express Setup](/docs/en/operation_templates/34_forming_express/34_1_2d_forming_express_setup/).

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image028.jpg' | relative_url }})

Pridanie operácie tvarovania po operácii rýchleho prenosu tepla

## Definícia operácie „Dwell on die“

  
Operácia „Dwell on die“ (zotrvanie na forme) alebo „Dwelling“ slúži na nastavenie prenosu tepla z horúceho obrobku do okolia a do formy po tvarovaní a predtým, ako sa forma stiahne z obrobku. Používateľ musí túto operáciu pridať za operácie tvarovania, ako je znázornené na obr. 36.1.37.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image029.jpg' | relative_url }})

Pridanie operácie „Expresný prenos tepla“ po operácii tvarovania na účely nastavenia režimu vydržiavania

V režime „Bývanie“ bude používateľ vedený nastavovacími oknami rovnako ako v režime „Kúrenie“, s výnimkou ovládacích prvkov na zastavenie kúrenia, ako je znázornené na obr. 36.1.38. Na rozdiel od režimu „Kúrenie“ je v tomto režime povolené zadávať viac ako jeden objekt a systém automaticky prenesie všetky objekty z predchádzajúceho režimu do tohto režimu. Tento režim tiež pridáva možnosti tepelného výpočtu, umiestňovania objektov a definovania vzájomných vzťahov medzi objektmi, ktoré sú potrebné na výber tepelných výpočtov pre formy, umiestnenie objektov a definovanie a generovanie podmienok kontaktu medzi objektmi. Tieto dodatočné možnosti, ktoré sa líšia od možností režimu kúrenia, sú popísané v časti 36.1.5. Definovanie režimu „Odpočinok na forme“.

### Definícia tepelného stavu

V tomto okne je potrebné definovať podmienky ohrevu, ako sú doba zdržania (trvanie procesu), teplota okolia a koeficient konvekcie, ako je znázornené na obr. 36.1.38. Pre všetky typy ohrevu systém štandardne definuje podmienky ohrevu; používateľ musí zadať údaje o nastaveniach procesu zmenou predvolených hodnôt.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image030.jpg' | relative_url }})

Okno nastavení teplotných podmienok

Po nastavení teplotných podmienok musí používateľ definovať ovládacie prvky simulácie; podrobnosti o nastavení ovládacích prvkov simulácie nájdete v časti Definícia ovládacích prvkov simulácie.

  
Databáza „Next“ sa musí vygenerovať v prípade interaktívneho nastavenia alebo ak ide o prvú operáciu prenosu; v opačnom prípade sa databáza vygeneruje automaticky počas simulácie. Ďalšie informácie o ovládacích prvkoch simulácie a generovaní databázy nájdete v článkoch „Simulation_controls_Definition“ a „Generate Database“.

**Súvisiace témy:**

[33.1. 2D Forming Setup](/docs/en/operation_templates/33_forming/33_1_2d_forming_setup/)

[34.1. 2D Forming Express Setup](/docs/en/operation_templates/34_forming_express/34_1_2d_forming_express_setup/).

[36.2.3D Heat Transfer Express Operation](/docs/en/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/)
