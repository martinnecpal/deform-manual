---
lang: sk
title: "27. Úvod do tvorby správ"
---

# 27\. Úvod do tvorby správ

Funkcia generovania správ v programoch MO a Next Gen Post pomáha používateľom automaticky vytvárať správy s kontúrovými grafmi pre vybrané stavové premenné, sledovaním bodov, grafmi zaťaženia a zdvihu atď. Správu je možné uložiť vo formáte PDF (2D a 3D) alebo ako súbor PPT. Správu môžeme vygenerovať buď v interaktívnom režime, alebo v dávkovom režime (pozri obr. 27.1.).

![]({{ '/assets/images/post_processor/27_introduction_to_report_generation/image001.jpg' | relative_url }})

Nastavenie generovania správ

**V režime hromadného odosielania**: Po dokončení nastavenia všetkých operácií pridajte operáciu „Generovanie správy“ zo zoznamu operácií v Průzkumníku. Dokončite nastavenie generovania správy a spustite simuláciu. Po dokončení simulácie všetkých operácií, ktoré predchádzajú generovaniu správy, sa spustí operácia „Generovanie správy“, ktorá vygeneruje správu pre vybrané stavové premenné a grafy.

**V interaktívnom dávkovom režime**: V položke „Next Gen“ na karte „Report“ môžeme vygenerovať správu výberom požadovaných stavových premenných a grafov alebo pomocou súboru .DS. Na vygenerovanie správy je možné použiť aj súbor .DS.

**Ponuka sekcií:** Vlastné sekcie definované používateľom je možné pridávať a odstraňovať pomocou tlačidiel ![]({{ '/assets/icons/post_icons/mo_add_section_button.jpg' | relative_url }}) (Pridať novú sekciu) a ![]({{ '/assets/icons/post_icons/mo_delete_section_button.jpg' | relative_url }}) (Odstrániť sekciu) na karte „Sekcia“, ako aj pomocou ikon na paneli nástrojov. Pozri obr. 27.2.

![]({{ '/assets/images/post_processor/27_introduction_to_report_generation/image002.jpg' | relative_url }})

Ponuka sekcie

**Ponuka Správa:** Nižšie sú uvedené možnosti dostupné na karte Správa, ako je znázornené na obr. 27.3.,

![]({{ '/assets/images/post_processor/27_introduction_to_report_generation/image003.jpg' | relative_url }})

Ponuka správ

  * **Vytvoriť**: Táto voľba slúži na vytvorenie správy pre pridanú kapitolu na karte Správa. Pomocou tejto voľby je možné vytvoriť správu aj na základe importovanej alebo načítanej šablóny správy.

  * **Vytvoriť****automatickú****správu**: Vytvorí sa automatická správa, ktorá bude obsahovať predvolenú časť týkajúcu sa toku kovu, graf stavových premenných so stavovými premennými „napätie-efektívne“, „deformácia-efektívne“ a „teplota“, graf zdvihu v závislosti od zaťaženia a súhrnný graf teploty.

  * **Otvoriť priečinok**: Otvorí pracovný priečinok v Průzkumníku Windows.

  * **Načítať šablónu správy**: Pomocou tejto možnosti môže používateľ načítať uloženú šablónu správy (súbor s príponou *.ds*).

  * **Uložiť šablónu správy**: Pomocou tejto možnosti môže používateľ uložiť údaje zo správy do šablóny (súbor s príponou *.ds*).

**MikTeX:** Od verzie DEFORM v12.0 sa na generovanie správ v programe DEFORM používa softvér MikTeX.

V časti „Vytvoriť súbor PDF“ si používateľ môže teraz prezrieť obsah jednotlivých kapitol, súhrn jednotlivých operácií a údajov o objektoch, ako aj výstupy jednotlivých sekcií. Ďalšie informácie týkajúce sa vygenerovanej správy nájdete v kapitole [28\. Report Generation](/docs/en/post_processor/28_report_generation/28_report_generation/), v sekcii [Generating Report](../28_report_generation/28_report_generation.htm#Generating__Report).

**Súvisiace témy:**

[28\. Report Generation](/docs/en/post_processor/28_report_generation/28_report_generation/)
