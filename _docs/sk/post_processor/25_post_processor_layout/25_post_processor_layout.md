---
lang: sk
title: "25. Rozloženie postprocesora"
---

# 25\. Rozloženie postprocesora

25.1. Okno na úpravu nastavení funkcií príspevkov

25.2. Strom objektov

25.2.1. Možnosti operačného stromu

25.2.2. Možnosti pravého tlačidla myši (RMB) v strome objektov

25.3. Grafické okno

25.4. Vytváranie správ

25.5. Ponuka widgetu v doku

Postprocesor poskytuje používateľovi intuitívne grafické používateľské rozhranie, ktoré mu umožňuje prezerať výstupy simulácie, interpretovať výsledky a generovať správy v rôznych formátoch, ako sú PDF, PPT atď. Funkcia PIP v programe Next Gen Post pomáha používateľovi porovnávať výstupy simulácie z viacerých databáz.

Rozloženie grafického rozhrania postprocesora (pozri obr. 25.1.) možno rozdeliť na zobrazenie krokov, strom objektov, okno na úpravu nastavení postprocesora a grafické okno.

![]({{ '/assets/images/post_processor/25_post_processor_layout/image001.jpg' | relative_url }})

Rozloženie postprocesora

**Okno zobrazenia krokov** ponúka možnosti výberu a prehrávania simulovaných krokov, ako aj výber operácií a zobrazenie informácií týkajúcich sa aktuálnej operácie a kroku.

**Grafické okno** zobrazuje grafické znázornenie objektov. Grafické okno možno použiť na zobrazenie kontúrových grafov, grafov, toku zŕn atď.

**Nástroje na tvorbu grafov** slúžia na vykresľovanie rôznych stavových premenných, sledovanie bodových dráh stavových premenných, skúmanie toku zŕn pomocou programu Flownet, extrahovanie údajov z databázy, vytváranie súhrnných grafov, tvorbu animácií atď.

**Strom objektov** obsahuje zoznam objektov a riadi ich zobrazenie. Kartu „Správa“ v okne stromu objektov môže používateľ využiť na vytvorenie správy o výsledkoch simulácie.

Okno na úpravu nastavení **funkcií príspevku** slúži na výber a úpravu funkcií príspevku a ich nastavení pre grafy stavových premenných, sledovanie bodov, Flownet, súhrnné grafy, extrakciu údajov, grafy zaťaženia a posunu, symetriu, rezanie (len pre 3D), oblasť záujmu, nastavenie animácie atď.

## Okno s nastaveniami funkcií príspevku

Okno úprav nastavení funkcií postprocesora je oblasť, v ktorej sa zobrazujú možnosti a nastavenia pre vybrané funkcie postprocesora, ako je znázornené na obr. 25.1. V tejto oblasti je možné tieto možnosti a nastavenia nastaviť a upravovať.

Možnosti a nastavenia jednotlivých funkcií sú vysvetlené spolu s danou funkciou ďalej v časti Funkcie príspevkov.

## Strom objektov

V tomto okne sú k dispozícii objekty a informácie o ich zobrazení, ako napríklad viditeľnosť objektov, geometria, sieť, priehľadnosť, rovina rezu, sledovanie bodov a informácie o sieti Flownet, ako je znázornené na obr. 25.1.

Používateľ môže vybrať objekt, ktorý sa má zobraziť v grafickom okne, kliknutím ľavým tlačidlom myši na príslušný objekt v stromovej štruktúre a zmeniť jeho režimy zobrazenia. Funkcie „Point tracking“ a „Flownet“ je možné skryť alebo odstrániť kliknutím pravým tlačidlom myši na odkaz „Point tracking“/„Flownet tracking“ v stromovej štruktúre objektov.

### **Možnosti operačného stromu**

**[2D][3D]:**

**Zobraziť objekt ![]({{ '/assets/icons/pre_icons/mo_show_obj_icon.jpg' | relative_url }}):** Zapne/vypne vybraný objekt zo stromu objektov.

**Zobraziť sieť ![]({{ '/assets/icons/pre_icons/mo_show_mesh_icon.jpg' | relative_url }}):** Zobrazí alebo skryje sieť vybraného objektu zo stromu objektov.

**Zobraziť geometriu ![]({{ '/assets/icons/pre_icons/mo_show_geo_icon.jpg' | relative_url }}) :** Zobrazí alebo skryje geometriu vybraného objektu zo stromu objektov.

