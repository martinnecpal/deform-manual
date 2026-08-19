---
lang: sk
title: "48.2. Tvarovanie prúdom"
---

# 48.2. Tvarovanie prúdom 

48.2.1. Ako pridať operáciu tvarovania prúdom

48.2.2. Postup

48.2.3. Nastavenie simulácie

48.2.4. Výber objektov pre nastavenie

48.2.5. Stránka obrobku

48.2.5.1. Definovanie 2D priečneho rezu obrobku

48.2.5.2. Stránka „Mriežka obrobku“

48.2.5.3. Stránka s materiálmi

48.2.5.4. Definovanie BCC obrobku

48.2.6. Definovanie objektu „Mandrel“

48.2.6.1. Definovanie 2D priečneho rezu trnu

48.2.6.2. Vytvorenie 3D geometrie trnu

48.2.6.3. Vytvorenie siete okolo trnu

48.2.6.4. Určenie materiálu tŕňa

48.2.6.5. Vytvorenie BCC s mandrelom

48.2.6.6. Nastavenie referenčného bodu pre trn

48.2.7. Definovanie objektu „Roll“

48.2.7.1. Definovanie geometrie valca, siete, materiálu a BCC

48.2.7.2. Stránka s orientáciou zvitku

48.2.8. Tabuľka prechodov

48.2.9. Ovládacie prvky

48.2.9.1. Automatické polohovanie

48.2.9.2. Pokročilé umiestňovanie objektov

48.2.10. Kontakt

48.2.11. Ovládacie prvky na zastavenie

48.2.12. Ovládacie prvky simulácie

48.2.13. Vytvorenie databázy

## Ako pridať operáciu tvarovania tokom

Operácia odstreďovania sa používa na nastavenie operácie tepelného tvárnenia. Operáciu tepelného tvárnenia je možné nastaviť v prostredí integrovaného výrobného procesu, ku ktorému sa dostanete z hlavného okna grafického používateľského rozhrania. Novú úlohu vytvoríte buď výberom položky Súbor ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Nová úloha, alebo kliknutím na ikonu Nová úloha ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). V časti Typ úlohy a Systém jednotiek vyberte voľbu 3D Spinning. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) (ako je znázornené na obr. 48.2.1.). Otvorí sa šablóna Integrovaného výrobného procesu a v editore operácií uvidíte, že bola pridaná operácia 3D Spinning.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0001.jpg' | relative_url }})

Pridanie operácie točenia z hlavného okna grafického rozhrania

  
Operáciu tvarovania prúdom môžeme nastaviť aj tak, že do prostredia Integrovaného výrobného procesu pridáme operáciu odstreďovania z kontextového menu Nový projekt pri otvorení novej úlohy v prostredí Integrovaného výrobného procesu, ako je znázornené na obr. 48.2.2. Pomocou možnosti „Kopírovať existujúci projekt“ môžeme z kontextového menu Nový projekt importovať predtým uložené projekty ako nový projekt.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0002.jpg' | relative_url }})

V okne „Nový projekt“ zadejte názov projektu a vyberte prvú operáciu

  
Operáciu tvarovania tokom môžeme nastaviť pridaním operácie odstreďovania do editora operácií z karty „Explorer“ v prostredí integrovaného výrobného procesu, a to kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie odstreďovania (ako je znázornené na obr. 48.2.3.) alebo presunutím operácie odstreďovania do okna editora operácií pomocou funkcie „drag and drop“. Keď sa operácia „Spinning“ pridá do editora operácií, ak je aktuálny smer nahor obrazovky smer „Z“, zobrazí sa nám vyskakovacie okno „Zmeniť os smeru nahor obrazovky“, ako je znázornené na obr. 48.2.3. V tomto vyskakovacom okne kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_change_button.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0003.jpg' | relative_url }})

Pridanie operácie zo zoznamu operácií v Průzkumníkovi – vyskakovacie okno smerujúce nahor

Teraz sa v okne na úpravu nastavení vlastností otvorí stránka Výber procesu, ako je znázornené na obr. 48.2.4.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0004.jpg' | relative_url }})

Pridanie operácie zo zoznamu operácií v Průzkumníkovi

## Postup

Na stránke procesu vyberte operáciu „**Flow****forming**“. Rýchlosť otáčania hriadeľa (w) môžeme nastaviť na stránke procesu, ako je znázornené na obr. 48.2.5.

