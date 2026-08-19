---
lang: sk
title: "43.1. Návod na tvarovanie valcovaním"
---

# 43.1. Návod na valcovanie tvaroviek

43.1.1. Ako pridať operáciu „Shape Rolling“

43.1.2. Operácia valcovania tvaru v editore operácií

43.1.3. Úroveň valcovacej skupiny

43.1.3.1. Postup

43.1.3.2. Stránka obrobku

  * 2D geometria

  * 2D sieť

  * Stránka s materiálmi

  * Stránka BCC (skupina Rolling)

43.1.3.3. Stránka „Zoznam skladieb“

43.1.3.4. Tabuľka prechodov

  * Prvý polčas

  * Nastavenie viacerých priechodov

  * Typ súpravy valcov

  * Definovanie geometrie drážky valca v tabuľke priechodov

  * Rýchlosť valca

  * Medzera medzi valcami

  * Otáčanie (°)

  * Spätné valenie (pre typ Lagrangeovho valenia)

  * Zobraziť všetky valce (pre asymetrické valcovanie)

  * Spustenie 2,5D simulácie

  * Stojanový stôl

  * Nastavenia stojana

43.1.3.5. Stránka nastavení 3D

  * Nastavenia geometrie 3D valca

  * Nastavenia 3D Roll mesh

  * Nastavenia 3D obrobku

  * Stránka s nastaveniami 3D pre typ ALE Rolling

  * Stránka nastavení 3D pre typ Lagrangeovho valenia

43.1.3.6. Ovládacie prvky simulácie

43.1.3.7. Vytvorenie databázy

43.1.4. Úroveň valcovania tvaru

43.1.4.1. Stojanový stôl

43.1.4.2. Stránka „Roll Stand“

  * Stránka o geometrii valcov

  * Stránka „Roll Mesh“

  * Stránka „Pohyb valcov“

43.1.4.3. Stránka s geometriou tabuľky/príručky

43.1.4.4. Stránka „Objekt obrobku“

  * Sieťka obrobku

  * Objemová kompozícia (BCC) obrobku

  * Pohyb obrobku

  * Inicializácia obrobku

  * Obrobok s integrovanou sieťou Flownet

43.1.4.5. Polohovanie

43.1.4.6. Plánované umiestnenie

43.1.4.7. Kontakt

43.1.4.8. Ovládacie prvky simulácie

43.1.4.9. Vytvorenie databázy

## Ako pridať operáciu „Valcovanie tvaru“

Operáciu valcovania tvarov je možné nastaviť v prostredí integrovaného výrobného procesu, do ktorého sa dostanete z „GUI Main“. Novú úlohu vytvoríte buď výberom položky File ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) New Problem, alebo kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). V časti „Typ úlohy“ a „Systém jednotiek“ vyberte prepínač „3D valcovanie tvarov“, ako je znázornené na obr. 43.1.1. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). Otvorí sa sprievodca integrovaným výrobným procesom a v editore operácií uvidíte, že bola pridaná operácia 3D valcovania tvarov.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0001.jpg' | relative_url }})

Pridanie operácie valcovania tvaru z hlavného okna grafického rozhrania

Operáciu valcovania tvarov môžeme do prostredia Integrovaného výrobného procesu pridať aj z kontextového menu „Nový projekt“, keď sa v tomto prostredí otvorí nový problém, ako je znázornené na obr. 43.1.2. Pomocou možnosti „Kopírovať existujúci projekt“ môžeme z kontextového menu „Nový projekt“ importovať predtým uložené projekty ako nový projekt.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0002.jpg' | relative_url }})

V okne „Nový projekt“ zadajte názov projektu a vyberte „Prvá operácia“

  
Operáciu „Valcovanie profilov“ môžeme do editora operácií pridať aj z karty „Explorer“ v prostredí integrovaného výrobného procesu – kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie „Valcovanie profilov“ (ako je znázornené na obr. 43.1.3.) alebo presunutím operácie „Valcovanie profilov“ do okna editora operácií metódou drag-and-drop. Po pridaní operácie „Valcovanie profilov“ do editora operácií sa v okne na úpravu nastavení vlastností otvorí stránka výberu procesu.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0003.jpg' | relative_url }})

Pridanie operácie „Valcovanie tvaru“ zo zoznamu operácií v Průzkumníku

## Operácia valcovania tvaru v editore operácií

Operácia tvarového valcovania sa nastavuje v dvoch rôznych fázach: na úrovni „valcovacej skupiny“ a na úrovni „valcovacieho priechodu“. Vo fáze „valcovacej skupiny“ definujeme operáciu na najvyššej úrovni pomocou objektov 2D priečnych rezov (obrobku aj drážok) a informácií o priechodoch. Na základe týchto informácií môže používateľ vygenerovať 3D objekty a následne definovať ovládacie prvky simulácie. Ak na úrovni priechodu nie je potrebné modelovať žiadne špecifické zmeny, používateľ môže spustiť simuláciu s týmito údajmi. Ovládacie prvky simulácie a ďalšie definície procesu stanovené na úrovni valcovacej skupiny sú spoločné pre všetky priechody. V etape valcovacieho priechodu môže používateľ vykonať konkrétne zmeny v každom priechode, ako napríklad pridať alebo odstrániť stoly/vodiace lišty, pridať alebo odstrániť stanice, definovať podmienky pre vytváranie novej siete a podobne.  
Po pridaní operácie valcovania tvaru v editore operácií si všimneme oranžovú lištu okolo operácie valcovacieho priechodu (ako je znázornené na obr. 43.1.4.), čo znamená, že sa nachádzame vo fáze valcovacej skupiny. Keď vyberieme operáciu valcovania, oranžový pásik skupiny valcovania zmení farbu na modrú a vybraná operácia valcovania bude zvýraznená oranžovým ohraničením, ako je znázornené na obr. 43.1.5.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0004.jpg' | relative_url }})

Je zvolená úroveň skupiny „Rolling“

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0005.jpg' | relative_url }})

Je zvolená operácia „Rolling Pass“

## **Úroveň skupiny Rolling**

### Postup

Na stránke „Proces“ bude používateľ zadávať nastavenia procesu a vyberie typ simulácie valcovania, ktorá sa má vykonať.  
**Typ valenia**: Šablóna valenia ponúka dva rôzne typy valenia. Jedným z nich je valenie ALE v ustálenom stave a druhým je Lagrangeovské (inkrementálne) valenie.   
**Lagrangeov typ valcovania:** Pri Lagrangeovom type valcovania je počiatočný tvar obrobku modelovaný rovnako ako skutočný obrobok a počas simulácie sa obrobok postupne posúva (deformuje) vo všetkých smeroch na základe výsledkov inkrementálnych rovníc a hodnoty stavových premenných sa aktualizujú. Dokončenie simulácie trvá dlhšie, pretože simulácia musí pokračovať, kým obrobok neprejde cez poslednú sadu valcov, aby bolo možné vizualizovať výsledok procesu valcovania; zároveň sa vypočítava a aktualizuje posun vo všetkých smeroch. 

**Typ valcovania ALE**: Pri type valcovania ALE (Augmented Lagrangian Eulerian) sa počiatočný obrobok modeluje približne tak, aby sa viac približoval konečnému tvaru (na lepšiu aproximáciu sa používajú 2,5D simulácie), pričom sa obrobok posúva iba v smeroch Y a Z, nie však v smere valcovania, a aktualizujú sa hodnoty stavových premenných. Simulácie ALE je možné zastaviť po dosiahnutí ustáleného stavu na základe kritérií zastavenia ALE; počet krokov potrebných na dosiahnutie ustáleného stavu závisí od toho, do akej miery dokážeme modelovať počiatočné podmienky obrobku tak, aby sa priblížili podmienkam ustáleného stavu. Simulácie ALE zvyčajne trvajú kratšie a pomáhajú rýchlo vizualizovať výsledok procesu valcovania.  
**Tepelné výpočty**: Na stránke „Tepelné výpočty“ (pozri obr. 43.1.6.) sú k dispozícii možnosti výberu typov objektov, na ktorých sa majú vykonať tepelné výpočty. Používateľ má na výber možnosti „Výpočty len v obrobku“ alebo dokonca „Výpočty aj vo valcoch“ v prípade neizotermických modelov, resp. „Výpočty pri konštantnej teplote“ v prípade izotermických modelov. V prípade nastavenia procesu valcovania za tepla môže používateľ zvoliť výpočty len v obrobku alebo aj vo valcoch. V prípade procesu valcovania za studena môže používateľ zvoliť konštantnú teplotu alebo výpočet len v obrobku, aby mohol sledovať zmeny teploty v obrobku.  
**Symetria:** Na karte „Symetria“ (pozri obr. 43.1.6.) máme k dispozícii možnosti výberu úplnej, polovičnej alebo štvrtinovej symetrie v závislosti od geometrickej symetrie, ktorú chceme v nastavení modelovať.  
**Koeficient trenia**: Môžeme nastaviť hodnotu koeficientu trenia medzi valcami a obrobkom. Táto hodnota koeficientu trenia sa uplatňuje medzi všetkými valcami a obrobkom vo všetkých priechodoch; používateľ môže túto hodnotu v prípade potreby upraviť na úrovni jednotlivých priechodov valcovania (pozri obr. 43.1.6.). 

