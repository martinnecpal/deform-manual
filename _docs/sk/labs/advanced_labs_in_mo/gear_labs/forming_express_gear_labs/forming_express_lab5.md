---
lang: sk
title: "Vytvorenie Express Lab5"
---

# Cvičenie č. 5. Premena z 2D na 3D

### Vytvorenie nového problému

Vytvorte nový projekt s názvom **FE_Gear23** a skopírujte existujúci projekt **FE_Gear_LargerBillet** (pozri obr. L5.1.) spolu s databázou.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab5_image0001.jpg' | relative_url }})

Okno „Nový projekt“ v programe MO

### Pridávanie operácií

Kliknite pravým tlačidlom na druhú dlaždicu operácie v editore operácií a odstráňte ju. Pridajte nasledujúce operácie:

  * [2D] Heat Transfer Express

  * Konvertor z 2D na 3D (nachádza sa v časti „Simulačný operátor“ na karte „Prehliadač“)

  * [3D] Forming Express

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab5_image0002.jpg' | relative_url }})

Zoznam operácií v editore operácií

V počiatočnej dlaždici **Upset** v editore operácií kliknite pravým tlačidlom myši na **obrobok** a vyberte možnosť **Preniesť objekt do všetkých operácií**. (Pozri obr. L5.2.)

### Prevádzka v núdzovom režime

Vyberte operáciu „Upset“ a v stromovej štruktúre objektov kliknite na vetvu „Výpočet teploty“. Použite možnosť **„Vypočítať teplotu iba v obrobku“**, ako je znázornené na obr. L5.3.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab5_image0003.jpg' | relative_url }})

Okno na výpočet teploty

**Vytvorenie databázy**

Kliknite na vetvu **Generate DB** v strome operácií a kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste skontrolovali a vygenerovali databázu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}), aby ste prešli na operáciu Heat Transfer Express.

### Prevádzka služby Heat Transfer Express

#### Postup

Na stránke „Proces“ vyberte typ vykurovania **Transfer**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby sa zobrazil zoznam objektov.

#### Výber objektov

Zaškrtnite políčko **Iba 1 obrobok** a v stromovej štruktúre objektov vyberte vetvu „Teplotné podmienky“, aby ste mohli definovať čas prenosu.

#### Teplotné podmienky

Nastavte **čas prenosu** na **5** sekúnd a potvrďte **predvolenú teplotu a koeficient konvekcie**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod do ovládacích prvkov simulácie.

#### Ovládacie prvky simulácie

Použite predvolené hodnoty a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nespustí operácia prevodníka z 2D do 3D.

### Operácia prevodu 2D na 3D

Skontrolujte, či je **Z** nastavené nahor (v súlade s ostatnými modelmi) a v 3D parametroch zadajte počiatočný uhol a **Revolve****angle** ako **0**, resp. **360**. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Geometria obrobku.

#### Geometria obrobku

Typ geometrie ponechajte na predvolenom type „Solid“. Položka **Počet sekcií** určuje počet geometrických sekcií po obvode. Jedna sekcia na jeden stupeň otáčania je vhodná, preto nastavte **Počet sekcií** na **360**. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_3d_preview_button.jpg' | relative_url }}) si zobrazíte náhľad 3D geometrie a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku so sieťou obrobku.

#### Sieť obrobku

Typ siete a **počet prvkov** ponechajte v predvolených hodnotách, teda **tetraéder** a **32 000**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Materiál obrobku“.

#### Materiál obrobku

Na stránke „Materiál“ ponechajte položku „Materiál“ nastavenú na (zdedené). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na hlavnú stránku „Horná forma“.

### 3D Forming Express

#### Všeobecný prehľad o hornej matrici

Ponechajte predvolenú teplotu **300** °F pre hornú maticu a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou hornej matice.

#### Geometria hornej matrice

Naimportujte súbor STL s geometriou hornej matrice „**gear top die.****STL**“ pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Importovať geometriu zo súboru) tak, že vyhľadáte cestu k súboru s geometriou v inštalačnom priečinku V*_* \Tutorials.

Pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) určte referenčný bod na ploche flash. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na hlavnú stránku o pohybe matrice.

#### Pohyb hornej matrice

Nastavte **rýchlosť** na konštantnú hodnotu **3** palcov za sekundu v smere **-Z**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Spodná matrica“.

#### Všeobecné informácie o spodnej matrici

Ponechajte predvolenú teplotu **300** °F pre spodnú formu a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou spodnej formy.

#### Geometria spodnej matrice

Naimportujte súbor STL s geometriou spodnej matrice „**gear bottom die.****STL**“ pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Importovať geometriu zo súboru) tak, že vyhľadáte cestu k súboru s geometriou v inštalačnom priečinku V*_* \Tutorials. Matrica je orientovaná pozdĺž inej osi ako obrobok. Tým sa budeme zaoberať v neskoršom kroku. Definujte referenčný bod na odtokovom žľabe pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku polohovania.

#### Polohovacie matrice

Otočte obe matice o **90** ° okolo osi **X** tak, aby boli zarovnané s obrobkom. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Plánované polohovanie“.

#### Plánované umiestnenie

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_auto_button.jpg' | relative_url }}), aby ste vygenerovali nasledujúce naplánované polohovanie, ako je znázornené na obr. L5.4. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Primárny zdvih matrice“.

'

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab5_image0004.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

#### Zdvih primárneho valca

V zadávacom poli nastavte hodnotu primárneho zdvihu matrice na **1,5**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky zastavenia.

#### Ovládacie prvky na zastavenie

Nastavte vzdialenosť medzi objektmi na **0,25** palca a ako referenčné objekty zvoľte „Top die“ a „Bottom die“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre simuláciu zdvihu.

#### Ovládacie prvky simulácie

Nastavte **Počet krokov** na **1000**, **Krok** na **5**; použijeme metódu krokovania typu **User** s konštantným **posunom matrice** nastaveným na **0,02** palca.

Uložte projekt a kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií), aby ste spustili simuláciu.

### Spustenie a sledovanie simulácie

3D simulácie je možné spustiť rýchlejšie využitím viacerých procesorov alebo viacerých jadier v jednom procesore. Ak má váš počítač 4-jadrový procesor, kliknite na označenie ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}).

nastavte režim simulácie na **Interaktívny** a vyberte **Pokračovať****Spustiť**  
nastavte MPI 3D na hodnotu **4.** (pozri [Fig. L3.17.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab3/' | relative_url }}#Fig_L3_17_Run_option_window))

Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) a následne na ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}).

Po dokončení simulácie kliknite na tlačidlo režimu MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), aby ste si prezreli výsledky.

### Prezrite si výsledky

Prejdite všetky kroky a sledujte tvary objektov pri operáciách v 2D a 3D.

'![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab5_image0005.jpg' | relative_url }})

Tvar objektu – obrobok pred prevodom do 3D a po prevode do 3D objektu
