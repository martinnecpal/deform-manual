---
lang: sk
title: "Vytvorenie Express Lab7"
---

# Laboratórna práca č. 7. Hydraulický lis

Existujú dva spôsoby modelovania správania hydraulického lisu:

  1. Predpokladajme, že lis udržiava konštantnú rýchlosť, kým nedosiahne maximálne zaťaženie, a potom zostane pri maximálnom zaťažení (dvojkroková metóda).

  2. Predpokladajme, že lis sa pri približovaní k maximálnemu zaťaženiu postupne spomaľuje (metóda výkonového obalu).

Dvojkroková metóda sa ľahšie nastavuje a je užitočná pre simulácie s riadením sily aj v iných prípadoch ako pri hydraulických lisoch. Metóda výkonovej obálky lepšie odzrkadľuje skutočné správanie hydraulického lisu.

### Dvojkroková metóda

#### Vytvoriť nový problém

Vytvorte nový projekt s názvom **FE_Gear_Hydraulic_Dwell** a skopírujte existujúci projekt **FE_Gear_LargerBillet**. Uistite sa, že je **zaškrtnutá** **možnosť Kopírovať databázový súbor**. Kliknite na **2.** operáciu a prejdite na pohyb **Top****Die**.

#### Priradiť pohyb hornej matrice

Nastavte pohyb na **Hydraulický****lis** a nastavte **Rýchlosť** na **konštantnú****hodnotu 2** palce/sek. Akonáhle lis dosiahne maximálne lisovacie zaťaženie (4000 klb.), zostaneme v tejto polohe po dobu 3 sekúnd. Dobrým pravidlom je 100 krokov na sekundu zdržania, takže použijeme 300 krokov. Maximálne zaťaženie definujeme v ďalšom kroku na stránke Ovládanie zastavenia.

Nastavte **celkový****doba zdržania** na **3** sekundy, ako je znázornené na obr. L7.1. Systém aktualizuje túto hodnotu po dosiahnutí zaťaženia zdržania. Kliknite na vetvu **Ovládacie prvky zastavenia** v strome objektov, aby ste definovali ovládacie prvky zastavenia.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0001.jpg' | relative_url }})

Hydraulický pohyb s reguláciou zdržania

#### Definovanie ovládacích prvkov na zastavenie

**Zrušte zaškrtnutie políčka****Vzdialenosť****medzi****objektmi** a **zaškrtnite políčko****Maximálne****zaťaženie**. Nastavte hodnotu **zaťaženia** na **4000** klb. (Pozri obr. L7.2.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0002.jpg' | relative_url }})

Maximálne zaťaženie hydraulického lisu na spustenie fázy zdržania

#### Vytvorenie databázy

Prejdite na stránku **Generate****DB** a vygenerujte databázu. V okienku „Lost Steps“, ktoré informuje, že pri generovaní databázy budú vymazané existujúce kroky druhej operácie, kliknite na **Yes**. Kliknutím na tlačidlo MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode (nad stromom operácií) spustíte simuláciu.

####  Spustiť a sledovať simuláciu

Kliknite na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať****Spustiť**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

#### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

#### Graf

V postprocesore použite nástroj „Graf“ na znázornenie grafu rýchlosti Y v závislosti od času. Všimnite si, že lis sa pohybuje konštantnou rýchlosťou **2** **palce/sekundu** a potom počas trojsekundovej doby zastavenia výrazne spomaľuje.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0003.jpg' | relative_url }})

Graf závislosti rýchlosti Y od času so zobrazením bodu dotyku

Zaznačte závislosť zaťaženia Y od času. Všimnite si, že zaťaženie lisu dosiahne maximum **4000 klb** a počas doby zdržania sa udrží na tejto konštantnej hodnote.

Pomocou ikony „Kontaktné body“ (![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }})) si môžete zobraziť kontakt s formami. Pozrite si, o koľko sa kontakt zväčšuje počas fázy zdržania. Práve to často rozhoduje o tom, či sa forma pri kovaní na hydraulickom lise naplní, alebo nie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0004.jpg' | relative_url }})

Graf závislosti zaťaženia Y od času so zobrazením kontaktov

### Metóda výkonovej obálky

#### Vytvorenie nového problému

Vytvorte nový projekt s názvom **FE_Gear_Hydraulic_PowerLimit** a skopírujte existujúci projekt **FE_Gear_LargerBillet**. Uistite sa, že je **zaškrtnutá** možnosť **Kopírovať****databázu****súbor**. Kliknite na **2.** operáciu a prejdite na pohyb **Horná****matrica**.

#### Pohyb hornej matrice

Nastavte pohyb na **hydraulický****lis**, rýchlosť nastavte na **konštantnú****hodnotu 2** palce/sek. a **zaškrtnite** možnosť ****Obmedzenie výkonu****. (Pozri obr. L7.5.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0005.jpg' | relative_url }})

Hydraulické ovládacie prvky pohybu s obmedzením výkonu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}) a zadajte do tabuľky „Power Limit“ uvedené hodnoty. Táto krivka určuje maximálnu rýchlosť, ktorú môže lis udržiavať pri danom zaťažení pri kovaní (pozri obr. L7.6.).

**Sila** |  **Rýchlosť**  
---|---  
0 |  3  
500 |  3  
1000 |  2,875  
1500 |  2,625  
2000 |  2,375  
2500 |  2  
3000 |  1,4  
3500 |  0,75  
4000 |  0,01  
4500 |  0  
5000 |  0  
  
![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0006.jpg' | relative_url }})

Okno obmedzenia výkonu

Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezastavia ovládacie prvky.

#### Ovládacie prvky na zastavenie

**Zrušte zaškrtnutie políčka****Vzdialenosť****medzi****objektmi** a **zaškrtnite políčko****Maximálne****zaťaženie**. Nastavte hodnotu **Maximálne****zaťaženie** na **4000** klb.

#### Vytvorenie databázy

Prejdite na stránku **Generate** DB a vygenerujte databázu. V okienku „Lost Steps“, ktoré vás informuje, že pri generovaní databázy budú vymazané existujúce kroky druhej operácie, kliknite na **Yes**. Kliknutím na tlačidlo MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode (nad stromom operácií) spustite simuláciu.

#### Spustiť a sledovať simuláciu

Kliknite na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať****Spustiť**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

#### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

#### **Graf**

V postprocesore použite nástroj Graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) na vytvorenie grafu rýchlosti Y v závislosti od času. Všímajte si, že lis sa pohybuje konštantnou **rýchlosťou** **2** palce/sekundu a následne výrazne spomaľuje, ako je znázornené na obr. L7.7.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0007.jpg' | relative_url }})

Graf závislosti rýchlosti Y od času

Vykreslite graf Y – zaťaženie v závislosti od času. V prípade výkonového obmedzenia môžeme pozorovať, že keď zaťaženie prekročí hodnotu **2500** klb, rýchlosť postupne klesá z hodnoty 2 in/sec. Všimnite si, že zaťaženie lisu tiež dosahuje maximálnu hodnotu 4000 klb. (Pozri obr. L7.8.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0008.jpg' | relative_url }})

Graf závislosti Y-zaťaženia od času
