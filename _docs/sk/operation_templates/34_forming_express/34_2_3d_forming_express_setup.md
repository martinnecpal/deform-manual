---
lang: sk
title: "34.2. Rýchle nastavenie 3D tvarovania"
---

# 34.2. Rýchle nastavenie 3D tvarovania

34.2.1. Ako pridať operáciu Forming Express

34.2.2. Definícia nastavení procesu

34.2.3. Nastavenia výpočtu teploty

34.2.4. Výber objektov

34.2.5. Objekt – základná definícia

34.2.6. Definícia geometrie objektu

34.2.7. Definícia roviny symetrie pre obrobok

34.2.8. Definícia objektovej siete

34.2.9. Materiál

34.2.10. Okrajové podmienky

34.2.11. Ovládacie prvky pohybu

34.2.12. Polohovanie

34.2.13. Plánované umiestnenie

34.2.14. Vzťahy medzi objektmi

34.2.15. Stanovenie primárneho zdvihu matrice alebo celkovej doby spracovania

34.2.16. Ovládacie prvky na zastavenie

34.2.17. Ovládacie prvky simulácie

34.2.18. Vytvorenie databázy

## Ako pridať operáciu 3D Forming Express

Operáciu „Forming Express“ je možné spustiť dvoma spôsobmi,

  1. Vytvorenie rýchlej a nezávislej prevádzky.

  2. Spustenie operácie „Express MO Wizard“.

  3. 

****

**Na pridanie funkcie „Forming express“ s nezávislým prevádzkovaním**

Vytvorte nový problém výberom položky Súbor ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Nový problém alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 34.2.1. Zvoľte prepínač 3D Forming Express. Následne zadajte Názov úlohy, v poli Jednotky v rozbaľovacom okne Nová úloha zvoľte prepínač Systém jednotiek a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoríte novú úlohu pomocou sprievodcu Forming Express.

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image001.jpg' | relative_url }})

Pridanie samostatnej operácie 3D Forming Express.

Následne sa otvorí operácia 3D Forming Express, ako je znázornené na obr. 34.2.2.

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image002.jpg' | relative_url }})

Sprievodca Independent Forming Express.

Tu môžete pridávať alebo odstraňovať expresné operácie a simulačné operátory. Expresné operácie pre prenos tepla sú vysvetlené v časti [36\. Introduction to Heat Transfer Express.](/docs/en/operation_templates/36_heat_transfer_express/36_introduction_to_heat_transfer_express_operations/)

Fungovanie konvertora z 2D do 3D je vysvetlené v časti [44.1. 2D to 3D Convertor](/docs/en/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/)

Boolovské operácie sú vysvetlené v časti [45.1. Boolean Operator.](/docs/en/operation_templates/45_boolean_operation/45_1_boolean_operation/)

Postup kopírovania/zrkadlenia je vysvetlený v časti [46.1. Copy Mirroring](/docs/en/operation_templates/46_copy_mirroring/46_1_copy_mirroring/)

**Pridanie operácie Forming Express v sprievodcovi MO.**

Vytvorte nový problém buď výberom položky Súbor ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Nový problém, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 34.2.3. Vyberte prepínač „Integrovaný výrobný proces“ a v poli jednotiek vyberte prepínač systému jednotiek. Zadajte názov úlohy a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvorte novú úlohu s použitím metódy Deform Integrated Manufacturing Process (MO).

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image003.jpg' | relative_url }})

Spustenie sprievodcu MO

Otvorí sa sprievodca MO. Operáciu Forming Express je možné pridať v sprievodcovi MO na karte „Explorer“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky „2D Forming Express“. Operáciu Forming Express môže používateľ pridať aj pretiahnutím do editora operácií, ako je znázornené na obr. 34.2.4. Operáciu Forming Express je možné pridať aj po interaktívnych operáciách prenosu tepla alebo v dávkovom/plánovanom režime.

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image003.jpg' | relative_url }})

Do editora operácií bola pridaná operácia „3D Forming Express“

## Definícia nastavení procesu

V okne „Proces“ je potrebné pre operáciu „Tvarovanie“ nastaviť simulačné režimy, ako sú „Typ geometrie“, „Typ procesu“, „Zložitosť tvaru“ a „Presnosť“, ako je znázornené na obr. 34.2.5.

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image004.jpg' | relative_url }})

Okno nastavení procesu

**Typ geometrie**

V nástroji Forming je možné vytvoriť úplné alebo symetrické 3D geometrické modely výberom príslušných prepínačov **Celý diel** alebo **Symetria**.  
Ak je tvarovaná súčiastka asymetrická alebo je potrebné počas tvarovania analyzovať akékoľvek asymetrické správanie, musí používateľ zvoliť typ geometrického modelu **Celá súčiastka**.  
Ak je tvarovaná časť symetrická, používateľ môže zvoliť typ geometrie **Symetria** na nastavenie symetrického modelu úlohy; tým sa za oknom geometrie obrobku zobrazí okno na výber symetrických rovín. V okne symetrie musí používateľ vybrať symetrické roviny, aby sa rýchlosť pozdĺž symetrickej roviny zafixovala.

**Typ procesu**

V programe Forming Express sú k dispozícii tri typy procesov: tvárnenie za studena, tvárnenie za tepla a kovanie za tepla. Pri operácii tvárnenia za studena bude režim prenosu tepla vypnutý, takže počas simulácie nedochádza k výpočtu teploty. Pri typoch tvárnenia za tepla a kovania za tepla bude režim prenosu tepla zapnutý a aktivuje sa okno výpočtu teploty. Okno „Výpočet teploty“ (pozri obr. 34.2.5..) ponúka možnosti výberu izotermického a neizotermického nastavenia.

**Zložitosť tvaru a presnosť**

Posuvníky pre zložitosť tvaru a presnosť simulácie (pozri obr. 34.2.5.) ovplyvňujú nastavenia siete a počet časových krokov použitých v simulácii. To zase ovplyvňuje dĺžku behu a úroveň detailov dostupnú v simulácii.

**Zložitosť tvaru:**

  * **Jednoduché**: Geometria objektov je svojou povahou jednoduchá. Vyžadujú si minimálny počet prvkov, ich riešenie je jednoduchšie a trvá kratšie.

  * **Stredná**: Geometria objektov je stredne zložitá (nie príliš zložitá).

  * **Zložité**: Geometria objektov má zložitý charakter.

  
