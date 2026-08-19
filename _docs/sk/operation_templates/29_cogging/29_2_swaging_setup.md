---
lang: sk
title: "29.2. Nastavenie lisovania"
---

# 29.2. Nastavenie lisovania

29.2.1. Terminológia lisovania

29.2.2. Metóda polohovania

29.2.3. Ako pridať operáciu lisovania

29.2.4. Stránka procesu

29.2.5. Tabuľka prechodov

29.2.6. Zoznam materiálov

29.2.7. Stránka objektu

29.2.8. Okienko na polotovary

  * Geometria

  * Sieťovina

  * Materiál

  * Okrajové podmienky

  * Nehnuteľnosť

29.2.9. Horná matrica

  * Geometria

  * Sieťovina

  * Materiál

  * Ovládanie pohybu

29.2.10. Polohovanie

29.2.11. Plánované umiestnenie

29.2.12. Kontakt

29.2.13. Náhľad simulácie

29.2.14. Ovládacie prvky simulácie

29.2.15. Vytvorenie databázy

29.2.16. Spustenie simulácie

29.2.17. Následné spracovanie

Operácia lisovania vedie používateľa k jednoduchému nastaveniu procesu pomocou tabuľky priechodov, nastavení opätovného ohrevu, základných operácií a ovládacích prvkov pohybu. Tabuľka priechodov pomáha používateľovi nastaviť operáciu lisovania v jednej akcii po zadaní posuvu matrice a otáčania polotovaru. Tabuľka priechodov umožňuje používateľovi ľahko nastaviť viacero priechodov kopírovaním nastavení z jedného priechodu do druhého. Operáciu je možné nastaviť buď s použitím dvoch, alebo štyroch matíc podľa požiadaviek používateľa; pri lisovaní sa zvyčajne používajú 4 matice. Lisovacie údery sa zastavujú na základe definovaného zdvihu lisovania.

## Terminológia v oblasti lisovania

**Automatický výpočet rezov:** Aktiváciou tejto možnosti systém automaticky vypočíta počet rezov, ktoré sa majú simulovať, na základe axiálneho posuvu na jeden rez pre danú dĺžku polotovaru.

**Počet krokov:** Pomocou tejto možnosti môže používateľ ručne nastaviť požadovaný počet krokov pre simuláciu zubového posunu.

Poznámka: Čo sa rozumie pod pojmom „Bite“?

Zub je nič iné ako dĺžka, o ktorú sa zub deformuje pri danom posuve.

**Axiálna rýchlosť posuvu:** Ide o vzdialenosť, o ktorú sa súprava matíc posunie pri každom zábere v axiálnom smere pozdĺž dĺžky sochoru (nominálny záber).

Napr.: - Predpokladajme, že ak nastavíme axiálnu rýchlosť posuvu na 10 mm a dĺžku polotovaru na 60 mm, sada matíc sa po každom zábere posunie o 10 mm, takže celú dĺžku pokryje 7 zábermi vrátane počiatočného záberu.

Radiálny posun na jeden zdvih: ide o vzdialenosť, o ktorú sa súprava matíc posunie v radiálnom smere pri jednom zdvihu.

**Hrúbka prierezu:** Hrúbka prierezu je hrúbka, ktorú je potrebné zachovať na sochore v smere primárneho pohybu matrice. Slúži tiež na riadenie zastavenia a na počiatočné nastavenie polohy matríc. V procese lisovania sa nepoužíva.

**Smer pohybu:** Určuje konkrétny smer (+X alebo -X) axiálneho pohybu valca.

**Otočenie po každom zábere (°)**: Pomocou tejto možnosti môže používateľ nastaviť uhol, o ktorý sa má polotovar otočiť po každom zábere.

**Otočenie na jeden priechod (°):** Pomocou tejto možnosti môže používateľ nastaviť uhol, o ktorý sa má polotovar otočiť po každom priechode.