**Koeficient prenosu tepla**: Na stránke procesu môžeme nastaviť hodnotu koeficientu prenosu tepla, ktorá sa bude uplatňovať na všetky priechody (pozri obr. 43.1.6.).

**Predvolené nastavenia prostredia**: Na stránke „Proces“ môžeme definovať hodnoty teploty prostredia a koeficientu konvekcie pre simulácie valcovania aj prenosu tepla, ktoré sa následne uplatnia na všetky operácie valcovania a prenosu tepla (pozri obr. 43.1.6.). Tieto nastavenia prostredia môžeme tiež prispôsobiť pre každý priechod na stránke „Tabuľka priechodov“ (pozri obr. 43.1.6.).

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0006.jpg' | relative_url }})

Definícia nastavení procesu

### Stránka obrobku

Na tejto stránke môžeme definovať teplotu a typ objektu obrobku, ako je znázornené na obr. 43.1.7. Štandardne je vybraný typ objektu „Plastický“; ak chce používateľ zohľadniť vplyv elastických vlastností, môže použiť typ objektu „Elastoplastický“. Používateľ môže importovať objekty z iných databáz alebo kľúčových súborov pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) alebo uložiť údaje o objektoch pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0007.jpg' | relative_url }})

Stránka s definíciou objektu obrobku

  * #### 2D geometria

Geometriu prierezu polotovaru je možné importovať zo súboru pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) alebo ju vytvoriť z ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) (základné tvary). Úpravy importovanej alebo vytvorenej geometrie je možné vykonať pomocou voľby ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}). Geometriu je možné uložiť pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0008.jpg' | relative_url }})

Stránka o geometrii

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0009.jpg' | relative_url }})

Stránka o geometrických primitívoch

  * #### 2D sieť

Sieť 2D priečneho rezu môžeme vytvoriť definovaním počtu prvkov v režime s návodom. Pokročilé možnosti na ovládanie vytvárania 2D siete sú dostupné prostredníctvom prepínača „expertný režim“ ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) na paneli nástrojov. Ďalšie informácie nájdete v [13.1. 2D Mesh Genearation](/docs/en/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/).

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0010.jpg' | relative_url }})

Nastavenia siete v režime s navádzaním

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0011.jpg' | relative_url }})

Nastavenia siete v režime pre pokročilých

  * #### Stránka o materiáloch

Na stránke materiálov sa zobrazujú všetky materiály pridané do zoznamu materiálov (ako je znázornené na obr. 43.1.12.). Používateľ môže vybrať požadovaný materiál a priradiť ho k príslušnému objektu. Ak požadovaný materiál nie je v zozname k dispozícii, môže ho používateľ na stránke materiálov objektu načítať pomocou funkcie Importovať údaje o materiáli zo súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) alebo pomocou možnosti Načítať z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). Ak materiál nie je k dispozícii v knižnici DEFORM, môže používateľ pomocou ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) vytvoriť nový materiál. Používateľ môže materiál zo zoznamu odstrániť pomocou ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) alebo údaje o materiáli upraviť pomocou ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}). Upravený alebo novo definovaný materiál je možné uložiť pomocou možností ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0012.jpg' | relative_url }})

Stránka s materiálmi

  * #### Stránka BCC (skupina s priebežným aktualizovaním)

Na stránke „Okrajové podmienky“ môže používateľ objektu priradiť rôzne okrajové obmedzenia. Okrajové podmienky určujú, ako okraj objektu interaguje s ostatnými objektmi a s prostredím. Medzi bežne používané okrajové podmienky patrí výmena tepla s prostredím pri simuláciách zahŕňajúcich prenos tepla, predpísaná rýchlosť na vynútenie symetrie a kontakt medzi objektmi v modeli. Obr. 43.1.13. znázorňuje rôzne okrajové podmienky, ktoré je možné priradiť k objektu vo fáze „Rolling Group“.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0013.jpg' | relative_url }})

Stránka BCC

### Stránka so zoznamom skladieb

Na stránke so zoznamom drážok môže používateľ vytvoriť alebo načítať priečne rezy drážok valcov, ktoré sa používajú v danej operácii. Drážku môžeme pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Po pridaní drážky je potrebné vybrať príslušnú drážku a definovať jej geometriu pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) alebo ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}). Používateľ má k dispozícii niekoľko preddefinovaných konštrukcií valcov, prípadne má možnosť vytvoriť valce z primitív. Môžeme tiež definovať stred otáčania a os drážok, ako je znázornené na obr. 43.1.14. Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) môžeme zoznam drážok uložiť do súboru a pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon2.jpg' | relative_url }}) môžeme zoznam drážok importovať.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0014.jpg' | relative_url }})

Stránka so zoznamom skladieb

  
**Definovanie geometrie drážky pomocou funkcie „Define Primitive“**

****Po kliknutí na označenie ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) sa otvorí okno „Roll groove primitives“ (Prvky drážky valca), ako je znázornené na obr. 43.1.15. Môžeme vybrať ľubovoľný tvar drážky, nastaviť jej parametre a následne kliknúť na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), čím vytvoríme geometriu drážky.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0015.jpg' | relative_url }})

Okno „Roll Groove Primitive“

### Tabuľka priechodov

V tabuľke priechodov môže používateľ definovať počet priechodov a polôh v každom priechode spolu s nastaveniami priechodu, ako je znázornené na obr. 43.1.16. V tejto tabuľke priechodov môže používateľ definovať typ súpravy valcov, vybrať drážky valcov, ktoré sa majú použiť, rýchlosť valcov (ot./min.), medzeru medzi valcami (mm), otáčanie obrobku (°) pred vstupom do priechodu, teplotu valcov, čas presunu do nasledujúceho priechodu po dokončení aktuálneho priechodu a zaškrtnúť políčko „Prispôsobiť prostredie“, aby mohol upraviť nastavenia prostredia, ak sa líšia od predvolených hodnôt definovaných na stránke „Proces“ alebo pomocou tlačidla „Prostredie“ na stránke tabuľky priechodov.

#### **Prvý polčas**

Táto funkcia slúži na simuláciu procesu prenosu tepla výlučne pre obrobok pred operáciou 1. Používateľ môže aktivovať funkciu „Prvý proces prenosu tepla“, aby simuloval čas prenosu z pece do operácie 1. Pre všetky ostatné operácie môže používateľ využiť položku „Čas prenosu“ v tabuľke operácií na určenie času medzi koncom aktuálne vybranej operácie a nasledujúcou operáciou.

#### **Nastavenie viacerých priechodov**

****V procese valcovania môžeme definovať viacero priechodov kliknutím na tlačidlo one![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) v tabuľke priechodov. Ak chce používateľ nejaký priechod odstrániť, vyberie príslušný priechod a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}). V editore operácií môžeme tiež pozorovať, že pri zvyšovaní alebo znižovaní počtu priechodov sa príslušne pridávajú alebo odstraňujú dlaždice tvarov valcovacích priechodov. Od verzie V14.0 sa po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridá nový priechod kopírovaním údajov z predchádzajúcej tabuľky priechodov.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0016.jpg' | relative_url }})

Stránka s prehľadom tabuliek

#### **Typ súpravy valcov**

V závislosti od usporiadania valcov na valcovacom stojane môže používateľ z roletového menu vybrať typ súpravy valcov, ako je znázornené na obr. 43.1.17. V závislosti od zvoleného typu súpravy valcov systém valce automaticky umiestni. V prípade ľubovoľného typu súpravy valcov musí používateľ určiť počet valcov a ich polohu. 

#### **Náhodné hody**

