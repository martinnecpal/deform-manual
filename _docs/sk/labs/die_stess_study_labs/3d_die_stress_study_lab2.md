---
lang: sk
title: "3D analýza napätia v čipe s laboratóriom Shrink Fit Lab"
---

# Laboratórna práca č. 3: Štúdia napätia v 3D forme

2.1. Úvod

2.2. Otvorenie súboru projektu

2.3. Pridať analýzu namáhania výlisku

2.4. Pridávanie objektov

2.5. Horná matrica

2.6. Spodná forma

2.7. Horná opora

2.8. Spodná opora

2.9. Definícia vzťahu medzi objektmi

2.10. Ovládacie prvky simulácie

2.11. Vytvorenie databázy

2.12. Následné spracovanie

## Úvod

Cieľom tohto laboratórneho cvičenia je vykonať analýzu napätí v lisovacej forme. Ak sa analýza napätia vykonáva len na jednom nástroji, na získanie presných hodnôt napätia stačí jednokroková simulácia. Ak sa analýza napätia vykonáva na zostavách lisovacích nástrojov, kde dochádza k interakcii medzi nástrojmi, zvyčajne je potrebných viac ako jeden krok, aby sa sústava nástrojov dostala do rovnovážneho stavu pri pôsobiacom zaťažení.

Pri typickej simulácii namáhania lisovacích foriem sa obrobok odstráni a sily, ktoré obrobok pôsobí na lisovacie formy, sa interpolujú na nástroje. V tomto laboratórnom cvičení sa bude modelovať aj montáž s kontrakčným uložením.

## Otvorenie súboru projektu

Otvorte predtým simulovaný súbor [**Spike_Forging.moproj**]({{ '/docs/sk/labs/basic_labs/3d_labs/lab03_spike_forging/' | relative_url }}) v ![]({{ '/assets/icons/pre_icons/mo_integrated_manufacturing_proc.jpg' | relative_url }}) (integrovaný výrobný proces DEFORM) v [Lab03 Spike Forging]({{ '/docs/sk/labs/basic_labs/3d_labs/lab03_spike_forging/' | relative_url }}), ako je znázornené na obr. 3DDSL2.1. Otvorí sa používateľské rozhranie integrovaného výrobného procesu.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0001.jpg' | relative_url }})

Otvorenie súboru projektu z hlavného okna grafického používateľského rozhrania

## Pridať štúdiu o namáhaní lisovacej formy

V ľavom hornom rohu okna zobrazenia kliknite ľavým tlačidlom myši na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) a vyberte operáciu **Pridať analýzu napätia v čipe**, ako je znázornené na obr. 3DDSL2.2.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0002.jpg' | relative_url }})

Doplnenie štúdie o namáhaní výliskov

Operácia „Die stress“ sa automaticky pridá do editora operácií na novej karte, ako je znázornené na obr. 3DDSL2.3. Ak chcete vykonať operáciu „Die stress“, vyberte **krok 90** na stránke výberu krokov, ako je znázornené na obr. 3DDSL2.3. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0003.jpg' | relative_url }})

Pridanie operácie „Die stress“ z programu Explorer

## Pridávanie objektov

Potrebujeme dva nové objekty, aby sme mohli analyzovať vplyv tepelného zúženia na hornú maticu a zabezpečiť oporu pre spodnú maticu. Stlačením tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) pridajte dva objekty a pomenujte ich „Horná opora“ a „Spodná opora“, ako je znázornené na obr. 3DDSL2.4. Pre všetky objekty zvolíme typ „Elastic“. Keďže horná matrica už má sieť, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím prejdete na stránku objektu „Top die“.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0004.jpg' | relative_url }})

Pridávanie objektov

## Horná matrica

### Definícia objektu „Top die“

V predvolenom nastavení sa typ tuhých objektov z načítaného kroku zmení na pružný. Pre objekt „Top Die“ ponechajte typ objektu ako pružný. Od verzie v13.1.1 boli na stránke objektu zavedené dve nové možnosti na umiestnenie lisovacích foriem v budúcich krokoch pri analýze napätia lisovacích foriem vo viacerých krokoch. Pri analýze napätia lisovacích foriem v jednom kroku tieto možnosti nemusíme používať, preto nechajte políčko Potrebné umiestnenie nezaškrtnuté. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku Materiál.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0013.jpg' | relative_url }})

Na začiatok stránky objektu „Die“

### Priradiť materiál

V okne „Materiál“ vyberte materiál **AISI-H-13**, ako je znázornené na obr. 3DDSL2.6, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0005.jpg' | relative_url }})

Okno „Materiál“

