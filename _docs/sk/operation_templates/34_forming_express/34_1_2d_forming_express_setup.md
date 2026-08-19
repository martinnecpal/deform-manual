---
lang: sk
title: "34.1. Rýchle nastavenie 2D tvarovania"
---

# 34.1. Rýchle nastavenie 2D tvarovania

34.1.1. Ako pridať operáciu 2D Forming Express

34.1.2. Definícia nastavení procesu

34.1.3. Nastavenia výpočtu teploty

34.1.4. Výber objektov

34.1.5. Objekt – základná definícia

34.1.6. Definícia geometrie objektu

34.1.7. Definícia siete objektu

34.1.8. Materiál

34.1.9. Okrajové podmienky

34.1.10. Ovládacie prvky pohybu

34.1.11. Polohovanie

34.1.12. Plánované umiestnenie

34.1.13. Vzťahy medzi objektmi

34.1.14. Stanovenie dĺžky zdvihu primárneho lisovacieho nástroja alebo celkovej doby spracovania

34.1.15. Ovládacie prvky na zastavenie

34.1.16. Ovládacie prvky simulácie

34.1.17. Vytvorenie databázy

## Ako pridať operáciu v programe 2D Forming Express

**Operáciu „Forming Express“ je možné spustiť dvoma spôsobmi**,

  1. Vytvorenie rýchlej a nezávislej prevádzky.

  2. Spustenie operácie „Express MO Wizard“.

**Na pridanie funkcie „Forming express“ s nezávislým prevádzkovaním**

Vytvorte nový problém výberom položky Súbor ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Nový problém alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 34.1.1. Vyberte prepínač 2D Forming Express. Následne zadajte Názov problému, v poli Jednotky v rozbaľovacom okne Nový problém vyberte prepínač Systém jednotiek a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoríte nový problém pomocou sprievodcu Forming Express.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image001.jpg' | relative_url }})

Pridanie samostatnej operácie 2D Forming Express.

  
Následne sa otvorí operácia „2D Forming Express“, ako je znázornené na obr. 34.1.2.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image002.jpg' | relative_url }})

Sprievodca programom Independent Forming Express

Tu môžete pridávať alebo odstraňovať expresné operácie a simulačné operátory. Expresné operácie pre prenos tepla sú vysvetlené v časti [36.1 Introduction to Heat Transfer Express](/docs/en/operation_templates/36_heat_transfer_express/36_introduction_to_heat_transfer_express_operations/).

Fungovanie konvertora z 2D do 3D je vysvetlené v časti [44.1. 2D to 3D Convertor](/docs/en/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/).

Boolovské operácie sú vysvetlené v časti [45.1. Boolean Operator](/docs/en/operation_templates/45_boolean_operation/45_1_boolean_operation/)

Postup kopírovania/zrkadlenia je vysvetlený v časti [46.1. Copy Mirroring](/docs/en/operation_templates/46_copy_mirroring/46_1_copy_mirroring/)

**Pridanie operácie Forming Express do integrovaného výrobného procesu (MO).**

Vytvorte nový problém buď výberom položky Súbor ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Nový problém, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 34.1.3. Vyberte prepínač „Integrovaný výrobný proces“ a v poli jednotiek vyberte prepínač systému jednotiek. Zadajte názov úlohy a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvorte novú úlohu s použitím metódy Deform Integrated Manufacturing Process (MO).

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image003.jpg' | relative_url }})

Spustenie sprievodcu MO

Otvorí sa sprievodca MO. Operáciu Forming Express je možné pridať v sprievodcovi MO na karte „Explorer“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky „2D Forming Express“. Operáciu Forming Express môže používateľ pridať aj pomocou funkcie drag and drop do editora operácií, ako je znázornené na obr. 34.1.4. Operáciu Forming Express je možné pridať aj po interaktívnych operáciách prenosu tepla alebo v dávkovom/naplánovanom režime.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image004.jpg' | relative_url }})

Do editora operácií bola pridaná operácia „2D Forming Express“

## Definícia nastavení procesu

V okne „Proces“ je potrebné pre operáciu rýchleho tvárnenia nastaviť simulačné režimy, ako sú „Typ geometrie“, „Typ procesu“, „Zložitosť tvaru“ a „Presnosť“, ako je znázornené na obr. 34.1.5.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image005.jpg' | relative_url }})

Okno nastavení procesu

**Typ geometrie**

V nástroji Forming je možné nastaviť iba dva geometrické modely, a to „Axisymmetric“ a „Plane Strain“.

Axisymetrické modely predstavujú priečny rez vzhľadom na stredovú os. Model preto vyžaduje, aby deformujúca sa geometria bola osovo symetrická a nachádzala sa v prvom a štvrtom kvadrante (t. j. X > 0). Systém navyše predpokladá, že prúdenie v každej radiálnej rovine je identické. (Pozri [Fig. 9.1.2.](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Fig._9.1.2._Example_for_types_of_geometry_model))

Pri rovinnom deformovaní sa predpokladá, že geometria má jednotkovú hĺbku a že predná aj zadná plocha sú fixované. Simulácia vychádza z predpokladu, že objekty sa budú správať rovnako v akomkoľvek priereze v smere šírky aj výšky objektu. (Pozri [Fig. 9.1.2.](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Fig._9.1.2._Example_for_types_of_geometry_model))

Ďalšie typy geometrie – „Rovinné napätie“ a „Krútenie“ – sú k dispozícii iba pri 2D operácii tvarovania; podrobnosti nájdete v [2D Forming Setup](/docs/en/operation_templates/33_forming/33_1_2d_forming_setup/).

**Typ procesu**

V programe Forming Express sú k dispozícii tri typy procesov: tvárnenie za studena, tvárnenie za tepla a kovanie za tepla. Pri operácii tvárnenia za studena bude režim prenosu tepla vypnutý, takže počas simulácie nedochádza k výpočtu teploty. Pri typoch tvárnenia za tepla a kovania za tepla bude režim prenosu tepla zapnutý a aktivuje sa okno výpočtu teploty. Okno „Výpočet teploty“ (pozri obr. 34.1.5.) ponúka možnosti výberu izotermického a neizotermického nastavenia.

**Zložitosť tvaru a presnosť**

Posuvníky pre zložitosť tvaru a presnosť simulácie (pozri obr. 34.1.5.) ovplyvňujú nastavenia siete a počet časových krokov použitých v simulácii. To zase ovplyvňuje dĺžku behu a úroveň detailov dostupnú v simulácii.

**Zložitosť tvaru:**

  * **Jednoduché**: Geometria objektov je svojou povahou jednoduchá. Vyžadujú si minimálny počet prvkov, ich riešenie je jednoduchšie a trvá kratšie.

  * **Stredná**: Geometria objektov je stredne zložitá (nie príliš zložitá).

  * **Zložité**: Geometria objektov má zložitý charakter.

  
**Presnosť tvaru:**

  * **Rýchly**: Vhodný na rýchle vyhodnotenie procesu. Výmenou za rýchlejšie časy spustenia však existuje vyššie riziko, že sa prehliadnu dôležité detaily.

  * **Stredná**: Simulácia používa nastavenia, ktoré sa snažia dosiahnuť rovnováhu medzi výpočtovým časom a presnosťou.

  * **Presné**: Vykonáva sa veľmi podrobná analýza procesu, ktorá zvyčajne zachytí aj tie najmenšie detaily. Čas potrebný na výpočet a požiadavky na úložný priestor sú vyššie.

## Nastavenia výpočtu teploty

Okno „Výpočet teploty“ (pozri obr. 34.1.6.) ponúka možnosti výberu medzi izotermickým a neizotermickým nastavením. Izotermické nastavenie slúži na udržanie konštantnej teploty, zatiaľ čo neizotermické nastavenie slúži na výpočet teploty iba v obrobku alebo v obrobku a formách.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image006.jpg' | relative_url }})

Okno nastavení typu výpočtu teploty

**Izotermické**: Simulácia sa vykonáva za predpokladu konštantnej teploty. Zmeny teploty spôsobené deformáciou, ohrevom alebo výmenou tepla s okolím sa nezohľadňujú. Vhodné pre procesy, pri ktorých zmeny teploty významne neovplyvňujú výsledky simulácie. Príklady zahŕňajú: väčšinu procesov tvárnenia za studena a procesov tvárnenia za tepla, pri ktorých sa vplyv zmeny teploty z praktických dôvodov zanedbáva. V tomto nastavení nemajú formy ani výpočet siete, ani výpočet teploty.  
**Neizotermický**: Proces, pri ktorom teplota systému nie je konštantná. Zahrnutie výpočtov teploty zlepší predpovede toku materiálu a predpovede zaťaženia, najmä v procesoch, kde dochádza k výrazným zmenám teploty. Výpočet teploty v nástrojoch ďalej zlepšuje výpočet teploty obrobku, pretože zmena teploty nástroja ovplyvňuje únik tepla z obrobku.

