---
lang: sk
title: "48.1. Príručka pre točenie"
---

# 48.1. Príručka pre točenie

48.1.1. Ako pridať operáciu „Spinning“

48.1.2. Postup

48.1.3. Nastavenie simulácie

48.1.4. Výber objektov pre nastavenie

48.1.5. Stránka obrobku

48.1.5.1. Definovanie 2D priečneho rezu obrobku

48.1.5.2. Stránka „Mriežka obrobku“

48.1.5.3. Stránka s materiálmi

48.1.5.4. Definovanie BCC obrobku

48.1.6. Definovanie objektu „Mandrel“

48.1.6.1. Definovanie 2D priečneho rezu trnu

48.1.6.2. Vytvorenie 3D geometrie trnu

48.1.6.3. Vytvorenie siete okolo tŕňa

48.1.6.4. Určenie materiálu trnu

48.1.6.5. Vytvorenie BCC s trnom

48.1.6.6. Nastavenie referenčného bodu pre trn

48.1.7. Definovanie objektu „Roll“

48.1.7.1. Definovanie geometrie valca, siete, materiálu a BCC

48.1.7.2. Stránka s orientáciou rolky

48.1.8. Tabuľka priechodov

48.1.9. Ovládacie prvky

48.1.9.1. Automatické polohovanie

48.1.9.2. Pokročilé umiestňovanie objektov

48.1.10. Kontakt

48.1.11. Ovládacie prvky na zastavenie

48.1.12. Ovládacie prvky simulácie

48.1.13. Vytvorenie databázy

## Ako pridať operáciu „Spinning“

Operáciu točenia je možné nastaviť v prostredí integrovaného výrobného procesu, ku ktorému sa dostanete z hlavného okna grafického používateľského rozhrania (GUI). Novú úlohu vytvoríte buď výberom položky Súbor ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Nová úloha, alebo kliknutím na ikonu Nová úloha ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). V časti Typ úlohy a Systém jednotiek vyberte prepínač 3D točenie. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) (ako je znázornené na obr. 48.1.1.). Otvorí sa šablóna Integrovaný výrobný proces a v editore operácií uvidíme, že bola pridaná operácia 3D Spinning.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0001.jpg' | relative_url }})

Pridanie operácie točenia z hlavného okna grafického rozhrania

  
Operáciu „Spinning“ môžeme do prostredia integrovaného výrobného procesu pridať aj z kontextového menu „Nový projekt“, keď sa v tomto prostredí otvorí nový problém, ako je znázornené na obr. 48.1.2. Pomocou možnosti „Kopírovať existujúci projekt“ môžeme z kontextového menu „Nový projekt“ importovať predtým uložené projekty ako nový projekt.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0002.jpg' | relative_url }})

V okne „Nový projekt“ zadajte názov projektu a vyberte prvú operáciu

  
Operáciu „Spinning“ môžeme do editora operácií pridať aj z karty „Explorer“ v prostredí „Integrated Manufacturing Process“ – kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie „Spinning“ alebo presunutím operácie „Spinning“ do okna editora operácií metódou drag-and-drop. Keď sa operácia „Spinning“ pridá do editora operácií a ak je aktuálny smer nahor obrazovky smer „Z“, zobrazí sa nižšie uvedené vyskakovacie okno, ako je znázornené na obr. 48.1.3. V okne „Zmeniť os smeru nahor obrazovky“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_change_button.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0003.jpg' | relative_url }})

Pridanie operácie zo zoznamu operácií v Průzkumníkovi – vyskakovacie okno smerom nahor na obrazovke

Teraz sa v okne na úpravu nastavení vlastností otvorí stránka „Výber procesu“, ako je znázornené na obr. 48.1.4.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0004.jpg' | relative_url }})

Spustili prevádzku 3D Spinning

## Postup

Na stránke procesu je štandardne zvolená možnosť „Spinning“. Pomocou šablóny operácie „Spinning“ môžeme nastaviť operáciu „Flow forming“. Rýchlosť otáčania hriadeľa (w) môžeme definovať na stránke procesu, ako je znázornené na obr. 48.1.5.

**Rýchlosť otáčania (w)**: Používateľ môže nastaviť rýchlosť vretena, ktorá sa bude uplatňovať na koníček a vretenovú hlavu, ak sa používajú.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0005.jpg' | relative_url }})