Voľné valce sa používajú pri úlohách, v ktorých sú valce umiestnené špecifickým spôsobom tak, aby spĺňali osobitné požiadavky. Tieto valce môžu byť umiestnené v ľubovoľnej polohe v priestore, pričom im možno priradiť ľubovoľnú hodnotu podľa požiadaviek úlohy. Základné kroky pri navrhovaní konštrukcie s voľnými valcami.

  1. Definujte geometriu drážky na stránke „Zoznam drážok“ (ako je znázornené na obr. 43.1.14.).

  2. Na stránke „Pass table“ vyberte ako typ sady hodov (Rollset type) v rámci Passu možnosť **Arbitrary**, vyberte Pass a kliknite na ![]({{ '/assets/icons/pre_icons/mo_stand_table_button.jpg' | relative_url }}) (ako je znázornené na obr. 43.1.18.).

  3. Vyberte stojan 1 a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_stand_settings.._button.jpg' | relative_url }}). V nastaveniach stojana zadajte počet valcov. Zadajte uhol voči susednému valcu a zo zoznamu vyberte geometriu drážky pre všetky valce. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) (ako je znázornené na obr. 43.1.19.).

  4. V tabuľke stojana nastavte medzeru medzi valcami a rýchlosť valcov a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) (ako je znázornené na obr. 43.1.20.).

  5. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku nastavení 3D, vygenerujte 3D geometriu a prezrite si ju (ako je znázornené na obr. 43.1.21.).

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0017.jpg' | relative_url }})

Priradenie typu Rollset

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0018.jpg' | relative_url }})

Výber ľubovoľného typu súboru hodov

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0019.jpg' | relative_url }})

Nastavenie stojana

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0020.jpg' | relative_url }})

Definovanie podrobností o stánku

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0021.jpg' | relative_url }})

Súprava valcov s ľubovoľným usporiadaním (štyri valce)

####   
Definovanie geometrie drážky valca v tabuľke priechodov

K dispozícii je niekoľko preddefinovaných vzorov valcov, z ktorých si môže používateľ vybrať; inak má možnosť vytvoriť valce z základných prvkov na stránke „Zoznam drážok“. Používateľ môže vybrať drážku z roletového menu v riadku „Horný valec“/„Spodný valec“. Ak sú valce asymetrické, v tabuľke priechodov/tabuľke stojanov sú viditeľné oba valce – horný aj spodný. Asymetrické valcovanie môže používateľ aktivovať zaškrtnutím políčka vedľa položky „Zobraziť všetky valce“. Ak geometria valca nie je vytvorená z dostupných základných tvarov, je dôležité venovať pozornosť údajom o priereze, strede valca, osi valca a priemere valca.

#### **Rýchlosť valcov**

Používateľ môže nastaviť rýchlosť valcovania v riadku „Rýchlosť valcovania“. Táto rýchlosť sa uplatňuje na všetky valce; ak používateľ požaduje diferencovanú rýchlosť valcovania, môže ju nastaviť na stránke „Pohyb“ príslušného objektu vo fáze „Pass“. 

####   
**Medzera medzi valcami**

„Medzera medzi valcami“ je vzdialenosť, ktorá sa používa na umiestnenie valcov pomocou ohraničujúceho obdĺžnika. Ide o vzdialenosť medzi horným a dolným valcom, ako je znázornené na obr. 43.1.22.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0022.jpg' | relative_url }})

Definícia medzery medzi valcami

  
V prípade typu „Rollset definovaný používateľom“ je potrebné valce umiestniť ručne namiesto automatického umiestnenia (metódou ohraničujúceho obdĺžnika), ako je znázornené na obr. 43.1.23. To sa hodí v prípade, ak je geometria valcov už správne umiestnená.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0023.jpg' | relative_url }})

Definícia medzery medzi valcami pre užívateľsky definovanú sadu valcov

#### **Rotácia (°)**

Používateľ môže pred spustením simulácie priechodu definovať otáčanie obrobku. Obrobok sa otočí o hodnotu zadanú v poli „Rotácia (°)“, než bude polohovaný pomocou valcov. Táto možnosť nie je k dispozícii pri prvom priechode, pri Lagrangeovom modeli so štvrtinovou symetriou ani pri modeli s polovičnou symetriou. V prípade modelu „Full“ môže používateľ zadať uhol a táto možnosť je k dispozícii pre oba typy valcovania – ALE aj Lagrangeovské, ako je znázornené na obr. 43.1.24. V prípade modelu ALE s štvrtinovou symetriou je možné otáčať iba o 90 stupňov, a to zaškrtnutím príslušného políčka, ako je znázornené na obr. 43.1.25.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0024.jpg' | relative_url }})

Striedanie medzi priechodmi pri plnom modeli

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0025.jpg' | relative_url }})

Striedanie medzi priechodmi pri štvrtinovom modeli

**Reverzné valenie (pre typ Lagrangeovho valenia)**  
Pri simulácii valcovania typu Lagrange je obrobku štandardne priradený pohyb v smere osi +X, avšak ak zaškrtneme políčko „Reverse rolling“ (Obrátené valcovanie), pohyb obrobku sa v porovnaní s predchádzajúcim priechodom obráti, čím dosiahneme pohyb obrobku tam a späť, ako je znázornené na obr. 43.1.26.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0072.jpg' | relative_url }})

Možnosť spätného valenia pre simuláciu valenia typu Lagrange.

#### **Zobraziť všetky valce (pre asymetrické valcovanie)**

Toto políčko je zaškrtnuté, ak chceme nastaviť asymetrické valcovanie. Ak je toto políčko zaškrtnuté, používateľ môže definovať odlišné drážky pre horný a dolný valec, ako je znázornené na obr. 43.1.27.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0026.jpg' | relative_url }})

Definícia asymetrického valcovania

  
**Spustenie 2,5D simulácie**  
Táto simulácia sa väčšinou používa pre typ valcovania ALE na vytvorenie počiatočného tvaru obrobku. Simulácia 2,5D poskytne informácie o približnej miere deformácie obrobku na konci valcovania. Na použitie simulácie 2,5D môže používateľ definovať počet rezov pozdĺž kontaktu medzi valcami a obrobkom a kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_2_5_d_simulation_run_button.jpg' | relative_url }}) (v roletovom menu je predvolene vybraná možnosť „From start“). Po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_2_5_d_simulation_run_button.jpg' | relative_url }}) sa spustí simulácia 2,5D a súbor so správami sa aktualizuje v priebehu simulácie. Ak chceme simuláciu 2,5D zastaviť, môžeme kliknúť na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_stop_icon.jpg' | relative_url }}) a po dokončení simulácie kliknúť na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby sme simuláciu uzavreli a zobrazenie výsledkov. 

Od verzie 14.0 môže používateľ opäť spustiť 2,5D simuláciu alebo pokračovať v simulácii vybranej z roletového menu. Po dokončení 2,5D simulácie obsahuje roletové menu všetky simulácie, ktoré sa nachádzajú v 2,5D databáze, a používateľ si môže vybrať jednu z nich, od ktorej chce pokračovať (pozri obr. 43.1.28.).

  
Zaškrtávacie políčko **Roll Forming** je užitočné pri tvárnení tenkých profilov alebo plechov, kde prevláda ohyb nad deformáciou.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0027.jpg' | relative_url }})

Súbor so správami zo simulácie počas 2,5D simulácie

Ak chcete zobraziť výsledky 2,5D simulácie, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_show_results_button.jpg' | relative_url }}). Zobrazí sa tabuľka výsledkov valcovania, ako je znázornené na obr. 43.1.29. Stavovú premennú môžeme tiež znázorniť graficky pomocou roletového menu stavových premenných a výberom príslušnej stavovej premennej. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte stránku Výsledky. Výsledky 2,5D simulácie môžete otvoriť v postprocesore kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_open_in_post_label.jpg' | relative_url }}). Vidíme, že výsledky každého priečneho rezu sú uložené postupne v jednotlivých krokoch a pre každý priechod existuje samostatná operácia. 

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0028.jpg' | relative_url }})

Výsledky 2,5D simulácie

####   
Stojanový stôl ![]({{ '/assets/icons/pre_icons/mo_stand_table_button.jpg' | relative_url }})

Prechod môže mať jeden alebo viacero stojanov. Ak má prechod viacero stojanov, používateľ môže vybrať príslušný prechod a následne kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_stand_table_button.jpg' | relative_url }}), čím otvorí okno tabuľky stojanov príslušného prechodu. V tabuľke stojanov môže používateľ pridávať alebo odstraňovať stojany pomocou tlačidiel ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}). Vzdialenosť medzi aktuálnym a predchádzajúcim stojanom je špecifikovaná v položke „Poloha X“. Používateľ môže vybrať príslušný stĺpec stojana a kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_stand_settings.._button.jpg' | relative_url }}). V tabuľke stojanov môžeme spustiť 2,5D simuláciu pre viaceré stojany, podobne ako v tabuľke priechodov (pozri obr. 43.1.30.).

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0029.jpg' | relative_url }})

Stránka s viacerými stojanmi pre Pass 1

####   
Nastavenia stojana ![]({{ '/assets/icons/pre_icons/mo_stand_settings.._button.jpg' | relative_url }})

