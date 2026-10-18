---
lang: sk
title: "Laboratórna úloha č. 12: Napätie v matrici s držiakom"
---

# Laboratórna úloha č. 12: Napätie v matrici s držiakom

V tomto laboratórnom cvičení vykonávame analýzu napätia v matrici v rámci projektu Spike_Nonisothermal a pridávame jeden dodatočný objekt s názvom „Holder“, ktorý slúži na podoprenie spodnej matrice.

12.1. Otvorenie súboru projektu

12.2. Pridať analýzu napätia v matrici

12.3. Výber kroku

12.4. Pridať objekt

12.5. Nastavenie hornej matrice

12.6. Nastavenie spodnej matrice

12.7. Nastavenie držiaka

12.8. Vytvorenie kontaktu

12.9. Ovládacie prvky simulácie

12.10. Vytvorenie databázy

12.11. Spustenie simulácie

12.12. Následné spracovanie výsledkov

## Otvorenie súboru projektu

Otvorte v programe DEFORM MO predtým simulovaný súbor **Spike_NoniSothermal.moproj**, ako je znázornené na obr. L12.1. Otvorí sa predspracovateľ programu MO.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0001.jpg' | relative_url }})

Hlavná obrazovka DEFORM GUI

## Pridať analýzu napätia v matrici

Ak je [Lab 06 Die Stress operation]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_06_die_stress/' | relative_url }}) už hotové, po otvorení projektu Spike_Nonisothermal sa zobrazí karta „Die stress Study 1“, ako je znázornené na obr. L12.2. V ľavom hornom rohu okna „Display“ kliknite ľavým tlačidlom myši na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }})“ a vyberte operáciu „Add Die stress Study“, ako je znázornené na obr. L12.2.

V editore operácií bola k operácii „Napätie v lisovacej forme“ pridaná záložka „Štúdia napätia v lisovacej forme“, ako je znázornené na obr. L12.3.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0001.jpg' | relative_url }})

Pridanie operácie s napätím v matrici

## Výber kroku

Ak chcete vykonať operáciu „Die stress“, vyberte na stránke výberu krokov **krok 50**, ako je znázornené na obr. L12.3. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0002.jpg' | relative_url }})

Zoznam výberu krokov

## Pridať objekt

Pridajte jeden objekt kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) na stránke „Objekty“ (pozri obr. L12.4.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top die BCC“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0003.jpg' | relative_url }})

Stránka „Pridávanie objektov“

## Nastavenie hornej matrice

### Definícia objektu „Top die“

V predvolenom nastavení sa typ tuhých objektov z načítaného kroku zmení na pružný. Pre objekt „Top Die“ ponechajte typ objektu ako pružný. Od verzie v13.1.1 boli na stránke objektu zavedené dve nové možnosti na umiestnenie foriem v budúcich krokoch pri analýze napätia foriem vo viacerých krokoch. Pri analýze napätia foriem v jednom kroku tieto možnosti nemusíme používať, preto nechajte políčko „Potrebné umiestnenie“ nezaškrtnuté. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na stránku „Horná forma“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0018.jpg' | relative_url }})

Na začiatok stránky objektu

### Nastavenie okrajovej podmienky

Na hornú plochu hornej matrice nastavte okrajovú podmienku rýchlosti **Vy = 0**. Táto okrajová podmienka zabraňuje odletu matrice pri pôsobení síl (pozri obr. L12.6.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Interpolácia síl“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0004.jpg' | relative_url }})

Na začiatok stránky BCC

### Vynútená interpolácia

Na stránke „Interpolácia sily“ kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) a po vykonaní interpolácie sily sa v zozname správ zobrazí správa o interpolácii sily (pozri obr. L12.7). Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Spodná matrica“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0005.jpg' | relative_url }})

Okno interpolácie sily hornej matrice

## Nastavenie spodnej matrice

### Definícia objektu spodnej matrice

Pre spodnú formu ponecháme typ objektu ako „Elastic“ a zrušíme zaškrtnutie políčka „Need positioning“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka BCC, kde priradíte okrajové podmienky.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0019.jpg' | relative_url }})

Stránka objektu „Spodná matrica“

### Spodná matica BCC

Na stránke BCC zaškrtnite predvolenú deformáciu BCC pre ľavú stranu obrobku v smere osi X; predvolené BCC sa priradia automaticky na základe výberu typu úlohy ako osovo symetrickej (pozri obr. L12.9.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Interpolácia síl.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0006.jpg' | relative_url }})

Stránka „Spodná matrica BCC“

### Vynútená interpolácia

Kliknite na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) a po vykonaní interpolácie sily sa v zozname správ zobrazí správa o interpolácii sily (pozri obr. L12.10). Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Objekt 4“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0007.jpg' | relative_url }})

Vynútiť okno interpolácie

## Držiak

### Definícia objektu „Holder“

Pre **HOLDER** vyberieme typ objektu **Elastic** a zrušíme zaškrtnutie políčka „Potrebné polohovanie“ (pozri obr. L12.11.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})., aby ste prešli na stránku Geometria a vytvorili geometriu. 

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0008.jpg' | relative_url }})

