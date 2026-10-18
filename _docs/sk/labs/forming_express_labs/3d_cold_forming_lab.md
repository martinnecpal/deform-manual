---
lang: sk
title: "Laboratórium 3D tvárnenia za studena"
---

# Laboratórium 3D tvárnenia za studena

V tomto laboratórnom cvičení nastavíme jednoduchú operáciu tvárnenia skrutiek v rámci operácie „MO 3D forming express“. Táto operácia tvárnenia pozostáva z 3 fáz:

  1. Operácia vytláčania: V tejto operácii vytláčame obrobok.

  2. Operácia kužeľového vyťahovania: Pri tejto operácii vyťahujeme hornú časť obrobku.

  3. Obrábanie s šesťhrannou hlavou: Pri tomto procese dodávame hornej ploche obrobku šesťhranný tvar.

Po dokončení operácie tvárnenia vykonáme analýzu napätí v lisovacej forme, aby sme zistili napätia v hornej lisovacej forme.

Operácia 1: Operácia vytláčania

Operácia 2: Operácia s kužeľovým výfukom

Operácia 3: Operácia s šesťhrannou hlavou

Operácia 4: Operácia „Die Stress“

## Operácia vytláčania

### Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené na obr. 3DCFL1.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno programu DEFORM GUI

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. 3DCFL1.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Zadajte názov úlohy ako „**3D_******Bo** lt **“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt (pozri obr. 3DCFL1.3.), v tomto bode bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**3D_******Bolt** **“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0003.jpg' | relative_url }})

Sprievodca MO – Nový projekt

### Pridať operácie

Po kliknutí na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) sa otvorí sprievodca viacerými operáciami, v ktorom môžete nastaviť úlohu. V tomto cvičení ukážeme, ako nastaviť všetky 3 operácie v dávkovom režime. Pridajte tri operácie 3D Forming Express zo zoznamu operácií v Průzkumníku. Operáciu môžete pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie 3D Forming Express alebo ju môžete pridať aj pretiahnutím do Editoru operácií.

**Zmena názvu operácie:**

Zmeňte názov operácie na „**Extrude**“ dvojitým kliknutím na pole Forming v editore operácií, ako je znázornené na obr. 3DCFL1.4.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0004.jpg' | relative_url }})

Úprava názvu operácie

### Nastavenia definovania procesu

Na stránke „Proces“ vyberte typ procesu „Tvarovanie za studena“ a typ geometrie „Celý diel“.

Posuvníky pre zložitosť tvaru a presnosť simulácie ovplyvňujú nastavenia siete a počet časových krokov použitých v simulácii. To zase ovplyvňuje dĺžku behu a úroveň detailov dostupných v simulácii.

V tejto simulácii použijeme ako zložitosť nastavenia „Simple“ a „Moderate“ a nastavíme posuvníky tak, ako je znázornené na obr. 3DCFL1.5 nižšie, a klikneme na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0005.jpg' | relative_url }})

Stránka procesu

### Pridávanie objektov

V tejto operácii použijeme **1 obrobok + 2 matrice**, ako je znázornené na obr. 3DCFL1.6., kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0006.jpg' | relative_url }})

Stránka na výber počtu objektov

### Definícia obrobku

Použite predvolený názov objektu „Workpiece“ a predvolenú teplotu objektu, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

**Poznámka**: Na stránke „Objekt“ sa nachádza tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_object.._button.jpg' | relative_url }}). Slúži na import kompletných údajov o objekte z iného súboru DEFORM; v tejto chvíli ho však nebudeme používať.

#### Import geometrie obrobku

Na stránke „Geometria“ kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **bolt-cutoff.STL**, ako je znázornené na obr. 3DCFL1.7.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0007.jpg' | relative_url }})

Stránka importu objektu

Kliknite na geometriu ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Popis toho, čo predstavuje povolenú geometriu, je uvedený v okne GEOMETRY CHECKING RESULT, ako je znázornené na obr. 3DCFL1.8. Geometria odrezaného skrutku je povolená. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0008.jpg' | relative_url }})

Stránka na kontrolu geometrie

#### Sieť obrobku

Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_preview_mesh_button2.jpg' | relative_url }}) vygenerujte povrchovú sieť s predvoleným počtom prvkov. Pri aktuálnych nastaveniach v časti „Zložitosť tvaru objektov“ je predvolený počet priestorových prvkov 52 000, ako je znázornené na obr. 3DCFL1.9.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0009.jpg' | relative_url }})

