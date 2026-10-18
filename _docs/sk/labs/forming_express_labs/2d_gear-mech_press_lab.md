---
lang: sk
title: "Laboratórium 2D Gear-Mech Press"
---

# Laboratórium 2D Gear-Mech Press

V tomto laboratórnom cvičení nastavíme jednoduchú operáciu s polotovarom ozubeného kolesa pomocou ovládacích prvkov pohybu mechanického lisu v sprievodcovi 2D Forming Express.

1\. Operácia 1

1.1 Vytvorenie novej úlohy

1.2 Postup

1.3. Výpočet teploty

1.4. Stránka objektu

1.5. Obrobok

1.6. Horná matrica

1.7. Spodná forma

1.8. Polohovanie

1.9. Ovládacie prvky na zastavenie

1.10. Zdvih primárneho lisovacieho nástroja

1.11. Ovládacie prvky simulácie

1.12. Vytvorenie databázy

1.13. Spustenie simulácie

1.14. Následná spracovanie výsledkov

2\. Operácia 2

2.1. Formulácia problému

2.2. Horná matrica

2.3. Spodná forma

2.4. Polohovanie

2.5. Zdvih primárneho lisovacieho nástroja

2.6 Ovládacie prvky simulácie

2.7. Vytvorenie databázy

2.8. Spustenie simulácie

2.9. Následná spracovanie výsledkov

## Operácia 1

### Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main. Vytvorte nový problém buď výberom položky **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem**, alebo kliknutím na ikonu New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Problem Setup. Vyberte radiacie tlačidlo „**2D Forming Express**“ a v poli jednotiek vyberte radiacie tlačidlo „**English**“, ako je znázornené na obr. 2DGML1.1. Názov úlohy zadajte ako „******Gear-MechPress**“ a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoríte novú úlohu s využitím integrovaného výrobného procesu.

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0001.jpg' | relative_url }})

Okno na výber typu problému

Overte, či sa v editore operácií nachádza dlaždica operácie **2D Forming Express**. Premenujte prvú operáciu na „**Upset**“ dvojitým kliknutím na dlaždicu operácie v editore operácií (pozri obr. 2DGML1.2.).

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0002.jpg' | relative_url }})

Pomenovanie názvu operácie v editore operácií

### Postup

Na stránke „Process“ vyberte možnosti **2D Axisymmetric** a **Hot forging** a nastavte oba posuvníky o jeden stupeň nižšie ako „moderate“, aby ste skrátili čas simulácie (pozri obr. 2DGML1.3.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku výpočtu teploty.

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0003.jpg' | relative_url }})

Stránka procesu

### Výpočet teploty

Na stránke „Výpočet teploty“ vyberte možnosť **konštantná teplota (izotermická)**. Výberom konštantnej teploty zanedbávame zmeny teploty obrobku počas tvárnenia. Kliknite na stránku „![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) k objektu“.

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0004.jpg' | relative_url }})

Stránka „Výpočet teploty“

### Stránka objektu

Na stránke „Objekty“ vyberte **1 obrobok + 2 formy** a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku obrobku.

### Obrobok

Pre náš obrobok použijeme teplotu objektu **2200****°F**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku s geometriou obrobku.

#### Geometria obrobku

Na stránke „Geometria“ budeme na definovanie geometrie obrobku používať dostupné základné geometrické tvary. Vyberte základný tvar „Valec“ a nastavte rozmery **valca** na **polomer 2,5 palca**, **výšku 8,267in** a **polomer rohu 0,1in (R1 a R2)** (pozri obr. 2DGML1.5.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) na zatvorenie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku siete.

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0005.jpg' | relative_url }})

Definovanie geometrie

#### Sieť obrobku

Uistite sa, že na stránke „Mesh“ je vybraný systém. V poli „Počet prvkov“ by sa mala zobrazovať hodnota 1000. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím prejdete na stránku s materiálmi obrobku.

#### Materiál obrobku

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice), ako je znázornené na obr. 2DGML1.6. Zaškrtnite iba políčko „Hot Forming“ (Tepelné tvárnenie). Ak sú zaškrtnuté všetky políčka kategórií, vyberte kategóriu **Steel_at_Extended_Temperatures** (Oceľ pri rozšírených teplotách) a potom **AISI-8620[1550-2200F(850 -1200C)]** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Materiál sa pridá do zoznamu materiálov a bude vybraný. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Top Die Geometry (Geometria hornej matrice).

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0006.jpg' | relative_url }})