**Zobraziť kontaktné uzly: ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}) **Zapne zobrazenie kontaktov pre vybraný objekt zo stromu objektov spolu so všetkými ostatnými objektmi. (Pozri obr. 25.1.)

  
**[3D]:**

**Nastaviť priehľadnosť ![]({{ '/assets/icons/pre_icons/mo_transparent.jpg' | relative_url }}) :** Zapne alebo vypne priehľadnosť vybraného objektu zo stromu objektov.

**Zobraziť zadnú stranu ![]({{ '/assets/icons/pre_icons/mo_show_backfac_icon.jpg' | relative_url }}):** Zapína/vypína zadnú stranu objektu vybraného v stromovej štruktúre objektov; táto funkcia je užitočná najmä v prípade, ak je objekt nastavený ako priehľadný. (Pozri obr. 25.2.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image032.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image033.jpg' | relative_url }})

  
(a) (b)

Sieť plastického objektu v režime tieňovaného vykresľovania; (a) so zapnutým zobrazením zadných plôch (b) s vypnutým zobrazením zadných plôch

**[2D][3D]:**  
**Režimy zobrazenia objektov:** Program DEFORM ponúka 3 rôzne režimy zobrazenia objektov, ako je znázornené na obr. 25.1.

**Režim jedného objektu ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}):** Zobrazí sa iba vybraný objekt zo stromu objektov. Všetky ostatné objekty sú skryté.

**Režim viacerých objektov**![]({{ '/assets/icons/pre_icons/mo_show_multi_obj_icon.jpg' | relative_url }}): V grafickom okne sa zobrazujú všetky objekty. Objekt vybraný zo stromu objektov je v 3D režime zobrazený v jednolitej farbe, zatiaľ čo všetky ostatné objekty sú priehľadné. (Pozri obr. 25.3.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image034.jpg' | relative_url }})

Režim viacerých objektov pri výbere plastového obrobku

  
**Režim objektu používateľa**![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}): Používateľ môže nezávisle prepínať medzi režimami Zobrazenie, Geometria, Sieť, Priehľadnosť (len pre 3D) a Rezová rovina (len pre 3D) daného objektu. To je možné vykonať zaškrtnutím alebo odškrtnutím príslušných políčok, ako je znázornené na obr. 25.4.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image035.jpg' | relative_url }})

Okno v režime užívateľsky definovaných objektov

  
Nižšie sú uvedené nastavenia, ktoré musíme zvoliť na základe požiadaviek na zobrazenie objektov,

**Použiť možnosti zobrazenia**![]({{ '/assets/icons/pre_icons/mo_apply_display_option.jpg' | relative_url }}) : Použije vybranú možnosť zobrazenia pre objekty.

**Viditeľné**![]({{ '/assets/icons/pre_icons/mo_visible.jpg' | relative_url }}) : Zapne/vypne zobrazenie vybraného objektu.

**Mesh**![]({{ '/assets/icons/pre_icons/mo_mesh_icon.jpg' | relative_url }}) : Zobrazí alebo skryje sieť vybraného objektu.

**Geometria**![]({{ '/assets/icons/pre_icons/mo_geometry _icon.jpg' | relative_url }}) : Zobrazí alebo skryje geometriu vybraného objektu.

**Transparency![]({{ '/assets/icons/pre_icons/mo_transparent.jpg' | relative_url }})** : Zapne/vypne priehľadnosť vybraného objektu.

**Slice**![]({{ '/assets/icons/pre_icons/mo_slice.jpg' | relative_url }}) : Zapne/vypne rovinu rezu pre vybraný objekt, na ktorom sa má vykonať rez.

### **Možnosti pravého tlačidla myši (RMB) v strome objektov**

**Údaje k úlohe** [2D, 3D]:   
Ponuka „Problem Data“ obsahuje nasledujúci príkaz, ako je znázornené na obr. 25.5 a obr. 25.6.

**[2D, 3D]:**

**Vybrať všetky objekty**: Keď používateľ klikne na túto možnosť, zaškrtnú sa všetky políčka v stĺpci „Vybrať“ v strome operácií.

**Zrušiť výber všetkých objektov**: Keď používateľ klikne na túto možnosť, zruší sa zaškrtnutie všetkých políčok v stĺpci „Výber“ v strome operácií.

**Zapnúť všetky objekty**: Keď používateľ klikne na túto možnosť, zapnú sa všetky objekty v okne zobrazenia.

