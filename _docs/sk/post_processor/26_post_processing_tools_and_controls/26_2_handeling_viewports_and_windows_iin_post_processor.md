---
lang: sk
title: "26.2. Práca s oknom zobrazenia a oknami v postprocesore"
---

# 26.2. Práca s zobrazením a oknami v postprocesore

26.2.1. Ponuka „Viewport“

26.2.2. Ponuka Windows

## Ponuka „Viewport“

Obr. 26.2.1. znázorňuje položky ponuky „Viewport“ v postprocesore; používateľ má k dispozícii možnosti „Multi-viewport“, „Porovnanie databázy“ pre vybranú databázu, „Prepojiť databázu“, „Prepojiť krok“, „Synchronizovať zobrazenie“, „Synchronizovať stavovú premennú“ a „Synchronizovať graf X-Y“ spolu s možnosťou „Porovnanie databázy“, Obnoviť, Prispôsobiť zobrazenie, Zobraziť späť, Izometrické zobrazenie, Posunúť obrazovku nahor, Načítať zobrazenie, Uložiť zobrazenie a možnosti osvetlenia. 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_2_viewports/image001.jpg' | relative_url }})

Ponuka „Viewport“ v postprocesore 

  * **Viac zobrazení** ![]({{ '/assets/icons/post_icons/mo_multi_viewport_icon.jpg' | relative_url }}): Okno „Display“ je štandardne v režime jedného zobrazenia, je však možné ho rozdeliť na maximálne 8 zobrazení. Táto možnosť pomáha používateľovi porovnávať súčasne rôzne kontúry stavových premenných a grafy tej istej databázy. (Pozri obr. 26.2.2.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_2_viewports/image002.jpg' | relative_url }})

Viacnásobný zobrazený okno

  * **Databáza odkazov** ![]({{ '/assets/icons/post_icons/mo_link_database_icon.jpg' | relative_url }}): 

**Odkaz na**: ukazuje ten istý krok vo viacerých databázach

**Odkaz nefunkčný**: zobrazuje rôzne kroky v rôznych databázach

  * **Krok s odkazom** ![]({{ '/assets/icons/post_icons/mo_link_steps_icon.jpg' | relative_url }}):

**Databáza odkazov**: Odkaz na: zobrazuje ten istý krok vo viacerých databázach

**Odkaz nefunkčný**: zobrazuje rôzne kroky v rôznych databázach

  * **Zobrazenie synchronizácie** ![]({{ '/assets/icons/post_icons/mo_sync_view_icon.jpg' | relative_url }}):

**Synchronizácia zapnutá**: používa (synchronizuje) rovnaké zobrazenie (posun/zoom/otočenie), výber objektov vo viacerých zobrazeniach

**Synchronizácia vypnutá**: používať nezávislé zobrazenie (posúvanie/zoomovanie/otáčanie), výber objektov vo viacerých zobrazeniach

  * **Synchronizačná stavová premenná** ![]({{ '/assets/icons/post_icons/mo_sync_state_variable_icon.jpg' | relative_url }}):

**Synchronizácia zapnutá**: používať (synchronizovať) tú istú stavovú premennú vo viacerých zobrazeniach

**Synchronizácia vypnutá**: v rôznych zobrazeniach sa používa nezávislá stavová premenná

  * **Synchronizácia X-Y Plot![]({{ '/assets/icons/post_icons/mo_sync_x-y_plot_icon.jpg' | relative_url }})** :

**Synchronizácia zapnutá**: použiť (synchronizovať) rovnakú akciu vo viacerých zobrazeniach

**Synchronizácia vypnutá**: používajte nezávislé akcie vo viacerých zobrazeniach.

Medzi funkcie budú patriť rozdeľovanie, graf zaťaženia a zdvihu a súhrnný graf.

  * **Database Compassion** ![]({{ '/assets/icons/post_icons/mo_database_comparison_icon.jpg' | relative_url }}): Poskytuje nástroje na prepojenie rôznych databáz na základe rozsahu prepojenia, metódy prepojenia a typu prepojenia na účely porovnania. (Pozri obr. 26.2.3.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_2_viewports/image003.jpg' | relative_url }})

Porovnanie databáz

**Metóda relatívneho prepojenia**: Prepojenie sa vykonáva pomocou normalizovaných hodnôt kroku, zdvihu a času v rámci zvoleného rozsahu.

  * **Obnoviť (F5)** ![]({{ '/assets/icons/pre_icons/mo_refresh_icon.jpg' | relative_url }}) : Ikona obnovenia znovu vykreslí obrazovku, odstráni všetky meracie značky a aktualizuje všetky zmeny vykonané v farebnej palete.

  * **Prispôsobiť zobrazenie (F3):** Prispôsobí všetky zobrazené objekty alebo grafy tak, aby sa zmestili do aktuálneho zobrazenia.

  * **Zobraziť predchádzajúci pohľad (F4):** Vráti objekty do predchádzajúcej zobrazenj pozície.

  * **Izometrický pohľad** ![]({{ '/assets/icons/pre_icons/mo_iso_view_icon.jpg' | relative_url }}): Táto voľba zobrazí izometrický pohľad aktuálneho zobrazenia. Táto voľba nie je k dispozícii pre 2D systémy. Tieto voľby nie sú k dispozícii v 2D režime, keďže sa naň nevzťahujú.

  * **Obrazovka smerom nahor** : ****[3D]: Táto voľba zobrazuje izometrický pohľad v 3D tak, že vybraná os bude smerovať nahor. Napríklad, ak používateľ v možnosti „Obrazovka smerom nahor“ vyberie kladnú os Z, ako je znázornené na obr. 26.2.4., a následne zvolí možnosť izometrického pohľadu, os Z bude v izometrickom pohľade smerovať nahor. Toto neplatí pre 2D režim.

  
![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image005.jpg' | relative_url }})

Možnosti ponuky zobrazenia smerom nahor

  * ******Ponuka „Viewport“****![]({{ '/assets/icons/pre_icons/mo_plus_x_view_icon.jpg' | relative_url }}), **![]({{ '/assets/icons/pre_icons/mo_minus_x_view_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_plus_y_view_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_minus_y_view_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_plus_z_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_minus_z_icon.jpg' | relative_url }}) : ****Na nižšie uvedenom obr. 26.2.5. sú zobrazené možnosti ponuky „Viewport“. Pomocou týchto možností alebo ikon na paneli nástrojov môže používateľ obnoviť alebo prispôsobiť zobrazenie, prepnúť na izometrické alebo akékoľvek smerové zobrazenie, nastaviť os smerujúcu nahor, uložiť a načítať zobrazenia a meniť nastavenia osvetlenia zobrazení. 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image011.jpg' | relative_url }})

Rôzne možnosti výberu zobrazenia

  * **Načítanie a uloženie zobrazenia:** Používateľ môže presúvať alebo meniť pohľady na geometrie pomocou nástrojov na zobrazenie, ako sú posúvanie, dynamické priblíženie a priblíženie pomocou rámčeka v okne zobrazenia. Tieto pohľady je možné uložiť pomocou možnosti „Uložiť“ dostupnej na karte „Zobrazenie“, ako je znázornené na obr. 26.2.6.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image013.jpg' | relative_url }})

Uložiť okno zobrazenia – Možnosti ponuky

Ak sa pohľad uloží ako lokálny výrez, tento pohľad sa uloží iba pre aktuálny pracovný projekt a je možné ho zobraziť pomocou možnosti načítania, ako je znázornené na obr. 26.2.7. Ak je pohľad uložený ako globálny pohľad, nastavené pohľady sa stanú predvolenými pohľadmi pre akýkoľvek projekt. Aby sa globálne pohľady aktivovali pre projekty, musí používateľ ukončiť aktuálny projekt. Používateľ môže kopírovať globálne pohľady ako lokálne pohľady pomocou možnosti „Načítať“ a lokálne pohľady ako globálne pohľady pomocou možnosti „Uložiť“.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image012.jpg' | relative_url }})

Načítať možnosti ponuky okna zobrazenia

  * **Osvetlenie**: Táto funkcia umožňuje používateľovi meniť jas a farbu osvetlenia grafického okna; je tiež možné pridať ďalšie vypínače osvetlenia a ovládať ich polohy, ako je znázornené na obr. 26.2.8., obr. 26.2.9. a obr. 26.2.10.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image014.jpg' | relative_url }})

Okno „Všeobecné vlastnosti osvetlenia“

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image015.jpg' | relative_url }})

Okno vlastností „Nastavenia osvetlenia“

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image016.jpg' | relative_url }})

Okno „Pokročilé vlastnosti svetla“

Pozri kapitolu [ 8\. Pre-Processor Layout](/docs/en/pre_processor/8_pre_processor_layout/8_pre-processor_layout/), časť [Set Lighting Property](../../pre_processor/8_pre_processor_layout/8_pre-processor_layout.htm#Set_Lighting_Property).

## Ponuka Windows

Na obr. 26.2.11 je zobrazené menu programu Post-Processor v okne Windows; v zozname Windows sú k dispozícii možnosti Detach, Testify, Tile, Tile Horizontally a Tile Vertically. Tieto možnosti fungujú vtedy, keď v programe Post-Processor otvoríme dve alebo viac databáz.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_2_viewports/image004.jpg' | relative_url }})

Ponuka postprocesora v systéme Windows 

  * **Oddeliť**: Ak v ponuke Windows zvolíte možnosť „Oddeliť“, okná so zoznamami jednotlivých databáz sa budú zobrazovať samostatne a nebudú prispôsobené veľkosti zobrazeného okna.

  * **Testify**: Ak v ponuke Windows vyberiete možnosť Testify, zobrazí sa okno so zoznamom jednotlivých databáz v podobe zoznamu kariet.

  * **Tile** : Ak v ponuke Windows vyberiete možnosť Tile, okná jednotlivých databáz sa zobrazia v dlaždicovom zobrazení.

  * **Usporiadať horizontálne**: Ak je v ponuke Windows zvolená možnosť „Usporiadať horizontálne“, okná jednotlivých databáz sa zoradia horizontálne.

  * **T******ile** Vertically**: Ak je v ponuke Windows zvolená možnosť „Tile Horizontally“, okná jednotlivých databáz sa zoradia vertikálne.

**Súvisiace témy:**

[8\. Pre-Processor Layout](/docs/en/pre_processor/8_pre_processor_layout/8_pre-processor_layout/)
