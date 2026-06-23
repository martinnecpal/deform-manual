---
lang: sk
title: "26.6.16. Interaktívne rozdeľovanie na rezy"
---

# 26.6.16. Krájanie

[3D]: Dialógové okno pre rezanie umožňuje používateľovi vyrezať rez do obrobku. Po vytvorení rezu sú v oblasti rezu viditeľné tieňované obrysy. Dialógové okno sa zobrazí tak, ako je znázornené na obr. 26.6.16.1. Rez sa dá vytvoriť kliknutím na čiaru ohraničujúceho obdĺžnika objektu. Predvolený režim pre rovinu rezu je jej definovanie bodom, na ktorom rovina leží, a vektorom, ktorý je normálny (alebo kolmý) k rovine rezu. Smer normály určuje stranu roviny, ktorá bude odrezaná. Po výbere roviny je možné zmeniť polohu bodu tak, že vyberiete hodnotu bodu, ktorá zodpovedá smeru normály roviny, a potiahnete posuvník.

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image001.jpg' | relative_url }})

Okno 3D rezania

**Režimy**: bod + normála: Zadajte bod a normálu na určenie reznej roviny. (Pozri obr. 26.6.16.2. a obr. 26.6.16.3.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image002.jpg' | relative_url }})

Príklad rezania pomocou metódy „Bod + Normála“ s jednou rovinou

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image003.jpg' | relative_url }})

Príklad rezania pomocou metódy „Bod + normála“ s dvoma rovinami

**3 body**: Zadajte tri body na určenie roviny rezu. (Pozri obr. 26.6.16.4.)

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image004.jpg' | relative_url }})

Príklad krájania pomocou metódy troch bodov pre rôzne hodnoty

**Bod+Os+Uhol**: Zadajte bod, os a uhol na určenie reznej roviny. (Pozri obr. 26.6.16.5.)

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image008.jpg' | relative_url }})

Príklad rezania pomocou metódy „bod + os + uhol“

****

**Add![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) **: pomocou tejto možnosti môže používateľ pridať rezovú rovinu.

**Delete![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) **: pomocou tejto možnosti môže používateľ odstrániť definovanú rezovú rovinu

**Cutter![]({{ '/assets/icons/pre_icons/mo_cutter_icon.jpg' | relative_url }}) **: pomocou tejto možnosti môže používateľ rozkrojiť objekt.

**Preview![]({{ '/assets/icons/pre_icons/mo_preview_icon.jpg' | relative_url }}) **: pomocou tejto funkcie môže používateľ zobraziť alebo skryť rezovú rovinu.

**Graf SV max** ![]({{ '/assets/icons/pre_icons/mo_sv_max_point_button.jpg' | relative_url }}): rez cez bod, v ktorom má stavová premenná maximálnu hodnotu.

**SV min plo** t ![]({{ '/assets/icons/pre_icons/mo_sv_min_point_button.jpg' | relative_url }}): prejsť cez bod, ktorý má minimálnu hodnotu stavovej premennej.

**Duplikovať**![]({{ '/assets/icons/pre_icons/mo_duplicate_button.jpg' | relative_url }}) : Vytvorí sadu rezacích rovín rovnobežných s vybranou rovinou. (Pozri obr. 26.6.16.6.)

**Obrátiť**: Zaškrtnite toto políčko, ak chcete obrátiť normálu vybranej reznej roviny

**Save![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) **: pomocou tejto možnosti môže používateľ uložiť geometriu 2D rezu a/alebo stavovú premennú. 2D geometriu je možné uložiť vo formátoch .IGS, DXF alebo .KEY.

**Uloženie rezacích rovín** ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ uložiť údaje o rezacích rovinách do súboru vo formáte .dss.

**Načítať roviny rezania ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}): **Pomocou tejto možnosti môže používateľ načítať uložený súbor s rovinami rezania.

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image005.jpg' | relative_url }})

Príklad duplikácie reznej roviny s 3 rezacími rovinami

**Obrátiť**: Zaškrtnite toto políčko, ak chcete obrátiť normálu vybranej reznej roviny. (Pozri obr. 26.6.16.7.)

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image007.jpg' | relative_url }})

Príklad roviny spätného rezania

**Zobrazenie rezacieho roviny** :

**Krivka**: Pri rozkrájaní objektu sa na displeji zobrazuje iba jeho obrys.

**Rovina**: Pri rezaní objektu sa na displeji zobrazuje iba povrch objektu.

**Krivka + rovina**: Pri rezaní objektu sa na displeji zobrazujú ako hranice, tak aj povrch objektu. (Pozri obr. 26.6.16.8.)

**Rozrezať všetky objekty**![]({{ '/assets/icons/pre_icons/mo_slice_all_objects_button.jpg' | relative_url }}) : rozrezať všetky zobrazené objekty pomocou vybranej roviny.

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image008.jpg' | relative_url }})

Príklad možností zobrazenia rezacieho rovinného zobrazenia

**Farba rezu**: Slúži na zapnutie a vypnutie farby rezanej roviny. (Pozri obr. 26.6.16.9.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image009.jpg' | relative_url }})

Možnosť farebného zobrazenia rezu v rovine
