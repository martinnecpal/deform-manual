---
lang: sk
title: "Laboratórium 2D tvárnenia za studena 1"
---

# Laboratórium 2D tvárnenia za studena

V tomto laboratórnom cvičení nastavíme jednoduchú operáciu tvárnenia skrutiek v rámci operácie „MO 2D forming express“. Táto operácia tvárnenia pozostáva z 3 fáz:

  1. Operácia vytláčania

  2. Prevádzka s kužeľovým dúchadlom

  3. Práca s imbusovou hlavou

Po dokončení operácie tvárnenia vykonávame analýzu napätí v lisovacej forme, aby sme zistili napätia v hornej lisovacej forme.

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0008.jpg' | relative_url }})

Operácia 1: Operácia vytláčania

Operácia 2: Operácia s kužeľovým výfukom

Operácia 3: Operácia s šesťhrannou hlavou

Operácia 4: Operácia na odstránenie napätia

## Operácia vytláčania

### Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené na obr. 2DCFL1.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno grafického rozhrania QT4

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. 2DCFL1.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Názov úlohy zadajte ako „******Bolt**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), čím otvoríte nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Stránka „Nový problém“

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt, v ktorom bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**Bolt**“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

### Pridať operácie

V tomto cvičení ukážeme, ako nastaviť všetky tri operácie v dávkovom režime. Pridajte tri operácie „2D Forming express“ zo zoznamu operácií v Průzkumníku. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie „2D Forming express“ alebo ju môžete pridať aj pretiahnutím do oblasti Editoru operácií.

### Zmena názvu operácie:

Zmeňte názov operácie na „**Extrude**“ dvojitým kliknutím na pole „Forming“ v editore operácií, ako je znázornené na obr. 2DCFL1.3.

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0001.jpg' | relative_url }})

Úprava názvu operácie

### Nastavenia definovania procesu

Na stránke „Proces“ vyberte ako **Typ procesu** možnosť **Tvarovanie za studena** a ako **Typ geometrie** vyberte možnosť **2D osovo symetrické**.

Posuvníky pre zložitosť tvaru a presnosť simulácie ovplyvňujú nastavenia siete a počet časových krokov použitých v simulácii. To zase ovplyvňuje dĺžku behu a úroveň detailov dostupnú v simulácii.

Pre túto simuláciu použijeme predvolené nastavenia „Stredná zložitosť“ a „Stredná presnosť“ a nastavíme posuvníky tak, ako je znázornené na obr. 2DCFL1.4. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0002.jpg' | relative_url }})

Stránka procesu

###  Pridávanie objektov

V tejto operácii by sme mali mať **1 obrobok + 3 matrice**, ako je znázornené na obr. 2DCFL1.5. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0003.jpg' | relative_url }})

Stránka na výber počtu objektov

### Definícia obrobku

Použite predvolený názov objektu **Obrobok** a predvolenú teplotu objektu **Predvolená** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

Poznámka: Na stránke „Objekt“ sa nachádza tlačidlo „Importovať objekt“. Slúži na import kompletných údajov o objekte z iného súboru DEFORM, čo však v tomto momente nie je to, čo chceme urobiť.

### Vytvoriť geometriu

Na stránke „Geometria“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Definujte **C****valec** s **polomerom** **0,135”** a **výškou** **1,29”**, ako je znázornené na obr. 2DCFL1.6. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Na obrazovke by sa mala zobraziť geometria výrezu s polomerom 0,135”.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a potom v rozbalovacom okne kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}), aby ste skontrolovali, či je geometria v poriadku. V stavovom okne sa zobrazí správa, že geometria je správna. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby sa otvorilo okno „Skontrolujte a opravte geometriu“, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Sieť“.

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0004.jpg' | relative_url }})

Definovanie geometrie

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0005.jpg' | relative_url }})

Stránka o geometrii

### Sieť obrobku