**Rýchlosť otáčania (w):** Používateľ môže nastaviť rýchlosť vretena, ktorá sa bude aplikovať na koníček a vretenovú hlavu, ak sa používajú.

Pomocou šablóny môže používateľ nastaviť operácie tvárnenia tokom typu „vpred“ aj „späť“. V závislosti od typu procesu si používateľ môže vybrať príslušnú operáciu. 

**Typ s predným posuvom:** Valce a ťahaný materiál sa pohybujú v rovnakom axiálnom smere.

**Opačný typ:** Valce a ťahaný materiál sa pohybujú v opačnom axiálnom smere.

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0001.jpg' | relative_url }})

Stránka o procese tvarovania prúdom

## Nastavenie simulácie

Používateľ si môže vybrať metódu riešenia (ALE alebo Lagrangeovu), typ riešiteľa (implicitný alebo explicitný) a tepelné výpočty, ako je znázornené na obr. 48.2.6.

**Tepelné výpočty:** Na karte „Tepelné výpočty“ (pozri obr. 48.2.6.) máme k dispozícii možnosti výberu typov objektov, na ktorých sa majú vykonať tepelné výpočty. Používateľ má na výber medzi výpočtami len na obrobku alebo aj na valcoch v prípade neizotermických modelov. V prípade izotermických modelov môže používateľ vypnúť tepelné výpočty výberom konštantnej teploty.

**Cieľový objem**: Ak zaškrtneme políčko „Aktívne vo FEM“, obrobku sa priradí cieľový objem pre metódu „**Aktívne vo FEM**“.

**Express**: Používateľ môže zvoliť riešiteľ ALE Express na zvýšenie rýchlosti simulácie otáčania metódou ALE. Ak je zvolený tento riešiteľ, valec musí mať v strede otvor a medzi vretenníkom/koníkom a obrobkom musia byť definované kritériá neoddelenia.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0006.jpg' | relative_url }})

Stránka „Nastavenie simulácie“

  
Správanie sa zariadenia na tvarovanie prúdom v závislosti od výberu riešenia a riešiteľa je vysvetlené v nasledujúcej tabuľke,

**Objekt** |  **ALE + implicitný** |  **ALE + explicitný** |  **Lagrangeov + implicitný** |  **Lagrangeov + explicitný**  
---|---|---|---|---  
**Typ obrobku** |  Tvrdý plast |  Elastoplast |  Tvrdý plast |  Elastoplast  
**Iteračná metóda** |  MUMPS+ Priama iterácia |  Explicitná + N-R |  MUMPS + Priama iterácia |  Explicitná + N-R  
**Sieť obrobku** |  Nerovnomerná sieť v obvodovom smere (jemná sieť v mieste kontaktu). Pre explicitnú metódu sa uprednostňuje rovnomerná sieť |  Rovnomerná sieť v obvodovom smere  
**Pohyb obrobku** |  Obrobku nie je priradený žiadny pohyb  
V metóde ALE sa sieť v smere obruče neaktualizuje, preto sa nepozoruje žiadna rotácia objektu |  Lagrangeovská simulácia ukazuje skutočnú rotáciu obrobku. Pohyb obrobku sa dosahuje zavedením „prilepeného“ BCC na rozhraní s trnom a vretenníkom.  
**Trn/ koníček, vretenník/ valce, typ objektu** |  Pevný  
**Pohyb upínacieho trnu / koníka a vretenníka** |  Je definovaný iba uhlový pohyb typu „Rotácia 1“ okolo stredovej osi objektu  
**Pohyb valcov** |  Uhlový pohyb typu „Rotácia 1“ alebo krútiaci moment je definovaný okolo stredovej osi objektu  
Je možné definovať posun valcov (typ definície rýchlosti, sily alebo dráhy). Valce nekrúžia.  
**Rozhranie** |  Rozhranie s upevneným BCC na styčnej ploche medzi „obrobkom/trnom“ a „obrobkom/prednou hlavou“.  
|  Ak sa zistí okno trenia, použije sa „vyhľadávanie s ľahkým kontaktom“.  
Pevná zóna sa automaticky vytvorí pri detekcii priľnavosti BCC  |  |  Pri detekcii okna trenia sa použije „zjednodušené vyhľadávanie kontaktov“.  
  
## Výber objektov pre nastavenie

