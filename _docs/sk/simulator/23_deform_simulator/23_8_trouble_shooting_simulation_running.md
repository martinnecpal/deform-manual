---
lang: sk
title: "23.8. Riešenie problémov pri spúšťaní simulácie"
---

# 23.8. Riešenie problémov pri spúšťaní simulácie

23.8.1. Správy v súbore správ

23.8.2. Simulácia prerušená v dôsledku chyby používateľa alebo chýb súvisiacich s licenciou

23.8.3. Pri zápornom kroku nie je možné vykonať prečlenenie siete

23.8.4. Dôrazne odporúčame prepočítať sieť

23.8.5. Negatívna jacobiánova matica

23.8.6. Riešenie nekonverguje

23.8.7. Matica tuhosti je negatívne definitná

23.8.8. Nulový otočný bod

23.8.9. Extrapolácia údajov

23.8.10. Nesprávny tvar prvku

23.8.11. Nezhodné číslo kroku

23.8.12. Prekročenie limitu systémovej pamäte

Súbor správ obsahuje podrobný záznam simulácie po jednotlivých iteráciách. Ukazuje, do akej miery sa každá iterácia približuje ku konečnému riešeniu, a to výpočtom normy relatívnej chyby medzi po sebe idúcimi krokmi, a to tak pre uzlové rýchlosti, ako aj pre uzlové sily. Sú tu tiež uvedené informácie o vytváraní kontaktov medzi uzlami a tiež o prípadnom náhlom zastavení. Protokolový súbor je záznamom o vykonávaní modulu.

## Správy v súbore správ

Ak sa simulácia predčasne zastaví, odporúča sa skontrolovať koniec súboru so správami, aby ste zistili, prečo sa simulácia zastavila. Keďže simulácia prebieha v dávkovom režime, existujú tri miesta, kde môže byť uvedené ukončenie operácie. V súbore správ simulácia označí normálne ukončenie modulu FEM. Ak dôjde k abnormálnemu ukončeniu simulácie v dôsledku neplatnej operácie v module FEM alebo pri generovaní siete, bude to uvedené buď v súbore .LOG, alebo v príkazovom okne, kde bol program DEFORM pôvodne spustený. Toto môže byť sprevádzané aj súborom core, ktorý by sa mal čo najskôr odstrániť, keďže tieto súbory často zaberajú veľké množstvo miesta na disku.

## Simulácia bola prerušená v dôsledku chyby používateľa alebo chýb súvisiacich s licenciou.

Nasledujúce informácie platia iba pre verzie DEFORM2D v9.1 alebo DEFORM3D v6.1, resp. pri prevádzke týchto produktov s použitím správcu licencií vydaného spolu s DEFORM v10.0.

Po inštalácii programu DEFORM je potrebné nastaviť oprávnenia pre súbor stavu (ktorý monitoruje simulácie bežiace na počítači) pomocou príkazu „chmod 777 DEFORM.STA“. Ak sa tak nestane, modul FEM nebude môcť zapisovať do súboru stavu a následne sa ukončí. Ak chcete simuláciu spustiť znova, najskôr prejdite do adresára DEFORM_DIR, spustite program INSTALL3D a vyberte možnosť na opätovné vytvorenie súboru so stavom.

Poznámka:

Ak sa používateľovi zobrazí správa „Príkaz nebol nájdený“, mal by spustiť program INSTALL3D zadaním príkazu ./INSTALL3D. Týmto krokom donúti operačný systém ignorovať nastavené cesty a spustiť iba súbor nachádzajúci sa v aktuálnom adresári.

Ak pri používaní programu DEFORM s novým Správcom licencií dôjde k zastaveniu programu a zobrazí sa nasledujúca správa alebo vyskakovacie okno, možné príčiny pri spustení Správcu licencií a programu DEFORM na tom istom počítači sú: Program LManagerServer.exe prestal fungovať, nespustil sa po reštarte systému, hardvérový kľúč bol odstránený počas behu programu DEFORM alebo sa používa nesprávna kombinácia hardvérového kľúča a súboru s heslom.

