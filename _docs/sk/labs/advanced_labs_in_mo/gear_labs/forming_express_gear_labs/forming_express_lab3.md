---
lang: sk
title: "Vytvorenie Express Lab3"
---

# Laboratórna práca č. 3. Kovanie s výpočtami teploty

V tomto cvičení budeme modelovať kovanie toho istého polotovaru ozubeného kolesa, tentoraz však s výpočtami teploty, bez úvodnej operácie zhutňovania a v 3D namiesto 2D (2D cvičenie s ozubenými kolesami).

Na simuláciu použijeme systém viacerých operácií:

  * Vyberanie rozohriateho polotovaru z pece a jeho presun na vzduchu do kováčskych nástrojov

  * Uloženie polotovaru na kováčske nástroje

  * Kovanie polotovaru.

Ak sa operácia prevrátenia nevykoná, na vnútornej strane polotovaru ozubeného kolesa vznikne záhyb. Na preskúmanie tohto záhybu použijeme rôzne nástroje na následné spracovanie.

### Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**Anglický**“ pomocou prepínača. Zadajte názov úlohy „**FE_Gear_3D_Thermal**“ a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoríte novú úlohu s použitím integrovaného výrobného procesu Deform.

Spustí sa grafické rozhranie MO spolu s oknom „New Project“ (Nový projekt), v ktorom je názov projektu nastavený na „FE_Gear_3D_Thermal“. Uistite sa, že políčko „First operation“ (Prvá operácia) nie je zaškrtnuté, keďže operáciu pridáme neskôr, a použite predvolený (domovský) adresár, ako je znázornené na obr. L3.1. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste pridali projekt. Na tento projekt sa bude odkazovať v budúcich laboratórnych cvičeniach, preto je dôležité použiť rovnaký názov ako vyššie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0001.jpg' | relative_url }})

Nové okno projektu MO

### Pridať operácie

Pridajte tri operácie z programu Explorer:

  * [3D] Heat Transfer Express

  * [3D] Heat Transfer Express a

  * [3D] Forming Express