Stránka o procese spriadania

## Nastavenie simulácie

Používateľ si môže vybrať metódu riešenia (ALE alebo Lagrangeovu), riešiteľ (implicitný alebo explicitný) a tepelné výpočty, ako je znázornené na obr. 48.1.6.

**Tepelné výpočty:** Na karte „Tepelné výpočty“ (pozri obr. 48.1.6.) máme k dispozícii možnosti výberu typov objektov, na ktorých sa majú vykonať tepelné výpočty. Používateľ má možnosť zvoliť výpočty iba pre obrobok alebo v prípade neizotermických modelov aj pre valce. V prípade izotermických modelov môže používateľ vypnúť tepelné výpočty výberom konštantnej teploty.

**Cieľový objem**: Ak zaškrtnete políčko „Aktívne vo FEM“, obrobku sa priradí cieľový objem pre metódu „**Aktívne vo FEM**“.

**Express**: Používateľ môže zvoliť riešiteľ ALE Express na zvýšenie rýchlosti simulácie otáčania metódou ALE. Ak je zvolený tento riešiteľ, valec musí mať v strede otvor a medzi vretenníkom/koníkom a obrobkom musia byť definované kritériá neoddělitelnosti.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0006.jpg' | relative_url }})

Stránka „Nastavenie simulácie“

  
Správanie sa konfigurácie spiningu v závislosti od výberu riešenia a riešiteľa je vysvetlené v nasledujúcej tabuľke,

**Objekt** |  **ALE + implicitná metóda** |  **ALE + explicitná metóda** |  **Lagrangeova metóda + implicitná metóda** |  **Lagrangeova metóda + explicitná metóda**  
---|---|---|---|---  
**Typ obrobku** |  Tvrdý plast |  Elastoplast |  Tvrdý plast |  Elastoplast  
**Iteračná metóda** |  MUMPS+ Priama iterácia |  Explicitná + N-R |  MUMPS + Priama iterácia |  Explicitná + N-R  
**Sieť obrobku** |  Nerovnomerná sieť v obvodovom smere (jemná sieť v mieste kontaktu). Pre explicitnú metódu sa odporúča rovnomerná sieť |  Rovnomerná sieť v obvodovom smere  
**Pohyb obrobku** |  Obrobku nie je priradený žiadny pohyb  
V metóde ALE sa sieť v smere obruče neaktualizuje, preto sa nepozoruje žiadna rotácia objektu |  Lagrangeovská simulácia ukazuje skutočnú rotáciu obrobku. Pohyb obrobku sa dosahuje zavedením „prilepeného“ BCC na rozhraní s tŕňom a hlavou vretena.  
**Trn/koník, vreteno/valce, typ objektu** |  Tuhý  
**Pohyb upínacieho trnu/koníka a vretenníka** |  Je definovaný iba uhlový pohyb typu „Rotácia 1“ okolo stredovej osi objektu  
**Pohyb valcov** |  Uhlový pohyb typu „Rotácia 1“ alebo krútiaci moment je definovaný okolo stredovej osi objektu  
Je možné definovať posun valcov (typ definície rýchlosti, sily alebo dráhy). Valce sa neotáčajú po obežnej dráhe.  
**Rozhranie** |  Rozhranie s upevneným BCC na styčnom mieste medzi „obrobkom/trnom“ a „obrobkom/prednou hlavou“.  
|  Ak sa zistí okno trenia, použije sa „vyhľadávanie s ľahkým kontaktom“.  
Pevná zóna sa automaticky vytvorí pri detekcii priľnavosti BCC  |  |  Pri detekcii okna trenia sa použije „vyhľadávanie ľahkého kontaktu“.  
  
## Výber objektov pre nastavenie

Používateľ si môže z dostupných typov objektov vybrať objekty, ktoré sa majú použiť v nastavení, ako je znázornené na obr. 48.1.7. Používateľ môže zvoliť „Počet valcov“, ktoré sa majú použiť v nastavení. Ak je valcov viac ako 1, uhol medzi nimi v smere proti smeru hodinových ručičiek je možné definovať v tabuľke pod poľom „Počet valcov“, ako je znázornené na obr. 48.1.7.

  
Poznámka: V poli „Počet rolí“ môže používateľ zadať maximálne 3 role.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0007.jpg' | relative_url }})

