---
lang: sk
title: "36.2. 3D Heat Transfer Express"
---

# 36.2. 3D Heat Transfer Express

36.2.1. Ako pridať operáciu 3D Heat Transfer Express

36.2.2. Definícia nastavení procesu

36.2.3. Typ vykurovania

36.2.4. Nastavenie režimu kúrenia

  * Objekt – základná definícia

  * Definícia geometrie objektu

  * Definícia sieťového modelu objektu

  * Definícia materiálu

  * Okrajové podmienky

  * Definícia teplotných podmienok

  * Definícia ovládacích prvkov na zastavenie

  * Definícia ovládacích prvkov simulácie

  * Vytvoriť databázu

36.2.5. Definícia prevádzky prenosu tepla

  * Výber objektov

  * Umiestňovanie objektov a vytváranie vzťahov medzi objektmi

  * Definícia tepelného stavu

36.2.6. Definovanie operácie „Odpočinok na matrici“

  * Definovať tepelné výpočty

  * Výber objektov

  * Polohovanie

  * Plánovanie umiestnenia

  * Generovanie kontaktov medzi objektmi

  * Definícia teplotných podmienok

36.2.7. Pokračovanie v definovaní tvárniacich operácií

  * Definícia prevádzky s dobou zdržania na čipoch

  * Definícia teplotných podmienok

## Ako pridať operáciu „3D Heat Transfer Express“

Operácia „Heat Transfer Express“ je dostupná cez sprievodcu MO Wizard, ktorý je možné otvoriť z hlavného grafického rozhrania. Operáciu „Heat Transfer Express“ je možné pridať v sprievodcovi MO Wizard na karte „Explorer“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky „3D Heat Transfer Express“. Užívateľ ju môže pridať aj pomocou funkcie drag and drop do Editoru operácií, ako je znázornené na obr. 36.2.1. Operáciu Heat Transfer Express je možné pridať aj interaktívne po operáciách prenosu tepla po simulácii predchádzajúcich operácií alebo v dávkovom/naplánovanom režime.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image001.jpg' | relative_url }})

Do editora operácií bola pridaná operácia „3D Heat Transfer Express“

## Definícia nastavení procesu

V okne „Process“ je potrebné pre operáciu prenosu tepla nastaviť simulačné režimy, ako sú „Geometry Type“, „Heating Type“, „Shape Complexity“ a „Accuracy“, ako je znázornené na obr. 36.2.1.

**Typ geometrie**

V programe Heat Transfer Express 3D je možné nastaviť modely s plnou geometriou a symetrickou geometriou výberom príslušných prepínačov typu geometrie: **Celý** diel alebo **Symetria**.

  
Ak je obrobok asymetrický alebo je potrebné skúmať akékoľvek asymetrické správanie počas prenosu tepla a následných operácií tvárnenia, musí používateľ zvoliť typ geometrického modelu „Celá súčiastka“.

  
Ak je obrobok symetrický, používateľ môže zvoliť typ geometrie „Symetrická“, aby nastavil symetrický model úlohy; tým sa za oknom geometrie obrobku zobrazí okno na výber symetrických rovín. V okne symetrie musí používateľ vybrať symetrické roviny, aby stanovil rýchlosť pozdĺž symetrickej roviny.

## Typ vykurovania

V režime Heat Transfer Express sú v 2D aj 3D k dispozícii štyri typy ohrevu alebo procesov prenosu tepla, a to (pozri obr. 36.2.1.):

  * **Kúrenie**

  * **Prenos**

  * **Odpočinok na kocke a**

  * **Zotrvanie na čipe**

Ohrievanie obrobku, prenos tepla pri presúvaní obrobku z pece do lisu, odloženie obrobku na formu (pred tvárnením) a zotrvanie obrobku na forme po tvárnení je možné jednoducho nastaviť pomocou príslušného typu ohrevu. Podrobnejšie informácie o týchto typoch ohrevu sú uvedené v dokumente [36\. Introduction to heat transfer express operation](/docs/en/operation_templates/36_heat_transfer_express/36_introduction_to_heat_transfer_express_operations/), pozri časť „Typy ohrevu“.

V režimoch „Odpočinok“ a „Prevádzka“ sa aktivuje okno pre tepelný výpočet, ktoré ponúka možnosti výberu, či sa má počítať prenos tepla cez matrice, alebo nie. Tieto možnosti budú podrobnejšie vysvetlené v popisoch príslušných režimov.

**Zložitosť tvaru a presnosť**

Posuvníky pre zložitosť tvaru a presnosť simulácie (pozri obr. 36.2.1.) ovplyvňujú nastavenia siete a počet časových krokov použitých v simulácii. To zase ovplyvňuje dĺžku behu a úroveň detailov dostupnú v simulácii.

**Zložitosť tvaru:**

  * **Jednoduché**: Geometria objektov je svojou povahou jednoduchá. Vyžadujú si minimálny počet prvkov, ich riešenie je jednoduchšie a trvá kratšie.

  * **Stredná**: Geometria objektov je stredne zložitá (nie príliš zložitá).

  * **Zložité**: Geometria objektov má zložitý charakter.

  
**Presnosť tvaru:**

  * **Rýchly**: Vhodný na rýchle vyhodnotenie procesu. Výmenou za rýchlejšie časy spustenia však existuje vyššie riziko, že sa prehliadnu dôležité detaily.

  * **Stredná**: Simulácia používa nastavenia, ktoré sa snažia dosiahnuť rovnováhu medzi výpočtovým časom a presnosťou.

  * **Presné**: Vykonáva sa veľmi podrobná analýza procesu, ktorá zvyčajne zachytí aj tie najmenšie detaily. Čas potrebný na výpočet a požiadavky na úložný priestor sú vyššie.

## Definícia režimu kúrenia

