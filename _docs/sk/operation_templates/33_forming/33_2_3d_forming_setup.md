---
lang: sk
title: "33.2. Nastavenie 3D tvarovania"
---

# 33.2. Nastavenie 3D tvarovania

33.2.1. Zoznam materiálov

33.2.2. Pridávanie objektov

33.2.3. Obrobok

  * Geometria

  * Sieťovina

  * Materiál

  * Okrajové podmienky

  * Ovládanie pohybu

  * Nehnuteľnosť

  * Inicializovať

33.2.4. Polohovanie

33.2.5. Plánované umiestnenie

33.2.6. Kontakt

33.2.7. Ovládacie prvky na zastavenie

33.2.8. Ovládacie prvky simulácie

33.2.9. Vytvorenie databázy

Operácia „3D formovanie“ sa dá použiť na nastavenie zložitých 3D prietokových úloh, ktoré nie je možné simulovať v 2D prostredí. Vykĺbenie valcovitých dielov je plne trojrozmerný proces a ak sa takéto správanie očakáva, musí sa modelovať práve ako trojrozmerný proces. Osovo symetrická simulácia nezobrazí vzpruženie, aj keby k nemu došlo v skutočnom procese (pozri obr. 33.2.1.).

![]({{ '/assets/images/about_deform/1_7_geometry_representation/1_7_image002.jpg' | relative_url }})

Vykĺbenie

## Zoznam materiálov

Aby simulácia dosiahla vysokú úroveň presnosti, je dôležité poznať vlastnosti materiálu, ktoré sú potrebné na definovanie materiálu používaného v programe DEFORM.

  
Pri nastavovaní simulácie je potrebné pre objekty špecifikovať vlastnosti materiálov. V operácii MO Forming je možné načítať všetky materiály potrebné pre danú operáciu naraz a požadovaný materiál vybrať neskôr pri nastavovaní úlohy. Používateľ môže pridať materiál výberom možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) „načítať údaje o materiáli z knižnice“, ako je znázornené na obr. 33.2.2. Používateľ môže vybrať požadovaný materiál z kategórií a potom kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}), ako je znázornené na obr. 33.2.3. 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image001.jpg' | relative_url }})

Okno „Zoznam materiálov“

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image002.jpg' | relative_url }})

Importovať materiál z okna knižnice

  
(alebo) 

Ďalším spôsobom pridania materiálu je kliknutie na ikonu materiálu na karte prehliadača, čím sa zobrazí zoznam materiálov z knižnice zoradených do rôznych kategórií, ako je znázornené na obr. 33.2.4. Vyberte požadovaný materiál a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}). Používateľ môže požadovaný materiál pridať aj pomocou funkcie „drag and drop“ (ťahanie a púšťanie) do okna materiálu.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image003.jpg' | relative_url }})

Pridať materiál z karty „Materiál“ v Průzkumníku

(alebo)

V okne so zoznamom materiálov je možné pridať nový materiál kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Po pridaní materiálu kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vyberte príslušnú kartu, kde zadáte potrebné údaje pre simuláciu, ako je znázornené na obr. 33.2.5.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image005.jpg' | relative_url }})

Pridať materiál z okna so zoznamom materiálov

**Import údajov o materiáloch zo súboru** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}): Importuje údaje o materiáloch zo súboru s príponou .Key alebo .DB.  
**Načítať údaje o materiáli z knižnice** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}): Importuje materiál z knižnice.  
**Uloženie údajov o materiáli do súboru**![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) : Uloží materiál do súboru.  
**Uložiť údaje o materiáli do knižnice**![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ uložiť materiál do knižnice a v budúcnosti ho podľa potreby opäť načítať pre ďalšie simulácie.

**Zloženie zmesi**

Materiály typu „zmes“ ([MSTMTR](/docs/en/keyword_documentation/m/mstmtr/)) sa používajú v prípade, že sa v simulácii má modelovať fázová premena. Premenlivý materiál sa modeluje ako „zmes“ fáz, z ktorých sa skladá. Napríklad uhlíková oceľ sa môže modelovať ako zmes austenitu, perlitov, bainitu a martenzitu. Ak je definovaný zmesový materiál, mali by sa definovať pravidlá transformácie, ktoré riadia prechod jednej fázy do druhej. (Pozri obr. 33.2.6.)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image004.jpg' | relative_url }})

Pridanie zmesi materiálov

**Kopírovať vlastnosti ![]({{ '/assets/icons/pre_icons/mo_copy_properties.jpg' | relative_url }})**

Slúži na kopírovanie bežných vlastností materiálov, ako sú plastické, elastické, tepelné atď., z jedného materiálu do druhého pri vytváraní/definovaní údajov o materiáli, ako je znázornené na obr. 33.2.7. V tomto dialógovom okne je potrebné vybrať zdroj a cieľ kopírovania vlastností, ako aj samotné vlastnosti, ktoré sa majú skopírovať.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image005.jpg' | relative_url }})

Okno „Kopírovať vlastnosti materiálu“

**Previesť jednotky ![]({{ '/assets/icons/pre_icons/mo_convert_units_button.jpg' | relative_url }})**

Slúži na prevod jednotkového systému aktuálne vybraného materiálu zo zoznamu materiálov zo systému SI na anglický systém alebo naopak, prípadne môže používateľ použiť akýkoľvek iný násobný koeficient, ako je znázornené na obr. 33.2.8. Stlačením tlačidla ![]({{ '/assets/icons/pre_icons/mo_si_to_english_button.jpg' | relative_url }}) alebo ![]({{ '/assets/icons/pre_icons/mo_english_to_si_button.jpg' | relative_url }}) sa zobrazia príslušné násobné koeficienty pre prevod z ![]({{ '/assets/icons/pre_icons/mo_si_to_english_button.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_english_to_si_button.jpg' | relative_url }}); stlačením tlačidla ![]({{ '/assets/icons/pre_icons/mo_convert_button.jpg' | relative_url }}) sa vykoná prevod a okno prevodu sa zatvorí. Túto prevodnú tabuľku je možné uložiť pomocou tlačidla „Save“ a je možné ju tiež upraviť pomocou programu WordPad/Notepad a opätovne načítať do súboru UNITCONV.DAT pomocou tlačidla „Load“.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image006.jpg' | relative_url }})

Okno pre prevod jednotiek

## Pridať objekty

Používateľ môže pridať požadovaný počet objektov pre simuláciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Na obr. 33.2.9 sú zobrazené tri objekty pridané pre jednoduchú operáciu zúženia. 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image007.jpg' | relative_url }})

Okno „Objekty“

## Obrobok

Na tejto stránke môže používateľ nastaviť požadovanú teplotu pre objekt a vybrať typ objektu, ako je znázornené na obr. 33.2.10. Pre obrobok je štandardne vybraný typ objektu „Plast“ a používateľ môže tiež importovať údaje o objekte z iných databázalebo súborov Keyfile z používateľom definovanej knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) alebo z adresára úlohy ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a dokonca môže údaje o objekte uložiť do súboru Keyfile v používateľom definovanej knižnici ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}) alebo v adresári úlohy ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) pomocou príslušných tlačidiel.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image008.jpg' | relative_url }})