Stránka objektov (Nastavenie otáčania)

## Stránka obrobku

Používateľ môže definovať názov obrobku, teplotu a typ objektu, ako je znázornené na obr. 48.1.8. V závislosti od výberu riešiteľa v nastaveniach simulácie musí používateľ zvoliť typ objektu. Pre implicitný riešiteľ sa volí typ „Plastický objekt“ a pre explicitný riešiteľ typ „Elastoplastický objekt“. Používateľ môže importovať objekty z iných databáz alebo súborov kľúčov pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) alebo uložiť údaje o objektoch pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0008.jpg' | relative_url }})

Stránka objektu obrobku

### Definovanie 2D priečneho rezu obrobku

Používateľ môže definovať 2D priečny rez obrobku pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) alebo ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}). Stred a os geometrie sa definujú v časti „Informácie o 2D priečnom reze“, ako je znázornené na obr. 48.1.9. Systém predpokladá, že geometria sa bude štandardne otáčať okolo osi X. Preto by os stredu geometrie 2D priečneho rezu mala byť kolineárna s globálnou osou X. Používateľ môže importovať 2D priečny rez z iných databáz alebo súborov kľúčov pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) alebo uložiť údaje 2D priečneho rezu pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0009.jpg' | relative_url }})

Stránka 2D geometrie

### Stránka „Mriežka obrobku“

Nastavenie Spinning používa ako metódu generovania počiatočnej siete pre Lagrangeov aj ALE typ simulácie tehlovú sieť. Ak pri generovaní tehlovej siete v Lagrangeovom type simulácie nastanú akékoľvek problémy, pri opätovnom vytváraní siete sa použije tetraedrová sieť. Používateľ môže vygenerovať sieť priečneho rezu pre definované nastavenia kliknutím na označenie ![]({{ '/assets/icons/pre_icons/mo_generate_2d_mesh_button.jpg' | relative_url }}) a 3D sieť s definovanými nastaveniami možno vygenerovať kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}), pozri obr. 48.1.10.

#### Sieť s priečnym rezom

  * **Počet prvkov:** Používateľ tu môže určiť počet prvkov, ktoré sa majú použiť v sieti prierezu, pozri obr. 48.1.10. Systém vygeneruje sieť prierezu po kliknutí na označenie ![]({{ '/assets/icons/pre_icons/mo_generate_2d_mesh_button.jpg' | relative_url }}), ktoré sa otočí s cieľom vygenerovať 3D sieť.

####   
Parametre vytvárania 3D siete

  * **Počet otočených úsekov:** Používateľ môže vytvoriť 3D sieť tak, že definuje počet otočených úsekov v obvodovom smere a klikne na ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}), pozri obr. 48.1.10.

  * **Rovnomerná hrúbka vrstiev v obvodovom smere:** Ak sa použije táto voľba, vytvorí sa 3D sieť s vrstvami rovnakej hrúbky v obvodovom smere, pozri obr. 48.1.10. Táto voľba sa odporúča pre nastavenie simulácie typu „Explicit“.

  * **Jemnejšia sieť v oblasti kontaktu:** Používateľ môže vytvoriť jemnejšiu sieť v oblasti kontaktu zadaním uhla v poli „Uhol“. V rámci zadaného uhla v mieste kontaktu s valcami sa vytvorí jemná sieť s pomerom veľkostí zadaným v poli „Pomer veľkostí“, pozri obr. 48.1.10.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0010.jpg' | relative_url }})

Stránka so sieťou obrobkov

### Stránka s materiálmi

Na stránke materiálu môže používateľ načítať materiál pomocou funkcie „Importovať údaje o materiáli zo súboru“ (![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})) alebo pomocou možnosti „Načítať z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})), pozri obr. 48.1.11. Po načítaní materiálu môže používateľ vybrať materiál, ktorý sa má použiť pre príslušný objekt. Ak materiál nie je k dispozícii v knižnici DEFORM, môže ho používateľ vytvoriť pomocou ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Používateľ môže materiál zo zoznamu odstrániť pomocou ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) alebo údaje o materiáli upraviť pomocou ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}). Upravený alebo novo definovaný materiál je možné uložiť pomocou ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0011.jpg' | relative_url }})

Priradenie materiálu k obrobku

### Definovanie BCC obrobku