## Vybrať objekty

V tomto okne si môže používateľ v závislosti od nastavenia procesu vybrať počet objektov potrebných na vykonanie operácie (pozri obr. 34.1.7.). Používateľ musí mať na pamäti, že v simulácii môže byť len jeden plastový objekt. Je možné pridať maximálne 100 foriem.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image007.jpg' | relative_url }})

Okno na výber objektov

## Základná definícia objektu

Základná definícia objektu zahŕňa názov objektu, typ a teplotu. Okrem toho je možné pomocou tlačidla „Pokročilé“ inicializovať hodnoty premenných stavu objektu a údaje o objekte, ako sú geometria, sieť, okrajové podmienky a materiál, je možné importovať zo súboru DEFORM .DB /.Key. (Pozri obr. 34.1.8.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image008.jpg' | relative_url }})

Okno obrobku

  
**Názov objektu**: Používateľ môže určiť názov pre všetky objekty dostupné v danej operácii.

**Typ objektu******: Typ objektu ([OBJTYP](/docs/en/keyword_documentation/o/objtyp/)) určuje, či a ako sa modeluje deformácia pre každý jednotlivý objekt v úlohe DEFORM. V operácii Forming Express sú k dispozícii len dva typy objektov, a to plastický a tuhý, ktoré sú automaticky preddefinované podľa čísla objektu, takže obrobok bude plastický a formy budú tuhé. Ďalšie typy objektov sú vysvetlené v kapitole 11. Všeobecná definícia údajov o objektoch, podrobnosti nájdete v [11.4. Object Type](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type).

  * **Plast**: Plastové objekty sa modelujú ako tuhé plastické alebo tuhé viskoplastické materiály v závislosti od vlastností materiálov. Model predpokladá, že napätie v materiáli lineárne rastie s rýchlosťou deformácie až do prahovej hodnoty rýchlosti deformácie, označovanej ako limitná rýchlosť deformácie ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)). Po prekročení medznej rýchlosti deformácie sa materiál deformuje plasticky. Plastické správanie materiálu objektu sa špecifikuje pomocou funkcie tečenia materiálu alebo údajov o tečnom napätí ([FSTRES](/docs/en/keyword_documentation/f/fstres/)). V operácii Forming Express sa obrobok automaticky priradí k typu objektu „Plast“.

  * **Tuhé**: Tuhé objekty sa modelujú ako nedeformovateľné materiály. Pri analýze deformácie je geometria objektu reprezentovaná geometrickým profilom ([DIEGEO](/docs/en/keyword_documentation/d/diegeo/)). Údaje o riešení deformácie dostupné pre tuhé objekty zahŕňajú zdvih objektu, zaťaženie a rýchlosť. Geometrický profil sa používa pre všetky analýzy deformácie a sieť pre tuhý objekt sa používa pre všetky výpočty tepelnej vodivosti, transformácie a difúzie. V programe Forming Express sú lisovacie formy alebo nástroje automaticky priradené k kategórii „Tuhé“, keďže ide o nedeformovateľné objekty.

**Poznámka:**

Je potrebné poznamenať, že typ objektu je v programe Forming Express preddefinovaný číslom objektu.

Na stránke „Objekt“ sa nachádza tlačidlo „Importovať objekt“. Slúži na import kompletných údajov o objekte z iného súboru DEFORM.

**Teplota objektu**: Používateľ môže nastaviť teplotu objektu v poli „Teplota“ v príslušnom okne objektu, ako je znázornené na obr. 34.1.8.

  
**Pokročilé nastavenia objektu**: Pokročilé nastavenia v časti „Možnosti inicializácie“ (pozri obr. 34.1.9.) sa zídu v prípade, že používateľ importuje objekt z predchádzajúceho projektu alebo úlohy, alebo ak sa operácia „express“ pridá až po niekoľkých iných operáciách a je potrebné inicializovať niekoľko dôležitých stavových premenných.

  
Pomocou pokročilých nastavení môže používateľ zadať teplotu, deformáciu, rýchlosť, poškodenie a posun, ku ktorým došlo v deformovateľnom objekte. (Pozri obr. 34.1.9.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image009.jpg' | relative_url }})

Pokročilé nastavenia objektov

V operácii „Forming“ je možné inicializovať ďalšie premenné; podrobnosti nájdete v [19\. Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/).

  
Priemerná rýchlosť deformácie ([AVGSTR](/docs/en/keyword_documentation/a/avgstr/)) je charakteristická priemerná hodnota efektívnej rýchlosti deformácie. Na začiatku simulácie by sa mala zadať aproximácia tejto hodnoty.

Medzná rýchlosť deformácie ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)) definuje medznú hodnotu efektívnej rýchlosti deformácie, pod ktorou sa plastický alebo porézny materiál považuje za tuhý a správa sa ako materiál podobný newtonovskej tekutine.

  
![]({{ '/assets/icons/pre_icons/mo_reset_button.jpg' | relative_url }}) : Pomocou tejto funkcie môže používateľ obnoviť hodnoty premenných v počiatočnom stave.

  
Ďalšie možnosti vlastností objektu „Deformácia“, ktoré sú k dispozícii v operácii „Tvarovanie“, nájdete v [16.1. Deformation Properties.](/docs/en/pre_processor/16_object_properties/16_1_deformation_properties/)

## Definícia geometrie objektu

Okno „Geometria“ slúži na vytvorenie geometrie objektu, ako je znázornené na obr. 34.1.10. Pred vytvorením geometrie sú k dispozícii iba možnosti „Definovať primitív“ a „Upraviť geometriu“, avšak po vytvorení geometrie sa aktivujú možnosti „Skontrolovať“, „Zmenšiť“ a „Obrátiť geometriu“ a po vygenerovaní siete sa aktivuje možnosť „Extrahovať zo siete“.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image010.jpg' | relative_url }})

Okno s definíciou geometrie

**Definovať primitív ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }})**

  * **Pre osovo symetrický typ:** Na stránke s geometrickými primitívami je k dispozícii päť základných tvarov, ktoré možno použiť na vytvorenie geometrií, ako je znázornené na obr. 34.1.11. V každom prípade musí používateľ prispôsobiť rozmery tak, aby zodpovedali danej úlohe.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image011.jpg' | relative_url }})

Okno s geometrickými primitívami pre typ geometrie „Axisymmetric“

  * **Pre typ rovinného deformovania:** Na stránke s geometrickými primitívami sa nachádzajú tri základné tvary, ktoré možno použiť na vytvorenie geometrií, ako je znázornené na obr. 34.1.12. V každom prípade musí používateľ prispôsobiť rozmery tak, aby zodpovedali danej úlohe.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image012.jpg' | relative_url }})

Okno s geometrickými primitívami pre typ geometrie „Rovinné deformácie“

**Check![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})**

Po vytvorení geometrie objektu sa aktivuje tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Je potrebné skontrolovať orientáciu geometrie. To je možné urobiť kliknutím na tlačidlo **![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})**. Zobrazí sa okno „Skontrolujte a opravte geometriu“, ako je znázornené na obr. 34.1.13 nižšie. Geometria sa opraví, ak obsahuje nejaké chyby, po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}). Po oprave geometrie alebo ak geometria neobsahuje žiadne chyby, zobrazí sa správa „Geometria je správna“ a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Ďalšie informácie nájdete v časti [Check Geometry](../../pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining.htm#Check_Geometry) v kapitole [12.1. 2D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/).

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image013.jpg' | relative_url }})

Okno „Skontroluj a oprav geometriu“

**Scale![]({{ '/assets/icons/pre_icons/mo_scale_label.jpg' | relative_url }}) **

Geometriu je možné pri tvárnení zmenšiť alebo zväčšiť tak, aby zohľadňovala teplotnú rozťažnosť, a to stanovením mierky. (Pozri obr. 34.1.14.) Mierku je možné vypočítať na základe teplotného rozdielu a údajov o materiáli závislých od teploty. Upravenú geometriu je možné uložiť v rôznych formátoch na ukladanie geometrie.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image014.jpg' | relative_url }})

Okno „Scale Geo“

**Reverse![]({{ '/assets/icons/pre_icons/mo_reverse_label.jpg' | relative_url }}) **

Táto funkcia obráti orientáciu geometrie. Pri geometrii s jedným okruhom musí byť orientácia 2D geometrie vždy smerom dovnútra; pri geometrii s viacerými okruhmi môže mať okruh, ktorý sa nachádza v oboch oblastiach, orientáciu na ktorúkoľvek stranu, avšak topológia musí byť definovaná.

**Výňatok zo siete**![]({{ '/assets/icons/pre_icons/mo_extract_from_mesh.jpg' | relative_url }})****

Táto funkcia extrahuje geometrické údaje z aktuálneho objektu s mriežkou v databáze pre všetky typy objektov s výnimkou tuhého objektu.

**Edit![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }})**