Okno obrobku

### **Geometria**

Okno „Geometria“ slúži na definovanie geometrie objektu, ako je znázornené na obr. 33.2.11. Ak nie je definovaná žiadna geometria, aktívne bude iba pole „Definovať primitívy“, ostatné možnosti budú sivé. Po vytvorení geometrie sa aktivujú všetky možnosti.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image009.jpg' | relative_url }})

Okno Geometria

**Definícia Primitive![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) **

Máme k dispozícii tri rôzne typy geometrických primitív, ako sú krabica, valec a dutý valec, ako je znázornené na obr. 33.2.12. Pomocou nástrojov „Extrude“ a „Revolve“ je možné previesť 2D prierez na 3D.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image010.jpg' | relative_url }})

Okno geometrických primitív

**Ohraničenie výňatku** ![]({{ '/assets/icons/pre_icons/mo_extract_border_button.jpg' | relative_url }})

Táto funkcia extrahuje geometrické údaje z aktuálneho objektu s mriežkou v databáze pre všetky typy objektov s výnimkou tuhého objektu.

**Check![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})**

Vždy skontrolujte geometriu. Program DEFORM disponuje kontrolným algoritmom, ktorý overuje počet neplatných hrán, neplatnú orientáciu, mnohouholníky s malou plochou a počet plôch. Nie je možné odhaliť všetky typy chýb.

Použitím tejto možnosti „Skontrolovať geometriu“ sa otvorí okno „Výsledky kontroly geometrie“, ktoré obsahuje prehľad geometrie objektu (pozri obr. 33.2.13.). V prípade objektu s uzavretým objemom by mala byť prítomná 1 plocha, 0 voľných hrán a 0 neplatných entít (ako je označené kružnicou nižšie na obr. 33.2.13.). Objekty, ktoré sú importované ako plochy a nie ako telesa, budú mať voľnú hranu, ale aj tak by mali mať len 1 plochu.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image011.jpg' | relative_url }})

Výsledky kontroly geometrie

**Scale![]({{ '/assets/icons/pre_icons/mo_scale_label.jpg' | relative_url }})**

Geometriu je možné pri tvárnení zmenšiť alebo zväčšiť tak, aby zohľadňovala teplotnú rozťažnosť, a to stanovením mierky. (Pozri obr. 33.2.14.) Mierku je možné vypočítať na základe teplotného rozdielu a údajov o materiáli závislých od teploty. Upravenú geometriu je možné uložiť v rôznych formátoch na ukladanie geometrie.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image012.jpg' | relative_url }})

Okno „Geometria mierky“

**Reverse![]({{ '/assets/icons/pre_icons/mo_reverse_label.jpg' | relative_url }})**

Táto funkcia obráti smer povrchu/normály geometrie. Smer povrchu/normály geometrie by mal byť vždy smerom von.

**Nájsť Axis![]({{ '/assets/icons/pre_icons/mo_find_axis_label.jpg' | relative_url }})**

Táto funkcia automaticky určí os geometrie na základe jej definície a zobrazí ju.

**Nastavenie siete Brick Mesh**

Na definovanie mriežky typu „Brick“ musí používateľ určiť počiatočnú a koncovú plochu vytvorenej geometrie, ako je znázornené na obr. 33.2.15. Mriežka typu „Brick“ sa používa pre geometrie s pravidelným alebo identickým prierezom.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image017.jpg' | relative_url }})

Nastavenie okna „Brick Mesh“ pre extrudovanie

Sieť tehál je možné vytvoriť výberom možností „Extrude“ (Extrudovať) alebo „Revolve“ (Otočiť) v závislosti od geometrie. Ak používateľ zvolí voľbu „Extrude“, sieť tehál sa extruduje vzhľadom na počiatočný a koncový bod, ako je znázornené na obr. 33.2.16.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image013.jpg' | relative_url }})

Tehlová mriežka extrudovaného objektu

Ak používateľ vyberie prepínač „Revolve“, sieť tehál sa otočí v smere osi Z, ako je znázornené na obr. 33.2.17 a obr. 33.2.18.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image014.jpg' | relative_url }})

Nastavenie okna s mriežkou pre otáčanie

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image015.jpg' | relative_url }})

Tehlová mriežka rotujúceho objektu

**Fix![]({{ '/assets/icons/pre_icons/mo_fix_label.jpg' | relative_url }})**

Táto funkcia rieši geometrické problémy, pri ktorých sa vyskytujú buď viaceré plochy, alebo otvorené oblasti (diery), a to odstránením všetkých nadbytočných plôch a vyplnením dier. Pri menších alebo ohraničených problémoch to funguje dobre. Pri zložitejších súboroch, ako je tento, však oprava nemusí priniesť želaný výsledok. (Pozri obr. 33.2.19.)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image016.jpg' | relative_url }})

Určenie geometrie formy na kľukový hriadeľ

**Preskúmať**![]({{ '/assets/icons/pre_icons/mo_examine_label.jpg' | relative_url }})