**Presnosť tvaru:**

  * **Rýchly**: Vhodný na rýchle vyhodnotenie procesu. Výmenou za rýchlejšie časy spustenia však existuje vyššie riziko, že sa prehliadnu dôležité detaily.

  * **Stredná**: Simulácia používa nastavenia, ktoré sa snažia dosiahnuť rovnováhu medzi výpočtovým časom a presnosťou.

  * **Presné**: Vykonáva sa veľmi podrobná analýza procesu, ktorá zvyčajne zachytí aj tie najmenšie detaily. Čas potrebný na výpočet a požiadavky na úložný priestor sú vyššie.

## Nastavenia výpočtu teploty

Okno „Výpočet teploty“ (pozri obr. 34.2.6.) ponúka možnosti výberu izotermického a neizotermického nastavenia. Izotermické nastavenie slúži na udržanie konštantnej teploty, zatiaľ čo neizotermické nastavenie slúži na výpočet teploty iba v obrobku alebo v obrobku a formách.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image006.jpg' | relative_url }})

Okno nastavení typu výpočtu teploty

**Izotermické**: Simulácia sa vykonáva za predpokladu konštantnej teploty. Zmeny teploty spôsobené deformáciou, ohrevom alebo výmenou tepla s okolím sa nezohľadňujú. Vhodné pre procesy, pri ktorých zmeny teploty významne neovplyvňujú výsledky simulácie. Príklady zahŕňajú: väčšinu procesov tvárnenia za studena a procesov tvárnenia za tepla, pri ktorých sa vplyv zmeny teploty z praktických dôvodov zanedbáva. V tomto nastavení nemajú matrice ani výpočet siete, ani výpočet teploty.

**  
Neizotermický**: Proces, pri ktorom teplota systému nie je konštantná. Zahrnutie výpočtov teploty zlepší predpovede toku materiálu a predpovede zaťaženia, najmä v procesoch, kde dochádza k výrazným zmenám teploty. Výpočet teploty v nástrojoch ďalej zlepšuje výpočet teploty obrobku, pretože meniaca sa teplota nástroja ovplyvňuje únik tepla z obrobku.

## **Vybrať objekty**

V tomto okne si môže používateľ v závislosti od nastavenia procesu vybrať počet objektov potrebných na vykonanie operácie (pozri obr. 34.2.7.). Používateľ musí mať na pamäti, že v simulácii môže byť len jeden plastový objekt. Je možné pridať maximálne 100 foriem.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image007.jpg' | relative_url }})

Okno na výber objektov

## Základná definícia objektu

Základná definícia objektu zahŕňa názov objektu, typ a teplotu. Okrem toho je možné pomocou tlačidla „Pokročilé“ inicializovať hodnoty premenných stavu objektu a údaje o objekte, ako sú geometria, sieť, okrajové podmienky a materiál, je možné importovať zo súboru DEFORM .DB /.Key. (Pozri obr. 34.2.8.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image008.jpg' | relative_url }})

Okno obrobku

**Názov objektu**: Používateľ môže určiť názov pre všetky objekty dostupné v danej operácii.

**Typ objektu******: Typ objektu ([OBJTYP](/docs/en/keyword_documentation/o/objtyp/)) určuje, či a ako sa modeluje deformácia pre každý jednotlivý objekt v úlohe DEFORM. V operácii Forming Express sú k dispozícii len dva typy objektov, a to plastický a tuhý, ktoré sú automaticky preddefinované podľa čísla objektu, takže obrobok bude plastický a formy budú tuhé. Ďalšie typy objektov sú vysvetlené v kapitole 11. Všeobecná definícia údajov o objektoch, podrobnosti nájdete v [11.4. Object Type](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type).

  * **Plast**: Plastové objekty sa modelujú ako tuhé plastické alebo tuhé viskoplastické materiály v závislosti od vlastností materiálov. Model predpokladá, že napätie v materiáli lineárne rastie s rýchlosťou deformácie až do prahovej hodnoty rýchlosti deformácie, označovanej ako limitná rýchlosť deformácie ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)). Po prekročení medznej rýchlosti deformácie sa materiál deformuje plasticky. Plastické správanie materiálu objektu sa špecifikuje pomocou funkcie toku napätia materiálu alebo údajov o toku napätia ([FSTRES](/docs/en/keyword_documentation/f/fstres/)). V operácii Forming Express sa obrobok automaticky priradí k typu objektu „Plast“.

  * **Tuhé**: Tuhé objekty sú modelované ako nedeformovateľné materiály. Pri analýze deformácie je geometria objektu reprezentovaná geometrickým profilom ([DIEGEO](/docs/en/keyword_documentation/d/diegeo/)). Údaje o riešení deformácie dostupné pre tuhé objekty zahŕňajú zdvih objektu, zaťaženie a rýchlosť. Geometrický profil sa používa pre všetky analýzy deformácie a sieť pre tuhý objekt sa používa pre všetky výpočty tepelné, transformačné a difúzne. V programe Forming Express sa lisovacie formy alebo nástroje automaticky priraďujú k kategórii „Tuhé“, keďže ide o nedeformovateľné objekty.

**Poznámka:**

Je potrebné poznamenať, že typ objektu je v programe Forming Express preddefinovaný číslom objektu.

Na stránke „Objekt“ sa nachádza tlačidlo „Importovať objekt“. Slúži na import kompletných údajov o objekte z iného súboru DEFORM.

**Teplota objektu**: Používateľ môže nastaviť teplotu objektu v poli „Teplota“ v príslušnom okne objektu, ako je znázornené na obr. 34.2.8.

  
**Pokročilé nastavenia objektu**: Pokročilé nastavenia v časti „Možnosti inicializácie“ (pozri obr. 34.2.9.) sa zídu v prípade, že používateľ importuje objekt z predchádzajúceho projektu alebo úlohy, alebo ak sa operácia „express“ pridá až po niekoľkých iných operáciách a je potrebné inicializovať niekoľko dôležitých stavových premenných.

Pomocou pokročilých nastavení môže používateľ inicializovať teplotu, deformáciu, rýchlosť, poškodenie a posunutie, ku ktorým došlo v deformovateľnom objekte. (Pozri obr. 34.2.9.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image005.jpg' | relative_url }})

Pokročilé nastavenia objektov

V operácii „Formovanie“ je možné inicializovať ďalšie premenné; podrobnosti nájdete v [19\. Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/).

  
Priemerná rýchlosť deformácie ([AVGSTR](/docs/en/keyword_documentation/a/avgstr/)) je charakteristická priemerná hodnota efektívnej rýchlosti deformácie. Na začiatku simulácie by sa mala zadať aproximácia tejto hodnoty.

Medzná rýchlosť deformácie ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)) definuje medznú hodnotu efektívnej rýchlosti deformácie, pod ktorou sa plastický alebo porézny materiál považuje za tuhý a správa sa ako materiál s newtonovskými vlastnosťami.