Možnosť „Editácia geometrie“ slúži na vytvorenie geometrie objektu alebo na úpravu existujúcej geometrie. Importovanú geometriu je možné upravovať v okne „Editácia geometrie“. Na stránke „Geometria“ kliknite na označenie ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a prezrite si dostupné možnosti na vytvorenie a úpravu geometrie, ako je znázornené na obr. 34.1.15.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image015.jpg' | relative_url }})

Okno „Upraviť geometriu“

Geometriu je možné vytvoriť pomocou nástroja na vytváranie slučiek alebo zadaním súradníc geometrie do tabuľky v editore geometrie v pravom dolnom rohu okna, ako je znázornené na obr. 34.1. Obr. 34.1.15. buď v režime XYR, alebo v režime Čiara-Oblúk. Ďalšie podrobnosti o 2D editore geometrie nájdete v kapitole [12.2. 2D Geometry Data Editing](/docs/en/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/).

**Ďalšie možnosti geometrie**

  * **Zobraziť geometriu vnútri značky**: Zaškrtnutím tejto možnosti sa aktivuje zobrazenie orientácie geometrie.

  * **Určiť referenčný bod**: Používateľ môže vybrať referenčný bod geometrie kliknutím na toto tlačidlo v zobrazovacom okne. Tento referenčný bod je potrebný na určenie vzdialenosti medzi objektmi pomocou ovládacích prvkov na zastavenie.

  * **Import geometrie zo súboru** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) : Pomocou tejto možnosti môže používateľ importovať geometriu zo súboru.

  * **Načítať geometriu z knižnice** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ importovať geometriu z knižnice.

  * **Uloženie geometrie do súboru** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}): Uloží geometriu do súboru.

  * **Uložiť geometriu do knižnice** ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ uložiť geometriu do knižnice.

  * **Odstrániť geometriu** ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ odstrániť geometriu.

## Definícia objektovej siete

Okno „Vytvorenie siete“ umožňuje používateľovi vytvoriť sieť pre aktuálny objekt. Na obr. 34.1.16 je zobrazené okno „Vytvorenie siete“ v systémovom režime. V tomto režime systém automaticky nastaví počet prvkov siete na základe zložitosti tvaru a výberu nastavenia presnosti v pracovnom okne.

**Režim systému**: Pri použití funkcie **Generate Mesh** musí používateľ vygenerovať sieť pre objekty a po jej vygenerovaní sa aktivuje tlačidlo **Delete** Mesh, ktoré slúži na odstránenie aktuálnej siete objektu.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image016.jpg' | relative_url }})

Okno nastavení siete v režime Systém

**Režim definovaný používateľom**: Možnosť režimu siete definovaného používateľom je znázornená na obr. 34.1.17. V tomto režime môže používateľ meniť počet prvkov posúvaním posuvníka a pomocou pokročilých možností upravovať pomer veľkostí, hrúbku prvkov, váhový faktor a kritériá pregenerovania siete.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image017.jpg' | relative_url }})

Nastavenia siete v užívateľsky definovanom režime

**Počet prvkov (MGNELM)**

Počet prvkov siete predstavuje približný počet prvkov, ktoré systém vygeneruje. Automatický generátor siete (AMG) použije hodnotu pre [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) a vygeneruje sieť, ktorá bude obsahovať približne rovnaký počet prvkov.

Chyba medzi počtom zadaných prvkov a počtom vygenerovaných prvkov sa zvyčajne pohybuje okolo desiatich percent. Pri generovaní siete sa na určenie hustoty siete používa zadaný celkový počet prvkov v kombinácii s ovládacími prvkami „Bod“ a „Parameter“.

**Pokročilé nastavenia siete**

**Všeobecné nastavenia**

Okrem počtu prvkov môže používateľ zvoliť aj hrúbku prvkov a hodnoty pomeru veľkostí, aby dosiahol požadovanú sieť.

  * **Počet prvkov v smere hrúbky (MGTELM):** Maximálny pomer hrúbky je jedným z viacerých spôsobov, ako regulovať hustotu siete počas automatického generovania siete (AMG). Počet prvkov v smere hrúbky predstavuje približný počet prvkov, ktoré systém vygeneruje v smere hrúbky v akejkoľvek oblasti dielu. Automatický generátor siete (AMG) použije hodnotu pre [MGTELM](/docs/en/keyword_documentation/m/mgtelm/) a vygeneruje sieť, ktorá bude mať tento počet prvkov v najtenšej časti. Napríklad, ak je [MGTELM](/docs/en/keyword_documentation/m/mgtelm/) nastavené na 4, AMG sa pokúsi vytvoriť 4 prvky v smere hrúbky geometrie.

Smer hrúbky objektu je kolmý na os rozvetvenej stredovej čiary pre každú oblasť dielu. Celkový počet prvkov, ktoré sa majú vygenerovať v sieti, sa riadi hodnotou počtu prvkov v kľúčovom slove [MGNELM](/docs/en/keyword_documentation/m/mgnelm/). Ak hodnota prvkov hrúbky vedie k sieti, ktorá obsahuje viac prvkov, ako je hodnota špecifikovaná v [MGNELM](/docs/en/keyword_documentation/m/mgnelm/), hodnota [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) sa zníži tak, aby sieť obsahovala približne [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) prvkov. Ak hodnota [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) vedie k sieti, ktorá obsahuje menej ako [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) prvkov, zostávajúce prvky budú rozdelené medzi ostatné užívateľom špecifikované parametre hustoty siete (krivka, deformácia, rýchlosť deformácie a teplota).

  * **Pomer veľkostí prvkov (MGSIZR):** Maximálny pomer veľkostí medzi prvkami je jedným z viacerých spôsobov, ako regulovať hustotu siete počas automatického vytvárania siete (AMG) prostredníctvom špecifikácie pomeru hustôt uzlov.

Pri hodnote 3 pre [MGSIZR](/docs/en/keyword_documentation/m/mgsizr/) bude najväčšia hrana prvku na objekte približne trojnásobkom veľkosti najmenšej hrany prvku na tom istom objekte. Ak sa požadujú prvky rovnakej veľkosti, pomer veľkostí je 1. Ak je pomer veľkostí 0, pomer veľkostí prvkov nebude mať vplyv na rozloženie hustoty siete.

**Faktory, ktoré sa zohľadňujú**