V nastaveniach stojana môže používateľ vybrať dizajn valcov typu „Groove“ a nastaviť ich rýchlosť. V prípade ľubovoľných a používateľom definovaných valcov je možné určiť uhol valca voči susednému valcu. Zobrazujú sa tu tiež údaje o symetrii valcov, ako je znázornené na obr. 43.1.31.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0030.jpg' | relative_url }})

Stránka nastavení valcovacieho stojanu

### Stránka nastavení 3D

Na tejto stránke môže používateľ definovať nastavenia na prevod 2D priečneho rezu na 3D geometriu. Tieto nastavenia sa líšia pre typy valcovania Lagrangeov a ALE.

#### **Stránka nastavení 3D pre typ ALE Rolling**

Stránka nastavení 3D pre funkciu ALE Rolling je zobrazená na obr. 43.1.32. Používateľ môže kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) vedľa položiek „3D geometria valcov“, „3D sieť valcov“ a „3D sieť obrobku“, aby upravil príslušné nastavenia. Nastavenia 3D geometrie valcov sú znázornené na obr. 43.1.33. Možnosti 3D siete valcov sú znázornené na obr. 43.1.34. Možnosti 3D siete obrobku sú znázornené na obr. 43.1.35.

Po definovaní nastavení pre položky „3D Workpiece“ aj „3D Rolls“ môže používateľ kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button_2.jpg' | relative_url }}) na stránke 3D nastavení, čím sa vygenerujú 3D geometrie a sieť; nastavenie vyzerá tak, ako je znázornené na obr. 43.1.39.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0031.jpg' | relative_url }})

Stránka nastavenia 3D pre typ ALE Rolling

#### **Nastavenia geometrie 3D valca ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }})**

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0032.jpg' | relative_url }})

Stránka „3D geometria valca“ pre typ valcovania ALE

  * **Počet vrstiev:** Používateľ môže určiť počet vrstiev v rámci rotácie 2D priečneho rezu.

  * **Pomer veľkostí:** Ak používateľ používa jemnejšiu geometriu, tu je možné definovať pomer medzi maximálnou a minimálnou veľkosťou v oblasti s jemnejšou geometriou.

  * **Možnosť „Uniform Geometry“ (Jednotná geometria):** Ak používateľ zvolí toto začiarkavacie políčko, 3D geometria sa vygeneruje s jednotnou hrúbkou vrstvy po celom obvode 2D priečneho rezu.

  * **Jemnejšia geometria od:** Ak chce používateľ dosiahnuť jemnejšiu geometriu v kontaktnej oblasti s cieľom zvýšiť presnosť výpočtov, môže určiť počiatočný a koncový uhol tejto jemnejšej geometrie. 

**Nastavenia 3D valcovej siete ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }})**

Táto možnosť bude k dispozícii až po výbere možnosti „Obrobok a valce (neizotermické)“ na stránke procesu. Na stránke nastavení siete valcov môže používateľ definovať počet prvkov pre 2D sieť priečneho rezu, parametre 3D siete a materiál valcov. Tieto nastavenia sa uplatňujú na všetky valce. Používateľ môže tieto nastavenia upraviť v príslušnom priechode.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0073.jpg' | relative_url }})

Stránka na generovanie 3D sieťových valcov pre typ valcovania ALE

  * **Prerez**: Používateľ môže určiť požadovaný počet prvkov pre 2D sieť prierezu.

  * **Vytvorenie rovnomernej siete**: Ak používateľ zaškrtne toto políčko, 3D sieť sa vygeneruje s rovnomernou hrúbkou vrstvy po celom obvode 2D priečneho rezu.

  * **Jemnejšia sieť od** : Ak chce používateľ v oblasti kontaktu jemnejšiu sieť s cieľom zvýšiť presnosť výpočtov, môže určiť počiatočný a koncový uhol tejto jemnejšej siete.

  * **Materiál****pre****zvitky**: Materiál pre zvitky môžeme priradiť importovaním údajov o materiáloch zo súboru alebo z knižnice.

#### Nastavenia 3D obrobku ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }})

Na stránke nastavení obrobku môže používateľ určiť dĺžku obrobku, metódu vytvárania siete a nastavenia siete, ktoré sa majú použiť pri generovaní 3D tvaru.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0033.jpg' | relative_url }})

Stránka na generovanie 3D siete obrobku pre typ valcovania ALE

  * **Dĺžka obrobku:** Používateľ si môže vybrať dĺžku definovanú v „Systéme“ alebo zvoliť možnosť „Používateľ“ a podľa potreby zadať vlastnú veľkosť.

  * **Metóda vytvárania siete:** Pri valcovaní typu ALE sú k dispozícii 3 metódy vytvárania siete,

  * **Booleovská operácia:** Tvar obrobku sa vytvorí a rozdeli na sieť vykonaním booleovskej operácie v mieste kontaktu valca s obrobkom.

  * **Výsledky 2,5D:** Tvar obrobku v mieste kontaktu valca s obrobkom sa vytvorí a rozdeli na sieť na základe výsledkov 2,5D.

  * **Tenký rez:** Táto voľba sa používa pri simulácii tenkých plechov. Tvar obrobku sa vytvorí a rozdeli na sieť podobne ako pri boolovských operáciách, avšak pozdĺž hrúbky sa pridá viac vrstiev.

  * **Nastavenie hustoty 3D siete**

  * **Počet vrstiev:** Tu sa definuje počet vrstiev, ktoré sa majú použiť v smere valcovania na vytvorenie siete obrobku.

  * **Pomer veľkostí:** Ak sa pre dosiahnutie presných výsledkov používa jemnejšie sito bližšie ku kontaktnej zóne, na určenie hrúbky vrstiev sa použije pomer veľkostí. Ide o pomer medzi maximálnou a minimálnou hrúbkou vrstvy.

  * **Rovnomerná hrúbka vrstiev:** Ak chce používateľ vytvoriť obrobok s konštantnou hrúbkou vrstiev v smere valcovania, môže zvoliť túto možnosť. Sieť vytvorená s použitím možnosti „**Rovnomerná****hrúbka vrstiev**“ bude vyzerať tak, ako je znázornené na obr. 43.1.36.

  * **Jemnejšia sieť od:** Parameter „Jemnejšia sieť od“ slúži na definovanie počiatočného a koncového bodu jemnejšej siete. Hodnota sa zadáva v rozmedzí od 0 do 1, pričom 0 predstavuje začiatok obrobku a 1 koniec obrobku. Sieť obrobku vygenerovaná pomocou parametra „Jemnejšia sieť od“ vyzerá tak, ako je znázornené na obr. 43.1.37.

  * **Zóny s jemnejšou sieťou:** Pomocou tejto možnosti môže používateľ definovať rôzne zóny s odlišným počtom vrstiev v každej zóne. Východiskovou polohou je absolútna vzdialenosť, od ktorej sa vytvárajú zóny siete; štandardne je to výstupný koniec obrobku. Sieť obrobku vygenerovaná pomocou možnosti „Zóny s jemnejšou sieťou“ vyzerá tak, ako je znázornené na obr. 43.1.38.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0034.jpg' | relative_url }})

Vytvorenie siete pomocou možnosti „Jednotná hrúbka vrstiev“

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0035.jpg' | relative_url }})

Vytvorenie siete pomocou možnosti „Jemnejšia sieť od“

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0036.jpg' | relative_url }})

Vytvorenie siete pomocou možnosti „Zóny s jemnejšou sieťou“

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0037.jpg' | relative_url }})

Nastavenie 3D pre typ ALE Rolling

#### Stránka nastavení 3D pre typ Lagrangeovho valenia

