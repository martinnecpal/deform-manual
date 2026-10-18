---
lang: sk
title: "Polotovar na ozubené kolesá SI Lab 2"
---

# Cvičenie 2. Prechod z 2D do 3D – vykonanie 3D operácie po 2D operácii

Ďalšia simulácia bude pokračovať v 3D režime. Ak chcete teda spustiť predspracovanie v 3D režime, načítajte výsledky z predchádzajúcej 2D simulácie a prevedite obrobok do 3D, ako je popísané v tomto cvičení.

### Pridať operátor „Convertor“

Na prevod výsledkov obrobku z predchádzajúcej 2D operácie je potrebné po 2D operácii pridať operátor na prevod z 2D do 3D. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky „2D to 3D Convertor“ v zozname simulačných operátorov na karte **Explorer![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Operácie**, ako je znázornené na obrázku [Fig. L2.1.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab2/' | relative_url }}#Fig_l2_1_Adding_2D_to_3D_Convertor_Operator)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab2_image0001.jpg' | relative_url }})

Pridanie operátora na konverziu z 2D na 3D

### Výber nastavenia prevodníka

V editore operácií vyberte operátor prevodníka 2D na 3D, čím otvoríte tento prevodník. Stlačte tlačidlo ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}), čím sa zobrazí rozbaľovacie okno „Setup type“ (pozri [Fig. L2.2.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab2/' | relative_url }}#Fig_L2_2_Setup_type_popup_for_operation_2_2D_to_3D_converter)), a nastavte úlohu v dávkovom režime.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab2_image0002.jpg' | relative_url }})

Vyskakovacie okno s typom nastavenia pre operáciu 2 – Konvertor z 2D do 3D

Vyberte rádio tlačidlo **Y** is up, overte, či je **revolution****angle** nastavený na **360** a **start****angle** na **0**, ako je znázornené na obrázku [Fig. L2.3.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab2/' | relative_url }}#Fig_L2_3_Configuration_settings_window). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vyberte objekty, ktoré chcete previesť.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab2_image0003.jpg' | relative_url }})

Okno nastavení konfigurácie

### Vyberte objekty na konverziu

Operátor na začiatku procesu odovzdá všetky objekty. Keďže horná a spodná matrica sa musia vymeniť pre nasledujúcu operáciu, ponechajte len objekt „Workpiece“. Vyberte teda objekt „Top die“ a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) (Odstrániť objekt) odstráňte hornú matricu. Podobným spôsobom odstráňte objekt „Bottom die“, ako je znázornené na [Fig. L2.4.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab2/' | relative_url }}#Fig_L2_4_Object_selection_window).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab2_image0004.jpg' | relative_url }})

Okno na výber objektov

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre objekty a tiež pre okná obrobkov, keďže v okne obrobku nie sú potrebné žiadne zmeny.

### Vytvorenie 3D geometrie obrobku

Skontrolujte výstupnú geometriu a uistite sa, že typ geometrie je „Solid“ (teleso), potvrďte predvolený počet sekcií a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_preview_button.jpg' | relative_url }}), aby ste vygenerovali 3D geometriu (pozri [Fig. L2.5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab2/' | relative_url }}#Fig_L2_5_Geometry_conversion_window)). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste vygenerovali sieť pre 3D geometriu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab2_image0005.jpg' | relative_url }})

Okno na prevod geometrických jednotiek

### Vytvoriť 3D sieť obrobku

Vyberte typ siete „tetrahedron“ a zmeňte „Cieľový počet prvkov“ na **20 000**. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) vygenerujte 3D sieť (pozri [Fig. L2.6.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab2/' | relative_url }}#Fig_L2_6_Mesh_conversion_window)).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab2_image0006.jpg' | relative_url }})

Okno na konverziu siete

Ak sa geometria alebo sieť, prípadne oboje, neprekonvertovali v príslušných oknách, potom v okne **Konvertovať** môže používateľ konvertovať geometriu, sieť alebo oboje pre všetky objekty naraz pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) podľa stavu výberu zobrazeného v tabuľke, ako je znázornené na obrázku [Fig. L2.7.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab2/' | relative_url }}#Flg_l2_7_Convert_window_to_convert_both_geometry_and_mesh_at_a_time)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab2_image0007.jpg' | relative_url }})

Okno „Previesť“ slúži na súčasnú konverziu geometrie aj siete

### Vytvorenie databázy po konverzii

V strome operácií vyberte položku „Generate DB“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vygenerovali databázu potrebnú pre 3D operáciu.

Obrobok sa v tomto bode stane vstupným materiálom pre druhú operáciu. Zachovajú sa faktory, ako sú presný tvar, deformácia (zpevnenie), poškodenie, tok kovu, rozloženie teploty (ak sa vypočíta) a ďalšie informácie.

Kliknite na [Gear Blank SI Lab 3]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}), aby ste pokračovali v postupnej 3D operácii.