Pri prevádzke v režime ohrevu alebo v režime pece sa modeluje ohrev sochory v peci. Po výbere nastavení procesu systém zobrazí prispôsobené okná pre operáciu ohrevu, ktoré používateľa prevedú nastavením tejto operácie. Pre túto operáciu je povolený len jeden objekt (pozri obr. 36.2.2.) a tento objekt sa pridá automaticky. Pridajú sa predvolené nastavenia procesu vhodné pre operáciu ohrevu.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image002.jpg' | relative_url }})

Okno na definovanie objektu vykurovacieho režimu

### Základná definícia objektu

Základná definícia objektu zahŕňa názov objektu, typ a teplotu. Okrem toho je možné pomocou tlačidla „Advanced“ inicializovať hodnoty premenných stavu objektu a údaje o objekte, ako sú geometria, sieť, okrajové podmienky a materiál, je možné importovať zo súboru DEFORM .DB /.Key. (Pozri obr. 36.2.3.)

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image003.jpg' | relative_url }})

Okno obrobku

  
**Názov objektu**: Používateľ môže definovať názov všetkých objektov dostupných v danej operácii.

  
**Typ objektu**: Typ objektu ([OBJTYP](/docs/en/keyword_documentation/o/objtyp/)) určuje, či a ako sa modeluje deformácia pre každý jednotlivý objekt v úlohe typu DEFORM. V operácii Forming Express sú k dispozícii len dva typy objektov, a to plastický a tuhý, ktoré sú automaticky preddefinované podľa čísla objektu, takže obrobok bude plastický a formy budú tuhé. V operácii Forming je k dispozícii viac typov objektov, podrobnosti nájdete v [11.4. Object Type](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type).

  
**Plast**: Plastové objekty sa modelujú ako tuho-plastický alebo tuho-viskoplastický materiál v závislosti od vlastností materiálov. Model predpokladá, že napätie v materiáli lineárne rastie s rýchlosťou deformácie až do prahovej hodnoty rýchlosti deformácie, označovanej ako limitná rýchlosť deformácie ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)). Po prekročení medznej rýchlosti deformácie sa materiál deformuje plasticky. Plastické správanie materiálu objektu sa špecifikuje pomocou funkcie tečenia materiálu alebo údajov o tečivom napätí ([FSTRES](/docs/en/keyword_documentation/f/fstres/)). V programe Heat Transfer Express sa obrobok automaticky priradí k typu objektu „Plast“.  
**Tuhé**: Tuhé objekty sa modelujú ako nedeformovateľné materiály. V analýze deformácie je objekt reprezentovaný geometrickým profilom ([DIEGEO](/docs/en/keyword_documentation/d/diegeo/)). Údaje o riešení deformácie dostupné pre tuhé objekty zahŕňajú zdvih objektu, zaťaženie a rýchlosť. Sieť pre tuhý objekt sa používa iba na výpočty tepelného prenosu, transformácie a difúzie. V programe Heat Transfer Express sú lisovacie formy alebo nástroje automaticky priradené k typu „Tuhý“, keďže ide o nedeformovateľné objekty.

**Poznámka:**

Je potrebné poznamenať, že typ objektu je v operácii programu Heat Transfer Express preddefinovaný číslom objektu. Prvý objekt bude z plastu a pri ďalšom pridávaní sa budú pridávať iba tuhé objekty.  
Na stránke „Objekt“ sa nachádza tlačidlo „Importovať objekt“. Slúži na import kompletných údajov o objekte z iného súboru DEFORM.

  
**Teplota objektu**: Používateľ môže nastaviť teplotu objektu v poli „Teplota“ v príslušnom okne objektu, ako je znázornené na obr. 36.2.3.

**Pokročilé nastavenia objektu**: Pokročilé nastavenia v časti „Možnosti inicializácie“ (pozri obr. 36.2.4.) sa zídu v prípade, ak používateľ importuje objekt z predchádzajúceho projektu alebo úlohy, alebo ak sa operácia „express“ pridá až po niekoľkých iných operáciách a je potrebné inicializovať niekoľko dôležitých stavových premenných.  
Pomocou pokročilých nastavení môže používateľ zadať teplotu, deformáciu, rýchlosť, poškodenie a posun, ku ktorým došlo v deformovateľnom objekte. (Pozri obr. 36.2.4.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image005.jpg' | relative_url }})

Pokročilé nastavenia objektov

  
V operácii „Forming“ je možné inicializovať ďalšie premenné; podrobnosti nájdete v operácii [35\. 2D Heat Transfer](/docs/en/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/) a [Initialize](../35_heat_transfer/35_1_2d_heat_transfer_operation.htm#Initialize).

Priemerná rýchlosť deformácie ([AVGSTR](/docs/en/keyword_documentation/a/avgstr/)) je charakteristická priemerná hodnota efektívnej rýchlosti deformácie. Na začiatku simulácie by sa mala zadať aproximácia tejto hodnoty.

Medzná rýchlosť deformácie ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)) definuje medznú hodnotu efektívnej rýchlosti deformácie, pod ktorou sa plastický alebo porézny materiál považuje za tuhý a správa sa ako materiál s newtonovskými vlastnosťami.

![]({{ '/assets/icons/pre_icons/mo_reset_button.jpg' | relative_url }}) : Pomocou tejto funkcie môže používateľ obnoviť hodnoty premenných v počiatočnom stave.

Ďalšie možnosti vlastností objektu „Deformácia“, ktoré sú k dispozícii v operácii „Tvarovanie“, nájdete v [16.1. Deformation Properties.](/docs/en/pre_processor/16_object_properties/16_1_deformation_properties/)

### Definícia geometrie objektu