Nastavenia, ktoré sme zadali v programe [Objects Shape Complexity]({{ '/docs/sk/operation_templates/34_forming_express/34_1_2d_forming_express_setup/' | relative_url }}#Shape_Complexity_and_Accuracy), určili počet prvkov a počet časových krokov, ktoré sa mali použiť v simulácii.

Aby sa toto laboratórne cvičenie spustilo rýchlo, zmeňte počet prvkov na 1000 tak, že vyberiete prepínač „user defined“ a kliknete na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). V okne „Display“ by sa mala na obrobku zobraziť sieť s približne 1000 prvkami.

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0006.jpg' | relative_url }})

Stránka s mriežkou

### Materiál obrobku

V okne „Material“ načítajte materiál **AISI-1010,COLD[70F(20C)** z knižnice materiálov DEFORM v kategórii **Steel** pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To je možné vykonať tak, ako je znázornené na obr. 2DCFL1.9, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Materiál je možné načítať aj zo zoznamu materiálov v prehliadači. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Top Die“.

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0007.jpg' | relative_url }})

Okno „Knižnica materiálov“

### Definícia pojmu „Top Die“

Na stránke „Top Die“ zmeňte názov hornej matrice na **Punch** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import geometrie dierovacieho nástroja:

Naimportujte súbor **bolt-punch1.IGS** pomocou tlačidla „Načítať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), ako je znázornené na obr. 2DCFL1.10, a následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0009.jpg' | relative_url }})

Import geometrie výseku

### Priradiť pohyb pre úder

V nastaveniach pohybu vyberte **S******p** **rýchlosť**. Uistite sa, že pohyb prebieha v smere **–Y**, zadajte rýchlosť **10** palcov za sekundu, ako je znázornené na obr. 2DCFL1.11. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0010.jpg' | relative_url }})

Stránka o pohybe úderu

### Definícia spodnej matrice

Na stránke „Spodná forma“ zmeňte názov spodnej formy na **Forma** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import geometrie lisovacej formy

Kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **bolt-die1.IGS**. Následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vyhadzovač

Na stránke objektu 4 zmeňte názov objektu 4 na **Ejector**. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import geometrie vyhadzovača

Kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **bolt-ejector1.IGS**. Následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Umiestňovanie objektov

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) sa otvorí stránka na polohovanie objektov. Vyberte možnosť **Polohovanie podľa kolízie** a ako **Polohovaný objekt** zvoľte **Obrobok** a ako **Referenciu** zvoľte **Formu**. Mali by ste použiť **smer** priblíženia **–Y**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Obrobok sa posunul smerom nadol, až kým nedošlo k kontaktu s maticou. Zväčšite pravý dolný roh obrobku a uvidíte, že hodnota kolízie 0,0001 bola pre tieto geometrie trochu príliš veľká a medzi objektmi došlo k príliš veľkému prekrývaniu. Pridajte k hodnote interferencie ďalších päť núl, aby bola 0,000000001, a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Mali by ste vidieť, že obrobok je teraz umiestnený v matrici so správnou mierou prekrývania. Umiestnite **razník** tak, aby sa dotýkal **obrobku**. Opäť použite smer priblíženia **–Y**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili okno „Positioning object“, a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). 

### Definovanie kontaktných podmienok

V časti „Kontakt“ stromovej štruktúry je štandardne priradený systémom definovaný predvolený koeficient trenia 0,08, čo zodpovedá tvárneniu za studena s použitím karbidových matíc. Výberom prepínača „Definované používateľom“ môže používateľ v prípade potreby definovať aj iné hodnoty trenia pomocou roletového menu (pozri obr. 2DCFL1.12.). Program DEFORM automaticky určí vhodnú toleranciu kontaktu pre tento model. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}). Mal by sa zobraziť kontakt medzi obrobkom a ostatnými objektmi, s ktorými prichádza do styku. V tomto cvičení použijeme predvolený typ „**Definované systémom**“, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0011.jpg' | relative_url }})

Okno na definovanie vzťahov medzi kontaktmi

### Nastaviť primárny zdvih matrice

Hlavný zdvih matrice je odhad vzdialenosti, ktorú prejde razník počas tvárnenia.

