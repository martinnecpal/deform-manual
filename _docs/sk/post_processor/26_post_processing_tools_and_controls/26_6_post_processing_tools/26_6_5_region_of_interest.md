---
lang: sk
title: "26.6.5. Oblasť záujmu"
---

# 26.6.5. Oblasť záujmu

  * Oblasť záujmu

  * Vrátenie sa späť

  * Vrátenie sa späť – príklad

**Zaujímavá oblasť**

Oblasť záujmu (ROI) je ľubovoľný tvar (2D alebo 3D), ktorý vymedzuje oblasť, ktorá je pre používateľa zaujímavá z hľadiska posudzovania výsledkov.

  
Tieto oblasti možno použiť na získanie minimálnych a maximálnych hodnôt stavových premenných pre konkrétnu oblasť v objekte. Kontúrové grafy možno oříznúť tak, aby zachytávali len požadovanú oblasť.

  
Oblasť záujmu je možné definovať tak, že najskôr pridáte oblasti pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať oblasť). Používateľ musí dvakrát kliknúť na pridanú oblasť, aby mohol upraviť jej názov a definovať jej geometriu pomocou geometrických nástrojov. (Pozri obr. 26.6.5.1., obr. 26.6.5.2. a obr. 26.6.5.3.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image001.jpg' | relative_url }})

Definícia oblasti záujmu pre 2D 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image002.jpg' | relative_url }})

Definícia oblasti záujmu pre 3D 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image003.jpg' | relative_url }})

3D zobrazenie oblastí záujmu v drôtenom zobrazení

Definovanú geometriu je možné umiestniť pomocou možnosti polohovania, ako je znázornené na obr. 26.6.5.4.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image004.jpg' | relative_url }})

Určenie polohy oblasti záujmu

Po definovaní geometrie sledovaných oblastí vyberte tieto oblasti a kliknutím na tlačidlo ![]({{ '/assets/icons/post_icons/mo_generate_region_mesh_button.jpg' | relative_url }}) vygenerujte sieť pre tieto oblasti. V prípade 3D modelu je možné nastavenia siete pre každú oblasť individuálne upraviť na karte „Mesh“, ako je znázornené na obr. 26.6.5.5.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image005.jpg' | relative_url }})

Okno nastavení siete oblasti záujmu 3D modelu

Používateľ môže vykresliť stavovú premennú objektu s oblasťami a pomocou nastavení v stromovej štruktúre objektov ovládať viditeľnosť týchto oblastí. Tým sa zobrazí kontúrový graf pre konkrétne oblasti. Príklady výškových grafov pre 2D príklad rebrového výstuže sú uvedené na obr. 26.6.5.6 a pre 3D príklad nosiča ozubeného kolesa sú uvedené na obr. 26.6.5.7.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image006.jpg' | relative_url }})

Príklad 2D rebrového výstuže s kontúrami efektívneho deformácie v oblasti záujmu

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image007.jpg' | relative_url }})

Príklad 3D nosiča ozubeného kolesa s kontúrami efektívneho deformácie v oblasti záujmu

**Vrátenie sa späť**

**(2D)** : Pre 2D objekty je teraz k dispozícii možnosť spätného sledovania ako oblasti záujmu, ktorá umožňuje sledovať túto oblasť späť v surovom materiáli po procese tvárnenia. Môžeme tiež vykresliť stavové premenné v rámci tvaru oblasti záujmu, ktorá bola spätne sledovaná.

  
Používateľ musí pridať oblasť záujmu (ROI) a definovať jej geometriu, na čo sa aktivuje možnosť „Back Track“. Teraz kliknite na tlačidlo „Back Track“, aby systém začal vypočítavať oblasť spätného sledovania. Po dokončení spätného sledovania si používateľ môže všimnúť, že sa zobrazuje iba oblasť záujmu vybraná na spätné sledovanie (pozri obr. 26.6.5.8.).

  
Použite tlačidlo „Prehrávať späť“ a sledujte, ako sa oblasť vracia späť do počiatočného stavu. Môžeme tiež znázorniť stavovú premennú a sledovať jej rozloženie v oblasti spätného sledovania.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image008.jpg' | relative_url }})

Po vytvorení Back Tracku

**Príklad:**

  * Naimportujte súbor **MO2_Heatup_Rest_Upset_Boolean_EN_new**.DB z inštalačnej zložky 2D/LABS v programe NG a prejdite na posledný krok (pozri obr. 26.6.5.9.),

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image009.jpg' | relative_url }})

Databáza bola načítaná v poslednom kroku

  * V ponuke Súbor vyberte možnosť Exportovať a uložte súbor s kľúčom pod názvom „**MachinedShape.KEY**“ (pozri obr. 26.6.5.10.).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image010.jpg' | relative_url }})

Uloženie súboru objektu pomocou možnosti Exportovať

  * Teraz načítajte krok 1628 (záverečný krok operácie 3)

  * Otvorte oblasť záujmu (ROI), kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) na pridanie novej oblasti záujmu a kliknite na ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), vyberte súbor „**MachinedShape.KEY**“ a na stránke výberu objektov vyberte objekt obrobku (pozri obr. 26.6.5.11).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image011.jpg' | relative_url }})

Otvorte uložený súbor s kľúčom na stránke „Oblasť záujmu“

  * Kliknite na ![]({{ '/assets/icons/post_icons/mo_generate_region_mesh_button.jpg' | relative_url }}); po vytvorení siete sa aktivuje možnosť ![]({{ '/assets/icons/post_icons/mo_back_track_button.jpg' | relative_url }}) a vytvorená oblasť siete sa zvýrazní červenou farbou (pozri obr. 26.6.5.12.)

.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image012.jpg' | relative_url }})

Po vytvorení siete oblasti záujmu

  * Teraz kliknite na ![]({{ '/assets/icons/post_icons/mo_back_track_button.jpg' | relative_url }}). Po dokončení výpočtov spätného sledovania sa zobrazí oblasť vybraná na spätné sledovanie, ako je znázornené na obr. 26.6.5.13.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image013.jpg' | relative_url }})

Do zoznamu v stromovej štruktúre objektov a do ponuky pravého tlačidla myši bola pridaná možnosť vrátiť sa späť

  * Teraz zatvorte okno ROI, spustite animáciu „Backward“ a sledujte zobrazenú oblasť (pozri obr. 26.6.5.14.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image014.jpg' | relative_url }})

Zobrazenie regiónu „Back Track“

  * Zobrazenie objektu s možnosťami „Back Track Off“ a „Back Track On“ (pozri obr. 26.6.5.15.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_5_region_of_interest/image015.jpg' | relative_url }})

Možnosti vrátenia sa späť v RMB v stromovej štruktúre objektov