Váhovacie koeficienty alebo parametre (systémom definovaná hustota siete) pre zakrivenie hranice, teplotu, deformáciu a rýchlosť deformácie určujú relatívne váhy hustoty siete, ktoré sa majú priradiť k príslušnému parametru. (Pozri obr. 34.1.18.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image018.jpg' | relative_url }})

Okno nastavení váhových koeficientov

Hustoty teploty, deformácie a rýchlosti deformácie sa prideľujú na základe gradientov týchto parametrov, nie na základe ich absolútnych hodnôt. To znamená, že oblasť s rýchlou zmenou teploty v určitom smere bude obsahovať viac prvkov ako oblasť s rovnomernou vysokou teplotou.

Hodnoty zo všetkých kľúčových slov týkajúcich sa hustoty siete sa počas procesu generovania siete kombinujú, čím sa vytvorí rozloženie hustoty siete v rámci geometrických hraníc.

Operácia formovania obsahuje ďalší váhový faktor, a to možnosti v okne „Mesh Density“ (Hustota siete), pomocou ktorých môže používateľ definovať konkrétnu oblasť v priestore, ktorá sa bude počas deformácie pohybovať spolu s ostatnými objektmi s príslušnou hustotou siete. Pozrite si kapitolu [13.1.5. Mesh Weighting factors.](../../pre_processor/13_mesh_generation/13_1_2d_mesh_generation.htm#13.1.5._Mesh_weighting_factors).

**Kritériá pre generovanie novej siete**

Kritériá pregenerovania siete (Autoremesh) predstavujú najpohodlnejší spôsob, ako riešiť pregenerovanie siete objektov, ktoré prechádzajú veľkou plastickou deformáciou. Okno Kritériá pre vytváranie novej siete (pozri obr. 34.1.19.) obsahuje skupinu parametrov, ktoré na základe priradenia určitých spúšťačov riadia, kedy a ako často sa bude sieť na objektu so sieťou regenerovať. Existujú štyri kľúčové slová, ktoré riadia spustenie postupu premenovania siete pre objekt: Hĺbka interferencie ([RMDPTH](/docs/en/keyword_documentation/r/rmdpth/)), Max. časový prírastok ([RMTIME](/docs/en/keyword_documentation/r/rmtime/)), Max. krokový prírastok ([RMSTEP](/docs/en/keyword_documentation/r/rmstep/)) a Max. prírastok zdvihu ([RMSTRK](/docs/en/keyword_documentation/r/rmstrk/)). Keď sa splnia kritériá pregenerovania siete pre ktorékoľvek z týchto kľúčových slov alebo sa sieť stane nepoužiteľnou (záporná jacobiánska matica), objekt sa pregeneruje. Ak objekt počas simulácie spĺňa ktorékoľvek z kritérií pre vytvorenie novej siete, vygeneruje sa nová sieť, informácie o riešení zo starej siete sa interpolujú na novú sieť a simulácia pokračuje. Ďalšie informácie o kritériách pre vytvorenie novej siete nájdete v [13.1.8. Remeshing criteria.](../../pre_processor/13_mesh_generation/13_1_2d_mesh_generation.htm#13.1.8._Remeshing_criteria)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image019.jpg' | relative_url }})

Okno „Kritériá pre výpočet novej siete“

**Pokročilé nastavenia**

Na obr. 34.1.20. je zobrazené okno „Pokročilé nastavenia“.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image020.jpg' | relative_url }})

Okno s pokročilými nastaveniami siete

  * **Rozlíšenie mriežky ([MGGRID](/docs/en/keyword_documentation/m/mggrid/)): **Pri vytváraní 2D siete objektu je potrebná vzorkovacia mriežka na diskretizáciu hustoty siete v celej počiatočnej geometrii. Rozlíšenie mriežky ([MGGRID](/docs/en/keyword_documentation/m/mggrid/)) určuje rozstup vzorkovacích mriežok, ktoré sa používajú na vzorkovanie hustôt siete. Zvýšenie hodnoty rozdelenia X alebo rozdelenia Y bude mať za následok ostrejšie prechody medzi oblasťami s odlišnou hustotou siete. V prípade vyprázdňovania, kde je potrebný veľmi vysoký gradient siete v úzkej oblasti, môže byť potrebné tieto hodnoty zvýšiť, aby sa zachytili veľké zmeny gradientu siete na krátkych vzdialenostiach.

  * **Parametre pridávania uzlov ([MGERR](/docs/en/keyword_documentation/m/mgerr/)): **Parametre pridávania uzlov ([MGERR](/docs/en/keyword_documentation/m/mgerr/)) určujú maximálnu povolenú vzdialenosť a uhlovú chybu medzi hranicou objektu a stranou príslušného prvku mriežky. Tolerancie vzdialenosti a uhla sa používajú na zachytenie kritickej geometrie hraníc, ktorá by inak mohla byť pri generovaní siete stratená. Ak je potrebné, aby objekt zachytil veľmi malé prvky, maximálnu vzdialenosť je možné znížiť, alebo ak je potrebné umiestniť uzol pod malým uhlom, je možné znížiť aj uhlovú chybu. Používateľ bude musieť tieto hodnoty meniť len zriedka. Pre veľmi malé diely je hodnota 0,01 % ohraničujúceho obdĺžnika objektu dobrým východiskovým číslom, ktoré možno použiť pre [MGERR](/docs/en/keyword_documentation/m/mgerr/) na lepšie zvládnutie rozlíšenia siete.

**Skontrolujte Mesh![]({{ '/assets/icons/pre_icons/mo_check_mesh_button.jpg' | relative_url }})**

Sieť je možné skontrolovať z hľadiska prípadných problémov pomocou funkcie „Check Mesh“. Ak je sieť bezchybná, po kliknutí na možnosť „Check Mesh“ sa zobrazí vyskakovacie okno, ako je znázornené na obr. 34.1.21.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image003.jpg' | relative_url }})

Skontrolujte vyskakovacie okno so sieťou

**Odstrániť sieť**![]({{ '/assets/icons/pre_icons/mo_delete_mesh_button.jpg' | relative_url }})   
Odstráni sieť vytvorenú pre daný objekt.

**Zobraziť sieť** ![]({{ '/assets/icons/pre_icons/mo_show_mesh_button.jpg' | relative_url }})

Keď používateľ klikne na tlačidlo „Zobraziť sieť“, v okne zobrazenia sa zobrazí vygenerovaná sieť. Tlačidlo „Zobraziť sieť“ prepína medzi zobrazením siete a geometrie objektu.

**Predvolené nastavenie ![]({{ '/assets/icons/pre_icons/mo_default_settings_button.jpg' | relative_url }})**

Keď používateľ klikne na kartu „Predvolené nastavenia“, všetky nastavenia sa zmenia na predvolené hodnoty. Okno „Mesh“ bude štandardne neaktívne, keďže nie sú definované žiadne okná typu „Mesh“. Ak chce používateľ aktivovať okno „Mesh“, musí zmeniť váhový koeficient hustoty siete tak, že posuvník nastaví na hodnotu 1.

Na rozdiel od operácie „Forming“ nie sú v operácii „Forming express“ k dispozícii možnosti „Coating mesh“ a „User Mesh Density Window“; informácie o týchto možnostiach nájdete v [13.1.7. Coating Mesh](../../pre_processor/13_mesh_generation/13_1_2d_mesh_generation.htm#13.1.7._Coating), resp. [ 13.1.6. Mesh Density windows](../../pre_processor/13_mesh_generation/13_1_2d_mesh_generation.htm#13.1.6._Mesh_density_windows).

## Materiál

Na obr. 34.1.22. je zobrazené okno s materiálmi. Používateľ môže pridať alebo importovať materiál zo súboru kľúčových slov alebo ho načítať z knižnice materiálov DEFORM.

  
Po načítaní systém automaticky priradí načítaný materiál k objektu. Používateľ môže tiež upravovať plastické a tepelné vlastnosti, a to napätie pri tečení, tepelnú vodivosť, tepelnú kapacitu, hustotu a emisivitu, a to pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image021.jpg' | relative_url }})

Okno s materiálmi

Po pridaní materiálu kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) – otvorí sa okno s materiálom, ako je znázornené na obr. 34.1.23.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image022.jpg' | relative_url }})

Okno na úpravu materiálu

Požadované vlastnosti závisia od fyzikálnych javov simulovaných v programe DEFORM. Vlastnosti materiálov, ktoré musí používateľ zadať, závisia od typov materiálov, ktoré používateľ v simulácii využíva. V kapitole [10\. Material Data](/docs/en/pre_processor/10_material_data/10_material_data/) má používateľ prístup ku všetkým vlastnostiam materiálov; ďalšie informácie nájdete v kapitole [10\. Material Data](/docs/en/pre_processor/10_material_data/10_material_data/).

## Okrajové podmienky

V okne „Forming express Boundary conditions“ môže používateľ objektu priradiť iba okrajové podmienky „Rýchlosť deformácie“, „Teplotná výmena s prostredím“ a „Teplota“. Okrajové podmienky určujú, ako hranica objektu interaguje s inými objektmi a s prostredím. Najčastejšie používanými okrajovými podmienkami sú výmena tepla s okolím pri simuláciách zahŕňajúcich prenos tepla a predpísaná rýchlosť na vynútenie symetrie v modeli. Obr. 34.1.24. znázorňuje rôzne okrajové podmienky, ktoré je možné priradiť k objektu.

  
V predvolenom nastavení bude rýchlosť pozdĺž stredovej osi objektu obrobku v osovo symetrickom type geometrie pevne stanovená, ako je znázornené na obr. 34.1. Obr. 34.1.24. . Okrem toho sa pri procesoch teplej a horúcej kovania priradí výmena tepla s okolím ku všetkým povrchom okrem symetrického povrchu, ako je znázornené na obr. 34.1.25.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image023.jpg' | relative_url }})

Pre obrobok bola nastavená okrajová podmienka symetrie

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image024.jpg' | relative_url }})

Pre obrobok bola stanovená okrajová podmienka výmeny tepla s okolím

BCC sú rozdelené do kategórií [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/), [Thermal](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/), [Diffusion](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/) a [Heating](/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/). Ďalšie informácie o týchto BCC nájdete v [14\. Boundary Conditions.](../../pre_processor/14_boundary_conditions).

## Ovládanie pohybu

Ovládacie prvky pohybu je možné aplikovať na tuhé objekty a hraničné uzly objektov s sieťou. Povrch definovaný týmito uzlami možno považovať za „tuhý povrch“. Počas simulácie sa obmedzené uzly budú pohybovať synchronizovane rýchlosťou a smerom definovaným ovládacími prvkami pohybu. V nástroji Forming Express je k dispozícii iba typ posuvného pohybu spomedzi troch typov pohybov dostupných v 2D prostredí (operácia tvárnenia), ktorými sú posuv, rotácia a krútenie.

**Translačný pohyb:**

Počas simulácie sa viazané uzly budú pohybovať synchronizovane rýchlosťou a smerom, ktoré sú definované ovládacími prvkami pohybu. (Pozri obr. 34.1.26.)

  
V funkcii Forming Express je v rámci typu pohybu „Translation“ k dispozícii len šesť typov ovládacích prvkov pohybu, a to [Speed](/docs/en/pre_processor/15_movement_controls_definition/15_1_speed/), [Load](/docs/en/pre_processor/15_movement_controls_definition/15_2_force/), [Hammer](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/), [Screw press](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/), [Mechanical press](/docs/en/pre_processor/15_movement_controls_definition/15_5_mechanical_press/) a [Hydraulic press](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/). Operácia tvarovania obsahuje okrem ovládacích prvkov pre pohyb „Forming Express“ aj ovládacie prvky pre translačný pohyb [Sliding Die](/docs/en/pre_processor/15_movement_controls_definition/15_7_sliding_die/) a [Path](/docs/en/pre_processor/15_movement_controls_definition/15_8_path/), ako aj typy rotačného a torzného pohybu. Ďalšie informácie nájdete v [15\. Movement Controls.](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/).

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image025.jpg' | relative_url }})

Okno na ovládanie translačného pohybu

V dolnej časti okna na ovládanie pohybov (pozri obr. 34.1.26.) môže používateľ importovať špecifikácie pohybov z iných súborov kľúčových slov alebo databázových súborov, načítať informácie o lise z knižnice, uložiť nastavenia pohybov do súboru alebo do knižnice pohybov, prezrieť si náhľad a vymazať definíciu pohybu. Používateľ môže tiež načítať pohyb z knižnice lisov pomocou prehliadača, ako je znázornené na obr. 34.1.26.

**Rýchlosť:** Ide o predvolené ovládanie pohybu. Určuje rýchlosť a smer nástroja, ako je znázornené na obr. 34.1.26.

**Regulácia zaťaženia/sily:** Pri regulácii sily je rýchlosť objektu obmedzovaná tak, aby sa udržalo zadané zaťaženie. Ak je objekt tuhý, zaťaženie predstavuje výslednicu sily pôsobiacej zo strany netuhého objektu v dôsledku relatívneho pohybu týchto dvoch objektov. Používateľ musí špecifikovať veľkosť a smer zaťaženia, ako je znázornené na obr. 34.1.27.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image026.jpg' | relative_url }})

Nastavenia ovládacích prvkov pohybu nákladu

**Mechanický lis**: Typ „Mechanický lis“ napodobňuje cyklický pohyb mechanického lisu (pozri obr. 34.1.28.). Možnosť „Mechanický lis“ simuluje pohyb objektov poháňaných mechanickým lisom. V režime Forming je k dispozícii iba riadenie mechanického kľukového lisu; okrem toho bude v operácii Forming k dispozícii aj riadenie kĺbového lisu. Informácie o kĺbovom lise nájdete v [15.5.2. Knuckle Press.](../../pre_processor/15_movement_controls_definition/15_5_mechanical_press.htm#15_5_2_Knuckle_or_Wedge_Press).

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image027.jpg' | relative_url }})

Nastavenia riadenia mechanického pohybu

Ak používateľ nastaví typ pohybu pre primárnu maticu na „Mechanický lis“, definície riadenia pohybu pre všetky ostatné objekty budú vymazané a používateľ nebude môcť definovať riadenie pohybu pre ostatné objekty.

  
Parametre potrebné na určenie pohybu mechanického lisu sú:

**Celkový zdvih**: Celkový zdvih mechanického lisu predstavuje celkový posun matrice z jej najvyššej polohy do najnižšej polohy. Mernou jednotkou v anglickom systéme je palec a v systéme SI je to milimeter.

**Tvarovací zdvih**: je vzdialenosť, ktorú prejde primárna matrica od začiatku operácie až po dolnú mŕtvu polohu.

**Aktuálny zdvih**: je vektor, ktorý udáva aktuálnu vzdialenosť, ktorú prekonala horná matrica, a jej smer pozdĺž osi pohybu.

**Počet zdvihov za sekundu**: Počet zdvihov za sekundu vyjadruje frekvenciu lisovacích zdvihov. Ide o mieru počtu zdvihov za sekundu alebo cyklov za sekundu.

**Smer**: Smer sa používa na určenie smeru, v ktorom sa bude aplikovať obrys objektu.

**Dĺžka ojnice**: Ako je vidieť na obr. 2.8.19, dĺžka ojnice môže ovplyvňovať rýchlosť piestu. Ak je dĺžka ojnice známa, je možné ju zadať do príslušného poľa. Ak nie je známa, môže sa ponechať na hodnote nula a jej vplyv na rýchlosť piestu sa nebude zohľadňovať.

**Možnosť „Forming Stroke“**: Údaje pre „Forming Stroke“ je teraz možné definovať dvoma spôsobmi:

**Presný tvarovací zdvih**: Ak je zvolená možnosť „presný tvarovací zdvih“, tvarovací zdvih sa rovná hodnote primárneho zdvihu lisovacej formy.

**Vzdialenosť medzi maticami**: Ak je zvolená možnosť „Vzdialenosť medzi maticami“, zdvih kovania = (aktuálna vzdialenosť medzi definovanými bodmi) – (zastavovacia vzdialenosť medzi definovanými bodmi)

Upraviteľné? | Prvá operácia | Ďalšia operácia | Editor krokov  
---|---|---|---  
Definícia hornej matrice | Hodnota hornej matrice sa načíta z databázy  
Typ | Áno | Áno | Áno | Nie  
Smer | Áno | Áno | Áno | Nie  
Celkový zdvih, zdvih/s, tuhosť a dĺžka ojnice | Áno | Áno | Áno | Nie  
Možnosť formovacieho zdvihu | Áno | Áno | Nie* | Nie  
  
*Ak sa horná matrica načítava z databázy, skryjú sa možnosti „tvarovací zdvih“, „tvarovací zdvih“ a „aktuálny zdvih“.

Pri zmene celkového zdvihu sa aktuálny zdvih prepočíta tak, aby sa zachovala hodnota formovacieho zdvihu.

Pri importe projektu zo staršej verzie systém automaticky nastaví metódu presného formovacieho zdvihu. Ak sa importuje projekt s kritériom zastavenia na základe vzdialenosti medzi formami, systém prejde na metódu vzdialenosti medzi formami.

**Kovanie kladivom:** Proces kovania kladivom je riadený energiou. Počas pracovného zdvihu prebieha deformácia dovtedy, kým sa celková kinetická energia nevyčerpá prostredníctvom plastickej deformácie materiálu a pružnej deformácie piestu a kovadliny v okamihu, keď sa povrchy matrice a piestu dotknú.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image029.jpg' | relative_url }})

Nastavenia riadenia pohybu kladiva

Pri kovaní kladivom sa na plastickú deformáciu obrobku využíva len časť kinetickej energie piestu. Zvyšná energia sa stráca cez kovadlinu a rám stroja. Tieto hodnoty je možné nastaviť v okne ovládania pohybu.

  
V zásade existujú dva typy kladív. Prvým je [anvil type hammer](../../pre_processor/15_movement_controls_definition/15_3_hammer.htm#15_3_1_Anvil_Type_Hammer) a druhým [counter blow hammer](../../pre_processor/15_movement_controls_definition/15_3_hammer.htm#15_3_2_Counterblow_Hammer). Vzorce a predpoklady použité pre oba typy operácií kovania kladivom sa vzťahujú na [15.3. Hammer Energy.](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/)

Pri kladive typu „Anvil“ sa obrobok spolu so spodnou sadou foriem umiestňuje na nehybné kovadlinu. Pri jednoduchom gravitačnom kladive sa piest zrýchľuje pôsobením gravitácie a akumuluje energiu.

Pohyb protirázového kladiva je možné nastaviť zaškrtnutím políčka „Protirázové kladivo“, ako je znázornené na obr. 34.1.29. Následne je možné špecifikovať aj druhý pohybujúci sa objekt kladiva, ako aj hmotnosť tohto druhého pohybujúceho sa kladiva. Hmotnosti objektov nemusia byť rovnaké, celková energia sa však rozdelí medzi obe matrice kladiva.

Použiť tabuľku úderov: Zaškrtnutím tejto možnosti môže používateľ definovať viacero úderov kladivom, ako je znázornené na obr. 34.1.30. V tomto okne musí používateľ zvoliť počet úderov a účinnosť úderu pre každý úder. Spolu s údermi môže používateľ zvoliť teplotu opätovného ohrevu po každom údere, zadať dobu zdržania a otočiť obrobok v 2D. Takto je možné navrhnúť zdržanie a presun po každom údere. Deformáciu je možné inicializovať aj spolu s opätovným ohrevom zaškrtnutím príslušného políčka, čím sa inicializuje akumulovaná deformácia po dobe výdrže pri nastavení teploty opätovného ohrevu obrobku.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image031.jpg' | relative_url }})

Tabuľka nastavení viacerých úderov kladivom

Ďalšie informácie o riadení kladivového lisu nájdete v dokumente [15.3. Hammer Energy.](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/)

**Hydraulický lis:** V režime Forming Express disponuje hydraulický lis (pozri obr. 34.1.31.) iba reguláciou otáčok. Operácia Forming obsahuje okrem regulácie rýchlosti aj reguláciu priemernej rýchlosti deformácie; informácie o nej nájdete v [15.6. Hydraulic Press.](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/). Okrem rýchlosti môže používateľ zadať limit výkonu, dobu zdržania a počet krokov zdržania.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image028.jpg' | relative_url }})

Nastavenia riadenia pohybu hydraulického lisu

**Poznámka:**

Na aktiváciu regulácie maximálnej rýchlosti je potrebné nastaviť limit výkonu.

Ďalšie informácie o riadení hydraulického lisu nájdete v kapitole [15.6. Hydraulic Press.](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

**Šnekový lis**

Jedinečnou vlastnosťou šnekového lisu (pozri obr. 34.1.32.) je spôsob jeho pohonu. Motor poháňa zotrvačník, ktorý je buď priamo spojený so šnekovým vretenom, alebo sa k nemu môže pripojiť.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image030.jpg' | relative_url }})

Nastavenia riadenia pohybu šnekového lisu

Údaje potrebné na prevádzku nástroja poháňaného šnekovým lisom sú:

**Energia:** Energia rozbehu je veličina vyjadrujúca celkovú energiu, ktorú bude zotrvačník obsahovať po dosiahnutí požadovanej rýchlosti a pred zapojením spojky. Jednotky pre energiu rozbehu sú v anglickom systéme klb-in a v systéme SI N-mm.

  
**Účinnosť vyfukovania:** Účinnosť vyfukovania predstavuje podiel celkovej energie, ktorý sa premení na energiu deformácie. Zvyšná energia sa absorbuje prostredníctvom spojkového mechanizmu, trenia a rámu stroja. Táto veličina nemá žiadne jednotky. V programe Forming Express môžeme použiť iba konštantnú hodnotu, avšak pri formovacích operáciách môže používateľ definovať aj funkciu sily. Ďalšie informácie nájdete v [15.4. Screw Press.](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/).

  
**Moment zotrvačnosti:** Moment zotrvačnosti je moment zotrvačnosti zotrvačníka. Anglické jednotky zotrvačnosti sú klb*in*s2 a jednotky SI sú N-mm*s2. Hmotnostný moment zotrvačnosti pre kruhový disk s osou Z kolmou na stred je I = 2 ET /ω2, kde ET je celková energia zotrvačníka a ω je uhlová  
rýchlosť v radiánoch za sekundu.

  
**Posun piestu alebo stúpanie vodiacich skrutiek:** Posun piestu udáva vzdialenosť, o ktorú sa skrutka posunie za jednu otáčku zotrvačníka. To pomáha pri určovaní lineárnej rýchlosti piestu. Jednotkami v anglickom systéme pre posun piestu sú palce na otáčku, zatiaľ čo jednotkami v systéme SI sú milimetre na otáčku. Ak sú známe len uhol stúpania a priemer vretena, posun ramena možno vypočítať pomocou vzorca πdsin(θt), kde d je priemer vretena a θt je uhol stúpania vretena.

  
**Použiť tabuľku úderov:** Zaškrtnutím tejto možnosti môže používateľ definovať viacero úderov, ako je znázornené na obr. 34.1.33. V tomto okne musí používateľ zvoliť počet úderov a účinnosť každého úderu. Okrem úderov môže používateľ zvoliť opätovné zahriatie po každom údere, zadať dobu zdržania a otočiť obrobok v 2D. Takže opätovné zahriatie, presun  
a je možné nastaviť dobu zdržania po každom údere.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image032.jpg' | relative_url }})

Tabuľka nastavení viacerých úderov skrutkového lisu

Ďalšie informácie o šnekovom lise nájdete v katalógu [15.4. Screw Press.](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/)

## Polohovanie

Na obr. 34.1.34. je zobrazené okno na nastavenie polohy.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image033.jpg' | relative_url }})

Okno na umiestňovanie objektov

**Automatické polohovanie** ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }})

Kliknutím na toto tlačidlo systém automaticky umiestni objekty vzhľadom na smer pohybu hornej matrice; táto možnosť sa najlepšie hodí pre jednoduché nastavenie s tromi objektmi: obrobkom, hornou matricou a spodnou matricou.

Ak sa ako typ riadenia pohybu primárnej matrice používa mechanický lis, potom sa vykoná automatické polohovanie  
prebieha v dvoch krokoch:

  1. Poloha spodnej matrice voči obrobku pri spojení s hornou matricou bez úpravy zdvihu

  2. Poloha, v ktorej horná matrica zasahuje do obrobku pri aktualizácii zdvihu.

Systém vždy aktualizuje zdvih podľa polohy objektu, pre ktorý je definovaný mechanický lis (horná matrica). Zaškrtávacie políčko „Aktualizovať zdvih“ by malo byť v rýchlych operáciách skryté.

**Umiestňovanie objektov ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }})**