Táto funkcia slúži na preskúmanie bodov a polygónov 3D geometrie. Súradnice bodov geometrie je možné upravovať pomocou polí pre súradnice bodov a po zmene týchto súradníc stlačením tlačidla „Apply“. Aktuálny výber zobrazenia bodov a polygónov je zvýraznený guľou alebo kockou pomocou začiarkavacích políčok v spodnej časti okna.(Pozri obr. 33.2.20.) Od verzie DEFORM V12 môžeme pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) („Detect zones“) vedľa poľa Surface vypočítať počet zón existujúcich v geometrii a pre každú zónu môžeme pomocou možnosti „Assignment“ priradiť iný materiál alebo ID vrstvy. Táto voľba pomáha používateľovi modelovať viacvrstvové kompozity, dutiny, inklúzie, aditívnu výrobu atď.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image018.jpg' | relative_url }})

Nastavenia geometrie okna „Examine“

**Roviny symetrie ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }})**

Je možné definovať ako rovinnú symetriu, tak aj rotačnú symetriu. V prípade rovinné symetrie bude simulácia obsahovať dodatočné informácie, ktoré jej umožnia zabrániť vytváraniu prebytku materiálu v jej okolí. V prípade rotačnej symetrie sa pri vytváraní siete automaticky nastavia správne okrajové podmienky na plochách. Cieľom je vytvoriť jednotné miesto na aplikovanie symetrických okrajových podmienok pre všetky objekty.

**Určenie rovinná symetria**

Ak chcete určiť rovinnú symetriu, vyberte symetrickú rovinu na geometrii a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Podmienka rovinná symetria sa pridá do zoznamu aktuálne zadaných symetrií. (Pozri obr. 33.2.21.) Po definovaní roviny symetrie sa počas generovania siete zobrazí vyskakovacie okno so správou, ako je znázornené na obr. 33.2.22., v ktorom sa používateľ opýta, či chce vytvoriť predvolenú okrajovú podmienku. Používateľ môže zvoliť možnosť „Nie“, ak nechce použiť predvolenú okrajovú podmienku (BCC) priradenú systémom na základe definovaných podmienok symetrie.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image019.jpg' | relative_url }})

Priradenie symetrických plôch

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image020.jpg' | relative_url }})

Vyskakovacie okno „Predvolené okrajové podmienky“

**Poznámka**: Oznamové okno „Symetria“ sa zobrazí len vtedy, keď nastavíme úlohu v režime Expert.

**Určenie rotačnej symetrie**

Na definovanie rotačnej symetrie zadajte bod a vektor osi otáčania, ako aj stupeň symetrie, ako je znázornené na obr. 33.2.23. Potom kliknite na počiatočnú a koncovú rovinu geometrie v smere otáčania, aby sa uplatnila rotačná symetria. Podmienka symetrie sa pridá do zoznamu aktuálne zadaných symetrií. Ďalšie informácie o možnosti rotačnej symetrie nájdete v [Rotational Symmetry.](../../pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining.htm#Specifying_Rotational_Symmetry)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image021.jpg' | relative_url }})

Okno rotačnej symetrie

**Premena z 2D na 3D ![]({{ '/assets/icons/pre_icons/mo_2d_to_3d_conversion.jpg' | relative_url }})**

Používateľ môže definovať geometriu 2D priečneho rezu, ktorú je možné použiť na vytvorenie 3D geometrie zaškrtnutím políčka „Použiť priečny rez“.

**Definícia Primitive![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }})**

Máme tri rôzne typy geometrických primitív, ako sú tyč, valec a dutý valec, ako je znázornené na obr. 33.2.24. Toto okno geometrie sa zobrazuje pri geometrii typu rovinného deformovania.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image007.jpg' | relative_url }})

Okno s geometrickými primitívami 2D pre rovinné deformácie a rovinné napätia 

Zobrazí sa okno geometrie pre typ geometrie „Axisymmetric“, ktoré je znázornené na obr. 33.2.25.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image006.jpg' | relative_url }})

Okno s geometrickými primitívami 2D pre osovo symetrické a torzné modely

**Check![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})**

Po vytvorení geometrie objektu sa aktivuje tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Je potrebné skontrolovať orientáciu geometrie. To je možné urobiť kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), čím sa zobrazí vyskakovacie okno, ako je znázornené na obr. 33.2.26 nižšie. Ak sa vyskytnú nejaké chyby, geometria sa opraví po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}). Po oprave geometrie alebo ak geometria neobsahuje žiadne chyby, zobrazí sa správa „Geometria je správna“ a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Ďalšie informácie nájdete v časti [12.1. 2D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/) [Check Geometry](../../pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining.htm#Check_Geometry). 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image022.jpg' | relative_url }})

Vyskakovacie okno „Skontrolovať geometriu“

**Upraviť**![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }})

Možnosť „Úprava geometrie“ slúži na vytvorenie geometrie objektu alebo na úpravu existujúcej geometrie. Importovanú geometriu je možné upraviť v okne „Úprava geometrie“. Ďalšie informácie o úprave geometrie nájdete v časti [ Edit Geometry](33_1_2d_forming_setup.htm#Edit_) v nastaveniach Forming 2D.

**Zobraziť geometriu vnútri značky**

Zaškrtnutím tejto možnosti sa aktivuje zobrazenie orientácie geometrie.

**Nastavenia![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }})**

Po vytvorení 2D geometrie pomocou týchto nastavení môže používateľ z 2D geometrie vytvoriť 3D geometriu.

**Extrudovať**

Používateľ môže importovať 2D priečny rez alebo použiť definovaný 2D priečny rez geometrie a vytiahnuť ho v požadovanom smere. To je možné urobiť aj pri importe súborov s 2D priečnymi rezmi z databázy alebo kľúčového súboru. (Pozri obr. 33.2.27.) 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image023.jpg' | relative_url }})

Nastavenia okna 2D priečneho rezu pre extrudovanie

**Revolve**

Používateľ môže načítať 2D priečny rez geometrie a na základe symetrie ju otočiť, čím získa 3D priečny rez. (Pozri obr. 33.2.28.)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image024.jpg' | relative_url }})

