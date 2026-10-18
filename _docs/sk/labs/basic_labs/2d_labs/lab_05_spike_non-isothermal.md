---
lang: sk
title: "Laboratórna úloha č. 05: Neizotermické pridávanie vzorky"
---

# Laboratórna úloha 05: Neizotermický nárast teploty

5.1. Vytvorenie nového problému

5.2. Pridanie operácie

5.3. Výber typu geometrie

5.4. Vkladanie obrobkov a foriem

5.5. Pridávanie objektov

5.6. Nastavenie obrobku

5.7. Nastavenie hornej matrice

5.8. Nastavenie spodnej matrice

5.9. Ovládacie prvky na nastavenie polohy

5.10. Vytváranie kontaktov medzi objektmi

5.11. Krok

5.12. Vytvorenie databázy

5.13. Spustenie simulácie

5.14. Následné spracovanie výsledkov

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené na obr. L5.1 nižšie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno grafického rozhrania programu DEFORM

Nový problém vytvoríte buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. L5.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Názov úlohy zadajte ako „******Spike_Nonisothermal**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), čím otvoríte nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt (pozri obr. L5.3.), v tomto momente bude používateľ vyzvaný, aby zadal názov projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názov tejto relácie. V tejto relácii použijeme ako názov projektu „**Spike_Nonisothermal**“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0001.jpg' | relative_url }})

Vyskakovacie okno „Nový projekt“ s oknom MO

Používateľ môže tiež zmeniť systém jednotiek (systém jednotiek vybraný v ponuke Súbor sa nastaví ako predvolený) a pridať operáciu výberom z roletového zoznamu „Prvá operácia“ a zaškrtnutím príslušného políčka (pozri obr. L5.4.), v tomto cvičení pridáme operáciu 2D Forming zo zoznamu operácií v Průzkumníku, preto nezatrhávajte políčko „Prvá operácia“ a v dialógovom okne „Nový projekt“ nezatrhávajte operáciu „2D Forming“. Pomocou možnosti Kopírovať existujúci projekt môžeme importovať predtým uložené projekty ako nový projekt. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0002.jpg' | relative_url }})

Výber prvej operácie v dialógovom okne Nový projekt

## Pridanie operácie

Po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) sa otvorí sprievodca viacerými operáciami, v ktorom môžete nastaviť úlohu. Pridajte operáciu 2D tvárnenia zo zoznamu operácií v prehliadači. Operáciu môžete pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie 2D tvárnenia alebo ju môžete pridať aj pretiahnutím do oblasti Editoru operácií. (Pozri obr. L5.5.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0003.jpg' | relative_url }})

Pridať operáciu 2D tvárnenia do editora operácií

## Výber typu geometrie

V tomto laboratórnom cvičení používame osovo symetrické geometrie, preto v položke „Typ geometrie“ (obr. L5.6.) vyberte voľbu **2D osovo symetrická** a potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Materiál“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0004.jpg' | relative_url }})

Výber typu osovo-symetrickej geometrie

## Vkladanie obrobkov a foriem

V okne Zoznam materiálov načítajte materiál **AISI-1025[1800-2200F(1000-1200C)]** z knižnice materiálov DEFORM, z **kategórie Oceľ** pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice) a načítajte materiál **AISI-H-13** z kategórie **Die_material**. To môžete urobiť tak, ako je znázornené na obr. L5.7 nižšie, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0005.jpg' | relative_url }})

Okno knižnice materiálov

Materiál je možné priradiť aj zo zoznamu materiálov v prehliadači kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) vedľa položky AISI-1025[1800-2200F(1000-1200C)], prípadne ho môže používateľ pridať aj pretiahnutím a umiestnením do oblasti zoznamu materiálov, ako je znázornené na obr. L5.8. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno objektu.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0006.jpg' | relative_url }})

Zoznam materiálov pre Explorer

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0007.jpg' | relative_url }})

Okno „Materiál“

## Pridávanie objektov

Ak v okne „Objekty“ ešte nie sú tri objekty, pridajte ich kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}). Tieto tri objekty budú pomenované ako „Obrobok“, „Horná matrica“ a „Spodná matrica“. (Pozri obr. L5.10.), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0008.jpg' | relative_url }})

Okno objektu 

## Upevnenie obrobku

V okne „Workpiece“ (Obrobok) zmeňte názov objektu na **Billet**, nastavte počiatočnú teplotu polotovaru na **1800°** F a ako typ objektu vyberte **Plastic**, ako je znázornené na obr. L5.11. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})..

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0009.jpg' | relative_url }})

