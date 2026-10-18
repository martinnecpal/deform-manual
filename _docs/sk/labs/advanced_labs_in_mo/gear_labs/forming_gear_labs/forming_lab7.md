---
lang: sk
title: "Laboratórium tvarovania 7"
---

# Laboratórna práca č. 7. Hydraulický lis

Existujú dva spôsoby modelovania správania hydraulického lisu:

  1. Predpokladajme, že lis si udržiava konštantnú rýchlosť, kým nedosiahne maximálne zaťaženie, a potom zostane na maximálnom zaťažení (dvojkroková metóda).

  2. Predpokladajme, že lis sa pri približovaní k maximálnemu zaťaženiu postupne spomaľuje (metóda výkonového obalu).

Dvojkroková metóda sa ľahšie nastavuje a je užitočná pre simulácie s riadením sily aj v iných prípadoch ako pri hydraulických lisoch. Metóda výkonového obalu lepšie odráža skutočné správanie hydraulického lisu.

### Dvojkroková metóda

#### Vytvoriť nový problém

Vytvorte nový projekt s názvom **Gear_Hydraulic_Dwell** a skopírujte existujúci projekt **Gear_LargerBillet**. Uistite sa, že je zaškrtnutá možnosť **Kopírovať databázový súbor**. Kliknite na druhú operáciu a prejdite na stránku **Top****Die** Movement.

#### Priradiť pohyb hornej matrice

Nastavte pohyb na **hydraulický** lis a nastavte **rýchlosť** na konštantnú hodnotu **2** i**n/sec** (pozri obr. L7.1.). Kliknite na kartu **Dwell**. Nastavíme maximálne zaťaženie lisu, čas, počas ktorého bude lis udržiavaný pri tomto zaťažení, počet časových krokov zdržania a rýchlosť zastavenia, po ktorej sa lis zastaví.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0001.jpg' | relative_url }})

Okienko pre pohyb hornej matrice

Akonáhle lis dosiahne maximálne lisovacie zaťaženie (4000 klb.), ponecháme ho v tejto polohe po dobu 3 sekúnd. Dobrým pravidlom je 100 krokov na jednu sekundu zdržania, takže použijeme 300 krokov.

Nastavte **Max. zaťaženie** na **4000** klb, **Min.****rýchlosť** na 0**,005** in/sec, **Celkový****doba zdržania****** na **3** sekundy a **Počet krokov** na **300**. (Pozri obr. L7.2.)

Upozorňujeme, že **aktuálny****doba zdržania****čas** by sa mal vždy začínať od hodnoty **0**. Systém tento čas aktualizuje hneď po dosiahnutí zaťaženia zdržania.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0002.jpg' | relative_url }})

Okno záložky „Dwell“ hydraulického lisu

#### Vytvorenie databázy

Prejdite na stránku **Generate****DB** a vygenerujte databázu. Kliknutím na tlačidlo MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode (nad stromom operácií) spustite simuláciu.

#### Spustiť a sledovať simuláciu

Kliknite na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať****Spustiť**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, a potom ako režim simulácie vyberte rádiové tlačidlo **Interaktívny**. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

#### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

#### Graf

V postprocesore použite nástroj Graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) na vytvorenie grafu rýchlosti Y v závislosti od času. (Pozri obr. L7.3.)

_Všimnite si, že lis udrží rýchlosť 2 palce za sekundu a potom počas trojsekundového zastavenia výrazne spomalí._

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0003.jpg' | relative_url }})

Graf rýchlosti Y v závislosti od času so znázornením bodu dotyku

Zaznačte závislosť **zaťaženia Y** od **času**. Všimnite si, že zaťaženie lisu dosiahne maximum **4000** klb a počas doby zdržania zostáva na tejto konštantnej hodnote. (Pozri obr. L7.4.)

Pomocou ikony „Kontaktné body ![]({{ '/assets/icons/post_icons/mo_show_cotact_icon.jpg' | relative_url }})“ si môžete zobraziť kontakt s formami. Pozrite si, o koľko sa kontakt zväčšuje počas fázy zdržania. To je často rozhodujúci faktor medzi vyplnením a nevyplnením formy pri kovaniu v hydraulickom lise.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0004.jpg' | relative_url }})

Graf závislosti zaťaženia Y od času so znázornením kontaktu

### Metóda výkonovej obálky

#### Vytvorenie nového problému

Vytvorte nový projekt s názvom **Gear_Hydraulic_PowerLimit** a skopírujte existujúci projekt **Gear_LargerBillet**. Uistite sa, že je **zaškrtnutá** možnosť **Kopírovať databázový súbor**. Kliknite na **2. operáciu** a prejdite na pohyb **Top****Die**.

#### Pohyb hornej matrice

Nastavte pohyb na **hydraulický****lis**, rýchlosť nastavte na **konštantnú****2** in/sec. a **zaškrtnite** možnosť **Power****Limit**, ako je znázornené na obr. L7.5.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0005.jpg' | relative_url }})

Okienko pre pohyb hornej matrice

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}) a v tabuľke „Power Limit“ zadajte nižšie uvedené hodnoty. Táto krivka určuje maximálnu rýchlosť, ktorú môže lis udržiavať pri danom zaťažení pri kovaní (pozri obr. L7.6.).

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
  
![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0006.jpg' | relative_url }})

Okno obmedzenia výkonu

Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezastavia ovládacie prvky.

#### Ovládacie prvky na zastavenie

Nastavte **Max****load** primárneho lisovacieho nástroja na **4000** klb (Y). Prejdite na **kartu Vzdialenosť foriem** a inicializujte ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) tak, aby sa deaktivovalo. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) v okienku, ktoré sa zobrazí s otázkou, či chcete použiť tieto nastavenia.

#### Vytvorenie databázy

Prejdite na stránku „Generate DB“ a vygenerujte databázu. Kliknutím na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustite simuláciu.

#### Spustiť a sledovať simuláciu

Kliknite na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno Možnosti spustenia. Pomocou predvolenej možnosti **Pokračovať****Spustiť** vyberte možnosť „**Pokračovať od posledného kroku**“ a potom ako režim simulácie vyberte prepínač **Interaktívny**. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

#### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

#### Graf

V postprocesore použite nástroj Graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) na vytvorenie grafu **rýchlosti Y** v závislosti od **času**. Všimnite si, že lis udržiava rýchlosť 2 in/sec a potom počas trojsekundovej prestávky výrazne spomalí.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0007.jpg' | relative_url }})

Graf závislosti rýchlosti Y od času

V postprocesore vyneste graf **Rýchlosť Y** v závislosti od **času**.

Všimnite si, že lis udržiava rýchlosť 2 palce za sekundu takmer až do konca simulácie, potom však začne výrazne spomaľovať, ako je znázornené na obr. L7.7.

Zaznačte **zaťaženie Y** v závislosti od **času**. Všimnite si, že zaťaženie lisu dosahuje maximálnu hodnotu 4000 klb. (Pozri obr. L7.8.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0008.jpg' | relative_url }})

Graf závislosti zaťaženia Y od času
