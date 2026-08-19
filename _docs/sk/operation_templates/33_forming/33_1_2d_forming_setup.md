---
lang: sk
title: "33.1. Nastavenie 2D tvárnenia"
---

# 33.1. Nastavenie 2D tvárnenia

33.1.1. Typ geometrie

33.1.2. Zoznam materiálov

33.1.3. Pridať objekty

33.1.4. Obrobok

  * Geometria

  * Sieťovina

  * Materiál

  * Okrajové podmienky

  * Ovládanie pohybu

  * Nehnuteľnosť

  * Inicializovať

33.1.5. Polohovanie

33.1.6. Plánované umiestnenie

33.1.7. Kontakt

33.1.8. Ovládacie prvky na zastavenie

33.1.9. Ovládacie prvky simulácie

33.1.10. Vytvorenie databázy

## Typ geometrie

V module 2D Forming je v súčasnosti možné nastaviť štyri typy geometrických modelov ([GEOTYP](/docs/en/keyword_documentation/g/geotyp/)), ako je znázornené na obr. 33.1.1.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image001.jpg' | relative_url }})

Okno „Typ 2D geometrie“

  * **Osovo symetrický**

  * **Rovinné deformácie**

  * **Krútiaci moment**

  * **Rovinné napätie**

Ďalšie informácie o týchto typoch geometrie nájdete v časti [9.1.2._Geometry_type_(GEOTYP)_[2D]](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\])   
Ovládacie prvky simulácie sú vysvetlené na konci tejto kapitoly v časti 33. 1.9. Ovládacie prvky simulácie

## Zoznam materiálov

Aby simulácia dosiahla vysokú úroveň presnosti, je dôležité poznať vlastnosti materiálu, ktoré sú potrebné na špecifikáciu materiálu použitého v programe DEFORM.

  
Pri nastavovaní simulácie je potrebné pre objekty špecifikovať vlastnosti materiálov. V operácii MO Forming je možné načítať všetky materiály potrebné pre danú operáciu naraz a požadovaný materiál vybrať neskôr pri nastavovaní úlohy. Používateľ môže pridať materiál výberom možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) „Načítať údaje o materiáli z knižnice“, ako je znázornené na obr. 33.1.2. Používateľ môže vybrať požadovaný materiál z kategórií a potom kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}), ako je znázornené na obr. 33.1.3.

  
![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image002.jpg' | relative_url }})

Okno „Zoznam materiálov“

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image003.jpg' | relative_url }})

Importovať materiál z okna knižnice

  
(alebo) 

Ďalším spôsobom pridania materiálu je kliknutie na ikonu materiálu na karte prehliadača, čím sa zobrazí zoznam materiálov z knižnice zoradených do rôznych kategórií, ako je znázornené na obr. 33.1.4. Vyberte požadovaný materiál a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}). Používateľ môže požadovaný materiál pridať aj pomocou funkcie „drag and drop“ (ťahaj a pusť) do okna materiálu.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image004.jpg' | relative_url }})

Pridať materiál z karty „Materiál“ v programe Explorer

  
(alebo) 

V okne so zoznamom materiálov je možné pridať nový materiál kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Po pridaní materiálu kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vyberte príslušnú kartu, kde zadáte potrebné údaje pre simuláciu, ako je znázornené na obr. 33.1.5.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image005.jpg' | relative_url }})

Pridať materiál z okna Zoznam materiálov

**Import údajov o materiáloch zo súboru** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}): Importuje údaje o materiáloch zo súboru s príponou .Key alebo .DB.  
**Načítať údaje o materiáli z knižnice** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}): Importuje materiál z knižnice.  
**Uloženie údajov o materiáli do súboru**![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) : Uloží materiál do súboru.  
**Uloženie údajov o materiáli do knižnice**![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ uložiť materiál do knižnice a v budúcnosti ho podľa potreby opäť načítať pre ďalšie simulácie.

**Zloženie zmesi**

Materiály typu „zmes“ ([MSTMTR](/docs/en/keyword_documentation/m/mstmtr/)) sa používajú v prípade, že sa v simulácii má modelovať fázová premena. Premenlivý materiál sa modeluje ako „zmes“ fáz, z ktorých sa skladá. Napríklad uhlíková oceľ sa môže modelovať ako zmes austenitu, perlitov, bainitu a martenzitu. Ak je definovaný zmesový materiál, je potrebné definovať pravidlá premeny, ktoré riadia premenu jednej fázy na druhú. (Pozri obr. 33.1.6.)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image004.jpg' | relative_url }})

Pridanie zmesi materiálov

  
**Kopírovať vlastnosti ![]({{ '/assets/icons/pre_icons/mo_copy_properties.jpg' | relative_url }})**

Slúži na kopírovanie bežných vlastností materiálov, ako sú plastické, elastické, tepelné atď., z jedného materiálu do druhého pri vytváraní/definovaní údajov o materiáli, ako je znázornené na obr. 33.1.7. V tomto dialógovom okne je potrebné vybrať zdroj a cieľ kopírovania vlastností, ako aj samotné vlastnosti, ktoré sa majú skopírovať.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image005.jpg' | relative_url }})

Okno „Kopírovať vlastnosti materiálu“

**Previesť jednotky ![]({{ '/assets/icons/pre_icons/mo_convert_units_button.jpg' | relative_url }})**

Slúži na prevod jednotkového systému aktuálne vybraného materiálu zo zoznamu materiálov zo systému SI na anglický systém alebo naopak, prípadne môže používateľ použiť akýkoľvek iný násobný koeficient, ako je znázornené na obr. 33.1.8. Stlačením tlačidla ![]({{ '/assets/icons/pre_icons/mo_si_to_english_button.jpg' | relative_url }}) alebo ![]({{ '/assets/icons/pre_icons/mo_english_to_si_button.jpg' | relative_url }}) sa zobrazia príslušné násobné koeficienty pre prevod z ![]({{ '/assets/icons/pre_icons/mo_si_to_english_button.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_english_to_si_button.jpg' | relative_url }}); stlačením tlačidla ![]({{ '/assets/icons/pre_icons/mo_convert_button.jpg' | relative_url }}) sa prevod vykoná a okno prevodu sa zatvorí. Túto prevodnú tabuľku je možné uložiť pomocou tlačidla „Save“ a je možné ju tiež upraviť pomocou programu WordPad/Notepad a opätovne načítať do súboru UNITCONV.DAT pomocou tlačidla „Load“.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image006.jpg' | relative_url }})

Okno pre prevod jednotiek

## **Pridať objekty**

Používateľ môže pridať požadovaný počet objektov pre simuláciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Na obr. 33.1.9 sú zobrazené tri objekty pridané pre jednoduchú operáciu zúženia. 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image007.jpg' | relative_url }})

Okno „Objekty“

## **Obrobok**

Na tejto stránke môže používateľ nastaviť požadovanú teplotu pre objekt a vybrať typ objektu, ako je znázornené na obr. 33.1.10. Pre obrobok je štandardne vybraný typ objektu „Plast“ a používateľ môže tiež importovať údaje o objekte z iných databázalebo zo súborov Keyfile z používateľom definovanej knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) alebo z adresára úlohy ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a dokonca môže údaje o objekte uložiť do súboru Keyfile v používateľom definovanej knižnici ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}) alebo v adresári úlohy ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) pomocou príslušných tlačidiel.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image010.jpg' | relative_url }})

