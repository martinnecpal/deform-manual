---
lang: sk
title: "23.4. Monitor procesov"
---

# 23.4. Monitor procesov

23.4.1. Panel s podrobnými informáciami

23.4.2. Panel s podrobnosťami

23.4.3. Panel filtrov

23.4.4. Ďalšie možnosti v programe Process Monitor

23.4.5. Pomocný program pre simulačného klienta

  
![]({{ '/assets/images/simulator/23_deform_simulator/23_4_process_monitor/image001.jpg' | relative_url }})

Stav monitorovania procesu pre spustenú úlohu

## Panel s podrobnými informáciami 

Monitor procesov zobrazuje stav všetkých simulácií bežiacich na procesore. Tabuľka monitora procesov sa aktualizuje vždy, keď beží niektorý z licencovaných modulov (buď DEF_AMG, alebo iné podobné procesy). Monitor procesov získava informácie zo servera License Manager, aby určil stav simulácií alebo produktov zo všetkých systémov pripojených k tomu istému License Manageru, a zobrazuje príslušné informácie o vybranej databáze alebo produkte v rôznych stĺpcoch, ako napríklad: 

  * **Typ problému****** – Informácie o type problému zobrazujú názov databázy alebo produktu, ktorý sa momentálne používa.

  * **Stav** – Stav databázy/produktu. 

  * **Aktuálny krok** – Aktuálny simulačný krok príslušnej databázy.

  * **Celkový počet krokov** – Celkový počet simulačných krokov priradených v databáze.

  * **Operácie** – Možnosť ukončiť ![]({{ '/assets/icons/simulator_icons/mo_kill_button.jpg' | relative_url }}) a zmeniť poradie úloh v fronte tak, že ich posuniete nahor na ![]({{ '/assets/icons/simulator_icons/move_up_button.jpg' | relative_url }}) alebo nadol na ![]({{ '/assets/icons/simulator_icons/move_down_button.jpg' | relative_url }}).

  * **Používateľské meno** – Meno používateľa, ktorý odoslal databázu alebo používa produkt. 

  * **Počítač** – zariadenie, na ktorom beží príslušná databáza alebo sa používa daný produkt.

  * **2D/3D** – Typ geometrického modelu v databáze v aktuálnom simulačnom kroku (2D alebo 3D).

  * **Bity** – FEM beží v 32/64-bitovom režime.

  * **Verzia** – Verzia Deformu použitá na vytvorenie databázy.

  * **Čas spustenia** – Čas a dátum, kedy sa simulácia spustí.

  * **Čas ukončenia** – Čas a dátum, kedy sa simulácia ukončila.

  * **ID úlohy** – ID úlohy pridelené pre databázu/produkt.

  * **Cesta** – Zobrazuje cestu, na ktorej sa nachádza databáza.

  
Množstvo podrobných informácií, ktoré sa majú zobraziť, je možné regulovať filtrovaním informácií podľa systému alebo stavu. Stĺpce je možné zapnúť alebo vypnúť pomocou začiarkavacích políčok v paneli „Podrobnosti“. 

## **Panel s podrobnosťami**

Panel podrobností obsahuje začiarkavacie políčka, ktoré slúžia na ovládanie zobrazenia stĺpcov v zozname informácií o úlohe. Tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_pm_detail_panel.jpg' | relative_url }})Zobraziť/Skryť panel podrobností slúži na zobrazenie alebo skrytie panelu podrobností, ktorý sa nachádza v spodnej časti okna, ako je znázornené na obr. 23.4.2. Panel podrobností zobrazuje podrobnosti o úlohe vybranej v zozname informácií o úlohách. V paneli podrobností sa tiež nachádzajú začiarkavacie políčka, pomocou ktorých je možné zapnúť alebo vypnúť zobrazenie nasledujúcich stĺpcov: Cesta, Čas začatia, Čas ukončenia, 2D/3D, Verzia, Aktuálny krok, Celkový počet krokov, Meno používateľa, Počítač, Bity a ID úlohy.

![]({{ '/assets/images/simulator/23_deform_simulator/23_4_process_monitor/image002.jpg' | relative_url }})

