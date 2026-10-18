---
lang: sk
title: "Laboratórna úloha č. 09: Viacnásobná operácia s nástrojom „Hammer“"
---

# Cvičenie 09: Viacnásobná operácia v programe Hammer

Cieľom tohto laboratórneho cvičenia je ukázať používateľovi, ako v programe DEFORM pripraviť simuláciu viacerých úderov pre tri po sebe idúce údery kladivom s využitím operácie „2D Multi Blow Forging“. Simulácia sa vykonáva ako 2D neizotermická simulácia.

9.1. Vytvorenie nového problému

9.2. Pridanie operácie

9.3. Import súboru s kľúčom

9.4. Nastavenia procesu

9.5. Úprava tabuľky „Blow“

9.6. Vytváranie kontaktu medzi objektmi

9.7. Vytvorenie databázy

9.8. Spustenie simulácie

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek zvoľte prepínač „**Angličtina**“. Názov úlohy zadajte ako „**HM_FORGE**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili novú úlohu s použitím integrovaného výrobného procesu Deform.

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt (pozri obr. 9.1.), kde bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tomto cvičení použijeme ako názov projektu „****HM_FORGE****“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_09_hammer_multiple_operation/2d_mobl9_image0001.jpg' | relative_url }})

Priradenie názvu projektu

Používateľ môže tiež zmeniť systém jednotiek, umiestnenie súboru na uloženie projektu a pridať operáciu výberom z roletového zoznamu „Prvá operácia“ a zaškrtnutím príslušného políčka (pozri obr. 9.1.). Pomocou možnosti „Kopírovať existujúci projekt“ je možné importovať predtým uložené projekty ako nové projekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

## Pridanie operácie

Otvorí sa sprievodca viacerými operáciami. Zoznamu operácií v prehliadači pridajte operáciu „2D Multi Blow Forging“. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) pre operáciu „2D Multi Blow Forging“ alebo ju môžete pridať aj pretiahnutím do editora operácií. (Pozri obr. 9.2.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_09_hammer_multiple_operation/2d_mobl9_image0002.jpg' | relative_url }})

Do editora operácií bola pridaná operácia „Multi Blow Forging“

## Importovanie súboru s kľúčom

Naimportujte súbor **HAMMER_LAB.KEY** z inštalačnej zložky DEFORM \2d\LABS pomocou možnosti Import ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}).

## Nastavenie parametrov procesu

Energia bola načítaná z definície pohybu primárneho lisovacieho nástroja. Zachovajte rovnakú energiu. Zaškrtnite políčko „Použiť rotáciu obrobku“, aby sa obrobok po každom údere otočil. Nechajte zaškrtnuté políčko „Použiť pauzu“, pretože v tomto laboratórnom cvičení medzi údermi nedochádza k ohrevu. Nezaškrtávajte políčko „Použiť opätovný ohrev“. (pozri obr. 9.3.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste upravili tabuľku úderov.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_09_hammer_multiple_operation/2d_mobl9_image0003.jpg' | relative_url }})

Stránka procesu

## Úprava tabuľky „Blow“

V tabuľke „Blow Table“ pridajte okrem predvoleného úderu ešte dva ďalšie údery, čím sa ich celkový počet zvýši na tri. Vo všetkých troch riadkoch zmeňte čas zdržania (Dwell time) na 1,5 sekundy dvojitým kliknutím na príslušné pole. V prvom riadku zaškrtnite políčko „Flip“. V druhom riadku zaškrtnite políčko „Flip“ a nastavte hodnotu „% Blow“ na 90. V treťom riadku nastavte hodnotu „% Blow“ na 80. (Pozri obr. 9.4.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Contact“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_09_hammer_multiple_operation/2d_mobl9_image0004.jpg' | relative_url }})

Upraviť tabuľku Blow

## Vytváranie kontaktu medzi objektmi

Na stránke „Kontakt“ kliknite na tlačidlo vzťahu medzi obrobkom a obrobkom ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}), aby ste v roletovom menu nastavili hodnotu šmykového trenia na **0******.2** 5 – **Teplé tvárnenie** (pozri obr. 9.5.), Hodnota 0,25 sa pridá ako hodnota šmykového trenia a po nastavení hodnoty koeficientu prenosu tepla (HTC) na **Tvarovanie** sa automaticky pridá hodnota 0,004 (pozri obr. 9.6.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_09_hammer_multiple_operation/2d_mobl9_image0005.jpg' | relative_url }})

Okno definície údajov o deformáciách medzi objektmi

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_09_hammer_multiple_operation/2d_mobl9_image0006.jpg' | relative_url }})

Okno definície údajov o tepelnej interakcii medzi objektmi

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna „Kontakt“; keďže podmienky trenia sú rovnaké pre všetky páry objektov, tlačidlom ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných. Po vykonaní tejto operácie budú mať všetky vzťahy definované trenie 0,25 a HTC 0,004. Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určite vhodnú toleranciu kontaktu (vypočíta sa hodnota približne 0,00099"), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}), aby sa vygenerovali kontakty pre všetky vzťahy (pozri obr. 9.7.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Vytvorenie databázy.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_09_hammer_multiple_operation/2d_mobl9_image0007.jpg' | relative_url }})

Vytvorený vzťah s kontaktom

## Vytvorenie databázy

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) spustíte kontrolu programu, či sa pri nastavení úlohy niečo neprehliadlo. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli zadať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), aby ste spustili simuláciu.

## Spustenie simulácie

Kliknite na ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“. Po kliknutí na možnosť „Spustiť“ sa otvorí dialógové okno „Spustiť simuláciu“. Použite predvolenú možnosť **Pokračovať v spúšťaní** na výber možnosti „**Pokračovať od posledného kroku**“ a potom vyberte režim simulácie **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

Priebeh simulácie je možné počas jej vykonávania sledovať v režime Simulácia prostredníctvom okien Simulačné správy a Simulačná grafika. Kliknutím na kartu Simulačné správy zobrazíte súbor správ. Pokiaľ je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) (čo je predvolené nastavenie), súbor správ sa bude aktualizovať každých pár sekúnd.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia práve nachádza, a tiež informácie o tom, ako dobre simulácia prebieha.

Po ukončení simulácie sa na koniec súboru LOG pridá nasledujúca správa:

„VŠETKY OPERÁCIE BOLI UKONČENÉ.“

****

**Súvisiace témy:**

[15\. Movement Controls Settings]({{ '/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/' | relative_url }})

[6.2. Integrated Manufacturing Process Simulation layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/' | relative_url }})

[6.3. Integrated Manufacturing Process Post-processor layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/' | relative_url }})

[25\. Post Processor Layout]({{ '/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/' | relative_url }})