Na stránke „Okrajové podmienky“ môže používateľ objektu priradiť rôzne okrajové obmedzenia. Okrajové podmienky určujú, ako hranica objektu interaguje s inými objektmi a s prostredím. Bežne používanými okrajovými podmienkami sú výmena tepla s prostredím pri simuláciách zahŕňajúcich prenos tepla a kontakt medzi objektmi v modeli. V závislosti od výberu „Procesu“ a „Nastavenia simulácie“ systém generuje predvolené BCC pre neizotermický proces a pre objekty, ktoré sú v kontakte. Obr. 48.1.12. znázorňuje rôzne BCC, ktoré je možné priradiť k objektu. Ďalšie informácie nájdete v [14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/).

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0012.jpg' | relative_url }})

Stránka BCC pre obrobok

## Definovanie objektu „Mandrel“

Trn je pri spriadaní veľmi dôležitý objekt, keďže materiál tečie po povrchu trnu a prijíma jeho tvar. Trn môže mať tvar jednoduchého valca alebo môže mať určitý profil. Typ objektu trnu je „Tuhý“. Na stránke objektu trnu môže používateľ definovať názov objektu a teplotu (pozri obr. 48.1.13.). Používateľ môže importovať objekt z iných databáz alebo kľúčových súborov pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) alebo uložiť údaje o objekte pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0013.jpg' | relative_url }})

Stránka objektu „Mandrel“

### Definovanie 2D priečneho rezu trnu

2D prierez pre trn je možné definovať podobne ako 2D prierez obrobku, ako je vysvetlené v časti „Definovanie 2D prierezu obrobku“. Používateľ môže definovať 2D prierez, ktorý sa použije na vytvorenie 3D geometrie.

###  Vytvorenie 3D geometrie trnu 

Používateľ musí vytvoriť 3D geometriu pre všetky objekty v nastavení operácie točenia. Operácia tvarovania tokom/točenia využíva 2D priečny rez na vytvorenie 3D geometrie otáčaním okolo definovanej osi a stredu na stránke objektu „Obrobok“. Po definovaní možností digitalizácie, počtu otočených rezov a jemnejšej geometrie v kontaktnej oblasti musí používateľ kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}), aby vytvoril 3D geometriu, ako je znázornené na obr. 48.1.14.

**Digitalizácia:** Pomocou parametrov „Podiel tolerancie dĺžky“ / „Maximálny prípustný uhol“ / „Minimálny prípustný uhol“ je možné riadiť body digitalizácie na 2D priečnom reze s cieľom dosiahnuť presné zobrazenie 2D priečneho rezu, pozri obr. 48.1.14.

**Počet otočených rezov:** Pri generovaní 3D geometrie z 2D priečneho rezu môže používateľ určiť počet vrstiev v smere obruče.

**Jemnejšia geometria v kontaktnej oblasti:** Používateľ môže zaškrtnúť toto políčko, ak potrebuje vygenerovať jemnejšiu 3D geometriu v mieste kontaktu s obrobkom s cieľom zlepšiť výpočty kontaktu. Používateľ môže pre jemnejšiu sieť definovať hodnotu „Uhla“ v mieste kontaktu a „Pomeru veľkostí“.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0014.jpg' | relative_url }})

Stránka na generovanie 3D geometrie

### Vytvorenie siete okolo trnu

Ak chce používateľ vykonať tepelné výpočty v rámci neizotermickej simulácie, môže vytvoriť sieť pre trn. Nastavenia siete a postup jej generovania sú podobné ako pri generovaní siete obrobku.

### Určenie materiálu trnu 

Používateľ môže pri načítaní zo knižnice priradiť materiál zo zoznamu podobne ako pri definovaní materiálu obrobku.

### Vytvorenie BCC s mandrelom

V závislosti od výberu položiek „Nastavenie simulácie“ a „Riešiteľ“ systém automaticky vygeneruje BCC. Medzi bežne používané typy BCC patria „Výmena tepla s okolím“ a „Kontakt“; ďalšie informácie nájdete v [14\. BCC Controls](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/).

### Nastavenie referenčného bodu pre trn

