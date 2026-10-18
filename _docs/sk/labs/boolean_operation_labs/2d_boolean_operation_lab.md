---
lang: sk
title: "Laboratórium 2D booleovských operácií"
---

# Laboratórium s 2D booleovskými operáciami

1.1. Úvod

1.2. Vytvorenie nového problému

1.3. Pridávanie 2D operácií tvárnenia

1.4. Import súboru Rib_web_SI.KEY

1.5. Vytvorenie databázy

1.6. Následné spracovanie výsledkov

1.7. Pridanie boolovskej operácie

1.8. Výber objektov

1.9. Definovanie geometrie rezača

1.10. Vytvorenie databázy

## Úvod

V tomto laboratórnom cvičení ukážeme, ako nastaviť boolovskú operáciu pomocou vzorového kľúčového súboru „Rib Web“, aby sme odstránili odlesky v nástroji MO Wizard.

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. 2DBL1.1. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**SI**“. Názov úlohy zadajte ako „**2D_Boolean_Lab**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image014.jpg' | relative_url }})

Okno na výber umiestnenia problému

## Pridávanie 2D tvárniacich operácií

Otvorí sa sprievodca viacerými operáciami s novým projektom s názvom **2D_Boolean_Lab**, v ktorom môžete nastaviť úlohu. Zoznamu operácií v Průzkumníku pridajte operáciu 2D Forming. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie 2D Forming (pozri obr. 2DBL1.2.) alebo ju môžete pridať aj pretiahnutím do oblasti Editor operácií.

![]({{ '/assets/images/labs/boolean_operation_labs/2d_boolean_operation_lab/image0001.jpg' | relative_url }})

Do editora operácií bola pridaná operácia 2D tvárnenia

##  Import súboru Rib_web_SI.KEY

Naimportujte súbor **Rib_web_SI.KEY** z inštalačnej zložky programu DEFORM \2D\2D_Examples\SI\Forging Directory pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka na vytvorenie databázy.

## Vytvorenie databázy

Na stránke „Generate DB“. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) necháte program skontrolovať, či sa pri nastavení úlohy na niečo nezabudlo.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“ (od kroku -1), potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) sa spustí simulácia.

Ak simulácia prebehne bez problémov, na koniec súboru so správami sa pridá nasledujúca správa: „NORMAL STOP: Simulácia bola dokončená a zastavená v časovom kroku určenom používateľom“.

## Následné spracovanie výsledkov

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), kde si môžete prezrieť výsledky; otvorí sa postprocesor MO. Prejdite jednotlivými krokmi, aby ste si prezreli tvar obrobku (pozri obr. 2DBL1.3.).

![]({{ '/assets/images/labs/boolean_operation_labs/2d_boolean_operation_lab/image0002.jpg' | relative_url }})

Okno postprocesora MO

## Pridanie booleovskej operácie

Kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) – otvorí sa predspracovateľ MO. 

V tejto operácii definujeme oblasť, ktorá má mať v oblasti flashu boolovskú hodnotu.

V Průzkumníku pridajte zoznamu Operácie operátor Boolean 2D. V editore operácií kliknite na operátor Boolean 2D (pozri obr. 2DBL1.4.).

![]({{ '/assets/images/labs/boolean_operation_labs/2d_boolean_operation_lab/image0003.jpg' | relative_url }})

Pridanie boolovského operátora 2D

## Výber objektov

V predvolenom nastavení sa obrobok prenesie do booleovskej operácie. V prípade potreby môžeme preniesť objekty foriem pomocou možnosti „Preniesť objekt do nasledujúcej operácie“ v kontextovom menu pravého tlačidla myši. (Pozri obr. 2DBL1.5.)

![]({{ '/assets/images/labs/boolean_operation_labs/2d_boolean_operation_lab/image0004.jpg' | relative_url }})

Odovzdanie objektu do booleovskej operácie

Ak používateľ nechce, aby sa výsek presunul na ďalšiu operáciu, nie je potrebné výseky presúvať. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Geometria rezačky“.

## Definovanie geometrie frézy

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a vytvorte geometriu dvoch slučiek na odstránenie prebytku materiálu z obrobku, ako je znázornené na obr. 2DBL1.6 a obr. 2DBL1.7. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím sa dostanete na stránku na vytvorenie databázy. 

![]({{ '/assets/images/labs/boolean_operation_labs/2d_boolean_operation_lab/image0005.jpg' | relative_url }})

Slučky v geometrii

![]({{ '/assets/images/labs/boolean_operation_labs/2d_boolean_operation_lab/image0006.jpg' | relative_url }})

Definovanie boolovskej geometrie

## Vytvorenie databázy

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Po vytvorení databázy prejdite na časť „Post“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

Teraz prejdite na krok s booleovskou operáciou a pozrite sa na obrobok. Používateľ môže tiež skontrolovať stavové premenné interpolované na novú sieť obrobku po vykonaní booleovskej operácie.

![]({{ '/assets/images/labs/boolean_operation_labs/2d_boolean_operation_lab/image0007.jpg' | relative_url }})

Obrobok po boolovskej operácii

![]({{ '/assets/images/labs/boolean_operation_labs/2d_boolean_operation_lab/image0008.jpg' | relative_url }})

Rozloženie deformácie obrobku po booleovskej operácii

![]({{ '/assets/images/labs/boolean_operation_labs/2d_boolean_operation_lab/image0009.jpg' | relative_url }})

Rozloženie poškodenia obrobku po boolovskej operácii