Okno „Geometria“ slúži na vytvorenie geometrie objektu, ako je znázornené na obr. 36.2.5. Pred vytvorením geometrie je k dispozícii iba možnosť „Definovať primitívnu geometriu“, avšak po vytvorení geometrie sa aktivujú možnosti „Skontrolovať“, „Zmenšiť“, „Obrátiť“, „Opraviť“ a „Označiť“ geometriu povrchu a po vygenerovaní siete sa aktivuje možnosť „Extrahovať okraj“. 

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image006.jpg' | relative_url }})

Okno s definíciou geometrie

**Definovať primitív ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }})**

V rámci geometrických primitív existujú tri základné tvary, ako sú Krabica, Valec a Dutý valec, ktoré možno použiť na vytvorenie geometrií, ako je znázornené na obr. 36.2.6. V každom prípade musí používateľ prispôsobiť rozmery tak, aby zodpovedali danej úlohe. Okrem týchto primitívov je možné použiť funkcie Extrude a Revolve na prevod 2D priečneho rezu na 3D. Objekty s rotačnou symetriou sa vytvárajú pomocou možnosti uhla otáčania pre primitíva Cylinder, Hollow Cylinder a Revolve. 

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image007.jpg' | relative_url }})

Okno geometrických primitív 

**Check![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) **

Vždy skontrolujte geometriu. Program DEFORM disponuje kontrolným algoritmom, ktorý overuje počet neplatných hrán, neplatnú orientáciu, mnohouholníky s malou plochou a počet plôch. Nie je možné odhaliť všetky typy chýb.

Použitím tejto možnosti „Skontrolovať geometriu“ sa otvorí okno „Výsledky kontroly geometrie“, ktoré obsahuje prehľad geometrie objektu (pozri obr. 36.2.7.). V prípade objektu s uzavretým objemom by mala byť prítomná 1 plocha, 0 voľných hrán a 0 neplatných entít (ako je označené kružnicou nižšie na obr. 36.2.7.). Objekty, ktoré sú importované ako plochy a nie ako telesa, budú mať voľnú hranu, ale aj tak by mali mať len 1 plochu. 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image011.jpg' | relative_url }})

Výsledky kontroly geometrie

**Scale![]({{ '/assets/icons/pre_icons/mo_scale_label.jpg' | relative_url }}) **

Geometriu je možné pri tvárnení zmenšiť alebo zväčšiť tak, aby zohľadňovala teplotnú rozťažnosť, a to stanovením mierky. (Pozri obr. 36.2.8.) Mierku je možné vypočítať na základe teplotného rozdielu a údajov o materiáli závislých od teploty. Upravenú geometriu je možné uložiť v rôznych formátoch na ukladanie geometrie.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image014.jpg' | relative_url }})

Okno „Scale Geo“

  
**Reverse![]({{ '/assets/icons/pre_icons/mo_reverse_label.jpg' | relative_url }}) **

Táto funkcia obráti smer povrchu/normály geometrie. Smer povrchu/normály geometrie by mal byť vždy smerom von.

**Fix![]({{ '/assets/icons/pre_icons/mo_fix_label.jpg' | relative_url }})**

Táto funkcia rieši geometrické problémy, pri ktorých sa vyskytujú buď viaceré plochy, alebo otvorené oblasti (diery), a to odstránením všetkých nadbytočných plôch a vyplnením dier. Pri menších alebo ohraničených problémoch to funguje dobre. V prípade zložitejších súborov, ako je tento, nemusí oprava priniesť požadovaný výsledok. (Pozri obr. 36.2.9.) 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image016.jpg' | relative_url }})

Určenie geometrie formy na kľukový hriadeľ

**Označiť povrch**

Označením akéhokoľvek povrchu sa tento povrch vylúči z výpočtov kontaktov počas simulácie. Aj keby sa obrobok s týmto objektom dostal do kontaktu, táto funkcia sa zvyčajne používa pre povrchy lisovacích foriem a razníkov, kde v reálnych podmienkach nedochádza k vytváraniu kontaktov, aby sa zabránilo nežiaducim výpočtom kontaktov.

**Ďalšie možnosti geometrie**

**Zobraziť geometriu vnútri značky:** Zaškrtnutím tejto možnosti sa aktivuje zobrazenie orientácie geometrie.

**Určiť referenčný bod**: Používateľ môže vybrať referenčný bod geometrie kliknutím na toto tlačidlo v zobrazovacom okne. Tento referenčný bod je potrebný na určenie vzdialenosti medzi objektmi pomocou ovládacích prvkov na zastavenie.

**Import geometrie zo súboru** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}): Importuje geometriu zo súboru  
**Načítať geometriu z knižnice** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}): Importuje geometriu z knižnice  
**Uloženie geometrie do súboru** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) : Uloží geometriu do súboru.  
**Uložiť geometriu do knižnice** ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ uložiť geometriu do knižnice.  
**Odstrániť geometriu** ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}): používateľ môže odstrániť geometriu.

### Definícia roviny symetrie pre obrobok

  
Okno „Symetria“ sa zobrazí po okne „Geometria“, ak používateľ vyberie typ geometrie „Symetria“. Symetriu je potrebné definovať s cieľom zafixovať rýchlosť uzlov na rovinách symetrie, ako je znázornené na obr. 36.2.10. Najskôr musí používateľ vybrať rovinu symetrie kliknutím ľavým tlačidlom myši; vybraná rovina sa zafarbí na zeleno. Následne kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridá vybranú rovinu; v prípade viac ako jednej roviny symetrie zopakujte rovnaké kroky. Pre vybranú rovinu systém zobrazí stred a normálu, ako je znázornené na obr. 36.2.10.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image002.jpg' | relative_url }})

Okno s definíciou roviny symetrie

### Definícia objektovej siete

Okno „Vytvorenie siete“ umožňuje používateľovi vytvoriť sieť pre aktuálny objekt. Na obr. 36.2.11 je zobrazené okno „Vytvorenie siete“ v systémovom režime. V tomto režime systém automaticky nastaví počet prvkov siete na základe zložitosti tvaru a výberu nastavenia presnosti v pracovnom okne.