Používateľ môže definovať referenčný bod pre trn a umiestniť trn vzhľadom na počiatok DEFORM pozdĺž osi X. Systém zobrazí vypočítanú hodnotu D od počiatku DEFORM na základe aktuálnej polohy upínacieho tŕňa, ako je znázornené na obr. 48.1.15. „D“ je vzdialenosť medzi počiatkom DEFORM a počiatkom upínacieho tŕňa pozdĺž osi X a bude sa používať na umiestnenie upínacieho tŕňa.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0015.jpg' | relative_url }})

Stránka nastavenia referenčného bodu

## Definovanie objektu „Roll“

Každý valec je potrebné definovať samostatne. Valce sú objektmi typu „Rigid Object“ a je možné na nich vytvoriť sieť, ak je potrebné vykonať tepelné výpočty v neizotermickom simulačnom nastavení. Na stránke objektu valca môže používateľ definovať názov objektu a teplotu. Používateľ môže importovať objekt valca z iných databáz alebo kľúčových súborov pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) alebo uložiť údaje o objekte pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

### Definovanie geometrie valca, siete, materiálu a BCC

Geometriu valca, sieť (v prípade neizotermického nastavenia), materiál a BCC je možné definovať podobne ako v metodike opísanej v bode 48.1.5.1. Definovanie 2D priečneho rezu obrobku, 48.1.6.2. Vytvorenie 3D geometrie tŕňa, 48.1.5.3. Definovanie materiálu obrobku a 48.1.5.4. Definovanie BCC obrobku.

### Stránka s orientáciou rolí

Pri operáciách točenia si valce vyžadujú špecifický prístup k nastaveniu vzhľadom na použitie riadenia pohybu po dráhe. Posun valca bude definovaný dráhou, ktorá sa aplikuje v lokálnom UV (axiálnom/radiálnom) súradnicovom systéme. Tento pohyb bude sledovať jeden bod na valci, tzv. referenčný bod (východiskový bod). Aktuálna poloha referenčného bodu, a teda aj valca, sa určuje na základe údajov o dráhe a aktuálneho času. Každý valec, ktorý sleduje dráhu, musí mať definovaný referenčný bod.  
Používateľ môže vybrať referenčný bod náklonu pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) vedľa poľa „Roll Datum“ (pozri obr. 48.1.16), čím sa zobrazia možnosti „Rotation center“, „Stred čela“ a „Rohový bod“, ako je znázornené na obr. 48.1.16., ktoré sa majú použiť ako „Referenčný bod valca“. Na základe výberu sa automaticky vypočítajú súradnice referenčného bodu. Pri výbere referenčného bodu valca by mal používateľ vybrať bod na čiernej polovici zobrazeného priečneho rezu valca. Používateľ môže súradnice referenčného bodu zadať aj ručne. Používateľ môže definovať „Uhol orientácie“ vo vzťahu k osi X, ako je znázornené na obr. 48.1.17. Uhol orientácie je potrebné nastaviť pred definovaním referenčného bodu valca. Referenčný bod valca je potrebné znovu vybrať vždy, keď sa uhol orientácie zmení.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0016.jpg' | relative_url }})

Stránka „Orientácia rolky“ – Sprievodca nastavením referenčného bodu

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0017.jpg' | relative_url }})

Stránka o orientácii rolí – uhol orientácie

## Tabuľka priechodov

Proces odstreďovania môže zahŕňať jeden alebo viacero prechodov; používateľ môže definovať údaje o pohybe pri viacerých prechodoch a viacerých otáčkach pomocou „Tabuľky prechodov“, ako je znázornené na obr. 48.1.18. Po kliknutí na tlačidlo sa zobrazia ovládacie prvky pre pohyb otáčania, ako je znázornené na obr. 48.1.19. Používateľ môže definovať posuvný pohyb pomocou typov „[Speed](/docs/en/pre_processor/15_movement_controls_definition/15_1_speed/)“ a „[Path](/docs/en/pre_processor/15_movement_controls_definition/15_8_path/)“. Pre rotačný pohyb sú k dispozícii typy uhlová rýchlosť a krútiaci moment. 

Pohyb typu „Path“ sa bežne používa v procese Spinning. Ďalšie informácie o tom, ako definovať pohyb typu „[Path](/docs/en/pre_processor/15_movement_controls_definition/15_8_path/)“, nájdete v časti [15\. Movement controls](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/). Po definovaní údajov o pohybe po dráhe môže používateľ pomocou ![]({{ '/assets/icons/pre_icons/mo_show_path_movement_info_in_2d_button.jpg' | relative_url }}) zobraziť dráhu, ktorú bude referenčný bod valčeka sledovať v 2D, ako je znázornené na obr. 48.1.20.