Stránka nastavení 3D pre typ „Lagrangian Rolling“ je znázornená na obr. 43.1.40. Okrem nastavení „3D Roll“ a „3D Workpiece“ sú k dispozícii aj nastavenia „Pusher“, „Auto position“ a „Prevent twisting“. Po definovaní nastavení 3D obrobku, 3D valcov a posúvača kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button_2.jpg' | relative_url }}) na stránke nastavenia 3D, čím vygenerujete 3D geometrie a sieť; nastavenie vyzerá tak, ako je znázornené na obr. 43.1.44.

  * **Nastavenia 3D Roll ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}):** Tieto nastavenia sú podobné nastaveniam 3D Roll v ALE, s tým rozdielom, že tu nemáme k dispozícii možnosti na vytvorenie jemnejšej geometrie, ako je znázornené na obr. 43.1.41.

  * **Nastavenia 3D Roll siete** **![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }})**: Tieto nastavenia sú podobné nastaveniam 3D Roll siete v ALE, s tým rozdielom, že tu nie sú k dispozícii možnosti na vytvorenie jemnejšej siete, ako je znázornené na obr. 43.1.42.

  * **Nastavenia 3D obrobku** **![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }})**: Na vytvorenie siete pre obrobok pri Lagrangeovskom valcovaní môžeme použiť typ siete „Tetrahedral“ alebo „Brick“, ako je znázornené na obr. 43.1.43.

  * **Posúvač:** Používateľ môže použiť posúvač na posunutie obrobku smerom k valcom určitou rýchlosťou, aby dokončil simuláciu tvarovacieho valcovania. Ak používateľ nechce použiť posúvač, môže zvoliť možnosť „Žiadny“. Ak používateľ chce použiť posúvač, môže ho definovať takto:

  * **Objekt:** Ak je táto možnosť zvolená, vytvorí sa samostatný tuhý objekt „Pusher“, ktorého predvolená rýchlosť sa vypočíta na základe rýchlosti otáčania. Rozmery objektu a sieť je možné upraviť v nastaveniach objektu „Pusher“ vo fáze „Pass“.

  * **BCC:** Ak je táto voľba zvolená, eliminuje umelé deformácie na konci obrobku spôsobené kontaktom s posúvačom. Táto funkcia sa aktivuje prostredníctvom okrajovej podmienky posúvača na obrobku a priradí riadenie pohybu k obrobku. Rýchlosť sa vypočíta na základe rýchlosti valca a je možné ju upraviť zmenou rýchlosti obrobku na stránke „Pohyb“ v časti „Fáza prechodu“.

  * **Zabrániť krúteniu:** Ak používateľ nechce pri valcovaní modelovať krútenie obrobku, môže zaškrtnúť toto políčko, čím zabráni krúteniu. Ak je toto políčko zaškrtnuté, zabráni to otáčaniu obrobku pri Lagrangeovom valcovaní, takže obrobok zostane počas celého procesu valcovania pevne pripojený k osi x. Zaškrtnutím políčka „Zabrániť krúteniu“ sa obrobku automaticky priradí okrajová podmienka „Bez otáčania“.

  * **Automatické umiestnenie ![]({{ '/assets/icons/pre_icons/mo_auto_position_button.jpg' | relative_url }}):** Používateľ môže všetky vygenerované objekty automaticky umiestniť kliknutím na tlačidlo **![]({{ '/assets/icons/pre_icons/mo_auto_position_button.jpg' | relative_url }})**. Obrobok bude umiestnený tak, aby sa dotýkal hornej valce prvej sady valcov v smere valcovania, a posúvač bude umiestnený na zadnom konci obrobku tak, aby sa dotýkal obrobku v smere valcovania.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0038.jpg' | relative_url }})

Stránka s nastaveniami 3D pre Lagrangeov model valenia typu 3

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0039.jpg' | relative_url }})

Stránka „3D geometria valca“ pre valcovanie lagrangovského typu 

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0074.jpg' | relative_url }})

Stránka s 3D rolovacou mriežkou pre Lagrangovský typ valenia 

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0040.jpg' | relative_url }})

Stránka na generovanie 3D siete obrobku pre valcovanie lagrangovského typu

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0041.jpg' | relative_url }})

3D nastavenie pre valenie lagrangovského typu

### Ovládacie prvky simulácie

Nastavenia riadenia simulácie je možné definovať na úrovni skupiny valcovania (Rolling Group) a pomocou ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_passes_button.jpg' | relative_url }}) ich aplikovať na všetky priechody. Používateľ môže tieto nastavenia upraviť pre akýkoľvek konkrétny priechod v časti „Simulation Controls“ na úrovni priechodu; pokročilé nastavenia sú dostupné v expertnom režime na úrovni priechodu. Nastavenia riadenia simulácie pre typy valcovania ALE a Lagrangeovské sú znázornené na obr. 43.1.45. „Globálne nastavenia krokov“ sú podobné pre oba typy (ALE aj Lagrangeovské), zatiaľ čo nastavenia kritérií zastavenia sa líšia.

#### Ovládacie prvky globálnych krokov

**Počet krokov:** Počet krokov, ktoré sa majú simulovať počas každého priechodu a HT, je možné definovať na úrovni valcovacej skupiny, pričom táto hodnota sa uplatní na všetky priechody a operácie HT v rámci danej valcovacej skupiny. Ak sa simulácia zastaví na základe kritérií zastavenia skôr, ako sa dokončia definované kroky, nasledujúca operácia začne pokračovaním od predchádzajúcej operácie.

**Krok:** Hodnota kroku (STPINC), ktorá sa má uložiť do databázy, určuje počet krokov, ktoré systém uloží do databázy. Pri behu simulácie sa musí vypočítať každý krok, ale nemusí sa nutne uložiť do databázy. Uložením väčšieho počtu krokov sa zachová viac informácií o procese, čo však bude vyžadovať väčší úložný priestor.

**Čas na jeden krok:** Ak je zadaný čas na jeden krok, použije sa časový interval na jeden krok. Posun formy na jeden krok bude rovný časovému kroku vynásobenému rýchlosťou formy.

**Posun na jeden krok:** Ak je špecifikovaný posun na jeden krok, primárna matrica sa v každom časovom kroku posunie o zadanú hodnotu. Celkový posun primárnej matrice bude rovný posunu na jeden krok vynásobenému celkovým počtom krokov.

**Používateľ:** Umožní to používateľom nastaviť si vlastnú veľkosť kroku. Používateľ by mal zvoliť vhodnú veľkosť kroku tak, aby na základe počtu krokov splnil podmienku zastavenia.

**Systém:** Na základe počtu krokov automaticky vypočíta veľkosť kroku tak, aby bola splnená podmienka zastavenia.

#### Kritériá na ukončenie 

**Kritériá ukončenia simulácie ALE:** Simulácia ALE sa môže automaticky ukončiť po dosiahnutí ustáleného stavu na základe klesajúcich gradientov stavových premenných a dosiahnutia výstupnej časti pri korekciách geometrie. Toto kritérium ukončenia je možné aktivovať zaškrtnutím políčka „Skontrolovať konvergenciu ALE v ustálenom stave“ a definovaním nastavení konvergencie ALE v ustálenom stave.

**Kritérium zastavenia na základe objemovej rýchlosti**: Simulácia sa zastaví, keď pomer objemovej rýchlosti medzi vstupom a výstupom spĺňa kritériá na zastavenie.  
**ALE s reguláciou objemovej rýchlosti**: Ak je funkcia ALE s reguláciou objemovej rýchlosti zapnutá, simulácia sa bude snažiť zachovať konštantnú objemovú rýchlosť medzi výstupom a vstupom a minimalizovať rozdiel medzi objemovou rýchlosťou na vstupe a výstupe, čím sa zvýši presnosť výsledku.  
**ALE s tuhým prenosom**: Ak je zapnutá funkcia ALE s tuhým prenosom, systém identifikuje tuhé zóny a deformačné zóny podobne ako v prípade RSE a uzly v tuhej zóne sa nebudú aktualizovať, čo vo všeobecnosti skráti čas potrebný na dosiahnutie konvergencie.  
**Lagrangeovské kritériá zastavenia:** Simulácie valcovania podľa Lagrangeovej metódy je možné automaticky zastaviť v okamihu, keď sochora prejde stredom poslednej sady valcov, alebo v akejkoľvek rovine pozdĺž smeru valcovania podľa želania používateľa. Rovinu zastavenia je možné definovať v položke „Kritériá zastavenia“ zadaním súradníc na rovine zastavenia, pričom smerom valcovania je predvolene smer valcovania, ktorý sa nastaví automaticky (pozri obr. 43.1.45). Po tom, čo všetky uzly obrobku prekročia tento definovaný bod (imaginárnu rovinu), simulácia sa pre daný priechod zastaví. Tieto nastavenia je možné definovať nezávisle pre každý priechod na úrovni „Priechod“; smer valcovania +X alebo -X je možné zvoliť na základe pohybu valcov, ako je znázornené na obr. 43.1.45.

**Riešiteľ**: Nastavenia riešiteľa môžeme použiť pre všetky prechody valcovacej skupiny, ako je znázornené na obr. 43.1.45. Štandardne je zvolený riešiteľ „MUMPS“ pre simuláciu valcovania typu ALE a riešiteľ „Konjugovaný gradient“ pre simuláciu valcovania typu Lagrange.  
**Metóda iterácie**: Používateľ si môže vybrať metódu iterácie, ako je znázornené na obr. 43.1.45 – buď priamu iteráciu, alebo metódu Newton-Raphson, ktorá sa bude uplatňovať vo všetkých priechodoch valcovacej skupiny.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0042.jpg' | relative_url }})