Okno obrobku

###   
**Geometria**

Okno „Geometria“ slúži na vytvorenie geometrie objektu (pozri obr. 33.1.11.).

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image009.jpg' | relative_url }})

Okno s definíciou geometrie

**Definovať primitív ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }})**

**Pre osovo symetrický alebo torzný typ**

Na stránke „Geometrické primitívy“ sa nachádza šesť základných tvarov, ktoré možno použiť na vytvorenie geometrických útvarov, ako je znázornené na obr. 33.1.12. V každom prípade musí používateľ prispôsobiť rozmery tak, aby zodpovedali danej úlohe.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image006.jpg' | relative_url }})

Okno s geometrickými primitívami pre osovo symetrické a torzné modely

**Pre typ rovinného deformovania alebo rovinného napätia**

Na stránke „Geometrické primitívy“ sa nachádzajú tri základné tvary, ktoré možno použiť na vytvorenie geometrických útvarov, ako je znázornené na obr. 33.1.13. V každom prípade musí používateľ prispôsobiť rozmery tak, aby zodpovedali danej úlohe.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image007.jpg' | relative_url }})

Okno s geometrickými primitívami pre rovinné deformácie a napätia

**Skontrolujte**![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})

Po vytvorení geometrie objektu sa aktivuje tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Je potrebné skontrolovať orientáciu geometrie. To je možné urobiť kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Zobrazí sa okno „Skontrolujte a opravte geometriu“, ako je znázornené na obr. 33.1.14. Geometria sa opraví, ak obsahuje nejaké chyby, po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}), ako je znázornené na obr. 33.1.14. Po oprave geometrie alebo ak geometria neobsahuje žiadne chyby, zobrazí sa správa „Geometria je správna“ a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Ďalšie informácie nájdete v časti [12.1. 2D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/) [Check Geometry](../../pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining.htm#Check_Geometry). 

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image008.jpg' | relative_url }})

Okno „Skontroluj a oprav geometriu“

  
**Scale![]({{ '/assets/icons/pre_icons/mo_scale_label.jpg' | relative_url }}) **

Geometriu je možné pri formovacích operáciách zmenšiť alebo zväčšiť tak, aby zohľadňovala teplotnú rozťažnosť, a to stanovením zmenšovacieho alebo zväčšovacieho koeficientu (pozri obr. 33.1.15.). Zmenšovací alebo zväčšovací koeficient je možné vypočítať na základe teplotného rozdielu a údajov o materiáli závislých od teploty. Upravenú geometriu je možné uložiť v rôznych formátoch na ukladanie geometrie. 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image012.jpg' | relative_url }})

Okno „Mierka Geo“

**Späť**![]({{ '/assets/icons/pre_icons/mo_reverse_label.jpg' | relative_url }})

Táto funkcia obráti orientáciu geometrie. Pri geometrii s jedným okruhom musí byť orientácia 2D geometrie vždy smerom dovnútra; pri geometrii s viacerými okruhmi môže mať okruh, ktorý sa nachádza v oboch oblastiach, orientáciu na ktorúkoľvek stranu, avšak musí byť definovaná topológia.

**Ohraničenie výrezu** ![]({{ '/assets/icons/pre_icons/mo_extract_border_button.jpg' | relative_url }})

Táto funkcia extrahuje geometrické údaje z aktuálneho objektu s mriežkou v databáze pre všetky typy objektov s výnimkou tuhého objektu.

**Geometria konštrukcie ![]({{ '/assets/icons/pre_icons/mo_construct_by_substraction_button.jpg' | relative_url }}) **

Táto voľba slúži na vytvorenie geometrie odpočítaním geometrie iných objektov, ktoré už existujú. Tu je potrebné určiť počiatočný bod, šírku a výšku geometrie objektu, od ktorej sa majú odpočítať ostatné geometrie, ako je znázornené na obr. 33.1.16.  
. 

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image011.jpg' | relative_url }})

Okno „Vytvoriť geometriu“

**Upraviť** ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }})