Monitor procesu s vypínacími panelmi 

  
![]({{ '/assets/icons/simulator_icons/mo_pm_reset_column_button.jpg' | relative_url }}) **Obnoviť nastavenia stĺpcov**: Toto tlačidlo obnoví stav všetkých začiarkavacích políčok v paneli Detail na ich predvolené nastavenia. Predvolene sú začiarknuté všetky začiarkavacie políčka okrem polí „Path“ a „Bits“.

## Panel filtrov

Panel filtrov slúži na filtrovanie úloh, ktoré sa zobrazujú v zozname informácií o úlohách. Filtrovanie sa vzťahuje buď na stav spustenia úlohy, alebo na počítač, na ktorom úloha beží. ![]({{ '/assets/icons/simulator_icons/mo_pm_filter_panel_button.jpg' | relative_url }})Tlačidlo Zobraziť/Skryť panel filtrov slúži na zobrazenie alebo skrytie panelu filtrov (pozri obr. 23.4.2.). 

**Filtrovať podľa štátu**

Možnosť „**Filtrovať podľa stavu**“ umožňuje filtrovanie úloh podľa ich aktuálneho stavu. Stavmi sú „Čaká na spracovanie“, „Beží“ a „Dokončené“. Možnosti sa zapínajú alebo vypínajú kliknutím na príslušný stav. Výsledky sa zobrazia v zozname informácií o úlohách, ako je znázornené na obr. 23.4.3. Upozorňujeme, že stav „Dokončené“ sa vzťahuje iba na úlohy, ktoré sú súčasťou skupiny, napríklad úlohy DOE.

![]({{ '/assets/images/simulator/23_deform_simulator/23_4_process_monitor/image003.jpg' | relative_url }})

![]({{ '/assets/images/simulator/23_deform_simulator/23_4_process_monitor/image009.jpg' | relative_url }})

Možnosti filtrovania podľa stavu v nástroji na monitorovanie procesov 

  
**Filtrovať podľa počítača**

Možnosť „**Filtrovať podľa počítača**“ zobrazuje názvy všetkých počítačov, ktoré sú pripojené k rovnakému správcovi licencií a na ktorých beží niektorý z licencovaných modulov (vypožičaná licencia FEM alebo UI). Počítače je možné zapnúť alebo vypnúť kliknutím na príslušný počítač v zozname. Výsledky sa zobrazia v zozname informácií o úlohe, ako je znázornené na obr. 23.4.4.

![]({{ '/assets/images/simulator/23_deform_simulator/23_4_process_monitor/image004.jpg' | relative_url }})

Možnosť „Filtrovať podľa počítača“ v nástroji na sledovanie procesov

Keď sa dávkové úlohy odosielajú na viaceré simulačné servery, počítač im nie je pridelený, kým sa nezačnú vykonávať. V stĺpci „Počítač“ sa pri týchto čakajúcich úlohách zobrazujú počítače, na ktorých by sa mohli potenciálne spustiť, ako je znázornené na obr. 23.4.5. Zaškrtávacie políčko „**zahrnúť úlohy v čakacom rade**“ umožňuje zahrnúť tieto úlohy do filtra počítačov, ako je znázornené na obr. 23.4.6.

![]({{ '/assets/images/simulator/23_deform_simulator/23_4_process_monitor/image005.jpg' | relative_url }})

Úloha DOE zaradená do fronty s využitím viacerých simulačných serverov

![]({{ '/assets/images/simulator/23_deform_simulator/23_4_process_monitor/image006.jpg' | relative_url }})

Filtrovanie podľa počítača bez možnosti „Zahrnúť položky v čakacom zozname“ a s možnosťou „Zahrnúť položky v čakacom zozname“

