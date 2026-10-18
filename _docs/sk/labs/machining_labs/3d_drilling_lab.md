---
lang: sk
title: "3D vŕtacie laboratórium"
---

# 3D vŕtacie laboratórium

1.1 Zhrnutie

1.2. Spustenie sprievodcu 3D obrábaním

1.3. Definujte údaje o procese obrábania

1.4. Definovanie vrtáka

1.4.1. Definícia objektu vrtáka

1.4.2. Definovanie geometrie vrtáka

1.4.3. Priradenie materiálu nástroja

1.4.4. Generovanie povrchovej siete pre nástroj

1.4.5. Definovanie BCC pre nástroj

1.5. Definovanie obrobku

1.5.1. Definícia objektu obrobku

1.5.2. Definovanie geometrie obrobku

1.5.3. Definovanie materiálu obrobku

1.5.4. Generovanie pletiva obrobku

1.5.5. Definovanie BCC pre obrobok

1.6. Umiestnenie predmetov

1.7. Definovanie parametrov opotrebenia nástroja

1.8. Definovanie vzťahov medzi predmetmi

1.9. Definovanie krokových ovládacích prvkov

1.10. Generovanie databázy

1.11. Simulácia pretekov

1.12. Výsledky simulácie po spracovaní

Zhrnutie

V tomto laboratóriu ukážeme, ako nastaviť vŕtacie laboratórium pomocou sprievodcu 3D rezaním. Simulácie vŕtania v DEFORMÁCII sú časovo náročné vzhľadom na počet otáčok vŕtačky potrebných na stanovenie charakteristického správania. Preto bude vynaložené maximálne úsilie na optimalizáciu veľkosti problému. Úvahy zahŕňajú zachovanie čo najmenšej veľkosti obrobku pri zachytávaní geometrie (priemeru aj hrúbky), použitie najväčšieho prvku, ktorý dokáže primerane zachytiť geometriu triesky, a prípadné predtvarovanie obrobku, aby sa eliminovala potreba simulovať prenikanie prechodného bodu predtým, ako vŕtačka dosiahne plnú hĺbku. Tento návod bude používať príklad 6 mm vŕtačky s dvoma závitmi, ktorá beží pri 400 otáčkach za minútu s posuvom 0,15mm/ot.

## Spustenie sprievodcu 3D obrábaním

Vytvorte nový problém buď výberom **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})* ***Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 3DDL1.1.) Vyberte prepínač „ * * 3D rezanie * * “ a systém jednotiek ako „**SI * * “ (pozri obr. 3DDL1.1). Definujte názov problému ako „**3D_Drilling** “ a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvorte nový problém s operáciou 3D rezania v sprievodcovi MO.

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0001.jpg' | relative_url }})

Vytvorenie novej operácie obrábania

## Definujte údaje o procese obrábania

Na stránke „Proces“ vyberte typ rezania ako „* * Vŕtanie * *“, zadajte * * Teplota prostredia ** ako ** 20 ** °C a použite predvolený * * Konvekčný koeficient ** ako ** 0,02 ** N/s/mm/C. Definujte * * Rýchlosť otáčania * * ako ** 400 ** ot./min. a ** rýchlosť posuvu ** (f) ako **0,15** mm/ot., ako je znázornené na obr. 3DDL1.2. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Nástroj.

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0002.jpg' | relative_url }})

Nastavenie parametrov procesu pre prevádzku vŕtania

## Definovanie vrtáka

### Definícia objektu vrtáka

Na tejto stránke nástroja definujte * * teplotu * * ako **20** °C a zapnite začiarkavacie políčko „**Vypočítať*** * teplotu nástroja ** “, aby sme mohli nástroj na výpočet rozloženia teploty sieťovať, ako je znázornené na obr. 3DDL1.3. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Geometria nástroja.

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0003.jpg' | relative_url }})

Stránka objektu nástroja

### Definovanie geometrie vrtáka

