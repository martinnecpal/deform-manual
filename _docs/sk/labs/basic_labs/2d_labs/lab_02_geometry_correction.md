---
lang: sk
title: "Laboratórna práca č. 02 – Oprava geometrie"
---

# Cvičenie 02 – Oprava geometrie

2.1. Vytvorenie nového problému

2.2. Pridanie operácie tvárnenia

2.3. Typ geometrie

2.4. Pridanie objektu

2.5. Úprava geometrie

2.6. Uloženie úlohy

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené nižšie na obr. L2.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno grafického rozhrania DEFORM

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. L2.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Názov úlohy zadajte ako „**Junk**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili novú úlohu s použitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa sprievodca hromadnými operáciami s dialógovým oknom Nový projekt (pozri obr. L2.3.). V tomto bode bude používateľ vyzvaný, aby zadal názov projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názov tejto relácie. V tejto relácii použijeme ako názov projektu „**Junk**“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0003.jpg' | relative_url }})

Okno na výber miesta problému

Používateľ môže tiež zmeniť systém jednotiek (systém jednotiek vybraný v ponuke Súbor sa nastaví ako predvolený) a pridať operáciu výberom z roletového zoznamu „Prvá operácia“ a zaškrtnutím príslušného políčka (pozri obr. L2.4.). Pomocou možnosti „Kopírovať existujúci projekt“ môžeme importovať predtým uložené projekty ako nové projekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0002.jpg' | relative_url }})

Priradenie názvu problému

## Pridanie formovacej operácie

Otvorí sa sprievodca viacerými operáciami s novým projektom s názvom „Junk“. Zoznamu operácií v prehliadači pridajte operáciu „2D Forming“. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky „2D Forming“ alebo ju môžete pridať aj pretiahnutím do editora operácií. (Pozri obr. L2.5.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0003.jpg' | relative_url }})

Sprievodca MO s 2D tvarovacou operáciou

## Typ geometrie

Pre toto laboratórne cvičenie je v poriadku predvolený typ geometrie (osovo symetrický). Na nastavenie úlohy si používateľ môže vybrať požadovaný typ geometrie. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Objekty“.

## Pridanie objektu

V tomto laboratórnom cvičení potrebujeme len jeden objekt. Ak sa v zozname objektov už nachádzajú tri objekty, odstráňte posledné dva objekty kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) a v zozname ponechajte len objekt „Workpiece“ (pozri obr. L2.6.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s geometriou obrobku.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0004.jpg' | relative_url }})

Pridávanie objektov

## Úprava geometrie

Na stránke „Geometria“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}), ako je znázornené na obr. L2.7. Otvorí sa okno na úpravu geometrie, ako je znázornené na obr. L2.8.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0005.jpg' | relative_url }})

Okno Geometria

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0006.jpg' | relative_url }})

Okno „Upraviť geometriu“

V okne 2D Geometry Editor zadajte do tabuľky nasledujúce súradnice XYR, ako je znázornené na obr. L2.9.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0007.jpg' | relative_url }})

Editor 2D geometrie

Kliknutím na ikonu „Zobraziť čísla vrcholov ![]({{ '/assets/icons/pre_icons/mo_show_vertex_numbers_icon.jpg' | relative_url }})“ sa vytvorenej geometrii priradia čísla v každom bode, ako je znázornené na obr. L2.10.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0008.jpg' | relative_url }})

Geometria so zobrazením normálnych vektorov

Pomocou ikony Box Zoom ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) zväčšite priesečník týchto dvoch oblúkov. Používateľ môže vidieť, že koncové body týchto dvoch oblúkov sa nesústreďujú správne, ako je znázornené na obr. L2.11. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0009.jpg' | relative_url }})

Zobrazenie geometrie chyby

Definovaná geometria sa zobrazí v okne „Display“, ako je znázornené na obr. L2.12.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0010.jpg' | relative_url }})

Geometria v okne zobrazenia

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}). Malo by sa zobraziť okienko so správou „Geometria bola opravená“, ako je znázornené na obr. L2.13. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pre zobrazenie kontextového menu. V závislosti od veľkosti prvku a predvolenej tolerancie, ktorú systém zvolil, môže byť pri niektorých opravách potrebných viac pokusov alebo zvýšenie hodnoty tolerancie na základe úsudku používateľa.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_02_geometry_correction/lab2_image0011.jpg' | relative_url }})

Vyskakovacie okno „Skontroluj geometriu“

Predvolené nastavenia korekcie fungovali v prípade tejto geometrie dobre a vytvorili medzi oboma oblúkmi tenkú čiaru.

## Uloženie problému

Výberom možnosti Export v ponuke Súbor uložte súbor kľúčových slov pre daný problém pod názvom „Junk“. Údaje sa uložia do súboru Junk.KEY.

****

**Súvisiace témy:**

[12.2. 2D Geometry Data Editing]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/' | relative_url }})