Stránka objektu „Holder“

### Vytvorenie geometrie pre držiak

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a vytvorte geometriu tak, že do tabuľky zadáte nasledujúce hodnoty súradníc XYR (pozri obr. L12.12.) a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte stránku „Edit“. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

**X** |  **Y** |  **R**  
---|---|---  
4 |  -3 |  0  
4 |  -1 |  0  
1 |  -1 |  0  
1 |  -3 |  0  
  
Hodnota súradníc XYR v geometrii

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0009.jpg' | relative_url }})

Dialógové okno „Upraviť geometriu“

### Vytvorenie siete pre držiak

Nastavte **počet prvkov** na **150** a vygenerujte sieť pomocou ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) (pozri obr. L12.13.), potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Material“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0010.jpg' | relative_url }})

Stránka „Holder Mesh“

### Priradenie materiálu pre držiteľa

Pre držiak zvoľte materiál **AISI-H-13** výberom zo zoznamu materiálov (pozri obr. L12.14.), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0011.jpg' | relative_url }})

Priradenie materiálu držiaka

### Nastavenie okrajovej podmienky pre Holdera

Nastavte okrajovú podmienku rýchlosti **Vy** = 0 na spodnej ploche držiaka, ako je znázornené na obr. L12.15, a potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Kontakt“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0012.jpg' | relative_url }})

Stránka držiteľa BCC

## Vytvorenie kontaktu

Na stránke „Kontakt“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), aby ste pridali vzťah **Držiak** – **Spodná matrica**, ako **Hlavný objekt** vyberte **HOLDER** a ako **Podriadený objekt** vyberte **Spodná matrica**, nastavte hodnotu trenia na **0,12** a vytvorte kontakt kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_button.jpg' | relative_url }}) (pozri obr. L12.16.), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0013.jpg' | relative_url }})

Stránka s kontaktnými údajmi

## Ovládacie prvky simulácie

V nastaveniach simulácie nastavte **Počet krokov simulácie** na hodnotu **5**, **krok na uloženie** na hodnotu **1** a **Maximálny čas trvania procesu** **na jeden krok** na hodnotu **0,1** s, ako je znázornené na obr. L12.17. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0014.jpg' | relative_url }}).

Stránka s ovládacími prvkami simulácie

## Vytvorenie databázy

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

## Spustenie simulácie

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Spustite simuláciu kliknutím na akčný štítok ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) a pomocou predvolenej možnosti **Pokračovať v behu** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Ak simulácia prebehne bez problémov, na koniec súboru so správami sa pridá nasledujúca správa: „NORMAL STOP: Simulácia bola dokončená a zastavená v časovom kroku určenom používateľom“.

## Následné spracovanie výsledkov

Po dokončení simulácie prejdite do režimu „post“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), ako je znázornené na obr. L12.18.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0015.jpg' | relative_url }})

Režim odosielania MO

**Skontrolujte výsledné napätie vo všetkých objektoch**

Kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}), vykreslite **efektívne napätie** a **maximálne hlavné napätie** a sledujte graf, ako je znázornené na obr. L12.19 a obr. L12.20. Tieto dve veličiny sú najdôležitejšími premennými pri simulácii napätia v lisovacej forme.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0016.jpg' | relative_url }})

Graf pôsobenia napätia v zobrazení s plným tieňovaním

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/2d_mobl12_image0017.jpg' | relative_url }})

Graf maximálneho hlavného napätia v líniovom zobrazení

Ak chcete pokračovať v ďalšom laboratórnom cvičení [13 Die Stress with Shrink Fit]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/' | relative_url }}), nezatvárajte projekt MO. Pozrite si [Lab 13 Die Stress with Shrink Fit]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/' | relative_url }}).

****

**Súvisiace témy:**

[11\. General Object Data Definition]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }})

[14\. Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/' | relative_url }})

[6.2. Integrated Manufacturing Process Simulation layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/' | relative_url }})

[6.3. Integrated Manufacturing Process Post-processor layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/' | relative_url }})

[25\. Post Processor Layout]({{ '/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/' | relative_url }})