Okno s mriežkou v systémovom režime

Prejdite do časti „Objekty – Zložitosť tvaru“ a posuňte posuvník „Presnosť“ z polohy „Stredná“ do polohy „Rýchla“. Vráťte sa na obrazovku „Sieť“ a znovu vytvorte sieť pomocou ![]({{ '/assets/icons/pre_icons/mo_preview_mesh_button2.jpg' | relative_url }}). Tentoraz sa predvolený počet prvkov znížil na 16 000. Podobné výsledky sa dosiahnu aj pri zmene polohy posuvníka „Presnosť“.

#### Použitie pokročilého vytvárania sietí

Vyberte voľbu **User defined**, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_advanced_button.jpg' | relative_url }}), vyberte možnosť „Min Element Size“ a zadajte veľkosť prvku 0,02” a použite pomer veľkosti 1, ako je znázornené na obr. 3DCFL1.10. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_surface_mesh_button.jpg' | relative_url }}). Výsledná povrchová sieť bude rovnomerná s prvkami s veľkosťou približne .020”.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0010.jpg' | relative_url }})

Pokročilé nastavenia užívateľsky definovanej siete

#### Vytvorte sieť na použitie v simuláciách

Konečná sieť, ktorú vygenerujeme, sa použije v nasledujúcich simuláciách. Vráťte sa do časti „Objekty – Zložitosť tvaru“ a nastavte posuvníky späť na „Jednoduchá zložitosť“ a „Stredná presnosť“. Kliknite na položku „Mesh“ pod položkou „Workpiece“ v stromovej štruktúre projektu a potom vygenerujte sieť kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) (![]({{ '/assets/icons/pre_icons/mo_preview_mesh_button2.jpg' | relative_url }}) vygeneruje iba povrchovú sieť, zatiaľ čo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vytvorí najskôr povrchovú sieť a potom objemovú sieť).

#### Zadanie materiálu obrobku

V okne „Material“ načítajte materiál **AISI-1010,COLD[70F(20C)]** z knižnice materiálov DEFORM v kategórii **Steel** pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To je možné vykonať tak, ako je znázornené na obr. 3DCFL1.11, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Materiál je možné načítať aj zo zoznamu materiálov v prehliadači, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka Top Die.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0011.jpg' | relative_url }})

Okno „Knižnica materiálov“

### Definícia pojmu „Top Die“

Na stránke „Top Die“ zmeňte názov objektu na **Punch** a použite predvolenú teplotu objektu (68 °F), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Importovať geometriu hornej matrice

Naimportujte súbor **bolt-punch1.STL** pomocou tlačidla „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})), ako je znázornené na obr. 3DCFL1.12, a následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0012.jpg' | relative_url }})

Import geometrie hornej matrice

#### Priradiť pohyb pre úder

V možnostiach pohybu vyberte rýchlosť. Uistite sa, že pohyb prebieha v smere **–Y**, zadajte rýchlosť **10** palcov za sekundu, ako je znázornené na obr. 3DCFL1.13. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0013.jpg' | relative_url }})

Stránka o pohybe úderu

### Definícia spodnej matrice

Na stránke „Spodná forma“ použite predvolenú teplotu objektu (68 °F) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Import geometrie spodnej matrice

Kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **bolt-die1.STL**. Následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Umiestňovanie objektov

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) sa otvorí stránka na nastavenie polohy objektov. Vyberte ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }})positioning a ako objekt **polohovania** vyberte Obrobok a ako referenciu **Matrica**. Ako je znázornené na obr. 3DCFL1.14, mal by sa použiť smer priblíženia **–Y**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Podobne umiestnite razník tak, aby sa dotýkal obrobku, pomocou metódy ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) so smerom priblíženia **–Y**. Obrobok je umiestnený na matrici a razník je umiestnený na obrobku tak, aby sa navzájom dotýkali. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0014.jpg' | relative_url }})

Okno na umiestňovanie objektov

### Definovanie kontaktných podmienok