Nastavenia okna 2D rezu pre funkciu „Revolving“

**Vygenerovať 3D![]({{ '/assets/icons/pre_icons/mo_generate_3d_button.jpg' | relative_url }})**

Kliknutím na toto tlačidlo je možné vytvorenú 2D geometriu vytiahnuť alebo otočiť a vytvoriť tak 3D geometriu.

**Zobraziť normálové vektory geometrie**

Táto funkcia zobrazuje normálové vektory povrchu geometrie. Ak je geometria uzavretým objemom, správna orientácia je daná vtedy, keď normály povrchu smerujú von z objektu. Ak geometria nie je uzavretým objemom, ale ide len o povrch, správna orientácia je daná vtedy, keď normály smerujú k obrobku.(Pozri obr. 33.2.29.)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image025.jpg' | relative_url }})

Zobraziť normálové vektory geometrie

**Import geometrie zo súboru** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}): Importuje geometriu zo súboru  
**Načítať geometriu z knižnice** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}): Importuje geometriu z knižnice  
**Uloženie geometrie do súboru** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) : Uloží geometriu do súboru.  
**Uložiť geometriu do knižnice** ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ uložiť geometriu do knižnice.  
**Odstrániť geometriu** ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}): Odstráni vytvorenú geometriu.

**Nastavenia**

**Import 2D**

Tolerancia: Tu sa nastavuje úroveň tolerancie pri spájaní dvoch susedných bodov, ktoré sú blízko pri sebe, pri importe objektu v geometrických formátoch IGS a DXF pred prenosom údajov do programu DEFORM. (Pozri obr. 33.2.30.)

**Počet diskretizačných bodov:**

Text, ktorý sa má pridať.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image018.jpg' | relative_url }})

Okno nastavení tolerancií v 2D geometrii

**Import 3D**

Tolerancia: Tu sa definuje úroveň spojenia dvoch hraničných bodov, ktoré sa pri importe objektu z geometrických formátov STL a pred prenosom údajov do programu DEFORM nachádzajú blízko seba. (Pozri obr. 33.2.30.)

**Mierka**: Táto voľba zmení mierku 3D geometrie pri načítaní importovanej geometrie. Ak chcete zmeniť mierku importovanej geometrie, je potrebné zadať požadovanú mierku ešte pred jej importom. Predvolená hodnota je 1, čo znamená žiadne zmenšenie; pri hodnote 0,5 sa geometria zmenší na polovicu pôvodnej veľkosti a pri hodnote 2 sa zväčší na dvojnásobok pôvodnej veľkosti. (Pozri obr. 33.2.30..) 

### Sieťovina

Na nižšie uvedenom obr. 33.2.31 sú zobrazené možnosti generovania siete v režime s návodom. V režime s návodom môže používateľ na stránke „Sieť“ vygenerovať tetraedrickú sieť.

Počet prvkov, ktoré sa majú pre daný objekt vygenerovať, je možné určiť jednoduchým posunutím posuvníka a výberom vhodnej hodnoty pre aktuálnu simuláciu v poli „Počet prvkov“. Funkcia ![]({{ '/assets/icons/pre_icons/mo_mesh_preview_button.jpg' | relative_url }}) umožňuje používateľovi zobraziť náhľad povrchovej siete objektu. Akonáhle je používateľ spokojný s náhľadom povrchovej siete, sieť sa môže na objekte vygenerovať kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Funkcia ![]({{ '/assets/icons/pre_icons/mo_delete_button.jpg' | relative_url }}) vymaže vygenerovanú sieť.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image026.jpg' | relative_url }})

Možnosti okna „Mesh“ v režime s navádzaním

Na nastavenie parametrov siete, ako sú veľkosť, tvar, hustota, typ prvkov atď., musí používateľ prejsť do expertného režimu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}), kde sú k dispozícii pokročilejšie možnosti vytvárania siete. Na obr. 33.2.32. sú zobrazené možnosti siete dostupné v expertnom režime. Na vytvorenie siete pre objekt máme k dispozícii možnosti tetraedrickej siete a tehličkovej siete. Ďalšie informácie týkajúce sa tetraedrickej siete nájdete v kapitole [13.2. 3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/).

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image027.jpg' | relative_url }})

Možnosti okna „Mesh“ v režime pre pokročilých

Na nižšie uvedenom obr. 33.2.33 sú zobrazené možnosti generovania mriežky typu „Brick“ v režime Expert. Ďalšie informácie týkajúce sa tetraedrickej mriežky nájdete v kapitole [13.3. 3D Brick Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/).

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image028.jpg' | relative_url }})

Možnosti mriežky tehál v režime Expert

###  Materiál

Na nižšie uvedenom obr. 33.2.34. je zobrazené okno s materiálmi. Používateľ môže priradiť požadovaný materiál zo zoznamu alebo ho importovať zo súboru či knižnice. Používateľ môže tiež pridať nový materiál. Ďalšie informácie o tom, ako priradiť materiál, nájdete v časti Zoznam materiálov.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image029.jpg' | relative_url }})

Okno „Materiál“

