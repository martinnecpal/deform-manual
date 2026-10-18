---
lang: sk
title: "Laboratórium 3D Gear-Mech Press"
---

# Laboratórium mechanických lisov 3D Gear

V tejto časti nastavíme jednoduchú operáciu s polotovarom ozubeného kolesa s využitím pohybu mechanického lisu v sprievodcovi programu 3D Forming Express.

## Prekvapenie 

### Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main. Vytvorte nový problém buď výberom položky **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem**, alebo kliknutím na ikonu New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Problem Setup. Vyberte prepínač „**3****D Forming Express**“ a v poli jednotiek vyberte systém jednotiek pomocou prepínača „**English**“, ako je znázornené na obr. 3DGML1.1. Názov úlohy zadajte ako „**3D-****Gear-MechPress**“ a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoríte novú úlohu s využitím integrovaného výrobného procesu.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0001.jpg' | relative_url }})

Okno na výber typu problému

Overte, či sa v editore operácií nachádza dlaždica operácie „3D Forming Express“. Premenujte prvú operáciu na „**Upset**“ dvojitým kliknutím na dlaždicu operácie v editore operácií (pozri obr. 3DGML1.2.).

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0002.jpg' | relative_url }})

Pomenovanie názvu operácie v editore operácií

### Postup

Na stránke „Process“ vyberte možnosti **Symmetry** a **Hot forging** a nastavte oba posuvníky o jeden stupeň nižšie ako „moderate“, aby ste skrátili čas simulácie (pozri obr. 3DGML1.3.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku výpočtu teploty.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0003.jpg' | relative_url }})

Stránka procesu

### Výpočet teploty

Na stránke „Výpočet teploty“ vyberte možnosť **konštantná teplota (izotermická)**. Výber konštantnej teploty znamená, že zanedbávame zmeny teploty obrobku počas tvárnenia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) do položky „Objekty“.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0004.jpg' | relative_url }})

Stránka „Výpočet teploty“

### Stránka objektu

Na stránke objektov vyberte **1 obrobok + 2 matrice** a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku obrobku.

### Obrobok

Pre náš obrobok použijeme teplotu objektu **2200°F**. Prejdite na stránku s geometriou obrobku.

#### Geometria obrobku

Na stránke „Geometria“ definujeme základný tvar nášho obrobku. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Vyberte typ **Valec** a nastavte rozmery obrobku na **2,5** v poli **Polomer** (R), **8,267** v poli **Výška** (H) a **0,1** v poli **Rádus rohu****polomer** (r), s **uhlom otáčania** **90** a **počet rezoch** **45** (pozri [Fig. 3DGML1.5.]()). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pre zatvorenie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku Symetria.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0005.jpg' | relative_url }})

Definovanie geometrie obrobku

#### Symetria obrobku

Definujte **rovinnú symetriu** pre obrobok na symetrických plochách. Vyberte plochy tak, ako je znázornené na obr. 3DGML1.6. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujte sieť.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0006.jpg' | relative_url }})

Okno „Symetria obrobku“

#### Sieť obrobku

Vytvorte sieť pre hodnotu nastavenia **System****type** kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obr. 3DGML1.7. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s materiálmi pre obrobok.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0007.jpg' | relative_url }})

Vytvorenie siete obrobku

####  Materiál obrobku

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice), ako je znázornené na obr. 3DGML1.8. Vyberte kategóriu **Steel_at_Extended_Temperatures**, potom **AISI-8620[1550-2200F(850 -1200C)]** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Materiál sa pridá do zoznamu materiálov a bude vybraný. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Top Die Geometry (Geometria hornej matrice).

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0008.jpg' | relative_url }})

Výber materiálu obrobku z knižnice materiálov

### Horná matrica

#### Geometria hornej matrice

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a naimportujte súbor **3d_flat top die.stl** zo zložky 3D\ LABS nachádzajúcej sa v inštalačnom adresári a skontrolujte geometriu. Označte symetrické plochy pomocou funkcie „Mark surface“, ako je znázornené na obr. 3DGML1.9. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0009.jpg' | relative_url }})

Priradenie roviny symetrie pre hornú matricu pomocou možnosti „Označiť povrch“