## Metóda polohovania matice

  * ****[**0 - % (Percentage or fraction of billet length between 0 to 1)** :](29_1_cogging_setup.htm#Die_positioning_using_the_percentage_as_reference) Počiatočná alebo koncová poloha sa určuje ako zlomok dĺžky polotovaru od príslušných koncov polotovaru, pričom sa zohľadňuje smer zubovania.

  * [**1 – ref (Reference points)**](29_1_cogging_setup.htm#Die_positioning_with_reference_point): Počiatočná alebo koncová poloha sa určuje výberom dvoch bodov na polotovare; v tabuľke sú zobrazené iba súradnice x.

  * [**2 – dst (Absolute distance from billet ends)**](29_1_cogging_setup.htm#Die_positioning_using_the_distance_as_reference): Počiatočná alebo koncová poloha sa určuje na základe vzdialenosti od príslušných koncov sochory, pričom sa zohľadňuje smer zubového posunu.

  * [**3 -ofst (Offset)**](29_1_cogging_setup.htm#DIe_positioning_using_Offset_as_reference): Počiatočná poloha je určená ako relatívna vzdialenosť od predchádzajúcej polohy matrice.

Ďalšie podrobnosti o metódach polohovania matrice sú vysvetlené v časti „Nastavenie coggingu“; ďalšie informácie nájdete v časti [29.1.2.Die Positioning Method](29_1_cogging_setup.htm#29_1_2_Die_Positioning_Method)

## Ako pridať operáciu lisovania

Operácia lisovania je k dispozícii v rámci operácie 3D Cogging a je prístupná cez sprievodcu MO Wizard, ktorý je možné otvoriť z hlavného grafického rozhrania. V sprievodcovi MO je možné operáciu zubovania pridať z karty „Explorer“ kliknutím na tlačidlo vedľa položky „3D Cogging“ a výberom typu procesu „Swaging“ v okne nastavení procesu, ako je znázornené na obr. 29.2.1. Operáciu môže používateľ pridať aj pomocou funkcie drag and drop do editora operácií.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image001.jpg' | relative_url }})

Do nástroja Operation Explorer bola pridaná operácia „Cogging“

## Stránka procesu

Na obr. 29.2.2. sú zobrazené možnosti nastavenia podmienok procesu; tieto možnosti sú vysvetlené nižšie.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image002.jpg' | relative_url }})

Okno procesu

**Typ procesu**

  * **Cogging**: Ide o proces predĺženia sochoru zmenšením jeho priemeru.

  * **Swagin****g** : Modelovanie procesov rotačného kovania sa nazýva „swagging“.

Cieľom lisovania je modelovanie postupného tvarovania viacerých úsekov/prechodov v rámci jednej operácie s automatickým zastavením a opätovným spustením medzi jednotlivými krokmi procesu.

Sprievodca lisovaním slúži na vytvorenie hlavných súborov a súborov s kľúčovými slovami pre polotovary, lisovacie formy a trny, ktoré obsahujú potrebné informácie o procese, geometrii a materiáloch potrebné na spustenie simulácie lisovania.

**Teplotné podmienky**  
Lisovanie je zvyčajne proces spracovania za studena, využíva sa však aj v teplotnom rozsahu polotepla a tepla. Používateľ má teda možnosť zvoliť si tepelné výpočty pre obrobok aj lisovacie formy.

  * **Studená izotermická**: Pri tomto procese budeme môcť pozorovať iba deformáciu sochoru.

**Poznámka**: Ak zvolíme voľbu „Cold Isothermal“, možnosti prenosu tepla sa zneaktívnia (zšednú).

  * **Horúci – výpočet teploty iba v sochore**: V tomto procese môžeme vypočítať teplotu iba v sochore. Keďže sa na lisovacích formách a manipulátoroch nevykonávajú žiadne tepelné výpočty, pre ne sa nevytvára žiadna sieť. Budeme môcť vykonať operácie týkajúce sa prenosu tepla aj deformácie.

  * **Horúci proces – výpočet teploty v sochore a formách**: V rámci tohto procesu vieme vypočítať teplotu v sochore, formách a manipulátoroch. Všetky objekty by mali byť rozdelené na sieť, keďže potrebujeme vykonať tepelné výpočty na sochore, formách a manipulátoroch. Budeme môcť vykonať výpočty prenosu tepla aj deformácie.

Prenos tepla medzi jednotlivými zdvihmi je možné nastaviť aj zaškrtnutím políčka „Prenos tepla na jeden zdvih“, ako je znázornené na obr. 29.2.2. Podrobnejšie informácie o týchto prevádzkových cykloch sú uvedené v časti „Nastavenie coggingu“ [Heat transfer per bite.](29_1_cogging_setup.htm#Heat_Transfer_Per_Bite)

**Nastavenie objektu**

  * **Počet matíc:** Proces lisovania sa vykonáva buď s použitím 4 matíc, alebo 2 matíc, v závislosti od prierezu a rozsahu deformácie. Používateľ si môže vybrať buď 4 matrice, alebo 2 matrice na základe simulovaného procesu. Možnosť rotačnej symetrie obrobku je k dispozícii iba pri použití 4 matíc; túto možnosť je možné aktivovať zaškrtnutím políčka „Použiť rotačnú symetriu“.

  * **Použitie odlišnej geometrie pre hornú a spodnú maticu:** Ak sú v procese lisovania geometrie v sade matíc odlišné, zaškrtnutím tohto políčka budeme môcť definovať odlišné typy geometrií pre hornú a spodnú maticu.

  * **Použitie manipulátorov**: Ak sa používajú manipulátory, používateľ môže zaškrtnúť toto políčko, čím aktivuje definíciu manipulátora a jeho nastavenia. V procese lisovania sa nepoužíva (používa sa v procese zubovania).

  * **Použiť mandrel**: Zaškrtnutím tohto políčka bude mať používateľ možnosť použiť mandrel pri nastavení spracovania dutých obrobkov. Používa sa najmä pri procese lisovania na vytvorenie vnútorných profilov s úzkymi toleranciami, ktoré môžu byť valcovité, kužeľovité alebo stupňovité. Tvarovanie na trne umožňuje výrobu vnútorných profilov, ako sú drážky, neokrúhle tvary, špirálovité tvary atď.

  * **Použiť rotačnú symetriu**: Zaškrtnutím tohto políčka bude môcť používateľ definovať symetriu na obrobku, pozri obr. Využitím symetrie je možné skrátiť čas simulácie.

  * **Opätovné zahriatie obrobku medzi priechodmi** je možné simulovať pomocou zaškrtávacieho políčka „Použiť adaptívne opätovné zahriatie“ v okne procesu a definovaním vstupných údajov. Podrobnejšie informácie nájdete v časti „Nastavenie coggingu“ [Use Adaptive Reheat.](29_1_cogging_setup.htm#Use_Adaptive_Reheat)

## Tabuľka priechodov

Na obr. 29.2.3. je zobrazená tabuľka priechodov. V tejto tabuľke definujeme informácie o celom priechode pre nastavenie lisovania. Rôzne možnosti dostupné v tabuľke priechodov sú vysvetlené v časti Terminológia lisovania. Informácie o priechode sa pri pridávaní nového priechodu preberajú z predchádzajúceho priechodu a potrebné údaje je možné upravovať podľa požiadaviek procesu. Pozrite si časť 29.2.1. Terminológia lisovania.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image003.jpg' | relative_url }})

Okno s tabuľkou priechodov pre proces lisovania

Tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}): Toto tlačidlo slúži na zvýšenie počtu prechodov o jednu jednotku.

Tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}): Toto tlačidlo slúži na vymazanie existujúceho prístupového kódu.

![]({{ '/assets/icons/pre_icons/mo_swap_button.jpg' | relative_url }}) : Ak klikneme na tlačidlo „swap“, parametre priechodu sa na zobrazenie usporiadajú horizontálne. (Pozri obr. 29.2.4.)

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image004.jpg' | relative_url }})

Po vymenení miest odovzdať informácie z tabuľkového okna v horizontálnom smere

![]({{ '/assets/icons/pre_icons/mo_pass_details_button.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ zadať pokročilé informácie o preukazoch, ktoré sa vzťahujú na všetky preukazy – pozri obr. 29.2.5.

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image012.jpg' | relative_url }})

Okno „Pokročilé informácie o preukaze“

**Prechod medzi dvojicami matíc:**

Táto voľba platí iba v prípade, ak sa používajú 4 matrice a veľkosť deformácie, t. j. zdvih kovania, sa líši pre horizontálnu sadu matríc a vertikálnu sadu matríc používaných pri zubovaní. Ďalšie podrobnosti nájdete v časti [Shift between pairs of dies](29_1_cogging_setup.htm#Shift_between_pairs_of_dies) v kapitole [Pass table.](29_1_cogging_setup.htm#29_1_6_Pass_Table).

##  Zoznam materiálov

Aby simulácia dosiahla vysokú úroveň presnosti, je dôležité poznať vlastnosti materiálu, ktoré sú potrebné na špecifikáciu materiálu použitého v programe DEFORM.

Pri nastavovaní simulácie je potrebné pre objekty špecifikovať vlastnosti materiálov. V operácii MO Swaging je možné načítať všetky materiály potrebné pre danú operáciu naraz a požadovaný materiál vybrať neskôr pri nastavovaní úlohy. Používateľ môže pridať materiál výberom možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) „Načítať údaje o materiáli z knižnice“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) po výbere požadovaného materiálu z kategórií, ako je znázornené na obr. 29.2.6.

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image014.jpg' | relative_url }})

Importovať materiál z okna knižnice

(alebo)

Ďalším spôsobom pridania materiálu je kliknutie na ikonu materiálu na karte prehliadača, čím sa zobrazí zoznam materiálov z knižnice rozdelených do rôznych kategórií, ako je znázornené na obr. 29.2.7. Vyberte požadovaný materiál a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}). Používateľ môže požadovaný materiál pridať aj pomocou funkcie „drag and drop“ (ťahaj a pusť) do okna materiálu.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image005.jpg' | relative_url }})

Pridávanie materiálu z karty „Explorer“

(alebo)

V okne so zoznamom materiálov je možné pridať nový materiál kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Po pridaní materiálu kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vyberte príslušnú kartu, kde zadáte potrebné údaje pre simuláciu, ako je znázornené na obr. 29.2.8.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image006.jpg' | relative_url }})

Pridať materiál z okna Zoznam materiálov

**Import údajov o materiáloch zo súboru** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}): Importuje údaje o materiáloch zo súboru s príponou .Key alebo .DB.

**Načítať údaje o materiáloch z knižnice** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}): Importuje materiály z knižnice.

