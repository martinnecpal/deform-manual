---
lang: sk
title: "Laboratórna práca č. 04 – Prenos tepla"
---

# Laboratórna úloha č. 04 – Prenos tepla

4.1. Vytvorenie novej úlohy

4.2. Pridanie operácie prenosu tepla

4.3. Zmena názvu operácie

4.4. Ohrev v peci

4.5. Ohrev v peci

4.6. Teplotné podmienky v peci

4.7. Nastavenie obrobku

4.8. Ovládacie prvky krokov vykurovacej pece

4.9. Vytvorenie databázy pre vykurovaciu pec

4.10. Prevádzka s vzduchovým chladením

4.11. Stránka procesu prevádzky s vzduchovým chladením

4.12. Regulácia krokov pri vzduchovom chladení

4.13. Vytvorenie databázy pre vzduchové chladenie

4.14. Spustenie simulácie

4.15. Následné spracovanie výsledkov

V tomto laboratórnom cvičení nastavíme dve operácie:

**Operácia 1** – Ohrev v peci: V rámci tejto operácie zahrievame sochoru v peci po dobu 1 hodiny pri teplote 1800 °F.

**Operácia 2** – Chladenie vzduchom: Pri tejto operácii chladíme polotovar pri izbovej teplote po dobu 60 sekúnd.

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main, ako je znázornené nižšie [Fig. L4.1.]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_04_heat_transfer/' | relative_url }}#Fig_L4_1_DEFORM-2D/3D_GUI_main_window)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno grafického používateľského rozhrania programu DEFORM-2D/3D

Vytvorte nový problém buď výberom položky **Súbor****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. L4.2. Vyberte tlačidlo „**Integrovaný výrobný proces**“ a ako systém jednotiek vyberte „**Angličtina**“ pomocou príslušného tlačidla. Názov úlohy zadajte ako „**Heat_Transfer**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak toto políčko nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili novú úlohu s použitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu úlohy

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt (pozri obr. L4.3.). V tomto bode bude používateľ vyzvaný, aby zadal názov projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názov tejto relácie. V tejto relácii použijeme ako názov projektu „**Heat_Transfer**“. Ako **prvú operáciu** vyberte operáciu **2D prenos tepla** a **zaškrtnite** **políčko**, aby ste operáciu prenosu tepla pridali ako prvú operáciu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0001.jpg' | relative_url }})

MO Okno nastavení nového projektu

## Pridanie operácie prenosu tepla

Sprievodca viacerými operáciami otvorí operáciu 2D prenosu tepla s novým projektom s názvom Heat_Transfer (pozri obr. L4.4.). Pridajte ďalšiu operáciu 2D prenosu tepla ako druhú operáciu zo zoznamu operácií v Průzkumníku. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie 2D prenosu tepla alebo ju môžete pridať aj pretiahnutím a umiestnením do oblasti Editoru operácií.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0002.jpg' | relative_url }})

Projekt prenosu tepla v MO s 2D simuláciou prenosu tepla

## Zmena názvu operácie

Ak chcete zmeniť názov operácie, dvakrát kliknite na pole „Prenos tepla“ v zozname 2D operácií prenosu tepla v editore operácií, zmeňte názov operácie na „**Ohrev v peci**“ a stlačte klávesu Enter. Opakujte rovnaký postup, aby ste zmenili názov druhej operácie prenosu tepla na „**Chladenie vzduchom** “, pozri obr. L4.5 a obr. L4.6.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0003.jpg' | relative_url }})

Zmena názvu operácie v editore operácií

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0004.jpg' | relative_url }})

Po zmene názvu operácie

## Kúrenie v peci

V rámci tohto procesu zahrievame sochoru pri izbovej teplote v ohrevnej peci na teplotu 1800 °F po dobu 3600 sekúnd, kým nedosiahne ustálený stav.

## Kúrenie v pecnom procese

Zvýraznite prvú operáciu 2D prenosu tepla a na stránke s typom geometrie vyberte typ geometrie **2D osovo symetrická** (pozri obr. L4.7.). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0005.jpg' | relative_url }})

Stránka na výber typu geometrie

Na stránke „Typ prenosu tepla“ vyberte typ prenosu tepla **Teplo v peci**, ako je znázornené na obr. L4.8. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0006.jpg' | relative_url }})

Výber typu prenosu tepla

## Stav procesu v peci

Na stránke „Process Condition“ (Podmienky procesu) nastavte **teplotu prostredia** na **1800** °F, ako **čas procesu** použite predvolenú hodnotu **3600** sekúnd a v tomto laboratórnom cvičení použite predvolenú hodnotu koeficientu konvekcie. (pozri obr. L4.9.) Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). V ovládacom paneli simulácie vyberte predvolené nastavenie a klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Obrobok“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0007.jpg' | relative_url }})