Na tejto stránke Vložiť geometriu musí používateľ definovať geometriu nástroja pomocou odkazu Definovať primitívne. Pomocou odkazu ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), ako je znázornené na obr. 3DDL1.4., otvoríme okno „Drillbit Primitive“, ako je znázornené na obr. 3DDL1.5. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) vytvoríte geometriu vrtáka pomocou parametrov, ako je znázornené na obr. 3DDL1.5.

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0004.jpg' | relative_url }})

Stránka geometrie nástroja

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0005.jpg' | relative_url }})

Definovanie geometrie vrtáka

### Priradenie materiálu nástroja

V okne Materiál potrebujeme načítať materiál z knižnice. Takže kliknite na možnosť „Load form Library“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a vyberte ** tvarovanie za tepla ****die material** category a vyberte „**Carbide(15%Cobalt)** “ material from the list to assign the material for tool as shown in the Fig. 3DDL1.6. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujete povrchovú sieť pre nástroj.

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0006.jpg' | relative_url }})

Priradenie materiálu nástroja

### Generovanie povrchovej siete pre nástroj

Na stránke Tool mesh vyberte metódu **Use****Relative* ** * mesh * **size**. Definujte **cieľový počet prvkov** ako **20000** a ** pomer veľkosti ** ako **0,3**, ako je znázornené na obr. 3DDL1.7. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vygenerujete povrchovú sieť. Sieť vyzerá tak, ako je znázornené na obr. 3DDL1.7. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na BCC.

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0007.jpg' | relative_url }})

Generovanie povrchovej siete nástroja pomocou relatívnej veľkosti ôk

### Definovanie BCC pre nástroj

Na tejto stránke BCC môže používateľ definovať tepelné BCC „* * teplo * ***výmena s* ***prostredím** “ a „**teplota** “. Predvolený BCC je automaticky priradený k vonkajšiemu povrchu vrtáka po vygenerovaní povrchovej siete, ako je znázornené na obr. 3DDL1.8.

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0008.jpg' | relative_url }})

Výmena tepla BCC nad nástrojom

## Definovanie obrobku

### Definícia objektu obrobku

Na tejto stránke objektu obrobku definujte teplotu ako * * 20 * * °C a typ objektu ako **plast**, ako je znázornené na obr. 3DDL1.9. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku geometrie obrobku.

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0009.jpg' | relative_url }})

Stránka objektu obrobku

### Definovanie geometrie obrobku

Na tejto stránke Geometria obrobku musíme definovať geometriu obrobku pomocou ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Na primitívnej stránke geometrie obrobku vyberte prepínač **valec** a definujte * * priemer ** (D) ako * * 12 mm * *, * * hrúbku * * ako * *4 mm** a **vrták****hrot** hĺbku ako **3,15mm**, ako je znázornené na obr. 3DDL1.10.

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0010.jpg' | relative_url }})

Vytvorenie geometrie obrobku valca

### Definovanie materiálu obrobku

V okne Materiál potrebujeme načítať materiál z knižnice. Takže kliknite na možnosť „**Load*** *Form*** *Library * * “ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a vyberte ** AISI-1045 (Machining)** z kategórie * * Steel * * pre priradenie materiálu k obrobku, ako je znázornené na obr. 3DDL1.11. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujete sieťovinu pre obrobok.

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0011.jpg' | relative_url }})

Priradenie materiálu pre obrobok

### Generovanie pletiva obrobku

Po vygenerovaní geometrie obrobku na strane s okami pomocou metódy **absolútnej veľkosti ôk ** definujte pomer veľkosti ** ako ** 10 ** a ** minimálnu veľkosť prvku ** ako ** 0,04 ** mm, ako je znázornené na obr. 3DDL1.12. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) dokončíte generovanie siete pre obrobok.

**Runtime meshing parametre:**

Ak chcete nastaviť parametre záberu za chodu, prepnite do expertného režimu pomocou ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}). V expertnom režime zvoľte**váhové faktory** kartu a definujte **Kmeň** hmotnosť na približne **0,65** , **Kmeň***rýchlosť** hmotnosť na približne **0,35** a nastavte iné hmotnosti na nulu (vrátane okien s okami) ako parametre sieťoviny za chodu (pozri obr. 3DDL1.13.). Po nastavení faktorov váženia prepnite do režimu vedenia pomocou ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na BCC.

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0012.jpg' | relative_url }})

