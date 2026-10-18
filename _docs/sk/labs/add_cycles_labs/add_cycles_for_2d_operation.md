---
lang: sk
title: "Pridať cykly pre 2D operáciu"
---

# Pridať cykly pre 2D operáciu

1.1. Úvod

1.2. Otvorenie súboru projektu

1.3. Nastavenie projektu MO

1.3.1. Operácia 1: Prevádzka pece

1.3.2. Operácia 2: Operácia leteckého prevozu

1.3.3. Operácia 3: Odpočinok na matrici

1.3.4. Operácia 4: Tvarovanie

1.4. Úprava operácie 4

1.5. Plánované umiestnenie

1.6. Vytvorenie databázy

1.7. Pridávanie cyklov

1.8. Stránka „Cycles“

1.9. Následné spracovanie

## Úvod

Cieľom tohto laboratórneho cvičenia je spustiť operáciu MO pomocou cyklov. Ak potrebuje používateľ spustiť tú istú deformačnú operáciu na viacerých nových dieloch s použitím tej istej sady foriem, môžeme využiť funkciu „Cyklus“.

## Otvorenie súboru projektu

Vytvorte novú úlohu buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nová úloha**, alebo kliknutím na ikonu Nová úloha ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. L1.1. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Názov úlohy zadajte ako „******Add_cycles_2D_lab1**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „Zobraziť dialógové okno s možnosťami“, nezobrazí sa vám dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problém s definovaním okna

Spustí sa sprievodca MO spolu s oknom na zadanie názvu projektu; definovaný názov úlohy sa aktualizuje na „**Add_cycles_2D_lab1**“ ako názov projektu a aktualizuje sa vybraný systém jednotiek. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pridáte projekt.

## Nastavenie projektu MO

Najskôr budeme simulovať problém MO (viacnásobná operácia) so štyrmi operáciami (3 operácie prenosu tepla a 1 operácia tvárnenia) v dávkovom režime, potom pridáme cykly pre operáciu tvárnenia. Pridajte teda tri 2D operácie prenosu tepla a jednu 2D operáciu tvárnenia (pozri obr. L1.2.).

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_2d_operation/image001.jpg' | relative_url }})

Pridanie operácií prenosu tepla a tvárnenia

###  Operácia 1: Prevádzka pece

  * Ako typ geometrie vyberte „2D osovo symetrická“.

  * Ako typ prenosu tepla vyberte možnosť „Teplo v peci“.

  * Na stránke s podmienkami procesu nastavte čas ohrevu na 3600 sekúnd, teplotu okolia na 2000 °F a koeficient konvekcie na 7,7e-6 Btu/sek/in²/F.

  * Zaškrtávacie políčko „Prenos tepla“ zaškrtnite iba na stránke „Ovládacie prvky simulácie“.

  * V okne „Materiál“ načítajte materiál **AISI** -**8620** z knižnice materiálov DEFORM v kategórii „Oceľ“ pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice).

  * Na stránke „Objekty“ pridajte len jeden objekt.

  * Na stránke s obrobkom nastavte teplotu obrobku na 68 °F.

  * Na stránke „Geometria obrobku“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a naimportujte súbor „**Disk_wkp****.****igs**“ z priečinka 2D\LABS. Geometriu skontrolujte a opravte pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}).

  * Vytvorte sieť s použitím 2000 prvkov.

  * Ak chcete obrobku priradiť materiál, vyberte v okne materiálov materiál „**AISI****-8620**“.

  * Na stránke „Nastavenia krokov“ nastavte počet simulačných krokov na 100, pričom dĺžka každého kroku je 36 sekúnd, a uložte nastavenia každých 10 krokov

  * Vytvorte databázu a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k ďalšej operácii.

