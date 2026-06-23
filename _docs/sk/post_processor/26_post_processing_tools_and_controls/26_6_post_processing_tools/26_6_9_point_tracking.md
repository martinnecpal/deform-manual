---
lang: sk
title: "26.6.9. Sledovanie bodov"
---

# 26.6.9. Sledovanie bodu ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }})

  * Sprievodca výberom bodov

  * Nastavenia sledovania bodov

**[2D, 3D]:** Funkcia sledovania bodov sa dá využiť na analýzu toku materiálu, sledovanie chýb a analýzu správania stavových premenných v danom bode. V rámci sledovania bodov môže používateľ počas simulácie sledovať viac ako 1000 bodov. Aby mohol používateľ využiť sledovanie bodov, musí najskôr vybrať body na objektoch v grafickom okne kliknutím ľavým tlačidlom myši na požadované miesta (pozri obr. 26.6.9.1. a obr. 26.6.9.2.).

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image001.jpg' | relative_url }})

Definícia sledovacích bodov pre 2D 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image002.jpg' | relative_url }})

Definícia sledovacích bodov pre 3D 

  
V závislosti od požiadaviek môže používateľ pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }}) vykonať príslušné nastavenia. Používateľ môže určiť, či sú vybrané body pohyblivé alebo pevné, formát súboru na uloženie a stavové premenné, ktoré je potrebné uložiť. (Pozri obr. 26.6.9.3.)

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image003.jpg' | relative_url }})

Okno nastavení sledovania bodov

Nakoniec kliknutím na tlačidlo ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}) sa zaznamenajú body pre všetky kroky DB a následne sa zobrazí graf stavových premenných spolu s grafom stavových premenných pre rôzne vybrané body v závislosti od času, ako je znázornené na obr. 26.6.9.4 a obr. 26.6.9.5.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image004.jpg' | relative_url }})

Grafy sledovania bodov v grafickom okne pre 2D

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image005.jpg' | relative_url }})

Grafy sledovania bodov v grafickom okne pre 3D

**Pridávanie bodov**: Body je možné pridať na trasu kliknutím ľavým tlačidlom myši na požadované miesto  
tlačidlo, keď je toto tlačidlo vybrané.

**Vymazanie bodov**: Body je možné vymazať kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_delete_current_row_icon.jpg' | relative_url }}) (Vymazať aktuálny riadok z tabuľky), čím sa vymaže jeden riadok, alebo pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}) (Vymazať všetky riadky z tabuľky), čím sa vymažú všetky zadané údaje v okne „Údaje o sledovaní bodov“.

  
**Uloženie bodov do súboru** ![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) : Táto funkcia uloží vybrané body do súboru, ktorý je možné kedykoľvek načítať späť do okna sledovania bodov v tej istej databáze alebo do iných databáz na účely sledovania bodov.

  
**Načítanie bodov zo súboru** ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}): Uložené body je možné načítať do aktuálneho objektu načítaním predtým uloženého súboru s údajmi o sledovaní bodov.

**Sprievodca výberom bodov**![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}): Keď používateľ klikne na Sprievodca výberom bodov, otvorí sa okno „Stavová premenná medzi 2 bodmi“, kde môže definovať počiatočnú a koncovú plochu/body na generovanie bodov buď v priamke, alebo podľa obrysu objektu, alebo v kruhovom vzore pre 3D. Po definovaní bodov je možné body vygenerovať pomocou tlačidla „Generovať“. Po vygenerovaní, ak klikneme na „OK“, systém presmeruje do okna sledovania bodov, kde môže používateľ vidieť vygenerované body v tabuľke a v okne zobrazenia. Kliknutím na tlačidlo „Sledovať“ spustíte sledovanie bodov a zobrazí sa graf sledovania bodov (pozri obr. 26.6.9.6. a obr. 26.6.9.7.). Ďalšie podrobnosti nájdete v [26.6.8. State varaible between 2 points](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_8_state_variables_between_2_points/)

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image006.jpg' | relative_url }})

Sprievodca výberom bodov s možnosťou nastavenia stavových premenných medzi dvoma bodmi

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image007.jpg' | relative_url }})

Sledovanie bodov pomocou sprievodcu výberom bodov

**Nastavenia sledovania bodov**![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }})

  * **Sledovanie:**

  * **Možnosť bodov: Presun bodov:** Ak zaškrtnete toto políčko, body definované na objekte sa budú pohybovať spolu s tokom materiálu.

  * **Pevné body:** Ak zaškrtnete toto políčko, body definované na objekte budú nehybné.

  * **Export:**

  * **Uloženie výsledkov do súboru:** Používateľ môže uložiť výsledky sledovania bodov vo formátoch RST alebo CSV a výsledky je možné zoradiť podľa bodov alebo krokov zaškrtnutím príslušného políčka. Predvolene sa výsledky ukladajú vo formáte RST; ak zaškrtnete políčko „Excel friendly“, výsledky sa uložia vo formáte CSV kompatibilnom s programom Excel. Zaškrtnutím políčka „Kompatibilné s Excelom“ sa zobrazia možnosti na uloženie všetkých stavových premenných alebo vybraných stavových premenných zo zoznamu vo formáte CSV. Odškrtnutím políčka „Uložiť všetko“ sa aktivujú možnosti na výber stavových premenných, ktoré sa majú uložiť. Používateľ môže pomocou tlačidla „Prechádzať“ vybrať umiestnenie na disku, kam sa majú výsledky sledovania bodov uložiť.

  * **Displej:**

  * **Osa:** Od verzie V12.01**,** má používateľ možnosť zvoliť si ako výstup na osi X buď čas, alebo zdvih.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image008.jpg' | relative_url }})

Možnosť nastavenia sledovania bodov
