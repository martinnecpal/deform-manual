---
lang: sk
title: "Laboratórium formovania 6"
---

# Laboratórna práca č. 6. Mechanický lis

### Úvod

Pri viacerých operáciách sa interaktívne nastavenie mechanického lisu výrazne líši od naplánovaného nastavenia. Prejdeme si obe možnosti.

Vzhľadom na jedinečnú kinematiku mechanického lisu musíme v každom okamihu presne vedieť, či sa lis nachádza v hornej alebo dolnej (prípadne prednej alebo zadnej) fáze zdvihu. To znamená, že potrebujeme poznať počiatočnú polohu.

Pri definovaní mechanického lisu je potrebné porozumieť niektorým špecifickým pojmom:

**Celkový zdvih** je celkový pohyb piesta od hornej úvrati (TDC) po dolnú úvratu (BDC).

**Kovací zdvih** je vzdialenosť, ktorú prejde piest od okamihu, keď sa po prvýkrát dotkne obrobku, až po dosiahnutie dolnej mŕtvej polohy.

**Zábery za sekundu** je rýchlosť zotrvačníka vyjadrená v cykloch za sekundu (zodpovedá rýchlosti lisu v prípade lisov bez spojkového pohonu).

V tomto návode použijeme celkový zdvih 16 palcov a počet zdvihov za sekundu 1 (t. j. 60 otáčok za minútu).

### Operácia 1 – Interaktívne nastavenie

#### Vytvorenie nového problému

Vytvorte nový projekt s názvom **Gear_Mechanical** a skopírujte existujúci projekt **Gear_LargerBillet**.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab6_image0001.jpg' | relative_url }})

Okno „Nový projekt“ v programe MO

V interaktívnom prostredí môžeme začať s hornou matricou správne umiestnenou na obrobku. Kliknite teda na prvú dlaždicu **Operácia****vytláčania****. Z stromu operácií prejdite na stránku **Pohyb****hornej****matice****.**

#### Pohyb hornej matrice

Zmeňte typ pohybu na **Mechanický****lis**. Nastavte **Celkový****zdvih** na **16** palcov a **Kováčsky****zdvih** na **6,3** palca (vzdialenosť od aktuálnej polohy po spodnú mŕtvu bodu). Nastavte **Cyklov/sek.** na hodnotu **1** (pozri obr. L6.2.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Ovládacie prvky zastavenia

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab6_image0002.jpg' | relative_url }})

Na začiatok stránky o pohybe matrice

#### Ovládacie prvky na zastavenie

Nastavte dorazový zdvih (posun primárnej matrice) na **16** palcov (smer **Y**), čo zodpovedá celkovému zdvihu lisu. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Generate DB“.

#### Vytvoriť databázu

Vytvorte databázu a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k druhej operácii.

### Operácia 2 – nastavenie plánovaných (hromadných) úloh

Pri dávkovom nastavení zvyčajne nevieme, kde sa bude nachádzať posúvač vo vzťahu k BDC v okamihu, keď sa dotkne obrobku. Preto musíme začať s posúvačom v známej polohe a pri spustení modelu aktualizovať príkazy na pohyb.

Ako štandardnú referenčnú polohu použijeme polohu TDC, následne pomocou plánovaného polohovania aktualizujeme polohu nástroja a zdvih kovania. 

Z stromu operácií prejdite na **stránku** **Polohovanie**.

#### Umiestňovanie objektov

  1. V mieste kolízie sa horná matrica posunie nadol k spodnej matrici

  2. Posuňte hornú matricu nahor o vzdialenosť 0,2 palca, čo zodpovedá medzere na odlievanie

  3. Posuňte hornú matricu nahor o celkový zdvih kovania, ktorý je 16 in. Teraz sa matrica nachádza v hornej úvrati.

Teraz sa vráť na stránku **Top****die****movement**.

#### Pohyb hornej matrice

Nastavte mechanický lis s hodnotou **Cyklov/s** = **1** a nastavte hodnotu **Celkový****zdvih** aj **Kovacie****zdvih** na **16** palcov. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Plánované polohovanie“.

#### Plánované polohovanie

Kolízia pri umiestňovaní obrobku na spodnú matricu.

Polohovanie hornej matice smerom nadol k obrobku. Všimnite si, že možnosť „Aktualizovať aktuálny zdvih“ je zaškrtnutá a sivá. Zdvih matice sa automaticky aktualizuje, keď k tomuto polohovaniu dôjde počas simulácie. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Ovládacie prvky zastavenia“.

#### Ovládacie prvky na zastavenie

Nastavte **Primárny****posun****matrice** na hodnotu **16** palcov (v smere Y) a na **kartu****Vzdialenosť****matrice** kliknite na ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}), čím inicializujete údaje o ovládacích prvkoch zastavenia vzdialenosti matice.

Po spustení projektu sa nástroj presunie do polohy, v ktorej bude v kontakte s obrobkom (bez ohľadu na jeho tvar), a zdvih kovania sa aktualizuje tak, aby odrážal novú vzdialenosť nad dolnou úvratou.

Uložte projekt a kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií), aby ste spustili simuláciu.

### Spustenie a sledovanie simulácie

Kliknite na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať****Spustiť**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

Prejdite všetky kroky. 

**Graf**

Kliknite na nástroj ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) a vytvorte graf rýchlosti Y v závislosti od času. Všimnite si, že rýchlosť klesá na nulu na konci každej operácie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab6_image0003.jpg' | relative_url }})

Graf rýchlosti Y v závislosti od času
