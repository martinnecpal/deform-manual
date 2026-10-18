---
lang: sk
title: "Laboratórium 1: Deformácie pri 2D obrábaní"
---

# Laboratórne cvičenie č. 1: Deformácie pri 2D obrábaní

1.1. Vytvorenie nového problému

1.2. Operácia sčítania

1.3. Okno objektu

1.4. Obrobok

1.5. Inštalácia svietidiel

1.6. Definovanie počiatočného obrábacieho priechodu

1.7. Polohovanie

1.8. Plánované umiestnenie

1.9. Kontakt

1.10. Náhľad simulácie

1.11. Riadenie simulácie

1.12. Vytvorenie databázy

1.13. Spustenie simulácie

1.14. Následné spracovanie výsledkov

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené nižšie na obr. 2DMDL1.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno programu DEFORM GUI

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 2DMDL1.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Názov úlohy zadajte ako „**2D_Machining_Distortion**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „Zobraziť dialógové okno s možnosťami“, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa sprievodca viacerými operáciami, v tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**2D_Machining_Distortion**“ (pozri obr. 2DMDL1.3.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0003.jpg' | relative_url }})

Okno nového projektu

## Pridávanie operácie

Otvorí sa sprievodca viacerými operáciami. Zoznamu operácií v prehliadači pridajte operáciu 2D deformácia pri obrábaní. Operáciu je možné pridať kliknutím na tlačidlo **2D deformácia pri obrábaní** ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo ju môžete pridať aj pretiahnutím do editora operácií (pozri obr. 2DMDL1.4.).

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0004.jpg' | relative_url }})

Pridanie operácie „2D deformácia pri obrábaní“

## Okno objektu

V okne objektu sú pre toto laboratórne cvičenie potrebné 4 upínacie zariadenia a 1 priechod, preto nastavte **počet upínacích zariadení na 4** a **počet** **priechodov** na **1** (pozri obr. 2DMDL1.5.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) na pridanie objektov a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0005.jpg' | relative_url }})

Okno objektu

## Obrobok

V rámci tejto operácie načítajte informácie o objekte výberom možnosti ![]({{ '/assets/icons/pre_icons/mo_import_object.._button.jpg' | relative_url }}). Používateľ môže vyhľadať súbor databázy. Načítajte súbor „**CoolingModel****.****DB**“ z inštalačnej zložky programu Deform **\2d\LABS\Machining_Distortion\** a vyberte príslušné číslo kroku (posledný krok pre toto cvičenie) a objekt (tento model má len jeden objekt) (pozri obr. 2DMDL1.6.). Pre toto cvičenie sú k dispozícii dva súbory. Jeden súbor kľúčových slov a jeden databázový súbor pre typickú simuláciu chladenia. Uvedený súbor kľúčových slov bol spustený na vytvorenie databázového súboru. Po načítaní objektu môže používateľ zmeniť názov objektu a vybrať možnosť „init displacement“, aby sa správne zaznamenalo deformovanie spôsobené výlučne odoberaním materiálu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0006.jpg' | relative_url }})

Okno na importovanie obrobkov

Načítaný objekt obsahuje súbor okrajových podmienok deformácie z predchádzajúcej simulácie chladenia. Používateľ si ich môže overiť v nasledujúcom okne „Okrajové podmienky“ (obr. 2DMDL1.7.) a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračovať ďalej.

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0007.jpg' | relative_url }})

Okno s okrajovými podmienkami

V okne „Initialize“ sú na inicializáciu k dispozícii niektoré bežne používané stavové premenné, ako napríklad teplota, deformácia, napätie, poškodenie, rýchlosť, posunutie atď. (pozri obr. 2DMDL1.8.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0008.jpg' | relative_url }})

Inicializovať okno

## Inštalácia svietidiel

Počet upínacích prvkov sa v okne „Object“ pridáva po štyroch, ako tomu bolo aj predtým. V tomto cvičení sa používajú štyri upínacie prvky. Dva v blízkosti osi a dva v blízkosti vzdialeného konca. Je možné ich načítať (alebo definovať) v ľubovoľnom poradí. Po načítaní môže používateľ skontrolovať geometriu a v prípade potreby ju upraviť.

### Zápas č. 1

V okne „Fixture 1“ zadajte názov upínacieho prípravku (ak sa má líšiť od predvoleného) a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) načítajte/definujte geometriu upínacieho prípravku. (Obr. 2DMDL1.9.) Geometriu upínacieho prípravku je možné definovať pomocou základných tvarov (ktoré je v prípade potreby možné aj interaktívne upravovať) alebo načítať existujúci súbor s geometriou (pozri obr. 2DMDL1.10.). Pre toto laboratórne cvičenie pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Importovať geometriu z knižnice) načítajme upínací prípravok 1 ako ten vľavo dole (**lb_fixture.GEO**) zo zložky **\2d\LABS\Machining_Distortion** v inštalačnej ceste.