V časti „Kontakt“ stromovej štruktúry bude štandardne priradený systémom definovaný predvolený koeficient trenia 0,08, čo zodpovedá tvárneniu za studena s použitím karbidových matíc (pozri obr. 3DCFL1.15.). Výberom tlačidla **Užívateľsky definované** môže užívateľ v prípade potreby pomocou rozbaľovacieho menu definovať aj iné hodnoty trenia. Program DEFORM automaticky určí pre tento model vhodnú toleranciu kontaktu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}). Mali by ste vidieť kontakty medzi obrobkom a ostatnými objektmi. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0015.jpg' | relative_url }})

Okno na definovanie vzťahov medzi kontaktmi

### Nastaviť primárny zdvih matrice

V tejto úlohe budeme vyťahovať na vzdialenosť 0,35”, ako je znázornené na obr. 3DCFL1.16. Do poľa „Total primary die travel“ (Celkový posun primárneho lisovacieho nástroja) preto zadajte hodnotu **0,35**" a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0016.jpg' | relative_url }})

Okno s primárnym nastavením zdvihu matrice

### Priradiť ovládacie prvky zastavenia

Chceme zastaviť simuláciu, keď sa razník posunie o 0,35”. Kliknite v stromovej štruktúre na položku Ovládacie prvky zastavenia a **zaškrtnite** možnosť **Zdvih matrice presahuje** zadanú hodnotu. Hodnota **0,35** ” definovaná v celkovom primárnom zdvihu matrice sa automaticky vloží do tohto poľa, ako je znázornené na obr. 3DCFL1.17. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0017.jpg' | relative_url }})

Okno s ovládacími prvkami na zastavenie

### Prehľad ovládacích prvkov simulácie

Počet simulačných krokov a veľkosť kroku sa nastavujú pomocou posuvníka „Zložitosť tvaru objektu“. Ak chcete zmeniť predvolené hodnoty, môžete tak urobiť výberom prepínača „Užívateľský typ“ a definovaním kroku. V tomto cvičení ponecháme predvolené hodnoty.

### Vytvoriť databázu

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení úlohy niečo nechýba. Počas kontroly,

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na kartu ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) a prejdite k ďalšej operácii.

## Prevádzka s kužeľovým dúchadlom

V rámci tejto operácie dovážame nové nástroje a meníme geometriu foriem.

**Zmena názvu operácie:**

V editore operácií zmeňte názov operácie na „**Cone Blow**“, ako je znázornené na obr. 3DCFL1.18.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0018.jpg' | relative_url }})

Zmena názvu operácie v editore operácií

### Nastavenie procesu pre operáciu vyfukovania kužeľa

Nechajte nastavenie „Zložitosť“ na hodnote „Jednoduché“ a nastavte „Presnosť“ na značku medzi hodnotami „Rýchla“ a „Stredná“, ako je znázornené na obr. 3DCFL1.19. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0019.jpg' | relative_url }})

Stránka procesu

### Pridávanie objektov

Táto operácia bude vyžadovať ešte jeden objekt, preto zmeňte nastavenie na **1 obrobok + 3 matrice**, ako je znázornené na obr. 3DCFL1.20, a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top die“.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0020.jpg' | relative_url }})

Stránka na výber počtu objektov

### Definícia pojmu „Top“

Na stránke Objekt vyberte prepínač **Definovať**, ako je znázornené na obr. 3DCFL1.21, a zmeňte názov objektu na **Punch**, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0021.jpg' | relative_url }})

Hlavná stránka Die

#### Importovať geometriu dierovacieho nástroja

Kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **bolt-punch2.STL**. Následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Definovanie pohybu úderu 

Použite údaje o pohybe z predchádzajúcej operácie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Definícia spodnej matrice

Na stránke „Objekt“ vyberte voľbu **Definovať** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Import geometrie spodnej matrice

Kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a **naimportujte súbor bolt-die2.STL**. Následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Definícia ejektora

Zmeňte názov objektu 4 na **Ejector** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0022.jpg' | relative_url }})

Stránka vyhadzovača

#### Import geometrie vyhadzovacej matrice

Kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **bolt-ejector2.STL**. Následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Plánované polohovanie“.

### Plánované umiestnenie

Pomocou polohovania s interferenciou najprv umiestnime obrobok k forme (smer priblíženia -Y) a potom razník k obrobku. Na stránke „Plánované polohovanie“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a vyberte prepínač ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte objekt polohovania na **obrobok** a referenčný bod na **spodnú** časť formy. Zmeňte smer priblíženia na **-Y** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Podobne pridajte naplánované polohovanie s ohľadom na kolízie pre razník a obrobok (smer priblíženia -Y pre razník), ako je znázornené na obr. 3DCFL1.23. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku Primárny zdvih formy.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0023.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