Ak sa program License Manager a DEFORM spúšťajú na rôznych počítačoch, okrem vyššie uvedených dôvodov môže dôjsť aj k prerušeniu sieťového pripojenia medzi licenčným serverom a klientskym počítačom, na ktorom beží DEFORM. Na obr. 23.8.1 je zobrazená chybová správa, ktorá sa v tomto prípade zobrazí.

![]({{ '/assets/images/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/image001.jpg' | relative_url }})

Chyba licenčného servera

## Pri zápornom kroku nie je možné vykonať prepočítanie siete

FEM engine vypíše túto správu a ukončí činnosť, ak práve prebehlo premeshovanie a v aktuálnom kroku sa vyskytne záporná jacobiánska matica, čo si vyžaduje opätovné premeshovanie. K tejto situácii zvyčajne dochádza v prípade, že premeshovanie nevytvorilo platnú sieť. Zastavenie simulácie zabráni tomu, aby sa systém DEFORM dostal do nekonečnej slučky.

Dôvodom môže byť to, že časový krok (DSMAX, DTMAX) môže byť veľký, ako sa to môže stať pri extrudovaní, kde rýchlosť piestu môže byť nízka, ale rýchlosť extrudátu môže byť veľmi vysoká, čo spôsobuje výrazné deformácie siete v blízkosti polomeru matrice. Ďalším príkladom je kovanie, keď sa materiál začne rozlievať a prvky v blízkosti oblasti rozliatia sa výrazne deformujú. Na zabránenie tomuto problému je možné znížiť časový krok, zvýšiť počet prvkov siete alebo zvýšiť hustotu siete v oblasti, kde dochádza k deformácii.