Ovládacie prvky simulácie pre režim GUIDED

**Použiť na všetky priechody:** Ak chce používateľ prepisovať nezávislé nastavenia simulácie globálnymi nastaveniami simulácie alebo aplikovať zmeny v globálnych nastaveniach simulácie na všetky priechody, môže použiť funkciu „Použiť na všetky priechody“, ako je znázornené na obr. 43.1.45. Tým sa prepíšu nastavenia simulácie všetkých priechodov globálnymi nastaveniami simulácie. Používateľ môže tiež pre každý priechod samostatne definovať nastavenia krokov a kritériá zastavenia, ako je znázornené na obr. 43.1.46. Nastavenia definované na úrovni priechodu budú mať prednosť pred globálnymi nastaveniami simulácie.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0043.jpg' | relative_url }})

Ovládacie prvky simulácie v režime GUIDED (prevádzková úroveň)

### Vytvoriť databázu

Na stránke „Generate DB“ môžeme vidieť prehľad nastavení simulácie operácie, ako je znázornené na obr. 43.1.47.

**Kontrola údajov**![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}): Týmto sa vykoná kontrola údajov. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvoriť databázu** ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}): Kliknutím na toto tlačidlo sa vygeneruje databáza pre konfiguráciu. Ak používateľ vytvorí databázu na úrovni valcovacej skupiny, databáza sa vygeneruje od začiatku valcovacej operácie. (Pozri obr. 43.1.47.)

**Pridať súbor .key:** Akékoľvek informácie, ktoré nie sú definované v šablóne, ale stále sa vzťahujú na proces, je možné načítať ako súbor .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt – tieto hodnoty je možné definovať v súbore .key a uložiť do zadaného adresára. V prípade potreby je možné zmeniť len hodnoty v súbore .key a simuláciu znovu spustiť, aby sa preskúmal vplyv zmeny parametrov.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0044.jpg' | relative_url }})

Vytvoriť stránku databázy

## Úroveň valcovania tvaru

Po dokončení definície údajov na globálnej úrovni a na úrovni „Rolling Group“ môže používateľ v editore operácií vybrať priechod a vykonať zmeny v príslušnom priechode. Po výbere priechodu sa v priestore editora vlastností otvorí stránka „Tabuľka stojanov“. Používateľ môže pridávať tabuľky, pridávať/odstraňovať stojany v tabuľke stojanov na úrovni priechodu; táto tabuľka stojanov je dostupná aj z tabuľky priechodov (pozri obr. 43.1.48). Kritériá pre tvorbu novej siete a pokročilé nastavenia pomocou expertného režimu sú dostupné iba na úrovni priechodu. Strom operácií na úrovni valcovacieho priechodu pre Lagrangovské valcovanie a ALE valcovanie vyzerá tak, ako je znázornené na obr. 43.1.48.

V moduloch ALE a Lagrangian Rolling Pass môže používateľ definovať alebo upravovať nasledujúce údaje pre príslušné objekty:  
**Obrobok:** Typ objektu (pre tvarové valcovanie sa uprednostňuje plastický/elastoplastický typ), geometria, nastavenia siete, materiál, okrajové podmienky, riadenie pohybu, počiatočné hodnoty stavových premenných (teplota, deformácia… atď.) a vstavaná sieť Flownet.

**Valce:** Typ objektu (pre tvarovanie valcov sa odporúča typ „Tuhý/Pružný“), geometria, nastavenia siete, materiál, okrajové podmienky a ovládacie prvky pohybu.

**Pusher** (typ Lagrangeovho valcovania): Typ objektu (pre valcovanie tvarov sa odporúča typ „Rigid“), geometria, nastavenia siete, materiál, okrajové podmienky a ovládacie prvky pohybu.

**Tabuľka/príručka** (typ valcovania podľa Lagrangea): Typ objektu (pre tvarové valcovanie sa odporúča typ „tuhý“), geometria, nastavenia siete, materiál a okrajové podmienky.

Okrem uvedených údajov môže používateľ nastaviť polohovanie medzi jednotlivými priechodmi, upravovať údaje medzi objektmi a nastavenia simulácie.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0045.jpg' | relative_url }})

Strom operácií na úrovni Rolling Pass

### Stojanový stôl

Keď používateľ otvorí úroveň „Pass“ pre daný Pass, otvorí sa stránka „Tabuľka porastov“. Používateľ môže pridať viacero stojanov, ak má priechod viac ako jeden stojan (pozri obr. 43.1.49.), údaje pre každý stojan je možné definovať pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_stand_settings.._button.jpg' | relative_url }}) (ďalšie podrobnosti o „Nastaveniach stojanov“ nájdete v časti Nastavenia stojanov na úrovni valcovacej skupiny). Definovanie typu súpravy valcov, geometrie drážky valcov, rýchlosti valcov a medzery medzi valcami v „Tabuľke stánkov“ je podobné ako v tabuľke priechodov.   
V tabuľke „Stand Table“ má používateľ možnosť zvoliť, či sa v príslušnom stojane má použiť stôl/vodiaca lišta (pozri obr. 43.1.49.); stojan môže mať „Table Front“ (na výstupnej strane) a „Table Back“ (na vstupnej strane) alebo len jednu z nich. Používateľ môže vybrať ľubovoľný stojan a stôl (pozri obr. 43.1.50.) a definovať ich údaje pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_define_button2.jpg' | relative_url }}) v hornej časti tabuľky stojanov, ako je znázornené na obr. 43.1.50. Ďalšie podrobnosti o definícii stola nájdete v časti Geometria stola. 

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0046.jpg' | relative_url }})

Stránka so zoznamom stolov (prevádzková úroveň)

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0047.jpg' | relative_url }})

Definovanie geometrie stola na stránke „Stand table“ (úroveň operácie)

### Stránka s valcami

Na tejto stránke sa zobrazujú údaje o zozname pre príslušné vybrané pracovisko, ako je znázornené na obr. 43.1.51; pozri nastavenia pracoviska na úrovni skupiny zoznamov.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0048.jpg' | relative_url }})

Valcovacia stolica – 1 strana (prevádzková úroveň)

#### Stránka „Geometria valca“

Na tejto stránke môže používateľ definovať alebo zmeniť nastavenia geometrie, ktorá sa generuje na stránke „3D Setup“. Používateľ má k dispozícii nastavenia geometrie v režime s návodom aj v expertnom režime (ako je znázornené na obr. 43.1.52 a obr. 43.1.53). Pokiaľ ide o pokročilé nastavenia geometrie, ktoré sú k dispozícii v expertnom režime, pozrite si časť Nastavenie 3D geometrie.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0049.jpg' | relative_url }})

Stránka s geometriou valca v režime GUIDED (prevádzková úroveň)

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0050.jpg' | relative_url }})

Stránka „Geometria valca“ v režime EXPERT (prevádzková úroveň)

#### 

#### Stránka s roletovou sieťou

Na prevádzkovej úrovni môžeme vygenerovať sieť valcov. Keď otvoríme stránku so sieťou valcov, štandardne je vybraný typ siete „Brick“, ako je znázornené na obr. 43.1.54. Ďalšie informácie nájdete v dokumentoch [13.2. 3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/) a [13.3. 3D Brick Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/). Lagrangeov typ valcovania je možné nastaviť pomocou mriežky typu „Brick“ aj „Tetrahedral“, zatiaľ čo typ valcovania ALE je možné nastaviť iba pomocou mriežky typu „Brick“.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0051.jpg' | relative_url }})

Stránka „Roll Mesh“ (prevádzková úroveň)

#### Stránka „Pohyb valca“

Pohyb okolo osi naklonu je možné definovať v režime s vedením aj v režime pre pokročilých. V režime s vedením môže používateľ definovať pohyb okolo osi naklonu ako uhlovú rýchlosť alebo krútiaci moment. Pohyb môže byť konštantný, závislý od času alebo závislý od uhla, ako je znázornené na obr. 43.1.55.  
Váleček môže byť odpružený; v takom prípade môže používateľ zaškrtnúť políčko „Odpružený“ a nastaviť tuhosť (môže byť konštantná alebo funkciou posunutia), predpätie, aktuálne posunutie a maximálne posunutie, ako je znázornené na obr. 43.1.56.  
Ak chce používateľ nastaviť akékoľvek pokročilé ovládacie prvky pohybu, môže tak urobiť prostredníctvom nastavení v režime Expert, ako je znázornené na obr. 43.1.57. Ďalšie informácie o týchto nastaveniach nájdete v [15\. Movement Controls Settings](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/). 

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0052.jpg' | relative_url }})

Ovládacie prvky pohybu valcov v režime GUIDED

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0053.jpg' | relative_url }})

