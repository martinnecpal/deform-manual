---
lang: sk
title: "Laboratórna práca č. 14 – Laboratórna práca s posuvnou maticou – objímka matice"
---

# Laboratórna práca č. 14 – Laboratórna práca s posuvnou maticou – puzdro matice

V tomto cvičení si ukážeme, ako nastaviť ovládanie pohybu posuvnej matrice. V tomto cvičení je spodná matrica posuvná a je uložená na pružinách upevnených na spodnej strane.

  
14.1. Vytvoriť nový problém

14.2. Typ geometrie

14.3. Ovládacie prvky simulácie

14.4. Vkladanie materiálu do stroja

14.5. Pridávanie objektov

14.6. Obrobok

14.7. Definícia hornej matrice

14.8. Definícia spodnej matrice

14.9. Definícia pinov

14.10. Polohovanie

14.11. Získavanie kontaktov

14.12. Ovládacie prvky na zastavenie

14.13. Ovládacie prvky krokov

14.14. Vytvorenie databázy

14.15. Spustenie simulácie

14.16. Následné spracovanie výsledkov

## Vytvoriť nový problém

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Anglický**“. Názov úlohy nastavte na „******Die_Sleeve**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), čím otvoríte nový problém s využitím integrovaného výrobného procesu Deform.

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt. V tomto bode bude používateľ vyzvaný, aby zadal názov projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názov tejto relácie; ako názov projektu použijeme „**Die_Sleeve**“. Pridajte **2D tvarovaciu operáciu** ako **prvú operáciu** tak, že ju vyberiete z roletového zoznamu Prvá operácia a zaškrtnete políčko, ako je znázornené na obr. L14.1. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0001.jpg' | relative_url }})

Sprievodca MO – Nový projekt

## Typ geometrie

V tomto laboratórnom cvičení budeme používať osovo symetrické geometrie, preto na stránke s typmi geometrií vyberte ako typ geometrie začiarkavacie políčko **2D Axisymmetric**, ako je znázornené na obr. L14.2, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0002.jpg' | relative_url }})

Výber typu osovo-symetrickej geometrie

## Ovládacie prvky simulácie

V tomto laboratórnom cvičení si ukážeme, ako nastaviť riadenie neizotermického pohybu posuvnej matrice. V okne „Simulation controls“ sa preto uistite, že sú zaškrtnuté oba **režimy** **Deformácia** a **Prenos tepla** (pozri obr. L14.3.). Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0003.jpg' | relative_url }})

Okno riadenia simulácie

## Vkladanie materiálu do obrobku

V okne Zoznam materiálov načítajte materiál „**AISI-4140**“ z knižnice materiálov DEFORM v kategórii Oceľ pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To je možné vykonať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}), ako je znázornené na obr. L14.4. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Objekt.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0004.jpg' | relative_url }})

Okno „Zoznam materiálov“

## Pridávanie objektov

Na túto operáciu potrebujeme štyri objekty, preto v okne „Objekty“ pridajte štyri objekty kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (pozri obr. L14.5.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0005.jpg' | relative_url }})

Okno na pridávanie objektov

## Obrobok

V okne „Workpiece“ (Obrobok) nastavte teplotu objektu na **1850** °F a ako typ objektu vyberte **Plastic** (Plast), ako je znázornené na obr. L14.6. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0006.jpg' | relative_url }})

Objekt „Billet“ – Okno

### Vytvorenie geometrie obrobku

Na stránke Geometria vyberte ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) a definujte **valec** s **polomerom** **1,5** ” a **výškou** **4,5** ” (pozri obr. L14.7.). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Skontrolujte geometriu a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0007.jpg' | relative_url }})

Definovanie geometrie

### Generovanie siete