**Vypnúť všetky objekty**: Keď používateľ klikne na túto možnosť, vypnú sa všetky objekty v okne zobrazenia.

**Zapnúť všetky obrobky (okrem RIGID)**: Zapne všetky objekty, ktoré nie sú tuhé. (Vypne všetky tuhé objekty)

**T******ur** n na všetkých telesách (RIGID)**: Zapne sa na každom objekte, ktorý je tuhý. (Všetky ostatné objekty sa vypnú)

**Zapnúť zobrazenie kontaktov pre všetky**: Táto funkcia zapne zobrazenie kontaktov všetkých objektov v okne zobrazenia.

**Vypnúť zobrazenie kontaktov pre všetky**: Táto funkcia vypne zobrazenie kontaktov všetkých objektov v okne zobrazenia.

**Import objektu**: Používateľ môže importovať objekt zo súboru s kľúčmi alebo z databázy.

**Import geometrie**: Používateľ môže importovať geometriu zo súboru kľúčov, databázy alebo vo formátoch IGS, STL a DXF.

**[3D]:**

**Zapnúť priehľadnosť pre všetko**: Táto funkcia nastaví objekty v okne zobrazenia ako priehľadné.

**Vypnúť priehľadnosť pre všetky**: Táto voľba vypne priehľadnosť objektov v okne zobrazenia.

**Zapnúť zobrazenie zadnej strany pre všetky objekty:** Zobrazuje zadnú stranu objektu; táto funkcia je užitočnejšia v prípade, ak sú objekty nastavené ako priehľadné.

**Vypnúť zadnú stranu pre všetky** : Táto voľba vypne zadnú stranu objektov.

![]({{ '/assets/images/post_processor/25_post_processor_layout/image008.jpg' | relative_url }})

Možnosti ponuky RMB na objektoch v strome operácií pre 2D 

![]({{ '/assets/images/post_processor/25_post_processor_layout/image007.jpg' | relative_url }})

Možnosti ponuky RMB na objektoch v strome operácií pre 3D 

**Údaje o objektoch [2D, 3D]**  
Ponuka „Údaje o objekte“ (pozri obr. 25.7., obr. 25.8. a obr. 25.9.) obsahuje v závislosti od typu objektu niektoré alebo všetky z nasledujúcich príkazov:

**[2D, 3D]:**

**Zobraziť geometriu**: Zobrazí geometriu objektu

**Zmeniť farbu odtieňa (Geometria)**: Zmení farbu výplne povrchovej plochy.

**Zmeniť farbu čiar (Geometria)**: Zmení farbu čiar ohraničujúcich hrany plôch.

**Export geometrie**: Pomocou tejto možnosti je možné uložiť údaje o geometrii objektu.

**Zobraziť sieť**: Zobrazí sieť objektu

**Zmeniť farbu odtieňa (Mesh)**: Zmení farbu výplne prvku.

**Zmeniť farbu čiar (Mesh)**: Zmení farbu čiar ohraničujúcich hrany prvkov.

**Zobraziť uzol kontaktu**: Zvýrazní kontakt pre vybraný objekt s ľubovoľným hlavným objektom. Ide o rýchly spôsob zobrazenia kontaktu. Ide o prepínacie menu. Jedným kliknutím zapnete zobrazenie uzla kontaktu. Ďalším kliknutím zobrazenie opäť vypnete.

**[3D]:**

**Zobraziť geometriu a normálové vektory**: Zapne zobrazenie geometrie s normálovými vektormi.

**Použiť plynulé tieňovanie (Mesh)**: Zabezpečí, aby sa tieňovanie siete zobrazovalo plynule.

**Zmeniť na priehľadné**: Táto funkcia zmení objekty na priehľadné.

**Zmena priehľadnosti:** Pomocou tejto možnosti je možné meniť priehľadnosť siete 3D objektu.

**Zobraziť zadnú stranu**: Zobrazí zadnú stranu objektu.

**Pohyb (len pre primárnu kocku)**

**Zobraziť posuvný pohyb** : V okne displeja sa zobrazí smer posuvného pohybu.

**Zobraziť rotačný pohyb**: V okne displeja sa zobrazí smer rotačného pohybu.

**Zaťaženie (len pre primárny valec)**: V okne displeja sa zobrazuje smer pohybu zaťaženia.

**Krok diferenciácie (prírastok SV)**: Pomocou možnosti „Krok diferenciácie“ môže používateľ znázorniť hodnotu stavovej premennej v danom kroku  
(Pozri obr. 25.10.) Používateľ môže znázorniť rozdiel medzi načítaným krokom a aktuálnym krokom (pozri nižšie obr. 25.11.).