## **Ďalšie možnosti v programe Process Monitor**

  * ![]({{ '/assets/icons/simulator_icons/mo_kill_button.jpg' | relative_url }})**Ukončiť****alebo****Odstrániť****úplne:** Týmto sa vybraná simulácia databázy okamžite „ukončí“. Všetky výpočty v aktuálnom kroku sa stratia.

  * **Zobraziť len simulačné úlohy:** Zaškrtnutím tohto políčka sa zobrazia informácie týkajúce sa iba databáz, ktoré sú v stave simulácie alebo čakajú na spracovanie; informácie týkajúce sa produktov/modulov, ktoré sú aktuálne v prevádzke, sa nezobrazia – pozri obr. 23.4.7.

![]({{ '/assets/images/simulator/23_deform_simulator/23_4_process_monitor/image007.jpg' | relative_url }})

Stav monitorovania procesov s a bez výberu možnosti „Zobraziť len simulačné úlohy“.

  * ![]({{ '/assets/icons/simulator_icons/mo_check_dead_client_button.jpg' | relative_url }}) **Skontrolovať neaktívnych klientov a vziať späť licencie**: Kliknutím na túto ikonu sa skontroluje, či existujú nejaké licencie na úlohy klientov, ktoré neboli vrátené; ak neboli vrátené, budú získané späť a sprístupnené na použitie.

  * ![]({{ '/assets/icons/simulator_icons/mo_pm_reload_job_info_button.jpg' | relative_url }})Načítať informácie o úlohe – Kliknutím na toto tlačidlo sa znovu načítajú informácie o úlohe z monitorovania licencií.

## Nástroj pre simulačného klienta

Pomocný program Simulation Client Utility slúži na zobrazenie informácií týkajúcich sa úloh v čakacom rade, ktoré boli odoslané z príslušného systému; spustiť ho možno kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_pm_simclient_button.jpg' | relative_url }}) v okne Process monitor. 

V roletovom zozname ![]({{ '/assets/icons/simulator_icons/mo_simclient_pulldown_option.jpg' | relative_url }}) môžeme vidieť nasledujúce možnosti (pozri obr. 23.4.8.),

  * **SimClient -list** : Zobrazí zoznam aktívnych simulačných úloh odoslaných z tohto klienta.

  * **SimClient -list today** : Zobrazí zoznam všetkých úloh, ktoré boli dnes odoslané na simuláciu z tohto klienta.

  * **SimClient -list rrrr-mm-dd** : Zobrazí zoznam všetkých úloh, ktoré boli odoslané v daný deň z tohto klienta.

  * **SimClient -list problem_id@problem_path** : Zobrazí informácie o príslušnej úlohe z tohto klienta na základe názvu a cesty.

  * **SimClient -query <job_group_id>**: Vypíše podrobné informácie o simulačnej úlohe na základe identifikátora skupiny úloh.

  * **SimClient -query <job_group_id> rrrr-mm-dd**: Vypíše podrobné informácie o skupine úloh na základe jej ID a dátumu.

  * **SimClient -bq_list** : Zobrazí zoznam všetkých simulačných úloh zo servera fronty dávkových úloh.

  * **SimClient -bq_kill <job_group_id>**: Ukončí simuláciu bežiacu v dávkovej fronte na základe identifikátora skupiny úloh.

  * **SimClient -copy <from> <to>:** Ručne skopíruje údaje zo vzdialeného simulačného servera na lokálny server podľa ciest uvedených v parametroch „from“ a „to“.

  * **SimClient -config** : Zobrazí alebo upraví konfiguráciu simulačných klientov.

  * **SimClient -help** : Zobrazí informácie o dostupných príkazoch a ich funkciách.

![]({{ '/assets/images/simulator/23_deform_simulator/23_4_process_monitor/image008.jpg' | relative_url }})

Okno nástroja Sim Client

**Súvisiace témy:**

[Start, Stop and Resume Simulation](/docs/en/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/)

[Queuing Simulations](23_2_interactive_and_batch_mode.htm#23_2_3_Queuing_Simulations)

[23.5. Setting up MPICH](/docs/en/simulator/23_deform_simulator/23_5_setting_up_mpich/)

[Pre-Processor](/docs/en/post_processor/post_processor_mainpg/)

[Integrated Manufacturing Process (MO)](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_integrated_manufacturing_process_layout/)

[Post- Processor](/docs/en/post_processor/post_processor_mainpg/)