Objekt „Billet“ – Okno

### Načítanie geometrie polotovaru

V okne Geometria načítajte súbor geometrie **Spike_Billet.IGS** z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) alebo ho môžete importovať aj pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru), ako je znázornené na obr. L5.12. Geometria sa nachádza v inštalačnom priečinku DEFORM v adresári \2D\Labs.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0010.jpg' | relative_url }})

Okno „Geometria polotovaru“

V predvolenom nastavení by mala byť zaškrtnutá voľba ![]({{ '/assets/icons/pre_icons/mo_show_geometry_inside_mark_radio_button.jpg' | relative_url }}) a malo by byť viditeľné tieňovanie určujúce orientáciu geometrie. Ak je objekt správne orientovaný (body usporiadané proti smeru hodinových ručičiek), tieňovanie sa zobrazí na vnútornej strane objektu.

Body, ktoré definujú túto importovanú geometriu, je možné zobraziť alebo upraviť kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}). Po načítaní súborov .IGS sa údaje importujú do programu DEFORM vo formáte Line-Arc, ktorý definuje geometriu pomocou čiar a oblúkov. Ak chcete zobraziť formát XYR geometrie, kliknite na tlačidlo **XYR**. (Pozri obr. L5.13.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0011.jpg' | relative_url }})

Geometrické údaje

Pri každom importe geometrie by sa táto mala skontrolovať. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}). Tým sa nielen odstránia prípadné problémy s geometriou, ale v prípade potreby sa aj opraví jej orientácia. Všimnite si, ako kontrola tejto geometrie zmenila orientáciu z hodinového smeru na protismer, čo je správne – pozri obr. L5.14.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0014.jpg' | relative_url }})

Skontrolujte a opravte geometriu

### Vytvorenie siete pre sochársky blok

Prepnite do režimu Expert kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Prepnúť do režimu Expert) na paneli nástrojov. Režim Expert ponúka viac možností pre podrobné nastavenia.

Radi by sme na polotovar umiestnili počiatočnú sieť s väčším počtom prvkov v pravom hornom rohu, kde spočiatku dôjde k najväčšej deformácii. To môžete urobiť buď pomocou okien siete, alebo pomocou užívateľsky definovaných hodnôt siete. V rámci tohto cvičenia použijeme užívateľsky definované hodnoty na umiestnenie počiatočnej siete na polotovar. 

Na stránke „Mesh“ aktivujte ![]({{ '/assets/icons/pre_icons/mo_user_defined_radio_button.jpg' | relative_url }}) na stránke „Geometry“. Chceme, aby pravý horný roh polotovaru mal sieť, ktorá je štyrikrát jemnejšia ako sieť v ostatných troch rohoch. Na dosiahnutie tohto cieľa priradíme pravému hornému rohu veľkosť oka 1 a ostatným rohom veľkosť oka 4.

Nastavte veľkosť prvku na 1 a kliknite na pravý horný roh polotovaru, potom nastavte veľkosť prvku na 4 a kliknite na ostatné tri rohy. Nastavte **počet prvkov** na **400** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Vytvorená sieť by mala vyzerať tak, ako je znázornené na obr. L5.15. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0012.jpg' | relative_url }})

Okno z mriežky z hliníkového bloku

Na definovanie počiatočnej siete používame užívateľsky definovanú sieť. Pri použití týchto užívateľsky definovaných hodnôt sa váhové faktory nezohľadňujú. Užívateľsky definované hodnoty sa však dajú použiť len na definovanie počiatočnej siete. Ak je počas simulácie potrebné pregenerovanie siete, na definovanie novej siete sa použijú váhové faktory.

Chceme nastaviť ešte jeden parameter súvisiaci s vytváraním siete. Existuje niekoľko kritérií, ktoré počas simulácie spustia prepočítanie siete polotovaru. Jedným z nich je tzv. „hlbka kolízie“, čo je vzdialenosť, do ktorej môže nástroj preniknúť do obrobku.