![]({{ '/assets/icons/pre_icons/mo_reset_button.jpg' | relative_url }}) : Pomocou tejto funkcie môže používateľ obnoviť hodnoty premenných v počiatočnom stave.

Ďalšie možnosti vlastností objektu deformácie, ktoré sú k dispozícii v operácii tvarovania, nájdete v [16.1. Deformation Properties.](/docs/en/pre_processor/16_object_properties/16_1_deformation_properties/)

## Definícia geometrie objektu

Okno „Geometria“ slúži na vytvorenie geometrie objektu, ako je znázornené na obr. 34.2.10. Pred vytvorením geometrie je k dispozícii iba možnosť „Definovať primitívnu geometriu“, avšak po jej vytvorení sa aktivujú možnosti „Skontrolovať“, „Zmenšiť“, „Obrátiť“, „Opraviť“ a „Označiť“ geometriu povrchu a po vygenerovaní siete sa aktivuje možnosť „Extrahovať zo siete“.

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image006.jpg' | relative_url }})

Okno s definíciou geometrie

**Definícia primitívu ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) **

V rámci geometrických primitív existujú tri základné tvary, ako sú Krabica, Valec a Dutý valec, ktoré možno použiť na vytvorenie geometrií, ako je znázornené na obr. 34.2.11. V každom prípade musí používateľ prispôsobiť rozmery tak, aby zodpovedali danej úlohe. Okrem týchto primitív je možné použiť funkcie Extrude a Revolve na prevod 2D priečneho rezu na 3D. Objekty s rotačnou symetriou sa vytvárajú pomocou možnosti uhla otáčania pre primitíva Cylinder, Hollow Cylinder a Revolve.

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image007.jpg' | relative_url }})

Okno s geometrickými primitívami pre typ 3D geometrie

**Check![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})**

Vždy skontrolujte geometriu. Program DEFORM disponuje kontrolným algoritmom, ktorý overuje počet neplatných hrán, neplatnú orientáciu, mnohouholníky s malou plochou a počet plôch. Nie je možné odhaliť všetky typy chýb.

Použitím tejto možnosti „Skontrolovať geometriu“ sa otvorí okno „Výsledky kontroly geometrie“, ktoré obsahuje prehľad geometrie objektu (pozri obr. 34.2.12.). V prípade objektu s uzavretým objemom by mala byť prítomná 1 plocha, 0 voľných hrán a 0 neplatných entít (ako je označené kružnicou nižšie na obr. 34.2.12.). Objekty, ktoré sú importované ako plochy a nie ako telesa, budú mať voľnú hranu, ale aj tak by mali mať len 1 plochu.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image011.jpg' | relative_url }})

Výsledky kontroly geometrie

**Scale![]({{ '/assets/icons/pre_icons/mo_scale_label.jpg' | relative_url }}) **

Geometriu je možné pri tvárnení zmeniť tak, aby zohľadňovala teplotnú rozťažnosť, a to stanovením zväčšovacieho koeficientu. (Pozri obr. 34.2.13.) Zväčšovací koeficient je možné vypočítať na základe teplotného rozdielu a údajov o materiáli závislých od teploty. Zmenenú geometriu je možné uložiť v rôznych formátoch na ukladanie geometrie.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image014.jpg' | relative_url }})

Okno „Scale Geo“

**Späť**![]({{ '/assets/icons/pre_icons/mo_reverse_label.jpg' | relative_url }})

Táto funkcia obráti smer povrchu/normály geometrie. Povrch/normála geometrie by mali byť vždy smerované von.

**Oprava** ![]({{ '/assets/icons/pre_icons/mo_fix_label.jpg' | relative_url }})

Táto funkcia rieši geometrické problémy, pri ktorých sa vyskytujú buď viaceré plochy, alebo otvorené oblasti (diery), a to odstránením všetkých nadbytočných plôch a vyplnením dier. Pri menších alebo ohraničených problémoch to funguje dobre. V prípade zložitejších súborov, ako je tento, však oprava nemusí priniesť požadovaný výsledok. (Pozri obr. 34.2.14.)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image016.jpg' | relative_url }})

Určenie geometrie formy na kľukový hriadeľ

**Označiť povrch**

Označením akéhokoľvek povrchu sa tento povrch vylúči z výpočtov kontaktov počas simulácie. Aj keby sa obrobok s týmto objektom dostal do kontaktu, táto funkcia sa zvyčajne používa pre povrchy lisovacích foriem a razníkov, kde v reálnych podmienkach nedochádza k vytváraniu kontaktov, aby sa zabránilo nežiaducim výpočtom kontaktov.

**Ďalšie možnosti geometrie**

  * **Zobraziť geometriu vnútri značky**: Zaškrtnutím tejto možnosti sa aktivuje zobrazenie normál povrchov geometrie  
zobrazenie. 

  * **Určiť referenčný bod**: Používateľ môže vybrať referenčný bod geometrie kliknutím na toto tlačidlo v zobrazovacom okne. Tento referenčný bod je potrebný na určenie vzdialenosti medzi objektmi pomocou ovládacích prvkov na zastavenie.

  * **Import geometrie zo súboru** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) : Pomocou tejto možnosti môže používateľ importovať geometriu zo súboru.

  * **Načítať geometriu z knižnice** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ importovať geometriu z knižnice.

  * **Uloženie geometrie do súboru** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}): Uloží geometriu do súboru.

  * **Uložiť geometriu do knižnice** ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ uložiť geometriu do knižnice.

  * **Odstrániť geometriu** ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ odstrániť geometriu.

## Definícia roviny symetrie pre obrobok

Okno „Symetria“ sa zobrazí po okne „Geometria“, ak používateľ vyberie typ geometrie „Symetria“. Symetriu je potrebné definovať s cieľom zafixovať rýchlosť uzlov na symetrických rovinách, ako je znázornené na obr. 34.2.15. Najskôr musí používateľ vybrať rovinu symetrie kliknutím ľavým tlačidlom myši; vybraná rovina sa zafarbí na zeleno. Následne kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridá vybranú rovinu; v prípade viac ako jednej roviny symetrie zopakujte rovnaké kroky. Pre vybranú rovinu systém zobrazí stred a normálu, ako je znázornené na obr. 34.2.15.

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image008.jpg' | relative_url }})

