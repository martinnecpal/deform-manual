---
lang: sk
title: "26.6.13. Nastavenie sledovania užívateľsky definovaných premenných"
---

# 26.6.13. Nastavenie sledovania užívateľsky definovanej premennej ![]({{ '/assets/icons/post_icons/mo_set_user_defined_state_variable_tracking_icon.jpg' | relative_url }})

To umožňuje používateľovi vykonávať následné spracovanie používateľsky definovaných premenných, ktoré sú definované v používateľských rutínach postprocesora. To sa vykoná výberom súboru DLL vygenerovaného z užívateľskej rutiny, čísla rutiny (pozri obr. 26.6.3.1.) v okne Sledovanie užívateľsky definovaných premenných a kliknutím na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}), čo užívateľovi umožňuje vybrať objekt a typ výpočtu (pozri obr. 26.6.13.2.) Kliknutím na ![]({{ '/assets/icons/post_icons/mo_flownet_track_data_button.jpg' | relative_url }}) sa začnú sledovať stavové premenné. Po sledovaní premenných budú k dispozícii na zobrazenie v dialógovom okne stavových premenných v skupine „User“ (pozri obr. 26.6.13.3.).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_13_set_user_defined_variable_tracking/image001.jpg' | relative_url }})

Okno vlastností knižnice používateľsky definovaných premenných

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_13_set_user_defined_variable_tracking/image002.jpg' | relative_url }})

Okno „Vlastnosti sledovania“ pre premenné definované používateľom

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_13_set_user_defined_variable_tracking/image003.jpg' | relative_url }})

Používateľom definované premenné príspevkov, ku ktorým sa pristupuje z okna „Premenné stavu“

Po dokončení sledovania premenných pre konkrétnu databázu sa v adresári problému vygeneruje súbor PDB, takže v nasledujúcich fázach následného spracovania môže používateľ na karte „Sledovanie“ vybrať existujúci súbor PDB a následne priamo vykresliť svoje premenné.  
Užívateľská rutina postprocesora je k dispozícii v štandardnom inštalačnom umiestnení,  
C:\Program files\SFTC\DEFORM\v*_*\UserRoutine\PostProcessor\PC_pstusr23.f (kde *_* je číslo verzie programu Deform) pre PC. Ďalšie informácie o užívateľských rutinách postprocesora nájdete v [Chapter 56. User routine.](/docs/en/user_routines/56_user_routines_in_deform/56_user_routines_in_deform/)
