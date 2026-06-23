---
lang: sk
title: "23.7. E-mailové oznámenie o simulácii"
---

# 23.7. E-mailové upozornenie na simuláciu

Táto funkcia umožňuje programu DEFORM odoslať e-mailové upozornenie na začiatku simulácie a na konci simulácie zaslať posledných 25 riadkov zo súboru správ a zo súboru protokolu. Nastavenia e-mailu sú dostupné v ponuke **Možnosti**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Prostredie**, ako je znázornené na obr. 23.7.1. Je potrebné zadať informácie o SMTP serveri, používateľské meno a heslo, ako je znázornené na obr. 23.7.2.

![]({{ '/assets/images/simulator/23_deform_simulator/23_7_email_the_results/image001.jpg' | relative_url }})

Nastavenia prostredia

E-maily sa odosielajú prostredníctvom protokolu SMTP s použitím StartTLS (alebo bez zabezpečenia), preto je potrebné zadať názov hostiteľa a port SMTP servera. Výberom rozbaľovacieho menu vpravo od poľa Port je možné automaticky vyplniť niektoré nastavenia pre niektoré verejné e-mailové služby (napr. Gmail a Outlook). (Pozri obr. 23.7.2.)

  
Podrobnosti o nastaveniach firemného SMTP e-mailového servera si prosím overte u svojho IT oddelenia.

![]({{ '/assets/images/simulator/23_deform_simulator/23_7_email_the_results/image002.jpg' | relative_url }})

Nastavenia e-mailových upozornení o stave simulácie

Ak váš e-mailový server vyžaduje prihlásenie (čo je u väčšiny z nich bežné), zaškrtnite políčko „Server vyžaduje prihlásenie“ a zadajte svoje používateľské meno a heslo.  
Oznámenia je možné zasielať na viacero e-mailových adries; cieľové e-mailové adresy nastavte v poliach **Adresy, na ktoré sa má e-mail odoslať**.  
Po vyplnení všetkých nastavení kliknite na tlačidlo **Otestovať nastavenia e-mailu**, aby ste ich overili. Ak je všetko v poriadku, na všetky cieľové adresy bude odoslaný potvrdzovací e-mail. (Pozri obr. 23.7.3.)

![]({{ '/assets/images/simulator/23_deform_simulator/23_7_email_the_results/image003.jpg' | relative_url }})

Výber verejného e-mailového servera

V prípade účtov Gmail s aktivovaným dvojstupňovým overovaním nájdete podrobnosti o nastavení hesla pre aplikáciu na tomto odkaze. _https://www.deform.com/redirects/gmailapppassword.html_

Predvolený port pre e-mailové servery SMTP s protokolom StartTLS je 587.