Používateľ môže v tabuľke hesiel definovať aj ďalšie údaje, ako je vysvetlené nižšie,

**Trvanie procesu:** Hodnotu trvania procesu môžeme definovať ako kritérium na zastavenie definovanej simulácie priechodu.

**Trenie valca:** Môžeme nastaviť hodnotu koeficientu trenia medzi valcom a obrobkom. Táto hodnota koeficientu trenia sa vzťahuje iba na vzťah medzi valcom a obrobkom; v prípade potreby ju môže používateľ upraviť na stránke s nastaveniami. 

**Koeficient prenosu tepla medzi valcom a obrobkom:** Môžeme definovať hodnotu koeficientu prenosu tepla medzi valcom a obrobkom. Táto hodnota koeficientu prenosu tepla sa vzťahuje iba na vzťah medzi valcom a obrobkom; používateľ môže túto hodnotu v prípade potreby upraviť na stránke s kontaktnými údajmi. 

**Doba zdržania:** Pri všetkých priechodoch môžeme v tabuľke priechodov použiť položku „Doba zdržania“ na určenie času medzi koncom aktuálneho vybraného priechodu a nasledujúcim priechodom.

**Teplota počas výdrže:** V tabuľke priechodov môžeme použiť položku „Teplota počas výdrže“ na určenie teploty prostredia počas doby výdrže.

**Koeficient konvekcie**: V tabuľke priechodov môžeme použiť položku „Koeficient konvekcie“ na zadanie hodnoty koeficientu konvekcie počas doby zdržania.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0018.jpg' | relative_url }})

Stránka s prehľadom tabuliek

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0019.jpg' | relative_url }})

Ovládacie prvky pohybu valcov

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0020.jpg' | relative_url }})

Informácie o pohybe po dráhe v 2D

## Ovládacie prvky (umiestňovanie objektov)

Polohu objektov je možné meniť pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) a „Pokročilé nastavenie polohy objektov“ ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}), ktoré sú k dispozícii na stránke „Ovládacie prvky“, ako je znázornené na obr. 48.1.21.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0021.jpg' | relative_url }})

Stránka ovládacích prvkov

### Automatické polohovanie

Pri spriadaní sa automatické polohovanie používa prevažne na polohovanie valcov na základe dráhy. Máme k dispozícii dve možnosti polohovania: „Počiatočné (t=0)“ a „Pri kontakte“, ako je znázornené na obr. 48.1.22.  
**Počiatočná poloha (t=0)** slúži na umiestnenie obrobku podľa definovaných súradníc dráhy v okamihu, keď je čas nulový, pozri obr. 48.1.23.  
Možnosť **Pri kontakte** slúži na pohyb valca po zadejenej dráhe, kým nedôjde ku kontaktu s obrobkom, a na aktualizáciu času, pozri obr. 48.1.24.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0022.jpg' | relative_url }})

Možnosti automatického polohovania

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0023.jpg' | relative_url }})

Poloha rotujúceho valca v počiatočnom stave (t = 0)

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0024.jpg' | relative_url }})

Polohovanie točiaceho sa valca v mieste kontaktu

### Pokročilé umiestňovanie objektov

Ak chce používateľ zmeniť polohu niektorého z objektov, môže na ovládacej stránke použiť tlačidlo „Pokročilé nastavenie polohy objektu“. K dispozícii sú rôzne možnosti umiestnenia objektov, ako je znázornené na obr. 48.1.25. Ďalšie informácie o týchto možnostiach nájdete v [19\. positioning objects.](/docs/en/pre_processor/19_object_positioning/19_object_positioning/).

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0025.jpg' | relative_url }})

Pokročilé možnosti umiestňovania objektov

## Kontakt

