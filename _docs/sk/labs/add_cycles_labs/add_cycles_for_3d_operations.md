---
lang: sk
title: "Pridať cykly pre 3D operácie"
---

# Pridať cykly pre 3D operácie

1.1. Úvod

1.2. Otvorenie súboru projektu

1.3. Nastavenie projektu MO

1.3.1. Operácia 1: Prevádzka pece

1.3.2. Operácia 2: Operácia leteckej prepravy

1.3.3. Operácia 3: Odpočinok na matrici

1.3.4. Operácia 4: Tvarovanie

1.4. Úprava operácie 4

1.5. Plánované umiestňovanie

1.6. Vytvorenie databázy

1.7. Pridávanie cyklov

1.8. Stránka „Cycles“

1.9. Následné spracovanie

## Úvod

Cieľom tohto laboratórneho cvičenia je spustiť operáciu MO pomocou cyklov. Ak potrebuje používateľ spustiť tú istú deformačnú operáciu na viacerých nových dieloch s použitím tej istej sady foriem, môžeme využiť funkciu „**Cyklus**“.

## Otvorenie súboru projektu

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Názov úlohy zadajte ako „******Add_cycles_3D_lab1**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

.

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_3d_operation/image0001.jpg' | relative_url }})

Problém s definovaním okna

Spustí sa sprievodca MO spolu s oknom na zadanie názvu projektu. Do poľa pre názov projektu, ako je znázornené na obr. L1.1., v tejto relácii zadáme názov projektu „**Add_cycles_3D_lab1**“ a klikneme na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

## Nastavenie projektu MO

Najskôr budeme simulovať problém MO so štyrmi operáciami (3 operácie prenosu tepla a 1 operácia tvárnenia) v dávkovom režime, potom pridáme cykly pre operáciu tvárnenia. Pridajte teda tri 3D operácie prenosu tepla a jednu 3D operáciu tvárnenia (pozri obr. L1.2.).

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_3d_operation/image0002.jpg' | relative_url }})

Pridanie operácií prenosu tepla a tvarovania

### Operácia 1: Prevádzka pece

  * Ako typ prenosu tepla vyberte možnosť „Teplo v peci“

  * Na stránke s podmienkami procesu nastavte čas ohrevu na 3600 sekúnd, teplotu okolia na 2000 °F a koeficient konvekcie na 7,7e-6 Btu/sek/palec²/F.

  * Zaškrtávacie políčko „Prenos tepla“ zaškrtnite iba na stránke „Ovládacie prvky simulácie“.

  * V okne „Material“ načítajte materiál **AISI-8620** z knižnice materiálov DEFORM v kategórii „Steel“ pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice).

  * Na stránke „Objekty“ pridajte len jeden objekt.

  * Na stránke obrobku nastavte teplotu obrobku na 68 °F.

  * Na stránke „Geometria obrobku“ sa 3D geometria vytvára otočením 2D geometrie, preto zaškrtnite políčko „Použiť priečny rez“, aby sa 2D geometria previedla na 3D geometriu, Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a v okne 2D geometrie kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice), aby ste načítali súbor 2D geometrie **Disk_wkp.igs** z inštalačného adresára DEFORM 2D\LABS\\. Po importe 2D geometrie kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) a potom na tlačidlo „2D->3D Conversion“. V okne nastavení vyberte typ konverzie „Revolve“ a vygenerujte 3D geometriu s uhlom 360 stupňov.

  * Vytvorte sieť s použitím predvoleného počtu 32 000 prvkov.

  * Ak chcete obrobku priradiť materiál, vyberte v okne materiálov materiál „**AISI-8620**“.

  * Na stránke „Nastavenia krokov“ nastavte počet simulačných krokov na 100, pričom dĺžka každého kroku má byť 36 sekúnd, a uložte výsledky každých 10 krokov.

  * Vytvorte databázu a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k ďalšej operácii.

### Operácia 2: Letecká prepravná operácia

  * Ako typ prenosu tepla vyberte možnosť „Prenos vzduchom“.

  * Na stránke s podmienkami procesu nastavte čas prenosu na 15 sekúnd, teplotu prostredia na 68 °F a koeficient konvekcie na 7,7e-6 Btu/s/in²/F.

  * Keďže obrobok je objekt typu „Read from DB“, nemusíme definovať žiadne ďalšie vlastnosti objektu.

  * V okne „Step Controls“ nastavte počet krokov na 15 s krokom 1 sekunda a ukladanie každých 5 krokov.

  * Prejdite na stránku na generovanie databázy a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k ďalšej operácii.