Možnosť „Editácia geometrie“ slúži na vytvorenie geometrie objektu alebo na úpravu existujúcej geometrie. Importovanú geometriu je možné upravovať v okne „Editácia geometrie“. Na stránke „Geometria“ kliknite na označenie ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a prezrite si dostupné možnosti na vytvorenie a úpravu geometrie, ako je znázornené na obr. 33.1.17.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image012.jpg' | relative_url }})

Okno „Upraviť geometriu“

Nižšie sú vysvetlené rôzne možnosti úpravy 2D geometrie,

**Vybrať** ![]({{ '/assets/icons/pre_icons/mo_select_icon.jpg' | relative_url }}): slúži na výber vrcholu alebo hrany geometrie.

**Výber oblasti**![]({{ '/assets/icons/pre_icons/mo_area select.jpg' | relative_url }}): slúži na výber geometrie viacerých prvkov v rámci obdĺžnika.

**Vytvoriť Loop![]({{ '/assets/icons/pre_icons/mo_create_loop.jpg' | relative_url }})**: slúži na vytvorenie geometrickej slučky vytvorením bodov a ich prepojením.

**Pridať bod do slučky** ![]({{ '/assets/icons/pre_icons/mo_add_points_to_loop.jpg' | relative_url }}): slúži na pridanie nových bodov do existujúcej slučky.

**Odstránenie bodu** ![]({{ '/assets/icons/pre_icons/mo_delete point.jpg' | relative_url }}): slúži na odstránenie bodu zo slučky.

**Zaoblenie rohu** ![]({{ '/assets/icons/pre_icons/mo_round_corner.jpg' | relative_url }}): slúži na vytvorenie zaoblenia v zvolenom bode.

**Nastavenie uhla** ![]({{ '/assets/icons/pre_icons/mo_set_angle.jpg' | relative_url }}): slúži na zmenu uhla hrany.

**Move![]({{ '/assets/icons/pre_icons/mo_move.jpg' | relative_url }}) **: slúži na presunutie bodu ťahaním na iné miesto.

**Posun na stredovú čiaru** ![]({{ '/assets/icons/pre_icons/mo_move_to_centerline.jpg' | relative_url }}) : slúži na posunutie najbližšieho bodu slučky na stredovú čiaru

**Offset![]({{ '/assets/icons/pre_icons/mo_offset.jpg' | relative_url }}) **: slúži na zmenu veľkosti geometrickej slučky.

**Nastaviť prvý bod ![]({{ '/assets/icons/pre_icons/mo_make_first_point.jpg' | relative_url }})**: slúži na nastavenie vybraného bodu ako prvého bodu v slučke; táto funkcia sa používa pri uzavretej slučke; ako prvý bod nemožno vybrať stred oblúka.

**Zmena smeru** ![]({{ '/assets/icons/pre_icons/mo_reverse_direction.jpg' | relative_url }}): slúži na zmenu smeru slučky s cieľom zmeniť orientáciu geometrie. Geometria by mala byť vytvorená proti smeru hodinových ručičiek; ak je geometria vytvorená v smere hodinových ručičiek, pomocou tejto možnosti môžeme zmeniť smer slučky.

**Uzavretá slučka** ![]({{ '/assets/icons/pre_icons/mo_close_loop.jpg' | relative_url }}): slúži na uzavretie otvorenej slučky.

**Rozdelenie slučky**![]({{ '/assets/icons/pre_icons/mo_split_loop.jpg' | relative_url }}): slúži na rozdelenie slučky vo vybranom bode.

**Podslučka** ![]({{ '/assets/icons/pre_icons/mo_sub_loop.jpg' | relative_url }}): slúži na výber vnútornej slučky ako podslučky v prípade topológie s viacerými slučkami; jej výberom môžeme priradiť materiál k geometrii s viacerými slučkami.

**Spojenie slučiek** ![]({{ '/assets/icons/pre_icons/mo_join_loop.jpg' | relative_url }}): slúži na spojenie dvoch slučiek výberom slučiek, ktoré sa majú spojiť; koncový bod prvej slučky sa spojí s prvým bodom druhej slučky.

**Spojiť všetky slučky** ![]({{ '/assets/icons/pre_icons/mo_join_all_loops.jpg' | relative_url }}) : slúži na zlúčenie všetkých slučiek.

**Odstrániť vybrané ![]({{ '/assets/icons/pre_icons/mo_delete_selected.jpg' | relative_url }})**: slúži na odstránenie vybraných slučiek alebo hrán.

**Odstrániť nevybrané** ![]({{ '/assets/icons/pre_icons/mo_delete_unselected.jpg' | relative_url }}) : slúži na odstránenie nevybraných hrán slučiek.

**Zobraziť Vertex![]({{ '/assets/icons/pre_icons/mo_show_vertex.jpg' | relative_url }})**: slúži na zobrazenie vrcholov geometrie.

**Zobraziť čísla vrcholov** ![]({{ '/assets/icons/pre_icons/mo_show_vertex_numbers_icon.jpg' | relative_url }}) : slúži na zobrazenie čísel vrcholov geometrie.