Okno s definíciou roviny symetrie

## Definícia objektovej siete

Okno „Vytvorenie siete“ umožňuje používateľovi vytvoriť sieť pre aktuálny objekt. Na obr. 34.2.16 je zobrazené okno „Vytvorenie siete“ v systémovom režime. V tomto režime systém automaticky nastaví počet prvkov siete na základe zložitosti tvaru a výberu nastavenia presnosti v pracovnom okne.

**Režim systému**

Používateľ musí pre objekty vytvoriť sieť tetraédrov. Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_mesh_preview_button.jpg' | relative_url }}) môže používateľ rýchlo vygenerovať povrchovú sieť alebo si prezrieť náhľad siete ešte pred vytvorením objemovej siete potrebnej pre daný objekt. Akonáhle je používateľ spokojný s náhľadom povrchovej siete, môže sieť na objekte vygenerovať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).  
Po vytvorení siete sa aktivuje tlačidlo „Odstrániť sieť“, ktoré slúži na odstránenie aktuálnej siete objektu. Ak chce používateľ zmeniť automaticky vypočítaný počet prvkov alebo upraviť pokročilé nastavenia, musí prejsť do režimu „Definované používateľom“.

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image009.jpg' | relative_url }})

Okno nastavení siete v režime Systém

**Režim definovaný používateľom**

Možnosť režimu užívateľsky definovanej siete je znázornená na obr. 34.2.17. V tomto režime môže užívateľ meniť počet prvkov posúvaním posuvníka a pomocou pokročilých možností upravovať pomer veľkostí, minimálnu veľkosť prvkov, kritériá pregenerovania siete a boolovské operácie. Používateľ môže vygenerovať povrchovú sieť a prezrieť si jej náhľad. Akonáhle je s povrchovou sieťou spokojný, môže vygenerovať objemovú sieť pre 3D objekt kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_solid_mesh_button.jpg' | relative_url }}).

**Počet prvkov (MGNELM):**

Počet prvkov siete predstavuje približný počet prvkov, ktoré systém vygeneruje. Automatický generátor siete (AMG) preberá hodnotu z poľa MGNELM a vygeneruje sieť, ktorá bude obsahovať približne rovnaký počet prvkov. Počet prvkov je možné určiť jednoduchým posunutím posuvníka a výberom vhodnej hodnoty pre aktuálnu simuláciu.

Rozdiel medzi počtom zadaných prvkov a počtom vygenerovaných prvkov sa zvyčajne pohybuje okolo desiatich percent. Ak chce používateľ zmeniť ďalšie nastavenia siete, musí kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_advanced_button.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image010.jpg' | relative_url }})

Nastavenia siete v užívateľsky definovanom režime