![]({{ '/assets/images/post_processor/25_post_processor_layout/image003.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/25_post_processor_layout/image004.jpg' | relative_url }})

(a) (b)

Možnosti kontextového menu na vybranom objekte v strome operácií (a) pre 3D a (b) pre 3D

![]({{ '/assets/images/post_processor/25_post_processor_layout/image006.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/25_post_processor_layout/image005.jpg' | relative_url }})

(a) (b)

Možnosti ponuky RMB v položke „Object Mesh“ v stromovej štruktúre operácií (a) pre 3D a (b) pre 3D

![]({{ '/assets/images/post_processor/25_post_processor_layout/image010.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/25_post_processor_layout/image009.jpg' | relative_url }})

(a) (b)

Možnosti ponuky RMB v položke „Geometria objektu“ v stromovej štruktúre operácií (a) pre 3D a (b) pre 3D

![]({{ '/assets/images/post_processor/25_post_processor_layout/image011.jpg' | relative_url }})

Krok vykresľovania rozdielov

![]({{ '/assets/images/post_processor/25_post_processor_layout/image012.jpg' | relative_url }})

Možnosť „Vykreslené interpolované SV“

**Údaje o materiáli ![]({{ '/assets/icons/pre_icons/mo_material_icon.jpg' | relative_url }}) : [2D, 3D]: **Tlačidlá „Údaje o materiáli“ v paneli RMB umožňujú používateľovi otvoriť okno s vlastnosťami materiálu (pozri obr. 25.12.). Ďalšie informácie nájdete v [Chapter 10. Material Data](/docs/en/pre_processor/10_material_data/10_material_data/)

![]({{ '/assets/images/post_processor/25_post_processor_layout/image013.jpg' | relative_url }})

Možnosti ponuky RMB pre materiál v strome operácií

## Grafické okno

V grafickom okne sa zobrazuje grafické znázornenie objektov. Zobrazujú sa tu kontúry stavových premenných nad objektmi, grafy, histogramy, sieť prietokov a vyplnenie čipu (kontaktné uzly). (Pozri obr. 25.1.)

Kliknutím pravým tlačidlom myši na grafické okno sa zobrazia niektoré možnosti na zobrazenie informácií o simulácii, nastavenie zobrazenia, meranie rozmerov a zmenu motívu pozadia. (Pozri obr. 25.13.) Ďalšie informácie o týchto možnostiach nájdete v [Graphics window RMB options.](../../integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout.htm#Graphics_window_RMB_options)

![]({{ '/assets/images/post_processor/25_post_processor_layout/image014.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/25_post_processor_layout/image015.jpg' | relative_url }})

(a) (b)

Možnosti grafického okna pomocou pravého tlačidla myši; (a) pre 2D, (b) pre 3D

**Zobraziť titulnú lištu:** Zobrazí titulnú lištu v okne zobrazenia.

## Vytváranie správ

Funkcia generovania správ umožňuje vytvárať správy v rôznych formátoch, ako sú ppt a pdf, pre vybrané funkcie následného spracovania, napríklad kontúry stavových premenných, sledovanie bodov, Flownet, výňatky z extrahovaných údajov, oblasti záujmu, súhrnné grafy, grafy zaťaženia a posunu a extrakciu údajov.

  
Ďalšie informácie o nastavení generovania správ nájdete v [Chapter 28. Report Generation](/docs/en/post_processor/27_introduction_to_report_generation/27_introduction_to_report_generation/).

## Ponuka widgetu v doku

Pomocou možností v ponuke widgetu Dock môže používateľ zapnúť alebo vypnúť zobrazenie krokov, strom operácií a okno na úpravu nastavení funkcií Post. (Pozri obr. 25.14.)

![]({{ '/assets/images/post_processor/25_post_processor_layout/image002.jpg' | relative_url }})

Ponuka widgetu Dock pre postprocesor 

**Súvisiace témy:**

[24\. Introduction to Post-Processor](/docs/en/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)

[26\. Post Processor Display controls](/docs/en/post_processor/26_post_processing_tools_and_controls/26_post_processor_features/)

[27\. Post Processing tools](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_post_processing_tools/)

[28\. Report Generation](/docs/en/post_processor/27_introduction_to_report_generation/27_introduction_to_report_generation/)
