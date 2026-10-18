---
lang: sk
title: "Laboratórium neizotermického kovania Tee Non"
---

# Laboratórium neizotermického kovania Tee Non

V tomto laboratórnom cvičení nastavíme jednoduchý neizotermický proces typu „Tee“, pri ktorom majú obrobok aj matrice sieťovú štruktúru.

1.1. Vytvorenie nového problému

1.2. Pridanie operácie v programe 3D Forming Express – Kovanie T-kusov

1.3. Proces

1.4. Tepelný výpočet

1.5. Výber počtu objektov

1.6. Obrobok

1.7. Horná matrica

1.8. Spodná matrica

1.9. Polohovanie objektov

1.10. Stránka s kontaktnými údajmi

1.11. Zdvih primárneho lisovacieho nástroja

1.12. Ovládacie prvky na zastavenie

1.13. Ovládacie prvky simulácie

1.14. Vytvorenie databázy

1.15. Spustenie simulácie

1.16. Následné spracovanie

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa okno DEFORM GUI Main, ako je znázornené na obr. 3DTEEL1.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno programu DEFORM GUI

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. 3DTEEL1.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Anglický**“. Názov úlohy zadajte ako „**TeeNonIso**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa okno „Integrated Manufacturing Process“ (pozri obr. 3DTEEL1.3.), kde bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „************TeeNonIso****“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otvorení operácie.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0003.jpg' | relative_url }})

Okno na výber miesta problému

## Pridanie operácie v programe 3D Forming Express – Kovanie T-kusov

Po kliknutí na tlačidlo „Dokončiť“ sa otvorí sprievodca viacerými operáciami, v ktorom môžete nastaviť daný problém. Zo zoznamu operácií v Průzkumníku pridajte operáciu 3**D Forming Express**. Operáciu môžete pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie 3D Forming Express alebo ju môžete pridať aj pretiahnutím do Editoru operácií.

**Zmena názvu operácie**

Zmeňte názov operácie na „**Tee_Forging**“ dvojitým kliknutím na pole „Forming“ v editore operácií, ako je znázornené na obr. 3DTEEL1.4.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0004.jpg' | relative_url }})

Úprava názvu operácie

## Postup

Na stránke **Proces** vyberte typ procesu „Kovanie za tepla“ kliknutím na prepínač **Kovanie za tepla**. V rámci tohto cvičenia budeme simulovať celý diel; ak nezvolíte typ geometrie „Celý diel“, táto možnosť bude predvolene vybraná. Posuvníky „Zložitosť tvaru“ a „Presnosť simulácie“ ovplyvňujú nastavenia siete a počet časových krokov použitých v simulácii. To zase ovplyvňuje dobu behu a úroveň detailov dostupných v simulácii. Pre túto simuláciu nastavte zložitosť tvaru objektu na **Stredná** a presnosť na **Rýchla**, ako je znázornené na obr. 3DTEEL1.5. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0005.jpg' | relative_url }})

Stránka procesu

## Tepelný výpočet

V tejto operácii vypočítame zmenu teploty v obrobku a formách, preto vyberte prepínač **Vypočítať****teplotu****v****obrobku****a****formách** (pozri obr. 3DTEEL1.6.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0006.jpg' | relative_url }})

Stránka „Tepelné výpočty“

## Výber počtu objektov

V tomto laboratórnom cvičení použijeme **1 obrobok a 2 matrice**, použijeme predvolený výber tak, ako je znázornené na obr. 3DTEEL1.7, a klikneme na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0007.jpg' | relative_url }})

Stránka na výber počtu objektov

## Obrobok

Obrobok bude mať počiatočnú teplotu 2250 °F. Zmeňte **teplotu** obrobku na **2150** °F. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (Pozri obr. 3DTEEL1.8.)

**Poznámka**: Na stránke „objekt“ sa nachádza tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_object.._button.jpg' | relative_url }}). Slúži na import kompletných údajov o objekte z iného súboru s údajmi o objektoch.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0008.jpg' | relative_url }})

Stránka objektu

### Import geometrie obrobku