**Zobraziť vnútro** ![]({{ '/assets/icons/pre_icons/mo_show_inside.jpg' | relative_url }}): slúži na zobrazenie orientácie geometrie.

**Zobraziť smer hrany** ![]({{ '/assets/icons/pre_icons/mo_show_edge_direction.jpg' | relative_url }}): slúži na znázornenie smeru vytvorenej slučky.

**Zobraziť materiál** ![]({{ '/assets/icons/pre_icons/mo_material_icon.jpg' | relative_url }}): slúži na načítanie a priradenie materiálu k oblasti geometrie.

**Mriežkové čiary**: V zobrazenom okne sa zobrazujú mriežkové čiary v horizontálnom a vertikálnom smere. (Pozri obr. 33.1.18.)

**Body mriežky**: V okne zobrazenia sa zobrazujú body mriežky v horizontálnom a vertikálnom smere. (Pozri obr. 33.1.18.)

**Mriežka: Žiadna**: Ak je táto voľba zvolená, body mriežky a čiary mriežky v horizontálnom a vertikálnom smere sa v okne zobrazenia nezobrazujú. (Pozri obr. 33.1.18.)

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image013.jpg' | relative_url }})

Okno definície mriežky

**Zobraziť os** ![]({{ '/assets/icons/pre_icons/mo_show_axis.jpg' | relative_url }}) : Zobrazí os v okne zobrazenia

**Zobraziť stredovú čiaru** ![]({{ '/assets/icons/pre_icons/mo_show_centreline.jpg' | relative_url }}) : Zobrazí stredovú čiaru v okne zobrazenia

**Zmestiť všetko** ![]({{ '/assets/icons/pre_icons/mo_fit_all_icon.jpg' | relative_url }}) : Zmestí všetky zobrazené objekty do aktuálneho zobrazenia.

**Zväčšenie rámčeka** ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) : Funkcia zväčšenia okna umožňuje podrobné preskúmanie malej oblasti aktuálne definovaných objektov. Oblasť priblíženia sa vyberie podržaním klávesov Ctrl + Alt a kliknutím ľavým tlačidlom myši, pričom ťahaním myši ohraničíte vybranú oblasť zobrazeným rámčekom. Po uvoľnení tlačidla myši sa vybraná oblasť vyplní v okne zobrazenia.  
**Zoom** ![]({{ '/assets/icons/pre_icons/mo_zoom_icon.jpg' | relative_url }}): Funkcia zoomu dynamicky mení veľkosť oblasti objektu, ktorá vyplňuje aktívne zobrazenie. Veľkosť zobrazenia je možné zmeniť tak, že podržíte kláves Alt, kliknete ľavým tlačidlom myši v aktívnom zobrazení a otočením kolieska myši dopredu alebo dozadu zväčšíte alebo zmenšíte veľkosť objektu v okne zobrazenia.

**Panning![]({{ '/assets/icons/pre_icons/mo_pan_icon.jpg' | relative_url }}) **: Funkcia posúvania prispôsobí oblasť vyplňujúcu aktívne zobrazenie bez zmeny veľkosti zobrazeného objektu.

**Editor 2D geometrie**

**Karta Geometria**

Na karte Geometria môžeme zadávať alebo upravovať geometrické prvky. Geometrické prvky je možné zadávať dvoma spôsobmi: metódou „Čiara-oblouk“ a metódou „XYR“.

****

**Metóda XYR**

Formát XYR (DIEGEO) spočíva v definovaní súradnice X, súradnice Y a polomeru pre každý bod geometrie, ktorá definuje objekt. Nakreslí sa oblúk so zadaným polomerom, ktorý spája priamky, ktoré by sa pretínali v bode definovanom súradnicami X a Y. (Pozri obr. 33.1.19.)

  
Tabuľka XYR sa zobrazí priamo v okne Geometria. Táto tabuľka umožňuje špecifikovať a/alebo upravovať geometriu objektu prostredníctvom viacerých bodov vo formáte XYR. X a Y sú súradnice x a y bodu a R je polomer bodu (ak má definovať zakrivenú čiaru).

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image014.jpg' | relative_url }})

2D geometrický editor s typom XYR Geo

**Metóda priamky a oblúka**

Formát Line-Arc (DIEGEO) je podobný formátu XYR v tom, že umožňuje definovať oblúky, je však viac orientovaný na entity. Formát XYR definuje spojovacie body a typ spojenia, zatiaľ čo formát Line-Arc definuje čiary a oblúky, z ktorých sa objekt skladá, a nie samotné spojenia. Hlavným dôvodom používania formátu Line-Arc je skutočnosť, že súbory IGES sú formátované podľa schémy Line-Arc. (Pozri obr. 33.1.20.)

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image015.jpg' | relative_url }})

2D geometrický editor s geometrickým typom „Čiara-oblouk“

Pridať slučku ![]({{ '/assets/icons/pre_icons/mo_add_loop_button.jpg' | relative_url }}): Kliknutím na toto tlačidlo pridáte novú slučku; táto voľba je potrebná na definovanie topológie objektov s viacerými hranicami.

**Odstrániť slučku** ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) : Odstráni existujúcu slučku.

**Pridať vrchol** ![]({{ '/assets/icons/pre_icons/mo_add_vertex_button.jpg' | relative_url }}): Kliknutím na toto tlačidlo pridáte do slučky nový vrchol.

**Odstrániť vrchol** ![]({{ '/assets/icons/pre_icons/mo_delete_vertex_button.jpg' | relative_url }}) : Odstráni existujúci vrchol v slučke.