**Režim systému**

Pomocou **![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }})** musí používateľ vytvoriť sieť tetraédrov pre objekty. Používateľ môže vytvoriť  
Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_mesh_preview_button.jpg' | relative_url }}) je možné rýchlo zobraziť náhľad povrchovej siete alebo náhľad siete ešte pred vytvorením objemovej siete potrebnej pre daný objekt. Akonáhle je používateľ spokojný s náhľadom povrchovej siete, sieť je možné na objekte vytvoriť kliknutím na **![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }})**.

Po vytvorení siete sa aktivuje tlačidlo „![]({{ '/assets/icons/pre_icons/mo_delete_button.jpg' | relative_url }})“, ktoré slúži na vymazanie aktuálnej siete objektu. Ak chce používateľ zmeniť automaticky vypočítaný počet prvkov alebo upraviť pokročilé nastavenia, musí prejsť do režimu „User Defined Mode“.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image003.jpg' | relative_url }})

Okno nastavení siete v režime Systém

**Režim definovaný používateľom**

Možnosť režimu užívateľsky definovanej siete je znázornená na obr. 36.2.12. V tomto režime môže užívateľ meniť počet prvkov posúvaním posuvníka a pomocou pokročilých možností upravovať pomer veľkostí, minimálnu veľkosť prvkov, kritériá pregenerovania siete a boolovské operácie. Používateľ môže vygenerovať povrchovú sieť a prezrieť si jej náhľad. Akonáhle je s povrchovou sieťou spokojný, môže vygenerovať objemovú sieť pre 3D objekt kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_solid_mesh_button.jpg' | relative_url }}).

**Počet prvkov (MGNELM):**

Počet prvkov siete predstavuje približný počet prvkov, ktoré systém vygeneruje. Automatický generátor siete (AMG) preberá hodnotu z [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) a vygeneruje sieť, ktorá bude obsahovať približne rovnaký počet prvkov. Počet prvkov je možné určiť jednoduchým posunutím posuvníka a výberom vhodnej hodnoty pre aktuálnu simuláciu.

  
Chyba medzi počtom zadaných prvkov a počtom vygenerovaných prvkov sa zvyčajne pohybuje okolo desiatich percent.

  
Ak chce používateľ zmeniť ďalšie nastavenia siete, musí kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_advanced_button.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image010.jpg' | relative_url }})

Nastavenia siete v užívateľsky definovanom režime