Vhodnou hodnotou pre hĺbku interferencie je približne jedna tretina najmenšej veľkosti prvku deformovaného objektu. Zväčšite pravý horný roh polotovaru pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) a potom pomocou ![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) zmerajte dĺžku hrany malého prvku. Hodnota pre **Hĺbku interferencie** bude približne 0,038 / 3 = **0,013** a mala by sa nastaviť na karte Kritériá pregenerovania siete. (Pozri obr. L5.16.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0013.jpg' | relative_url }})

Okno s kritériami pre výpočet novej siete

### Zadanie materiálu obrobku

Na priradenie materiálu k obrobku vyberte v okne materiálov materiál **AISI-1025[1800-2200F(1000-1200C)]**. Postupujte podľa obrázku L5.17. nižšie a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0014.jpg' | relative_url }})

Priradenie materiálu na výkovky

### Obrobok BCC

Na stránke BCC zaškrtnite predvolene priradenú BCC „Deformácia“ pre ľavú stranu obrobku v smere osi X a BCC „Výmena tepla s okolím“ pre celý vonkajší povrch sochory (čo nezahŕňa stredovú os, keďže tieto uzly sa nachádzajú vnútri objektu). Ak nie je BCC priradené, priraďte ho ručne podľa obrázkov L5.18 a L5.19. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Top Die“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0015.jpg' | relative_url }})

Nastavená rýchlosť BCC pre obrobok

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0016.jpg' | relative_url }})

Priradená výmena tepla s prostredím BCC pre obrobok

## Nastavenie hornej matrice

Na stránke „Top die“ (pozri obr. L5.20.) vyberte ako typ objektu **Rigid** a nastavte **teplotu** objektu na **300** °F, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0017.jpg' | relative_url }})

Na začiatok stránky

###  Načítavanie geometrie hornej matrice

V okne Geometria načítajte súbor geometrie **Spike_TopDie.IGS** z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) alebo ho môžete importovať aj pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru), ako je znázornené na obr. L5.21.Geometria sa nachádza v inštalačnom priečinku DEFORM v adresári \2D\Labs. Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0010.jpg' | relative_url }})

Hlavná stránka „Geometria lisovacích foriem“

### Vytvorenie siete pre hornú matricu

Nastavte **počet prvkov** na **250** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Váhové faktory sa použijú na rozdelenie týchto 250 prvkov. Predvolené nastavenie kladie veľký dôraz na zakrivenie povrchu. Všimnite si, že zakrivená časť formy má menšie prvky ako rovné časti. (Pozri obr. L5.22.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0018.jpg' | relative_url }})

Hlavná stránka „Die mesh“

### Priradiť materiál pre hornú matricu

Pre hornú matricu priraďte materiál **AISI-H-13** tak, že v zozname materiálov vyberiete položku **AISI-H-13**, ako je znázornené na obr. L5.23., a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0019.jpg' | relative_url }})

Priradenie materiálu hornej matrice zo zoznamu materiálov

### Top Die BCC

Skontrolujte predvolené priradenie BCC „Heat exchange with Environment“ pre hornú maticu a uistite sa, že je toto predvolené priradenie BCC „Heat exchange with Environment“ priradené k celému vonkajšiemu povrchu hornej matice (pozri obr. L5.24.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0020.jpg' | relative_url }})

Na začiatok stránky BCC

### Priradiť pohyb k hornej kocky

Nastavte **rýchlosť** **2** **palce za sekundu** v smere **Y** (pozri obr. L5.25.). Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Bottom die“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0021.jpg' | relative_url }})

Hlavná stránka „Pohyb matrice“

##  Nastavenie spodnej matrice

Na stránke „Bottom die“ (pozri obr. L5.26.) vyberte ako typ objektu **Rigid** a nastavte teplotu objektu na **300** °F, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0022.jpg' | relative_url }})

Stránka spodnej matrice

### Načítavanie geometrie spodnej matrice

V okne Geometria načítajte súbor geometrie **Spike_BottomDie.IGS** z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) alebo ho môžete importovať aj pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru). Geometria sa nachádza v inštalačnom priečinku DEFORM v adresári \2D\Labs. Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vytvorenie siete pre spodnú formu

Nastavte **počet prvkov** na **250** a pri predvolených nastaveniach siete vygenerujte sieť kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) (pozri obr. L5.27.). Následne kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0023.jpg' | relative_url }})

Stránka so sieťovinou spodnej matrice

### Priradiť materiál pre spodnú formu

Pre spodnú matricu nastavte materiál **AISI-H-13** tak, že v zozname materiálov vyberiete AISI-H-13, ako je znázornené na obr. L5.28., a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0019.jpg' | relative_url }})

Stránka „Pohyb spodnej matrice“

### Spodná matrica BCC

Skontrolujte predvolene priradenú výmenu tepla s prostredím BCC pre spodnú formu a uistite sa, že predvolene priradená výmena tepla s prostredím BCC je priradená k celému vonkajšiemu povrchu spodnej formy (čo nezahŕňa os, keďže tieto uzly sa nachádzajú vo vnútri formy) (pozri obr. L5.29.). Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Positioning“ (Polohovanie).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0024.jpg' | relative_url }})