**Priradiť k** ![]({{ '/assets/icons/pre_icons/mo_assign_to_pull_down_button.jpg' | relative_url }}): Pomocou tejto funkcie môže používateľ priradiť vybranú slučku k ľubovoľnej geometrii objektu.

**Karta „Objekty“**

Na karte „Objekty“ môžeme vybrať objekt zo zoznamu, čím skryjeme geometriu vybraného objektu v grafickom okne, ak sa v ňom zobrazuje viac ako jedna geometria objektu. (Pozri obr. 33.1.21.)

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image016.jpg' | relative_url }})

Okno objektov v 2D geometrickom editore

**Karta „Slučky“**

Na karte „Slučky“ môžeme načítať a priradiť materiál k vybraným slučkám. Okrem toho sa v podrobnostiach príslušnej slučky zobrazuje priradený materiál. (Pozri obr. 33.1.22.)

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image017.jpg' | relative_url }})

Okno materiálov v editore 2D geometrie

**Zobraziť geometriu vnútri značky:** Zaškrtnutím tejto možnosti sa aktivuje zobrazenie orientácie geometrie.

**Import geometrie zo súboru** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}): Importuje geometriu zo súboru  
**Načítať geometriu z knižnice** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}): Importuje geometriu z knižnice  
**Uloženie geometrie do súboru** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) : Uloží geometriu do súboru.  
**Uložiť geometriu do knižnice** ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ uložiť geometriu do knižnice.  
**Odstrániť geometriu** ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}): Odstráni vytvorenú geometriu.

**Nastavenia**![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }})

**Import 2D**

**Tolerancia**

Tu sa nastavuje úroveň tolerancie pri spájaní dvoch susedných bodov, ktoré sú blízko pri sebe, keď sa objekt importuje v geometrických formátoch IGS a DXF, a pred prenesením údajov do programu DEFORM. (Pozri obr. 33.1.23.)

**Počet diskretizačných bodov**

**Text sa má doplniť.**

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image018.jpg' | relative_url }})

Okno „Tolerancie 2D geometrie“

### **Sieťovina**

Na obr. 33.1.24. sú zobrazené možnosti generovania siete v režime Guided. Počet prvkov, ktoré sa majú pre objekt vygenerovať, je možné určiť jednoduchým posunutím posuvníka a výberom vhodnej hodnoty pre aktuálnu simuláciu v poli „Počet prvkov“. Sieť na objekte je možné vygenerovať kliknutím na funkciu ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Funkcia ![]({{ '/assets/icons/pre_icons/mo_delete_button.jpg' | relative_url }}) vygenerovanú sieť odstráni.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image019.jpg' | relative_url }})

Okno nastavení siete v režime s návodom

Na nastavenie parametrov siete, ako sú veľkosť, tvar, hustota, typ prvku atď., musí používateľ prejsť do expertného režimu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}), kde sú k dispozícii pokročilejšie možnosti vytvárania siete. Na obr. 33.1.25. sú zobrazené možnosti vytvárania siete dostupné v expertnom režime.

**Všeobecné nastavenia**

Okno „Mesh Generation“ (pozri obr. 33.1.25.) umožňuje používateľovi vytvoriť sieť pre aktuálny objekt. Hustotu siete môže určiť buď systém na základe nastavení, alebo ju môže používateľ nastaviť priamo.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image020.jpg' | relative_url }})

Okno nastavení siete v režime pre pokročilých

**Materiál**

Na obr. 33.1.26. je zobrazené okno materiálov. Používateľ môže priradiť požadovaný materiál zo zoznamu alebo ho importovať a uložiť zo súboru či knižnice. Používateľ môže tiež pridať nový materiál, a dokonca aj upravovať a odstraňovať materiály zo zoznamu priamo z okna materiálov objektu. Ďalšie informácie o tom, ako priradiť materiál, nájdete v [10\. Material Data](/docs/en/pre_processor/10_material_data/10_material_data/).

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image029.jpg' | relative_url }})

Okno s materiálmi