V tejto úlohe budeme vyťahovať na vzdialenosť **0,80** ”, preto zadajte túto hodnotu do poľa „Total primary die travel“ (Celkový zdvih primárneho lisovacieho nástroja) a zaškrtnite políčko „Exact amount“ (Presná hodnota), ako je znázornené na obr. 2DCFL1.13.)

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0012.jpg' | relative_url }})

Okno s primárnym nastavením zdvihu matrice

### Priradiť ovládacie prvky zastavenia

Chceme simuláciu zastaviť, keď sa razník posunie o 0,80”. Kliknite v stromovej štruktúre na položku „Stopping Controls“ a zaškrtnite možnosť **Max****die stroke**. Do poľa zadajte hodnotu **0,80** ” tak, ako je znázornené na obr. 2DCFL1.14. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0013.jpg' | relative_url }})

Okno s ovládacími prvkami na zastavenie

### Prehľad ovládacích prvkov simulácie

Počet simulačných krokov a veľkosť kroku sa nastavujú pomocou posuvníka „Object Shape Complexity“ (Zložitosť tvaru objektu). Ak chcete zmeniť predvolené hodnoty, môžete tak urobiť výberom prepínača „user type“ (užívateľský typ) a definovaním kroku. V tomto cvičení ponecháme predvolené hodnoty. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vytvoriť databázu

Na stránke „Generate DB“. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) spustíte kontrolu programu, či v nastavení úlohy niečo nechýba. Počas kontroly:

Správy v červenej farbe označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) a prejdite k ďalšej operácii.

## Prevádzka s kužeľovým výfukom

V rámci tejto operácie zavádzame nové nástroje zmenou geometrie foriem.

### Zmena názvu operácie:

V editore operácií zmeňte názov operácie 2 na „**Cone Blow**“, ako je znázornené na obr. 2DCFL1.15.

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0014.jpg' | relative_url }})

Zmena názvu operácie v editore operácií

### Nastavenie procesu pre operáciu vyfukovania kužeľa

Nechajte nastavenie **Zložitosť** na hodnote **Jednoduché** a zmeňte nastavenie **Presnosť** na **Rýchle**, ako je znázornené na obr. 2DCFL1.16. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0015.jpg' | relative_url }})

Stránka procesu

### Pridávanie objektov

Táto operácia nevyžaduje žiadny nový objekt, takže nastavenie 1 obrobok + 3 matrice nezmeníme; kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Horná matrica“.

### Vysvetlenie pojmu „punch“

Na stránke „Objekt“ vyberte voľbu **Definovať** typ objektu, ako je znázornené na obr. 2DCFL1.17., a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0016.jpg' | relative_url }})

Stránka s definíciou pojmu „punch“

### Import geometrie dierovacieho nástroja

Kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **bolt-punch2.IGS**. Následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Definícia pohybu úderu 

Použite údaje o pohybe hornej matrice z predchádzajúcej operácie a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). 

### Definícia

Na stránke Objekt vyberte voľbu **Definovať** typ objektu a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import geometrie formy

Kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **bolt-die2.IGS**. Následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Plánované polohovanie“.

### Plánované umiestnenie

Pomocou metódy polohovania na základe interferencie najprv polohujeme obrobok k forme (smer priblíženia -Y) a potom razník k obrobku. Na stránke „Plánované polohovanie“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a vyberte prepínač ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte **Objekt polohovania** na **Obrobok** a **Referenciu** na **Formu**. Zmeňte smer priblíženia na **-Y** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Podobne pridajte naplánované polohovanie s ohľadom na kolízie pre **razník** a **obrobok** (smer priblíženia -Y), ako je znázornené na obr. 2DCFL1.18. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku Primárny zdvih matrice.

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0017.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

### Zdvih primárneho valca

Musíme nastaviť približnú hodnotu, o ktorú sa razník počas tejto operácie posunie. Na konci tejto operácie sú matrice od seba vzdialené približne 0,2”, preto nastavte hodnotu na **0,2** ”, ako je znázornené na obr. 2DCFL1.19. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0018.jpg' | relative_url }})

Základný zdvih matrice

### Nastavenie kritérií zastavenia