#### Stránka „Pohyb hornej matrice“

Tu definujeme našu hornú formu ako **mechanický lis**. Zvoľte tlačidlo **mechanický lis** a pozrite si dostupné možnosti (pozri obr. 3DGML1.10.).

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0010.jpg' | relative_url }})

Stránka venovaná mechanickému hodinkovému mechanizmu

Zachovajte predvolený smer pohybu **–Z**. Tuhosť a dĺžka spojovacej tyče sú voliteľné vstupné údaje pre definovanie mechanického lisu. Pre prvú operáciu použijeme **celkový****zdvih** **40** palcov a **1** zdvih/sek. Vyberte vzdialenosť medzi maticami a potvrďte aktuálny zdvih = -(celkový zdvih). Klikajte, kým sa nezobrazí stránka s geometriou spodnej matice ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (pozri obr. 3DGML1.11.).

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0011.jpg' | relative_url }})

Údaje o pohybe hornej matrice

### Spodná matrica

#### Geometria spodnej formy

Na stránke s geometriou spodnej formy kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Vyberte typ **Cylinder** a nastavte rozmery spodnej formy na **8** palcov **polomeru** (R), **4** palce **výšky** (H), s **Revolve****90° a počet **rezov** 45, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) na zatvorenie (pozri obr. 3DGML1.12.). Teraz kliknite na **Označiť povrch** a priraďte roviny symetrie tak, ako sme to definovali pre hornú formu.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0012.jpg' | relative_url }})

Geometria spodnej matrice

Pozrite si polohu troch objektov (pozri obr. 3DGML1.13.). Horná a spodná forma sa momentálne nachádzajú vnútri obrobku, čo povedie k nadmernému prepočítavaniu siete a nerealistickým výsledkom. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Positioning“.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0013.jpg' | relative_url }})

Poloha objektov po vytvorení

### Polohovanie

Na stránke polohovania kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}). Mali by ste vidieť polohu hornej a dolnej matrice nad a pod obrobkom. Automatické polohovanie vykonáva dve akcie:

  1. Poloha spodnej matrice voči obrobku pri spojení s hornou matricou bez úpravy zdvihu

  2. Poloha, v ktorej horná matrica zasahuje do obrobku počas aktualizácie zdvihu.

Po umiestnení foriem ponechajte predvolené nastavenia kontaktov a prejdite na stránku s ovládacími prvkami zastavenia.

### Ovládacie prvky na zastavenie

Pri metóde založenej na vzdialenosti medzi maticami musíme určiť kritérium zastavenia **vzdialenosť medzi objektmi**. Vybrané body by mali byť podobné tým, ktoré sú zobrazené nižšie.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0014.jpg' | relative_url }})

Vzdialenosť medzi objektmi Brzdové ovládacie prvky

V prvej operácii chceme, aby sa horná matrica posunula o 6 palcov, aby sa vytvoril správny tvar. Zadajte hodnotu vzdialenosti medzi objektmi **2,267** palca (pozri obr. 3DGML1.14.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}), aby ste prešli na hlavnú stránku zdvihu matrice.

### Zdvih primárneho valca

Všimnite si, že celkový posun primárneho lisovacieho nástroja je nastavený na približne 6 palcov. Metóda „vzdialenosť medzi lisovacími nástrojmi“ automaticky vypočíta celkový posun primárneho lisovacieho nástroja za používateľa. **Ak je zaškrtnuté políčko „presná hodnota“, ako tvoriaci zdvih sa použije hodnota zobrazená v poli „celkový posun primárneho lisovacieho nástroja“** (pozri obr. 3DGML1.15.). **V kroku 2 sa budeme venovať situáciám, keď nie je zaškrtnuté políčko „presná hodnota“**. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Ovládacie prvky simulácie“.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0015.jpg' | relative_url }})

Základný zdvih matrice

### Ovládacie prvky simulácie

Budeme používať predvolené systémové nastavenia (pozri obr. 3DGML1.16.) a prejdeme na stránku na vytvorenie databázy.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0016.jpg' | relative_url }})

Stránka s ovládacími prvkami simulácie