Po pridaní materiálu kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}); otvorí sa okno s materiálom, ako je znázornené na obrázku [Fig. 10.9.](../../pre_processor/10_material_data/10_material_data.htm#Fig._10.9._Edit_material_window). Požadované vlastnosti závisia od fyzikálnych javov, ktoré sa simulujú v programe DEFORM. Vlastnosti materiálu, ktoré musí používateľ špecifikovať, závisia od typov materiálov, ktoré používateľ využíva v simulácii. V tejto časti sú popísané údaje o materiáloch, ktoré je možné špecifikovať pre simuláciu v programe DEFORM.

  
Jednotlivé súbory údajov sú:

  * [Plastic ](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_plastic_data/)
  * [Elastic](/docs/en/pre_processor/10_material_data/10_2_elastic_data/10_2_elastic_data/)
  * [Thermal ](/docs/en/pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data/)
  * [Diffusion ](/docs/en/pre_processor/10_material_data/10_4_diffusion_data/10_4_diffusion_data/)
  * [Dislocation ](/docs/en/pre_processor/10_material_data/10_5_dislocation_data/)
  * [Grain ](/docs/en/pre_processor/10_material_data/10_6_grain_data/10_6_grain_data/)
  * [Hardness ](/docs/en/pre_processor/10_material_data/10_7_hardness_data/10_7_hardness_data/)
  * [Elec/ Mag ](/docs/en/pre_processor/10_material_data/10_8_elec_mag_data/10_8_elec_mag_data/)
  * [Transformation](/docs/en/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/)
  * [Coarsening](/docs/en/pre_processor/10_material_data/10_10_coarsening_data/)
  * [Texture ](/docs/en/pre_processor/10_material_data/10_11_texture_data/)
  * [Miscellaneous](/docs/en/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_miscellaneous_data/)

V tejto časti sa rozoberá spôsob definovania jednotlivých dátových súborov a uvádza sa, pre aký typ simulácie je ktorý z nich potrebný.

Knižnica materiálov DEFORM obsahuje niekoľko stoviek súborov údajov. Takmer všetky materiály obsahujú údaje o plastickosti (tečivé napätie), pružnosti a tepelných vlastnostiach. V závislosti od zamýšľaného použitia môžu údaje o materiáloch zahŕňať aj údaje týkajúce sa mikrostruktúry.

Používateľ by mal overiť, či je materiál vybraný z knižnice vhodný pre proces, ktorý chce modelovať. Ďalšie informácie o vlastnostiach materiálov nájdete v dokumente [10\. Material Data](/docs/en/pre_processor/10_material_data/10_material_data/).

### Okrajové podmienky

Na stránke „Okrajové podmienky“ môže používateľ priradiť objektu rôzne okrajové obmedzenia. Okrajové podmienky určujú, ako okraj objektu interaguje s inými objektmi a s prostredím. Najčastejšie používané okrajové podmienky sú výmena tepla s prostredím pri simuláciách zahŕňajúcich prenos tepla, predpísaná rýchlosť na vynútenie symetrie alebo predpísanie pohybu v úlohách, ako je ťahanie dielu cez lisovaciu formu, zúženie pri modelovaní zúžených krúžkov na nástrojoch, predpísaná sila pre analýzu napätia v lisovacej forme a kontakt medzi objektmi v modeli. Obr. 33.2.35. znázorňuje rôzne okrajové podmienky, ktoré je možné priradiť k objektu.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image033.jpg' | relative_url }})

Okno „Okrajové podmienky“

BCC sú rozdelené do kategórií [Symmetry](/docs/en/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/), [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/), [Thermal](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/), [Diffusion](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/) a [Heating](/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/). Ďalšie informácie o týchto BCC nájdete v [14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/).

### **Ovládanie pohybu**

Ovládacie prvky pohybu je možné použiť na tuhé objekty a hraničné uzly objektov s sieťou. Povrch vymedzený týmito uzlami možno považovať za „tuhý povrch“. Počas simulácie sa obmedzené uzly budú pohybovať synchronizovane rýchlosťou a smerom definovanými ovládacími prvkami pohybu. V 3D prostredí sú k dispozícii dva typy ovládacích prvkov pohybu.

**Hnutie za preklad**

Medzi rôzne typy ovládacích prvkov pohybu, ktoré sú k dispozícii v rámci ovládacích prvkov pohybu pre preklad, patria [Speed](/docs/en/pre_processor/15_movement_controls_definition/15_1_speed/), [Force](/docs/en/pre_processor/15_movement_controls_definition/15_2_force/), [Hammer](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/), [Screw press](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/), [Mechanical press](/docs/en/pre_processor/15_movement_controls_definition/15_5_mechanical_press/), [Hydraulic press](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/), [Sliding Die](/docs/en/pre_processor/15_movement_controls_definition/15_7_sliding_die/) a [Path](/docs/en/pre_processor/15_movement_controls_definition/15_8_path/), ako je znázornené na obr. 33.2.36. Ďalšie informácie o týchto ovládacích prvkoch pohybu nájdete v [15\. Movement controls settings.](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image035.jpg' | relative_url }})

Preklad okna „Ovládacie prvky pohybu“

**Rotačný pohyb**

Rotačný pohyb je definovaný uhlovou rýchlosťou alebo krútiacim momentom okolo pevného stredu otáčania. V rámci ovládacích prvkov pre rotačný pohyb sú k dispozícii dva typy ovládacích prvkov: krútiaci moment a uhlová rýchlosť, ako je znázornené na obr. 33.2.37. Ďalšie informácie nájdete v [15.9. Rotational movement.](/docs/en/pre_processor/15_movement_controls_definition/15_9_rotational_movement/).

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image034.jpg' | relative_url }})

Okno Ovládacie prvky rotačného pohybu

Ďalšie informácie o týchto ovládacích prvkoch nájdete v [15\. Movement Controls Settings.](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

### Nehnuteľnosť

V okne „Vlastnosti objektu“ sa zadávajú rôzne parametre objektu, ktoré ovplyvňujú buď termomechanické správanie objektu, alebo správanie numerického riešenia. (Pozri obr. 33.2.38.) Ďalšie informácie nájdete v [16\. Object properties.](/docs/en/pre_processor/16_object_properties/16_object_properties/).

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image036.jpg' | relative_url }})

Okno vlastností objektu

### **Inicializácia**

V okne „Initialize“ sú k dispozícii na inicializáciu niektoré bežne používané stavové premenné, ako napríklad teplota, deformácia, napätie, poškodenie, rýchlosť, posunutie atď. Používateľ môže inicializovať hodnoty týchto stavových premenných tak, že ich zadá do príslušného poľa a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). Obr. 33.2.39. znázorňuje rôzne stavové premenné, ktoré sú k dispozícii v okne Initialize. V prípade stavových premenných, ako sú rýchlosť a posunutie, kde je k dispozícii toľko vstupných polí, koľko je rozmerov, musí používateľ v príslušných poliach zadať smerové hodnoty premenných a následným kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) sa vypočíta celková rýchlosť a posunutie. V závislosti od typu stavovej premennej ich môže používateľ inicializovať aj z okien s údajmi o uzloch a prvkoch. Ďalšie informácie o tom, ako inicializovať stavové premenné v oknách „Node“ a „Element“ (pozri obr. 33.2.40. a obr. 33.2.41.), nájdete v [17.1. Object node variables](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) a [17.2. Object element variables.](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/).

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image030.jpg' | relative_url }})

Okno inicializácie

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image031.jpg' | relative_url }})

Okno „Údaje uzla“

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image032.jpg' | relative_url }})

Okno „Údaje o prvku“

## Polohovanie

Na obrázku 33.2.42 nižšie je zobrazené okno na nastavenie polohy.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image037.jpg' | relative_url }})

Okno na nastavenie polohy

**Automatické polohovanie** ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }})