Stránka s podmienkami procesu

## Upevnenie obrobku

Zmeňte názov objektu na „**Billet**“ a ako typ objektu vyberte ****(pozri obr. L4.10.). Na začiatku simulácie sa sochor vloží do pece, preto by mala byť teplota nastavená na izbovú teplotu, t. j. 68 °F. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0008.jpg' | relative_url }})

Okno objektu obrobku

### Vytvorenie geometrie

Na stránke „Geometria“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}), do tabuľky 1 zadajte nasledujúce hodnoty súradníc XYR (pozri obr. L4.11) a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}),

X |  Y |  R  
---|---|---  
0 |  0 |  0  
1,5 |  0 |  0,12  
1,5 |  4 |  0,12  
0 |  4 |  0  
  
Hodnota súradníc XYR v geometrii

Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), použite predvolené parametre kontroly a kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}). Zobrazí sa správa: „**Geometria je správna**“. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a následne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0009.jpg' | relative_url }})

Stránka „Úprava geometrie obrobku“

### Vytvorenie siete

Použite predvolené nastavenia systémovej siete a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Vygeneruje sa sieť s približne 1000 prvkami. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

###  Priradiť materiál na výkovky

V okne Zoznam materiálov načítajte materiál **AISI-1025[1800–2200 °F (1000–1200 °C)]** z knižnice materiálov DEFORM v kategórii Oceľ pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}); na karte „Thermal“ (Tepelné vlastnosti) v údajoch o materiáli môžete pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) zobraziť údaje o tepelnej kapacite a tepelnej vodivosti. Materiál AISI-1025 bol načítaný do úlohy a automaticky priradený k polotovaru. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0010.jpg' | relative_url }})

Okno na úpravu materiálu

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0011.jpg' | relative_url }})

Údaje o tepelnej vodivosti materiálov

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0012.jpg' | relative_url }})

Údaje o tepelnej kapacite materiálu

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0013.jpg' | relative_url }})

Okno „Materiál objektu“

### Definovanie okrajových podmienok prenosu tepla v polotovare

Na stránke BCC skontrolujte predvolené priradenie výmeny tepla s prostredím BCC na celý vonkajší povrch polotovaru (čo nezahŕňa os, keďže tieto uzly sa nachádzajú vnútri objektu). Predvolené BCC sa priraďujú automaticky na základe výberu typu úlohy ako osovo symetrickej (pozri obr. L4.16.). Potom klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Step“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0014.jpg' | relative_url }})

Okno BCC z hliníkového bloku

## Ovládacie prvky krokov vykurovacej pece

Na stránke „Kroky“ zmeňte **Počet krokov** na **240**, nastavte **krok ukladania** na **10** a **Čas** definície kroku riešenia na **15** sekúnd (pozri obr. L4.17.), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0015.jpg' | relative_url }})

Stránka s ovládacími prvkami krokov

## Vytvorenie databázy pre vykurovaciu pec

Po úplnom nastavení operácie je posledným krokom vytvorenie databázového súboru. Modul FEM (časť programu DEFORM®, ktorá vypočítava riešenie) používa databázový súbor na ukladanie riešení problému pomocou metódy konečných prvkov. Pri generovaní databázy v preprocesore DEFORM MO sa všetky informácie definované v preprocesore (napríklad vlastnosti materiálov, riadenie pohybu, geometrie objektov atď.) prenesú do databázového súboru.

Na stránke „Generate DB“. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) spustíte kontrolu programu, či sa pri nastavení úlohy na niečo nezabudlo. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli zadať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}), aby ste prešli k ďalšej operácii.

## Prevádzka s vzduchovým chladením

V tomto kroku nechávame polotovar 60 sekúnd vychladnúť na izbovú teplotu a z databázy sa načíta údaj o polotovare.

## Stránka s popisom prevádzky s vzduchovým chladením

Na stránke „In Process“ vyberte typ prenosu tepla ako **Prenos vzduchom**. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

Zmeňte **čas prenosu** na **60** sekúnd, použite predvolenú teplotu okolia (68 °F) a predvolenú hodnotu konvekčného koeficientu, ako je znázornené na obr. L4.18. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Object“ (Objekt). Ak sú v zozname objektov pridané objekty „Top die“ (Horná forma) a „Bottom Die“ (Spodná forma), odstráňte objekt 2 a objekt 3 pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Step“ (Krok).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0016.jpg' | relative_url }})

Okno s podmienkami procesu