Výber materiálu obrobku z knižnice materiálov

### Horná matrica

#### Geometria hornej matrice

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a naimportujte súbor „**flat top die.igs**“ zo zložky 2D\ LABS nachádzajúcej sa v inštalačnom adresári a nezabudnite po importe geometriu otočiť. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

#### Stránka „Pohyb hornej matrice“

Tu definujeme našu hornú matricu ako mechanický lis. Zvoľte tlačidlo **mechanický lis** a pozrite si dostupné možnosti.

Zachovajte predvolený smer pohybu **–Y**. Tuhosť a dĺžka ojnice sú voliteľné vstupné údaje pre definovanie mechanického lisu. Pre prvú operáciu použijeme **celkový zdvih** **40** palcov a **1** zdvih/sek. Vyberte „**Vzdialenosť medzi maticami**“ a potvrďte aktuálny zdvih = -(celkový zdvih) (pozri obr. 2DGML1.7). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s geometriou spodnej matice.

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0007.jpg' | relative_url }})

Údaje o pohybe hornej matrice

### Spodná matrica

#### Geometria spodnej matrice

Na stránke s geometriou spodnej formy vyberte možnosť „Definovať primitív“, aby ste vytvorili spodnú formu pomocou valcového primitívu. Zadajte **polomer** **8** palcov a **výšku** **4** palce a po dokončení kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) (pozri obr. 2DGML1.8.).

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0008.jpg' | relative_url }})

Geometria spodnej matrice

Pozrite si polohu troch objektov (pozri obr. 2DGML1.9.). Horná a spodná forma sa momentálne nachádzajú vnútri obrobku, čo povedie k nadmernému prepočítavaniu siete a nerealistickým výsledkom. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Polohovanie“.

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0009.jpg' | relative_url }})

Poloha objektov po vytvorení

### Polohovanie

Na stránke polohovania kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}). Mali by ste vidieť polohu hornej a dolnej matrice nad a pod obrobkom. Automatické polohovanie vykonáva dve akcie:

  1. Poloha spodnej matrice voči obrobku pri spojení s hornou matricou bez úpravy zdvihu

  2. Poloha, v ktorej horná matrica zasahuje do obrobku počas aktualizácie zdvihu.

Po umiestnení foriem ponechajte predvolené nastavenia kontaktov a prejdite na stránku s ovládacími prvkami zastavenia.

### Ovládacie prvky na zastavenie

Pri metóde „vzdialenosť medzi formami“ je potrebné určiť kritériá zastavenia na základe vzdialenosti medzi objektmi. Vyberte body na hornej a spodnej forme podobne ako body znázornené na obr. 2DGML1.10.

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0010.jpg' | relative_url }})

Vzdialenosť medzi objektmi Brzdové ovládacie prvky

Pri prvej operácii chceme, aby sa horná matrica posunula o **6 palcov**, aby sa vytvoril správny tvar. Zadajte hodnotu vzdialenosti medzi matricami **2,267****palca** pre vzdialenosť medzi objektmi, ako je znázornené na obr. 2DGML1.10.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}), aby ste prešli na hlavnú stránku zdvihu matrice.

### Zdvih primárneho valca

Všimnite si, že celkový posun primárneho lisovacieho nástroja je nastavený približne na 6 palcov. Metóda „vzdialenosť medzi lisovacími nástrojmi“ automaticky vypočíta celkový posun primárneho lisovacieho nástroja za používateľa. **Ak je zaškrtnuté políčko „presná hodnota“, ako tvoriaci zdvih sa použije hodnota zobrazená v poli „celkový posun primárneho lisovacieho nástroja“** (pozri obr. 2DGML1.11.**). V kroku 2 sa budeme venovať situáciám, keď nie je zaškrtnuté políčko „presná hodnota“.** Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Simulation controls“ (Ovládacie prvky simulácie).

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0011.jpg' | relative_url }})

Základný zdvih matrice