**Uloženie údajov o materiáli do súboru**![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) : Uloží materiál do súboru.

**Uloženie údajov o materiáli do knižnice****** ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ uložiť materiál do knižnice a v budúcnosti ho podľa potreby opäť načítať pre ďalšie simulácie.

****

**Zloženie zmesi**

Materiály typu „zmes“ ([MSTMTR](/docs/en/keyword_documentation/m/mstmtr/)) sa používajú v prípade, že sa v simulácii má modelovať fázová premena. Premenlivý materiál sa modeluje ako „zmes“ fáz, z ktorých sa skladá. Napríklad uhlíková oceľ sa môže modelovať ako zmes austenitu, perlitov, bainitu a martenzitu. Ak je definovaný zmesový materiál, mali by sa definovať pravidlá premeny, ktoré riadia premenu jednej fázy na druhú. (Pozri obr. 29.2.9.)

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image018.jpg' | relative_url }})

Pridanie zmesi ako materiálu

**Vlastnosti kópie**

Slúži na kopírovanie bežných vlastností materiálov, ako sú plastické, elastické, tepelné atď., z jedného materiálu do druhého pri vytváraní/definovaní údajov o materiáli, ako je znázornené na obr. 29.2.10. V tomto dialógovom okne je potrebné vybrať zdroj a cieľ kopírovania vlastností, ako aj samotné vlastnosti, ktoré sa majú skopírovať.

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image019.jpg' | relative_url }})