## Ovládacie prvky pre vzduchové chladenie

Na stránke „Kroky“ zmeňte **Počet krokov** na **60**, **nastavte krok ukladania** na **4** a **čas** definície kroku riešenia na **1** s/krok (pozri [Fig. L4.19.]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_03_spike_isothermal/' | relative_url }})), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0017.jpg' | relative_url }})

Stránka s ovládacími prvkami krokov

## Vytvorenie databázy pre vzduchové chladenie

Na stránke „Generate DB“ skontrolujte stav. Ak sa zobrazuje stav „Chyba zadania“, skontrolujte chýbajúce údaje a dokončite nastavenie. Uložte projekt a prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), kde spustíte simuláciu.

## Spustenie simulácie

Kliknite na ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“ (pozri obr. L4.20.). Po kliknutí na možnosť „Spustiť“ sa otvorí dialógové okno „Spustiť simuláciu“ (pozri obr. L4.21.). Použite predvolenú možnosť **Pokračovať v spustení**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0032.jpg' | relative_url }})

Možnosti simulácie

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0024.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať v režime Simulácia prostredníctvom okien Simulačné správy a Simulačná grafika. Kliknutím na kartu Simulačné správy zobrazíte súbor správ. Pokiaľ je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}), čo je predvolené nastavenie, súbor správ sa bude aktualizovať každých pár sekúnd.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Po ukončení simulácie sa na koniec súboru LOG pridá nasledujúca správa: „MULTIPLE OPERATION COMPLETED.“

## Následné spracovanie výsledkov

Po dokončení simulácie prejdite na kartu, čím sa otvorí postprocesor MO.

### Graf stavovej premennej

Kliknite na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) a ako premennú vyberte „Teplota“. Kliknite pravým tlačidlom myši na farebnú lištu v okne DISPLAY a ako typ farebnej lišty vyberte „Teplota“. Tým sa pri zobrazení teplôt dosiahne intuitívnejšie farebné schéma (pozri obr. L4.22.).

Prejdite jednotlivými krokmi a sledujte, ako sa polotovar zahrieva v režime ohrevu a ako chladne v režime vzduchového chladenia (pozri obr. L4.23.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0018.jpg' | relative_url }})

Zobrazenie premennej stavu „Teplota“ s typom „Teplota“ a typom farebnej stupnice

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0019.jpg' | relative_url }})

Graf teploty pre laboratórne úlohy z oblasti prenosu tepla

### Zhrnutie

Tlačidlo „Summary“ slúži na vytvorenie grafu minimálnych a maximálnych hodnôt stavových premenných. Kliknutím na ![]({{ '/assets/icons/post_icons/mo_summary_icon.jpg' | relative_url }}) otvoríte okno SUMMARY. Ak chcete lepšie pochopiť, ako sa v tomto laboratórnom cvičení zahrieval a ochladzoval blok, vyberte kartu Thermal a potom kliknite na ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) pre zobrazenie teploty (pozri obr. L4.24.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0020.jpg' | relative_url }})

Graf s prehľadom teplôt

### Sledovanie bodov

Teploty v konkrétnych miestach sochory je možné sledovať pomocou funkcie bodového sledovania.

Kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }}) otvoríte okno „POINT TRACKING“. Sledujte teploty v troch bodoch v polovici dĺžky polotovaru, približne v miestach znázornených na obr. L4.25 a obr. L4.26.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0021.jpg' | relative_url }})

Výber bodov pre sledovanie bodov

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0022.jpg' | relative_url }})

Graf teploty vo vybranej oblasti s využitím funkcie sledovania bodov

Radi by sme sa podrobnejšie pozreli na kroky na konci simulácie, keď prebieha chladenie vzduchom. Kliknite pravým tlačidlom myši na graf v zobrazovacom okne a zo zoznamu vyberte možnosť „Nastaviť vlastnosti grafu“, zmeňte rozsah osí X aj Y na hodnoty uvedené nižšie na obr. L4.27 a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button2.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_04_heat_transfer/2d_mobl4_image0023.jpg' | relative_url }})

Okno „Vlastnosti grafu“

Po vykonaní týchto zmien je oveľa ľahšie vidieť, že bod na vonkajšom priemere polotovaru (bod 3) chladol oveľa rýchlejšie ako bod v blízkosti stredu (bod 1).

**Súvisiace témy:**

[35.1. 2D Heat Transfer Operation]({{ '/docs/sk/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/' | relative_url }})

[6.3. Integrated Manufacturing Process Post-processor layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/' | relative_url }})

[25\. Post Processor Layout]({{ '/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/' | relative_url }})