Dvojitým kliknutím na názov prvej operácie ho zmeňte na **Air Transfer**. Názov druhej operácie zmeňte na **Rest on Die**. Názov tretej operácie „Forming“ ponechajte bez zmeny (pozri obr. L3.2.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0002.jpg' | relative_url }})

Premenované názvy operácií v editore operácií

Kliknite pravým tlačidlom myši na **obrobok** a vyberte možnosť **Preniesť objekt do všetkých operácií**. Podobne kliknite pravým tlačidlom myši na **hornú matricu** a **spodnú matricu** a pre obe vyberte možnosť **Preniesť objekt do nasledujúcej operácie** (pozri obr. L3.3.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0003.jpg' | relative_url }})

Editor operácií po odovzdaní objektov nasledujúcim operáciám

### Definícia pojmu „preprava vzduchu“

Kliknite na operáciu „Air Transfer“. V tomto cvičení použijeme celý diel. Skontrolujte, či je typ ohrevu nastavený na „Transfer“. Posuvníky **Presnosť** a **Zložitosť** nechajte nastavené na hodnotu **Stredná**. (Pozri obr. L3.4.). Na stránke „Objekty“ ponechajte zvolenú možnosť **Iba 1 obrobok** a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Obrobok“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0004.jpg' | relative_url }})

Okno procesu

### Definovanie všeobecných údajov o obrobku

Nastavte teplotu obrobku na **2250** °F. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou.

#### Vytvorenie geometrie obrobku z primitívu

Definujte geometriu ako základný **valec** s **priemerom** **5** palcov, **výškou** **8,1** palca a **polomerom rohu** **0,2** palca. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na vytvorenie siete.

#### Vytvorenie siete pre obrobok

Vytvorte sieť pomocou predvoleného nastavenia systémovej siete s 80 000 prvkami. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Material“ (Materiál).

####  Priradiť materiál k obrobku

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice). Vyberte kategóriu **Steel_at_Extended_Temperatures**, potom **AISI-8620[1550-2200F(850 -1200C)]** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Kliknite na položku **AISI-8620[1550–2200 °F (850 – 1200 °C)]** v okne materiálov, aby ste materiál priradili k obrobku. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku BCC.

#### Obrobok BCC

Okrajové podmienky pre výmenu tepla s okolím by sa mali definovať automaticky. Overte to tak, že v strome okrajových podmienok kliknete na položku „Defined“ v časti „Heat Exchange with environment“ a skontrolujete, či sú všetky plochy zelené, ako je znázornené na obr. L3.5. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby sa otvorila stránka „Heat Condition“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0005.jpg' | relative_url }})

Okno BCC obrobku

### Nastaviť teplotné podmienky

Nastavte **čas prenosu** na **5** sekúnd, potvrďte **predvolenú teplotu prostredia** a **koeficient konvekcie** (pozri obr. L3.6.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky simulácie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0006.jpg' | relative_url }})

Okno nastavení teploty

### Ovládacie prvky simulácie

Použite predvolené ovládacie prvky simulácie definované systémom, takže nie sú potrebné žiadne zmeny. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujte databázu.

### Vytvoriť databázu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}). Ak sa na karte „Správy“ nenachádzajú žiadne chyby ani varovania, pokračujte a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Teraz kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}), aby ste prešli k ďalšej operácii.

### Operácia „Rest on Die“

Pri druhej operácii bude typ prenosu tepla **Odpočinok na matrici**. Tým sa simuluje únik tepla z obrobku do nástroja od okamihu, keď je obrobok umiestnený na spodnú matricu, až do dokončenia zdvihu lisu. Pri tejto operácii by sa obrobok mal dotýkať spodnej matrice, zatiaľ čo horná matrica by mala byť umiestnená v určitej vzdialenosti od obrobku.

**Poznámka:** Forma typu „Dwell“ je určená na odvod tepla po kovaní a využíva vyššie koeficienty odvodu tepla, ktoré zodpovedajú úplnejšiemu kontaktu s formou.

### Definícia výpočtu teploty

Použite možnosť **Vypočítať teplotu iba v obrobku**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Objekty“.

### Určte počet objektov

Zachovajte možnosť **1 obrobok + 2 matrice**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Obrobok“.

### Obrobok

Všetky údaje o obrobku sa načítajú z výsledkov prvej operácie v databáze. Preskočte obrobok a prejdite k hornej matrici.

### Hlavná stránka „Top die“

Skontrolujte, či je teplota hornej matrice **300** °F. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou hornej matrice.

**Importovať geometriu hornej matrice**

****Naimportujte súbor STL s geometriou hornej matrice „**gear top die.STL**“ pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Importovať geometriu zo súboru) a vyhľadajte cestu k súboru s geometriou v inštalačnom priečinku V*_* \Tutorials. Matrica je orientovaná pozdĺž inej osi ako obrobok. Tým sa budeme zaoberať v neskoršom kroku.

Pri simuláci formovania použijeme riadenie zastavenia na základe vzdialenosti medzi formami, avšak keďže nástroje sú definované v aktuálnej operácii, je potrebné teraz definovať aj referenčné body. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) a vyberte bod na odlievanej ploche (pozri obr. L3.7.), čím vyberiete referenčný bod na hornej matrici. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujte spodnú matricu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0007.jpg' | relative_url }})

Vytvoriť hornej matice so zvoleným referenčným bodom

### Všeobecná stránka o spodnej matrici

Skontrolujte, či je teplota spodnej formy **300** °F. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou spodnej formy.

**Importovať geometriu spodnej formy**  
Naimportujte súbor STL s geometriou spodnej matrice „**gear bottom die.STL**“ pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Importovať geometriu zo súboru) tak, že vyhľadáte cestu k súboru s geometriou v inštalačnom priečinku V*_* \Tutorials. Matrice je orientovaná pozdĺž inej osi ako obrobok. Tým sa budeme zaoberať v nasledujúcom kroku.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) a vyberte bod na odtokovom žľabe (pozri obr. L3.8.), čím vyberiete referenčný bod na spodnej matrici. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste určili polohu objektu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0008.jpg' | relative_url }})

Spodná matrica s vybraným referenčným bodom

### Určenie polohy pre odpočinok pri teple

V tomto bode je obrobok orientovaný pozdĺž osi **Z** a nástroje sú orientované pozdĺž osi Y, ako je znázornené na obr. L3.9.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0009.jpg' | relative_url }})

Orientácia matíc a obrobku

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}). Najskôr otočte matrice tak, aby boli orientované pozdĺž osi Z. Nastavte metódu na **Rotácia** a použite nasledujúce nastavenia:

Polohovací objekt: **Horná matrica**.

Osa: X

Stred otáčania: Definovaný používateľom (0,0,0)