Používateľ si môže z dostupných typov objektov vybrať objekty, ktoré sa majú použiť v nastavení, ako je znázornené na obr. 48.2.7. Používateľ môže zvoliť „Počet valcov“, ktoré sa majú použiť v nastavení. Ak je valcov viac ako 1, uhol medzi nimi proti smeru hodinových ručičiek je možné definovať v tabuľke pod poľom „Počet valcov“, ako je znázornené na obr. 48.2.7.

Poznámka: V poli „Počet rolí“ môže používateľ zadať maximálne 3 role.

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0002.jpg' | relative_url }})

Stránka objektov (Nastavenie otáčania)

## Definovanie obrobku

Používateľ môže definovať názov obrobku, teplotu a typ objektu, ako je znázornené na obr. 48.2.8. V závislosti od výberu riešiteľa v nastavení simulácie musí používateľ vybrať typ objektu. Pre implicitný riešiteľ sa volí typ objektu „Plastický“ a pre explicitný riešiteľ typ objektu „Elastoplastický“. Používateľ môže importovať objekty z iných databáz alebo súborov kľúčov pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) alebo uložiť údaje o objektoch pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0003.jpg' | relative_url }})

Stránka objektu obrobku

### Definovanie 2D prierezu obrobku

Používateľ môže definovať 2D priečny rez obrobku pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) alebo ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}). Stred a os geometrie sa definujú v časti „Informácie o 2D priečnom reze“, ako je znázornené na obr. 48.2.9. Používateľ môže importovať 2D prierez z iných databáz alebo súborov kľúčov pomocou možností ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) alebo uložiť údaje o 2D priereze pomocou možností ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}). 

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0004.jpg' | relative_url }})

Stránka 2D geometrie

###  Vytvorenie siete obrobku

Nastavenie formovania tokom využíva tehličkovú sieť ako metódu generovania počiatočnej siete pre simulácie typu Lagrange aj ALE. Ak pri generovaní tehličkovej siete v simulácii typu Lagrange vzniknú akékoľvek problémy, pri opätovnom vytváraní siete sa použije tetraedrová sieť. Používateľ môže vygenerovať sieť priečneho rezu pre definované nastavenia kliknutím na označenie ![]({{ '/assets/icons/pre_icons/mo_generate_2d_mesh_button.jpg' | relative_url }}) a 3D sieť s definovanými nastaveniami možno vygenerovať kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}), pozri obr. 48.2.10.

#### Sieť s priečnym rezom

Počet prvkov: Používateľ tu môže určiť počet prvkov, ktoré sa majú použiť v sieti priečneho rezu, pozri obr. 48.2.10. Systém vygeneruje sieť priečneho rezu po kliknutí na označenie ![]({{ '/assets/icons/pre_icons/mo_generate_2d_mesh_button.jpg' | relative_url }}), ktoré sa otočí s cieľom vygenerovať 3D sieť.

#### Parametre vytvárania 3D sietí

**Počet otočených úsekov:** Používateľ môže vytvoriť 3D sieť definovaním počtu otočených úsekov v obvodovom smere a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}), pozri obr. 48.2.10.

**Rovnomerná hrúbka vrstiev v obvodovom smere:** Ak sa použije táto voľba, vygeneruje sa 3D sieť s vrstvami rovnomernej hrúbky v obvodovom smere, pozri obr. 48.2.10. Táto voľba sa odporúča pre nastavenie simulácie typu „Explicit“.

**Jemnejšia sieť v kontaktnej oblasti:** Používateľ môže vytvoriť jemnejšiu sieť v kontaktnej oblasti zadaním uhla v poli „Uhol“. V rámci zadaného uhla v mieste kontaktu s valcami sa vytvorí jemná sieť s pomerom veľkostí zadaným v poli „Pomer veľkostí“, pozri obr. 48.2.10.

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0005.jpg' | relative_url }})

Stránka so sieťou obrobkov

### Určenie materiálu obrobku

Na stránke materiálu môže používateľ načítať materiál pomocou funkcie „Importovať údaje o materiáli zo súboru“ (![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})) alebo pomocou možnosti „Načítať z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})), pozri obr. 48.2.11. Po načítaní materiálu môže používateľ vybrať materiál, ktorý sa má použiť pre príslušný objekt. Ak materiál nie je k dispozícii v knižnici DEFORM, používateľ môže pomocou ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) vytvoriť nový materiál. Používateľ môže materiál zo zoznamu odstrániť pomocou ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) alebo údaje o materiáli upraviť pomocou ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}). Upravený alebo novo definovaný materiál je možné uložiť pomocou ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}). 

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0006.jpg' | relative_url }})

