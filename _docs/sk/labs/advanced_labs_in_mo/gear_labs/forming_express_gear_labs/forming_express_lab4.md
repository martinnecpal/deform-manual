---
lang: sk
title: "Založenie spoločnosti Express Lab4"
---

# Cvičenie č. 4. Symetria

### Vytvorenie nového problému

Ak chcete preskúmať 3D symetriu v programe DEFORM, otvorte nový projekt s názvom **FE_Gear_3D_Thermal_Sym** a s jednotkami **English**.

Tento projekt je rovnaký ako predchádzajúci **FE_Gear_3D_Thermal** ([Lab 3]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab3/' | relative_url }})), s tou výnimkou, že je modelovaných len 45° obrobku. Aby sa tento 45° sektor dielu deformoval rovnako ako celý diel, je potrebné použiť symetrické okrajové podmienky. V tomto laboratórnom cvičení sa budeme venovať rozdielom pri nastavovaní simulácie so symetriou.

### Pridať operácie

Pridajte tri operácie z programu Explorer:

  * [3D] Heat Transfer Express

  * [3D] Heat Transfer Express a

  * [3D] Forming Express

Dvojitým kliknutím na názov prvej operácie ho zmeňte na **Air Transfer**. Názov druhej operácie zmeňte na **Rest on Die**. Názov tretej operácie „Forming“ ponechajte bez zmeny.

Kliknite pravým tlačidlom na **obrobok** a vyberte možnosť **Preniesť objekt do všetkých operácií**. Podobne kliknite pravým tlačidlom na **hornú matricu** a **spodnú matricu** a pre oba objekty použite možnosť **Preniesť objekt do nasledujúcej operácie**.

### Definícia pojmu „preprava vzduchu“

Kliknite na operáciu **Air Transfer**. V tomto cvičení použijeme **Symmetry**. Overte, či je typ ohrevu nastavený na **Transfer**. Posuvníky **Presnosť** a **Zložitosť** nechajte v polohe **Stredná**. (Pozri obr. L4.1.). Na stránke Objekty ponechajte voľbu **Iba 1 obrobok** a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Obrobok.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab4_image0001.jpg' | relative_url }})

Okno procesu

#### Zadajte všeobecné údaje o obrobku

Nechajte teplotu obrobku na hodnote 2250 °F. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou.

#### Vytvorenie geometrie obrobku z primitívu

Definujte geometriu ako základný **valec** s **priemerom** **5** palcov, **výškou** **8,1** palca, **uhol otáčania****** **45** stupňov a **polomer rohu****** **0,2** palca. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) priraďte symetriu. (Pozri obr. L4.2.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab4_image0002.jpg' | relative_url }})

Okno „Geometrické primitívy obrobku“

#### Nastavenie symetrie pre obrobok

Každú z dvoch rezaných plôch sme pridali ako rovinu symetrie tak, že sme ich označili myšou a následne klikli na ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Kliknite na každú z položiek v časti „Planárna symetria“ a sledujte, ako sa plochy zvýraznia (pozri obr. L4.3).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab4_image0003.jpg' | relative_url }})

Okno „Symetria obrobku“

#### Vytvorenie siete pre obrobok

Vyberte voľbu **Užívateľsky definované** a nastavte **Cieľový počet prvkov** na hodnotu **10 000** a vygenerujte sieť.

#### Priradiť materiál k obrobku

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice). Vyberte kategóriu **Steel_at_Extended_Temperatures**, potom **AISI-8620[1550-2200F(850 -1200C)]** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Kliknite na položku **AISI-8620[1550–2200 °F (850 – 1200 °C)]** v okne s materiálmi, aby ste materiál priradili k obrobku. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku BCC.

#### Obrobok BCC

Uistite sa, že na rovinách symetrie sú definované okrajové podmienky symetrie a že výmena tepla s okolím je definovaná na všetkých plochách okrem rovín symetrie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Heat Condition“ (Teplotné podmienky).

#### Nastaviť teplotné podmienky