### Operácia 2: Letecká preprava

  * Ako typ prenosu tepla vyberte možnosť „Prenos vzduchom“.

  * Na stránke s podmienkami procesu nastavte čas prenosu na 15 sekúnd, teplotu prostredia na 68 °F a koeficient konvekcie na 7,7e-6 Btu/s/in²/F.

  * Keďže obrobok je objekt typu „Read from DB“, nemusíme definovať žiadne ďalšie vlastnosti objektu.

  * V okne „Step Controls“ nastavte počet krokov na 15 s krokom 1 sekunda a ukladanie každých 5 krokov.

  * Prejdite na stránku generovania databázy a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k ďalšej operácii.

### Operácia 3: Odpočinok na kockách

  * Ako typ prenosu tepla vyberte možnosť „Rest on die“.

  * Na stránke s podmienkami procesu nastavte čas prenosu na 4 s, teplotu prostredia na 68 °F a konvekčný koeficient na 7,7e-6 Btu/s/in²/F.

  * Na stránke „Top die Geometry“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a načítajte súbor „**Disk_top****.igs**“ z priečinka 2D\LABS. Geometriu skontrolujte a opravte pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}).

  * Vytvorte sieť s použitím 600 prvkov.

  * Na stránke „Top die material“ načítajte materiál **AISI-H13** z knižnice materiálov DEFORM.

  * Na stránke „Geometria spodnej matrice“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a načítajte súbor „**Disk_btm****.igs**“ z adresára 2D\LABS. Geometriu skontrolujte a opravte pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}).

  * Vytvorte sieť s použitím 600 prvkov.

  * Na stránke „Materiál spodnej matrice“ vyberte v okne materiálov materiál **AISI-H13**.

  * Umiestnite hornú matricu pomocou posunu (x=0, y=4) v smere osi Y.

  * Na stránke „Plánované polohovanie“ definujte polohu spodnej formy ako polohu s kolíziou vo vzťahu k obrobku v smere osi Y.

  * Na stránke „Kontakt“ pridajte jeden vzťah, kde „Spodná forma“ bude ako „Hlavný prvok“ a „Obrobok“ ako „Podriadený prvok“. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) a v roletovom menu na karte „Tepelná“ vyberte pre koeficient prenosu tepla možnosť „Voľný kontakt“.

  * V okne „Step Controls“ nastavte počet krokov na 10 s krokom 0,4 sekundy a ukladanie po každých 2 krokoch.

  * Prejdite na stránku generovania databázy a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k ďalšej operácii.

### Operácia 4: Tvarovanie

  * Na stránke „Objekty“ pridajte tri objekty.

  * Na stránke „Obrobok“ vyberte volič „Načítať z databázy“.

  * Podobne vyberte aj pre ostatné dva objekty volič „Čítať z databázy“.

  * Na stránke „Top die Movement“ nastavte konštantný pohyb formy s hodnotou 1 palec/sekundu v zápornom smere osi „Y“.

  * Na stránke „Plánované polohovanie“ definujte hornú polohu matrice ako polohu s kolíziou vo vzťahu k obrobku v zápornom smere osi Y.

  * Na stránke „Kontakt“ pre všetky predvolené vzťahy vyberte zo zoznamu možnosť „Tepelné tvárnenie (s mazáním)“. Automaticky sa vyberie hodnota trenia 0,3.

  * V okne „Step Controls“ nastavte počet krokov na 100, rýchlosť posuvu matrice na 0,0725” na krok a krok prírastku na 10 pre primárnu maticu (ktorá je v tejto operácii objektom č. 2).

  * Prejdite na stránku na generovanie databázy, uložte projekt a vyberte kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}).

  * Simuláciu spustíte kliknutím na akčný štítok ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), pomocou predvolenej možnosti **Pokračovať v behu** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}).

  * Po dokončení simulácie prejdite na fázu Post na následné spracovanie.

  * Po dokončení následného spracovania prejdite do predspracovávacieho modulu kliknutím na kartu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}).

##  Úprava operácie 4

Na karte ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) vyberte operáciu 4 (tvarovacia operácia) a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Obrobok“.

### Obrobok