Stránka „Spodná forma BCC“

## Polohovanie

V tomto cvičení umiestnime hornú matricu nad polotovar pomocou možnosti „Interference“ v nástroji „Position Objects“. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}), vyberte možnosť „Interference“ (Interferencia) ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}), ako polohovací objekt vyberte „Top Die“ (Horná matrica) a ako referenčný objekt vyberte „Billet“ (Sochor), ako smer priblíženia vyberte smer -Y a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Horná matrica sa umiestni na sochor, ako je znázornené na obr. L5.30. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Kontakt“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0025.jpg' | relative_url }})

Stránka „Polohovanie objektov“

## Kontakt

Vyberte kontakt typu **užívateľ** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi polotovarom, hornou matricou a spodnou matricou, ako je znázornené na obr. L5.31.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0026.jpg' | relative_url }})

Stránka s kontaktnými údajmi

Zvýraznite vzťah **Top Die – Billet** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) tento vzťah upravte. V časti obrazovky venovanej treniu (pozri obr. L5.32.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné procesy tvárnenia.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0027.jpg' | relative_url }})

Stránka „Deformácia vzťahov medzi objektmi“

V roletovom menu „Trenie“ vyberte zo zoznamu položku **Kovanie za tepla (s mazáním)**; do poľa „Konštantné trenie“ sa vloží hodnota trenia **0,3**. Na **kartu „Thermal“** vyberte v zozname typ **Forming** pre koeficient prenosu tepla. Do poľa „Heat transfer coefficient“ sa vloží hodnota **0,004**. (Pozri obr. L5.33.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0028.jpg' | relative_url }})

Stránka „Inter Object Relation Thermal“

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna „Inter-Object“. Keďže podmienky trenia sú pre všetky páry objektov rovnaké, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných. Po vykonaní tejto operácie budú mať všetky vzťahy definované trenie 0,3. Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určite vhodnú toleranciu kontaktu (vypočíta sa hodnota približne 0,0012566"), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktu. Ak otočíte objekty v grafickom okne, uvidíte, že medzi dvoma objektmi bol vytvorený kontakt. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí okno Step.

## Krok

Zmeňte názov operácie na „**Spike_Nonisothermal**“, ako je znázornené na obr. L5.34.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0029.jpg' | relative_url }})

Ovládacie prvky krokov – záložka „Hlavná“ v režime pre pokročilých

Vyberte kartu „Simulačné kroky“ (![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }})), nastavte **Počet simulačných krokov** na **100** a **Krok na uloženie** na **5**. Nastavte **Hornú matricu** ako **Primárnu****matrici**. (Pozri obr. L5.35.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0030.jpg' | relative_url }})

Krok ovláda kartu „Simulačné kroky“ v expertnom režime

Na určenie vhodnej veľkosti kroku vyberte ikonu a zmerajte dĺžku hrany niekoľkých menších prvkov v polotovare. Priemerná dĺžka krátkej hrany je približne 0,035”. V záložke „Krok“ (![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }})) použite pre veľkosť kroku ako posun matrice konštantný **posun matrice** **0,015** palca na krok, čo predstavuje 1/3 tejto dĺžky krátkej hrany (pozri obr. L5.36).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0031.jpg' | relative_url }})

Ovládacie prvky krokov – karta „Krok“ v expertnom režime

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a uložte súbor s kľúčovými slovami pre danú úlohu výberom možnosti Export v ponuke Súbor.

## Vytvorenie databázy

Po úplnom nastavení úlohy je posledným krokom vytvorenie databázového súboru. Modul FEM (časť programu DEFORM®, ktorá vypočítava riešenie) používa databázový súbor na ukladanie riešení úlohy metódou konečných prvkov. Pri generovaní databázy v preprocesore DEFORM MO sa všetky informácie definované v preprocesore (napríklad vlastnosti materiálov, riadenie pohybu, geometrie objektov atď.) prenesú do databázového súboru.

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení úlohy niečo nechýba. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch). 

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), aby ste spustili simuláciu.

## Spustenie simulácie

Kliknite na ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“ (pozri obr. L5.37.). Po kliknutí na možnosť „Spustiť“ sa otvorí dialógové okno „Spustiť simuláciu“ (pozri obr. L5.38.). Použite predvolenú možnosť **Pokračovať v spustení**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0032.jpg' | relative_url }})