Predvolený počet prvkov nestačí na zachytenie tvaru dokončovacieho prvku, preto nastavte **počet prvkov** na **2000** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), aby sa vytvorila sieť (pozri obr. L14.8.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0008.jpg' | relative_url }})

Stránka so sieťou obrobkov

### Priradenie materiálu na odliatky

Ak chcete obrobku priradiť materiál, vyberte materiál **AISI-4140** z okna materiálov (pozri obr. L14.9.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0009.jpg' | relative_url }})

Stránka s výberom materiálov

### Okrajové podmienky pre polotovar

Na stránke BCC skontrolujte, či sú pri položke „Deformácia“ nastavené BCC „Rýchlosť“ pre ľavú stranu obrobku v smere X a BCC „Výmena tepla s okolím“ pre celý vonkajší povrch polotovaru (čo nezahŕňa os, keďže tieto uzly sa nachádzajú vnútri objektu), ktoré sú pri vytváraní siete priradené štandardne. Ak nie sú BCC priradené, priraďte ich ručne, ako je znázornené na obr. L14.10 a obr. L14.11. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Top die object“ (Horná matica).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0010.jpg' | relative_url }})

Nastavená rýchlosť BCC pre obrobok

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0011.jpg' | relative_url }})

Priradená výmena tepla s prostredím BCC pre obrobok

## Definícia pojmu „Top Die“

Na stránke objektu „Top Die“ ponechajte názov „Top Die“, typ objektu **R****igid** a predvolenú teplotu 68 °F. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import geometrie hornej matrice

V okne Geometria načítajte geometrický súbor **DieSleeve_Lab_TopDie.geo** z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice), ako je znázornené na obr. L14.12., V rozbaľovacom okne „User Library“ (Knižnica používateľa), v ktorom sa pýta, či chcete použiť cestu k priečinku laboratórnych cvičení inštalácie ako predvolené umiestnenie knižnice, kliknite na **Áno**. Geometria sa nachádza v inštalačnom priečinku DEFORM v adresári \2D\LABS. Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku pohybu.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0012.jpg' | relative_url }})

Hlavná stránka „Geometria lisovacích foriem“

### Priradiť pohyb k hornej kocku

Pre toto laboratórne cvičenie nastavte **rýchlosť** **3** palce za sekundu v smere **-Y**. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Bottom Die“ (pozri obr. L14.13).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0013.jpg' | relative_url }})

Hlavná stránka „Pohyb matrice“

## Definícia spodnej matrice

Na stránke „Spodná forma“ ponechajte názov, typ objektu a predvolenú teplotu bez zmien a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import geometrie spodnej matrice

Načítajte súbor **DieSleeve_Lab_BottomDie**.**geo** pomocou tlačidla „Načítať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). Skontrolujte geometriu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s pohybmi.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0014.jpg' | relative_url }})

Stránka o geometrii spodnej matrice

### Priradiť pohyb spodnej kocky

Zvoľte typ pohybu **Posuvná matrička**. Definujte smer pohybu posuvnej matrice ako smer **-Y** s konštantnou **tuhosťou****500** klb/in, **predpätím****2500** klb a **max. zdvihom**. **2,5** in a druhý koniec pružiny vyberte ako **Fixed**, ako je znázornené na obr. L14.15. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až na stranu s objektom 4. Ďalšie informácie o ovládacích prvkoch pohybu posuvného lisovacieho nástroja nájdete v časti [15.7. Sliding Die]({{ '/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0015.jpg' | relative_url }})

Stránka o pohybe spodnej matrice

## Definícia výstupkov matice

V okne „Objekt 4“ zmeňte názov objektu 4 na **Die Pin**, ako typ objektu vyberte **Pevný** a ponechajte predvolenú teplotu bez zmien. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Geometria kolíkov

Načítajte súbor **DieSleeve_Lab_DiePin.geo** pomocou tlačidla „Načítať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (pozri obr. L14.16.). Skontrolujte geometriu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s polohovaním.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0016.jpg' | relative_url }})

Definovanie geometrie kolíkov