Okno „Kopírovať vlastnosti materiálu“

**Previesť jednotky ![]({{ '/assets/icons/pre_icons/mo_convert_units_button.jpg' | relative_url }})**

Slúži na prevod jednotkového systému aktuálne vybraného materiálu zo zoznamu materiálov zo systému SI na anglický systém alebo naopak, prípadne môže používateľ použiť akýkoľvek iný násobný koeficient, ako je znázornené na obr. 29.2.11. Kliknutím na toto tlačidlo sa zobrazia príslušné násobné koeficienty pre prevod z ![]({{ '/assets/icons/pre_icons/mo_si_to_english_button.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_english_to_si_button.jpg' | relative_url }}); následným kliknutím na tlačidlo „Previesť“ sa prevod vykoná a okno prevodu sa zatvorí. Túto prevodnú tabuľku je možné uložiť pomocou tlačidla „Uložiť“ a je možné ju tiež upraviť pomocou programu WordPad/Notepad a následne ju opäť načítať do súboru UNITCONV.DAT pomocou tlačidla „Načítať“.

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image020.jpg' | relative_url }})

Okno pre prevod jednotiek

## Stránka objektu

Na obr. 29.2.12. sú zobrazené informácie v okne objektu. Táto funkcia umožňuje zachovať veľkosť alebo tvar prvku v prípade väčšej deformácie, ako napríklad pri zubovaní. K dispozícii je tiež možnosť vyrovnania obrobku v prípade ohybu po každom zábere alebo prechode. Tieto funkcie sú užitočné pri operáciách s ozubením; podrobnosti o týchto možnostiach nájdete v [29.1.8. Object window](29_1_cogging_setup.htm#29_1_8_Object_window).

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image021.jpg' | relative_url }})

Okno objektu

## Okienko na polotovary

V tomto okne môže používateľ nastaviť požadovanú teplotu pre objekt a vybrať typ objektu, ako je znázornené na obr. 29.2.13. Pre sochársku hlinenú formu je štandardne vybraný typ objektu „Plast“. Používateľ môže tiež importovať objekt z iných databáz alebo súborov kľúčov pomocou tlačidla a vyhľadania príslušného súboru.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image007.jpg' | relative_url }})

Nastavenie teploty sochory

**Geometria**  
Okno „Geometria“ slúži na definovanie geometrie objektu, ako je znázornené na obr. 29.2.14. Ak nie je definovaná žiadna geometria, aktívne bude iba pole „Definovať primitívy“, ostatné možnosti budú sivé. Po vytvorení geometrie sa aktivujú všetky možnosti.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image008.jpg' | relative_url }})

Okno Geometria

  
**Definícia primitívu**  
Máme tri rôzne typy geometrických primitív pre polotovar: kruh, osemuholník a obdĺžnik, ako je znázornené na obr. 29.2.15.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image009.jpg' | relative_url }})

Okno s geometrickými primitívami pre celý diel

V prípade rotačnej symetrie bude k dispozícii iba primitív „dutý valec“, ako je znázornené na obr. 29.2.16.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image010.jpg' | relative_url }})

Okno s geometrickými primitívami pre rotačnú symetriu

Ďalšie informácie o možnostiach geometrie nájdete v [12.3. 3D Geometry Data Definition](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/)

**Sieťovina**  
**Cihlová sieťovina**  
Na nižšie uvedenom obr. 29.2.17 sú zobrazené možnosti generovania siete pre funkciu Brick Mesh v režime s návodom.

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image026.jpg' | relative_url }})

Možnosti mriežky tehál v režime s navádzaním

**2D rez**

  * **Prvky**: Počet sieťových prvkov predstavuje približný počet prvkov, ktoré budú vytvorené na 2D priečnom reze objektu. 

  * **Pomer veľkostí**: Pomer veľkostí je pomer medzi maximálnou veľkosťou prvku a minimálnou veľkosťou prvku v 2D priečnom reze.

  * **Počet vrstiev**: Slúži na nastavenie hrúbky vrstiev siete v axiálnom smere. Používateľ môže pre generovanie siete definovať požadovaný počet vrstiev. S rastúcim počtom vrstiev bude sieť hustejšia a hrúbka prvku v axiálnom smere sa zmenší. Podobne, ak sa počet vrstiev zníži, hrúbka prvku v axiálnom smere sa zvýši a počet vrstiev bude menší.

  * **Prekreslenie siete (tetraedrická sieť)**: Ak dôjde k výraznej deformácii a sieť typu „brick“ sa nedá prekresliť, systém automaticky zvolí tetraedrickú sieť a vygeneruje ju na základe definovaných nastavení.

  * **Počet prvkov**: Počet prvkov siete predstavuje približný počet prvkov, ktoré sa na objekte vygenerujú. Pri tetraedrickom prepočítaní siete sa použije tento definovaný počet prvkov.

  * **Vytvoriť sieť**: Sieť je možné vytvoriť kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

**Tetraedrická sieť**

Na nižšie uvedenom obr. 29.2.18 sú zobrazené možnosti generovania siete pre tetraedrickú sieť v režime s vedením.

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image028.jpg' | relative_url }})

Možnosti siete Tet v režime s vedením

  * **Prvky**: Počet sieťových prvkov predstavuje približný počet prvkov, ktoré sa vygenerujú na objekte. 

  * **Minimálna veľkosť prvku**: Ide o minimálnu veľkosť prvku; pri generovaní siete sa prvok vytvorí tak, aby spĺňal podmienku definovanej minimálnej veľkosti prvku. Veľkosť prvku neprekročí definovanú hodnotu.

  * **Pomer veľkostí**: Pomer veľkostí je pomer medzi maximálnou a minimálnou veľkosťou prvkov na objekte.

  * **Vytvoriť sieť**: Sieť je možné vytvoriť kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

Na nastavenie parametrov siete, ako sú veľkosť, tvar, hustota, typ prvkov atď., musí používateľ prejsť do expertného režimu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}), kde sú k dispozícii pokročilejšie možnosti vytvárania siete. Na obr. 29.2.19 nižšie sú zobrazené možnosti vytvárania siete dostupné v expertnom režime.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image011.jpg' | relative_url }})

