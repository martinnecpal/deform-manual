---
lang: sk
title: "26.6.14. Sledovanie objemu"
---

# 26.6.14. Sledovanie objemu ![]({{ '/assets/icons/post_icons/mo_volume_tracking_icon.jpg' | relative_url }})

Metóda sledovania objemu sleduje späť oblasť podplnenia a prebytku materiálu od hotového dielu až po predformu. Tieto informácie sa použijú na aktualizáciu tvaru predformy. 

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_14_volume_tracking/image001.jpg' | relative_url }})

Okno „Zaujímavá oblasť“

  
Používateľ sa môže v sprievodcovi sledovania objemu pohybovať pomocou tlačidla ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}) alebo môže prejsť priamo na konkrétnu stránku kliknutím na príslušnú voľbu.

**ROI**: Používateľ môže definovať okno ROI importom geometrie zo súboru. Oblasť mimo ROI sa považuje za oblasť výkovku. Pre oblasť vnútri ROI sa vypočíta plocha a objem podplnenia a tieto údaje sa spätne priradia k pôvodnému polotovaru. Používateľ musí definovať oblasť záujmu (ROI) pre sledovanie objemu (pozri obr. 26.6.14.1.).

**Analýza**: Po definovaní oblasti záujmu (ROI) môže používateľ v okne „Analýza“ pomocou tlačidla „Analýza“ zobraziť oblasti s nedostatočným vyplnením a prebytkom materiálu na obrobku. Na obrázku je červenou farbou označená oblasť s nedostatočným vyplnením a modrou farbou oblasť s prebytkom materiálu; v okne Analýza môžeme tiež pozorovať objem nedostatočného vyplnenia a objem prebytku materiálu spolu s ich percentuálnym podielom (pozri obr. 26.6.14.2). 

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_14_volume_tracking/image002.jpg' | relative_url }})

Okno analýzy sledovania objemu

**Späť:** Po analýze môže používateľ prejsť na stránku „Späť“ a kliknutím na tlačidlo „Späť“ spustiť výpočet objemu spätne až po počiatočný polotovar. Používateľ môže pomocou prehliadača krokov prejsť na prvý krok, kde je k dispozícii počiatočná sochora, a môžeme pozorovať objem materiálu presunutého do prebytku (modrá farba na obr. 26.6.14.3.) a do nedopĺňania (červená farba na obr. 26.6.14.3.).

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_14_volume_tracking/image003.jpg' | relative_url }})

Okno „Späť“

**Predforma**: Po dokončení spätného výpočtu môže používateľ prejsť na stránku „Predforma“, kde na základe výsledkov spätného výpočtu vygeneruje tvar predformy. Používateľ môže tiež definovať objemovú toleranciu pre prebytok materiálu, ktorá sa zohľadní pri generovaní predformy. Predformu môže používateľ vygenerovať kliknutím na tlačidlo Generovať na stránke Predforma. Na stránke Predforma má používateľ tiež možnosť vygenerovať predformu pre celý objekt alebo pre objekt s polovičnou symetriou. (pozri obr. 26.6.14.4.)

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_14_volume_tracking/image004.jpg' | relative_url }})

Okno sledovania objemu predliskov

**Výstup**: V okne „Výstup“ je možné tvar vygenerovanej predformy uložiť do súboru s geometriou pomocou možnosti „Uložiť geometriu“ (pozri obr. 26.6.14.5.).

  
Na jemné doladenie tvaru predformy je možné zvoliť rôzne rozlíšenia. Ak je predforma vytvorená s polovičnou symetriou, používateľ môže využiť možnosť „Vytvoriť úplný model zrkadlením polovičného modelu“, ktorá umožňuje zrkadlenie geometrie polovičného modelu do úplného modelu. Po výbere možnosti „Rozlíšenie“ alebo „Vytvoriť úplný model zrkadlením polovičného modelu“ kliknite na tlačidlo „Exportovať“, aby ste vytvorili novú geometriu predformy pre vybraný model a uložili ju. Používateľ môže geometriu uložiť do súboru (ikona ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }})) alebo do knižnice (ikona ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }})) na stránke „Výstup“.

  
  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_14_volume_tracking/image005.jpg' | relative_url }})

Okno „Sledovanie objemu“