Uhol: 90 stupňov.

Chceme otáčať obe matrice spoločne, preto prejdite na kartu **Coupled** a zaškrtnite políčko **Bottom Die**. Týmto sa spodná matrica prepojí s akýmkoľvek nastavením polohy (pozri obr. L3.10.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0010.jpg' | relative_url }})

Umiestnenie hornej formy s prepojeným spodným objektom

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) otočte nástroje tak, aby boli vyrovnané s obrobkom.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0011.jpg' | relative_url }})

Poloha objektov po otočení

V súčasnosti sú nástroje aj obrobok zarovnané pozdĺž osi Z, avšak nástroje sú od seba príliš blízko, ako je znázornené na obr. L3.11. Ďalším krokom je posunutie hornej matrice do polohy „hore“, ďalej od obrobku.

**Zrušte zaškrtnutie** položky **spojené****polohovanie** a potom nastavte polohu **hornej****matrice** pomocou funkcie **Offset** o **12** palcov v smere Z.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0012.jpg' | relative_url }})

Horná matrica po posunutí polohy

Nakoniec sa musíme uistiť, že spodná forma správne prilieha k obrobku. Keďže obrobok sa pri tejto operácii načítava z databázy, nemôžeme použiť bežné polohovanie. Môžeme však použiť naplánované polohovanie, ktoré sa dokončí počas behu projektu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte dialógové okno Polohovanie objektu a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku Naplánované polohovanie.

### Nastavenie plánovaného polohovania pre odpočinok pri zahrievaní

Pomocou ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridajte naplánovanú polohovaciu operáciu a pomocou funkcie **Interference** nastavte polohu **spodnej** **matrice** vo smere **Z** vo vzťahu k **obrobku**.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a na stránke naplánovaného polohovania by sa mala zobraziť táto naplánovaná operácia (pozri obr. L3.13.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre kontaktovanie

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0013.jpg' | relative_url }})

Plánované časové okno na umiestnenie

### Nastavenie kontaktných údajov pre Heat Resting

V okne „Kontakt“ použite predvolené **systémom definované** koeficienty a nastavenia tolerancie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali tepelné podmienky.

### Nastavenie podmienok ohrevu pre tepelné odľahčenie

Doba odpočinku bude **4** sekundy. Potvrďte predvolenú teplotu a koeficient konvekcie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku ovládacích prvkov simulácie.

### Nastavenie ovládacích prvkov simulácie pre tepelné odpočinutie

Použite definíciu kroku **User** a nastavte **čas na krok** na **0,1** s, **počet krokov** na **40** a **prírastok kroku pri ukladaní** na **5**. S týmito nastaveniami sa za sekundu vykoná 10 krokov, čo je vhodné pre simuláciu prenosu tepla s kontaktom. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na vytvorenie databázy.

### Vytvorenie databázy pre tepelnú stabilizáciu

Prebehne kontrola údajov. Zobrazí sa správa: „Stav: Pre túto operáciu nie je potrebné vytvoriť databázu. K tomu dôjde počas behu programu.“ Databáza sa vytvorí automaticky po dokončení prvej operácie.

### Tvarovací proces

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) alebo jednoducho kliknite na dlaždicu „Forming“ v editore operácií, aby ste nastavili operáciu tvárnenia.

Všetky objekty sa načítajú z databázy na konci predchádzajúcej operácie „Rest on Die“, takže stačí len nastaviť:

  * Ovládanie pohybu

  * Polohovanie

  * Vzťahy medzi objektmi

  * Simulácia a ovládacie prvky na zastavenie

### Priradiť pohyb hornej matrice