Možnosti simulácie

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0038.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať v režime Simulácia v častiach „Simulačné správy“ a „Simulačná grafika“. Kliknutím na kartu „Simulačné správy“ zobrazíte súbor správ. Pokiaľ je zaškrtnutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) (čo je predvolené nastavenie), súbor správ sa bude aktualizovať každých pár sekúnd.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Po ukončení simulácie sa na koniec súboru so správami pridá nasledujúca správa: „NORMAL STOP: Simulácia bola dokončená a zastavená v časovom kroku zadanom používateľom“. (Pozri obr. L5.39.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0032.jpg' | relative_url }})

Karta „Simulačné správy“

## Následné spracovanie výsledkov

Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), čím sa otvorí postprocesor MO. (Pozri obr. L5.40.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0033.jpg' | relative_url }})

Okno postprocesora MO

### Stavová premenná

Kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}), potom z ponuky „State Variable Temperature“ (Premenná stavu – teplota) vyberte položku **Temperature** (Teplota), kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) a pravým tlačidlom myši kliknite na položku **Color Bar** (Farebný pruh) v okne „Display“ (Zobrazenie) a ako typ farebného pruhu vyberte položku **Temperature** (Teplota). Ak máte v stromovej štruktúre objektov vybraný polotovar, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}), aby ste zobrazenie kontaktu medzi obrobkom a maticami. (Pozri obr. L5.41.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0034.jpg' | relative_url }})

Zobraziť premennú stavu „Teplota“

Prejdite jednotlivé kroky. Venujte osobitnú pozornosť teplotnému správaniu medzi sochárom a formami. Keďže sú formy prepletené, môžu sa zahrievať v miestach, kde prichádzajú do styku s horúcim sochárom. Podobne sa sochár ochladzuje v miestach, kde prichádza do styku s chladnejšími formami.

### Flownet

Postprocesor disponuje funkciami, ktoré pomáhajú používateľovi lepšie pochopiť, ako sa objekt deformuje počas simulácie. Jedna z týchto funkcií sa nazýva „Flow net“. Flow net je vzor, ktorý je možné aplikovať na priečny rez objektu a ktorý sa bude deformovať spolu s objektom. Deformácia tohto vzoru poskytne informácie o tom, ako sa deformuje konkrétna oblasť.

Kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_flownet_icon.jpg' | relative_url }}) otvoríte okno Flownet. Chceme definovať vzor pre nedeformovaný polotovar a potom sledovať, ako sa tento vzor deformuje v priebehu simulácie. Vyberte typ mriežky (pozri obr. L5.42.) a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0035.jpg' | relative_url }})

Okno Flownet

Nastavte **počet mriežok** na **10** v **smeru X** a na **20** v **smeru Y**. Kliknutím na ![]({{ '/assets/icons/post_icons/mo_preview_button.jpg' | relative_url }}) si môžete prezrieť tento počiatočný vzor mriežky. (Pozri obr. L5.43.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0036.jpg' | relative_url }})

Okno Grid Flownet

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}), aby ste vygenerovali tokovú sieť. Keď sa generovanie tokovej siete dokončí, kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste zatvorili program Flownet. Prejdite jednotlivými krokmi a sledujte, ako sa vzor tokovej siete deformuje. (Pozri obr. L5.44.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0037.jpg' | relative_url }})

Pridelené ubytovanie v spoločnosti Flownet

Ak chcete v laboratórnej úlohe „Die Stress“ pokračovať v riešení tejto úlohy, nezatvárajte projekt MO. Pozrite si [Lab 06 Die Stress]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_06_die_stress/' | relative_url }}).

**Súvisiace témy:**

[12.1. 2D Geometry Data Defining ]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/' | relative_url }})

[12.2. 2D Geometry Data Editing]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/' | relative_url }})

[13.1. 2D Mesh Generation]({{ '/docs/sk/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/' | relative_url }})

[14\. Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/' | relative_url }})

[15\. Movement Controls Settings]({{ '/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/' | relative_url }})

[17\. Object Data Initialize]({{ '/docs/sk/pre_processor/17_object_data_initialization/17_object_data_initialize/' | relative_url }})

[19\. Object Positioning]({{ '/docs/sk/pre_processor/19_object_positioning/19_object_positioning/' | relative_url }})

[20\. Inter-Object Data Definition]({{ '/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/' | relative_url }})

[9\. Simulation Controls]({{ '/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/' | relative_url }})

[6.3. Integrated Manufacturing Process Post-processor layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/' | relative_url }})

[25\. Post Processor Layout]({{ '/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/' | relative_url }})