Používateľ môže definovať kontakt medzi obrobkom a ostatnými valcovými objektmi stanovením vzťahov medzi objektmi. Pri operácii odstreďovania použijeme podmienky prilnutia pre obrobok s trnom a koníkom, ako je znázornené na obr. 48.1.26. Používateľ musí pre neizotermické procesy valcovania definovať koeficient trenia a koeficient prenosu tepla cez rozhranie a pre izotermický proces valcovania hodnotu trenia.  
**Systém:** Po výbere tohto začiarkavacieho políčka systém priradí predvolené vzťahy medzi objektmi. V prípade potreby môže používateľ pridať mazivá tak, že z roletového menu vyberie možnosť „Pridať nové“ a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}), alebo môže na účely simulácie načítať požadované mazivá z knižnice.

**Používateľ:** Pri operácii „Spinning“ je štandardne zaškrtnuté políčko „Používateľ“. Používateľ môže pridať vzťahy kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}), ako je znázornené na obr. 48.1.26. Používateľ môže zmeniť hodnotu každého vzťahu tak, že ho vyberie a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môže používateľ priradiť rovnaké hodnoty všetkým vzťahom. Kliknutím na tlačidlo môže používateľ vypočítať toleranciu kontaktu. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) môže používateľ vygenerovať vzťah kontaktu. Zaškrtnutím políčka vedľa vzťahu kontaktu môže používateľ definovať zotrvačný kontakt. Ďalšie informácie nájdete v časti [20.Inter-Object Relations.](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/).

Poznámka: Používateľ môže v nastaveniach simulácie typu ALE definovať okná trenia pre valce a trn, ako je znázornené na obr. 48.1.27, čím aktivuje vyhľadávanie „Lite Contact“, ktoré skráti čas vyhľadávania kontaktov.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0026.jpg' | relative_url }})

Stránka s kontaktnými údajmi

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0027.jpg' | relative_url }})

Definovanie okna trenia

## Ovládacie prvky na zastavenie

Používateľ môže ako kritérium ukončenia simulácie nastaviť jej trvanie, ako je znázornené na obr. 48.1.28.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0028.jpg' | relative_url }})

Stránka s ovládacími prvkami na zastavenie

## Ovládacie prvky simulácie

Používateľ môže nastaviť ovládacie prvky krokov pre simuláciu tak, ako je znázornené na obr. 48.1.29.

**Počet krokov:** Tu je možné zadať počet krokov, ktoré sa majú simulovať. Simulácia sa môže ukončiť skôr na základe kritérií ukončenia; ak je v tabuľke priechodov definovaný prenos tepla, simulácia pokračuje operáciou „Prenos tepla“. Tieto „Počet krokov“ nezahŕňajú čas prenosu; štandardne sa čas prenosu simuluje vždy v 100 krokoch.

**Krok:** Hodnota kroku, ktorá sa má uložiť do databázy, určuje počet krokov, ktoré systém uloží do databázy. Pri spustení simulácie sa musí vypočítať každý krok, ale nemusí sa nutne uložiť do databázy. Uložením väčšieho počtu krokov sa zachová viac informácií o procese, čo však bude vyžadovať viac úložného priestoru.

**Čas na jeden krok:** Ak je zadaný čas na jeden krok, použije sa časový interval na jeden krok. Posun formy na jeden krok bude rovný časovému kroku vynásobenému rýchlosťou formy.

**Posun na krok:** Ak je špecifikovaný posun na krok, primárny valec sa v každom časovom kroku posunie o uvedenú hodnotu. Celkový posun primárneho valca bude rovný posunu na krok vynásobenému celkovým počtom krokov.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0029.jpg' | relative_url }})

Stránka ovládacích prvkov simulácie

## Vytvoriť databázu

**Kontrola Data![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}):** Keď používateľ klikne na tento názov, systém skontroluje údaje. Ak sú údaje správne, môžeme vygenerovať databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvoriť databázu** ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}): Používateľ môže vytvoriť databázu kliknutím na tento nápis. (Pozri obr. 48.1.30.)  
**Pridať súbor .key**: Akékoľvek informácie, ktoré nie sú definované v šablóne, ale aj tak sa vzťahujú na proces, je možné načítať ako súbor .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt; tieto hodnoty je možné definovať ako súbor .key a uložiť do zadaného umiestnenia. V prípade potreby je možné zmeniť len hodnoty v súbore .key a simuláciu znovu spustiť, aby sa preskúmal vplyv zmeny parametrov.

![]({{ '/assets/images/operation_templates/48_spinning/48_1_spinning_manual/image0030.jpg' | relative_url }})

Vytvoriť stránku databázy