Môže byť užitočné znázorniť rýchlosti uzlov v [Preprocessor](/docs/en/pre_processor/7_introduction_to_pre-processor/). Neodporúča sa, aby posun uzlov v každom [ time step](/docs/en/pre_processor/9_simulation_controls/9_2_defining_step/) bol väčší ako dĺžka hrany prvkov. V tomto prípade môže byť užitočné [Polygon edge length substepping](../../pre_processor/9_simulation_controls/9_2_defining_step.htm#Polygon_length_sub_step_\(DPLEN\).

## Dôrazne odporúčame prepočítať sieť

  
Správa „Dôrazne sa odporúča prepočítať sieť kvôli nevyváženému nesúladu medzi hlavným a podriadeným objektom“ sa zobrazí v prípade, že veľkosť prvkov na povrchu podriadeného a hlavného objektu nie je správna. Pri definovaní vzťahov medzi objektmi typu „hlavný – podriadený“ je potrebné dodržiavať nasledujúce pravidlá:

  * podložka je z mäkšieho materiálu

  * podriadená sieť by mala mať jemnejšie/hustejšie oká ako hlavná sieť

Táto sieť je veľmi dôležitá v oblasti, kde sa master a slave navzájom dotýkajú. Ak je sieť na masteri v oblasti ich styku oveľa hustejšia ako sieť na slave, výsledky simulácie nebudú presné. Ak je pomer počtu prvkov na kontaktnej ploche medzi hlavným a podriadeným objektom väčší ako 3:1, v súbore správ sa ako varovanie zobrazí správa „Vzhľadom na nevyvážený nesúlad medzi hlavným a podriadeným objektom sa dôrazne odporúča prečlenenie siete“. Toto zníži presnosť riešenia a používateľ by mal podniknúť kroky na zmenu nastavenia [mesh densities](/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/) na objektoch.

## Negatívna jacobiánska matica

  
Program DEFORM využíva metódu konečných prvkov na riešenie úloh s veľkými deformáciami a nástroj AMG (Automatic Mesh Generator) na automatické vytvorenie optimalizovanej siete. Vo väčšine prípadov prebieha vytváranie a premenovanie siete veľmi plynulo. Existujú však prípady, keď simulácia nepokračuje kvôli zápornému Jacobianovmu maticu (neprijateľná sieť) v kroku bezprostredne po operácii premenovania siete. Vo väčšine prípadov je možné tieto prípady ľahko identifikovať na základe jednej z nasledujúcich oblastí:

K tomuto problému zvyčajne vedie uzavretý prekrývajúci sa okraj. Pozorne si prezrite priebeh simulácie a skontrolujte, či sa niekde nevytvorila malá oblasť, kde sa prekrývajúci sa okraj uzavrel. Ak takýto prekrývajúci sa okraj zistíte a chcete v simulácii pokračovať, môžete skúsiť:

  * Môže byť užitočné použiť funkciu „Surface Patch“ v nástroji [Preprocessor](/docs/en/pre_processor/7_introduction_to_pre-processor/) v časti „Objects Geometry“. Zlomy sa zobrazia ako krátke červené čiary, ktoré nevyzerajú tak, že by zvýrazňovali jediný prvok. Predtým, ako rozhodnete, že červená značka predstavuje ohyb, nezabudnite si objekt prezrieť z viacerých uhlov, pretože povrchové oblasti na zadnej strane objektu môžu byť zavádzajúce. Upravte geometriu tak, aby ste odstránili prekrývanie, a pokračujte v simulácii. To si vyžiada vytvorenie novej siete a interpoláciu, aby sa zachovala história deformácie, teploty a poškodenia.

  * Ak z akéhokoľvek dôvodu uzol prenikol do jednej z foriem, vytvorenie novej siete bude problematické. Túto situáciu je možné posúdiť kontrolou siete FEM všetkých objektov v kroku bezprostredne pred vytvorením novej siete. Uzol, ktorý sa nachádza vnútri povrchu formy, sa po vytvorení novej siete a interpolácii okrajových podmienok vráti späť na povrch formy, avšak prvok, ktorý mal pôvodne prijateľnú geometriu, sa môže počas tohto procesu výrazne zdeformovať.

  * Ak používateľ nastaví úlohu s veľmi veľkými časovými krokmi a s malou alebo žiadnou hodnotou [substepping criteria](../../pre_processor/9_simulation_controls/9_2_defining_step.htm#Sub-stepping_Controls), môže to viesť k problému spôsobenému výrazným deformovaním siete počas prvého kroku. Pozrite si [time step definition criteria](../../pre_processor/9_simulation_controls/9_2_defining_step.htm#9.2.2.Step_Increment) v časti [Preprocessor](/docs/en/pre_processor/7_introduction_to_pre-processor/) tejto príručky.

  * Ak je v 3D simulácii vypnuté subkrokovanie, je potrebné venovať veľkú pozornosť tomu, aby sa používali dostatočne malé časové kroky. To znamená, že vždy, keď posun uzla vypočíta polohu uzla vnútri tuhého objektu, uzol sa vráti späť na povrch formy. Ak sú posuny uzlov malé, nie je to zlý predpoklad, avšak ak sú posuny uzlov veľké, tento predpoklad môže stratiť platnosť.

Tieto návrhy slúžia ako všeobecné usmernenia a nemusia vyriešiť všetky problémy tohto druhu. Ak ste už preskúmali všetky tieto oblasti a následné pokusy o spustenie vášho problému zlyhali, odporúčame nám zaslať súbor s kľúčovými slovami na ďalšie preskúmanie.

## Riešenie nekonverguje

  
Existuje niekoľko bežných dôvodov, prečo riešenie nekonverguje.

  1. Materiál vykazuje pohyb veľkého tuhého telesa. Veľká časť deformujúceho sa telesa má veľmi nízku rýchlosť deformácie alebo je tuhá.

  2. Materiál nie je citlivý na rýchlosť deformácie.

  3. Elastoplastický materiál prechádza veľkou deformáciou alebo má nevhodnú počiatočnú hodnotu.

V prípadoch, keď sa problém nedá vyriešiť, by vám pri hľadaní príčiny mal pomôcť nasledujúci kontrolný zoznam. Pomôže vám to pri najbežnejších prípadoch.

  * Zvýšte hodnotu [ Force Norm or Velocity Norm](../../pre_processor/9_simulation_controls/9_5_solver_settings.htm#Convergence_error_limits_\(CVGERR\)) až o jeden rád. Hodnota Force Norm môže byť v skutočnosti zvýšená až na 0,1 alebo dokonca na niekoľko krokov úplne eliminovaná. To by nemalo viesť k významnej chybe, ale mohlo by to mať za následok zníženú presnosť výpočtov zaťaženia. Ak sa konvergencia zlepší, nechajte simuláciu bežať 3 alebo 4 kroky, potom skúste nastavenia znížiť na pôvodné hodnoty.

  * Ak sa simulácia vykonáva s hlavným [die movement](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/) v režime regulácie zaťaženia alebo energie, vykonajte niekoľko krokov v režime regulácie otáčok, aby sa riešenie mohlo stabilizovať, a až potom pokračujte v pôvodnom režime.

  * Zvýšte hodnotu [limiting strain rate](../../pre_processor/16_object_properties/16_1_deformation_properties.htm#16_1_6_Limiting_strain_rate_\(LMTSTR\) na 1/50 alebo 1/100 priemernej rýchlosti deformácie. To by nemalo mať žiadny významný vplyv na presnosť riešenia. Ak máte extrémne náročný prípad, pri ktorom je ťažké dosiahnuť konvergenciu, túto hodnotu môžete na niekoľko krokov znížiť na 1/10 priemernej rýchlosti deformácie a potom ju vrátiť na bežnejšiu hodnotu. V priebehu rokov sme odporúčali, aby limitná rýchlosť deformácie bola v rozmedzí 1/100 až 1/1000 priemernej rýchlosti deformácie. Ak je táto hodnota nastavená príliš nízko, bude to mať za následok umelo nižší výpočet zaťaženia.

  * Porovnajte svoje nastavenia [material data](/docs/en/pre_processor/10_material_data/10_material_data/) s podmienkami vášho procesu, aby ste sa uistili, že sa do FEM modulu neprenášajú žiadne „nezvyčajné“ vlastnosti materiálu. Venujte osobitnú pozornosť problémom s extrapoláciou. Ak sa napríklad vaše procesné podmienky nachádzajú v oblasti mimo definovanej oblasti tokového napätia, táto „citlivosť na reverznú rýchlosť deformácie“ spôsobuje problém (pozri obr. 23.8.2.), ktorý takmer znemožňuje, aby program DEFORM konvergoval k presnému riešeniu. Tento problém je možné vyriešiť opätovným vyhodnotením surových údajov a ich úpravou podľa potreby. Keďže je vysoko nepravdepodobné, aby materiál mal nižšie tečenie pri vyššej rýchlosti deformácie, bežnou príčinou tohto typu údajov je chýbajúca korekcia adiabatického ohrevu. Inými slovami, adiabatické zahrievanie pri vyšších rýchlostiach deformácie umelo zahrialo a zmäkčilo materiál, čo spôsobilo zdanlivo nižšie tečenie. Ak nie je možné určiť jasnú príčinu, nájdite údaje, ktoré nevykazujú túto citlivosť na opačnú rýchlosť deformácie.

![]({{ '/assets/images/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/image002.jpg' | relative_url }})

Extrapolácia prietokového napätia vedúca k inverznej rýchlosti deformácie

  * Znížte počet plastových objektov ([penalty constant](../../pre_processor/16_object_properties/16_1_deformation_properties.htm#16_1_4_Volume_penalty_constant_\(PENVOL\)) na hodnotu 250 000 až 500 000 pomocou konštantnej hodnoty ([PENVOL](/docs/en/keyword_documentation/p/penvol/)). Ak je táto hodnota v prípade bežných konštrukčných materiálov výrazne nižšia ako 100 000, môže to viesť k strate objemu.

  * Zmenšite časový krok. Táto rada platí najmä pre elasticko-plastické materiály. Veľmi malý časový krok často umožňuje systému DEFORM prekonať náročnú oblasť konvergencie. Až keď sa veľký počet uzlov dostane do kontaktu s formami a simulácia bude v plnom prúde, je možné opäť prejsť na väčší časový krok. Toho možno dosiahnuť buď reguláciou časového kroku, alebo pomocou modifikátora, ktorý vedie k subkrokovaniu, napríklad [DEMAX](/docs/en/keyword_documentation/d/demax/).

  * Zmeňte metódu výpočtu počiatočného odhadu. Informácie o počiatočnom odhade EP nájdete v dokumente [Object Properties](/docs/en/pre_processor/16_object_properties/16_object_properties/).

  * V prípade studených materiálov, ktoré vykazujú malú alebo žiadnu citlivosť na rýchlosť deformácie, ide o jeden z najnáročnejších prípadov na dosiahnutie konvergencie. V skutočnosti by mala existovať aspoň veľmi malá citlivosť na rýchlosť deformácie aj v oblasti studenej kovania. Používateľ môže konvergenciu podporiť vytvorením umelej citlivosti na rýchlosť deformácie. To nie je ďaleko od reality a dá sa to dosiahnuť pridaním súboru údajov o tečivom napätí pri vyššej rýchlosti deformácie s mierne vyššími hodnotami tečivého napätia. Pozrite si obr. 23.8.3., kde nájdete predstavu o tom, ako riešiť tento typ problému.

  * V niektorých prípadoch môžu byť problémy s konvergenciou spôsobené hrubou sieťou v oblasti s vysokou lokálnou deformáciou, napríklad pod rohom razníka počas operácie prepichovania. V takýchto prípadoch je potrebné vygenerovať jemnejšiu sieť a nastaviť kritériá pregenerovania siete tak, aby kládli väčší dôraz na zakrivenie hraníc a rýchlosť deformácie.

![]({{ '/assets/images/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/image003.jpg' | relative_url }})

Extrapolácia prietokového napätia vedúca k inverznej rýchlosti deformácie

  * V niektorých prípadoch môžu byť problémy s konvergenciou spôsobené hrubou sieťou v oblasti s vysokou lokálnou deformáciou, napríklad pod rohom razníka počas operácie prepichovania. V takýchto prípadoch je potrebné vytvoriť jemnejšiu sieť a nastaviť parameter [remeshing criteria](../../pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation.htm#13.2.8._Remeshing_criteria) tak, aby vykazoval väčší sklon k zohľadneniu zakrivenia hraníc a rýchlosti deformácie.

Tieto odporúčania slúžia ako všeobecné usmernenia a nemusia vyriešiť všetky problémy s nekonvergenciou. Hoci program DEFORM vykazuje pri väčšine úloh vynikajúcu konvergenciu, občas sa vyskytnú situácie, v ktorých môže používateľ naraziť na určité ťažkosti. Ak všetky tieto pokusy zlyhajú, odporúčame nám zaslať súbor s kľúčovými slovami na ďalšie preskúmanie.

## Matica tuhosti je negatívne definitná

Program DEFORM využíva metódu konečných prvkov na riešenie úloh plastickej deformácie, prenosu tepla a pružného priehybu. Pri použití tejto metódy sa matica tuhosti materiálu definuje na základe geometrie a vlastností materiálu. Ak sa používateľovi zobrazí správa „negatívne definovaná tuhosť“ alebo „nulový otočný bod“, je to spôsobené maticou tuhosti, ktorá má nulovú hodnotu. Tento problém je zvyčajne spôsobený vlastnosťou materiálu s nulovou hodnotou, ktorá súvisí s „tuhosťou“ alebo odporom voči tečeniu, teplu alebo deformácii.

Pri danom type simulácie existuje vlastnosť, ktorá s najväčšou pravdepodobnosťou vedie k tomuto problému. Je to nasledovné:

  * **Prenos tepla**: [Heat Capacity](../../pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data.htm#Heat_capacity) a/alebo T[hermal Conductivity.](../../pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data.htm#Thermal_conductivity)

  * **Elastic** : [Young's Modulus](../../pre_processor/10_material_data/10_2_elastic_data/10_2_elastic_data.htm#Young's_modulus).

  * **Plastická****deformácia**: [Flow Stress](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_flow_stress_models/).

  * Problémy s prenosom tepla je možné identifikovať na základe informácií v súbore správ. Informácie o iterácii budú obsahovať nadpis „Temperature Error Norm“ v časti bezprostredne pred ukončením daného problému.

  * Problémy s plastickou deformáciou je možné jasne identifikovať na základe informácií v súbore správ. Informácie o iteráciách budú obsahovať nadpisy „Force Error Norm“ a „Velocity Error Norm“ v časti bezprostredne pred ukončením výpočtu. Tieto správy sa zobrazia aj pri úlohách elastického typu (napätie v lisovacej forme).

## Nulový otočný bod

Pohyb tuhého telesa môže viesť k chybe „nulového otočného bodu“. To má za následok nárast normy rýchlosti a následné zlyhanie simulácie. Tento jav zvyčajne vyplýva z chýbajúcich adekvátnych okrajových podmienok a dá sa vyriešiť ich správnym definovaním. V prípade 2D simulácie existujú štyri možné geometrické režimy: [Axisymmetric](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Axisymmetric), [Plane Strain](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Plane_strain), [Plane Stress](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Plane_stress) a [Torsion](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Torsion). V prípade osovo symetrickej simulácie a simulácie krútenia je potrebné obmedziť iba smer y. V prípade simulácie rovinného deformovania a rovinného napätia je potrebné obmedziť smery x aj y pre objekty pokryté sieťou. V prípade tuhých objektov nie je potrebné žiadne obmedzenie, keďže fungujú skôr ako okrajové podmienky.

## Extrapolácia údajov

Mnohé z týchto problémov nie sú dôsledkom „nesprávnych údajov“ ani toho, že by používateľ zanedbal správne zadanie údajov. Problém súvisí s dátovým súborom, ktorý nepokrýva modelovaný proces. V takomto prípade sa dostupné údaje extrapolujú na procesné okno. V takomto prípade je potrebné materiál aktualizovať tak, aby zahŕňal údaje v skutočnom procesnom okne, alebo ho upraviť (najlepší odhad), aby sa zabezpečilo, že pri zahrnutí týchto kritických vlastností do rovníc tuhosti nemôžu nastať hodnoty na úrovni nuly alebo pod ňou. Ďalší popis nájdete na obr. 23.8.4.

![]({{ '/assets/images/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/image004.jpg' | relative_url }})

Automatická extrapolácia údajov o tepelnej kapacite

## Nesprávny tvar prvku

Ide o chybu vzniknutú v modulu FEM, ktorá upozorňuje na nebezpečné deformácie v sieti 3D simulácie. Dve hlavné príčiny tejto chyby sú: záporná jacobiánová matica, ktorú nie je možné vyriešiť, alebo chýbajúce hodnoty prietokového napätia. V prípade záporného jacobiánu budú problematické prvky (spolu so súradnicami uzlov týchto prvkov) uvedené v súbore BUG.MSG. Ak sú v zozname uvedené všetky prvky siete, pravdepodobne nebolo pre daný objekt definované prúdenie. Ak je uvedených len niekoľko prvkov, používateľ môže skúsiť načítať chybný krok do predspracovateľa a skontrolovať tvar prvkov a kód okrajových podmienok. Dôležitosť správne definovaných okrajových podmienok nemožno dostatočne zdôrazniť. Patrí sem aj zmysluplné kontaktné podmienky a podmienky s pevnou rýchlosťou.

## Nezhoda v čísle kroku

To znamená, že v čase spustenia alebo opätovného spustenia simulácie nie je najnovší krok v databáze záporný. V prípade programu DEFORM je záporná hodnota kroku iba indikátorom, ktorý signalizuje, že je možné simuláciu spustiť alebo opätovne spustiť. Záporná hodnota nemá žiadny algebraický význam, keďže ide iba o indikátor. Príčinou tejto chyby môže byť niektorá z nasledujúcich možností:

Bola odoslaná už spustená simulácia, na ktorej koniec je potrebné pridať záporný krok. Tento problém je možné vyriešiť jednoduchým opätovným vytvorením záporného kroku v súboroch [Pre-Processor](/docs/en/pre_processor/7_introduction_to_pre-processor/) a [submitting the simulation](/docs/en/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/).

Simulácia si vyžadovala prečlenenie siete a program [Pre-Processor](/docs/en/pre_processor/7_introduction_to_pre-processor/) nedokázal pred opätovným spustením simulácie vygenerovať záporný krok. Ak k tomu dôjde, skontrolujte prosím simuláciu a uistite sa, že pred touto chybou nedošlo k žiadnym problémom s programom [boundary conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/). Skontrolujte tiež, či je k dispozícii dostatok voľného miesta na disku a či máte v príslušnom adresári oprávnenia na zápis. Ak sa nepodarí zistiť príčinu, kontaktujte SFTC na adrese [support@deform.com](mailto:support@deform.com).

## Prekročenie limitu systémovej pamäte

Pri modeloch mimoriadne veľkých rozmerov sa môže používateľ stretnúť s problémom zastavenia FEM v dôsledku prekročenia limitu systémovej pamäte. V predvolenom nastavení sa riešič FEM teraz vo všetkých úlohách prepne z metódy CG na metódu SPARSE. Vo väčšine prípadov to prinesie skrátenie doby výpočtu. Riešiteľ SPARSE však spotrebúva viac systémovej pamäte ako riešiteľ CG. Preto môže byť 32-bitová alebo 64-bitová 3D FEM teraz náchylnejšia na zastavenie, ak je veľkosť modelu príliš veľká na to, aby sa zmestila do dostupnej systémovej pamäte. Obmedzenia pamäte uvalené na 32-bitové procesy môžu tiež spôsobiť zastavenie 32-bitovej 3D FEM kvôli veľkosti modelu. Pre 3D simulácie, najmä tie s veľkými modelmi, sa odporúča 64-bitová FEM. Používateľ môže aktivovať a ovládať prepínanie riešiteľa na stránke [Simulation Control - Control Files](/docs/en/pre_processor/9_simulation_controls/9_8_control_files/).

**Súvisiace témy:**

[2D Geometry types](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\])

[Step controls selection from Simulation controls](/docs/en/pre_processor/9_simulation_controls/9_2_defining_step/)

[Step increment controls](../../pre_processor/9_simulation_controls/9_2_defining_step.htm#Step_increment_control_\(DSMAX/DTMAX\))

[Velocity and Force error norms settings in Simulation controls](../../pre_processor/9_simulation_controls/9_5_solver_settings.htm#Convergence_error_limits_\(CVGERR\))

[Object types](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type)

[2D-remesh Criteria](../../pre_processor/13_mesh_generation/13_1_2d_mesh_generation.htm#13.1.8._Remeshing_criteria)

[3D-Remesh criteria](../../pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation.htm#13.2.8._Remeshing_criteria)

[Boundary conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[Inter-Object contact conditions](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[Material properties](/docs/en/pre_processor/10_material_data/10_material_data/)

[Object properties](/docs/en/pre_processor/16_object_properties/16_object_properties/)

[Limiting strain rate settings in Object properties](../../pre_processor/16_object_properties/16_1_deformation_properties.htm#16_1_6_Limiting_strain_rate_\(LMTSTR\))

[EP Initial guess](../../pre_processor/16_object_properties/16_1_deformation_properties.htm#16_1_2_Elasto-plastic_initial_guess_\(ELPSOL\))

[Submitting the problem to simulate](/docs/en/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/)