### Vytvoriť databázu

Na stránke „Generate DB“. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) spustíte kontrolu programu, či v nastavení úlohy nebolo niečo vynechané. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, uložte projekt a kliknite na režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), aby ste spustili simuláciu.

### Simulácia behu – Operácia 1

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Možnosti spustenia. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0017.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať na karte „Simulation Message“ a v časti „Simulation Graphics“ v oblasti zobrazenia „Graphics“ v režime simulácie. Pokiaľ je na karte „Simulation Message“ zaškrtnutá voľba „![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }})“ (čo je predvolené nastavenie), súbor správ sa bude automaticky aktualizovať.

### Následná spracovanie výsledkov – Operácia 1

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), kde si môžete prezrieť výsledok.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0018.jpg' | relative_url }})

Postprocesor MO

Niektoré dôležité stavové premenné je možné vybrať priamo z okna „Post Tools“, k ostatným sa dostanete cez dialógové okno „State Variable“ kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}).

Kliknite na graf ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) (zaťaženie – zdvih) a vytvorte graf času (s) v závislosti od zaťaženia (klb), ako aj graf času (s) v závislosti od rýchlosti (in/s) pre hornú maticu.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0019.jpg' | relative_url }})

Graf efektívnej stavovej premennej deformácie pre obrobok v poslednom kroku 1. operácie

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0020.jpg' | relative_url }})

Graf závislosti zaťaženia Z od času pre hornú matricu v 1. operácii

## Povrchová úprava zubov

### Zadanie úlohy

Pridajte novú operáciu 3D Forming Express a ako spôsob definovania operácie vyberte ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}).

### Horná matrica

V predvolenom nastavení sa všetky objekty odovzdajú do druhej operácie ako objekty načítané z databázy. Prejdite na stránku hornej matrice v strome. Všetky nastavenia z predchádzajúcej operácie sa odovzdajú do operácie 2, takže nie je potrebné vracať sa na predchádzajúce stránky. V prípade mechanického lisu je najlepšie nikdy nepoužívať hornú matricu načítanú z databázy. Ako typ objektu vyberte Define, aby ste definovali novú geometriu hornej matrice (pozri obr. 3DGML1.21.).

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0021.jpg' | relative_url }})

Hlavná stránka Die

#### Geometria hornej matrice

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou hornej matrice. Načítajte geometriu **3d_gear top die.stl** zo zložky 3D\ LABS, ktorá sa nachádza v inštalačnom adresári. Označte symetrické plochy pomocou funkcie „Označiť plochy“, ako je znázornené na obr. 3DGML1.22.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0022.jpg' | relative_url }})

Import geometrie hornej matrice

#### Pohyb hornej matrice