**Pokročilé nastavenia siete**

  * Všeobecné nastavenia siete: V programe DEFORM existujú dva rôzne typy sietí, ktoré je možné vytvoriť pre 3D objekty.

  * **Relatívna sieť:** Pomocou nastavenia relatívnej siete používateľ určí počet pevných prvkov, ktoré sa majú vygenerovať. Bez ohľadu na to, aký zložitý bude tvar dielu, počet prvkov zostane v podstate konštantný. (Obr. 36.2.13.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image011.jpg' | relative_url }})

Nastavenia relatívnej veľkosti ok

  * **Absolútna sieť**: Pri použití nastavenia absolútnej siete používateľ určí veľkosť prvkov a systém na základe zadaných rozmerov prvkov a geometrie určí celkový počet potrebných prvkov. S rastúcou zložitosťou modelu sa počet prvkov zvyčajne zvyšuje. (Obr. 36.2.14.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image012.jpg' | relative_url }})

Nastavenia absolútnej siete

  * **Pomer veľkostí prvkov (MGSIZR)**: Maximálny pomer veľkostí medzi prvkami je jedným z viacerých spôsobov, ako regulovať hustotu siete počas automatického generovania siete (AMG) prostredníctvom špecifikácie pomeru hustôt uzlov. Pri hodnote 3 pre [MGSIZR](/docs/en/keyword_documentation/m/mgsizr/) bude najväčšia hrana prvku na objekte približne 3-krát väčšia ako najmenšia hrana prvku na tom istom objekte. Ak sa požadujú prvky rovnakej veľkosti, pomer veľkostí je 1. Ak je pomer veľkostí 0, pomer veľkostí prvkov nebude mať vplyv na rozloženie hustoty siete.

  * **Kritériá pre výpočet novej siete:**

Kritériá pregenerovania siete (Autoremesh) predstavujú najpohodlnejší spôsob, ako riešiť pregenerovanie siete objektov, ktoré prechádzajú veľkou plastickou deformáciou. Okno Kritériá pre vytváranie novej siete (pozri obr. 36.2.14.) obsahuje skupinu parametrov, ktoré na základe priradenia určitých spúšťačov riadia, kedy a ako často sa bude sieť na objektu so sieťou regenerovať. Existujú štyri kľúčové slová, ktoré riadia spustenie postupu premenovania siete pre objekt: Hĺbka interferencie ([RMDPTH](/docs/en/keyword_documentation/r/rmdpth/)), Max. časový prírastok ([RMTIME](/docs/en/keyword_documentation/r/rmtime/)), Max. krokový prírastok ([RMSTEP](/docs/en/keyword_documentation/r/rmstep/)) a Max. prírastok zdvihu ([RMSTRK](/docs/en/keyword_documentation/r/rmstrk/)). Keď sú splnené kritériá pregenerovania siete pre ktorékoľvek z týchto kľúčových slov alebo sa sieť stane nepoužiteľnou (záporná jacobiánska matica), objekt sa pregeneruje, informácie o riešení zo starej siete sa interpolujú na novú sieť a simulácia pokračuje.

  * **Vzdialenosť prenikania (relatívna)**

Ak sa zadá záporné číslo (zlomok), program vykoná kontrolu každého okraja povrchu, ktorý má na oboch koncoch kontaktný uzol. Vypočíta sa vzdialenosť od stredu okraja k povrchu formy a vydelí sa pôvodnou dĺžkou okraja. Ak tento pomer prekročí veľkosť zadaného čísla, spustí sa prepočítanie siete.

  * **Maximálny prírastok zdvihu (RMSTRK)**

Vždy, keď prírastok zdvihu primárnej matrice od posledného kroku vytvárania novej siete prekročí maximálny prírastok zdvihu ([RMSTRK](/docs/en/keyword_documentation/r/rmstrk/)), spustí sa nový krok vytvárania novej siete.

  * **Maximálny časový krok (RMTIME)**

Vždy, keď uplynie maximálny časový interval ([RMTIME](/docs/en/keyword_documentation/r/rmtime/)) (hodnota uplynutého času) od posledného kroku premenovania siete, spustí sa nový krok premenovania siete.

  * **Maximálny krok (RMSTEP)**

Vždy, keď od posledného kroku premenovania siete dôjde k dosiahnutiu maximálneho kroku premenovania (počet krokov), spustí sa nový krok premenovania siete.

**Odstrániť sieť**![]({{ '/assets/icons/pre_icons/mo_delete_mesh_button.jpg' | relative_url }})

Odstráni sieť vytvorenú pre daný objekt.

Na rozdiel od operácie „Forming“ nie sú v operácii „Forming Express“ k dispozícii ďalšie možnosti siete, ako napríklad sieť s povrchovou úpravou, váhové koeficienty hustoty systémovej siete či možnosti okna „User Mesh Density“; informácie o týchto možnostiach nájdete v kapitole [13.2. 3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/).

### Definícia materiálu

Na obr. 36.2.15. je zobrazené okno s materiálmi. Používateľ môže pridať alebo importovať materiál zo súboru kľúčových slov alebo ho načítať z knižnice materiálov programu DEFORM.

  
Po načítaní systém automaticky priradí načítaný materiál k objektu. Používateľ môže vlastnosti materiálu upravovať aj pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image004.jpg' | relative_url }})

Okno s materiálmi

Po pridaní materiálu kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) – otvorí sa okno s materiálom, ako je znázornené na obr. 36.2.16.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image022.jpg' | relative_url }})

Okno na úpravu materiálu

Požadované vlastnosti závisia od fyzikálnych javov simulovaných v programe DEFORM. Vlastnosti materiálu, ktoré musí používateľ zadať, závisia od typov materiálov, ktoré používateľ v simulácii využíva. V operácii „Tvarovanie“ má používateľ prístup ku všetkým vlastnostiam materiálu; ďalšie informácie nájdete v [10\. Material Data.](/docs/en/pre_processor/10_material_data/10_material_data/).

### Okrajové podmienky

V okne „Forming express – Okrajové podmienky“ môže používateľ objektu priradiť iba okrajové obmedzenia typu „Rovinná symetria“, „Rýchlosť deformácie“, „Teplotná výmena s okolím“ a „Teplota“. Okrajové podmienky určujú, ako hranica objektu interaguje s inými objektmi a s okolím. Najčastejšie používanými okrajovými podmienkami sú výmena tepla s okolím pri simuláciách zahŕňajúcich prenos tepla a predpísaná rovina symetrie na vynútenie symetrie v modeli. Obr. 36.2.17. znázorňuje rôzne okrajové podmienky, ktoré je možné priradiť k objektu.

  
V predvolenom nastavení sa k objektu obrobku pridajú rovinné symetrické roviny podľa výberu symetrických rovín v okne symetrie, ako je znázornené na obr. 36.2.17. Okrem toho sa pri procesoch teplého a horúceho kovania priradí výmena tepla s okolím ku všetkým povrchom s výnimkou symetrických rovín, ako je znázornené na obr. 36.2.18.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image005.jpg' | relative_url }})

Pre obrobok bola nastavená okrajová podmienka symetrie

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image006.jpg' | relative_url }})

Pre obrobok bola nastavená okrajová podmienka výmeny tepla s okolím

Ďalšie možnosti BCC v rôznych kategóriách sú k dispozícii v predspracovaní a formovacích operáciách, napríklad [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/), [Thermal](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/), [Diffusion](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/) a [Heating](/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/). Ďalšie informácie o týchto BCC nájdete v [14\. Boundary Conditions.](../../pre_processor/14_boundary_conditions).

### Definícia tepelného stavu

V tomto okne je potrebné definovať tepelné podmienky, ako sú doba ohrevu (trvanie procesu), teplota okolia a konvekčný koeficient, ako je znázornené na obr. 36.2.19. Pre všetky typy ohrevu systém štandardne definuje podmienky ohrevu; na zmenu týchto predvolených nastavení je potrebné zadať údaje o nastaveniach procesu.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image012.jpg' | relative_url }})

Okno nastavení teplotných podmienok

### Definícia ovládacích prvkov na zastavenie

Iba v režime kúrenia poskytuje funkcia prenosu tepla ovládacie prvky na zastavenie simulácie, keď sa všetky uzly obrobku nachádzajú v stanovenom rozsahu teplôt od nastavenej hodnoty alebo okolitej teploty, ako je znázornené na obr. 36.2.20. Na obr. 36.2.20 sa simulácia zastaví, ak sú teploty všetkých uzlov v rozmedzí od 1199,5 °C do 1200,5 °C.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image013.jpg' | relative_url }})

Okno na ovládanie vypnutia kúrenia

### Definícia ovládacích prvkov simulácie

Systém DEFORM rieši časovo závislé nelineárne úlohy generovaním série riešení metódou konečných prvkov (FEM) v diskrétnych časových krokoch. V každom časovom kroku sa rýchlosti, teploty a ďalšie kľúčové premenné každého uzla v sieti konečných prvkov určujú na základe okrajových podmienok, termomechanických vlastností materiálov obrobku a prípadne riešení z predchádzajúcich krokov. Ostatné stavové premenné sa odvodzujú z týchto kľúčových hodnôt a aktualizujú sa pri každom časovom kroku. Dĺžka tohto časového kroku a počet simulovaných krokov sa určujú na základe informácií zadaných v ponuke nastavení krokov. Obr. 36.2.21. znázorňuje možnosti ovládania simulácie.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image014.jpg' | relative_url }})

Okno ovládacích prvkov simulácie v definícii systému

Používateľ musí určiť čas na jeden krok (definícia kroku), celkový počet krokov a veľkosť kroku, ktoré sa majú uložiť v definícii krokov používateľa a systému. V programe Heat Transfer Express sú k dispozícii tri typy definícií krokov: systémová, používateľská a automatická.

Typ **systému** (pozri obr. 36.2.21.) – automatický výpočet definície kroku na základe zadaného času ohrevu a zvolených nastavení presnosti a zložitosti. V závislosti od rôznych nastavení presnosti a zložitosti systém upraví prvky siete objektu a veľkosť kroku zmenou počtu krokov. Ak používateľ potrebuje zmeniť automaticky vypočítanú definíciu kroku, typ „Používateľ“ umožňuje zmeniť definíciu kroku.

Používateľ s typom **User** bude mať prístup k úprave definícií krokov podľa potreby, ako je znázornené na obr. 36.2.22.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image015.jpg' | relative_url }})

Ovládacie prvky pre definíciu krokov používateľa

Typ „Auto“ predstavuje krokové riadenie založené na teplote, pričom nastavenia DTPMAX určujú časový krok. Účelom týchto nastavení je špecifikovať časový krok simulácie, ktorá je riadená deformáciou vyvolanou teplotou. Používateľ musí určiť počiatočný časový krok (čas na krok), maximálnu zmenu teploty na krok, minimálny čas na krok a maximálny čas na krok, ako je znázornené na obr. 36.2.23.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image016.jpg' | relative_url }})

Pokročilé ovládacie prvky na definovanie krokov

**Zmena teploty na jeden krok (DTPMAX) [2D, 3D]:**

Maximálny prírastok zmeny teploty obmedzuje rozsah, o ktorý sa môže teplota ktoréhokoľvek uzla zmeniť počas jedného časového kroku. Ak je priradená hodnota odlišná od nuly, spustí sa nový podkrok, keď zmena teploty v ktoromkoľvek uzle dosiahne hodnotu DTPMAX. Maximálny/minimálny časový krok predstavuje najväčší a najmenší časový krok povolený pri podkrokovaní založenom na teplote.

### Vytvoriť databázu

**Overiť údaje**![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})****