Kliknutím na toto tlačidlo môže používateľ umiestniť objekty do požadovaných smerov. K dispozícii sú rôzne typy možností umiestnenia, ako napríklad [Drag](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_1_Drag_Positioning), [Offset](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_2_Offset_Positioning), [Interference](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_3_Interference_positioning), [Flip](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_6_Flip_positioning) a [Rotational](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_4_Rotational_positioning), ako je znázornené na obr. 34.1.35. Ďalšie informácie o týchto možnostiach nájdete v časti [19.Object Positioning.](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image034.jpg' | relative_url }})

Okno na umiestňovanie objektov

## Plánované polohovanie

Ak si používateľ nie je istý polohou objektu, ako je to v prípade objektov typu „Read From DB“, naplánované umiestňovanie pomôže objekty presne umiestniť.

Funkcia „Schedule positioning“ umožňuje používateľovi definovať umiestnenie objektov v nastaveniach MO pre nasledujúce operácie, pre ktoré sa nevytvára databáza (DB), tak, aby sa objekty umiestnili ešte pred vytvorením databázy počas spustenia simulácie v dávkovom režime. (Pozri obr. 34.1.36.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image035.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

## Vzťahy medzi objektmi

Účelom vzťahov medzi objektmi je definovať, ako rôzne objekty v simulácii vzájomne interagujú. Všetky objekty, ktoré sa v priebehu simulácie môžu navzájom dotýkať, musia mať definovaný kontaktný vzťah. V systéme Forming Express sa automaticky definuje vzťah medzi obrobkom a formami a vlastný kontakt pre obrobok, potom sa vygeneruje kontakt, keď používateľ klikne na ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}), ako je znázornené na obr. 34.1.37. Správa o vygenerovaných kontaktoch sa zobrazí na karte Správy pod grafickým oknom.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image036.jpg' | relative_url }})