**Pokročilé nastavenia siete**

  * **Všeobecné nastavenia siete**: V programe DEFORM existujú dva rôzne typy sietí, ktoré je možné vytvoriť pre 3D objekty.

  * **Relatívna sieť**: Pri použití nastavenia relatívnej siete používateľ určí počet pevných prvkov, ktoré sa majú vygenerovať. Bez ohľadu na to, aký zložitý bude tvar dielu, počet prvkov zostane v podstate konštantný. (Obr. 34.2.18.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image011.jpg' | relative_url }})

Nastavenia relatívnej veľkosti siete

  * **Absolútna sieť**: Pri použití nastavenia absolútnej siete používateľ určí veľkosť prvkov a systém na základe zadaných rozmerov prvkov a geometrie určí celkový počet potrebných prvkov. S rastúcou zložitosťou dielu sa počet prvkov zvyčajne zvyšuje. (Obr. 34.2.19.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image012.jpg' | relative_url }})

Nastavenia absolútnej siete

  * **Pomer veľkostí prvkov (MGSIZR):** Maximálny pomer veľkostí medzi prvkami je jedným z viacerých spôsobov, ako regulovať hustotu siete počas automatického generovania siete (AMG) prostredníctvom špecifikácie pomeru hustôt uzlov. Pri hodnote 3 pre [MGSIZR](/docs/en/keyword_documentation/m/mgsizr/) bude najväčšia hrana prvku na objekte približne 3-krát väčšia ako najmenšia hrana prvku na tom istom objekte. Ak sa požadujú prvky rovnakej veľkosti, pomer veľkostí je 1. Ak je pomer veľkostí 0, pomer veľkostí prvkov nebude mať vplyv na rozloženie hustoty siete.

  * **Kritériá pregenerovania siete:** Kritériá pregenerovania siete (Autoremesh) predstavujú najpohodlnejší spôsob, ako riešiť pregenerovanie siete objektov, ktoré prechádzajú veľkou plastickou deformáciou. Okno Kritériá pre vytváranie novej siete (pozri obr. 34.2.19.) obsahuje skupinu parametrov, ktoré na základe priradenia určitých spúšťačov riadia, kedy a ako často sa bude sieť na objektu so sieťou regenerovať. Existujú štyri kľúčové slová, ktoré riadia spustenie postupu premenovania siete pre objekt: Hĺbka interferencie ([RMDPTH](/docs/en/keyword_documentation/r/rmdpth/)), Max. časový prírastok ([RMTIME](/docs/en/keyword_documentation/r/rmtime/)), Max. krokový prírastok ([RMSTEP](/docs/en/keyword_documentation/r/rmstep/)) a Max. prírastok zdvihu ([RMSTRK](/docs/en/keyword_documentation/r/rmstrk/)). Keď sú splnené kritériá pregenerovania siete pre ktorékoľvek z týchto kľúčových slov alebo sa sieť stane nepoužiteľnou (záporná jacobiánska matica), objekt sa pregeneruje, informácie o riešení zo starej siete sa interpolujú na novú sieť a simulácia pokračuje.

  * **Vzdialenosť penetrácie (relatívna)**: Ak zadáte záporné číslo (zlomok), program vykoná kontrolu na každej hrane povrchu, ktorá má na oboch koncoch kontaktný uzol. Vypočíta sa vzdialenosť od stredu hrany k povrchu formy a vydelí sa pôvodnou dĺžkou hrany. Ak tento pomer prekročí veľkosť zadaného hodnoty, spustí sa prepočítanie siete.

  * **Maximálny prírastok zdvihu (RMSTRK)**: Vždy, keď prírastok zdvihu primárnej matrice od posledného kroku premenovania siete prekročí maximálny prírastok zdvihu ([RMSTRK](/docs/en/keyword_documentation/r/rmstrk/)), spustí sa nový krok premenovania siete. 

  * **Maximálny časový interval (RMTIME):** Vždy, keď uplynie maximálny časový interval ([RMTIME](/docs/en/keyword_documentation/r/rmtime/)) (hodnota uplynutého času) od posledného kroku premenovania siete, spustí sa nový krok premenovania siete.

  * **Maximálny prírastok kroku (RMSTEP):** Vždy, keď od posledného kroku premenovania siete dôjde k dosiahnutiu maximálneho prírastku kroku (počet krokov), spustí sa nový krok premenovania siete.

**Odstrániť sieť** ![]({{ '/assets/icons/pre_icons/mo_delete_mesh_button.jpg' | relative_url }}) : Odstráni sieť vytvorenú pre daný objekt.

Na rozdiel od operácie „Forming“ nie sú v operácii „Forming Express“ k dispozícii ďalšie možnosti siete, ako napríklad „Coating mesh“, „System mesh density weighting factors“ a „User Mesh Density Window“; informácie o týchto možnostiach nájdete v [13.2. 3D Tet Mesh Generation.](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/).

## Materiál

Na obr. 34.2.20. je zobrazené okno s materiálmi. Používateľ môže pridať alebo importovať materiál zo súboru kľúčových slov alebo ho načítať z knižnice materiálov programu DEFORM.

  
Po načítaní systém automaticky priradí načítaný materiál k objektu. Používateľ môže tiež upravovať plastické a tepelné vlastnosti, a to napätie pri tečení, tepelnú vodivosť, tepelnú kapacitu, hustotu a emisivitu, a to pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image013.jpg' | relative_url }})

Okno s materiálmi

Po pridaní materiálu kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) – otvorí sa okno s materiálom, ako je znázornené na obr. 34.2.21.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image022.jpg' | relative_url }})

Okno na úpravu materiálu

Požadované vlastnosti závisia od fyzikálnych javov simulovaných v programe DEFORM. Vlastnosti materiálov, ktoré musí používateľ zadať, závisia od typov materiálov, ktoré používateľ v simulácii využíva. V kapitole [10\. Material Data](/docs/en/pre_processor/10_material_data/10_material_data/) má používateľ prístup ku všetkým vlastnostiam materiálov; ďalšie informácie nájdete v kapitole [10\. Material Data](/docs/en/pre_processor/10_material_data/10_material_data/).

## Okrajové podmienky

V okne „Forming express Boundary conditions“ môže používateľ objektu priradiť iba okrajové podmienky typu „Rovinná symetria“, „Rýchlosť deformácie“, „Teplotná výmena s okolím“ a „Teplota“. Okrajové podmienky určujú, ako hranica objektu interaguje s inými objektmi a s okolím. Najčastejšie používanými okrajovými podmienkami sú výmena tepla s okolím pri simuláciách zahŕňajúcich prenos tepla a predpísaná rovina symetrie na vynútenie symetrie v modeli. Obr. 34.2.22 znázorňuje rôzne okrajové podmienky, ktoré je možné priradiť k objektu.  
V predvolenom nastavení sa k objektu obrobku pridajú rovinné symetrické roviny podľa výberu symetrických rovín v okne symetrie, ako je znázornené na obr. 34.2.22, a zároveň sa všetkým povrchom s výnimkou symetrických rovín priradí výmena tepla s okolím pre proces teplého a horúceho kovania, ako je znázornené na obr. 34.2.23.

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image014.jpg' | relative_url }})

Pre obrobok bola nastavená okrajová podmienka symetrie

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image015.jpg' | relative_url }})

Pre obrobok bola stanovená okrajová podmienka výmeny tepla s okolím

BCC sú rozdelené do kategórií [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/), [Thermal](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/), [Diffusion](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/) a [Heating](/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/). Ďalšie informácie o týchto BCC nájdete v [14\. Boundary Conditions.](../../pre_processor/14_boundary_conditions).

## Ovládanie pohybu

Ovládacie prvky pohybu je možné aplikovať na tuhé objekty a hraničné uzly objektov s sieťou. Povrch vymedzený týmito uzlami možno považovať za „tuhý povrch“. Počas simulácie sa obmedzené uzly budú pohybovať synchronizovane rýchlosťou a smerom definovanými ovládacími prvkami pohybu. V operácii Forming express je k dispozícii iba typ posuvného pohybu, rotačný pohyb je k dispozícii v operácii Forming. Podrobnejšie informácie nájdete v [34.1.10. Movement Controls.](34_1_2d_forming_express_setup.htm#34_1_10_Movement_Controls).

**Translačný pohyb:**

Počas simulácie sa viazané uzly budú pohybovať synchronizovane rýchlosťou a smerom, ktoré sú definované ovládacími prvkami pohybu. (Pozri obr. 34.2.24.)

V funkcii Forming Express je v rámci typu pohybu „Translation“ k dispozícii len šesť typov ovládacích prvkov pohybu, a to [Speed](/docs/en/pre_processor/15_movement_controls_definition/15_1_speed/), [Load](/docs/en/pre_processor/15_movement_controls_definition/15_2_force/), [Hammer](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/), [Screw press](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/), [Mechanical press](/docs/en/pre_processor/15_movement_controls_definition/15_5_mechanical_press/) a [Hydraulic press](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/). Operácia tvarovania obsahuje okrem ovládacích prvkov pre pohyb „Forming Express“ aj ovládacie prvky pre translačný pohyb [Sliding Die](/docs/en/pre_processor/15_movement_controls_definition/15_7_sliding_die/) a [Path](/docs/en/pre_processor/15_movement_controls_definition/15_8_path/), ako aj typy rotačného a torzného pohybu. Ďalšie informácie nájdete v [15\. Movement Controls.](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/).

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image016.jpg' | relative_url }})

Okno na ovládanie translačného pohybu

V dolnej časti okna na riadenie pohybov (pozri obr. 34.2.24.) môže používateľ importovať špecifikácie pohybov z iných súborov kľúčových slov alebo databázových súborov, načítať informácie o lise z knižnice, uložiť nastavenia pohybov do súboru alebo do knižnice pohybov, prezrieť si náhľad a odstrániť definíciu pohybu. Ďalšie informácie o všetkých pohyboch dostupných v programe Forming Express nájdete v referenčnom manuáli [ 34.1.10. Movement Controls.](34_1_2d_forming_express_setup.htm#34_1_10_Movement_Controls).

## Polohovanie

Na obr. 34.2.25. je zobrazené okno na nastavenie polohy.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image033.jpg' | relative_url }})

Okno na nastavenie polohy

**Automatické polohovanie** ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }})