### Priradenie okrajových podmienok

  1. Vyberte **hraničnú podmienku symetrickej roviny** a následne pridajte hraničnú podmienku ku každej zo symetrických rovín hornej matrice, ako je znázornené na obr. 3DDSL2.7.

  2. Na hornú plochu hornej matrice nastavte okrajovú podmienku rýchlosti **Vz = 0**. Táto okrajová podmienka zabraňuje odletu matrice pri pôsobení síl. (Pozri obr. 3DDSL2.8.) Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Interpolácia síl“.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0006.jpg' | relative_url }})

Nastavenie okrajových podmienok symetrie

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0007.jpg' | relative_url }})

Priradenie rýchlosti BCC

### Interpolácia síl pre hornú formu

Na stránke „Interpolácia sily“ kliknite na názov akcie „![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }})“, ako je znázornené na obr. 3DDSL2.9. Kliknutím na „![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})“ prejdite na stránku „Spodná matrica“.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0008.jpg' | relative_url }})

Okno „Interpolácia sily“

## Spodná matrica

### Definícia objektu spodnej matrice

Pre spodnú formu ponecháme typ objektu „Elastic“ a zrušíme zaškrtnutie políčka „Potrebné polohovanie“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Materiál“.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0014.jpg' | relative_url }})

Stránka objektu „Spodná matrica“

### Priradiť materiál

V okne „Materiál“ vyberte materiál **AISI-H-13**, ako je znázornené na obr. 3DDSL2.6, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

###  Priradenie okrajových podmienok

Vyberte okrajovú podmienku „Rovina symetrie“ a následne pridajte okrajovú podmienku ku každej z rovín symetrie, ako je znázornené na obrázku [ Fig. 3DDSL2.11.]({{ '/docs/sk/labs/die_stess_study_labs/3d_die_stress_study_across_multiple_operations/' | relative_url }}#Fig_3DDSL3_11_Interpolated_forces_onto_Punch_from_Billet). Použijeme objekt „Dolná opora“, aby sme zabránili odletu spodnej formy v smere Z. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Interpolácia síl“.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0010.jpg' | relative_url }})

Okno BCC

### Interpolácia síl pre spodnú maticu

Na stránke „Interpolácia sily“ kliknite na názov akcie „![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }})“, ako je znázornené na obr. 3DDSL2.12. Kliknutím na „![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})“ prejdite na stránku „Object3 General“.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0009.jpg' | relative_url }})

Vynútiť okno interpolácie

## Horná opora

Zmeňte názov objektu 3 na **Horná podpera** s typom objektu **Pružný**, ako je znázornené na obr. 3DDSL2.13, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0011.jpg' | relative_url }})

Stránka „Objekt hornej podpory“

### Import geometrie

Na stránke Geometria kliknite na možnosť „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **UpperSupport.STL** z inštalačnej zložky \SFTC\DEFORM\v*_*\3d\LABS. Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) skontrolujte geometriu. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Mesh“ (Sieť).

### Vytvoriť sieť

Zadajte **Cieľový počet prvkov** ako **12000**, ako je znázornené na obr. 3DDSL2.14. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Materiál.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0012.jpg' | relative_url }})

Okno na generovanie siete

### Priradiť materiál

V okne „Materiál“ vyberte materiál **AISI-H-13**, ako je znázornené na obr. 3DDSL2.6, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Priradenie okrajových podmienok

Zadajte **okrajové podmienky symetrickej roviny** na **dvoch symetrických plochách** hornej opory, ako je znázornené na obr. 3DDSL2.15.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0013.jpg' | relative_url }})

Priradenie symetrie BCC

Na **hornú plochu** nastavte okrajovú podmienku rýchlosti **Vz = 0**, aby objekt neodletel v smere osi Z, ako je znázornené na obr. 3DDSL2.16.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0014.jpg' | relative_url }})

Priradenie rýchlosti BCC

Na tento objekt sa tiež uplatňuje zúženie, preto vyberte okrajovú podmienku „Shrink Fit“. Zúženie je definované radiálne, preto je potrebné určiť os a bod. Pre túto analýzu je bod (0, 0, 0) stredom foriem a os Z je osou objektov. Ak sa zúženie aplikuje na vnútorný objekt, hodnota by mala byť záporná. Ak sa zúženie aplikuje na vonkajší objekt, hodnota by mala byť kladná. Keďže zúženie aplikujeme na vonkajší objekt, použite pre „Interference“ hodnotu 0,004 a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). Keď sa zobrazí výzva, či chcete posunúť súradnice uzlov, kliknite na ![]({{ '/assets/icons/pre_icons/mo_no_button.jpg' | relative_url }}). (Pozri obr. 3DDSL2.17.)

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0015.jpg' | relative_url }})

Správa o presune uzlových súradníc objektu