Definovanie údajov o pohybe s pružinovým pohonom v režime GUIDED

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0054.jpg' | relative_url }})

Ovládacie prvky pohybu valcov v režime EXPERT

### Stránka s geometriou tabuľky/príručky

Používateľ môže pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) definovať geometriu stola/vodítka pomocou základných prvkov. Po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) sa otvorí okno na definovanie základných prvkov stola/vodítka, ako je znázornené na obr. 43.1.58.

  
Používateľ môže definovať parametre tabuľky/vodítka a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) vygenerovať tabuľku/vodítko. Používateľ môže namiesto tabuľky definovať vodítko tak, že zaškrtne políčko „Definovať tabuľku ako vodítko pre valcovanie asymetrických tvarov“, ako je znázornené na obr. 43.1.59.  
**Počiatočný bod:** V prípade stola ide o súradnicu ľavého dolného rohu priečneho rezu Table2D (pozri obr. 43.1.58) a v prípade vodítka o stredový bod polomeru vnútorného ľavého rohu (pozri obr. 43.1.59).

**Parametre stola/vodidla:** Tu je možné nastaviť šírku (W), výšku (H) a dĺžku stola/vodidla.

**Hrúbka vodítka (T):** Tu je možné zadať hrúbku vodítka.

**Polomer rohu vodítka (ak je uvedený):** Tu je možné zadať polomer rohu vodítka.

**Polohovanie/Pass Line:** Stôl je možné zarovnať s valcom nastavením hodnoty „Pass line (PL)“ po zaškrtnutí políčka „Zarovnať k hornej alebo spodnej hrane valca pri valcovaní pásu“, pozri obr. 43.1.58. Stôl sa posunie nadol od hornej plochy spodného valca o hodnotu „Pass line“ a následne sa nastaví poloha s ohľadom na kolíziu v smere +X (pre zadný stôl) / -X (pre predný stôl).

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0055.jpg' | relative_url }})

Definícia základných geometrických prvkov tabuľky

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0056.jpg' | relative_url }})

Príručka – Definícia geometrických primitív

### Stránka objektu obrobku

Používateľ môže zadať názov objektu, teplotu a typ objektu (ako je znázornené na obr. 43.1.60.). Predvolene je vybraný typ [Plastic object type](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic); ak chce používateľ zohľadniť vplyv elastických vlastností, môže použiť typ objektu [Elasto-plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic). 

V prípade Lagrangeovho valcovania môžeme v prvom kroku importovať 3D objekt obrobku pomocou volieb ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). Ak sa objekt „Workpiece“ importuje zo súboru, nastavenia siete budú také, ako je znázornené na obr. 43.1.61, čo je podobné stránke siete pre operáciu tvárnenia.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0057.jpg' | relative_url }})

Stránka objektu obrobku

#### Sieť obrobku 

Nastavenia siete obrobku sú podobné nastaveniam siete na stránke 3D nastavenia v časti „Generovanie siete obrobku“ na úrovni skupiny valcovania. Podrobnosti o nastaveniach siete nájdete na stránke 3D nastavenia. V prípade Lagrangeovho nastavenia, ak importujeme objekt alebo geometriu obrobku, zobrazí sa stránka „Všeobecná sieť“ na generovanie 3D siete obrobku, ako je znázornené na obr. 43.1.61. Ďalšie informácie o tejto stránke „Sieť“ nájdete v dokumentácii [13.2. 3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/) a [13.3. 3D Brick Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/).

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0077.jpg' | relative_url }})

Všeobecná sieť obrobku pre importovaný objekt alebo geometriu.

  
**Vynútené prepočítanie siete medzi jednotlivými priechodmi pri type ALE „Rolling“**

Od druhého priechodu môže používateľ na stránke „Sieť obrobku“ zaškrtnúť políčko „Vynútiť prepočítanie siete“ a v časti „Vytvorenie siete medzi priechodmi“ nastaviť počet prvkov, čím sa pred začiatkom simulácie priechodu vygeneruje nová sieť (pozri obr. 43.1.62).  
**Sieť prierezov vstupu z poslednej operácie:**  
„Prerez pri výstupe“ alebo „Prerez pri poslednom kontakte valca“ z poslednej operácie možno použiť ako vstupný 2D prerez pre aktuálny priechod a na vytvorenie 3D siete ALE pre následné valcovanie.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0058.jpg' | relative_url }})

Stránka siete obrobku ALE pre druhý priechod

  
**Prepočítanie siete medzi iteráciami pri metóde typu Lagrangeovho valenia**

V režime Lagrangeovho valenia môže používateľ okrem funkcie „Force remeshing“ vykonať aj niektoré ďalšie akcie, ako je znázornené na obr. 43.1.63.

**Vynútené prepočítanie siete:** Ak je toto políčko zaškrtnuté, pred spustením simulácie priebehu sa vygeneruje nová sieť so zadaným počtom prvkov. V prípade mriežkovej siete definujeme cieľové prvky 2D priečneho rezu a v prípade tetraedrickej siete definujeme cieľové prvky 3D siete obrobku.

**Axiálne rozdelenie:** Zaškrtnutím tohto políčka je možné hrúbku vrstvy v novej sieti pozdĺž smeru valenia ovládať pomocou hodnoty axiálneho rozdelenia, a to buď pomocou absolútnej dĺžky, alebo pomeru strán.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0059.jpg' | relative_url }})

Stránka so sieťou obrobku v Lagrangeovom formulácii pre druhý prechod

  
**Postup na vyrovnanie obrobku s osou X:** Ak sa os obrobku posunie od osi X, os obrobku sa vyrovná s osou X.

**Booleovská hodnota medzi prechodmi**

Od druhého priechodu môže používateľ vykonávať boolovské operácie na odstránenie prebytočného materiálu a riadiť oblasti záujmu a veľkosť modelu v priebehu viacerých priechodov v typickom procese prechodného valcovania. Pri Lagrangeovom postupe sa dĺžka polotovaru alebo obrobku zvyšuje pri prechode z jedného priechodu do druhého. Systém sietí použitý v počiatočných priechodoch môže čoskoro stratiť účinnosť pri spracovaní kontaktných podmienok v nasledujúcich priechodoch v dôsledku natiahnutia prvkov v deformovanej oblasti. Jemnejšia sieť od začiatku priechodov by mohla byť výpočtovo náročnejšia. Pomocou tejto booleovskej operácie môže používateľ vybrať oblasť záujmu v smere valcovania a pravidelne odstraňovať obrobok, ktorý sa počas procesu valcovania natiahne za túto oblasť. Napríklad, ak nie je potrebné modelovať koncové efekty, môže používateľ po stanovenom počte priechodov orezať koncové oblasti, pričom zachová dobrý popis kontaktu a toku materiálu s veľkosťou modelu, ktorá je výpočtovo efektívna. To je možné vykonať pomocou rôznych dostupných možností uvedených nižšie (obr. 43.1.64.).  
Hodnoty S1 a S2 možno nastaviť v rozmedzí od 0 do 1, pričom S1 predstavuje prednú časť a S2 zadnú časť – hodnota 0 označuje prednú časť a hodnota 1 zadnú časť. Keď je S1 „0“, zachová sa mriežka prednej časti a keď je S2 „1“, zachová sa mriežka zadnej časti.  
V prípade typu tehlovej siete sa vygeneruje nová sieť na základe výberu na karte „Možnosti“,  
0 – Zachovať pôvodnú sieť medzi S1 a S2  
1 – Premietnite uzly na prednej a zadnej strane do roviny  
2 – Vyrovnajte axiálnu polohu, aby ste mohli odobrať vzorky z uzlov.  
3 – Určite axiálne polohy pre odber vzoriek z uzlov.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0060.jpg' | relative_url }})

Možnosť „Boolean Between Passes“ pre sieť birck

Od verzie v14 je možné pridať boolovskú operáciu medzi prechodmi aj v prípade obrobku s Tet-sieťou (obr. 43.1.65).

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0076.jpg' | relative_url }})

Možnosť „Boolean medzi prechodmi“ pre tetraedrickú sieť

#### Obrobok BCC 

**Pre typ ALE s posuvným mechanizmom**  
Používateľ môže v závislosti od požiadaviek procesu definovať údaje BCC týkajúce sa symetrie, deformácie, tepelného správania a difúzie. Pre typ valcovania ALE je potrebné definovať počiatočnú plochu (vstupný koniec) a voľnú plochu (výstupný koniec). Predvolene sú údaje BCC pre počiatočnú plochu a voľnú plochu priradené v rámci deformácie pre modely ALE, pozri obr. 43.1.66.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0061.jpg' | relative_url }})