Generovanie ôk obrobku pomocou absolútnej veľkosti ôk

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0013.jpg' | relative_url }})

Parametre váhového faktora generovania povrchovej siete obrobku Runtime

### Definovanie BCC pre obrobok

Na stránke BCC je v predvolenom nastavení rýchlosť všetkých uzlov na obvode obrobku fixovaná v smere X, Y a Z, ako je znázornené na obr. 3DDL1.14. Hraničné podmienky výmeny tepla sú automaticky priradené horným a spodným povrchom počas generovania siete, ako je znázornené na obr. 3DDL1.15. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Control.

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0014.jpg' | relative_url }})

Definovanie údajov BCC o rýchlosti

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0015.jpg' | relative_url }})

Definovanie výmeny tepla BCC

## Umiestnenie objektov

Na stránke Control kliknite na **'Position objects’** a skontrolujte polohu nástroja. Ak nástroj nie je v kontakte s obrobkom, umiestnite nástroj pomocou metódy interferencie a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujte parametre opotrebovania nástroja.

## Definovanie parametrov opotrebenia nástroja

Na stránke Opotrebenie nástroja zapnite začiarkavacie políčko „**Definovať****model na výpočet opotrebenia nástroja ** r“ a vyberte **Usui** model, použite predvolené parametre pre model Usui, ako je znázornené na obr. 3DDL1.16. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Kontakt.

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0016.jpg' | relative_url }})

Definovanie parametrov opotrebenia nástroja

## Definovanie vzťahov medzi objektmi

Na stránke Kontakt použijeme predvolené vzťahy. Kliknite na tlačidlo **Nástroj - Obrobok ** vzťah Upraviť a definujte koeficient šmykového trenia ako **0,6** a súčiniteľ prestupu tepla rozhrania ako **40** N/sec/mm/C (ako je znázornené na obr. 3DDL1.17.), kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) pre generovanie kontaktov. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Step Control.

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0017.jpg' | relative_url }})

stránka s kontaktnými informáciami

## Definovanie krokových ovládacích prvkov

Na stránke ovládania kroku definujte * * vrták * ** *hĺbku** ako **3,5 mm** a zvoľte * * Užívateľ * * prepínač pre nastavenie užívateľom definovaného** prírastku časového kroku * * ako * * 0,0005 * * , ponechajte zvyšok hodnôt v predvolenom nastavení, ako je znázornené na obr. 3DDL1.18. a pokračujte generovaním databázy kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0018.jpg' | relative_url }})

Stránka krokových ovládacích prvkov v režime SO SPRIEVODCOM

## Generovanie databázy

Na stránke Generovať databázu kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) a vygenerujte databázu. Sledujte správy na karte Správa informujúce o stave generovania databázy. Ak sa vyskytnú nejaké chyby, musíme ich opraviť pred generovaním databázy

## Simulácia behu

Po vygenerovaní databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad operačným stromom. Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. 3DDL1.19. Pomocou predvolenej možnosti **Pokračovať***Spustiť** vyberte možnosť „**Pokračovať z posledného kroku** “ (z kroku -1) a potom vyberte režim simulácie ako prepínač * * Interaktívne * *. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) pre spustenie simulácie.

Ak chcete definovať nastavenia MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}), okno Možnosti spustenia sa rozbalí a zobrazí možnosti definovania nastavení MPI pre simuláciu (maximálny počet procesorov, ktoré možno definovať v závislosti od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/machining_labs/3d_drilling_lab/image0019.jpg' | relative_url }})

Okno Spustiť simuláciu

Sledujte priebeh simulácie tak, že sa pozriete na kartu Simulation Message and Simulation Log a uistite sa, že je začiarknutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Používateľ môže zobraziť proces vŕtania, keď simulácia pokračuje do určenej hĺbky vŕtania z grafiky simulácie.

## Výsledky simulácie po spracovaní

Po dokončení simulácie skontrolujte výsledky prepnutím do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov simulácie. Prehrajte si kroky simulácie a sledujte tvorbu triesok počas procesu vŕtania.
