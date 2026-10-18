---
lang: sk
title: "Laboratórium tvarovania 5"
---

# Cvičenie č. 5. Premena z 2D do 3D

### Vytvorenie nového problému

Vytvorte nový projekt s názvom **Gear23** a skopírujte existujúci projekt **Gear_LargerBillet**.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab5_image0001.jpg' | relative_url }})

Okno „Nový projekt“ v programe MO

### Pridávanie operácií

Kliknite pravým tlačidlom myši na druhú dlaždicu operácie v editore operácií a odstráňte ju. Pridajte nasledujúce operácie:

  * [2D] Heat Transfer Express

  * Konvertor z 2D do 3D (nachádza sa v nástroji Simulation Operator)

  * [3D] Forming Express

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab5_image0002.jpg' | relative_url }})

Zoznam operácií v editore operácií

### Prevádzka v núdzovom režime

V úvodnej karte „Upset“ v editore operácií kliknite pravým tlačidlom myši na **obrobok** a vyberte možnosť **Preniesť objekt do všetkých operácií**.

Vyberte operáciu **Upset** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). Prejdite do časti „Simulation controls“ a **zaškrtnite****režim****Heat****transfer**.

**Vytvorenie databázy**  
V strome operácií vyberte položku **Generate****DB** a vygenerujte databázu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}), aby ste spustili operáciu Heat Transfer Express.

### Prevádzka služby „Heat Transfer Express“

#### Postup

Na stránke „V procese“ vyberte typ vykurovania **Transfer**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre zobrazenie zoznamu objektov.

#### Výber objektov

Zvoľte**len 1 obrobok** (rádiové tlačidlo). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre stav „Heat“.

#### Teplotné podmienky

Nastavte **čas prenosu****time** na **5** sekúnd a potvrďte **predvolenú teplotu** a **koeficient konvekcie****coefficient**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do ovládacích prvkov simulácie.

#### Ovládacie prvky simulácie

Použite predvolenú hodnotu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nespustí operácia konvertora 2D na 3D.

### Operácia prevodu 2D na 3D

Skontrolujte, či je **Z** nastavené nahor (v súlade s ostatnými modelmi) a či sú v 3D parametroch počiatočný uhol a uhol otáčania nastavené na 0 a 360, aby sa vytvoril celý obrobok. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Geometria obrobku.

#### Geometria obrobku

**Počet sekcií** určuje počet geometrických sekcií po obvode. Osvedčilo sa nastaviť jednu sekciu na jeden stupeň otáčania, preto nastavte **počet sekcií** na **360**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku so sieťou obrobku.

#### Sieť obrobku

Nechajte počet prvkov siete na predvolenom počte **32000**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Materiál obrobku“.

#### Materiál obrobku

Na stránke „Materiál“ ponechajte nastavenie „(zdedené)“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí hlavná stránka „Forming Express – Horná matrica“.

### 3D Forming Express

#### Všeobecný prehľad

Ponechajte predvolenú teplotu **300** °F pre hornú matricu a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou hornej matrice.

#### Geometria hornej matrice

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a pomocou ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) otvorte (importujte) súbor „**gear top die.STL**“. Geometria hornej matrice sa nachádza v inštalačnej zložke programu DEFORM v adresári \Tutorials. Pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) definujte referenčný bod na odlievacej ploche. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Pohyb hornej matrice.

#### Pohyb hornej matrice

Nastavte **rýchlosť** na konštantnú hodnotu **3** palcov za sekundu v smere **-Z**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku spodnej matrice.

#### Všeobecné informácie o spodnej matrici

Ponechajte predvolenú teplotu **300** °F pre spodnú maticu a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou spodnej matice.

#### Geometria spodnej matrice

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a pomocou ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) otvorte (importujte) súbor „**gear bottom die.STL**“. Geometria spodnej matrice ozubeného kolesa sa nachádza v inštalačnej zložke programu DEFORM v adresári \Tutorials. Pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) definujte referenčný bod na odtokovom žľabe. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku polohovania.

#### Polohovacie matrice

Otočte obe matice o 90° okolo osi X tak, aby boli zarovnané s obrobkom. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Naplánované polohovanie“.

#### Plánované umiestnenie

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_auto_button.jpg' | relative_url }}) na stránke s naplánovaným polohovaním a uvidíte naplánované polohovanie, ako je znázornené na obr. L5.3. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s ovládacími prvkami na zastavenie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab5_image0003.jpg' | relative_url }})

Plánované časové okno na zameranie polohy

#### Ovládacie prvky na zastavenie

Nastavte vzdialenosť medzi objektmi na **0,25** palca a ako referenčné objekty nastavte **hornú matricu** a **spodnú matricu**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste priradili stránku primárneho zdvihu matrice.

#### Zdvih primárneho valca

V zadávacom poli nastavte hodnotu **Primárny zdvih matrice** na **1,5**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky simulácie.

#### Ovládacie prvky simulácie

Nastavte **počet krokov** na **1000**, **Krok****prírastok** na **5**, vyberte metódu definície kroku **Typ****užívateľský** a definujte **konštantný****posun****matrice** ako **0,02** palca.

Uložte projekt a kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií), aby ste spustili simuláciu.

### Spustenie a sledovanie simulácie

3D simulácie je možné spustiť rýchlejšie využitím viacerých procesorov alebo viacerých jadier v jednom procesore. Ak má váš počítač 4-jadrový procesor, kliknite na označenie ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}).

nastavte režim simulácie na **Interaktívny** a vyberte **Pokračovať****Spustiť**  
zadajte počet procesorov na úlohu ako **4.** (**** pozri ****[Fig. L3. 13.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/forming_lab3/' | relative_url }}#Fig_L3_13_Run_option_window))****

****Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) a následne na **![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}).**

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Prezrite si výsledky

Prejdite všetky kroky a sledujte tvary objektov pri operáciách v 2D a 3D.