### Ovládacie prvky simulácie

Budeme používať predvolené systémové nastavenia a prejdeme na stránku na vytvorenie databázy (pozri obr. 2DGML1.12.).

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0012.jpg' | relative_url }})

Stránka „Ovládacie prvky simulácie“

### Vytvoriť databázu

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení úlohy niečo nechýba. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, uložte projekt a kliknite na režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), aby ste spustili simuláciu.

### Simulácia behu – Operácia 1

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Možnosti spustenia. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0024.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať na karte „Simulation Message“ a v časti „Simulation Graphics“ v oblasti zobrazenia „Graphics“ v režime simulácie. Pokiaľ je na karte „Simulation Message“ zaškrtnutá voľba „![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }})“ (čo je predvolené nastavenie), súbor správ sa bude automaticky aktualizovať.

### Následná spracovanie výsledkov – Operácia 1

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), kde si môžete prezrieť výsledok.

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0013.jpg' | relative_url }})

Postprocesor MO

Niektoré dôležité stavové premenné je možné vybrať priamo z okna „Post Tools“, k ostatným sa dostanete cez dialógové okno „State Variable“ kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}).

Kliknite na graf ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) (zaťaženie – zdvih) a vytvorte graf času (s) v závislosti od zaťaženia (klb), ako aj graf času (s) v závislosti od rýchlosti (in/s) pre hornú maticu.

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0014.jpg' | relative_url }})

Graf efektívnej stavovej premennej deformácie pre obrobok v poslednom kroku 1. operácie

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0015.jpg' | relative_url }})

Graf závislosti zaťaženia Y od času pre hornú matricu v 1. operácii

## Operácia 2

###  Zadanie úlohy

Pridajte novú operáciu **2D Forming Express** a ako spôsob definovania operácie vyberte „**NO****\- hromadné nastavenie**“.

### Horná matrica