Prejdite na hlavnú stránku pohybu matrice a vyberte presný tvarovací zdvih. Predchádzajúce nastavenia lisu pre celkový zdvih a počet cyklov za sekundu zostávajú nezmenené (pozri obr. 3DGML1.23.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku objektu spodnej matrice.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0023.jpg' | relative_url }})

Údaje o pohybe hornej matrice

### Spodná matrica

Ako typ objektu vyberte **Definovať**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku geometrie.

#### Geometria spodnej matrice

Načítajte súbor **3d_******gear** bottom die.stl** zo zložky 3D\ LABS, ktorá sa nachádza v inštalačnom adresári. Označte symetrické plochy pomocou funkcie „Mark surface“, ako je znázornené na obr. 3DGML1.24. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s nastavením polohy.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0024.jpg' | relative_url }})

Import geometrie spodnej matrice

### Polohovanie

Pri operácii 2 použijeme zaškrtávacie políčko „Poloha v dolnej mŕtvej polohe“ na výpočet nášho tvárniaceho zdvihu. Aby bolo možné použiť toto zaškrtávacie políčko, horná a spodná matrica musia byť umiestnené v dolnej mŕtvej polohe.

Pred polohovaním si poznačte hodnotu tvárneho zdvihu uvedenú na stránke venovanej pohybu hornej matrice. Na stránke venovanej polohovaniu nastavte **polohu kolízie** hornej matrice voči spodnej matrici v smere –Z.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0025.jpg' | relative_url }})

Určovanie polohy na základe interferencie

Potom **posuňte** **hornú matricu o 0,2 palca** v smere osi Z. Matice sa teraz nachádzajú v dolnej mŕtvej polohe. **Prejdite** na stránku pohybu hornej matrice a všimnite si, že zdvih formovania a aktuálny zdvih sa aktualizujú na základe použitého polohovania. **V prípade mechanického lisu v programe Forming Express sa zdvih formovania vždy aktualizuje pri polohovaní hornej matrice.**

### Zdvih primárneho valca

Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí hlavná stránka zdvihu lisovacej formy. Vezmite na vedomie, že nie je naplánované žiadne polohovanie a kritérium zastavenia na základe vzdialenosti medzi objektmi je na stránke „Ovládacie prvky zastavenia“ deaktivované, pretože na hornej stránke pohybu lisovacej formy bol zvolený presný tvarovací zdvih.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0026.jpg' | relative_url }})

Hlavná stránka o zdvihu matrice

Ako už bolo spomenuté, pri kontrole presnej hodnoty platí, že celkový primárny zdvih formy = tvárniaci zdvih. Tvárniaci zdvih bol nedávno aktualizovaný o polohovanie, čo vysvetľuje zápornú hodnotu zobrazenú pri celkovom primárnom zdvihu formy. Červený text označuje, že zadaná hodnota celkového primárneho zdvihu formy je mimo povoleného rozsahu (pozri obr. 3DGML1.26.).

Je na užívateľovi, aby opravil nesprávnu hodnotu celkového primárneho zdvihu matrice. Zaškrtnite políčko „Poloha spodného mŕtveho bodu“ a všimnite si, že v dôsledku toho už nie je zaškrtnuté políčko „Presná hodnota“.

**Ak nie je zaškrtnutá možnosť „presná hodnota“, celkový zdvih hlavnej matrice sa nezhoduje so zdvihom pri tvárnení a slúži iba na výpočet veľkosti kroku pre simuláciu. Používateľ musí zadať približnú hodnotu, o koľko sa má horná matrica podľa očakávania posunúť.**

V tomto prípade sa horná matrica musí posunúť približne o 2 palce, aby dosiahla dolnú úvratu (pozri obr. 3DGML1.27.).

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0027.jpg' | relative_url }})

Poloha dolnej mŕtvej polohy bola skontrolovaná na stránke „Primárny zdvih matrice“

Zaškrtnutím políčka „Poloha dolnej mŕtvej polohy“ sa automaticky pridá naplánované polohovanie a zdvih formovania sa nastaví na nulu. Prejdite na stránku „Naplánované polohovanie“ a „Pohyb hornej matrice“, kde si môžete tieto zmeny prezrieť. Hodnota zdvihu formovania sa aktualizuje po vykonaní naplánovaného polohovania pri generovaní DB. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Ovládacie prvky simulácie

Budeme používať predvolené systémové nastavenia (pozri obr. 3DGML1.28.) a prejdeme na stránku na vytvorenie databázy.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0028.jpg' | relative_url }})

Simulácia riadi údaje

### Vytvoriť databázu

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vygenerovali databázu. Keď program dokončí zapisovanie databázy, uložte projekt a kliknite na režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), aby ste spustili simuláciu.

### Simulácia behu – Operácia 2

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Možnosti spustenia. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

### Následné spracovanie výsledkov – Operácia 2

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), kde si môžete prezrieť výsledok.

Niektoré dôležité stavové premenné je možné vybrať priamo z okna „Post Tools“ a k ostatným sa dostanete cez dialógové okno „State Variable“ kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}).

Kliknite na graf ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) (zaťaženie – zdvih) a vytvorte graf času (s) v závislosti od zaťaženia (klb), ako aj graf času (s) v závislosti od rýchlosti (in/s) pre hornú maticu pri operácii 2.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0029.jpg' | relative_url }})

Graf efektívnej stavovej premennej deformácie pre obrobok v poslednom kroku 2. operácie

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0030.jpg' | relative_url }})

Graf závislosti zaťaženia Z od času pre hornú matricu v 2. operácii