Chceme tvarovať diel tak, aby vzdialenosť medzi razníkom a matricou nepresiahla 0,008”. Na obrazovke [Stopping Controls]({{ '/docs/sk/pre_processor/9_simulation_controls/9_3_stopping_controls/' | relative_url }}#9.3.8._Stopping_distance_\(MDSOBJ\)) zaškrtnite políčko vedľa položky **Vzdialenosť medzi objektmi**, aby ste túto možnosť aktivovali. Myšou kliknite na bod na spodnej strane razníka a potom kliknite na bod na hornej strane matrice. Na obrazovke by sa mala zobraziť šípka medzi týmito dvoma bodmi. Nastavte hodnotu tejto vzdialenosti na **0,008** ” v smere **Y**, ako je znázornené na obr. 2DCFL1.20. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0019.jpg' | relative_url }})

Stránka ovládacích prvkov zastavenia

### Prehľad ovládacích prvkov simulácie

Počet simulačných krokov a veľkosť kroku sa nastavujú pomocou posuvníka „Object Shape Complexity“. Ak chcete zmeniť predvolené hodnoty, môžete tak urobiť výberom rádio tlačidla „user type“ a definovaním kroku. V rámci tohto cvičenia ponecháme predvolené hodnoty; kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vytvoriť databázu

Pozrite si stav na stránke „Generate DB“; ak sa zobrazí chyba zadávania údajov, skontrolujte, či nechýbajú nejaké údaje, a doplňte ich. V rámci tejto laboratórnej úlohy by sa mala zobraziť správa: „Vytvorenie databázy nie je pre túto operáciu potrebné. Uskutoční sa počas behu programu.“ Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) prejdite k ďalšej operácii.

## Práca s imbusovým kľúčom

### Zmena názvu operácie

V editore operácií zmeňte názov operácie 3 na „**Hex Head**“.

### Definícia nastavení procesu

Zmeňte nastavenie **Zložitosť** na značku medzi „**Jednoduchá**“ a „**Stredná**“ a zvýšte hodnotu **Presnosť** na „**Stredná**“, ako je znázornené na obr. 2DCFL1.21. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku Top die.

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0020.jpg' | relative_url }})

Stránka procesu

### Vysvetlenie pojmu „punch“

Na stránke „Objekt“ vyberte prepínač typu objektu **Definovať**, ako je znázornené na obr. 2DCFL1.22., a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0021.jpg' | relative_url }})

Okno „Všeobecná definícia hornej matrice“

### Import geometrie výseku

Kliknite na tlačidlo „Načítať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a naimportujte súbor **bolt-punch3.IGS**. Následne skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Definovanie pohybu úderu

Použite údaje o pohybe hornej matrice z predchádzajúcej operácie a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Plánované polohovanie“.

### Plánované umiestnenie

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a vyberte prepínač ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte polohovací objekt na **Punch** a referenčný bod na **Workpiece** a smer priblíženia na **-Y**, ako je znázornené na obr. 2DCFL1.23., potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Primary die stroke.

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0022.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

### Definícia primárneho zdvihu matrice

Na stránke „Primárny zdvih matrice“ nastavte hodnotu primárneho zdvihu matrice na **0,143"**, ako je znázornené na obr. 2DCFL1.24. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0023.jpg' | relative_url }})

Okno primárneho posunu matrice

### Nastavenie kritérií zastavenia

Chceme zastaviť simuláciu, keď sa razník a matrica nachádzajú vo vzdialenosti do 0,010” od seba. Na obrazovke Ovládacie prvky zastavenia zaškrtnite políčko **Vzdialenosť medzi objektmi** a potom kliknite na body na spodnej strane razníka a na hornej strane matrice. Nastavte hodnotu tejto vzdialenosti na **0,010** ” v smere osi Y, ako je znázornené na obr. 2DCFL1.25.

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0024.jpg' | relative_url }})

Okno „Ovládacie prvky zastavenia“

### Prehľad ovládacích prvkov simulácie

Počet simulačných krokov a veľkosť kroku sa nastavujú pomocou posuvníka „Object Shape Complexity“. V tomto cvičení použijeme predvolené hodnoty. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vytvoriť databázu