Po pridaní materiálu kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}); otvorí sa okno s materiálom, ako je znázornené na obrázku [Fig. 10.9.](../../pre_processor/10_material_data/10_material_data.htm#Fig._10.9._Edit_material_window). Požadované vlastnosti závisia od fyzikálnych javov simulovaných v programe DEFORM. Vlastnosti materiálu, ktoré musí používateľ špecifikovať, závisia od typov materiálov, ktoré používateľ využíva v simulácii. Ďalšie informácie nájdete v [10\. Material Data](/docs/en/pre_processor/10_material_data/10_material_data/).

### Okrajové podmienky

Na stránke „Okrajové podmienky“ môže používateľ priradiť objektu rôzne okrajové obmedzenia. Okrajové podmienky určujú, ako okraj objektu interaguje s inými objektmi a s prostredím. Najčastejšie používané okrajové podmienky sú výmena tepla s prostredím pri simuláciách zahŕňajúcich prenos tepla, predpísaná rýchlosť na vynútenie symetrie alebo predpísanie pohybu v úlohách, ako je ťahanie dielu cez lisovaciu formu, zúženie pri modelovaní zúžených krúžkov na nástrojoch, predpísaná sila pre analýzu napätia v lisovacej forme a kontakt medzi objektmi v modeli. Obr. 33.1.27. znázorňuje rôzne okrajové podmienky, ktoré je možné priradiť k objektu.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image021.jpg' | relative_url }})

Okno s okrajovými podmienkami

BCC sú rozdelené do kategórií [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/), [Thermal](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/), [Diffusion](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/) a [Heating](/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/). Ďalšie informácie o týchto BCC nájdete v [14\. Boundary Conditions.](../../pre_processor/14_boundary_conditions).

### Ovládanie pohybu

Ovládacie prvky pohybu je možné použiť na tuhé objekty a hraničné uzly objektov s sieťou. Povrch vymedzený týmito uzlami možno považovať za „tuhý povrch“. Počas simulácie sa obmedzené uzly budú pohybovať synchronizovane rýchlosťou a smerom definovanými ovládacími prvkami pohybu. V 2D prostredí sú k dispozícii štyri typy ovládacích prvkov pohybu.

**Translačný pohyb**

Počas simulácie sa viazané uzly budú pohybovať synchronizovane rýchlosťou a smerom definovanými ovládacími prvkami pohybu. (Pozri obr. 33.1.28.)

  
Dva typy ovládacích prvkov pohybu, ktoré sú k dispozícii v rámci ovládacích prvkov pre posun, sú [Speed](/docs/en/pre_processor/15_movement_controls_definition/15_1_speed/), [Force](/docs/en/pre_processor/15_movement_controls_definition/15_2_force/), [Hammer](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/), [Screw press](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/), [Mechanical press](/docs/en/pre_processor/15_movement_controls_definition/15_5_mechanical_press/), [Hydraulic press](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/), [Sliding Die](/docs/en/pre_processor/15_movement_controls_definition/15_7_sliding_die/) a [Path](/docs/en/pre_processor/15_movement_controls_definition/15_8_path/). Ďalšie informácie nájdete v [15\. Movement controls settings.](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image022.jpg' | relative_url }})

Okno ovládania translačného pohybu

**Rotačný pohyb**

Rotačný pohyb je definovaný uhlovou rýchlosťou/krútiacim momentom okolo pevného stredu otáčania (pozri obr. 33.1.29.). Tento typ pohybu spôsobuje iba otáčanie. Pokiaľ nie je uvedené inak, posun je obmedzený. Rýchlosť otáčania sa nastavuje pomocou možnosti Spôsob riadenia a bod, okolo ktorého sa objekt otáča, sa nastavuje pomocou položky Stred rotačného pohybu. Ďalšie informácie nájdete v [15.9. Rotational movement.](/docs/en/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image023.jpg' | relative_url }})

Ovládacie prvky pre rotačný pohyb okna

**Krútivý pohyb**

Ovládacie prvky pre torzný pohyb sa dajú použiť iba v prípade torzných modelov. Táto možnosť ovládania pohybu je aktívna iba pre DEFORM-2D. Nastavenia pohybu sú znázornené na obr. 33.1.30. Ďalšie informácie nájdete v [15.10. Torsional movement.](/docs/en/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image024.jpg' | relative_url }})

Typ riadenia torzného pohybu

**Pohyb pri zváraní trením**

Ovládacie prvky pohybu pri zváraní trením sa dajú použiť iba v prípade 2,5D modelov zvárania trením. Táto možnosť ovládania pohybu je k dispozícii pre DEFORM-2D a je aktívna iba vtedy, ak je v nastaveniach simulácie vybraný typ geometrie „2,5D zváranie trením“. Tento pohyb možno použiť na definovanie pohybu mimo roviny. Ďalšie informácie nájdete v dokumente [15.11. Friction Welding movement](/docs/en/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/).

  
Ďalšie informácie o týchto ovládacích prvkoch nájdete v dokumente [15_Movement Controls Settings](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/).

### Nehnuteľnosť

V okne „Vlastnosti objektu“ sa zadávajú rôzne parametre objektu, ktoré ovplyvňujú buď termomechanické správanie objektu, alebo správanie numerického riešenia. (Pozri obr. 33.1.31.) Ďalšie informácie nájdete v [16\. Object properties.](../../pre_processor/16_object_properties).

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image025.jpg' | relative_url }})

Okno vlastností

### Inicializácia

V okne „Initialize“ sú na inicializáciu k dispozícii niektoré bežne používané stavové premenné, ako napríklad teplota, deformácia, napätie, poškodenie, rýchlosť, posun, hustota, veľkosť zŕn mikrostruktúry a veľkosť častíc.

  
Používateľ môže inicializovať hodnoty týchto stavových premenných tak, že ich zadá do príslušného poľa a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). Obr. 33.1.32. znázorňuje rôzne stavové premenné, ktoré sú k dispozícii v okne Initialize. V prípade stavových premenných, ako sú rýchlosť a posunutie, kde je k dispozícii toľko vstupných polí, koľko je rozmerov, musí používateľ definovať smerové hodnoty premenných v príslušných poliach a následným kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) sa vypočíta celková rýchlosť a posunutie. V závislosti od typu stavovej premennej ich môže používateľ inicializovať aj z dátových okien Uzol a Prvok (pozri obr. 33.1.33. a obr. 33.2.34.). Ďalšie informácie o tom, ako inicializovať stavové premenné v oknách „Uzel“ a „Prvok“, nájdete v [17.1. Object node variables](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) a [17.2. Object element variables.](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/).

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image028.jpg' | relative_url }})

Inicializovať okno

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image026.jpg' | relative_url }})

Okno „Údaje uzla“

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image027.jpg' | relative_url }})

Okno „Údaje o prvku“

## Polohovanie

Na obr. 33.1.35. je zobrazené okno na nastavenie polohy.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image030.jpg' | relative_url }})

Okno na nastavenie polohy

**Automatické polohovanie** ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }})