Okno na generovanie siete v režime pre pokročilých

Ďalšie informácie o možnostiach generovania sietí v expertnom režime nájdete v dokumentácii k [13.2. 3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/) a [13.3. 3D Brick Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/)

**Materiál**  
Na obr. 29.2.20. je zobrazené okno s materiálmi. Používateľ môže priradiť požadovaný materiál zo zoznamu alebo ho importovať zo súboru či knižnice. Používateľ môže tiež pridať nový materiál. Ďalšie informácie o tom, ako priradiť materiál, nájdete v kapitole [10\. Material Data](/docs/en/pre_processor/10_material_data/10_material_data/).

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image029.jpg' | relative_url }})

Okno s materiálmi

Po pridaní materiálu kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) – otvorí sa okno s materiálom, ako je znázornené na obr. 29.2.21.

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image030.jpg' | relative_url }})

Okno na úpravu materiálu

Požadované vlastnosti závisia od fyzikálnych javov, ktoré sa simulujú v programe DEFORM. Vlastnosti materiálu, ktoré musí používateľ zadať, závisia od typov materiálov, ktoré používateľ v simulácii využíva. Ďalšie informácie nájdete v časti „Materiál“ v nastaveniach programu Forming 3D.

**Okrajové podmienky**  
V okne „Okrajové podmienky“ môže používateľ priradiť objektu rôzne okrajové obmedzenia. Okrajové podmienky určujú, ako okraj objektu interaguje s ostatnými objektmi a s okolím. Najčastejšie používanými okrajovými podmienkami v programe Cogging sú výmena tepla s prostredím pri simuláciách zahŕňajúcich prenos tepla (pozri obr. 29.2.22..) a predpísaná rýchlosť na vynútenie symetrie (pozri obr. 29.2.23.), ktoré znázorňujú rôzne okrajové podmienky (BCC), ktoré je možné priradiť k objektu.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image012.jpg' | relative_url }})

Okno „Okrajové podmienky“

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image013.jpg' | relative_url }})

Priradená rotačná symetria BCC

BCC sú rozdelené do kategórií [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/), [Thermal](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/), [Diffusion](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/) a [Heating](/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/). Ďalšie informácie o týchto BCC nájdete v [14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/).

**Nehnuteľnosť**  
Rôzne parametre objektu, ktoré ovplyvňujú buď termomechanické správanie objektu, alebo správanie numerického riešenia, sa zadávajú v okne „Object-Properties“ (pozri obr. 29.2.24.). Ďalšie informácie o týchto možnostiach nájdete v [19\. Object properties.](/docs/en/pre_processor/10_material_data/10_material_data/)

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image032.jpg' | relative_url }})

Okno vlastností objektu

## Horná matrica

V tomto okne môže používateľ nastaviť požadovanú teplotu objektu a vybrať typ objektu, ako je znázornené na obr. 29.2.25. V prípade hornej formy je štandardne vybraný typ objektu „Rigid“ a používateľ môže tiež importovať objekt z iných databáz alebo súborov kľúčov pomocou tlačidla a vyhľadania príslušného súboru.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image014.jpg' | relative_url }})

Okienko „Top Die“

**Geometria**  
Okno „Geometria“ slúži na vytvorenie geometrie objektu, ako je znázornené na obr. 29.2.26. Ak ešte nebola vytvorená žiadna geometria, aktívne bude iba pole „Definovať primitívy“, ostatné možnosti budú sivé. Po vytvorení geometrie budú všetky možnosti aktívne.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image015.jpg' | relative_url }})

Okno Geometria

**Definícia primitívu**

Na obr. 29.2.27 je znázornená geometrická primitívna forma „Die“. K dispozícii je iba primitívna forma s rovnými plochami, avšak používateľ môže pomocou tlačidla importovať súbory (STL, GEO, PDA, NAS a UNV) a formy s profilmi, ktoré sa bežne používajú pri lisovaní.

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image035.jpg' | relative_url }})

Okno „Top Die Geometry Primitive“

Ďalšie informácie o možnostiach geometrie nájdete v [12\. 3. 3D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/)

