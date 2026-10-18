---
lang: sk
title: "Laboratórna úloha č. 10: Hydraulický lis"
---

# Laboratórna práca č. 10 – Hydraulický lis

Požiadavka: Na nastavenie tejto operácie musíme najprv nastaviť [Lab 03 Spike Isothermal Lab]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_03_spike_isothermal/' | relative_url }}).

V tomto laboratórnom cvičení sa zopakuje simulácia izotermického kovania hrotu na 1000-tonovom hydraulickom lise. Výsledky deformácie budú podobné ako v predchádzajúcich laboratórnych cvičeniach zameraných na kovanie hrotu, avšak rýchlosť sa zníži, keďže lisovi na konci zdvihu dôjde výkon. Na hornú matricu bude pôsobiť počiatočná rýchlosť 2 palce za sekundu. S rastúcim zaťažením pri tvárnení bude potrebný vyšší výkon, než aký je lis schopný dodať, čo bude mať za následok spomalenie pohybu matrice.

10.1. Vytvorenie novej úlohy

10.2. Pridanie operácie

10.3. Importovanie databázy

10.4. Nastavenie hydraulického pohybu hornej matrice

10.5. Vytvorenie databázy

10.6. Spustenie simulácie

10.7. Následné spracovanie výsledkov

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Anglický**“. Názov úlohy zadajte ako „******Spike_Hydraulic**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili novú úlohu s použitím integrovaného výrobného procesu Deform.

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt (pozri obr. L10.1.), kde bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tomto cvičení použijeme ako názov projektu „**Spike_Hydraulic**“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_10_hydraulic_press/2d_mobl10_image0001.jpg' | relative_url }})

Priradenie názvu projektu

Používateľ môže tiež zmeniť systém jednotiek, umiestnenie súboru na uloženie projektu a pridať operáciu výberom z roletového zoznamu „Prvá operácia“ a zaškrtnutím príslušného políčka (pozri obr. L10.1.). Pomocou možnosti „Kopírovať existujúci projekt“ môžeme importovať predtým uložené projekty ako nové projekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

## Pridanie operácie

Otvorí sa sprievodca viacerými operáciami. Zoznamu operácií v prehliadači pridajte operáciu 2D tvarovania. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) pre operáciu 2D tvarovania alebo ju môžete pridať aj pretiahnutím do editora operácií.

## Importovanie databázy

Pomocou možnosti Importu ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) načítajte databázu úlohy **Spike_Isothermal**, v okne výberu krokov (pozri obr. L10.2.) vyberte krok **-1** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Pohyb hornej matrice.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_10_hydraulic_press/2d_mobl10_image0002.jpg' | relative_url }})

Výber kroku v okne „Výber kroku“

**Poznámka**:

Na spustenie modelu hydraulického lisu sú potrebné dva parametre.

1\. Do poľa riadenia pohybu by sa mala zadávať riadiaca rýchlosť alebo menovitá počiatočná rýchlosť. Ak lis beží pri maximálnej možnej rýchlosti, táto rýchlosť by mala byť zhodná s rýchlosťou bez zaťaženia. Možné sú akékoľvek nastavenia v rámci výkonového rozsahu, vrátane rýchlosti (alebo zaťaženia) ako funkcie času alebo zdvihu.

2\. Výkonový rozsah, ktorý určuje maximálnu rýchlosť dostupnú pri akomkoľvek zaťažení, možno opísať pomocou dvojíc údajov. Tieto údaje sú konštantné pre akúkoľvek konfiguráciu lisu. Zvyčajne stačí päť alebo viac bodov na adekvátne stanovenie tohto limitu, pričom systém DEFORM® interpoluje údaje medzi jednotlivými bodmi. Mal by sa zahrnúť jeden bod pri nulovom zaťažení a jeden pri nulovej sile.

Pri používaní tohto modelu hydraulického lisu sú k dispozícii všetky ovládacie prvky na zastavenie, ako napríklad maximálny zdvih, maximálne zaťaženie alebo minimálna rýchlosť.

## Nastavenie hydraulického pohybu hornej matrice

Vyberte typ **hydraulického****pohonu**, nastavte konštantnú **rýchlosť** na hodnotu **2** palce/sek., **zaškrtnite** políčko **limit výkonu******výkonu** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}) a v tabuľke zadajte nižšie uvedené hodnoty krivky obmedzenia výkonu (pozri obr. L10.3.). Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste zatvorili okno Funkcia. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Generovať databázu.

**Sila (Klb-s)** |  **Rýchlosť (in/s)**  
---|---  
0 |  2,51  
100 |  2,50  
250 |  2,46  
450 |  2,40  
700 |  2,26  
1000 |  1,98  
1250 |  1,65  
1500 |  1,25  
1750 |  0,75  
2000 |  0,0  
  
Údaje o krivke obmedzenia výkonu pri pohybe hornej matrice

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_10_hydraulic_press/2d_mobl10_image0003.jpg' | relative_url }})

Dialógové okno na definovanie limitu výkonu pohybu hornej matrice

## Vytvorenie databázy

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) spustíte kontrolu programu, či sa pri nastavení úlohy niečo nevynechalo. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli zadať údaje o materiáloch). 

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Akonáhle program dokončí zapisovanie databázy, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), aby ste spustili simuláciu.

## Spustenie simulácie

Kliknite na ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“. Po kliknutí na možnosť „Spustiť“ sa otvorí dialógové okno „Spustiť simuláciu“. Použite predvolenú možnosť **Pokračovať v spúšťaní** na výber možnosti „**Pokračovať od posledného kroku**“ a potom nastavte režim simulácie na **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

Priebeh simulácie je možné sledovať počas jej behu prostredníctvom okien „Simulation Message“ a „Simulation Graphics“ v režime simulácie. Kliknutím na kartu „Simulation Message“ zobrazíte súbor správ. Pokiaľ je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) (čo je predvolené nastavenie), súbor správ sa bude aktualizovať každých pár sekúnd.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Po ukončení simulácie sa na koniec súboru „Message“ pridá nasledujúca správa:

"******Správa*******

„Simulácia bola dokončená a zastavená v časovom kroku zadanom používateľom“.

## Následné spracovanie výsledkov

Po dokončení simulácie kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), čím sa otvorí postprocesor MO.

**Graf zaťaženia a zdvihu:**

Vytvorte grafy **zaťaženie – zdvih** a **rýchlosť – zdvih** a sledujte ich tak, ako je znázornené na obr. L10.4 a obr. L10.5.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_10_hydraulic_press/2d_mobl10_image0004.jpg' | relative_url }})

Graf závislosti zaťaženia od zdvihu

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_10_hydraulic_press/2d_mobl10_image0005.jpg' | relative_url }})

Graf rýchlosti a ťahu

****

**Súvisiace témy:**

[15\. Movement Controls Settings]({{ '/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/' | relative_url }})

[6.2. Integrated Manufacturing Process Simulation layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/' | relative_url }})

[6.3. Integrated Manufacturing Process Post-processor layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/' | relative_url }})

[25\. Post Processor Layout]({{ '/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/' | relative_url }})