Kliknutím na toto tlačidlo systém automaticky umiestni objekty vzhľadom na smer pohybu hornej matrice; táto možnosť sa najlepšie hodí pre jednoduché nastavenie s tromi objektmi – obrobkom, hornou matricou a spodnou matricou.

**Umiestňovanie objektov**![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }})

Kliknutím na toto tlačidlo môže používateľ umiestniť objekty do požadovaných smerov. K dispozícii sú rôzne typy možností umiestnenia, ako napríklad [Drag](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_1_Drag_Positioning), [Offset](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_2_Offset_Positioning), [Interference](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_3_Interference_positioning), [Flip](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_6_Flip_positioning) a [Rotational](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_4_Rotational_positioning), ako je znázornené na obr. 33.1.36. Ďalšie informácie o týchto možnostiach nájdete v časti [19\. Object Positioning.](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image029.jpg' | relative_url }})

Okno na umiestňovanie objektov

## Plánované polohovanie

Ak si používateľ nie je istý polohou objektu, ako je to v prípade objektov typu „Read From DB“, naplánované umiestňovanie pomôže objekty presne umiestniť.

Funkcia „Schedule positioning“ umožňuje používateľovi definovať umiestnenie objektov v nastaveniach MO pre nasledujúce operácie, pre ktoré sa nevytvára databáza (DB), tak, aby boli objekty umiestnené ešte pred vytvorením databázy počas spustenia simulácie v dávkovom režime. (Pozri obr. 33.1.37.)

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image031.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

## Kontakt (vzťahy medzi objektmi)

Účelom vzťahov medzi objektmi je definovať, ako rôzne objekty v simulácii vzájomne interagujú. Tabuľka vzťahov zobrazuje aktuálne vzťahy medzi objektmi, ktoré boli definované, ako je znázornené na obr. 33.1.38. Všetky objekty, ktoré môžu prísť do kontaktu v priebehu simulácie, musia mať definovaný kontaktný vzťah. To zahŕňa aj objekt, ktorý má vzťah sám so sebou, ak dochádza k vlastnému kontaktu, ako je to v prípade prekrývania. Správne definovanie týchto vzťahov je veľmi dôležité, aby simulácia mohla presne modelovať proces tvárnenia.

**Systém**: Po výbere tohto prepínača systém priradí predvolené vzťahy medzi objektmi. V prípade potreby môže používateľ pridať mazivá výberom možnosti „Pridať nové“ z roletového menu a kliknutím na tlačidlo „Upraviť“, alebo môže na účely simulácie načítať požadované mazivá z knižnice.

**Používateľ**: Pri operácii „Forming“ je štandardne vybrané rádio tlačidlo „Používateľ“. Používateľ môže pridať vzťahy kliknutím na tlačidlo „Pridať“, ako je znázornené na obr. 33.1.38.

Ďalšie informácie nájdete na stránke [, 20. Inter-Object Relations](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image040.jpg' | relative_url }})

Okno definície medzi objektmi

## Ovládacie prvky na zastavenie

Parametre ukončenia určujú čas priebehu, po uplynutí ktorého sa simulácia ukončí. Simuláciu je možné ukončiť na základe maximálneho počtu simulovaných časových krokov, maximálnej kumulovanej elementárnej deformácie, maximálneho času priebehu, maximálneho zdvihu, minimálnej rýchlosti alebo maximálneho zaťaženia primárneho objektu. Simulácia sa zastaví, keď bude splnená podmienka ktoréhokoľvek z týchto parametrov ukončenia.

Ďalšie informácie nájdete v dokumente [Stopping Controls in Forming 3D setup.](33_2_3d_forming_setup.htm#33_2_7_Stopping_Controls)

## Ovládacie prvky simulácie

Systém DEFORM rieši časovo závislé nelineárne úlohy generovaním série riešení metódou konečných prvkov (FEM) v diskrétnych časových krokoch. V každom časovom kroku sa rýchlosti, teploty a ďalšie kľúčové premenné každého uzla v sieti konečných prvkov určujú na základe okrajových podmienok, termomechanických vlastností materiálov obrobku a prípadne riešení z predchádzajúcich krokov. Ostatné stavové premenné sa odvodzujú z týchto kľúčových hodnôt a aktualizujú sa pri každom časovom kroku. Dĺžka tohto časového kroku a počet simulovaných krokov sa určujú na základe informácií zadaných v ponuke nastavení krokov.

V ovládacích prvkoch simulácie v režime s návodom môže používateľ vybrať typ režimu simulácie a typ výstupu. Obr. 33.1.40 znázorňuje ovládacie prvky simulácie v režime s návodom. Obr. 33.1.39. znázorňuje stránku „Krok“ v režime s návodom, kde môže používateľ definovať ovládacie prvky operačného kroku a definíciu kroku. Tu sú k dispozícii základné možnosti potrebné na vytvorenie operácie, zatiaľ čo režim „Expert“ ponúka podrobnejšie možnosti.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image046.jpg' | relative_url }})

Režim s návodom – Okno krokov

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image049.jpg' | relative_url }})

Ovládacie prvky simulácie v režime s návodom

**Počet simulačných krokov (NSTEP)**

Parameter „Počet simulačných krokov“ určuje počet krokov, ktoré sa majú spustiť od počiatočného čísla kroku. Simulácia sa zastaví po vykonaní tohto počtu simulačných krokov, pokiaľ sa nespustí príkaz na zastavenie simulácie alebo ak simulácia nenarazí na problém. Napríklad, ak je počiatočné číslo kroku -35 ([NSTART](/docs/en/keyword_documentation/n/nstart/)) a je špecifikovaných 30 krokov ([NSTEP](/docs/en/keyword_documentation/n/nstep/)), simulácia sa zastaví po 65. kroku, pokiaľ sa skôr nespustí iný príkaz na zastavenie.

**Krok pri ukladaní (STPINC)**

Krok prírastku ([STPINC](/docs/en/keyword_documentation/s/stpinc/)), ktorý sa má uložiť do databázy, určuje počet krokov, ktoré systém uloží do databázy. Pri spustení simulácie sa musí vypočítať každý krok, ale nemusí sa nutne uložiť do databázy. Uložením väčšieho počtu krokov sa zachová viac informácií o procese, čo však bude vyžadovať viac úložného priestoru.

**Primárny čip (PDIE)**

Primárna matrica ([PDIE](/docs/en/keyword_documentation/p/pdie/)) je objekt, pre ktorý je definovaných mnoho kritérií zastavenia a krokovania. Napríklad brzdná vzdialenosť založená na zdvihu primárnej matrice. Keď zdvih objektu definovaného ako primárna matrica dosiahne hodnotu posunu primárnej matrice, simulácia sa zastaví bez ohľadu na to, či boli špecifikované ďalšie kroky. Funkcia „Krok podľa zdvihu“ určuje veľkosť kroku na základe pohybu primárnej matrice. Primárna matrica sa zvyčajne priraďuje k objektu, ktorý je najviac riadený kováčskym strojom. Napríklad matrica pripevnená k piestu mechanického lisu by bola označená ako primárny objekt.

**Ovládanie krokového prírastku ([DSMAX](/docs/en/keyword_documentation/d/dsmax/)/[DTMAX](/docs/en/keyword_documentation/d/dtmax/))**

Veľkosť kroku riešenia je možné riadiť časovým krokom alebo posunom primárnej matrice. Ak je špecifikovaný zdvih na krok, primárna matrica sa v každom časovom kroku posunie o zadanú hodnotu. Celkový posun primárneho lisovacieho nástroja bude rovný posunu na krok vynásobenému celkovým počtom krokov. Ak je špecifikovaný čas na krok, použije sa časový interval na krok. Posun lisovacieho nástroja na krok bude rovný časovému kroku vynásobenému rýchlosťou lisovacieho nástroja.

  
Nastavenia krokových regulátorov založených na teplote ([DTPMAX](/docs/en/keyword_documentation/d/dtpmax/)) tiež ovplyvňujú časový krok. Účelom týchto regulátorov je určiť časový krok simulácie, ktorá je riadená deformáciou vyvolanou teplotou.

Definícia riadenia krokového prírastku bola rozšírená tak, aby zahŕňala krokové funkcie závislé od času aj od zdvihu; tieto možnosti sú k dispozícii v režime Expert. To znamená, že veľkosť kroku (či už ide o čas na krok alebo zdvih na krok) je teraz možné definovať ako funkciu času alebo zdvihu. Táto funkcia umožňuje v prípade potreby dosiahnuť jemnejšie rozlíšenie uložených informácií o modeli. (typicky smerom ku koncu zdvihu, kde môžu nastať prudké zmeny zaťaženia formy, plnenia dutiny alebo tvorby prebytku materiálu)

Počet zdvihov na krok je často intuitívnejší. Čas na krok je však potrebné špecifikovať pri každej úlohe, v ktorej nedochádza k pohybu matice (napríklad pri prenose tepla), alebo pri každej úlohe, kde sa používa regulácia sily. 

Na obr. 33.1.41 sú zobrazené ovládacie prvky simulácie v režime Expert.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image032.jpg' | relative_url }})

Okno ovládacích prvkov simulácie v režime pre pokročilých

Možnosti definované v časti „Ovládacie prvky simulácie“ (pozri obr. 33.1.41.) ovplyvňujú numerické správanie riešenia. Hlavné ovládacie prvky slúžia na zadanie názvu simulácie, sústavy jednotiek, typu geometrie atď.

  
Ovládacie prvky pre kroky a ukončenie slúžia na určenie časového kroku, celkového počtu krokov a kritérií na ukončenie simulácie.

  
Tu je možné zadať podmienky spracovania, ako napríklad teplotu okolia a konvekčný koeficient.

Ďalšie informácie a popis možností v ovládacích prvkoch simulácie nájdete v [9\. Simulation Controls.](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

## Vytvoriť databázu

**Overiť údaje**![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})****

Systém skontroluje údaje. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvoriť databázu ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})**

Kliknutím na toto tlačidlo sa vygenerovala databáza pre nastavenie. (Pozri obr. 33.1.42.)

**Pridať súbor s kľúčmi**

Akékoľvek informácie, ktoré nie sú definované v sprievodcovi, ale napriek tomu sa vzťahujú na daný proces, je možné načítať ako súbor s príponou .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt – tieto hodnoty je možné definovať v súbore s príponou .key, následne stačí zmeniť len tento súbor a simuláciu je možné spustiť znova.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image048.jpg' | relative_url }})

Okno „Vytvoriť databázu“

**Súvisiace témy:**

[6.1. Integrated Manufacturing Process Pre- Processor Layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

[6.2. Integrated Manufacturing Process.Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Process Post - Processor layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[2D MO Basic Labs](/docs/en/labs/basic_labs/2d_labs/2d_labs/)