Priradenie materiálu k obrobku

### Definovanie BCC obrobku

Na stránke „Okrajové podmienky“ môže používateľ objektu priradiť rôzne okrajové obmedzenia. Okrajové podmienky určujú, ako hranica objektu interaguje s ostatnými objektmi a s okolím. Bežne používanými okrajovými podmienkami sú výmena tepla s okolím pri simuláciách zahŕňajúcich prenos tepla a kontakt medzi objektmi v modeli. V závislosti od výberu „Procesu“ a „Nastavenia simulácie“ systém generuje predvolené BCC pre neizotermický proces a pre objekty, ktoré sú v kontakte. Obr. 48.2.12. znázorňuje rôzne BCC, ktoré je možné priradiť k objektu. Ďalšie informácie nájdete v [14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/). 

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0007.jpg' | relative_url }})

Stránka BCC pre obrobok

## Definovanie objektu „Mandrel“

Trn je veľmi dôležitý objekt pri tvárnení dosiek, keďže materiál tečie po povrchu trnu a nadobúda jeho tvar. Trn môže mať tvar jednoduchého valca alebo môže mať určitý profil. Typ objektu trnu je „Tuhý“. Na stránke objektu „Mandrel“ môže používateľ definovať názov objektu a teplotu. Používateľ môže importovať objekt z iných databáz alebo kľúčových súborov pomocou možností ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) alebo uložiť údaje o objekte pomocou možností ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}). 

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0008.jpg' | relative_url }})

Stránka objektu „Mandrel“

### Definovanie 2D prierezu trnu

2D priečny rez pre upínací trn je možné definovať podobne ako 2D priečny rez obrobku, ako je vysvetlené v bode 48.2.5.1. Definovanie 2D priečneho rezu obrobku. Používateľ môže definovať 2D priečny rez, ktorý sa použije na vytvorenie 3D geometrie.

### Vytvorenie 3D geometrie trnu 

Používateľ musí vytvoriť 3D geometriu pre všetky objekty v nastavení operácie tvárnenia tokom. Operácia tvárnenia tokom/odstredivého tvárnenia využíva 2D prierez na vytvorenie 3D geometrie otáčaním okolo definovanej osi a stredu na stránke objektu obrobku. Po definovaní možností digitalizácie, počtu otočených rezov a jemnejšej geometrie v kontaktnej oblasti musí používateľ kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}), aby vytvoril 3D geometriu, ako je znázornené na obr. 48.2.14.

**Digitalizácia:** Na riadenie bodov digitalizácie na 2D priečnom reze s cieľom dosiahnuť presné zobrazenie 2D priečneho rezu je možné použiť „frakciu tolerancie dĺžky“ / „maximálny prípustný uhol“ / „minimálny prípustný uhol“; pozri obr. 48.2.14.

**Počet otočených rezov:** Pri generovaní 3D geometrie z 2D priečneho rezu môže používateľ určiť počet vrstiev v smere obruče.

**Jemnejšia geometria v oblasti kontaktu:** Používateľ môže zaškrtnúť toto políčko, ak potrebuje vygenerovať jemnejšiu 3D geometriu v mieste kontaktu s obrobkom s cieľom zlepšiť výpočty kontaktu. Používateľ môže pre jemnejšiu sieť definovať hodnotu „Uhla“ v mieste kontaktu a „Pomeru veľkostí“.

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0009.jpg' | relative_url }})

Stránka na generovanie 3D geometrie

### Vytvorenie siete okolo trnu

Ak chce používateľ vykonať tepelné výpočty v rámci neizotermickej simulácie, môže vytvoriť sieť pre trn. Nastavenia siete a postup jej vytvárania sú podobné ako v bode 48.5.2. Vytváranie siete obrobku.

### Určenie materiálu trnu 

Používateľ môže pri načítaní z knižnice priradiť materiál zo zoznamu podobne ako v bode 48.2.5.3. Definovanie materiálu obrobku.

### Vytvorenie BCC s mandrelom