Kliknutím na toto tlačidlo systém automaticky umiestni objekty vzhľadom na smer pohybu hornej matrice; táto možnosť sa najlepšie hodí pre jednoduché nastavenie s tromi objektmi: obrobkom, hornou matricou a spodnou matricou.

Ak sa ako typ riadenia pohybu primárnej matrice používa mechanický lis, potom sa vykoná automatické polohovanie  
prebieha v dvoch krokoch:

  1. Poloha spodnej matrice voči obrobku pri spojení s hornou matricou bez úpravy zdvihu

  2. Poloha, v ktorej horná matrica zasahuje do obrobku pri aktualizácii zdvihu.

Systém vždy aktualizuje zdvih podľa polohy objektu, pre ktorý je definovaný mechanický lis (horná matrica). Zaškrtávacie políčko „Aktualizovať zdvih“ by malo byť v rýchlych operáciách skryté.

**Umiestňovanie objektov ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }})**

Kliknutím na toto tlačidlo môže používateľ umiestniť objekty do požadovaných smerov. K dispozícii sú rôzne typy možností umiestnenia, ako napríklad [Drag](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_1_Drag_Positioning), [Offset](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_2_Offset_Positioning), [Interference](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_3_Interference_positioning), [Flip](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_6_Flip_positioning) a [Rotational](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_4_Rotational_positioning), ako je znázornené na obr. 34.2.26. Ďalšie informácie o týchto možnostiach nájdete v časti [19.Object Positioning.](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image017.jpg' | relative_url }})

Okno na umiestňovanie objektov

## Plánované polohovanie

Ak si používateľ nie je istý polohou objektu, ako je to v prípade objektov typu „Read From DB“, naplánované umiestňovanie pomôže objekty presne umiestniť.

Funkcia „Schedule positioning“ umožňuje používateľovi definovať umiestnenie objektov v nastavení MO pre nasledujúce operácie, pre ktoré sa nevytvára databáza (DB), tak, aby sa objekty umiestnili ešte pred vytvorením databázy počas spustenia simulácie v dávkovom režime. (Pozri obr. 34.2.27.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image018.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

## Vzťahy medzi objektmi

Účelom vzťahov medzi objektmi je definovať, ako rôzne objekty v simulácii vzájomne interagujú. Všetky objekty, ktoré sa v priebehu simulácie môžu navzájom dotýkať, musia mať definovaný kontaktný vzťah. V systéme Forming Express sa automaticky definuje vzťah medzi obrobkom a formami a vlastný kontakt pre obrobok, potom sa vygeneruje kontakt, keď používateľ klikne na ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}), ako je znázornené na obr. 34.2.28. Správa o vygenerovaných kontaktoch sa zobrazí na karte Správy pod grafickým oknom.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image036.jpg' | relative_url }})

Okno na generovanie kontaktov

Používateľ si môže zvoliť typ trenia – šmykové alebo Coulombovo – a nastaviť koeficient trenia. Mazivo použité na nástroji má veľký vplyv na veľkosť trenia medzi nástrojom a obrobkom. Trenie zase ovplyvňuje tok kovu na kontaktných plochách.

  
Systém poskytuje typické hodnoty trenia pri šmyku pomocou roletového menu; tieto hodnoty sú uvedené nižšie,

(0,08) pre procesy tvárnenia za studena (karbidové matrice)

(0,12) pre procesy tvárnenia za studena (oceľové formy)

(0,25) pre procesy tepelného tvárnenia

(0,3) pre procesy mazaného kovania za tepla

(0,7) pre procesy horúceho kovania bez mazania (nasucho)

(0,4) pre procesy tvárnenia hliníka

Hodnotu koeficientu prenosu tepla vedením si môže užívateľ nastaviť sám; systém zároveň ponúka aj typické hodnoty, a to:

(1 N/s/mm/°C alebo 0,0003 Btu/s/in²/°F) pre stav voľného pokoja

(1 N/s/mm/°C alebo 0,0003 Btu/s/in²/°F) pre obytné priestory

(11 N/s/mm/°C alebo 0,004 Btu/s/in²/°F) pri tvárnení

## Stanovenie primárneho zdvihu matrice alebo celkovej doby spracovania

  
Primárny zdvih formy (pozri obr. 34.2.29.) určuje celkovú dĺžku pohybu formy počas operácie. Ide o odhad celkového zdvihu formy v rámci jednej operácie. Používa sa na stanovenie hodnôt časových krokov.

Ak nie je zaškrtnuté políčko „presná hodnota“, približný cieľový posun nástroja bude predstavovať približne 125 % zadaného hodnoty.

Pomocou kurzora myši môže používateľ určiť hodnotu primárneho zdvihu výseku výberom dvoch bodov na objektoch.

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image019.jpg' | relative_url }})

Okno s definíciou celkového zdvihu primárneho lisovacieho nástroja

Ak používateľ použije možnosť „Načítať“ ako ovládací prvok pohybu, namiesto okna „Primárny zdvih matrice“ sa zobrazí okno „Celkový čas spracovania“; tento čas sa používa na odhad hodnôt krokovania.

**Základný zdvih matrice pre mechanický lis [metóda presného tvárnenia]:**

V prípade mechanického lisu sa zobrazí platný rozsah. (0 ~ „Celkový zdvih“) (Pozri obr. 34.2.30.)

Ak je celkový primárny zdvih matice rovný 0 alebo sa nachádza mimo povoleného rozsahu, vstup je neplatný a rozsah sa zobrazí červenou farbou.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image039.jpg' | relative_url }}) ![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image040.jpg' | relative_url }})

(a) V prvej operácii (b) V nasledujúcej operácii 

Možnosť základného zdvihu lisovacej matrice s metódou zdvihu Exact Forming 

Existujú 3 spôsoby, ako určiť presný zdvih formovania:

  1. Používateľ môže zadať presný tvarovací zdvih pre celkový primárny posun formy.

  2. Ak je aktuálna poloha matrice v hornej mŕtvej polohe, používateľ môže stlačiť tlačidlo **Poloha hornej mŕtvej polohy** (nástroj ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }})) alebo túto polohu skontrolovať v nasledujúcej operácii. Keď používateľ stlačí tlačidlo / skontroluje polohu hornej mŕtvej polohy (nástroj ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }})), v nasledujúcich operáciách sa odznačí políčko „Presná hodnota“. Tvarovací zdvih je nastavený na hodnotu rovnú celkovému zdvihu. Vykonáva sa alebo je naplánované automatické polohovanie. V prvej operácii sa primárny posun matrice aktualizuje na správny tvarovací zdvih. V nasledujúcich operáciách sa tvarovací zdvih aktualizuje po vykonaní naplánovaného polohovania.

