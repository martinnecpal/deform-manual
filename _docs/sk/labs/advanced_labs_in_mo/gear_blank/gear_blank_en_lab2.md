---
lang: sk
title: "Polotovar na ozubené kolesá EN Lab 2"
---

# Cvičenie 2. Prechod z 2D do 3D: vykonanie 3D operácie po 2D operácii

Ďalšia simulácia bude pokračovať v 3D režime. Ak teda chcete spustiť predspracovanie v 3D režime, načítajte výsledky z predchádzajúcej 2D simulácie a prevedte obrobok do 3D, ako je popísané v tomto cvičení.

### Pridať operátor konvertora

Na prevod výsledkov obrobku z predchádzajúcej 2D operácie je potrebné po 2D operácii pridať operátor na prevod z 2D do 3D. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky **Konvertor z 2D na 3D** v zozname **Simulačné operátory** na karte **Explorer**, ako je znázornené na obrázku [Fig. L2.1.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab2/' | relative_url }}#Fig_L2_1_Adding_2D_to_3D_Convertor_Operator).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab2_image0001.jpg' | relative_url }})

Pridanie operátora na prevod 2D na 3D

### Výber nastavenia prevodníka

V editore operácií vyberte operátor prevodníka 2D na 3D, čím otvoríte tento prevodník. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}) otvoríte rozbaľovacie okno „Setup type“ (pozri obr. L2.2) a nastavte úlohu v dávkovom režime.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab2_image0002.jpg' | relative_url }})

Vyskakovacie okno s typom nastavenia pre prevodník z 2D do 3D

Vyberte **Y** v hornej časti **rádio** tlačidla, overte, či je **uhol otáčania** nastavený na **360** a počiatočný uhol na 0, ako je znázornené na obr. L2.3. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vyberte objekty, ktoré chcete previesť.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab2_image0003.jpg' | relative_url }})

Okno nastavení konfigurácie

### Vyberte objekty konverzie

Operátor na začiatku spracovania odovzdá všetky objekty. Keďže horná a spodná matrica sa musia vymeniť pre ďalšiu operáciu, ponechajte len objekt „Workpiece“. Vyberte teda objekt „Top die“ a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) (Odstrániť objekt) odstráňte hornú matricu. Podobným spôsobom odstráňte objekt „Bottom die“, ako je znázornené na obr. L2.4.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab2_image0004.jpg' | relative_url }})

Okno na výber objektov

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre objekty a tiež pre okná obrobkov, keďže v okne obrobku nie sú potrebné žiadne zmeny.

### Vytvorenie 3D geometrie obrobku

Skontrolujte výstupnú geometriu a uistite sa, že typ geometrie je „Solid“, potvrďte predvolený počet rezov a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_preview_button.jpg' | relative_url }}) vygenerujte 3D geometriu. (Pozri obr. L2.5)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab2_image0005.jpg' | relative_url }})

Okno na prevod geometrických jednotiek

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste vygenerovali sieť pre 3D geometriu.

### Vytvorenie 3D siete obrobku

Vyberte typ siete „tetrahedron“ a zmeňte **cieľový počet prvkov** na **20 000**. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vygenerujte 3D sieť (pozri obr. L2.6.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab2_image0006.jpg' | relative_url }})

Okno na konverziu siete

Ak sa geometria alebo sieť, prípadne oboje, neprekonvertovali v príslušných oknách, potom v okne **Konvertovať** môže používateľ konvertovať geometriu, sieť alebo oboje pre všetky objekty naraz pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) podľa stavu výberu zobrazeného v tabuľke, ako je znázornené na obr. L2.7.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab2_image0007.jpg' | relative_url }})

Okno „Previesť“ slúži na súčasnú konverziu geometrie aj siete

### Vytvorenie databázy po konverzii

V strome operácií vyberte položku „Generate DB“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vygenerovali databázu potrebnú pre 3D operáciu.

Obrobok sa v tomto bode stane vstupným materiálom pre druhú operáciu. Zachovajú sa faktory, ako sú presný tvar, deformácia (zpevnenie materiálu), poškodenie, tok kovu, rozloženie teploty (ak je vypočítané) a ďalšie informácie.

Kliknite na [Lab 3. Sequential 3D forge operation]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab3/' | relative_url }}), aby ste nastavili Lab3