## Polohovanie

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}). Na stránke polohovania objektov vyberte možnosť Polohovanie podľa kolízie a ako **Polohovaný objekt** vyberte **Obrobok** a ako **Referenčný objekt** vyberte **Spodná matrica**. Mali by ste použiť smer priblíženia **–Y** a potom kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Obrobok je umiestnený nad spodnou maticou. Zväčšite pravý dolný roh obrobku a uvidíte, že predvolená hodnota kolízie 0,0001 bola pre tieto geometrie trochu príliš veľká, pretože medzi objektmi je príliš veľké prekrývanie. Pridajte k hodnote Interference ešte päť núl, aby bola 0,000000001, a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Mali by ste vidieť, že obrobok je teraz umiestnený v matrici so správnou mierou prekrývania. Umiestnite **hornú formu** (objekt polohy) nad **obrobok** (referenčný objekt) pomocou kolízie so smerom priblíženia **–Y**. (Pozrite obr. L14.17 a obr. L14.18.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0017.jpg' | relative_url }})

Umiestnenie objektov: Okno umiestnenia

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0018.jpg' | relative_url }})

Umiestnenie objektov: Objekty pred a po umiestnení

## Získavanie kontaktov

Vyberte typ kontaktu **Používateľ** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridajú vzťahy medzi obrobkom, hornou maticou, spodnou maticou a upínacím čapom, ako je znázornené na obr. L14.19.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0019.jpg' | relative_url }})

Predvolené vzťahy na stránke Vytvorenie kontaktu

Zvýraznite vzťah **Horná matrica – Obrobok** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) tento vzťah upravte. V časti obrazovky venovanej treniu (pozri obr. L14.20.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné procesy tvárnenia.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0020.jpg' | relative_url }})

Okno definície údajov medzi objektmi

V roletovom menu „Trenie“ vyberte zo zoznamu položku **Kovanie za tepla (s mazaním)**; do poľa „Konštantné trenie“ sa vloží hodnota **0,3**. Na karte **Tepelné** vyberte z roletového menu typu koeficientu prenosu tepla položku **Tvarovanie**; do poľa Koeficient prenosu tepla sa vloží hodnota **0,002**. (Pozri obr. L14.21.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0021.jpg' | relative_url }})

Stránka „Inter Object Relation Thermal“

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna kontaktov. Keďže podmienky trenia sú rovnaké pre všetky páry objektov, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z vybraného vzťahu do všetkých vzťahov. Po vykonaní tejto operácie budú mať všetky vzťahy definované trenie 0,3 a koeficient prenosu tepla 0,002.

V priebehu simulácie sa horná forma spúšťa nadol, dotýka sa spodnej formy a môže do nej vniknúť; preto je potrebné definovať kontaktný vzťah medzi hornou a spodnou formou, aby sa zabránilo vniknutiu. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridajte kontaktný vzťah, vyberte **Hornú matricu** ako **Hlavnú** a **Spodnú matricu**, pre ktorú sú definované ovládacie prvky posuvného pohybu ako **S******lav** e**. (Pozri obr. L14.22.)

Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určte vhodnú toleranciu kontaktu (vypočíta sa hodnota približne 0,00067"), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktu (pozri obr. L14.22.). Prejdite na kartu Správa alebo sledujte stavový riadok, aby ste zistili informácie o vygenerovaných kontaktoch. Kliknite na **![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})**.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0022.jpg' | relative_url }})

Kontakt vznikajúci medzi objektmi

## Ovládacie prvky na zastavenie

Chceme simuláciu zastaviť, keď sa horná matrica posunie o **4,5** ”. Na obrazovke „Stopping Controls“ zaškrtnite možnosť **Max Die stroke** a následne nastavte hodnotu zdvihu v osi **Y** na **4,5** ", ako je znázornené na obr. L14.23. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0023.jpg' | relative_url }})

Okno „Ovládacie prvky zastavenia“

## Ovládacie prvky krokov

Na stránke nastavení krokov nastavte **Počet krokov** na hodnotu **1000**, **Krok pre uloženie** na hodnotu **5** a **Posun matrice na krok** na hodnotu **0,01**. Keďže sme definovali väčší počet krokov, ako je potrebný na celkový posun primárneho lisovacieho nástroja, simulácia sa zastaví, keď dosiahne kontrolný bod zastavenia. Nastavte horný lisovací nástroj ako primárny, ak sa nevybral automaticky (pozri obr. L14.24). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0024.jpg' | relative_url }})

Okno „Ovládacie prvky krokov“

## Vytvoriť databázu

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení problému niečo nechýba. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáli).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu.

## Spustenie simulácie

Po vytvorení databázy prejdite do simulačného režimu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Run Options (Možnosti spustenia), ako je znázornené na obr. L14.25. Použite predvolenú možnosť **Pokračovať v spustení**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0032.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať na karte „Simulation Message“ a v časti „Simulation Graphics“ v oblasti zobrazenia „Graphics“ v režime simulácie. Ak je na karte „Simulation Message“ zaškrtnutá voľba „![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }})“ (čo je predvolené nastavenie), súbor správ sa bude automaticky aktualizovať.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia práve nachádza, a informácie o tom, ako dobre simulácia prebieha.

Po ukončení simulácie sa na konci súboru so správami zobrazí nasledujúca správa (pozri obr. L14.26.):

"PROGRAM SA ZASTAVIL!

„HODNOTA STROKE -4,5000000 PREKROČILA ŠPECIFIKOVANÝ LIMIT 4,5000000“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0025.jpg' | relative_url }})

Súbor so simulačnými správami

## Následné spracovanie výsledkov

Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), čím sa otvorí postprocesor MO. V **prehliadači krokov** kliknite pravým tlačidlom myši na niektorý krok a vyberte možnosť **Zobraziť****Zdvih**. Prehrávajte kroky a sledujte spodnú matricu, keď je zdvih hornej matrice okolo 2,4". Môžeme pozorovať, že spodná matrica sa začína pohybovať smerom nadol v zápornom smere osi Y spolu s hornou matricou. Ak vytvoríme graf zaťaženia v závislosti od zdvihu pre spodnú matricu, môžeme pozorovať, že sa spodná matrica pohybuje nadol, keď jej zaťaženie dosiahne 2513 klb (pozri obr. L14.27.), čo presahuje predpätie definované na stránke ovládacích prvkov pohybu spodnej matrice.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0026.jpg' | relative_url }})

Graf zaťaženia a zdvihu v okamihu, keď sa spodná matrica začne posúvať nadol

Počas prehrávania animácie sledujte tok materiálu a v poslednom kroku skontrolujte celkový posun hornej matrice. (Pozri obr. L14.28.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0027.jpg' | relative_url }})

Obrobok v poslednom kroku

#### Premenné stavu

Prejdite na posledný krok a zo zoznamu **Stavové veličiny** vyneste do grafu dôležité stavové veličiny, ako sú **efektívne deformácie**, **efektívne napätia**, **teplota** a **poškodenie**, ako je znázornené na obr. L14.29 až obr. L14.32.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0028.jpg' | relative_url }})

Graf premennej stavu efektívneho deformácie

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0029.jpg' | relative_url }})

Graf premennej stavu „efektívne napätie“

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0030.jpg' | relative_url }})

Graf premennej teploty

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0031.jpg' | relative_url }})

Graf premennej stavu poškodenia