| Prvá operácia | Ďalšia operácia | Editor krokov  
---|---|---|---  
Je definovaná horná matrica | Horná matrica je načítaná z databázy  
**Celkový posuv primárneho lisovacieho nástroja** | Zobrazuje vypočítaný tvarovací zdvih | Približný posuv lisovacieho nástroja, ktorý sa použije na výpočet DSMAX | N/A | N/A  
  
Ak sa v prvej operácii použije tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}), deaktivujte tlačidlá ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) pre hornú aj dolnú mŕtvu polohu, kým používateľ znovu nenavštívi stránku. Ak sa v nasledujúcej operácii zaškrtne políčko v sprievodcovi, systém vymaže všetky predchádzajúce naplánované polohy objektov 2 a 3.

  1. Ak je aktuálna poloha matrice v dolnej mŕtvej polohe, používateľ môže stlačiť tlačidlo **Dolná mŕtva poloha** (![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }})) alebo skontrolovať polohu dolnej mŕtvej polohy v nasledujúcej operácii. Ak používateľ stlačí tlačidlo / skontroluje polohu hornej mŕtvej polohy (![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }})), v nasledujúcich operáciách sa odznačí políčko „Presná hodnota“. Tvarovací zdvih je nastavený na hodnotu 0. Vykoná sa alebo naplánuje automatické polohovanie. Prvá operácia aktualizuje hodnotu primárneho posunu matrice o správny tvarovací zdvih. V nasledujúcej operácii sa vypočíta správny tvarovací zdvih po vykonaní naplánovaného polohovania.

| Prvá operácia | Ďalšia operácia | Editor krokov  
---|---|---|---  
Je definovaná horná matrica | Horná matrica sa načíta z databázy  
**Celkový zdvih primárneho lisovacieho nástroja** | Zobrazuje vypočítaný tvarovací zdvih | Približný zdvih lisovacieho nástroja, ktorý sa použije na výpočet DSMAX | N/A | N/A  
  
Ak sa pri prvej operácii použije ktorékoľvek z tlačidiel „Horná mŕtva poloha“ alebo „Spodná mŕtva poloha“ (![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }})), obe tlačidlá „Horná mŕtva poloha“ a „Spodná mŕtva poloha“ (![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }})) zostanú deaktivované, kým používateľ stránku znovu nenavštívi. 

**V nasledujúcich krokoch:**

Ak je zaškrtnuté políčko pre hornú alebo dolnú úvrati, systém vymaže naplánované polohovanie objektov 2 a 3.  
Ak je zaškrtnuté políčko BDC, zobrazí sa chybová správa o tom, že pre hornú matricu nie je naplánované polohovanie s ohľadom na interferenciu.  
Ak nie je zaškrtnuté políčko BDC, zobrazí sa varovná správa, že pre hornú matricu nie je naplánované polohovanie s ohľadom na interferenciu.

**Základný zdvih lisovacej formy pre mechanický lis [metóda merania vzdialenosti medzi formami]:**

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image041.jpg' | relative_url }}) ![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image042.jpg' | relative_url }})

(a) V prvej operácii (b) V nasledujúcej operácii 

Možnosť primárneho zdvihu matrice s metódou „Vzdialenosť medzi matricami“ v prvej operácii

Ak používateľ zvolí ako typ tvárneho zdvihu metódu „Vzdialenosť medzi maticami“, potom,

V prvej operácii bude posuv **celého primárneho lisovacieho nástroja** deaktivovaný a nastavený systémom.

V časti „Ďalšie operácie“ bude políčko **Presná suma** odškrtnuté a deaktivované. 

V nasledujúcich operáciách sa **celkový posun primárnej matrice** použije výlučne na výpočet veľkosti kroku definovanej systémom.

V ďalšom kroku je možné nastaviť presné ovládacie prvky zastavenia.

## Ovládacie prvky na zastavenie