### Zápas č. 2

Podobne ako v prípade Fixture 1, v prípade **Fixture 2** načítajte súbor v ľavom hornom rohu (**lu_fixture.GEO**) zo zložky **\2d\LABS\Machining_Distortion** v inštalačnej ceste.

### Zápas č. 3

Podobne ako v prípade Fixture 1, v prípade **Fixture 3** načítajte spodný prvok (**rb_fixture.GEO**) zo zložky **\2d\LABS\Machining_Distortion** v inštalačnej ceste.

### Zápas č. 4

Podobne ako v prípade Fixture 1, v prípade **Fixture 4** načítate súbor v pravom hornom rohu (**ru_fixture.GEO**) zo zložky **\2d\LABS\Machining_Distortion** v inštalačnej ceste.

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0009.jpg' | relative_url }})

Okno zápasu č. 1

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0010.jpg' | relative_url }})

Okno Geometria

## Definovanie počiatočného obrábacieho cyklu

Z hľadiska modelu sú informácie o obrábacom priechode tiež geometrickými údajmi, ktoré pri prekrývaní so surovcom určujú polohu a rozsah materiálu určeného na odstránenie. Ide teda o geometrické údaje, ktoré je možné definovať/načítať rovnakým spôsobom ako upínacie prípravky v predchádzajúcom kroku. Pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Importovať geometriu z knižnice) načítajte súbor „**pass1.****GEO**“ z inštalačnej cesty v priečinku **\2d\LABS\Machining_Distortion**, ako je znázornené na obr. 2DMDL1.12. Používateľ si môže túto geometriu skontrolovať.

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0011.jpg' | relative_url }})

Okno na odovzdanie

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0012.jpg' | relative_url }})

Okno Geometria

## Umiestnenie

V tejto operácii umiestňujeme upínacie prvky vo vzťahu k polotovaru tak, aby počas vykonávania postupu obrábania predstavovali správne obmedzenia pre polotovar. Zvoľte možnosť ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}), aby ste otvorili dialógové okno „Umiestňovanie objektov“. Tu zvoľte režim umiestňovania „**Interferencia**“. Zo zoznamu objektov vyberte ako referenčný objekt „Polotovar“ a postupne vyberte upínacie prvky 1 až 4 na polohovanie. (Obr. 2DMDL1.13.) Pre každú dvojicu by mal byť na polohovanie zvolený správny smer priblíženia. Smer priblíženia pre spodné upínacie prvky by mal byť „Y“ a pre horné upínacie prvky „-Y“. Používateľ môže použiť predvolenú hodnotu kolízie a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) vykonať polohovanie pre každú upínací prvok (pozri obr. 2DMDL1.14.).

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0013.jpg' | relative_url }})

Okno ovládacích prvkov

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0014.jpg' | relative_url }})

Okno „Umiestniť objekty“

## Plánované polohovanie