Okno na generovanie kontaktov

Používateľ si môže zvoliť typ trenia – šmykové alebo Coulombovo – a nastaviť koeficient trenia. Mazivo použité na nástroji má veľký vplyv na veľkosť trenia medzi nástrojom a obrobkom. Trenie zase ovplyvňuje tok kovu na kontaktných plochách.

  
Pre šmykové trenie sú uvedené typické hodnoty, ako je znázornené nižšie,

(0,08) pre procesy tvárnenia za studena (karbidové matrice)

(0,12) pre procesy tvárnenia za studena (oceľové formy)  
(0,25) pre procesy tepelného tvárnenia  
(0,3) pre procesy mazaného kovania za tepla  
(0,7) pre procesy horúceho kovania bez mazania (nasucho)  
(0,4) pre procesy tvárnenia hliníka

Hodnotu koeficientu prenosu tepla vedením si môže užívateľ nastaviť sám; systém zároveň ponúka aj typické hodnoty, a to:  
(1 N/s/mm/°C alebo 0,0003 Btu/s/in²/°F) pre stav voľného pokoja  
(1 N/s/mm/°C alebo 0,0003 Btu/s/in²/°F) pre obytné priestory  
(11 N/s/mm/°C alebo 0,004 Btu/s/in²/°F) pre tvárnenie

## Stanovenie primárneho zdvihu matrice alebo celkovej doby spracovania

Primárny zdvih formy (pozri obr. 34.1.38.) určuje celkovú dĺžku pohybu formy počas operácie. Ide o odhad celkového zdvihu formy v rámci jednej operácie. Používa sa na stanovenie hodnôt časových krokov.  
Ak nie je zaškrtnuté políčko „presná hodnota“, približný cieľový posun nástroja bude predstavovať približne 125 % zadaného hodnoty.  
Pomocou kurzora myši môže používateľ určiť hodnotu primárneho zdvihu výseku výberom dvoch bodov na objektoch.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image038.jpg' | relative_url }})

Okno s definíciou celkového zdvihu primárneho lisovacieho nástroja