Počiatočná plocha BCC pre typ valcovania ALE

**Pre typ s Lagrangeovým valením**  
Používateľ môže v závislosti od požiadaviek procesu definovať údaje o symetrii, deformácii, tepelnej vodivosti a difúzii pre BCC. Pre lagrangovský typ valcovania sú k dispozícii možnosti „Pusher“ a „No rotation“ v časti Deformácia -> Valcovanie, ako je znázornené na obr. 43.1. 67.

**BCC bez otáčania:** Táto BCC sa priradí, keď na stránke „3D Setup“ zaškrtneme políčko „Prevent twisting“ (Zabrániť krúteniu), ako je znázornené na obr. 43.1.68. Zabraňuje otáčaniu obrobku pri Lagrangeovom valcovaní, takže obrobok zostáva počas celého procesu valcovania pevne pripevnený k osi x.

**BCC „Pusher“:** Tento BCC sa priradí, keď na stránke 3D nastavení definujeme „Pusher“ ako BCC, ako je znázornené na obr. 43.1.69. Ak je priradený tento BCC, musí mať obrobok definované ovládacie prvky pohybu. Pri Lagrangeovom type valcovania sa rýchlosť automaticky vypočíta na základe rýchlosti valcov a priradí sa k obrobku; používateľ môže túto hodnotu v prípade potreby upraviť. 

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0062.jpg' | relative_url }})

BCC typu „Rolling“ pre Lagrangov typ „Rolling“

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0063.jpg' | relative_url }})

Typ bez rotácie – valcovanie BCC

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0064.jpg' | relative_url }})

Valcovací stroj typu „Pusher“ BCC

#### Pohyb obrobku 

Pri valcovaní typu Lagrange bude pohyb obrobku definovaný automaticky, ak je posúvač nastavený na BCC, a používateľ môže túto hodnotu upraviť na základe rýchlosti valcov; v prípade potreby ju môže zmeniť na stránke „Pohyb“, ako je znázornené na obr. 43.1.70. Pre typ valcovania ALE nie je potrebné definovať žiadne riadenie pohybu.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0065.jpg' | relative_url }})

Stránka o pohybe obrobku pre posúvač typu BCC

#### Inicializácia obrobku 

V okne „Initialize“ sú na inicializáciu k dispozícii niektoré bežne používané stavové premenné, ako sú teplota, deformácia, napätie, poškodenie, rýchlosť, posun, hustota, veľkosť zŕn mikrostruktúry a veľkosť častíc. Ak chce používateľ pri valcovaní s viacerými priechodmi inicializovať teplotu, deformáciu alebo veľkosť zŕn, môže využiť túto stránku na inicializáciu.  
Používateľ môže inicializovať hodnoty týchto stavových premenných tak, že ich zadá do príslušného poľa a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). Obr. 43.1.71. znázorňuje rôzne stavové premenné, ktoré sú k dispozícii v okne „Initialize“. V závislosti od typu stavovej premennej ich môže používateľ inicializovať aj z dátových okien uzlov a prvkov. Ďalšie informácie o tom, ako inicializovať stavové premenné v oknách „Node“ a „Element“, nájdete v [17.1. Node Data Window](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) a [17.2. Element Data Window](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/).

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0066.jpg' | relative_url }})

Inicializovať stránku

#### Obrobok s integrovanou sieťou Flownet 

Nastavenia valcovania s viacerými priechodmi zvyčajne generujú databázy s veľkým počtom krokov, a preto vykreslenie siete Flownet bude trvať dlho. Tento problém môže používateľ vyriešiť využitím funkcie „Built-in-Flownet“. Pri použití funkcie „Built-in-Flownet“ sa graf Flownet vypočíta priebežne počas simulácie problému. Ďalšie informácie nájdete v [Built in Flownet.](../../pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation.htm#13_2_9_Built_In_Flownet).

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0067.jpg' | relative_url }})

Vstavaná stránka Flownet

### Polohovanie 

Po kliknutí na tlačidlo „Auto position ![]({{ '/assets/icons/pre_icons/mo_auto_position_button.jpg' | relative_url }})“ na stránke 3D nastavení alebo na tlačidlo „Automatic Position ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }})“ na stránke polohovania sa všetky valce, obrobok a posúvače automaticky nastavia do správnej polohy. Ak chce používateľ zmeniť polohu niektorého z týchto objektov, môže použiť tlačidlo „Position objects“ na stránke polohovania. Na umiestnenie objektov sú k dispozícii rôzne možnosti polohovania, ako je znázornené na obr. 43.1.73. Ďalšie informácie o týchto možnostiach nájdete v časti [19\. Object positioning.](/docs/en/pre_processor/19_object_positioning/19_object_positioning/).

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0068.jpg' | relative_url }})

Možnosti umiestnenia objektov

### Plánované umiestnenie 

Ak si používateľ nie je istý polohou objektu, ako je to v prípade objektov typu „Čítanie z databázy“, naplánované polohovanie pomôže objekty presne umiestniť. Naplánované polohovanie umožňuje používateľovi definovať polohu objektov v nastaveniach integrovaného výrobného procesu pre nasledujúce operácie, pre ktoré sa databáza nevytvára, tak, aby boli objekty umiestnené ešte pred vytvorením databázy počas spustenia simulácie v dávkovom režime.

V programe Shape Rolling systém automaticky určí polohu v pláne pre operáciu 2. valcovacieho priechodu po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_auto_position_button.jpg' | relative_url }}) na stránke 3D Setup, ako je znázornené na obr. 43.1.74.

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0069.jpg' | relative_url }})

Stránka s plánovaným umiestnením

### Kontakt

Používateľ môže definovať kontakt medzi obrobkom a ostatnými valcovými objektmi tak, že stanoví vzťahy medzi objektmi, ako je znázornené na obr. 43.1.75. Globálna hodnota trenia definovaná na stránke Proces sa automaticky priradí a používateľ môže túto hodnotu prispôsobiť na stránke kontaktu na úrovni priechodu. Používateľ musí definovať koeficient trenia a koeficient prenosu tepla cez rozhranie pre neizotermické procesy valcovania a hodnotu trenia pre izotermický proces valcovania.

**Systém:** Po výbere tohto rádio tlačidla systém priradí predvolené vzťahy medzi objektmi. Okrem toho môže používateľ v prípade potreby pridať mazivá tak, že z roletového menu vyberie možnosť „Pridať nové“ a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button_2.jpg' | relative_url }}), alebo môže na účely simulácie načítať požadované mazivá z knižnice.

**Používateľ:** Pri operácii valcovania tvaru je štandardne zaškrtnuté tlačidlo „Používateľ“. Používateľ môže pridať vzťahy kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}), ako je znázornené na obr. 43.1.75. Používateľ môže upraviť hodnotu každého vzťahu tak, že ho vyberie a klikne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môže používateľ priradiť rovnaké hodnoty všetkým vzťahom. Kliknutím na tlačidlo môže používateľ vypočítať toleranciu kontaktu. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) môže používateľ vygenerovať kontaktný vzťah. Zaškrtnutím políčka vedľa kontaktného vzťahu môže používateľ definovať zotrvávací kontakt. Ďalšie informácie nájdete v časti [20.Inter-Object Relations](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/).

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0070.jpg' | relative_url }})

Stránka s kontaktnými údajmi

### Ovládacie prvky simulácie

Nastavenia ovládacích prvkov simulácie na úrovni priechodu sú podobné ako na úrovni valcovacej skupiny; pozri časť „Ovládacie prvky simulácie vo valcovacej skupine“. Ovládacie prvky simulácie definované na úrovni valcovacej skupiny sa automaticky uplatnia na úroveň priechodu po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_passes_button.jpg' | relative_url }}); používateľ môže tieto nastavenia upraviť pre každý priechod. Ak chce používateľ na úrovni jednotlivých priechodov využiť pokročilé nastavenia simulácie, musí zvoliť expertný režim, ako je znázornené na obr. 43.1.76. Pokiaľ ide o pokročilé nastavenia simulácie, pozri [9\. Simulation controls.](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

![]({{ '/assets/images/operation_templates/43_shape_rolling/43_1_shape_rolling_manual/image0071.jpg' | relative_url }})

Ovládacie prvky simulácie v expertnom režime (prevádzková úroveň)

### Vytvoriť databázu

Používateľ môže vytvoriť databázu na úrovni jednotlivého priechodu, ak ide o prvý priechod, alebo ak je v prípade viacpriechodového valcovania dokončená simulácia predchádzajúcich priechodov.

**Súvisiace témy:**

[43\. Introduction to Shape Rolling operation](/docs/en/operation_templates/43_shape_rolling/43_introduction_to_shape_rolling/)