**Sieťovina**  
Možnosti vytvárania sietí pre lisovacie formy sú podobné ako v prípade polotovaru; ďalšie informácie o vytváraní sietí nájdete v dokumente [Top Die Mesh](29_1_cogging_setup.htm#Top_Die_Mesh).

**Materiál**  
Priradenie materiálu k formám prebieha podobne ako v prípade sochoru. Používateľ môže vybrať požadovaný materiál zo zoznamu alebo ho importovať zo súboru či knižnice. Používateľ môže tiež pridať nový materiál. 

Vlastnosti materiálov, ktoré musí používateľ špecifikovať, závisia od typov materiálov, ktoré používateľ využíva v simulácii. V tejto časti sú popísané údaje o materiáloch, ktoré je možné špecifikovať pre simuláciu DEFORM. Ďalšie informácie nájdete v časti „Materiál“ v nastaveniach programu Forming 3D.

**Ovládanie pohybu**  
V závislosti od požiadaviek procesu a použitého zariadenia môže používateľ definovať nastavenia riadenia pohybu pre lisovacie matrice. Pre rýchle nastavenie lisovania sa použijú ovládacie prvky pohybu [Speed](/docs/en/pre_processor/15_movement_controls_definition/15_1_speed/) a [Mechanical press](/docs/en/pre_processor/15_movement_controls_definition/15_5_mechanical_press/), ako je znázornené na obr. 29.2.28. Ak chce používateľ definovať iné nastavenia riadenia pohybu ako tieto, môže použiť pokročilé rádio tlačidlo kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_movement_button.jpg' | relative_url }}); k týmto možnostiam sa dá dostať aj prepnutím do režimu Expert, ako je znázornené na obr. 29.2.29. Ďalšie informácie o týchto nastaveniach riadenia pohybu nájdete v časti [15\. Movement Controls Definition](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/).

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image036.jpg' | relative_url }})

Okno s ovládacími prvkami pohybu v režime s navádzaním

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image037.jpg' | relative_url }})

Okno s ovládacími prvkami pohybu v režime pre pokročilých

## Polohovanie

Na obrázku 29.2.30. je zobrazené okno na nastavenie polohy.

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image041.jpg' | relative_url }})

Okno ovládacích prvkov

Polohovanie matíc a manipulátorov je v sprievodcovi lisovaním riadené automaticky systémom a používateľ potrebuje tieto možnosti polohovania len zriedka, a to v prípadoch, keď sú matice importované z externého zdroja. Na polohovanie by stačilo nastaviť polohu hornej matrice, keďže šablóna automaticky kopíruje túto polohu aj pre ostatné matrice. V novom nastavení je na polohovanie viditeľná len horná matrica a hoci sa ostatné matrice počas úpravy nastavenia polohujú ručne, ich polohy sa neukladajú – ukladá sa len poloha hornej matrice, ktorá sa premietne aj na ostatné matrice. Ďalšie informácie o týchto možnostiach polohovania nájdete v nasledujúcich častiach.

  * **Automatické polohovanie ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }})**

Kliknutím na toto tlačidlo systém automaticky umiestni objekty vzhľadom na smer pohybu hornej matrice; táto možnosť sa najlepšie hodí pre jednoduché nastavenie s tromi objektmi: obrobkom, hornou matricou a spodnou matricou.

  * **Umiestňovanie objektov ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }})**

Kliknutím na toto tlačidlo môže používateľ umiestniť objekty do požadovaných smerov. K dispozícii sú rôzne typy možností umiestňovania, ako napríklad ťahanie, posun, kolízia, zrkadlenie a otáčanie, ako je znázornené na obr. 29.2.31. Ďalšie informácie o týchto možnostiach nájdete v [16.Object Positioning.](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/)

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image042.jpg' | relative_url }})

Okno na umiestňovanie objektov

## Plánované polohovanie

Funkcia „Schedule positioning“ umožňuje používateľovi definovať umiestnenie objektov v nastavení MO pre nasledujúce operácie, pre ktoré sa nevytvára databáza (DB), tak, aby boli objekty umiestnené ešte pred vytvorením DB počas spustenia simulácie v dávkovom režime. Táto možnosť sa zriedka používa aj v procese coggingu.

## Kontakt

Účelom vzťahov medzi objektmi je definovať, ako rôzne objekty v simulácii vzájomne interagujú. Tabuľka vzťahov zobrazuje aktuálne vzťahy medzi objektmi, ktoré boli definované, ako je znázornené na obr. 29.1.32. Všetky objekty, ktoré môžu prísť do kontaktu v priebehu simulácie, musia mať definovaný kontaktný vzťah. To zahŕňa aj objekt, ktorý má vzťah sám so sebou, ak dochádza k vlastnému kontaktu, ako je to v prípade prekrývania. Správne definovanie týchto vzťahov je veľmi dôležité, aby simulácia presne modelovala proces tvárnenia.

**Systém**: Po výbere tohto prepínača systém priradí predvolené vzťahy medzi objektmi. V prípade potreby môže používateľ pridať mazivá výberom možnosti „Pridať nové“ z roletového menu a kliknutím na tlačidlo „Upraviť“, alebo môže na účely simulácie načítať požadované mazivá z knižnice.

V režime Cogging je štandardne zvolená možnosť **User**; ak si používateľ**** želá definovať vlastné vzťahy, mal by zvoliť príslušné rádio tlačidlo. Používateľ môže pridať vzťahy kliknutím na tlačidlo Pridať, ako je znázornené na obr. 29.2.33.

  
Koeficienty trenia a prenosu tepla je možné nastaviť dokonca priamo z okna ovládacích prvkov simulácie, 

Ďalšie informácie nájdete v časti „Vzťahy medzi objektmi pri vytváraní 3D nastavenia“.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image016.jpg' | relative_url }})

Okno definície objektov Inter v režime Systém

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image044.jpg' | relative_url }})