Ak používateľ ako ovládacie prvky pohybu použije funkciu „Načítať“, namiesto okna „Primárny zdvih matrice“ sa zobrazí okno „Celkový čas spracovania“; tento čas sa používa na odhad hodnôt krokovania.

**Základný zdvih matrice pre mechanický lis [metóda presného tvárnenia]:**

V prípade mechanického lisu sa zobrazí platný rozsah. (0 ~ „Celkový zdvih“) (Pozri obr. 34.1.39.)

Ak je celkový primárny zdvih matice 0 alebo sa nachádza mimo platného rozsahu, vstup je neplatný a rozsah sa zobrazí červenou farbou.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image039.jpg' | relative_url }}) ![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image040.jpg' | relative_url }})

(a) V prvej operácii (b) V nasledujúcej operácii 

Možnosť základného zdvihu lisovacej matrice s metódou zdvihu Exact Forming 

Existujú 3 spôsoby, ako určiť presný zdvih formovania:

  1. Používateľ môže zadať presný tvarovací zdvih pre celkový primárny zdvih formy.

  2. Ak je aktuálna poloha matrice v hornej mŕtvej polohe, používateľ môže stlačiť tlačidlo **Poloha hornej mŕtvej polohy** (nástroj ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }})) alebo túto polohu skontrolovať v nasledujúcej operácii. Keď používateľ stlačí tlačidlo / skontroluje polohu hornej mŕtvej polohy (nástroj ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }})), v nasledujúcich operáciách sa zruší zaškrtnutie políčka „Presná hodnota“. Tvarovací zdvih je nastavený na hodnotu rovnú celkovému zdvihu. Vykonáva sa alebo je naplánované automatické polohovanie. V prvej operácii sa primárny posun matrice aktualizuje na správny tvarovací zdvih. V nasledujúcich operáciách sa tvarovací zdvih aktualizuje po vykonaní naplánovaného polohovania.

| Prvá operácia | Ďalšia operácia | Editor krokov  
---|---|---|---  
Je definovaná horná matrica | Horná matrica je načítaná z databázy  
**Celkový zdvih primárneho lisovacieho nástroja** | Zobrazuje vypočítaný tvárniaci zdvih | Približný zdvih lisovacieho nástroja, ktorý sa použije na výpočet DSMAX | N/A | N/A  
  
Ak sa v prvej operácii použije tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}), deaktivujte tlačidlá ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) pre hornú aj dolnú mŕtvu polohu, kým používateľ znovu nenavštívi stránku. V nasledujúcej operácii, ak bude zaškrtnuté políčko sprievodcu, systém  
odstráňte všetky predchádzajúce naplánované polohy objektov 2 a 3.

  1. Ak je aktuálna poloha matrice v dolnej mŕtvej polohe, používateľ môže stlačiť tlačidlo **Dolná mŕtva poloha** (![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }})) alebo skontrolovať polohu dolnej mŕtvej polohy v nasledujúcej operácii. Ak používateľ stlačí tlačidlo / skontroluje polohu hornej mŕtvej polohy (![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }})), v nasledujúcich operáciách sa odznačí políčko „Presná hodnota“. Tvarovací zdvih je nastavený na hodnotu 0. Vykoná sa alebo naplánuje automatické polohovanie. Prvá operácia aktualizuje hodnotu primárneho posunu matrice o správny tvarovací zdvih. V nasledujúcej operácii sa vypočíta správny tvarovací zdvih po vykonaní naplánovaného polohovania.

| Prvá operácia | Ďalšia operácia | Editor krokov  
---|---|---|---  
Je definovaná horná matrica | Horná matrica je načítaná z databázy  
**Celkový posuv primárneho lisovacieho nástroja** | Zobrazuje vypočítaný tvarovací zdvih | Približný posuv lisovacieho nástroja, ktorý sa použije na výpočet DSMAX | N/A | N/A  
  
Ak sa pri prvej operácii použije ktorékoľvek z tlačidiel „Horná mŕtva poloha“ alebo „Spodná mŕtva poloha“ (![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }})), obe tlačidlá „Horná mŕtva poloha“ a „Spodná mŕtva poloha“ (![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }})) zostanú deaktivované, kým používateľ stránku znovu nenavštívi. 

**V nasledujúcich krokoch:**

Ak je zaškrtnuté políčko pre hornú alebo dolnú úvrati, systém vymaže naplánované polohovanie objektov 2 a 3.  
Ak je zaškrtnuté políčko BDC, zobrazí sa chybová správa o tom, že pre hornú matricu nie je naplánované polohovanie s ohľadom na interferenciu.  
Ak nie je zaškrtnuté políčko BDC, zobrazí sa varovná správa, že pre hornú matricu nie je naplánované polohovanie s ohľadom na interferenciu.

**Základný zdvih lisovacej formy pre mechanický lis [metóda merania vzdialenosti medzi formami]:**

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image041.jpg' | relative_url }}) ![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image042.jpg' | relative_url }})

(a) V prvej operácii (b) V nasledujúcej operácii 

Možnosť primárneho zdvihu matice s metódou „Vzdialenosť medzi matricami“ v prvej operácii

Ak používateľ zvolí ako typ tvárneho zdvihu metódu „Vzdialenosť medzi maticami“, potom,

V prvej operácii bude posuv **celkovej primárnej matrice** deaktivovaný a nastavený systémom.

V časti Ďalšie operácie bude políčko **Presná suma** odznačené a deaktivované. 

V nasledujúcich operáciách sa **celkový posun primárnej matrice** použije výlučne na výpočet veľkosti kroku definovanej systémom.

V ďalšom kroku je možné nastaviť presné ovládacie prvky brzdenia.

## Ovládacie prvky na zastavenie

Parametre ukončenia určujú čas, po uplynutí ktorého sa simulácia ukončí. Simuláciu je možné ukončiť na základe maximálneho počtu simulovaných časových krokov, maximálneho zdvihu, maximálneho zaťaženia primárnej matrice, pomeru kontaktu k celkovej ploche povrchu alebo vzdialenosti medzi matricami. Simulácia sa zastaví, keď bude splnená podmienka ktoréhokoľvek z týchto parametrov ukončenia. (Pozri obr. 34.1.41.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image043.jpg' | relative_url }})

Okno ovládacích prvkov na zastavenie

**Maximálny zdvih matrice**: Ukončí simuláciu, keď celkový posun (SMAX) primárnej matrice dosiahne  
uvedená hodnota.

**Max. zaťaženie:** Ukončí simuláciu, keď zložka zaťaženia v smere X alebo Y primárneho telesa dosiahne hodnotu LMAX v smere X alebo Y. Zvyčajne sa používa v prípadoch, keď je riadenie pohybu primárneho objektu založené na rýchlosti alebo je určené používateľom.

**Pomer kontaktnej plochy:** Pomer kontaktnej plochy je pomer plochy, ktorá je v kontakte s lisovacími maticami, k celkovej povrchovej ploche polotovaru. Ak tento pomer prekročí stanovenú hodnotu, simulácia sa zastaví.

**Vzdialenosť medzi objektmi:** Ukončí simuláciu, keď vzdialenosť medzi referenčnými bodmi (MDSOBJ) na dvoch objektoch dosiahne zadanú hodnotu. Pomocou kurzora myši musí používateľ vybrať dva body na objektoch, aby zadal vzdialenosť. Ak používateľ už definoval referenčný bod pre formy, ako je uvedené v časti Geometria v položke Ďalšie možnosti geometrie, potom výberom objektov pre Objekt1 a Objekt2 sa na displeji zvýrazní vzdialenosť. Nakoniec musí používateľ zadať hodnotu vzdialenosti, pri ktorej sa má simulácia zastaviť, ako je znázornené na obr. 34.1.42.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image044.jpg' | relative_url }})

Definícia vzdialenosti medzi objektmi, ktoré zastavujú riadenie

V prípade mechanického pohonu lisu sa vždy kontroluje maximálny zdvih matrice, ktorý je deaktivovaný a musí sa rovnať celkovému zdvihu (pozri obr. 34.1.43.).

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image045.jpg' | relative_url }}) ![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image046.jpg' | relative_url }})

(a) Pre presný tvarovací zdvih – voliteľná funkcia mechanického lisu (b) Pre vzdialenosť medzi lisovacími nástrojmi – voliteľná funkcia mechanického lisu

Možnosť základného zdvihu lisovacej matrice s metódou zdvihu Exact Forming 