Na stránke „Obrobok“ zmeňte typ objektu na „plast“ v položke „Načítať z databázy“ (pozri obr. L1.3.). Po zmene typu objektu na „plast“ sa zobrazí objekt obrobku pre prvý krok 4. operácie. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka „Naplánované polohovanie“.

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_2d_operation/image002.jpg' | relative_url }})

Stránka obrobku

## Plánované polohovanie

Na stránke plánovaného umiestnenia sa musíme uistiť, že horná matrica je naplánovaná tak, aby bola umiestnená na hornej strane obrobku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka generovania databázy.

## Vytvoriť databázu

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Keď klikneme na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), zobrazí sa nám okienko s upozornením na stratu krokov, v ktorom budeme upozornení, že ak vytvoríme databázu, všetky kroky dostupné v rámci 4. operácie budú stratené. Na toto okienko kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). (pozri obr. L1.4.)

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_2d_operation/image003.jpg' | relative_url }})

Vyskakovacie okno „Stratené kroky“

## Pridávanie cyklov

Po vytvorení databázy vyberte editor operácií, kliknite pravým tlačidlom myši na štvrtú operáciu a vyberte možnosť „Pridať cykly“ (pozri obr. L1.5.).

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_2d_operation/image004.jpg' | relative_url }})

Pridávanie cyklov

## Stránka Cycles

Po pridaní cyklov kliknite na tlačidlo „Apply“, aby ste potvrdili predvolený počet cyklov **5** a uložili sprievodcu (pozri obr. L1.6.). Prejdite do režimu simulácie výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. L1.7. Použite predvolenú možnosť **Pokračovať v spustení**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, potom vyberte režim simulácie **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_2d_operation/image005.jpg' | relative_url }})

Okno „Pridať cykly“

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_2d_operation/image006.jpg' | relative_url }})

Okno režimu simulácie

## Následné spracovanie

V kroku „Prehliadač“ môžeme vidieť jednotlivé kroky operácie Cycles (pozri obr. L1.8.). Prehrajte si jednotlivé kroky, aby ste videli všetky operácie cyklu.

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_2d_operation/image007.jpg' | relative_url }})

Okno príspevku

**Stavová premenná:**

V nástrojoch príspevku vyberte možnosť „Strain-Effective“, aby ste si prezreli mieru deformácie, ktorú obrobok utrpel. Kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) otvoríte okno „State Variable“ (Stavová premenná), vyberte stavovú premennú „Strain-Effective“ (Efektívne deformácie), vyberte vyplnenie „Solid“ (Plná farba) kliknutím na tlačidlo „Solid display“ (Zobrazenie plnou farbou) a ako možnosť „Scaling“ (Mierka) vyberte ![]({{ '/assets/icons/post_icons/mo_local_scaling_radio_button.jpg' | relative_url }}). Táto možnosť použije lokálne minimálne a maximálne efektívne deformácie ako krajné hodnoty na farebnej lište. Mierku, tieňovanie a ďalšie nastavenia kontúrového grafu je možné zmeniť aj pomocou možností pravého tlačidla myši na farebnej lište. Prejdite jednotlivými krokmi simulácie a sledujte akumuláciu deformácie (pozri obr. L1.9.). Graf teploty zobrazuje teplotu obrobku spolu s teplotou lisovacích foriem, keďže sme lisovacie formy vytvorili na základe údajov z objektov databázy v operácii tvárnenia, pre všetky operácie cyklu sa používajú rovnaké lisovacie formy a môžeme sledovať zmenu teploty lisovacích foriem počas operácií cyklu (pozri obr. L1.11.).

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_2d_operation/image008.jpg' | relative_url }})

Graf efektívneho napätia

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_2d_operation/image009.jpg' | relative_url }})

Graf pôsobenia napätia

![]({{ '/assets/images/labs/add_cycles_labs/add_cycles_for_2d_operation/image010.jpg' | relative_url }})

Graf teploty