Kliknite na tlačidlo „Načítať geometriu z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})“ na stránke „Geometria“ a načítajte súbor **TeeBillet.stl**.

Skontrolujte geometriu kliknutím na akčný štítok ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Okno „Výsledok kontroly geometrie“ obsahuje popis toho, čo predstavuje správnu geometriu, ako je znázornené na obr. 3DTEEL1.9. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0009.jpg' | relative_url }})

Prejdite na stránku s geometriou

### Vytvorenie siete pre obrobok

Znížte počet prvkov siete na obrobku na približne 14 000. Urobíme to s cieľom dosiahnuť rýchle časy výpočtu počas trénovania. Vyberte prepínač typu **User****defined** a zmeňte hodnotu **T******ar** get number of Elements** na **14000**, ako je znázornené na**** obr. 3DTEEL1.10, a vygenerujte sieť. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0010.jpg' | relative_url }})

Stránka so sieťou obrobkov

### Priradiť materiál k obrobku

V okne „Material“ načítajte materiál **AISI-316[70-2020F(20-1100C)]** z knižnice materiálov DEFORM, z kategórie **Stainless_steel**, pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To je možné vykonať tak, ako je znázornené na obr. 3DTEEL1.11, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Materiál je možné načítať aj zo zoznamu materiálov v prehliadači. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0011.jpg' | relative_url }})

Okno s materiálmi

### Okrajové podmienky obrobku

Na stránke „Okrajové podmienky“ skontrolujte, či je pre obrobok predvolene priradená okrajová podmienka „Výmena tepla s prostredím“; táto podmienka by mala byť priradená k celému povrchu objektu, ako je znázornené na obr. 3DTEEL1.12. Ak nie je predvolene priradená, priraďte ju ručne. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0012.jpg' | relative_url }})

Výmena tepla s okolím – okrajová podmienka

## Horná matrica

Na stránke „Top die“ nastavte teplotu hornej formy na **300** °F a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import geometrie hornej matrice

Kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **TeeTop.stl**. Následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vytvorenie siete pre geometriu hornej matrice

Vytvorte sieť pre hornú matricu pomocou hodnoty nastavení siete typu systému kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obr. 3DTEEL1.13. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0013.jpg' | relative_url }})

Hlavná stránka o sieťovine

### Určiť materiál hornej formy

Načítajte materiál **AISI-H-13** z knižnice materiálov a priraďte ho k hornej matrici, ako je znázornené na obr. 3DTEEL1.14. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

**Poznámka**: Táto sieť sa používa iba na výpočty teploty. Geometria sa naďalej používa na výpočty deformácie.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0014.jpg' | relative_url }})

Hlavná stránka o materiáloch na výlisky

### Priradenie tepelnej výmeny s okrajovou podmienkou prostredia

Na stránke „Okrajové podmienky“ skontrolujte, či je pre hornú matricu predvolene priradená okrajová podmienka „Výmena tepla s prostredím“; táto podmienka by mala byť priradená k celému povrchu objektu, ako je znázornené na obr. 3DTEEL1.15. Ak nie je predvolene priradená, priraďte ju ručne. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0015.jpg' | relative_url }})

Priradená výmena tepla s prostredím BCC pre hornú formu

### Priradiť pohyb hornej kocky

V nastaveniach pohybu vyberte možnosť rýchlosti. Uistite sa, že pohyb prebieha v smere **–Z**, a zadajte **rýchlosť** **10** palcov za sekundu, ako je znázornené na obr. 3DTEEL1.16. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0016.jpg' | relative_url }})

Hlavná stránka o pohybe matrice

## Spodná matrica

Na stránke „Spodná forma“ nastavte teplotu spodnej formy na **300** °F a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import spodnej formy

Kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **TeeBottom.stl**. Následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vytvoriť sieť

Kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vygenerujte sieť pre hodnotu nastavení typu systému. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku materiálov.

### Určiť materiál spodnej matrice

Zo zoznamu materiálov vyberte materiál **AISI-H-13** a priraďte ho k spodnej matrici. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Priradiť výmenu tepla s prostredím BCC

