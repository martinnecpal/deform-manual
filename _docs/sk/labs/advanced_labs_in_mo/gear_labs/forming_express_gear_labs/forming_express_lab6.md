---
lang: sk
title: "Vytvorenie Express Lab6"
---

# Cvičenie č. 6. Mechanický lis

### Úvod

Pri viacerých operáciách sa interaktívne nastavenie mechanického lisu výrazne líši od naplánovaného nastavenia. Prejdeme si obe možnosti.

Vzhľadom na jedinečnú kinematiku mechanického lisu musíme v každom okamihu presne vedieť, či sa lis nachádza v hornej alebo dolnej časti zdvihu (alebo v prednej či zadnej časti). To znamená, že potrebujeme poznať počiatočnú polohu.

Pri definovaní mechanického lisu je potrebné porozumieť niektorým špecifickým pojmom:

**Celkový zdvih** je celkový pohyb piestu od horného mŕtveho bodu (TDC) po dolný mŕtvy bod (BDC).

**Kovací zdvih** je vzdialenosť, ktorú prekoná piest od okamihu, keď sa po prvýkrát dotkne obrobku, až po dosiahnutie dolnej mŕtvej polohy (BDC).

**Počet zdvihov za sekundu** je rýchlosť zotrvačníka vyjadrená v cykloch za sekundu (zodpovedá rýchlosti lisu v prípade lisu bez spojkového pohonu).

V tomto návode budeme používať **celkový zdvih 16 palcov** a **počet zdvihov za sekundu 1 zdvih za sekundu** (t. j. 60 otáčok za minútu).

### Operácia 1 – Interaktívne nastavenie

#### Vytvorenie nového problému

Vytvorte nový projekt s názvom **FE_Gear_Mechanical** a skopírujte existujúci projekt **FE_Gear_LargerBillet**.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab6_image0001.jpg' | relative_url }})

Okno „Nový projekt“ v MO

V interaktívnom prostredí môžeme začať s hornou matricou správne umiestnenou na obrobku. Kliknite teda na prvú dlaždicu operácie **Upset**. Zo stromu operácií prejdite na stránku **Top Die Movement**.

#### Definovanie pohybu hornej matrice pri zúžení

Zmeňte typ pohybu na „Mechanický lis“. Nastavte **Celkový zdvih** na **16** palcov a **Zdvih/s** na **1** (pozri obr. L6.2.). Nastavenie zdvihu **tvarovania** ponechajte na hodnote **Presný****tvarovací****zdvih**. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Ovládacie prvky zastavenia.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab6_image0002.jpg' | relative_url }})

Okienko pre pohyb hornej matrice

#### Určenie zdvihu primárneho lisovacieho nástroja pri lisovaní

Nastavte **celkový** **primárny****zdvih****matrice****** na **6,5** palca (rovnako ako v modeli [Lab 2]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab2/' | relative_url }})). (Pozrite obr. L6.3.). Ak je počiatočná poloha hornej matrice v hornej alebo dolnej úvrati, môžete použiť tlačidlo sprievodcu ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) na nastavenie polohy matrice a automatický výpočet tvárniaceho zdvihu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali stránku Ovládacie prvky zastavenia.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab6_image0003.jpg' | relative_url }})

Okno primárneho zdvihu matrice

#### Skontrolujte ovládacie prvky brzdenia, či nie sú poškodené

V ovládacích prvkoch zastavenia môžeme vidieť, že celkový zdvih definovaný v ovládacích prvkoch pohybu sa používa ako maximálny zdvih matrice. Toto pole bude deaktivované, keďže čerpá údaje z údajov mechanického lisu týkajúcich sa ovládacích prvkov pohybu hornej matrice. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí okno „Generate DB“, pričom ponechajte predvolené nastavenia ovládacích prvkov krokov.

#### Vytvoriť databázu

Vytvorte databázu a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k druhej operácii.

### Operácia 2 – nastavenie plánovaného (dávkového) spustenia

Pri dávkovom nastavení zvyčajne nevieme, kde sa bude nachádzať posuvník vo vzťahu k BDC v okamihu, keď sa dotkne obrobku. Preto musíme začať s posuvníkom v známej polohe a pri spustení modelu aktualizovať príkazy na pohyb.

Ako štandardnú referenčnú polohu použijeme polohu TDC, následne pomocou plánovaného polohovania aktualizujeme polohu nástroja a zdvih kovania. 

Z stromu operácií prejdite na stránku **Polohovanie**.

#### Umiestňovanie objektov

  1. **Zavedenie** **polohy** **hornej matrice** **do** **spodnej****matrice**

  2. **Posuňte****polohu** **hornej****matrice** smerom nahor v smere **+Y** o **medzeru****medzi dielmi** veľkosti **0,2** in

  3. **Posuňte****polohu** **hornej****matrice** smerom nahor v osi +Y o celkový zdvih kováčskej lisovacej hlavy, 16 palcov. Teraz sa matrica nachádza v polohe **TDC**.

Teraz sa vráť **späť** na stránku **Top** **die****movement**.

#### Definovanie pohybu hornej matrice pri tvárnení

Nastavte mechanický lis s počtom zdvihov za sekundu = 1 a nastavte **celkový****zdvih** na **16** palcov. Zmeňte možnosť **tvarovací****zdvih** na **presný****tvarovací****zdvih**. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka **Plánované** **polohovanie**. (Pozri obr. L6.4.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab6_image0004.jpg' | relative_url }})

Mechanický lis s priehľadom na pohyb pre tvárnenie

#### Plánované polohovanie

**Posunutie****obrobku****do** **spodnej polohy****voči** **spodnej matrici**.

**Interferencia****polohovanie** **hornej****matrice** smerom nadol k **obrobku**. Všimnite si, že možnosť „Aktualizovať aktuálny zdvih“ je zaškrtnutá a sivá. Zdvih matrice sa automaticky aktualizuje, keď k tomuto polohovaniu dôjde počas simulácie. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Ovládacie prvky zastavenia“.

#### Určenie primárneho zdvihu matrice pre zúženie

Nastavte **posun primárnej matice** na **16** palcov (v smere Y). Keďže sa primárna matica momentálne nachádza v hornej úvrati, skontrolujte jej aktuálnu polohu voči hornej úvrati.

Po spustení projektu sa nástroj presunie do polohy, v ktorej bude v kontakte s obrobkom (bez ohľadu na jeho tvar), a zdvih kovania sa aktualizuje tak, aby zohľadňoval novú vzdialenosť nad dolnou úvratou.

Uložte projekt a kliknite na tlačidlo režimu MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) (nad stromom operácií), aby ste spustili simuláciu.

### Spustenie a monitorovanie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Možnosti spustenia. Pomocou predvolenej možnosti **Pokračovať****Spustiť** vyberte možnosť „**Pokračovať od posledného kroku**“ a následne vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

Po ukončení simulácie by sa vám mal v spodnej časti súboru so správami zobraziť nasledujúci text.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab6_image0006.jpg' | relative_url }})

To znamená, že simulácia sa zastavila v okamihu, keď lis dosiahol dolnú mŕtvu polohu (BDC). Ak by ste sa pozreli do súboru protokolu, zistili by ste, že práve toto je aj dôvod, prečo sa zastavila prvá operácia.

### Prezrite si výsledky

Kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky. Prejdite si všetky kroky.

**Graf**  
Kliknite na nástroj ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) a vytvorte graf **Rýchlosť Y** v závislosti od **Času**. Všimnite si, že rýchlosť klesá na nulu na konci každej operácie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab6_image0005.jpg' | relative_url }})

Graf rýchlosti Y v závislosti od času