V závislosti od výberu položiek „Nastavenie simulácie“ a „Riešiteľ“ systém automaticky vygeneruje BCC. Medzi bežne používané typy BCC patria „Výmena tepla s okolím“ a „Kontaktné“ BCC; ďalšie informácie nájdete v [14\. BCC Controls](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/).

### Nastavenie referenčného bodu pre upínací trn

Používateľ môže definovať referenčný bod pre trn a umiestniť trn vo vzťahu k počiatku DEFORM pozdĺž osi X. Systém zobrazí vypočítanú hodnotu D od počiatku DEFORM na základe aktuálnej polohy trnu, ako je znázornené na obr. 48.2.15. „D“ je vzdialenosť medzi počiatkom Deform a počiatkom trnu pozdĺž osi X a bude sa používať na umiestnenie trnu.

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0010.jpg' | relative_url }})

Stránka nastavenia referenčného bodu

## Definovanie objektu „Roll“

Každý valec je potrebné definovať samostatne. Valce patria do typu „Rigid Object“ a je možné na nich vytvoriť sieť, ak je potrebné vykonať tepelné výpočty v neizotermickom simulačnom nastavení. Na stránke objektu valca môže používateľ definovať názov objektu a teplotu. Používateľ môže importovať objekt valca z iných databáz alebo kľúčových súborov pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) alebo uložiť údaje o objekte pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

### Definovanie geometrie valca, siete, materiálu a BCC

Geometriu valca, sieť (v prípade neizotermického nastavenia), materiál a BCC je možné definovať podobne ako v metodike opísanej v bode 48.2.5.1. Definovanie 2D priečneho rezu obrobku, 48.2.6.2. Vytvorenie 3D geometrie trnu, 48.2.5.3. Definovanie materiálu obrobku a 48.2.5.4. Definovanie BCC obrobku.

### Stránka s orientáciou rolí

Pri operácii tvarovania tokom si valce vyžadujú špecifický prístup k nastaveniu vzhľadom na to, že využívajú riadenie pohybu podľa dráhy. Posun valca bude definovaný dráhou, ktorá sa aplikuje v lokálnom UV (axiálnom/radiálnom) súradnicovom systéme. Tento pohyb sleduje jeden bod na valci, tzv. referenčný bod (východiskový bod). Aktuálna poloha referenčného bodu, a tým aj valca, je určená údajmi o dráhe a aktuálnym časom. Každý valec, ktorý sleduje dráhu, musí mať definovaný referenčný bod. 

Používateľ môže vybrať referenčný bod náklonu pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) vedľa poľa „Roll Datum“ (pozri obr. 48.2.16), čím sa zobrazia možnosti „Rotation center“, „Stred nosa“ a „Rohový bod“, ako je znázornené na obr. 48.2.16., ktoré sa majú použiť ako „Referenčný bod náklonu“. Na základe výberu sa automaticky vypočítajú súradnice referenčného bodu. Používateľ môže súradnice referenčného bodu zadať aj ručne. Používateľ môže definovať „Uhol orientácie“ vo vzťahu k osi X, ako je znázornené na obr. 48.2.17. 

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0011.jpg' | relative_url }})

Stránka orientácie zvitku – Sprievodca nastavením referenčného bodu zvitku 

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0012.jpg' | relative_url }})

Stránka o orientácii rolí – uhol orientácie

## Tabuľka priechodov