Systém skontroluje údaje. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvoriť databázu ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})**

Kliknutím na toto tlačidlo sa vytvorila databáza pre nastavenie. (Pozri obr. 36.2.24.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image050.jpg' | relative_url }})

Okno „Vytvoriť databázu“

## Definícia prevádzky prenosu tepla

Operácia „Prenos tepla“ sa bežne používa na nastavenie konvekčného prúdenia vzduchu počas presunu obrobku z pece do lisu. Používateľ môže túto operáciu pridať po operácii ohrevu alebo začať samotným prenosom tepla na ohriaty obrobok ako prvou operáciou. V operácii „Transfer“ bude používateľ vedený nastavovacími oknami rovnako ako v operácii „Heating“, s výnimkou ovládacích prvkov na zastavenie ohrevu, ako je znázornené na obr. 36.2.25. Podrobnosti o základnej definícii objektu, geometrii, sieti, materiáli a okrajových podmienkach nájdete v časti Definovanie operácie ohrevu. Okrem možností operácie ohrevu môže používateľ pridať viac ako jeden objekt, čím sa pridávajú možnosti polohovania objektov a definície vzájomných vzťahov medzi objektmi. Tieto možnosti sú popísané v tejto časti.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image007.jpg' | relative_url }})

Po ohreve v peci pridať operáciu prenosu tepla

### Výber objektov

V operácii „Prenos tepla“ je povolené použiť viac ako jeden objekt. V závislosti od nastavenia procesu si môže používateľ v tomto okne vybrať počet objektov potrebných na vykonanie operácie (pozri obr. 36.2.26.). Užívateľ musí mať na pamäti, že v simulácii môže byť len jeden plastový objekt. Je možné pridať maximálne 100 foriem.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image008.jpg' | relative_url }})

Nastavenia výberu objektov pri operácii presunu

### Umiestňovanie objektov a vytváranie vzťahov medzi objektmi

Ak používateľ vyberie viac ako jeden objekt, systém za objektmi pridá ovládacie prvky (polohovanie) a okná naplánovaného polohovania a kontaktu, aby sa objekty správne umiestnili a aby sa v prípade potreby v nastavení vytvoril kontakt medzi objektmi. Ďalšie podrobnosti o týchto možnostiach nájdete v časti [Defining Rest on die operation](36_1_2d_heat_transfer_express.htm#36_1_5_Defining_Rest_on_die_Operation), konkrétne v oddieloch [Positioning](36_1_2d_heat_transfer_express.htm#Positioning) a [Scheduled Positioning](36_1_2d_heat_transfer_express.htm#Schedule_Positioning).

### Definícia pojmu „tepelné podmienky“

V tomto okne je potrebné definovať podmienky ohrevu, ako sú doba prenosu (trvanie procesu), teplota okolia a koeficient konvekcie, ako je znázornené na obr. 36.2.27. Pre všetky typy ohrevu systém štandardne definuje podmienky ohrevu; používateľ musí zadať údaje o nastaveniach procesu zmenou predvolených hodnôt.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image019.jpg' | relative_url }})

Teplotné podmienky pri prevádzke prenosu

Po nastavení teplotných podmienok musí používateľ definovať ovládacie prvky simulácie; podrobnosti o nastavení ovládacích prvkov simulácie nájdete v časti Definícia ovládacích prvkov simulácie.

Databáza Next sa musí vytvoriť v prípade interaktívnej inštalácie alebo ak je operácia prenosu prvou operáciou; v opačnom prípade sa databáza vytvorí automaticky počas simulácie. Ďalšie informácie o ovládacích prvkoch simulácie a vytváraní databázy nájdete v častiach [Simuation controls Definition](36_1_2d_heat_transfer_express.htm#Simulation_controls_Definition) a [Generate Database](36_1_2d_heat_transfer_express.htm#Generate_Database).

## Definovanie operácie „Odpočinok na matrici“

Operácia „Odpočinok na forme“ alebo „Odpočinok“ slúži na nastavenie prenosu tepla z horúceho obrobku do okolia a do formy, na ktorej odpočíva pred tvarovaním. Používateľ môže túto operáciu pridať po operácii prenosu tepla alebo môže začať priamo operáciou odpočinku zahriateho obrobku ako prvou operáciou. V operácii odpočinku bude používateľ vedený nastavovacími oknami rovnako ako v operácii ohrevu, s výnimkou ovládacích prvkov na zastavenie ohrevu, ako je znázornené na obr. 36.2.28. Okrem možností operácie ohrevu môže používateľ pridať viac ako jeden objekt, čím sa pridajú možnosti tepelného výpočtu, polohovania objektov a definície vzťahov medzi objektmi. Tieto možnosti sú rozoberané v tejto časti.

Systém štandardne pridá dva objekty čipov a voľba pre výpočet tepelného správania sa zobrazí za oknom procesu, ako je znázornené na obr. 36.2.28.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image009.jpg' | relative_url }})

Pridanie operácie odpočinku po operácii prenosu tepla

### Definícia tepelných výpočtov

Okno „Výpočet teploty“ (pozri obr. 36.2.29.) ponúka možnosti „Neizotermické“, ktoré umožňujú vybrať výpočet teploty iba v obrobku alebo v obrobku aj v lisovacích formách.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image021.jpg' | relative_url }})

Okno na výber typu výpočtu teploty

**Neizotermický**: Proces, pri ktorom teplota systému nie je konštantná. Zahrnutie výpočtov teploty zlepší predpovede toku materiálu a predpovede zaťaženia, najmä v procesoch, kde dochádza k výrazným zmenám teploty. Výpočet teploty v nástrojoch ďalej zlepšuje výpočet teploty obrobku, pretože zmena teploty nástroja ovplyvňuje únik tepla z obrobku.

### Výber objektov

V tomto okne si môže používateľ v závislosti od nastavenia procesu vybrať počet objektov potrebných na vykonanie operácie (pozri obr. 36.2.30.). Používateľ musí mať na pamäti, že v simulácii môže byť len jeden plastový objekt. Je možné pridať maximálne 100 foriem.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image022.jpg' | relative_url }})

Okno na výber objektov

Podrobnosti o modeloch [basic object definition](36_1_2d_heat_transfer_express.htm#Object_Basic_definition), [geometry](36_1_2d_heat_transfer_express.htm#Object_geometry_definition), [mesh](36_1_2d_heat_transfer_express.htm#Object_Mesh_Definition), [material](36_1_2d_heat_transfer_express.htm#Material_Definition) a [boundary condition](36_1_2d_heat_transfer_express.htm#Boundary_Condition_Definition) nájdete v bode 36.2.4. Definovanie režimu kúrenia.

### Polohovanie

Ak sa objekty nečítajú z databázy, ako je znázornené na obr. 36.2.31, používateľ musí kliknúť na tlačidlo „Umiestniť objekty“, aby objekty umiestnil podľa požiadaviek nastavenia. Ďalšie informácie o možnostiach umiestňovania nájdete v [19.Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/). Ak sa objekty čítajú z databázy, ich umiestňovanie musí byť naplánované.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image010.jpg' | relative_url }})

Nastavenia okna „Positioning Objects“ pre typ „Read from DB“ a ďalšie typy objektov

### Plánovanie polohy

Ak si používateľ nie je istý polohou objektu, ako je to v prípade objektov typu „Read From DB“, naplánované umiestňovanie pomôže objekty presne umiestniť.

Funkcia „Schedule positioning“ umožňuje používateľovi definovať umiestnenie objektov v nastaveniach MO pre nasledujúce operácie, pre ktoré sa nevytvára databáza (DB), tak, aby sa objekty umiestnili ešte pred vytvorením databázy počas spustenia simulácie v dávkovom režime. (Pozri obr. 36.2.32.)

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image011.jpg' | relative_url }})

V rozvrhu umiestnite objekty do po sebe nasledujúcich operácií

### Generovanie kontaktov medzi objektmi

Účelom vzťahov medzi objektmi je definovať, ako rôzne objekty v simulácii vzájomne interagujú. Všetky objekty, ktoré môžu prísť do kontaktu v priebehu simulácie, musia mať definovaný kontaktný vzťah. V systéme Heat Transfer Express sa automaticky definuje vzťah medzi obrobkom a formami a vlastný kontakt pre obrobok, potom sa vygeneruje kontakt, keď používateľ klikne na tlačidlo, ako je znázornené na obr. 36.2.33. Správa o vygenerovaných kontaktoch sa zobrazí na karte Správy pod grafickým oknom.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image012.jpg' | relative_url }})

Nastavenia okna na generovanie kontaktov medzi objektmi v dávkovom režime

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image013.jpg' | relative_url }})

Nastavenia okna na generovanie kontaktov medzi objektmi v interaktívnom režime (alebo pre prvý  
operácia) 

V prípade, že expresná operácia prenosu tepla prebieha postupne, systém v dávkovom režime naplánuje definovanie a generovanie kontaktov tak, že počas behu inicializuje predchádzajúce kontakty; preto nie je možné generovať a inicializovať kontaktné uzly ani obnoviť nastavenia siete, ako je znázornené na obr. 36.2.34. Používateľ môže zvoliť hodnotu tolerancie pre generovanie kontaktov výberom prepínača „Definované používateľom“.

  
Hodnotu koeficientu prenosu tepla vedením si môže užívateľ nastaviť sám; systém zároveň ponúka aj typické hodnoty, a to (pozri obr. 36.2.33.)  
(1 N/s/mm/°C alebo 0,0003 Btu/s/in²/°F) pre stav voľného pokoja  
(1 N/s/mm/°C alebo 0,0003 Btu/s/in²/°F) pre obytné priestory  
(11 N/s/mm/°C alebo 0,004 Btu/s/in²/°F) pri tvárnení

### Definícia tepelného stavu

V tomto okne je potrebné definovať tepelné podmienky, ako sú doba odpočinku (trvanie procesu), teplota okolia a konvekčný koeficient, ako je znázornené na obr. 36.2.35. Pre všetky typy ohrevu systém štandardne definuje podmienky ohrevu; používateľ musí zadať údaje o nastaveniach procesu zmenou predvolených hodnôt.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image027.jpg' | relative_url }})

Okno nastavení teplotných podmienok

Po nastavení teplotných podmienok musí používateľ definovať ovládacie prvky simulácie; podrobnosti o nastavení ovládacích prvkov simulácie nájdete v časti Definícia ovládacích prvkov simulácie.

  
Databáza Next sa musí vygenerovať v prípade interaktívnej inštalácie alebo ak ide o prvú operáciu prenosu; v opačnom prípade sa databáza vygeneruje automaticky počas simulácie. Ďalšie informácie o ovládacích prvkoch simulácie a generovaní databázy nájdete v častiach [Simuation controls Definition](36_1_2d_heat_transfer_express.htm#Simulation_controls_Definition) a [Generate Database](36_1_2d_heat_transfer_express.htm#Generate_Database).

## Pokračovanie v definovaní tvárniacich operácií

Po vykonaní operácií rýchleho prenosu tepla môže používateľ pridať operácie tvárnenia (pozri obr. 36.2.36.) a pokračovať v nastavení neizotermickej deformácie. Operácie prenosu tepla je možné pridať aj medzi operácie tvárnenia, najmä po operácii tvárnenia s prispôsobeným typom ohrevu „Heat Dwelling“, ktorý je k dispozícii pre simuláciu zdržania a je vysvetlený v nasledujúcej časti Definovanie operácie zdržania na matrici. Ďalšie informácie o nastavení operácií tvárnenia nájdete v [3D Forming Setup](/docs/en/operation_templates/33_forming/33_2_3d_forming_setup/) alebo [3D Forming Express setup](/docs/en/operation_templates/34_forming_express/34_2_3d_forming_express_setup/).

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image014.jpg' | relative_url }})

Pridanie operácie tvarovania po operácii rýchleho prenosu tepla

### Definícia prevádzky s dobou zdržania na čipoch

Operácia „Dwell on die“ (zdržanie na forme) alebo „Dwelling“ slúži na nastavenie prenosu tepla z horúceho obrobku do okolia a do formy po tvarovaní a predtým, ako sa forma stiahne z obrobku. Používateľ musí túto operáciu pridať za operácie tvarovania, ako je znázornené na obr. 36.2.37.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image015.jpg' | relative_url }})

Pridanie operácie „Expresný prenos tepla“ po operácii tvarovania v rámci operácie zdržania  
nastavenie 

V režime „Bývanie“ bude používateľ vedený nastavovacími oknami rovnako ako v režime „Kúrenie“, s výnimkou ovládacích prvkov na zastavenie kúrenia, ako je znázornené na obr. 36.2.20. Na rozdiel od režimu „Kúrenie“ je v tomto režime povolené zadávať viac ako jeden objekt a systém automaticky prenesie všetky objekty z predchádzajúceho režimu do tohto režimu. Tento režim tiež pridáva možnosti tepelného výpočtu, umiestňovania objektov a definovania vzájomných vzťahov medzi objektmi, ktoré sú potrebné na výber tepelných výpočtov pre formy, umiestnenie objektov a definovanie a generovanie podmienok kontaktu medzi objektmi. Tieto dodatočné možnosti, ktoré sa líšia od možností režimu kúrenia, sú popísané v časti 36.2.6. Definovanie režimu „Odpočinok na forme“.

### Definícia tepelného stavu

V tomto okne je potrebné definovať podmienky ohrevu, ako sú doba zdržania (trvanie procesu), teplota okolia a koeficient konvekcie, ako je znázornené na obr. 36.2.38. Pre všetky typy ohrevu systém štandardne definuje podmienky ohrevu; používateľ musí zadať údaje o nastaveniach procesu zmenou predvolených hodnôt.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image030.jpg' | relative_url }})

Okno nastavení teplotných podmienok

Po nastavení teplotných podmienok musí používateľ definovať ovládacie prvky simulácie; podrobnosti o nastavení ovládacích prvkov simulácie nájdete v časti Definícia ovládacích prvkov simulácie.

  
Databáza Next sa musí vytvoriť v prípade interaktívnej inštalácie alebo ak je operácia prenosu prvou operáciou; v opačnom prípade sa databáza vytvorí automaticky počas simulácie. Ďalšie informácie o ovládacích prvkoch simulácie a vytváraní databázy nájdete v častiach [Simuation controls Definition](36_1_2d_heat_transfer_express.htm#Simulation_controls_Definition) a [Generate Database](36_1_2d_heat_transfer_express.htm#Generate_Database).

**Súvisiace témy:**

[3D Forming Setup](/docs/en/operation_templates/33_forming/33_2_3d_forming_setup/)

[3D Forming Express Setup](/docs/en/operation_templates/34_forming_express/34_2_3d_forming_express_setup/)

[2D Heat Transfer Express Operation](/docs/en/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/)