Parametre ukončenia určujú čas, po uplynutí ktorého sa simulácia ukončí. Simuláciu je možné ukončiť na základe maximálneho počtu simulovaných časových krokov, maximálneho zdvihu, maximálneho zaťaženia primárnej matrice, pomeru kontaktu k celkovej ploche alebo vzdialenosti medzi matricami. Simulácia sa zastaví, keď bude splnená podmienka ktoréhokoľvek z týchto parametrov ukončenia. (Pozri obr. 34.2.32.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image020.jpg' | relative_url }})

Okno ovládacích prvkov zastavenia

Ďalšie informácie o kontrolách zabraňujúcich deformácii nájdete v [34.1.15. Stopping Controls.](34_1_2d_forming_express_setup.htm#34_1_15_Stopping_controls)

## Ovládacie prvky simulácie

Systém DEFORM rieši časovo závislé nelineárne úlohy generovaním série riešení metódou konečných prvkov (FEM) v diskrétnych časových krokoch. V každom časovom kroku sa rýchlosti, teploty a ďalšie kľúčové premenné každého uzla v sieti konečných prvkov určujú na základe okrajových podmienok, termomechanických vlastností materiálov obrobku a prípadne riešení z predchádzajúcich krokov. Ostatné stavové premenné sa odvodzujú z týchto kľúčových hodnôt a aktualizujú sa pri každom časovom kroku. Dĺžka tohto časového kroku a počet simulovaných krokov sa určujú na základe informácií zadaných v ponuke nastavení krokov. Obr. 34.2.33. znázorňuje možnosti ovládania simulácie.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image047.jpg' | relative_url }})

Okno ovládacích prvkov simulácie v systémovom režime

Používateľ musí zadať číslo počiatočného kroku, celkový počet krokov, veľkosť kroku, ktorú chce uložiť, a definíciu kroku (posun formy alebo časový prírastok). V programe Forming Express je možné ako definíciu kroku použiť iba konštantný posun formy a konštantný časový prírastok. Pre všetky ovládacie prvky pohybu okrem zaťaženia sú ako typy definície kroku k dispozícii posun formy aj časový prírastok, pre ovládacie prvky pohybu zaťaženia je povolený iba časový prírastok.

**Typ systému: Krok – konštantný posun matrice:**

V prípade mechanického lisu sa pri tvárnení rýchlosť kroku vypočíta podľa vzorca [(celkový primárny zdvih matrice) / (počet krokov)] × 1,2, a to bez ohľadu na to, či je zaškrtnutá možnosť „presná hodnota“ alebo nie.  
Pri nemekanických lisovacích operáciách pri tvárnení sa veľkosť kroku rýchleho posuvu vypočíta ako [(celkový primárny zdvih matrice) / (počet krokov)], ak je zaškrtnutá možnosť „presná hodnota“ (pozri obr. 34.2.34.).  
V prípade nemekanických lisovacích operácií pri tvárnení sa rýchlosť kroku vypočíta podľa vzorca [(celkový primárny zdvih lisovacej formy) / (počet krokov)] × 1,2, ak nie je zadaná presná hodnota.

U**typ kroku – konštantný posun matrice:** Táto funkcia umožní používateľom zadať vlastnú veľkosť kroku. Používateľ by mal zvoliť vhodnú veľkosť kroku tak, aby na základe počtu krokov splnil podmienku zastavenia.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image048.jpg' | relative_url }})

Okno ovládacích prvkov simulácie v užívateľskom režime

**Počet simulačných krokov (NSTEP)**

Parameter „Počet simulačných krokov“ určuje počet krokov, ktoré sa majú spustiť od počiatočného čísla kroku. Simulácia sa zastaví po vykonaní tohto počtu simulačných krokov, pokiaľ sa nespustí riadiaci signál na zastavenie simulácie alebo ak simulácia nenarazí na problém. Napríklad, ak je počiatočné číslo kroku -35 (NSTART) a je špecifikovaných 30 krokov (NSTEP), simulácia sa zastaví po 65. kroku, pokiaľ sa skôr nespustí iný príkaz na zastavenie.

**Krok pri ukladaní (STPINC)**

Hodnota krokového prírastku (STPINC), ktorá sa ukladá do databázy, určuje počet krokov, ktoré systém uloží do databázy. Pri spustení simulácie sa musí vypočítať každý krok, ale nemusí sa nutne ukladať do databázy. Uložením väčšieho počtu krokov sa zachová viac informácií o procese, čo však bude vyžadovať väčší úložný priestor.

**Ovládanie krokového prírastku (DSMAX/DTMAX)**

Veľkosť kroku riešenia je možné riadiť časovým krokom alebo posunom primárnej matrice. Ak je špecifikovaný zdvih na krok, primárna matrica sa v každom časovom kroku posunie o zadanú hodnotu. Celkový posun primárnej matrice bude rovný posunu na krok vynásobenému celkovým počtom krokov. Ak je zadaný čas na krok, použije sa časový interval na krok. Posun matrice na krok bude rovný časovému kroku vynásobenému rýchlosťou matrice.

Počet zdvihov na krok je často intuitívnejší. Čas na krok je však potrebné určiť pri každej úlohe, v ktorej nedochádza k pohybu matice (napríklad pri prenose tepla), alebo pri každej úlohe, kde sa používa regulácia sily.

V operáciách tvárnenia je k dispozícii vylepšené nastavenie riadenia krokového posunu, ktoré teraz zahŕňa krokové funkcie závislé ako od času, tak aj od zdvihu. To znamená, že veľkosť kroku (či už ide o čas na krok alebo zdvih na krok) je teraz možné definovať ako funkciu času alebo zdvihu. Táto funkcia umožňuje v prípade potreby dosiahnuť jemnejšie rozlíšenie uložených informácií o modeli. (typicky ku koncu zdvihu, kde môžu nastať prudké zmeny zaťaženia lisovacej formy a plnenia dutiny alebo tvorby otrepov) – ďalšie informácie nájdete v dokumente [9.2. Defining step.](/docs/en/pre_processor/9_simulation_controls/9_2_defining_step/)

**Pokročilé ovládacie prvky simulácie**

Pokročilé ovládacie prvky simulácie ponúkajú možnosti výberu riešiteľov deformácií; k nim sa dostanete pomocou tlačidla. V prípade 3D Forming Express sú k dispozícii iba riešitelia konjugovaných gradientov, MUMPS a riešitelia riedkych deformácií (pozri obr. 34.2.35.). Predvolene je vybraný riešiteľ konjugovaných gradientov.

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image021.jpg' | relative_url }})

Nastavenia pokročilých ovládacích prvkov simulácie

Pri riešení určitých úloh ponúka tento riešiteľ oproti riešiteľovi pre riedke matice obrovské výhody. Informácie o riešiteľoch nájdete v časti „Forming operation“, ktorá v expertnom režime poskytuje viac možností ovládania simulácie; podrobnosti o týchto možnostiach nájdete v [9\. Simulation Controls.](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/).

## Vytvoriť databázu

**Overiť údaje** ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})

Systém skontroluje údaje. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvoriť databázu** ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) sa vygeneruje databáza pre inštaláciu. (Pozri obr. 34.2.36.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image050.jpg' | relative_url }})

Okno „Vytvoriť databázu“

Ak používateľ potrebuje niektorú z pokročilých možností, ktoré nie sú k dispozícii v režime Forming Express, môže k nim získať prístup bez straty definovaných údajov v operácii Forming Express prostredníctvom prechodu do režimu Forming. Táto možnosť je k dispozícii v ponuke pravého tlačidla myši v editore operácií, ako je znázornené na obr. 34.2.37. Ďalšie podrobnosti o tomto prechode na vyššiu úroveň operácie nájdete v [6.6.4. Upgrading Operations.](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_6_operations_management/6_6_4_upgrading_operations/)

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image022.jpg' | relative_url }})

Presun položky „Forming Express“ do pravého menu v rámci operácie formovania

Po vytvorení databázy musí používateľ vybrať kartu „Režim simulácie MO“, aby odoslal problém na simuláciu. Ďalšie informácie o režime simulácie MO nájdete v [6.2. MO Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/). Akonáhle sa na karte „Simulácia dokončená“ zobrazí príslušná správa, môže používateľ v režime MO Post skontrolovať výsledky. Ďalšie informácie o režime MO Post nájdete v [ 6.3. MO Post layout.](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/).

**Súvisiace témy:**

[34.1. 2D Forming Express Setup](/docs/en/operation_templates/34_forming_express/34_1_2d_forming_express_setup/)

[Promote Forming Express to Forming operation](../../integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_6_operations_management/6_6_4_upgrading_operations.htm#Fig._6.6.4.4._Forming_express_operation_after_promoting_it_to_forming_operation)

[6.2. MO Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. MO Post layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[33.1. 2D Forming Setup](/docs/en/operation_templates/33_forming/33_1_2d_forming_setup/)

[33.2. 3D Forming Setup](/docs/en/operation_templates/33_forming/33_2_3d_forming_setup/)