Funkcia plánovaného umiestňovania umožňuje používateľovi definovať umiestnenie objektov v nastavení MO pre nasledujúce operácie, pre ktoré sa nevytvára databáza (DB), tak, aby boli objekty umiestnené ešte pred vytvorením DB počas spustenia simulácie v dávkovom režime. V rámci tohto cvičenia túto funkciu plánovaného umiestňovania nepoužívame.

## Kontakt

V tejto fáze definujeme „4“ páry objektov typu master-slave. Najskôr zadajte kontakt a v dialógovom okne Kontakt štyrikrát kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať vzťah), čím určíte štyri páry objektov. Pre každý pár postupne vyberte jedno upínacie zariadenie ako hlavné a polotovar ako podriadený. Pre toto cvičenie nedefinujeme žiadne podmienky trenia. (V prípade potreby môže používateľ zvoliť možnosť ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Upraviť) na definovanie podmienok trenia) alebo môže priamo kliknúť na ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) a pridať všetky predvolené vzťahy. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vygenerovanie kontaktných podmienok (obr. 2DMDL1.15.). V tejto fáze budú kontaktné uzly zvýraznené v zobrazovacej oblasti. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na pokračovanie.

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0015.jpg' | relative_url }})

Kontaktné okienko

## Náhľad simulácie

Náhľad simulácie poskytuje prehľad o operácii, ktorá sa má vykonať, na základe definície procesu a priechodu. V okne „Simulation preview“ (pozri obr. 2DMDL1.16.) kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) (Prehrať náhľad dopredu) sa spustí animácia, ktorá zobrazí objekt, ktorý bol po cykle odstránený (pozri obr. 2DMDL1.17.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte.

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0016.jpg' | relative_url }})

Okno náhľadu simulácie

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0017.jpg' | relative_url }})

Náhľad nastavenia

## Riadenie simulácie

Posledným krokom pri generovaní údajov pre model je nastavenie parametrov simulácie, kde ako počiatočný krok zadáme hodnotu „-1“, počet krokov „2“ s ukladaním každého kroku a čas na jeden krok „1 sekunda“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku generovania databázy.

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0018.jpg' | relative_url }})

Ovládanie simulácie – možnosti režimu simulácie

## Vytvorenie databázy

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) na vytvorenie databázy. Pozrite si správu na karte „Message“, ktorá informuje o stave vytvárania databázy, ako je znázornené na obr. 2DMDL1.19. Keď program dokončí zapisovanie databázy, prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0019.jpg' | relative_url }})

Okno „Vytvoriť databázu“

## Spustenie simulácie

Kliknite na označenie akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“; otvorí sa dialógové okno „Možnosti spustenia“, ako je znázornené na obr. 2DMDL1.20.. Použite predvolenú možnosť **Pokračovať v spustení**, vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

Po dokončení simulácie môžeme vidieť, že na koniec súboru Message bola pridaná nasledujúca správa:

******Správa*******

Simulácia bola dokončená a zastavená v časovom kroku určenom používateľom.

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0020.jpg' | relative_url }})

Karta „Simulácia“ na odoslanie simulácie

## Následné spracovanie výsledkov

Po dokončení simulácie môže používateľ zadať ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), aby si prezrel výsledky modelu. Bežný postup spočíva v tom, že sa najskôr vyberie číslo kroku a potom stavové premenné, ktoré sa majú zobraziť. Niektoré dôležité stavové premenné je možné vybrať priamo z post-procesora a k ostatným sa dá dostať prostredníctvom tabuľky ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) (výberom). Obr. 2DMDL1.21 znázorňuje rozloženie efektívneho napätia po obrábacom cykle a obr. 2DMDL1.22 znázorňuje rozloženie maximálneho hlavného napätia po obrábacom cykle.

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0021.jpg' | relative_url }})

Rozloženie efektívneho napätia a deformácia polotovaru po obrábacom cykle

![]({{ '/assets/images/labs/machining_distortion_labs/2d_machining_distortion_lab1/image0022.jpg' | relative_url }})

Rozloženie maximálneho hlavného napätia a deformovaný polotovar po obrábacom cykle