Nastavte **čas prenosu** na **5** sekúnd, potvrďte predvolenú hodnotu teploty prostredia a koeficientu konvekcie (pozri [Fig. L3.6.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab3/' | relative_url }}#Fig_L3_6_Heat_condition_window)). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky simulácie.

#### Ovládacie prvky simulácie

Použite predvolené ovládacie prvky simulácie definované systémom, takže nie sú potrebné žiadne zmeny. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujte databázu.

#### Vytvoriť databázu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}). Ak sa na karte „Správy“ nenachádzajú žiadne chyby ani varovania, pokračujte a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Teraz kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}), aby ste prešli na ďalšiu operáciu.

### Operácia „Rest on Die“

Pri druhej operácii bude typ prenosu tepla nastavený na **Odpočinok na matrici**. Tým sa simuluje únik tepla z obrobku do nástroja od okamihu jeho umiestnenia na spodnú matricu až do dokončenia zdvihu lisu. Pri tejto operácii by mal obrobok priliehať k spodnej matrici, zatiaľ čo horná matrica by mala byť umiestnená v určitej vzdialenosti od obrobku.

Poznámka: Forma typu „Dwell“ je určená na odvod tepla po kovaní a využíva vyššie koeficienty odvodu tepla, ktoré zodpovedajú úplnejšiemu kontaktu s formou.

#### Definícia výpočtu teploty

Použite možnosť **Vypočítať teplotu iba v obrobku**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Objekty“.

#### Určte počet objektov

Zachovajte možnosť **1 obrobok + 2 matrice**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Obrobok“.

#### Definovanie obrobku na tepelné uvoľnenie

Všetky údaje o obrobku sa načítajú z výsledkov prvej operácie v databáze. Preskočte obrobok a prejdite na hornú matricu.

#### Hlavná stránka „Top die“

Skontrolujte, či je teplota hornej matrice **300** °F. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou hornej matrice.

#### Importovať geometriu hornej matrice

Načítajte súbor STL s geometriou hornej matrice „**gear top die.****STL**“ pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Importovať geometriu zo súboru) tak, že vyhľadáte cestu k súboru s geometriou v inštalačnej zložke V*_* \Tutorials. Matrice je orientovaná pozdĺž inej osi ako obrobok. Tým sa budeme zaoberať v neskoršom kroku.

Pri spustení simulácie tvárnenia použijeme riadenie zastavenia podľa vzdialenosti medzi formami, ale keďže nástroje sú definované v aktuálnej operácii, je potrebné teraz definovať aj referenčné body. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) a vyberte bod na odliatku (pozri [Fig. L3.7.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab3/' | relative_url }}#Fig_L3_7_Top_die_with_the_selected_reference_point)), čím vyberiete referenčný bod na hornej matrici. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali spodnú matricu.

#### Všeobecná stránka o spodnej matrici

Skontrolujte, či je teplota spodnej formy **300** °F. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou spodnej formy.

#### Import geometrie spodnej matrice

Načítajte súbor STL s geometriou spodnej matice „**gear bottom die.****STL**“ pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Importovať geometriu zo súboru) tak, že vyhľadáte cestu k súboru s geometriou v inštalačnom priečinku V*_* \Tutorials. Matrice je orientovaná pozdĺž inej osi ako obrobok. Tým sa budeme zaoberať v neskoršom kroku.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) a vyberte bod na odtokovom žľabe (pozri [Fig. L3.8.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab3/' | relative_url }}#Fig_L3_8_Bottom_die_with_the_selected_reference_point)), aby ste vybrali referenčný bod na spodnej matrici. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste určili polohu.

#### Určenie polohy pre odpočinok pri teple

V tomto bode je obrobok orientovaný pozdĺž osi Z a nástroje sú orientované pozdĺž osi Y, ako je znázornené na obrázku [Fig. L3.9.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab3/' | relative_url }}#Fig_L3_9_Orientation_of_does_and_Workpiece)

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}). Najskôr otočte formy tak, aby boli orientované pozdĺž osi Z. Nastavte metódu na **Rotácia**. Nastavte nasledujúce parametre:

Polohovací objekt: **Horná matrica**.

Osa: X

Stred otáčania: Definovaný používateľom (0,0,0)

Uhol: 90 stupňov.

Chceme otočiť obe matrice súčasne, preto prejdite na kartu **Coupled** a zaškrtnite políčko **Bottom****Die**. Tým sa prepojí akékoľvek vykonané polohovanie (pozri [Fig. L3.10.)]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab3/' | relative_url }}#Fig_L3_10_Positioning_Top_die_with_Coupled_Bottom_object)). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) otočte nástroje tak, aby boli zarovnané s obrobkom.

V súčasnosti sú nástroje aj obrobok zarovnané pozdĺž osi Z, avšak nástroje sú od seba príliš blízko, ako je znázornené na obrázku [Fig. L3.11.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab3/' | relative_url }}#Fig_L3_11_Objects_after_rotation_position). Ďalším krokom je posunúť hornú maticu do polohy „hore“, ďalej od obrobku.

Zrušte začiarknutie položky „spojené polohovanie“ a následne nastavte polohu **** Top **Die** pomocou funkcie **Offset** o **12** palcov v smere osi Z.

Nakoniec sa musíme uistiť, že spodná forma správne prilieha k obrobku. Keďže obrobok sa v tejto operácii načítava z databázy, nemôžeme použiť bežné polohovanie. Môžeme však využiť naplánované polohovanie, ktoré sa dokončí počas behu projektu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte dialógové okno Polohovanie objektu a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku Naplánované polohovanie.

#### Nastavenie plánovaného polohovania pre tepelné odpočinutie

Pomocou ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridajte naplánovanú polohovaciu operáciu a pomocou funkcie **Interference** nastavte polohu **spodnej matrice** vo smere **Z** vo vzťahu k **obrobku**.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a na stránke naplánovaného polohovania by sa mala zobraziť táto naplánovaná operácia (pozri [Fig. L3.13.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab3/' | relative_url }}#Fig_L3_13_Scheduled_positioning_window)). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre kontakt.

#### Nastavenie kontaktov pre funkciu „Heat Resting“

V okne „Kontakt“ použite predvolené **systémom definované** koeficienty a nastavenia tolerancie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujte tepelné podmienky.

#### Definovanie podmienok ohrevu pre tepelné odležanie

**Doba odpočinku** bude **4** sekundy. Potvrďte predvolenú teplotu a koeficient konvekcie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku ovládacích prvkov simulácie.

#### Nastavenie ovládacích prvkov simulácie pre tepelné odležanie

Použite definíciu kroku **User** a nastavte **čas na krok** na **0,1** s, **počet krokov** na **40** a **prírastok krokov pri ukladaní** na **5**. S týmito nastaveniami sa bude používať 10 krokov za sekundu, čo je vhodné pre simuláciu prenosu tepla zahŕňajúcu kontaktné podmienky. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na vygenerovanie databázy.

#### Vytvorenie databázy pre tepelné spevnenie

Prebehne kontrola údajov. Zobrazí sa správa: „Stav: Vytvorenie databázy nie je pre túto operáciu potrebné. Uskutoční sa počas behu programu.“ Databáza sa vytvorí automaticky po dokončení prvej operácie.

### Tvarovacia operácia

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) alebo jednoducho kliknite na dlaždicu „Forming“ v editore operácií, aby ste nastavili operáciu tvárnenia.

Všetky objekty sa načítajú z databázy na konci predchádzajúcej operácie „Rest on Die“, takže stačí len nastaviť:

  * Ovládanie pohybu

  * Polohovanie

  * Vzťahy medzi objektmi

  * Simulácia a ovládacie prvky na zastavenie

#### Priradiť pohyb hornej matrice

Kliknite na stránku **Pohyb hornej matrice** v strome operácií a nastavte **Rýchlosť** na konštantnú hodnotu **3** palcov za sekundu v smere **-Z**. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Plánované polohovanie“.

#### Plánované polohovanie

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a nastavte polohu **interferencie** medzi **hornej matrice** a obrobkom v smere **-Z**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Kontakt“.

#### Vzťah medzi objektmi

Použijú sa predvolené **systémom definované** nastavenia pre kovanie za tepla, takže nie je potrebné vykonávať žiadne zmeny.

#### Nastavenie primárnych ovládacích prvkov zdvihu matrice

Na stránke „Primárny zdvih matrice“ musíme nastaviť celkový zdvih matrice na hodnotu vhodnú pre túto operáciu tvarovania. Výška polotovaru je 8,1 palca. Táto hodnota je vhodná ako približná hodnota. Nastavte **Celkový zdvih primárnej matrice** na **8,1** palca. (Pozrite [Fig. L3.14.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab3/' | relative_url }}#Fig_L3_14_Primary_die_stroke_window)) Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky zastavenia.

#### Priradiť ovládacie prvky na zastavenie

Nastavte kritérium zastavenia **Vzdialenosť medzi objektmi** na hodnotu **0,25** palca, pričom ako referenčné objekty použite **Hornú matricu** a **Spodnú matricu** a ako smer nastavte **Z**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali ovládacie prvky simulácie (pozri [Fig. L3.15.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab3/' | relative_url }}#Fig_L3_15_Distance_between_objects_stopping_control)).

#### Definovanie riadenia simulácie pre tvárnenie

Použite typ definície kroku **system**, ktorý ako celkový posun použije 1,2-násobok hodnoty primárneho zdvihu matrice a vydelí ju predvoleným **počtom krokov** **100**, čo v tomto prípade znamená (1,2 × 8,1)/100 = 0,0972 palca na krok, a uložte každých **10** krokov do databázy. (Pozri [Fig. L3.16.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab3/' | relative_url }}#Fig_L3_16_Forming_operation_Simulation_controls_settings))

  
Ako bolo uvedené v časti o prevádzke v kľudovom režime, vykoná sa kontrola údajov, ktorá ukáže, či sa vyskytli nejaké chyby; v opačnom prípade sa chyby v databáze vygenerujú počas behu programu. Uložte projekt.

Kliknite na tlačidlo režimu MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) (nad stromom operácií), aby ste spustili simuláciu.

### Spustenie a sledovanie simulácie

3D simulácie je možné spúšťať rýchlejšie využitím viacerých procesorov alebo viacerých jadier na jednom procesore. Ak má váš počítač 4 jadrá, kliknite na označenie ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}).

nastavte režim simulácie na **Interaktívny** a vyberte **Pokračovať****Spustiť**  
nastavte MPI 3D na hodnotu **4.** (pozri [Fig. L3.17.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab3/' | relative_url }}#Fig_L3_17_Run_option_window))

Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) a následne na ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}).

Počas behu simulácie kliknite na tlačidlo „Teplota“ ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}), aby ste si v grafickom okne mohli prezrieť teploty. Na zviditeľnenie foriem je užitočné použiť **režim viacerých objektov** ![]({{ '/assets/icons/pre_icons/mo_show_multi_obj_icon.jpg' | relative_url }}). 

Po dokončení simulácie kliknite na tlačidlo režimu MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), aby ste si prezreli výsledky.

### Výsledky kontroly v režime príspevku

Kliknite na ikonu 3D zrkadlenie ![]({{ '/assets/icons/post_icons/mo_3d_mirroring_icon.jpg' | relative_url }}). Uistite sa, že je zvolená možnosť Pridať, a kliknite na **symetrickú****rovinu** objektu. Pridá sa zrkadlovo otočený objekt. Pokračujte v klikaní na rovinu symetrie, kým nevytvoríte celý objekt. Ak urobíte chybu, môžete použiť možnosť „Odstrániť“ na vymazanie pridaného úseku (pozri obr. L4.4.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab4_image0004.jpg' | relative_url }})

Okno 3D zrkadlenia v príspevku na MO

Prejdite jednotlivými krokmi simulácie. Porovnajte výsledky s výsledkami úplného modelu. Výsledky by mali byť v podstate rovnaké.

Poznámka: Pri vykresľovaní krivky závislosti zaťaženia od zdvihu sa zobrazované zaťaženie týka iba tohto 45° úseku. Dialógové okno Graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) obsahuje možnosť „Scale“ (Mierka), ktorá umožňuje vynásobiť zaťaženie číslom 8, čím sa získa zaťaženie potrebné na vytvorenie celého dielu. (Pozri obr. L4.5.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab4_image0005.jpg' | relative_url }})

Graf zdvihu zaťaženia so stupnicou