Kliknutím na toto tlačidlo systém automaticky umiestni objekty vzhľadom na smer pohybu hornej matrice; táto možnosť sa najlepšie hodí pre jednoduché nastavenie s tromi objektmi – obrobkom, hornou matricou a spodnou matricou.

**Umiestňovanie objektov** ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }})

Kliknutím na toto tlačidlo môže používateľ umiestniť objekty do požadovaných smerov. K dispozícii sú rôzne typy možností umiestnenia, ako napríklad [Drag](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_1_Drag_Positioning), [Drop](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_5_Drop_positioning), [Offset](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_2_Offset_Positioning), [Interference](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_3_Interference_positioning) a [Rotational](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_4_Rotational_positioning), ako je znázornené na obr. 33.2.43. Ďalšie informácie o týchto možnostiach nájdete v časti [19\. Object Positioning.](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image038.jpg' | relative_url }})

Okno na umiestňovanie objektov

## Plánované polohovanie

Ak si používateľ nie je istý polohou objektu, ako je to v prípade objektov typu „Read From DB“, naplánované umiestňovanie pomôže objekty presne umiestniť.

Funkcia „Schedule positioning“ umožňuje používateľovi definovať umiestnenie objektov v nastaveniach MO pre nasledujúce operácie, pre ktoré sa nevytvára databáza (DB), tak, aby boli objekty umiestnené ešte pred vytvorením databázy počas spustenia simulácie v dávkovom režime. (Pozri obr. 33.2.44.)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image039.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

## Kontakt (vzťahy medzi objektmi)

Účelom vzťahov medzi objektmi je definovať, ako rôzne objekty v simulácii vzájomne interagujú. Tabuľka vzťahov zobrazuje aktuálne definované vzťahy medzi objektmi. Všetky objekty, ktoré môžu prísť do kontaktu v priebehu simulácie, musia mať definovaný kontaktný vzťah. To zahŕňa aj objekt, ktorý má vzťah sám so sebou, ak dochádza k vlastnému kontaktu, ako je to v prípade prekrývania. Správne definovanie týchto vzťahov je veľmi dôležité, aby simulácia presne modelovala proces formovania. Kľúčové premenné, ktoré je potrebné definovať medzi kontaktujúcimi sa objektmi, sú:

  * [Friction factor](../../pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria.htm#20_1_1_Friction_\(FRCFAC\))

  * [Interface heat transfer coefficient](../../pre_processor/20_inter-object_data_definition/20_2_interface_thermal_data.htm#20_2_1_Interface_heat_transfer_coefficient_\(IHTCOF\))

  * [Contact relation](../../pre_processor/20_inter-object_data_definition/20_inter-object_data_definition.htm#20_1_Contact_relation_\(CNTACT\))

  * [Separation criterion](../../pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria.htm#20_1_4_Separation_Type)

Súčasťou riadenia interakcií medzi objektmi je aj generovanie okrajových podmienok medzi objektmi.

Vzťahy medzi objektmi určujú, ktoré objekty sa môžu navzájom dotýkať, a ako sa dotýkajúce sa objekty budú správať počas kontaktu. Pre každú dvojicu objektov sa tu nastavujú vzťahy kontaktu, okrajové podmienky medzi objektmi, vzťahy trenia a prenosu tepla (obr. 33.2.45.). Zjednodušene povedané, postup definovania vzťahov medzi objektmi prebieha v nasledujúcich krokoch.

  * Určte kombináciu „master-slave“ – V prípade jediného deformovaného objektu by mal byť deformovaný objekt vždy objektom typu „slave“. V prípade viacerých deformovaných telies by mal byť objektom typu „slave“ ten objekt, ktorý má na rozhraní týchto dvoch objektov jemnejšiu sieť.

  * Nastavte parametre pre danú dvojicu master-slave – to môžete urobiť kliknutím na tlačidlo „Edit“ a nastavením príslušných parametrov. (Pozri [Fig. 20.2.](../../pre_processor/20_inter-object_data_definition/20_inter-object_data_definition.htm#Fig_20_2_Inter_object_constant_Shear_Friction_options_for__2D) a [Fig. 20.3.](../../pre_processor/20_inter-object_data_definition/20_inter-object_data_definition.htm#Fig_20_3_Inter_object_constant_Shear_Friction_options_for_3D))

  * Vytvorenie kontaktu pre všetky objekty – Najskôr kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_initialize_button.jpg' | relative_url }}) a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}), čím sa vytvorí kontakt. Ak sa kontakt nevytvoril tak, ako ste očakávali, skontrolujte nasledujúce:

  * Orientácia geometrie tuhých objektov. Uistite sa, že geometria je vnútorná strana tuhých objektov zatienená.

  * Sieť v oblasti kontaktu. Ak je sieť hrubá, v blízkosti miesta kontaktu sa nemusia nachádzať žiadne uzly.

  * Uistite sa, že sú tieto časti skutočne v tesnej blízkosti jedna druhej.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image040.jpg' | relative_url }})

Okno definície údajov medzi objektmi

V MO máme dva typy vzťahov medzi objektmi. Sú to **User** a **System**.

**Systém**: Po výbere tohto prepínača (pozri obr. 33.2.46..) systém priradí predvolené vzťahy medzi objektmi. V prípade potreby môže používateľ pridať aj mazivá (pozri obr. 33.2.47.). Kliknutím na tlačidlo Upraviť môže používateľ definovať mazivá potrebné pre simuláciu. (pozri obr. 33.2.48.)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image041.jpg' | relative_url }})

Okno medzi objektmi s výberom systému

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image042.jpg' | relative_url }})

Pridávanie maziva v okne „Medzi objektmi“

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image043.jpg' | relative_url }})

Pridanie maziva z okna „Edit“

**Používateľ**: Pri operácii „Forming“ je štandardne vybrané rádio tlačidlo „Používateľ“. Používateľ môže pridať vzťahy kliknutím na tlačidlo „Pridať“, ako je znázornené na obr. 33.2.45.

Kliknutím na tlačidlo „Upraviť ****![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }})****“ môže používateľ nastaviť parametre trenia a prenosu tepla medzi fázami. Ďalšie informácie nájdete v časti [20\. Inter-object Data Definition](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/).

Ďalšie informácie o modeloch [Deformation](/docs/en/pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/), [Thermal](/docs/en/pre_processor/20_inter-object_data_definition/20_2_interface_thermal_data/), [Heating](/docs/en/pre_processor/20_inter-object_data_definition/20_3_interface_resisitivity/), [Friction window](../../pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria.htm#20_1_6_Friction_Window), [Tool wear](/docs/en/pre_processor/20_inter-object_data_definition/20_4_tool_wear/) a [Rigid contact](/docs/en/pre_processor/20_inter-object_data_definition/20_5_rigid_contact/) nájdete v kapitole [20\. Inter-object Data Definition](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/). 

## Ovládacie prvky na zastavenie

Parametre ukončenia určujú čas priebehu, po uplynutí ktorého sa simulácia ukončí. Simuláciu je možné ukončiť na základe maximálneho počtu simulovaných časových krokov, maximálnej kumulovanej elementárnej deformácie, maximálneho času priebehu, maximálneho zdvihu, minimálnej rýchlosti alebo maximálneho zaťaženia primárneho objektu. Simulácia sa zastaví, keď bude splnená podmienka ktoréhokoľvek z týchto parametrov ukončenia.

**Deformácia**

Na nižšie uvedenom obr. 33.2.49 sú znázornené rôzne typy zariadení na zastavenie deformácie.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image044.jpg' | relative_url }})

Okno „Ovládacie prvky zastavenia deformácie“

**Maximálny zdvih matrice**: Ukončí simuláciu, keď celkový posun ([SMAX](/docs/en/keyword_documentation/s/smax/)) primárnej matrice dosiahne zadanú hodnotu. Hodnota zdvihu pre daný objekt sa zadáva na karte „Pohyb objektu“.

**Maximálne zaťaženie**: Ukončí simuláciu, keď zložka zaťaženia v osi X, Y alebo Z primárneho telesa dosiahne hodnotu X, Y alebo Z nastavenú v parametri [LMAX](/docs/en/keyword_documentation/l/lmax/). Zvyčajne sa používa v prípadoch, keď je riadenie pohybu primárneho objektu založené na rýchlosti alebo je určené používateľom.

**Pomer kontaktnej plochy:** Pomer kontaktnej plochy je pomer plochy, ktorá je v kontakte s lisovacími formami, k celkovej povrchovej ploche polotovaru. Ak tento pomer prekročí stanovenú hodnotu, simulácia sa zastaví.

**Vzdialenosť medzi objektmi:** Ukončí simuláciu, keď vzdialenosť medzi referenčnými bodmi ([MDSOBJ](/docs/en/keyword_documentation/m/mdsobj/)) na dvoch objektoch dosiahne zadanú hodnotu.

**Tepelná**

Na nižšie uvedenom obr. 33.2.50 sú znázornené rôzne typy tepelných omezovačov.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image045.jpg' | relative_url }})

Okno „Ovládacie prvky tepelného zastavenia“

**Spôsob zastavenia**

**Žiadne**: Neaplikuje žiadne opatrenia na obmedzenie prehriatia

**Ľubovoľný uzol:** Simulácia sa zastaví, keď ktorýkoľvek uzol v sochore dosiahne zadanú hodnotu.  
**Všetky uzly**: Simulácia sa zastaví, keď všetky uzly v sochárskej surovici dosiahnu zadanú hodnotu.

**Vybraný uzol**: Simulácia sa zastaví, keď zadaný uzol v sochárskej surovine dosiahne zadanú hodnotu.  
**Priemer všetkých uzlov**: Simulácia sa zastaví, keď priemerná teplota všetkých uzlov v sochore dosiahne zadanú hodnotu.  
**Priemerná teplota povrchu + maximálna teplota**: Simulácia sa zastaví, keď priemerná teplota všetkých uzlov na povrchu sochory + maximálna teplota v sochore dosiahnu zadanú hodnotu.

**Teplotný rozsah**

Okrem jednej hodnoty je možné na zastavenie simulácie použiť aj teplotný rozsah.

**Zastaviť, ak teplota je mimo rozsahu**: Simulácia sa zastaví, ak hodnota teploty prekročí stanovený rozsah.

**Zastaviť, keď je teplota v rozsahu**: Simulácia sa zastaví, keď sa hodnota teploty nachádza v zadanom rozsahu.

## Ovládacie prvky simulácie

V ovládacích prvkoch simulácie v režime s návodom môže používateľ vybrať typ režimu simulácie a typ výstupu. Obr. 33.2.51 znázorňuje stránku „Krok“ v režime s návodom a obr. 33.2.52 znázorňuje ovládacie prvky simulácie v režime s návodom, kde môže používateľ definovať ovládacie prvky operačných krokov a definíciu krokov. Tu sú k dispozícii základné možnosti potrebné na vytvorenie operácie, zatiaľ čo režim Expert ponúka podrobnejšie možnosti.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image046.jpg' | relative_url }})

Režim s návodom – Krok

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image049.jpg' | relative_url }})

Ovládacie prvky simulácie v režime s návodom

Systém DEFORM rieši časovo závislé nelineárne úlohy generovaním série riešení metódou konečných prvkov (FEM) v diskrétnych časových krokoch. V každom časovom kroku sa rýchlosti, teploty a ďalšie kľúčové premenné každého uzla v sieti konečných prvkov určujú na základe okrajových podmienok, termomechanických vlastností materiálov obrobku a prípadne riešení z predchádzajúcich krokov. Ostatné stavové premenné sa odvodzujú z týchto kľúčových hodnôt a aktualizujú sa pri každom časovom kroku. Dĺžka tohto časového kroku a počet simulovaných krokov sa určujú na základe informácií  
uvedené v ponuke ovládacích prvkov krokov.

**Počet simulačných krokov (NSTEP)**

Parameter „Počet simulačných krokov“ určuje počet krokov, ktoré sa majú spustiť od počiatočného čísla kroku. Simulácia sa zastaví po vykonaní tohto počtu simulačných krokov, pokiaľ sa nespustí príkaz na zastavenie simulácie alebo ak simulácia nenarazí na problém. Napríklad, ak je počiatočné číslo kroku -35 ([NSTART](/docs/en/keyword_documentation/n/nstart/)) a je špecifikovaných 30 krokov ([NSTEP](/docs/en/keyword_documentation/n/nstep/)), simulácia sa zastaví po 65. kroku, pokiaľ sa skôr nespustí iný príkaz na zastavenie.

**Krok pri ukladaní (STPINC)**

Krok prírastku ([STPINC](/docs/en/keyword_documentation/s/stpinc/)), ktorý sa má uložiť do databázy, určuje počet krokov, ktoré systém uloží do databázy. Pri spustení simulácie sa musí vypočítať každý krok, ale nemusí sa nutne uložiť do databázy. Uložením väčšieho počtu krokov sa zachová viac informácií o procese, čo však bude vyžadovať väčší úložný priestor.

**Primárny čip (PDIE)**

Primárna matrica ([PDIE](/docs/en/keyword_documentation/p/pdie/)) je objekt, pre ktorý je definovaných mnoho kritérií zastavenia a krokovania. Napríklad brzdná vzdialenosť založená na zdvihu primárnej matrice. Keď zdvih objektu definovaného ako primárna matrica dosiahne hodnotu posunu primárnej matrice, simulácia sa zastaví bez ohľadu na to, či boli špecifikované ďalšie kroky. Funkcia „Krok podľa zdvihu“ určuje veľkosť kroku na základe pohybu primárnej matrice. Primárna matrica je zvyčajne priradená k objektu, ktorý je najviac riadený kováčskym strojom. Napríklad matrica pripevnená k piestu mechanického lisu by bola označená ako primárny objekt.

**Ovládanie krokového posunu ([DSMAX](/docs/en/keyword_documentation/d/dsmax/)/[DTMAX](/docs/en/keyword_documentation/d/dtmax/))**

Veľkosť kroku riešenia je možné riadiť časovým krokom alebo posunom primárnej matrice. Ak je špecifikovaný zdvih na krok, primárna matrica sa v každom časovom kroku posunie o zadanú hodnotu. Celkový posun primárnej matrice bude rovný posunu na krok vynásobenému celkovým počtom krokov. Ak je špecifikovaný čas na krok, použije sa časový interval na krok. Posun matrice na krok bude rovný časovému kroku vynásobenému rýchlosťou matrice.

  
Nastavenia krokových regulátorov založených na teplote ([DTPMAX](/docs/en/keyword_documentation/d/dtpmax/)) tiež ovplyvňujú časový krok. Účelom týchto regulátorov je určiť časový krok simulácie, ktorá je riadená deformáciou vyvolanou teplotou.

Definícia riadenia krokového prírastku bola rozšírená tak, aby zahŕňala krokové funkcie závislé od času aj od zdvihu; tieto možnosti sú k dispozícii v režime Expert. To znamená, že veľkosť kroku (či už ide o čas na krok alebo zdvih na krok) je teraz možné definovať ako funkciu času alebo zdvihu. Táto funkcia umožňuje v prípade potreby dosiahnuť jemnejšie rozlíšenie uložených informácií o modeli. (typicky smerom ku koncu zdvihu, kde môžu nastať prudké zmeny zaťaženia formy, plnenia dutiny alebo tvorby prebytku materiálu)

Počet zdvihov na krok je často intuitívnejší. Čas na krok je však potrebné špecifikovať pri každej úlohe, v ktorej nedochádza k pohybu matice (napríklad pri prenose tepla), alebo pri každej úlohe, kde sa používa regulácia sily. 

Na obr. 33.2.53 sú zobrazené ovládacie prvky simulácie v režime Expert.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image047.jpg' | relative_url }})

Ovládacie prvky simulácie v režime pre pokročilých

Možnosti definované v časti „Ovládacie prvky simulácie“ (pozri obr. 33.2.53.) ovplyvňujú numerické správanie riešenia. Hlavné ovládacie prvky slúžia na zadanie názvu simulácie, sústavy jednotiek, typu geometrie atď.

Ovládacie prvky pre kroky a ukončenie slúžia na určenie časového kroku, celkového počtu krokov a kritérií na ukončenie simulácie.  
Tu je možné zadať podmienky spracovania, ako napríklad teplotu okolia a konvekčný koeficient.

Ďalšie informácie a popis možností v ovládacích prvkoch simulácie nájdete v [9\. Simulation Controls.](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

## Vytvoriť databázu 

**Overiť údaje**![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})****

Systém skontroluje údaje. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvoriť databázu ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})**

Kliknutím na toto tlačidlo sa vygenerovala databáza pre nastavenie. (Pozri obr. 33.2.54.)

**Pridať súbor s kľúčom**

Akékoľvek informácie, ktoré nie sú definované v sprievodcovi, ale napriek tomu sa vzťahujú na daný proces, je možné načítať ako súbor s príponou .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt – tieto hodnoty je možné definovať v súbore s príponou .key, následne stačí zmeniť len tento súbor a simuláciu je možné spustiť znova.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image048.jpg' | relative_url }})

Okno „Vytvoriť databázu“