Pozrite si stav na stránke „Generate DB“; ak sa zobrazí chyba zadávania údajov, skontrolujte, či nechýbajú nejaké údaje, a doplňte ich. V rámci tejto laboratórnej úlohy by sa mala zobraziť správa: „Vytvorenie databázy nie je pre túto operáciu potrebné. Uskutoční sa počas behu programu.“ Uložte projekt a kliknite na režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), aby ste spustili simuláciu.

### Spustenie simulácie

Kliknite na označenie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“ (pozri obr. 2DCFL1.26.). Po kliknutí na možnosť „Spustiť“ sa otvorí dialógové okno „Spustiť simuláciu“, ako je znázornené na obr. 2DCFL1.27. Použite predvolenú možnosť **Pokračovať v spúšťaní**, vyberte možnosť „**Pokračovať od posledného kroku**“ (od kroku -1), potom nastavte režim simulácie na **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) sa spustí simulácia.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0032.jpg' | relative_url }})

Možnosti simulácie

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0034.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať na karte „Simulation Message“ a v časti „Simulation Graphics“ v oblasti zobrazenia „Graphics“ v režime simulácie. Pokiaľ je na karte „Simulation Message“ zaškrtnutá voľba „![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }})“ (čo je predvolené nastavenie), súbor správ sa bude automaticky aktualizovať.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Keď simulácia prebehne bez problémov, skontrolujte správy v súbore LOG; po dokončení všetkých operácií sa v súbore LOG zobrazí správa: „MULTIPLE OPERATION COMPLETED“. (Pozri obr. 2DCFL1.28.)

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0025.jpg' | relative_url }})

Správy v protokoloch

### Následné spracovanie výsledkov

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

Naplnila sa hlava úplne? Pozrite sa na kontaktnú plochu, aby ste lepšie videli, či nie je nejaké miesto nenaplnené.

Je zaťaženie pri tejto operácii väčšie ako zaťaženie požadované pri predchádzajúcich operáciách?

Vykreslite graf závislosti zaťaženia od zdvihu pre každú operáciu, aby ste mohli porovnať zaťaženie v jednotlivých operáciách.

### Stavové premenné

V zozname [State variables]({{ '/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_3_state_variables/' | relative_url }}) kliknite na ikonu „Efektívne deformácie“, aby ste znázornili veľkosť deformácie, ktorá pôsobila na obrobok. Ak chcete zmeniť nastavenia grafu, môžete kliknúť na ikonu „Nastavenie“ ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}). Na tejto obrazovke môžete zobraziť rôzne druhy kontúr (čiarkované, tieňované alebo plné) a tiež zmeniť rozsah premenných, ktorý sa zobrazuje na kontúrovej lište (pozri obr. 2DCFL1.29.). Pomocou možnosti „Nastavenia“ si môžete rozsah kontúrovej lišty definovať sami. Neváhajte experimentovať so zobrazením rôznych stavových premenných a možností grafu.

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0026.jpg' | relative_url }})

Graf stavovej premennej pri deformácii

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0027.jpg' | relative_url }})

Graf stavovej premennej pri napätí

##  Operácia „Die Stress“

###  Pridať operáciu s napätím v matrici

Po dokončení následného spracovania prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}).

Pridajte operáciu „Die stress 2D“ zo zoznamu operácií v programe Explorer a pridanú operáciu „Die stress“ otvorte dvojitým kliknutím na túto operáciu v zozname operácií.

### Vybrať objekty

V súčasnosti sa zaujímame iba o analýzu napätia v razníku pri operácii s šesťhrannou hlavou. Zoznamu teda odstráňte matricu (objekt 3) a vyhadzovač (objekt 4) kliknutím na tlačidlo odstrániť ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (pozri obr. 2DCFL1.31.)

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0028.jpg' | relative_url }})

Okno „Stress Objects“

Typ objektu obrobku bude štandardne nastavený na „Načítané z databázy“; tento objekt zostane zachovaný až do vytvorenia databázy, pričom pri jej generovaní bude odstránený. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Definícia pojmu „Top Die“