V predvolenom nastavení sa všetky objekty odovzdajú do druhej operácie ako objekty načítané z databázy. Prejdite na stránku hornej matrice v strome. Všetky nastavenia z predchádzajúcej operácie sa odovzdajú do operácie 2, takže nie je potrebné vracať sa na predchádzajúce stránky. V prípade mechanického lisu je najlepšie nikdy nepoužívať hornej matrice načítanú z databázy. Ako typ objektu pre hornú matricu vyberte „**Definovať**“ (pozri obr. 2DGML1.17.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku geometrie hornej matrice.

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0016.jpg' | relative_url }})

Stránka „Top Die“

#### Geometria hornej matrice

Načítajte geometriu **g****ear top die.IGS** zo zložky 2D\ LABS, ktorá sa nachádza v inštalačnom adresári. Skontrolujte geometriu a overte, či je správne tieňovanie a číslovanie bodov.

#### Pohyb hornej matrice

Prejdite na hlavnú stránku pohybu matrice a vyberte **presný tvarovací zdvih**. Predchádzajúce nastavenia lisu pre celkový zdvih a počet cyklov za sekundu zostávajú nezmenené (pozri obr. 2DGML1.18.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0017.jpg' | relative_url }})

Hlavná stránka o pohybe matrice

### Spodná matrica

Ako typ objektu vyberte **Definovať**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku geometrie.

#### Geometria spodnej matrice

Načítajte súbor **gear bottom die.IGS** zo zložky 2D\LABS, ktorá sa nachádza v inštalačnom adresári. Skontrolujte geometriu a overte, či je správne tieňovanie a číslovanie bodov. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s polohovaním.

### Polohovanie

Pri operácii 2 použijeme zaškrtávacie políčko „Poloha dolnej mŕtvej polohy“ na výpočet nášho tvárniaceho zdvihu. Aby bolo možné použiť toto zaškrtávacie políčko, horná a spodná matrica musia byť umiestnené v dolnej mŕtvej polohe.

Pred nastavením polohy si zapíšte hodnotu formovacieho zdvihu uvedenú na stránke venovanej pohybu hornej matrice. Na stránke venovanej nastavovaniu polohy nastavte **polohu kolízie** hornej matrice voči spodnej matrici v smere –Y.

Potom **posuňte** hornú matricu o 0,2 palca v smere osi Y. Matice sa teraz nachádzajú v dolnej mŕtvej polohe. **Prejdite** na stránku pohybu hornej matrice a všimnite si, že zdvih formovania a aktuálny zdvih sa aktualizujú na základe použitého polohovania. **V prípade mechanického lisu v programe Forming Express sa zdvih formovania vždy aktualizuje pri polohovaní hornej matrice.**

### Zdvih primárneho valca

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí hlavná stránka zdvihu lisovacej formy. Vezmite na vedomie, že nie je naplánované žiadne polohovanie a kritérium zastavenia na základe vzdialenosti medzi objektmi je na stránke „Ovládacie prvky zastavenia“ deaktivované, pretože na hornej stránke pohybu lisovacej formy bol zvolený presný tvarovací zdvih.

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0018.jpg' | relative_url }})

Hlavná stránka o zdvihu lisovacej matrice

Ako už bolo spomenuté, pri kontrole presnej hodnoty platí, že celkový primárny zdvih formy = tvárniaci zdvih. Tvárniaci zdvih bol nedávno aktualizovaný o polohovanie, čo vysvetľuje zápornú hodnotu, ktorá sa zobrazuje pri celkovom primárnom zdvihu formy. Červený text označuje, že zadaná hodnota celkového primárneho zdvihu formy je mimo povoleného rozsahu (pozri obr. 2DGML1.19.).

Je na užívateľovi, aby opravil nesprávnu hodnotu celkového primárneho zdvihu matrice. Zaškrtnite políčko „Poloha spodného mŕtveho bodu“ a skontrolujte, či sa v dôsledku toho už nezaškrtáva políčko „Presná hodnota“.

Ak nie je zaškrtnutá možnosť „presná hodnota“, celkový posun primárnej matrice sa nerovná formovaciemu zdvihu a slúži iba na výpočet veľkosti kroku pre simuláciu. Používateľ musí zadať približnú hodnotu, o koľko sa má horná matrica posunúť.

V tomto prípade sa horná matrica musí posunúť približne o 2 palce, aby dosiahla dolnú mŕtvu polohu (pozri obr. 2DGML1.20.).

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0019.jpg' | relative_url }})

Poloha dolnej mŕtvej polohy bola skontrolovaná na stránke „Primárny zdvih matrice“

Zaškrtnutím políčka „Poloha dolnej mŕtvej polohy“ sa automaticky pridá naplánované polohovanie a zdvih formovania sa nastaví na nulu. Prejdite na stránku „Naplánované polohovanie“ a „Pohyb hornej matrice“, kde si môžete tieto zmeny prezrieť. Hodnota zdvihu formovania sa aktualizuje po vykonaní naplánovaného polohovania pri generovaní DB. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazia ovládacie prvky simulácie.

### Ovládacie prvky simulácie

Budeme používať predvolené systémové nastavenia (pozri obr. 2DGML1.21.) a prejdeme na stránku na vytvorenie databázy.

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0020.jpg' | relative_url }})

Stránka Ovládacie prvky simulácie

### Vytvoriť databázu

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) a potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vygenerovali databázu. Keď program dokončí zapisovanie databázy, uložte projekt a kliknite na režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), aby ste spustili simuláciu.

### Simulácia behu – Operácia 2

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Možnosti spustenia. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“ (od kroku -1), potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

### Následné spracovanie výsledkov – Operácia 2

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), kde si môžete prezrieť výsledok.

Niektoré dôležité stavové premenné je možné vybrať priamo z okna „Post Tools“, k ostatným sa dostanete cez dialógové okno „State Variable“ kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}).

Kliknite na graf ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) (zaťaženie – zdvih) a vytvorte graf závislosti času (s) od zaťaženia (klb), ako aj graf závislosti času (s) od rýchlosti (in/s) pre hornú maticu pri operácii 2.

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0021.jpg' | relative_url }})

Graf efektívnej stavovej premennej deformácie pre obrobok v poslednom kroku 2. operácie

![]({{ '/assets/images/labs/forming_express_labs/2d_gear-mech_press_lab/image0022.jpg' | relative_url }})

Graf závislosti zaťaženia Y od času pre hornú matricu v 2. operácii