Na stránke „Okrajové podmienky“ skontrolujte, či je pre spodnú formu predvolene priradená okrajová podmienka „Výmena tepla s okolím“; táto podmienka by mala byť priradená k celému povrchu objektu, ako je znázornené na obr. 3DTEEL1.17. Ak nie je predvolene priradená, priraďte ju ručne. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0017.jpg' | relative_url }})

Priradená výmena tepla s prostredím BCC pre spodnú formu

## Umiestňovanie objektov

Kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) sa otvorí okno na umiestnenie objektu; pomocou myši umiestnite polotovar nad dutinu formy pomocou posunu aj otáčania. Následne použite funkciu „drop positioning“, aby sa polotovar usadil v dutine formy (pozri obr. 3DTEEL1.18.), a potom použite funkciu „interference position“ na umiestnenie hornej formy na obrobok. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0018.jpg' | relative_url }})

Stránka o umiestňovaní objektov

## Stránka s kontaktnými údajmi

Ako podmienku trenia vyberte **užívateľsky definované** – „**Kovanie za tepla (s mazáním)**“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}). Program DEFORM automaticky označí uzly, ktoré sú spočiatku v kontakte s lisovacou formou. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

## Zdvih primárneho valca

Budeme kovať na hrúbku 0,250”. Zmerajte aktuálnu vzdialenosť medzi hornou a spodnou matricou (pozri obr. 3DTEEL1.19.), od tejto hodnoty odčítajte 0,250 a túto hodnotu použite ako odhadovaný primárny zdvih matrice.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0019.jpg' | relative_url }})

Hlavná stránka o zdvihu matrice

## Ovládacie prvky na zastavenie

Chceme zastaviť, keď budú matrice od seba vzdialené 0,25 palca. Zaškrtnite políčko **Vzdialenosť medzi objektmi**, zadajte hodnotu **0,25** palca. Vyberte bod na spodnej ploche hornej formy a druhý bod na hornej ploche spodnej formy, ako je znázornené na obr. 3DTEEL1.20. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0020.jpg' | relative_url }})

Stránka ovládacích prvkov zastavenia

## Ovládacie prvky simulácie

Použite predvolené ovládacie prvky simulácie, ako je znázornené na obr. 3DTEEL1.21, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0021.jpg' | relative_url }})

Stránka s ovládacími prvkami simulácie

## Vytvoriť databázu

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení úlohy niečo nechýba. Počas kontroly

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), aby ste spustili simuláciu.

## Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 3DTEEL1.22. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“ (od kroku -1), potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) sa spustí simulácia.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0022.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať na karte „Simulation Message“ a v časti „Simulation Graphics“ v oblasti zobrazenia „Graphics“ v režime simulácie. Pokiaľ je na karte „Simulation Message“ zaškrtnutá voľba „![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }})“ (čo je predvolené nastavenie), súbor správ sa bude automaticky aktualizovať.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia práve nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Keď simulácia prebehne bez problémov, skontrolujte správy v súbore správ; po dokončení operácie sa zobrazia správy typu: „VZDIALENOSŤ MEDZI DVOMA OBJEKTAMI (2 3): 0,25000000 DOSIAHLA ŠPECIFIKOVANÝ LIMIT 0,25000000“

## Následné spracovanie

Po dokončení simulácie prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) na účely následného spracovania. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) v prehliadači krokov si môžete zobraziť všetky uložené kroky, ako je znázornené na obr. 3DTEEL1.23.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0023.jpg' | relative_url }})

Režim príspevku

Nastavte priehľadnosť výsekových foriem, zapnite kontaktné uzly zobrazenia ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}), spustite simuláciu a sledujte vzor vyplnenia, ako je znázornené na obr. 3DTEEL1.24.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0024.jpg' | relative_url }})

Režim zobrazenia, v ktorom sa objekty zobrazujú v režime priehľadnosti

**Stavová premenná** :

Zaznačte premenné teploty a deformácie obrobku a sledujte grafy tak, ako je znázornené na obr. 3DTEEL1.25 a obr. 3DTEEL1.26.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0025.jpg' | relative_url }})

Graf premennej teploty

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0026.jpg' | relative_url }})

Graf závislosti medznej deformácie od premennej