V predvolenom nastavení bude zaškrtnuté políčko „Die (Elastic)“ – použite typ objektu „Die“ a potom prejdite na stránku „![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh“.

### Hlavná stránka o sieťke na lisovacej forme

Nastavte počet prvkov na 2500, ako je znázornené na obr. 2DCFL1.32, a vygenerujte sieť. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Material“.

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0029.jpg' | relative_url }})

Okno so sieťkou

### Priradiť materiál pre hornú matricu

Načítajte materiál formy z knižnice materiálov. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice), vyberte kategóriu **Die_material**, potom **AISI-H-13** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Zo zoznamu vyberte **AISI-H-13**. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Okrajové podmienky.

### Nastavenie okrajovej podmienky pre hornú formu

Ďalej musíme na razník aplikovať okrajové podmienky, aby neodletel do vesmíru, keď naň pôsobia zaťaženia vznikajúce pri tvárnení.

V predvolenom nastavení sú pri osovo symetrickom telese všetky uzly v smere x na stredovej osi fixované; ak tomu tak nie je, uistite sa, že smer okrajovej podmienky je nastavený na X, a potom v rozbaľovacom okne kliknite na tlačidlo „By edge ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }})“. Pomocou tohto nastavenia môžeme pridať BCC ku všetkým uzlom/prvkom na hrane. Vyberte bod na stredovej osi výseku a mali by ste vidieť, že všetky uzly na stredovej osi sú zafixované v smere X. 

Teraz nastavte smer okrajovej podmienky na os Y, vyberte bod na hornej ploche razníka, aby ste zafixovali všetky tieto uzly v smere osi Y (pozri obr. 2DCFL1.33.). Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Vynútiť interpoláciu“.

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0031.jpg' | relative_url }})

Okrajová podmienka s predpísanou rýchlosťou

### Vynútená interpolácia

Po vytvorení siete je potrebné interpolovať formovacie zaťaženia z obrobku na razník. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}). Po interpolácii síl sa v nižšie uvedenom okne zobrazí správa porovnávajúca sily pôsobiace na obrobok s novými silami pôsobiacimi na razník, ako je znázornené na obr. 2DCFL1.34. Tieto sily by mali byť relatívne blízko seba (zvyčajne v rozmedzí približne 5 %). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí Generate DB.

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0030.jpg' | relative_url }})

Vynútiť okno interpolácie

### Vytvoriť databázu

Skontrolujte údaje a vytvorte databázu. Po vytvorení databázy prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

### Spustenie simulácie

Kliknite na označenie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“; po kliknutí na možnosť „Spustiť“ sa otvorí dialógové okno „Spustiť simuláciu“. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) sa simulácia spustí.

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

### Postprocesor

Hlavnými veličinami, na ktoré je potrebné sa zamerať pri simulácii napätia v tvare, sú **efektívne napätie** a **maximálne hlavné napätie**.

Efektívne napätie sa používa na zistenie, či v niektorej časti lisovacej formy došlo k plastickej deformácii. Ak má nejaká oblasť lisovacej formy efektívne napätie blízke alebo presahujúce medzu tečnosti materiálu lisovacej formy, v tejto oblasti hrozí riziko plastickej deformácie. (Pozri obr. 2DCFL1.35)

Maximálne hlavné napätie sa používa na zistenie, ktoré oblasti matrice sú v stave stlačenia a ktoré v stave ťahu. Maximálne hlavné napätie je mimoriadne dôležité pri určovaní, či na matrici dôjde k prasknutiu v dôsledku únavy materiálu. Ak chcete zobraziť maximálne hlavné napätie, kliknite na tlačidlo stavovej premennej ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) a potom zo zoznamu vyberte položku **Napätie – Maximálne hlavné**. (Pozri obr. 2DCFL1.36.)

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0032.jpg' | relative_url }})

Dej s dôrazom na napätie

![]({{ '/assets/images/labs/forming_express_labs/2d_cold_forming_lab1/image0033.jpg' | relative_url }})

Graf maximálneho hlavného napätia