### Operácia 3: Odpočinok na kockách

  * Ako typ prenosu tepla vyberte možnosť „Rest on die“.

  * Na stránke s podmienkami procesu nastavte čas prenosu na 4 s, teplotu prostredia na 68 °F a koeficient konvekcie na 7,7e-6 Btu/s/in²/F.

  * Na stránke „Top die Geometry“ sa 3D geometria vytvára otočením 2D geometrie, preto zaškrtnite políčko „Use cross section“, aby sa 2D geometria previedla na 3D geometriu, Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a v okne 2D geometrie kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice), aby ste načítali súbor 2D geometrie **Disk_top.igs** z inštalačného adresára DEFORM 2D\LABS\\. Po importe 2D geometrie kliknite na ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) a potom na tlačidlo 2D->3D Conversion. V okne nastavení vyberte typ konverzie Revolve a vygenerujte 3D geometriu s uhlom 360 stupňov.

  * Vytvorte sieť s 10 000 prvkami.

  * Na stránke „Top die material“ načítajte materiál **AISI-H-13** z knižnice materiálov DEFORM.

  * Na stránke „Geometria spodnej formy“ sa 3D geometria vytvára rotáciou 2D geometrie, preto zaškrtnite políčko „Použiť priečny rez“, aby sa 2D geometria previedla na 3D geometriu, Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a v okne 2D geometrie kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice), aby ste načítali súbor 2D geometrie **Disk_btm.igs** z inštalačného priečinka DEFORM 2D\LABS\\. Po importe 2D geometrie kliknite na ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) a potom na tlačidlo 2D->3D Conversion. V okne nastavení vyberte typ konverzie Revolve a vygenerujte 3D geometriu s otočením o 360 stupňov.

  * Vytvorte sieť s použitím 10 000 prvkov.

  * Na stránke „Materiál spodnej formy“ vyberte z okna materiálov materiál **AISI-H-13**.

  * Nastavte hornú matricu pomocou ofsetového polohovania (x = 0, y = 0 a Z = 4) v smere „Z“.

  * Na stránke s naplánovaným polohovaním definujte polohu spodnej formy ako polohu s kolíziou voči obrobku v smere „Z“.

  * Na stránke „Kontakt“ pridajte jeden vzťah, pričom „Spodná forma“ bude uvedená ako „Hlavný prvok“ a „Obrobok“ ako „Podriadený prvok“, a v roletovom menu na karte „Tepelné vlastnosti“ v položke „Koeficient prenosu tepla“ vyberte možnosť „Voľný kontakt“.

  * V okne „Step Controls“ nastavte počet krokov na 10 s krokom 0,4 sekundy a ukladanie po každých 2 krokoch.

  * Prejdite na stránku generovania databázy a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k ďalšej operácii.

### Operácia 4: Tvarovanie

  * Na stránke „Objekty“ pridajte tri objekty.

  * Na stránke „Obrobok“ vyberte prepínač „Načítať z databázy“.

  * Podobne vyberte aj pre ostatné dva objekty voľbu „Prečítať z databázy“.

  * Na stránke „Top die Movement“ nastavte konštantný posun formy rýchlosťou 1 palec/sekundu v zápornom smere osi „Z“.

  * Na stránke s naplánovaným polohovaním definujte hornú polohu matrice ako polohu s kolíziou vo vzťahu k obrobku v zápornom smere osi „Z“.

  * Na stránke „Kontakt“ pre všetky predvolené vzťahy zoznamu vyberte možnosť „Tepelné tvárnenie (s mazáním)“. Automaticky sa vyberie hodnota trenia 0,3.

  * V okne „Step Controls“ nastavte počet krokov na 100, posun matrice na 0,0725” na krok a krok prírastku na 10 pre primárnu matricu (ktorá je v tejto operácii objektom číslo 2).

  * Prejdite na stránku na generovanie databázy, uložte projekt a vyberte kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}).

  * Spustenie simulácie. Simuláciu spustíte kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), pomocou predvolenej možnosti **Pokračovať v behu** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}).

  * Po dokončení simulácie prejdite na fázu „Post“ (následné spracovanie).

  * Po dokončení následného spracovania prejdite do predspracovateľa kliknutím na kartu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}).