Okno definície medzi objektmi v užívateľskom režime

Ďalšie informácie nájdete v dokumente [20.Inter-Object Relations](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

## Ukážka simulácie

Náhľad simulácie poskytuje prehľad operácií, ako sú deformácia, výdrž, opätovné zahriatie atď., ktoré sa majú vykonať na základe definície procesu a tabuľky priechodov vo forme animácie. Ponúka tiež náhľad nastavenia pri každej operácii. V okne „Simulation Preview“ (Náhľad simulácie) sa kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_preview_play_button.jpg' | relative_url }}) spustí prehrávanie animácie (pozri obr. 29.2.34 a obr. 29.2.35).

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image017.jpg' | relative_url }})

Okno „Náhľad simulácie“ v prvom kroku

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image018.jpg' | relative_url }})

Okno „Náhľad simulácie“ v programe Bite

## Ovládacie prvky simulácie

Systém DEFORM rieši časovo závislé nelineárne úlohy generovaním série riešení metódou konečných prvkov (FEM) v diskrétnych časových krokoch. V každom časovom kroku sa rýchlosti, teploty a ďalšie kľúčové premenné každého uzla v sieti konečných prvkov určujú na základe okrajových podmienok, termomechanických vlastností materiálov obrobku a prípadne riešení z predchádzajúcich krokov. Ostatné stavové premenné sa odvodzujú z týchto kľúčových hodnôt a aktualizujú sa pri každom časovom kroku. Dĺžka tohto časového kroku a počet simulovaných krokov sa určujú na základe informácií zadaných v ponuke ovládacích prvkov krokov. Obr. 29.2.36. Ukazuje možnosti riadenia simulácie v režime „Guided“ (Vedený) pri operácii lisovania; tu sú k dispozícii základné možnosti potrebné pre operáciu tvárnenia, zatiaľ čo režim „Expert“ (Odborný) ponúka podrobnejšie možnosti.

V režime s návodom môže používateľ nezávisle definovať parametre simulácie pre operácie deformácie a prenosu tepla. Systém na základe týchto informácií vygeneruje súbor .MST a príslušné parametre simulácie uplatní na všetky operácie, ktoré sa majú vykonať. Tu je možné definovať aj koeficienty trenia a prenosu tepla.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image019.jpg' | relative_url }})

Okno ovládacích prvkov simulácie v režime s návodom

**Deformácia:**  
Počet simulačných krokov (NSTEP)  
Parameter „Počet simulačných krokov“ určuje počet krokov, ktoré sa majú vykonať od počiatočného čísla kroku alebo predchádzajúcej operácie. Simulácia sa zastaví po vykonaní tohto počtu simulačných krokov, pokiaľ sa nespustí príkaz na zastavenie simulácie alebo ak simulácia nenarazí na problém. Toto nastavenie je možné nastaviť samostatne pre operácie deformácie a prenosu tepla.

**Krok pri ukladaní**  
Krok prírastku (STPINC), ktorý sa má uložiť do databázy, určuje počet krokov, ktoré systém uloží do databázy. Pri spustení simulácie sa musí vypočítať každý krok, ale nemusí sa nutne uložiť do databázy. Uloženie väčšieho počtu krokov zachová viac informácií o procese, čo však bude vyžadovať viac úložného priestoru. Keďže operácia Cogging je zdĺhavý proces, používateľ by mal byť pri definovaní tejto hodnoty opatrný, aby bolo možné kontrolovať veľkosť súboru .DB. Toto nastavenie je možné nastaviť nezávisle pre operácie deformácie a prenosu tepla.

**Koeficient trenia**

Pomocou tejto možnosti sa nastavuje koeficient trenia medzi maticami a polotovarom a medzi trnom a polotovarom.

**Definícia kroku (DSMAX/DTMAX)**  
Veľkosť kroku riešenia je možné riadiť časovým krokom alebo posunom primárnej matrice. Ak je špecifikovaný zdvih na krok, primárna matrica sa v každom časovom kroku posunie o zadanú hodnotu. Celkový pohyb primárnej matrice bude rovný posuvu na krok vynásobenému celkovým počtom krokov. Ak je špecifikovaný čas na krok, použije sa časový interval na krok. Posuv matrice na krok bude rovný časovému kroku vynásobenému rýchlosťou matrice. V predvolenom nastavení v režime Cogging je ako primárna matrica definovaná horná matrica.

Definícia riadenia krokového prírastku bola rozšírená tak, aby zahŕňala krokové funkcie závislé od času aj od zdvihu; tieto možnosti sú k dispozícii v režime Expert. To znamená, že veľkosť kroku (či už ide o čas na krok alebo zdvih na krok) je teraz možné definovať ako funkciu času alebo zdvihu. Táto funkcia umožňuje jemnejšie rozlíšenie uložených informácií o modeli tam, kde je to žiaduce. (typicky na konci zdvihu, kde môže dochádzať k prudkým zmenám zaťaženia matrice)

**Prenos tepla:**  
**Matrice s koeficientom HT**

Tu je uvedený koeficient prenosu tepla medzi lisovacími maticami a sochárom, ktorý platí pre všetky operácie.

**Manipulátory koeficientov HT**

Tu je uvedený koeficient prenosu tepla medzi manipulátormi a sochou, ktorý platí pre všetky operácie. Pri lisovaní sa nepoužíva, keďže pri ňom sa používajú manipulátory na zubovanie.

****

**Metóda riešiteľa**

Používateľ má možnosť zvoliť si, či sa má použiť implicitný riešiteľ alebo explicitný riešiteľ.

**Implicitné:**

Použitie RSE: Funkciu RSE je možné aktivovať zaškrtnutím tohto políčka. Ďalšie informácie o RSE nájdete v časti RSE[MO] v dokumente [16.Object properties.](/docs/en/pre_processor/16_object_properties/16_object_properties/).

**Medzná rýchlosť deformácie**: Medzná rýchlosť deformácie (LMTSTR) definuje medznú hodnotu efektívnej rýchlosti deformácie, pod ktorou sa plastický alebo porézny materiál považuje za tuhý a správa sa ako materiál podobný newtonovskej kvapaline.

  
**Implicitný kontakt**: Zaškrtnutím tohto políčka môžete aktivovať metódu implicitného kontaktu medzi objektmi.

**Ovládacie prvky simulácie v režime Expert**

Na obr. 29.2.37 sú zobrazené ovládacie prvky simulácie v režime Expert. Ďalšie informácie a popis možností v ovládacích prvkoch simulácie nájdete v [9\. Simulation Controls.](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/).

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image047.jpg' | relative_url }})

Ovládacie prvky simulácie v režime pre pokročilých

## Vytvoriť databázu

****

**Skontrolujte Data![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})**