Proces tvarovania tlakom môže zahŕňať jeden alebo viacero priechodov; používateľ môže definovať údaje o pohybe pri viacerých priechodoch a viacerých valcoch pomocou „Tabuľky priechodov“, ako je znázornené na obr. 48.2.18. Po kliknutí na tlačidlo sa zobrazia ovládacie prvky pohybu valcov, ako je znázornené v [Fig. 48.2.19.](48_1_spinning_manual.htm#Fig_48_1_19__Roll_Movement_Controls). Používateľ môže definovať posuvný pohyb pomocou typov [Speed](/docs/en/pre_processor/15_movement_controls_definition/15_1_speed/) a [Path](/docs/en/pre_processor/15_movement_controls_definition/15_8_path/). Pre typ [Rotation movement](/docs/en/pre_processor/15_movement_controls_definition/15_9_rotational_movement/) sú k dispozícii typy uhlová rýchlosť a krútiaci moment.

Pohyb typu „Path“ sa bežne používa v procese tvarovania tokom. Ďalšie informácie o definovaní pohybu typu „[Path](/docs/en/pre_processor/15_movement_controls_definition/15_8_path/)“ nájdete v časti [15\. Movement controls.](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/). Po definovaní údajov o pohybe dráhy môže používateľ pomocou ![]({{ '/assets/icons/pre_icons/mo_show_path_movement_info_in_2d_button.jpg' | relative_url }}) zobraziť dráhu, ktorú bude referenčný bod valčeka sledovať v 2D, ako je znázornené na obr. 48.2.20.

Používateľ môže v tabuľke hesiel definovať aj ďalšie údaje, ako je vysvetlené nižšie,

**Trvanie procesu:** Hodnotu trvania procesu môžeme definovať ako kritérium na ukončenie definovanej simulácie Pass.

**Trenie valca:** Môžeme nastaviť hodnotu koeficientu trenia medzi valcom a obrobkom. Táto hodnota koeficientu trenia sa uplatňuje iba medzi valcom a obrobkom; používateľ ju môže v prípade potreby upraviť na stránke „Kontakt“. 

**Koeficient prenosu tepla medzi valcom a obrobkom:** Môžeme nastaviť hodnotu koeficientu prenosu tepla medzi valcom a obrobkom. Táto hodnota koeficientu prenosu tepla sa vzťahuje iba na vzťah medzi valcom a obrobkom; používateľ môže túto hodnotu v prípade potreby upraviť na stránke s nastaveniami. 

**Doba zdržania:** Pri všetkých priechodoch môžeme v tabuľke priechodov použiť položku „Doba zdržania“ na určenie času medzi koncom aktuálneho vybraného priechodu a nasledujúcim priechodom.

**Teplota počas výdrže:** V tabuľke priechodov môžeme použiť položku „Teplota počas výdrže“, aby sme určili teplotu prostredia počas doby výdrže.

**Koeficient konvekcie**: Pomocou položky „Koeficient konvekcie“ v tabuľke režimov môžeme určiť hodnotu koeficientu konvekcie počas doby výdrže.

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0013.jpg' | relative_url }})

Stránka s prehľadom tabuliek

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0014.jpg' | relative_url }})

Ovládacie prvky pohybu valcov

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0015.jpg' | relative_url }})

Informácie o pohybe po dráhe v 2D

## Ovládacie prvky (umiestňovanie objektov)

Polohu objektov je možné meniť pomocou možností „Automatické umiestňovanie“ a „Pokročilé umiestňovanie objektov“, ktoré sú k dispozícii na stránke „Ovládacie prvky“, ako je znázornené na obr. 48.2.21.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0021.jpg' | relative_url }})

Stránka ovládacích prvkov

### Automatické polohovanie

Pri technológii Flow Forming je možné automatické polohovanie nastaviť zadaním príslušných hodnôt, ako je znázornené na obr. 48.2.22.   
D = Vzdialenosť medzi vretenníkom / počiatkom a prvým valcom (X)  
K = uhol sklonu valcov voči osi X   
A = Vzdialenosť pozdĺž osi X od prvého valca (X) a ostatných valcov  
Po nastavení hodnôt sa valce nastavia podľa zadaných hodnôt parametrov, pozri obr. 48.2.23.

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0016.jpg' | relative_url }})

Možnosti automatického polohovania

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0017.jpg' | relative_url }})

Automatické polohovanie pre zariadenie na tvarovanie prúdom

### Pokročilé umiestňovanie objektov

Ak chce používateľ zmeniť polohu niektorého z objektov, môže na ovládacej stránke použiť tlačidlo „Pokročilé nastavenie polohy objektu“. Na umiestnenie objektov sú k dispozícii rôzne možnosti, ako je znázornené na obr. 48.2.24. Ďalšie informácie o týchto možnostiach nájdete v [19\. Object Positioning.](/docs/en/pre_processor/19_object_positioning/19_object_positioning/).

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0025.jpg' | relative_url }})

Pokročilé možnosti umiestňovania objektov

## Kontakt

Používateľ môže definovať kontakt medzi obrobkom a ostatnými valcovými objektmi stanovením vzťahov medzi objektmi. Pri operácii tvarovania tokom použijeme podmienky prilnutia pre obrobok s trnom a koníkom, ako je znázornené na obr. 48.2.25. Používateľ musí pre neizotermické procesy valcovania definovať koeficient trenia a koeficient prenosu tepla na rozhraní a pre izotermický proces valcovania hodnotu trenia. 

**Systém:** Po výbere tohto prepínača systém priradí predvolené vzťahy medzi objektmi. V prípade potreby môže používateľ pridať mazivá tak, že z roletového menu vyberie možnosť „Pridať nové“ a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}), alebo môže na účely simulácie načítať požadované mazivá z knižnice.