Po nastavení uvedených parametrov sa zobrazí horná podpera, ako je znázornené na obr. 3DDSL2.18.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0016.jpg' | relative_url }})

Okno s definíciou BCC

Ak si chcete lepšie prezrieť aplikované zúženie, kliknite na ikonu Object Nodes ![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}). Vykreslite vektorový graf premennej posunu pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_plot_vector_icon.jpg' | relative_url }}), aby ste si mohli prezrieť aplikované zúženie na hornej podpere, ako je znázornené na obr. 3DDSL2.19.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0017.jpg' | relative_url }})

Okno „Údaje uzla“

## Spodná opora

Zmeňte názov objektu 4 na **Lower Support** s typom objektu **Elastic**, ako je znázornené na obr. 3DDSL2.20, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0018.jpg' | relative_url }})

Stránka objektu „Spodná podpera“

### Import geometrie

Na stránke „Geometria“ kliknite na možnosť „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **LowerSupport.STL** z inštalačnej zložky \SFTC\DEFORM\v*_*\3d\LABS. Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) skontrolujte geometriu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vytvoriť sieť

Zadajte **T****arget number of Element****s** ako **14000**, ako je znázornené na obr. 3DDSL2.21., a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s materiálmi.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0019.jpg' | relative_url }})

Okno na generovanie siete

### Priradiť materiál

V okne „Materiál“ vyberte materiál **AISI-H-13**, ako je znázornené na obr. 3DDSL2.6, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Priradenie okrajových podmienok

Zadajte **okrajové podmienky symetrickej roviny** na **dvoch****symetrických****plánoch** dolnej opory, ako je znázornené na obr. 3DDSL2.22.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0020.jpg' | relative_url }})

Priradenie symetrie BCC

Na **spodnej ploche** nastavte okrajovú podmienku **rýchlosti** **Vz = 0**, aby objekt neodletel v smere osi Z. (Pozri obr. 3DDSL2.23.) Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Kontakt“.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0021.jpg' | relative_url }})

Okno s definíciami BCC

## Definícia vzťahu medzi objektmi

Na stránke „Kontakt“ dvakrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), aby ste do zoznamu pridali dva vzťahy. V prvom vzťahu vyberte ******Horná podpera** ako **Hlavný** objekt a **Horná matrica** ako **Podriadený** objekt s hodnotou trenia **0,3.** V druhom vzťahu vyberte ****Lower support**** ako **Master** a **Bottom Die****** ako **Slave** s hodnotou trenia **0,3**. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}), aby ste nastavili vhodnú toleranciu, a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktov. (Pozri obr. 3DDSL2.24.)

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0022.jpg' | relative_url }})

Okno medzi objektmi

## Ovládacie prvky simulácie

Nastavte **Počet simulačných krokov** na ******6** a **Krok na uloženie** na **1**. Nastavte **Max. uplynutý čas procesu na jeden krok** na **1** sekundu. (Pozri obr. 3DDSL2.25.)

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0023.jpg' | relative_url }})

Okno „Ovládacie prvky simulácie“

## Vytvoriť databázu

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Simuláciu spustite kliknutím na označenie akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) a výberom možnosti „Začať od posledného záporného kroku“. Po dokončení simulácie prejdite do režimu Post kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

## Následné spracovanie

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}) prejdete do režimu užívateľsky definovaných objektov, v ktorom môžete meniť vzhľad objektov. Pomocou ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}) zapnite kontakt pre hornú aj spodnú formu a obe podpery nastavte na priehľadné kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_transparent.jpg' | relative_url }}) pre každú z nich.

Táto simulácia bola spustená vo viacerých krokoch, aby sa kontakt a napätia mohli ustáliť a dosiahnuť rovnováhu.

Prejdite jednotlivými krokmi a sledujte, ako sa mení kontakt. Kontakt hornej matrice zostáva počas celej analýzy v podstate rovnaký, avšak kontakt spodnej matrice sa značne mení. Pôsobiace zaťaženie tlačí stred matrice smerom nadol, čo spôsobuje, že vonkajší priemer matrice sa zdvihne z podložky. Na konci simulácie sa kontakt stabilizoval a medzi jednotlivými krokmi sa už výrazne nemení.

Pomocou roletového menu „State Variable“ (Stavová premenná) vyneste na graf efektívne napätie a maximálne hlavné napätie, ako je znázornené na obr. 3DDSL2.26 a obr. 3DDSL2.27, ktoré predstavujú dve z najdôležitejších premenných pri simulácii napätia v lisovacej matrici.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0024.jpg' | relative_url }})

Graf premennej stavu „efektívne napätie“

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0025.jpg' | relative_url }})

Graf stavových premenných podľa princípu Stress-Max