Systém skontroluje údaje. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvoriť databázu ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})**

Kliknutím na toto tlačidlo sa vygeneruje databáza nastavení potrebná na spustenie simulácie. (Pozri obr. 29.2.38.)

**Pridať súbor s kľúčmi**

Akékoľvek informácie, ktoré nie sú definované v sprievodcovi, ale napriek tomu sa vzťahujú na daný proces, je možné načítať ako súbor s príponou .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt – tieto hodnoty je možné definovať v súbore s príponou .key, následne stačí zmeniť len tento súbor a simuláciu je možné odoslať znovu.

![]({{ '/assets/images/operation_templates/29_cogging/29_1_cogging_setup/image048.jpg' | relative_url }})

Okno „Vytvoriť databázu“

## Spustenie simulácie

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Simuláciu spustite kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) a výberom možnosti „spustiť od posledného záporného kroku“ v rozbaľovacom okne „Spustiť simuláciu“.

  
Priebeh simulácie môžete sledovať v okne „Simulation graphics“ a na kartách „Simulation Message“ a „Simulation Log“. Uistite sa, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) (pozri obr. 29.2.39.), aby sa súbory správ a protokolov automaticky aktualizovali a umožnili tak sledovanie priebehu simulácie. Pomocou možností na paneli nástrojov „Simulačná grafika“ je možné počas simulácie problému vykresľovať základné stavové premenné objektov, ako sú teplota, deformácia a kontakt.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image020.jpg' | relative_url }})

Simulačný režim

Pri simulácii lisovania sa všetky simulačné údaje o lisovaní počas behu ukladajú do súboru ProblemID.MST. Súbor ProblemID.MST umožňuje postupné vykonávanie simulácie lisovania, pričom každá operácia deformácie a prenosu tepla prebieha ako samostatná operácia na základe nastavení v okne procesu a tabuľke priechodov. Súbor ProblemID.MST riadi spustenie a zastavenie každej operácie. Pre všetky operácie sa správy o spustení a zastavení zobrazujú v súbore správ. Po dokončení všetkých operácií sa v súbore simulačného protokolu zobrazí správa „MULTIPLE OPERATION COMPLETED“ (Viacnásobná operácia dokončená).

## Následné spracovanie

Po dokončení simulácie si môže používateľ prezrieť výsledky tak, že pomocou tlačidla nad panelom nástrojov Simulácia prepne do režimu Post. (Pozri obr. 29.2.41)

Používateľ môže postupovať podľa jednotlivých krokov a znázorniť rozdelenie rôznych stavových premenných výberom ikon skratiek pre hlavné stavové premenné alebo pomocou ikony (Nastavenie stavových premenných) pre všetky stavové premenné, ako je znázornené na obr. 29.2.41.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image021.jpg' | relative_url }})

Prerez obrobku

K dispozícii sú aj ďalšie nástroje na spracovanie výsledkov, ako napríklad súhrnný graf minimálnych a maximálnych kriviek stavových premenných, grafy zaťaženia a zdvihu matrice, sledovanie bodov stavových premenných počas celej simulácie, analýza toku zŕn pomocou programu Flownet, zrkadlenie symetrických objektov, rozrezávanie objektov a vytváranie animačných súborov s výsledkami.

Na obr. 29.2.40 je obrobok so štvrtinovou symetriou, ako je znázornené na obr. 29.2.41, zrkadlovo otočený okolo osi, aby sa získal celkový pohľad na objekt.

![]({{ '/assets/images/operation_templates/29_cogging/29_2_swaging_setup/image022.jpg' | relative_url }})

Hrúbka prierezu obrobku

**Súvisiace témy:**

[29.1. Cogging Setup](/docs/en/operation_templates/29_cogging/29_1_cogging_setup/)

[Cogging Lab](/docs/en/labs/cogging_labs/cogging_lab1/)

[6.1. Integrated Manufacturing Process Pre- Processor Layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

[6.2. Integrated Manufacturing Process.Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Proces Post - Processor layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)