### Zdvih primárneho valca

Musíme nastaviť približnú vzdialenosť, o ktorú sa razník posunie počas tejto operácie. Vzdialenosť medzi maticami je pri tejto operácii približne 0,8”. Chceme, aby bol na konci operácie vzdialenosť medzi razníkom a matricou 0,25”, preto zmeňte túto hodnotu na 0,6”, ako je znázornené na obr. 3DCFL1.24. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0024.jpg' | relative_url }})

Základný zdvih matrice

Chceme tvarovať diel tak, aby sa razník a matrica nachádzali vo vzdialenosti do 0,25” od seba. Na obrazovke Ovládacie prvky zastavenia zaškrtnite políčko vedľa položky **Vzdialenosť medzi objektmi**, aby sa táto možnosť aktivovala. Myšou kliknite na bod na spodnej strane razníka a potom kliknite na bod na hornej strane matrice. Na obrazovke by sa mala zobraziť šípka medzi týmito dvoma bodmi. Nastavte hodnotu tejto vzdialenosti na **0,25** ” v smere **Y**, ako je znázornené na obr. 3DCFL1.25. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0025.jpg' | relative_url }})

Okno s ovládacími prvkami na zastavenie

### Prehľad ovládacích prvkov simulácie

Počet simulačných krokov a veľkosť kroku sa nastavujú pomocou posuvníka „Object Shape Complexity“ (Zložitosť tvaru objektu). Ak chcete zmeniť predvolené hodnoty, môžete tak urobiť výberom prepínača typu **user** a definovaním kroku. V tomto cvičení ponecháme predvolené hodnoty. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vytvoriť databázu

Pozrite si stav na stránke „Generate DB“; ak sa zobrazí chyba zadávania údajov, skontrolujte, či nechýbajú nejaké údaje, a doplňte ich. V rámci tejto série cvičení sa zobrazí správa: „Vytvorenie databázy nie je pre túto operáciu potrebné. Uskutoční sa počas behu programu.“ Kliknutím na kartu ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k ďalšej operácii.

## Práca s imbusovým kľúčom

**Zmena názvu operácie:**

V editore operácií zmeňte názov operácie na „**Hex Head**“.

### Definícia nastavení procesu

Zmeňte úroveň zložitosti na značku medzi „Jednoduchá“ a „Stredná“ a zvýšte presnosť na „Stredná“, ako je znázornené na obr. 3DCFL1.26. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top die“.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0026.jpg' | relative_url }})

Okno nastavení procesu

### Definícia pojmu „Top“

Na stránke Objekt vyberte prepínač **Definovať**, ako je znázornené na obr. 3DCFL1.27, a zmeňte názov objektu na **Punch**, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0027.jpg' | relative_url }})

Okno „Všeobecná definícia hornej matrice“

#### Importovať geometriu dierovacieho nástroja

Kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **bolt-punch3.STL**. Následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Definovanie pohybu úderu

Použite údaje o pohybe z predchádzajúcej operácie a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Plánované polohovanie“.

### Plánované umiestnenie

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a vyberte prepínač ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte polohovací objekt na **Punch** a referenčný bod na **Workpiece** a smer priblíženia na **-Y**, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) (pozri obr. 3DCFL1.28.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Primary die stroke.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0028.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

### Definícia primárneho zdvihu matrice

Na stránke „Primárny posuv matrice“ nastavte hodnotu primárneho posuvu matrice na **0,4466**, ako je znázornené na obr. 3DCFL1.29. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0029.jpg' | relative_url }})

Okno pohybu primárneho lisovacieho nástroja

### Definícia ovládacích prvkov na zastavenie

Chceme tvarovať diel tak, aby sa razník a matrica nachádzali vo vzdialenosti do 0,03” od seba. Na obrazovke „Stop Controls“ kliknite na „**Vzdialenosť****medzi objektmi dosiahne** “, aby ste túto možnosť aktivovali, a nastavte ju na **0,03** ” v smere **Y**. Kliknite na bod na spodnej strane razníka a potom na bod na hornej strane matrice, ako je znázornené na obr. 3DCFL1.30. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0030.jpg' | relative_url }})

Okno s ovládacími prvkami na zastavenie

### Prehľad ovládacích prvkov simulácie

Počet simulačných krokov a veľkosť kroku sa nastavujú pomocou posuvníka „Object Shape Complexity“ (Zložitosť tvaru objektu). V tomto cvičení použijeme predvolené hodnoty. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vytvoriť databázu

Pozrite si stav na stránke „Generate DB“; ak sa zobrazí chyba zadávania údajov, skontrolujte, či nechýbajú nejaké údaje, a doplňte ich. V rámci tejto série cvičení sa zobrazí správa: „Vytvorenie databázy nie je pre túto operáciu potrebné. Uskutoční sa počas behu programu.“

Uložte projekt a kliknite na režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), aby ste spustili simuláciu.

### Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 3DCFL1.31. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0031.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať na karte „Simulation Message“ a v časti „Simulation Graphics“ v oblasti zobrazenia „Graphics“ v režime simulácie. Pokiaľ je na karte „Simulation Message“ zaškrtnutá možnosť „![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }})“ (čo je predvolené nastavenie), súbor správ sa bude automaticky aktualizovať.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia práve nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Keď sa simulácia bez problémov dokončí, skontrolujte správy v súbore LOG; po dokončení všetkých operácií sa v správach v súbore LOG zobrazí text: „MULTIPLE OPERATION COMPLETED“. (Pozri obr. 3DCFL1.32.)

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0032.jpg' | relative_url }})

Súbor protokolu

### Následné spracovanie

Po dokončení simulácie prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). V prehliadači krokov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}), aby ste si zobraili všetky uložené kroky.

#### Premenné stavu:

V zozname stavových premenných kliknite na ikonu **Efektívne****deformácie**, aby ste znázornili veľkosť deformácie, ktorá pôsobila na obrobok. Ak chcete zmeniť nastavenia grafu, môžete kliknúť na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) Nastavenie. Na tejto obrazovke môžete zobraziť rôzne druhy kontúr (čiarkované, tieňované alebo plné) a tiež zmeniť rozsah premennej, ktorý sa zobrazuje na kontúrovom pruhu (pozri obr. 3DCFL1.33.). Pomocou možnosti Nastavenia si môžete rozsah kontúrového pruhu definovať sami. Neváhajte experimentovať so zobrazením rôznych stavových premenných a možností grafu.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0033.jpg' | relative_url }})

Graf stavovej premennej pri deformácii

#### Krájanie:

Na rozrezanie obrobku a foriem použite nástroj na rezanie ![]({{ '/assets/icons/post_icons/mo_slicing_option.jpg' | relative_url }}). Na rozrezanej ploche je možné zobraziť stavové premenné a pridaním reznej roviny pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) môžete použiť viacero rezacích rovín. (Pozri obr. 3DCFL1.34.)

Posuvník v okne SLICING vám umožňuje dynamicky posúvať rovinu rezu.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0034.jpg' | relative_url }})

Okno na krájanie

#### Sledovanie bodov:

Zo zoznamu krokov vyberte krok –1 a potom zo zoznamu Nástroje vyberte ikonu Sledovanie bodov ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }}). Vyberte niekoľko bodov na objekte a sledujte ich polohu. Ak sa naďalej zobrazuje stavová premenná, napríklad efektívne deformácie, hodnoty tejto premennej sa v týchto bodoch znázornia graficky v závislosti od času, ako je znázornené na obr. 3DCFL1.3.35.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0035.jpg' | relative_url }})

Graf znázorňujúci sledovanie bodov

#### Zdvih zaťaženia:

Veľkosť zaťaženia potrebného na deformáciu objektu je dôležitý výsledok, ktorý možno získať zo simulácie. Kliknite na ikonu ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}). Keď sa zobrazí okno GRAPH, v zozname objektov vyberte iba položku Punch, os X nastavte na Stroke a os Y nastavte na Y Load a pri výbere operácie vyberte operáciu 3. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) a v okne DISPLAY sa zobrazí krivka zaťaženia v závislosti od zdvihu, ako je znázornené na obr. 3DCFL1.36.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0036.jpg' | relative_url }})

Graf závislosti zdvihu od zaťaženia razníka v operácii 3

## Operácia „Die Stress“

###  Pridať operáciu s napätím v matrici

Po dokončení následného spracovania prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}).