## Úprava operácie 4 (Tvarovanie)

Na karte ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) vyberte operáciu 4 (Tvarovacia operácia) a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Obrobok“.

### Obrobok

Na stránke „Obrobok“ zmeňte typ objektu na „plast“ pomocou položky „Načítať z databázy“ (pozri obr. L1.3.). Po zmene typu objektu na „plast“ sa zobrazí objekt obrobku pre prvý krok 4. operácie. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Naplánované polohovanie“.

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_3d_operation/image0003.jpg' | relative_url }})

Stránka obrobku

## Plánované polohovanie

Na stránke plánovania polohovania sa musíme uistiť, že horná forma je naplánovaná tak, aby bola umiestnená na hornej strane obrobku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka generovania databázy.

## Vytvoriť databázu

Kliknite na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Keď klikneme na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), zobrazí sa nám okienko s upozornením na stratu krokov, v ktorom budeme upozornení, že ak vygenerujeme databázu, všetky kroky dostupné v rámci 4. operácie budú stratené. Na toto okienko kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). (pozri obr. L1.4.)

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_3d_operation/image0004.jpg' | relative_url }})

Vyskakovacie okno „Stratené kroky“

## Pridávanie cyklov

Po vytvorení databázy vyberte editor operácií, kliknite pravým tlačidlom myši na štvrtú operáciu a vyberte možnosť „Pridať cykly“. (pozri obr. L1.5.)

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_3d_operation/image0005.jpg' | relative_url }})

Pridávanie cyklov

## Stránka Cycles

Po pridaní cyklov kliknite na tlačidlo „Apply“, čím potvrdíte predvolený počet cyklov (5), a uložte sprievodcu (pozri obr. L1.6.). Prejdite do režimu simulácie výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknutím na označenie akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. L1.7. Použite predvolenú možnosť **Pokračovať v spustení**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, potom vyberte režim simulácie **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_3d_operation/image0006.jpg' | relative_url }})

Okno „Pridať cykly“

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_3d_operation/image0007.jpg' | relative_url }})

Okno simulačného režimu

## Následné spracovanie

V kroku „Prehliadač“ môžeme vidieť jednotlivé kroky fungovania cyklu (pozri obr. L1.8.). Prehrávajte jednotlivé kroky, aby ste videli všetky operácie cyklu.

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_3d_operation/image0008.jpg' | relative_url }})

Okno na zverejňovanie rozkrojených objektov.

**Stavová premenná:**  
V nástrojoch na príspevky vyberte možnosť „Strain-Effective“ (Deformačne efektívne), aby ste mohli skontrolovať mieru deformácie, ktorej bol obrobok vystavený. Kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) otvoríte okno „State Variable“ (Stavová premenná), vyberte stavovú premennú „Strain-Effective“ (Efektívne deformácie), kliknutím na tlačidlo „Solid display“ (Plné zobrazenie) vyberte možnosť „Solid shading“ (Plné tieňovanie) a ako možnosť „Scaling“ (Mierka) vyberte ![]({{ '/assets/icons/post_icons/mo_local_scaling_radio_button.jpg' | relative_url }}). Táto možnosť použije lokálne minimálne a maximálne efektívne deformácie ako krajné hodnoty na farebnej lište. Mierku, tieňovanie a ďalšie nastavenia kontúrového grafu je možné zmeniť aj pomocou možností pravého tlačidla myši na farebnej lište. Prejdite jednotlivými krokmi simulácie a sledujte akumuláciu deformácie (pozri obr. L1.9.). Graf teploty zobrazuje teplotu obrobku spolu s teplotou lisovacích foriem, keďže sme v operácii tvárnenia vytvorili lisovacie formy na základe údajov z objektov databázy, pre všetky operácie cyklu sa používajú rovnaké lisovacie formy a môžeme sledovať zmeny teploty lisovacích foriem v priebehu operácií cyklu (pozri obr. L1.11.).

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_3d_operation/image0009.jpg' | relative_url }})

Graf efektívneho napätia pre rezané objekty

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_3d_operation/image0010.jpg' | relative_url }})

Graf pôsobenia napätia pre rezané objekty

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_3d_operation/image0011.jpg' | relative_url }})

Graf teploty pre rozrezané objekty