**Používateľ:** Pri operácii tvárnenia tokom je štandardne vybrané rádio tlačidlo „Používateľ“. Používateľ môže pridať vzťahy kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}), ako je znázornené na obr. 48.2.26. Používateľ môže upraviť hodnotu každého vzťahu tak, že ho vyberie a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môže používateľ priradiť rovnaké hodnoty všetkým vzťahom. Kliknutím na tlačidlo môže používateľ vypočítať toleranciu kontaktu. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) môže používateľ vygenerovať kontaktný vzťah. Zaškrtnutím políčka vedľa kontaktného vzťahu môže používateľ definovať prilepený kontakt.

Ďalšie informácie nájdete v dokumente [20\. Inter-Object Relations](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/).

**Poznámka**: V nastaveniach simulácie typu ALE môže používateľ definovať okná trenia pre valce a trn, ako je znázornené na obr. 48.2.26., čím aktivuje vyhľadávanie typu „Lite Contact“, ktoré skráti čas potrebný na vyhľadávanie kontaktov.

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0018.jpg' | relative_url }})

Stránka s kontaktnými údajmi

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0019.jpg' | relative_url }})

Okno „Definovanie trenia“

## Ovládacie prvky na zastavenie

Používateľ môže ako kritérium ukončenia simulácie nastaviť jej trvanie, ako je znázornené na obr. 48.2.27.

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0020.jpg' | relative_url }})

Stránka s ovládacími prvkami na zastavenie

## Ovládacie prvky simulácie

Používateľ môže nastaviť ovládacie prvky krokov pre simuláciu tak, ako je znázornené na obr. 48.2.28.

**Počet krokov:** Tu je možné definovať počet krokov, ktoré sa majú simulovať. Simulácia sa môže ukončiť skôr na základe kritérií ukončenia; ak je v tabuľke priechodov definovaný prenos tepla, simulácia pokračuje operáciou „Prenos tepla“. Tieto „Počet krokov“ nezahŕňajú čas prenosu; štandardne sa čas prenosu simuluje vždy v 100 krokoch.

**Krok:** Hodnota kroku, ktorá sa má uložiť do databázy, určuje počet krokov, ktoré systém uloží do databázy. Pri spustení simulácie sa musí vypočítať každý krok, ale nie je nutné, aby sa každý z nich uložil do databázy. Uloženie väčšieho počtu krokov zachová viac informácií o procese, čo však bude vyžadovať viac úložného priestoru.

**Čas na jeden krok:** Ak je zadaný čas na jeden krok, použije sa časový interval na jeden krok. Posun formy na jeden krok bude rovný časovému kroku vynásobenému rýchlosťou formy.

**Posun na krok:** Ak je špecifikovaný posun na krok, primárna matica sa v každom časovom kroku posunie o zadanú hodnotu. Celkový posun primárnej matice bude rovný posunu na krok vynásobenému celkovým počtom krokov.

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0021.jpg' | relative_url }})

Stránka ovládacích prvkov simulácie

## Vytvoriť databázu

**Kontrola údajov** ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}): Keď používateľ klikne na tento popisok, systém skontroluje údaje. Ak sú údaje správne, môžeme vygenerovať databázu. Ak sú údaje správne, môžeme vygenerovať databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvoriť databázu** ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}): Užívateľ môže vytvoriť databázu kliknutím na tento nápis (pozri obr. 48.2.29.).

**Pridať súbor .key:** Akékoľvek informácie, ktoré nie sú definované v šablóne, ale stále sa vzťahujú na proces, je možné načítať ako súbor .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt; tieto hodnoty je možné definovať v súbore .key a uložiť do zadaného umiestnenia. V prípade potreby je možné zmeniť len hodnoty v súbore .key a simuláciu znovu spustiť, aby sa preskúmal vplyv zmeny parametrov.

![]({{ '/assets/images/operation_templates/48_spinning/48_2_flow_forming/image0022.jpg' | relative_url }})

Vytvoriť stránku databázy