Ak bola zvolená možnosť **Presný tvarovací zdvih**, políčko „Vzdialenosť medzi objektmi“ zostane nezaškrtnuté a táto funkcia bude deaktivovaná (obr. 34.1.43 (a)).

  
Ak bola zvolená možnosť **Vzdialenosť medzi výsekovými formami**, vzdialenosť medzi objektmi sa skontroluje a deaktivuje (obr. 34.1.43.(b).)

  
Ak bola zvolená možnosť **Vzdialenosť medzi formami**, používateľ musí určiť vzdialenosť medzi objektmi a referenčnými bodmi (obr. 34.1.43.(b)).

  
Ďalšie informácie o kontrolách zastavenia nájdete v [9.3.10. Temperature stopping contorls](../../pre_processor/9_simulation_controls/9_3_stopping_controls.htm#9.3.10._Temperature_stopping_control)

## Ovládacie prvky simulácie

Systém DEFORM rieši časovo závislé nelineárne úlohy generovaním série riešení metódou konečných prvkov (FEM) v diskrétnych časových krokoch. V každom časovom kroku sa rýchlosti, teploty a ďalšie kľúčové premenné každého uzla v sieti konečných prvkov určujú na základe okrajových podmienok, termomechanických vlastností materiálov obrobku a prípadne riešení z predchádzajúcich krokov. Ostatné stavové premenné sa odvodzujú z týchto kľúčových hodnôt a aktualizujú sa pri každom časovom kroku. Dĺžka tohto časového kroku a počet simulovaných krokov sa určujú na základe informácií zadaných v ponuke nastavení krokov. Obr. 34.1.44. znázorňuje možnosti ovládania simulácie.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image047.jpg' | relative_url }})

Okno ovládacích prvkov simulácie v systémovom režime

Používateľ musí zadať číslo počiatočného kroku, celkový počet krokov, veľkosť kroku, ktorú chce uložiť, a definíciu kroku (posun formy alebo časový prírastok). V programe Forming Express je možné ako definíciu kroku použiť iba konštantný posun formy a konštantný časový prírastok. Pre všetky ovládacie prvky pohybu okrem zaťaženia sú ako typy definície kroku k dispozícii posun formy aj časový prírastok, pre ovládacie prvky pohybu zaťaženia je povolený iba časový prírastok.

**Typ systému: Krok – konštantný posun matrice:**

V prípade mechanického lisu sa pri tvárnení rýchlosť kroku vypočíta podľa vzorca [(celkový primárny zdvih matrice) / (počet krokov)] × 1,2, a to bez ohľadu na to, či je zaškrtnutá možnosť „presná hodnota“ alebo nie.  
Pri nemekanických operáciách lisovania pri tvárnení sa veľkosť kroku rýchleho posuvu vypočíta ako [(celkový primárny zdvih matrice) / (počet krokov)], ak je zaškrtnutá možnosť „presná hodnota“ (pozri obr. 34.1.45.).  
V prípade nemekanických lisovacích operácií pri tvárnení sa rýchlosť kroku vypočíta podľa vzorca [(celkový primárny zdvih lisovacej formy) / (počet krokov)] × 1,2, ak nie je zadaná presná hodnota.

**Typ používateľa – Konštanta kroku posunu matrice**: Táto funkcia umožní používateľom zadať vlastnú veľkosť kroku. Používateľ by mal zvoliť vhodnú veľkosť kroku tak, aby na základe počtu krokov splnil podmienku zastavenia.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image048.jpg' | relative_url }})

Okno ovládacích prvkov simulácie v užívateľskom režime

**Počet simulačných krokov (NSTEP)**  
Parameter „Počet simulačných krokov“ určuje počet krokov, ktoré sa majú spustiť od počiatočného čísla kroku. Simulácia sa zastaví po vykonaní tohto počtu simulačných krokov, pokiaľ sa nespustí príkaz na zastavenie simulácie alebo ak simulácia nenarazí na problém. Napríklad, ak je počiatočné číslo kroku -35 ([NSTART](/docs/en/keyword_documentation/n/nstart/)) a je špecifikovaných 30 krokov ([NSTEP](/docs/en/keyword_documentation/n/nstep/)), simulácia sa zastaví po 65. kroku, pokiaľ sa skôr nespustí iný príkaz na zastavenie.

**Krok prírastku pri ukladaní (STPINC)**

Krok prírastku ([STPINC](/docs/en/keyword_documentation/s/stpinc/)), ktorý sa má uložiť do databázy, určuje počet krokov, ktoré systém uloží do databázy. Pri spustení simulácie sa musí vypočítať každý krok, ten však nemusí byť nutne uložený do databázy. Uložením väčšieho počtu krokov sa zachová viac informácií o procese, čo však bude vyžadovať väčší úložný priestor.

**Ovládanie krokového posunu ([DSMAX](/docs/en/keyword_documentation/d/dsmax/)/[DTMAX](/docs/en/keyword_documentation/d/dtmax/))**

Veľkosť kroku riešenia je možné riadiť časovým krokom alebo posunom primárnej matrice. Ak je špecifikovaný zdvih na krok, primárna matrica sa v každom časovom kroku posunie o zadanú hodnotu. Celkový posun primárnej matrice bude rovný posunu na krok vynásobenému celkovým počtom krokov. Ak je špecifikovaný čas na krok, použije sa časový interval na krok. Posun matrice na krok bude rovný časovému kroku vynásobenému rýchlosťou matrice.

Počet zdvihov na krok je často intuitívnejší. Čas na krok je však potrebné špecifikovať pri každej úlohe, v ktorej nedochádza k pohybu matice (napríklad pri prenose tepla), alebo pri každej úlohe, kde sa používa regulácia sily.

V operáciách tvárnenia je k dispozícii vylepšené nastavenie riadenia krokového posunu, ktoré teraz zahŕňa krokové funkcie závislé ako od času, tak aj od zdvihu. To znamená, že veľkosť kroku (či už ide o čas na krok alebo zdvih na krok) je teraz možné definovať ako funkciu času alebo zdvihu. Táto funkcia umožňuje jemnejšie rozlíšenie uložených informácií o modeli tam, kde je to žiaduce. (typicky ku koncu zdvihu, kde môžu nastať prudké zmeny zaťaženia formy, plnenia dutiny alebo tvorby otrepov) – ďalšie informácie nájdete v dokumente [9.2. Defining step.](/docs/en/pre_processor/9_simulation_controls/9_2_defining_step/)

**Pokročilé ovládacie prvky simulácie**

Pokročilé ovládacie prvky simulácie ponúkajú možnosti výberu riešiteľov deformácií; k nim sa dostanete pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_advanced_button.jpg' | relative_url }}). Pre 2D Forming Express sú k dispozícii iba riešitelia deformácií Skyline, MUMPS a Spools (pozri obr. 34.1.46.). Predvolene je vybraný riešiteľ MUMPS.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image049.jpg' | relative_url }})

Nastavenia pokročilých ovládacích prvkov simulácie

Operácia tvarovania ponúka v expertnom režime viac možností ovládania simulácie; podrobnosti o týchto možnostiach nájdete v [9\. Simulation Controls.](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

## Vytvoriť databázu

**Overiť údaje** ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})

Systém skontroluje údaje. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvoriť databázu** ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) sa vygeneruje databáza pre inštaláciu. (Pozri obr. 34.1.47.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image050.jpg' | relative_url }})

Okno „Vytvoriť databázu“

Ak používateľ potrebuje niektorú z pokročilých možností, ktoré nie sú k dispozícii v režime Forming Express, môže k nim získať prístup bez straty definovaných údajov v operácii Forming Express prostredníctvom prechodu do režimu Forming. Táto možnosť je k dispozícii v ponuke pravého tlačidla myši v editore operácií, ako je znázornené na obr. 34.1.48. Ďalšie podrobnosti o tomto prechode na vyššiu úroveň operácie nájdete v [6.6.4. Upgrading Operations.](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_6_operations_management/6_6_4_upgrading_operations/)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image051.jpg' | relative_url }})

Presun položky „Forming Express“ do pravého menu v rámci operácie formovania

Po vytvorení databázy musí používateľ vybrať kartu „Režim simulácie MO“, aby odoslal problém na simuláciu. Ďalšie informácie o režime simulácie MO nájdete v [6.2. MO Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/). Akonáhle sa na karte „Simulácia dokončená“ zobrazí príslušná správa, môže používateľ v režime MO Post skontrolovať výsledky. Ďalšie informácie o režime MO Post nájdete v [ 6.3. MO Post layout.](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/).

**Súvisiace témy:**

[34.2. 3D Forming Express Setup](/docs/en/operation_templates/34_forming_express/34_2_3d_forming_express_setup/)

[Promote Forming Express to Forming operation](../../integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_6_operations_management/6_6_4_upgrading_operations.htm#Fig._6.6.4.4._Forming_express_operation_after_promoting_it_to_forming_operation)

[6.2. MO Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. MO Post layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[33.1. 2D Forming Setup](/docs/en/operation_templates/33_forming/33_1_2d_forming_setup/)

[33.2. 3D Forming Setup](/docs/en/operation_templates/33_forming/33_2_3d_forming_setup/)
