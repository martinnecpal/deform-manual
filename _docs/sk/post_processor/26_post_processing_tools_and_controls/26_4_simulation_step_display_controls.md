---
lang: sk
title: "26.4. Ovládacie prvky na zobrazenie simulačných krokov"
---

# 26.4. Ovládacie prvky na zobrazenie simulačných krokov

26.4.1. Ponuka „Step“ a nástroje „Step“

26.4.2. Možnosti výberu krokov

26.4.3. Zoznam krokov

26.4.4. Relatívny pohyb

Prehliadač krokov (pozri obr. 26.4.1.) slúži na výber simulovaných krokov na kontrolu; objekt vybraného kroku sa zobrazí v grafickom okne. Okno zobrazenia krokov obsahuje možnosti výberu rôznych krokov a operácií, ako aj nástroje na rýchly výber a prehrávanie krokov. Okno zobrazenia krokov tiež zobrazuje informácie, ako sú názov simulácie, názov operácie, zdvih, čas, vybraný krok a číslo operácie. (Pozri obr. 26.4.1.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_4_simulation_step_display_controls/image001.jpg' | relative_url }})

Okno zobrazenia krokov

## Ponuka „Krok“ a nástroje v ponuke „Krok“ 

Nižšie sú vysvetlené rôzne možnosti rýchleho výberu krokov, ich prehrávania a výberu operácií. Aj v rámci **ponuky Krok** máme k dispozícii nižšie uvedené možnosti, ako je znázornené na obr. 26.4.2.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_4_simulation_step_display_controls/image006.jpg' | relative_url }})

Ponuka krokov postprocesora

**Prvý krok** ![]({{ '/assets/icons/post_icons/mo_first_step_icon.jpg' | relative_url }}): Vráťte zoznam krokov späť na prvý uložený krok.

**Posledný krok** ![]({{ '/assets/icons/post_icons/mo_last step_icon.jpg' | relative_url }}): Preskočiť zoznam krokov na posledný uložený krok.

**O krok vpred** ![]({{ '/assets/icons/post_icons/mo_next_step_icon.jpg' | relative_url }}) : Prejsť na ďalší uložený krok v zozname krokov.

****Jeden krok späť** **![]({{ '/assets/icons/post_icons/mo_prevoius_step_icon.jpg' | relative_url }}): Vráťte zoznam krokov o jeden uložený krok späť.

**Prehrávať dopredu**![]({{ '/assets/icons/post_icons/mo_play_button.jpg' | relative_url }}) : Zobrazuje kroky jeden po druhom, až kým sa od aktuálneho vybraného kroku nezobrazí posledný krok.

**Prehrávať spätne ![]({{ '/assets/icons/post_icons/mo_play_backward_icon.jpg' | relative_url }})** : Zobrazuje kroky jeden po druhom v opačnom poradí, až kým sa od aktuálne vybraného kroku nezobrazí prvý krok.

**Pozastaviť**![]({{ '/assets/icons/post_icons/mo_stop_play_backward_icon.jpg' | relative_url }}) : Pozastaví prehrávanie krokov.

**Op******e** operácia vpred ![]({{ '/assets/icons/post_icons/mo_next_oprn_icon.jpg' | relative_url }})**: Presun na posledný uložený krok aktuálnej operácie alebo na prvý uložený krok nasledujúcej operácie v zozname krokov.

****Op******e** operácia späť ** **![]({{ '/assets/icons/post_icons/mo_prev_oprn_icon.jpg' | relative_url }}): Prejsť na predchádzajúcu operáciu (posledný uložený krok) alebo na aktuálnu operáciu (prvý uložený krok) v zozname krokov.

**Simulácia** dopredu **![]({{ '/assets/icons/post_icons/mo_next_oprn_icon.jpg' | relative_url }})**: Presun na posledný uložený krok aktuálnej simulácie alebo na prvý uložený krok nasledujúcej simulácie v zozname krokov.

****Simulácia******späť**** **![]({{ '/assets/icons/post_icons/mo_prev_oprn_icon.jpg' | relative_url }}): Prejsť na predchádzajúci uložený krok predchádzajúcej simulácie alebo na prvý uložený krok aktuálnej simulácie v zozname krokov.

## Možnosti výberu krokov

Používateľ si môže z krokov uložených v databáze vybrať tie, ktoré chce zobraziť. K dispozícii sú rôzne typy výberu krokov, ako napríklad: prehľad, stručný, automatický, všetky a používateľský (dostupné aj v zozname krokov ![]({{ '/assets/icons/post_icons/mo_step_list_icon.jpg' | relative_url }})).

**Auto**: Ak je táto možnosť zvolená, systém automaticky vyberie kroky, ktoré sa majú zobraziť.

**Prvý**: Ak je táto možnosť zvolená, zobrazí sa len prvý krok všetkých operácií.

**Posledný**: Ak je táto voľba zvolená, zobrazí sa iba posledný krok zo všetkých operácií.

**Všetko**: Ak je táto možnosť zvolená, zobrazia sa všetky uložené kroky všetkých operácií v editore krokov.

**Stručný popis**: Ak je táto možnosť zvolená, v editore krokov sa zobrazujú iba prvý, posledný a jeden medziležiaci uložený krok operácií.

**Definované** používateľom: Ak je táto možnosť zvolená, zobrazia sa kroky, ktoré boli vybrané na zobrazenie zo zoznamu krokov ![]({{ '/assets/icons/post_icons/mo_step_list_icon.jpg' | relative_url }}). Pomocou tejto možnosti môže používateľ vybrať kroky, ktoré sa majú zobraziť.

## Zoznam krokov ![]({{ '/assets/icons/post_icons/mo_step_list_icon.jpg' | relative_url }})

Týmto spôsobom získate podrobnejšie informácie o všetkých uložených krokoch, ako sú číslo simulácie, číslo siete, čas, zdvih primárnej matrice, rozmery, číslo verzie a ohyb (pre 3D). V ľavom okne sa tiež zobrazuje postup operácií a v pravom okne sú k dispozícii ďalšie možnosti výberu krokov (pozri obr. 26.4.3.). Ďalšie informácie o typoch výberu krokov a možnostiach zoznamu krokov nájdete v časti [6.1.6. Step Editor](../../integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout.htm#6.1.6._Step_Editor).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_4_simulation_step_display_controls/image002.jpg' | relative_url }})

Možnosti výberu krokov v zozname krokov

## Relatívny pohyb [3D] ![]({{ '/assets/icons/post_icons/mo_relative_motion_button.jpg' | relative_url }})

S cieľom znížiť numerické chyby vyplývajúce z polohovania, aktualizácií geometrie atď. si simulačný model niekedy vyžaduje, aby používatelia umelo posúvali alebo otáčali objekty. Nová funkcia „relatívny pohyb“ umožňuje používateľom zobraziť výsledok simulácie, ktorý je identický so skutočnými procesmi (pozri obr. 26.4.4.). Používateľ môže vybrať referenčný objekt a pevnú os spolu s typom pohybu. Referenčný objekt je objekt, ktorý je v skutočnom procese nehybný, avšak na numerické účely sa naň aplikuje pohyb. Po vykonaní výberu môže používateľ kliknúť na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), na čo môže pozorovať, že všetky ostatné objekty sa budú pohybovať relatívne voči referenčnému objektu, zatiaľ čo referenčný objekt zostane nehybný podľa definovaných podmienok.

**Použitie:**

Cogging

Spinning

Tvarovanie za tepla

atď.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_4_simulation_step_display_controls/image003.jpg' | relative_url }})

Okno relatívneho pohybu

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_4_simulation_step_display_controls/image004.jpg' | relative_url }})

Okno pre prepočet typu relatívneho pohybu

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_4_simulation_step_display_controls/image005.jpg' | relative_url }})

Typ otáčania – Okno relatívneho pohybu

**Súvisiace témy:**

[26\. Post Processor Features](/docs/en/post_processor/26_post_processing_tools_and_controls/26_post_processor_features/)

[26.2. Viewport and Windows menu](/docs/en/post_processor/26_post_processing_tools_and_controls/26_2_handeling_viewports_and_windows_iin_post_processor/)