Pridajte operáciu „Die stress 3D“ zo zoznamu operácií v programe Explorer a pridanú operáciu „Die stress“ otvorte dvojitým kliknutím na túto operáciu v zozname operácií.

### Vybrať objekty

V súčasnosti sa zaujímame iba o analýzu napätia v razníku pri operácii s šesťhrannou hlavou. Zoznamu preto odstráňte spodnú matricu (object3) a vyhadzovač (object4) kliknutím na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) delete“. Kliknite na „![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})“. (Pozri obr. 3DCFL1.37.)

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0037.jpg' | relative_url }})

Okno „Stress Objects“

V predvolenom nastavení bude typ objektu obrobku „Načítané z databázy“; tento objekt tam zostane až do vytvorenia databázy, pričom pri jej generovaní bude odstránený. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Definícia pojmu „Top Die“

V predvolenom nastavení bude pre hornú formu vybrané rádio tlačidlo „Elastic“; potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Mesh“.

**Hlavná stránka o sieťovinách:**

Nastavte počet prvkov na **50000**, ako je znázornené na obr. 3DCFL1.38. Vygenerujte sieť a potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s materiálmi.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0038.jpg' | relative_url }})

Okno so sieťkou

**Priradiť materiál pre hornú matricu:**

Naimportujte materiál na výrobu foriem z knižnice materiálov. Zo zoznamu vyberte **AISI-H-13**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

**Nastavenie okrajovej podmienky pre hornú matricu:**

Ďalej musíme na razník aplikovať okrajové podmienky, aby neodletel do vesmíru, keď naň pôsobia zaťaženia vznikajúce pri tvárnení.

Na obrazovke „Deformation BCC“ vyberte rýchlosti „All“, ktoré majú byť fixované, a potom vyberte zadnú plochu razníka (možno bude potrebné razník otočiť).

Po výbere tejto plochy by mali byť všetky uzly na ploche zvýraznené. Tieto uzly sú momentálne vybrané, ale okrajová podmienka ešte nebola aplikovaná. Kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}), aby ste na danú plochu aplikovali okrajovú podmienku. (Pozri obr. 3DCFL1.39.) Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím prejdete na stránku Vynútiť interpoláciu.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0040.jpg' | relative_url }})

Pridanie okrajovej podmienky rýchlosti

**Vynútená interpolácia:**

Po vytvorení siete je potrebné interpolovať formovacie sily pôsobiace na obrobok na razník. Kliknite na **Interpolate Force**. Po interpolácii síl sa zobrazí správa porovnávajúca sily pôsobiace na obrobok s novými silami pôsobiacimi na razník, ako je znázornené na obr. 3DCFL1.40. Tieto sily by mali byť relatívne blízko seba (zvyčajne v rozmedzí približne 5 %). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Generate DB.

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0039.jpg' | relative_url }})

Vynútiť okno interpolácie

### Vytvoriť databázu

Skontrolujte údaje a vytvorte databázu. Po vytvorení databázy prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

### Spustenie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spustení) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) sa spustí simulácia. 

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

### Postprocesor

Hlavnými veličinami, na ktoré je potrebné sa zamerať pri simulácii napätia v tvárnici, sú efektívne napätie a maximálne hlavné napätie.

Efektívne napätie sa používa na zistenie, či v niektorej časti lisovacej formy došlo k plastickej deformácii. Ak má nejaká oblasť lisovacej formy efektívne napätie blízke alebo presahujúce medzu tečnosti materiálu lisovacej formy, v tejto oblasti hrozí riziko plastickej deformácie. (Pozri obr. 3DCFL1.41.)

Maximálne hlavné napätie sa používa na zistenie, ktoré oblasti matrice sú v stave stlačenia a ktoré v stave ťahu. Maximálne hlavné napätie je mimoriadne dôležité pri určovaní, či na matrici dôjde k prasknutiu v dôsledku únavy materiálu. Ak chcete zobraziť maximálne hlavné napätie, kliknite na tlačidlo „Nastaviť“ pre stavovú premennú ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) a potom zo zoznamu vyberte položku Napätie – Maximálne hlavné. (Pozri obr. 3DCFL1.42.)

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0041.jpg' | relative_url }})

Dej s dôrazom na napätie

![]({{ '/assets/images/labs/forming_express_labs/3d_cold_forming_lab/image0042.jpg' | relative_url }})

Graf maximálneho hlavného napätia