Kliknite na stránku **Top Die Movement** v stromovej štruktúre objektov a nastavte rýchlosť na konštantnú hodnotu **3** palcov za sekundu v smere **-Z**. Kliknite na ****![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Scheduled Positioning.

### Plánované polohovanie

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a nastavte polohu **kolízie** medzi **hornej maticou** a **obrobkom** v smere **-Z**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Kontakt“.

### Vzťah medzi objektmi

Použijú sa predvolené **systémom definované** nastavenia pre kovanie za tepla, takže nie sú potrebné žiadne zmeny. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Primárny zdvih matrice“.

### Nastavenie primárnych ovládacích prvkov zdvihu matrice

Na stránke „Primárny zdvih matrice“ musíme nastaviť celkový pohyb matrice na hodnotu vhodnú pre túto operáciu tvárnenia. Výška polotovaru je 8,1 palca. Táto hodnota je vhodná ako približná hodnota. Nastavte **Celkový zdvih primárneho lisovacieho nástroja** na **8,1** palca. (Pozri obr. L3.14.) Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky zastavenia.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0014.jpg' | relative_url }})

Okno primárneho zdvihu matrice

### Priradiť ovládacie prvky zastavenia

Nastavte kritérium zastavenia **Vzdialenosť medzi objektmi** na hodnotu **0,25** in, pričom ako referenčné objekty použite **Hornú matricu** a **Spodnú matricu** a ako smer nastavte **Z**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali ovládacie prvky simulácie (pozri obr. L3.15.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0015.jpg' | relative_url }})

Ovládanie zastavenia na základe vzdialenosti medzi objektmi

### Definovanie riadenia simulácie pre tvárnenie

Použite typ definície kroku **system**, ktorý ako celkový posun použije 1,2-násobok hodnoty primárneho zdvihu matrice a vydelí ho predvoleným **počtom krokov** **100**, čo v tomto prípade znamená (1,2 × 8,1)/100 = 0,0972 palca na krok, a uložte každé **10** krokov do databázy. (Pozri obr. L3.16.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0016.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie formovacích operácií

Ako bolo uvedené v časti o prevádzke v kľudovom režime, vykoná sa kontrola údajov, ktorá ukáže, či sa vyskytli nejaké chyby; v opačnom prípade sa databáza vytvorí počas behu programu. Uložte projekt.

Kliknutím na tlačidlo režimu MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) (nad stromom operácií) spustíte simuláciu.

### Spustenie a monitorovanie simulácie

3D simulácie je možné spúšťať rýchlejšie využitím viacerých procesorov alebo viacerých jadier v jednom procesore. Ak má váš počítač 4-jadrový procesor, kliknite na označenie ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}).

nastavte režim simulácie na **Interaktívny** a vyberte **Pokračovať****Spustiť**  
určte MPI 3D ako **4\. (** pozri **obr. L3. 17.)**

  
![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0017.jpg' | relative_url }})

Spustiť okno s voľbami

Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) a následne na ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}).

Počas behu simulácie kliknite na tlačidlo „Teplota“ ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}), aby ste si v grafickom okne mohli zobraziť teploty. Na zviditeľnenie foriem je užitočné použiť **režim viacerých objektov** ![]({{ '/assets/icons/pre_icons/mo_show_multi_obj_icon.jpg' | relative_url }}). 

Po dokončení simulácie kliknite na tlačidlo režimu MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), aby ste si prezreli výsledky.

### Výsledky kontroly v režime príspevku

Prejdite jednotlivými krokmi a sledujte, ako sa súčiastka deformuje.

Kliknite na ikonu „Slicing ![]({{ '/assets/icons/pre_icons/mo_slicing_option.jpg' | relative_url }})“. Obrobok a nástroje budú ohraničené žltým rámčekom. Kliknite na okraj rámčeka. Objekty budú rozrezané kolmo na tento okraj (_ak sa formy nerozrežú, uistite sa, že je zvolená možnosť „rozrezať všetky objekty“_). Posunutím modrého posuvníka doľava alebo doprava posuniete rovinu rozrezávania dopredu alebo dozadu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0018.jpg' | relative_url }})

Okno na rezanie v príspevku na MO

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte dialógové okno na rozdelenie.

Zaznamenajte teplotu ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) v obrobku. Prejdite do dialógového okna „Set Up ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }})“ a nastavte mierku na **User** s minimálnou hodnotou 1000 °F a maximálnou hodnotou 2500 °F. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

Kliknite pravým tlačidlom myši na farebný pruh teploty v grafickom okne a vyberte **Typ farebného pruhu** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Teplota**. Teploty sa teraz zobrazujú pomocou intuitívnejšej farebnej schémy.

Kliknite na možnosť „Sledovanie bodu“ (![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }})). Funkcia sledovania bodu umožňuje sledovať pohyb bodu, ako aj vývoj stavových premenných v danom bode. Vyberte niekoľko bodov na reze obrobku.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab3_image0019.jpg' | relative_url }})

Okno sledovania bodov v príspevku na MO

Kliknite na ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}). Program bude chvíľu trvať, kým zmeria teploty v týchto bodoch, a následne zobrazí výsledok v grafe.
