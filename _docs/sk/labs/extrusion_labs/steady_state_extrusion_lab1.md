---
lang: sk
title: "Laboratórium extrudovania v ustálenom stave 1"
---

# Laboratórne cvičenie č. 1: Extrúzia v ustálenom stave

V tomto cvičení nastavíme jednoduchý proces extrudovania v ustálenom stave importom databázy modelu [ALE Extrusion lab]({{ '/docs/sk/labs/extrusion_labs/ale_extrusion_lab1/' | relative_url }}) ([3D_ALE_EX_Lab1]({{ '/docs/sk/labs/extrusion_labs/ale_extrusion_lab1/' | relative_url }}#3D_ALE_EX_Lab1)). V rámci tohto cvičenia využijeme aj nastavenie dĺžky ložiska.

V rámci tejto laboratórnej úlohy sa z veľkého valcového polotovaru vytlačia 5 malých valcových dielov. Model obrobku použitý v programe ALE je symetrický, ako je znázornené na obr. SSEXTL1.1. Priemer D0 je 140 mm. Priemer D1 je 26 mm. Priemery D2 a D4 sú 27 mm. Priemery D3 a D5 sú 28 mm.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0001.jpg' | relative_url }})

Model obrobku

1.1. Vytvorenie nového problému

1.2. Pridanie operácie

1.3. Import databázy extrúzií ALE

1.4. Nastavenie simulácie

1.5. Ovládacie prvky krokov

1.6. Vytvorenie databázy

1.7. Spustenie simulácie

1.8. Následné spracovanie

1.9. Nastavenie dĺžky ložiska

1.10. Porovnanie výsledkov simulácií

## Vytvorenie nového problému 

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené na obrázku SSEXTL1.2.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno programu DEFORM GUI

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. SSEXTL1.3. Vyberte tlačidlo „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte systém jednotiek „**SI**“. Zadajte názov úlohy ako „**********3D_SS_EX_Lab1**** **“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

Stránka „Nový problém“

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom „Nový projekt“, kde bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**3D_SS_EX_Lab1**“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

##  Pridanie operácie

Pridajte operáciu „3D Extrusion“ zo zoznamu operácií v prehliadači. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ktoré sa nachádza vedľa položky „3D Extrusion“, alebo ju môžete pridať aj pretiahnutím do editora operácií. Po pridaní operácie „3D Extrusion“ sa štandardne otvorí okno nastavení procesu.

## Import databázy extrúzií ALE

V tomto bode môžeme importovať prvý krok z databázy ALE (databáza vytvorená v nastavení [**ALE Extrusion Lab1**]({{ '/docs/sk/labs/extrusion_labs/ale_extrusion_lab1/' | relative_url }}) (**3D_ALE_EX_Lab1**)). Kliknite na **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Import**, vyberte súbor **3D_ALE_EX_Lab1.DB** a zvoľte krok **-1.** Teraz už stačí len upraviť rozdiely medzi simuláciou ALE a novou analýzou ustáleného stavu.

## Nastavenie simulácie

Prejdite do časti **Nastavenie simulácie** a v položke Metóda simulácie vyberte voľbu **Extrúzia v ustálenom stave**. V časti **Zrýchlenie** nastavte **Aktualizáciu deformácie** a **Aktualizáciu teploty** na hodnotu **0** na krok, potom **zrušte zaškrtnutie** políčok **Aktualizácia deformácie** a **Aktualizácia teploty**. Nastavenie simulácie je znázornené na obr. SSEXTL1.4. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po ovládacie prvky krokov alebo vyberte Ovládacie prvky krokov zo stromu Operácie.

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0004.jpg' | relative_url }})

Nastavenie simulácie

## Ovládacie prvky krokov

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) v hornom paneli ponúk prejdete do expertného režimu pre krokové riadenie.

### Kroky simulácie

Pri simulácii extrudovania v ustálenom stave sa geometria aktualizuje až v poslednom kroku na základe vypočítaného poľa rýchlostí.

Ak vzťah medzi obrobkom a matricou v rámci oddelenia kontaktov nastavíme na „Neoddeliteľné“, pole rýchlostí dosiahne ustálený stav po 2 simulačných krokoch. V tejto situácii stačí na simuláciu extrudovania v ustálenom stave 5 simulačných krokov.

Ak vzťah medzi obrobkom a matricou definujeme ako „oddeliteľný“, v oblasti ložiska bude v každom simulačnom kroku dochádzať k oddeleniu a kontaktu. Preto potrebujeme viac simulačných krokov, aby rýchlostné pole dosiahlo ustálený stav. V tejto situácii zvyčajne stačí 10 simulačných krokov na extrudovanie v ustálenom stave.

V tomto laboratórnom cvičení sme teda v dialógovom okne „Simulačné kroky“ nastavili **Počet****** **simulačných** krokov na hodnotu „**5**“ a **Krok****inkrement** na **uloženie** na hodnotu „**1**“ v dialógovom okne Simulačné kroky (pozri obr. SSEXTL1.5.).

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0005.jpg' | relative_url }})

Nastavenie simulačného kroku

### Kritériá ukončenia

V dialógovom okne **Kritériá zastavenia** kliknite na kartu **ALE** **Steady** **State** a **zrušte zaškrtnutie** políčka „**Zapnúť riadenie zastavenia v ustálenom stave**“, ak nie je už zrušené (pozri obr. SSEXTL1.6.).

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0027.jpg' | relative_url }})

Ovládanie zastavenia

## Vytvoriť databázu

Potom prejdite na stránku „Generate DB“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali, či sa pri nastavení na niečo nezabudlo, a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) na vytvorenie databázy. Pozrite si správu na karte „Message“, ktorá informuje o stave vytvárania databázy.

## Spustenie simulácie

Po vytvorení databázy prejdite do simulačného režimu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. SSEXTL1.7. Použite predvolenú možnosť **Pokračovať****Spustiť** na výber možnosti „**Pokračovať od posledného kroku**“ (od kroku -1) a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Ak chcete nastaviť parametre MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}). Rozbalí sa okno „Run Options“, v ktorom sa zobrazia možnosti na nastavenie parametrov MPI pre simuláciu (maximálny počet procesorov, ktorý je možné nastaviť, závisí od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0007.jpg' | relative_url }})![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0007.jpg' | relative_url }})

Spustiť okno simulácie

Priebeh simulácie môžete sledovať na kartách „Simulation Message“ a „Simulation Log“; uistite sa, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Počas priebehu simulácie až po dosiahnutie zadaného kroku si používateľ môže prezrieť proces extrudovania na grafických zobrazeniach simulácie.

## Následné spracovanie

Po dokončení simulácie si výsledky prezrite tak, že prejdete do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov Simulácia.

Grafy **efektívneho****deformácie** a **teploty** obrobku v poslednom kroku sú uvedené na obr. SSEXTL1.8 a obr. SSEXTL1.9.

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0008.jpg' | relative_url }})

Efektívne rozloženie deformácie v poslednom kroku

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0009.jpg' | relative_url }})

Rozloženie teploty v poslednom kroku

Graf posunutia v smere X a posunutia v smere Y obrobku v poslednom kroku je uvedený na obr. SSEXTL1.10 a obr. SSEXTL1.11. Hoci sú posuny veľmi malé, nemôžeme pozorovať ohyb tvaru, ale z rozloženia posunov v smere X vidíme, že prevládajúci posun sa nachádza na profile D3 s zápornou hodnotou. Z rozloženia posunov v smere Y je zrejmé, že prevládajúci posun sa nachádza na profile D2 a má zápornú hodnotu. Z toho vyplýva, že okrajové profily (D2 a D3) sa po extrudovaní ohnuli smerom k centrálnemu profilu (D1), čo je podobné výsledku simulácie Lagrangeovej extrudácie.

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0010.jpg' | relative_url }})

X – Rozloženie posunu obrobku v poslednom kroku

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0011.jpg' | relative_url }})

Rozloženie posunu v smere Y obrobku v poslednom kroku

## Nastavenie dĺžky ložiska

Pri extrudovaní sú ohyby, skrútenia a zvlnenia profilov spôsobené hlavne nerovnomerným tokom materiálu. V tomto príklade, pri obvodových profiloch, materiál na vonkajšej strane tiekol rýchlejšie ako na vnútornej strane, čo spôsobilo ohyb. Ohyb obvodových profilov môžeme znížiť nastavením dĺžky ložiska.

Mali by sme si uchovať nastavenie simulácie a výsledky simulácie z tohto projektu a v rámci iného projektu vykonať simuláciu úpravy dĺžky ložiska.

### Simulácia postupného nastavovania dĺžky ložiska

V ponuke **Súbor** kliknite na položku Nový ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) a v oboch vyskakujúcich oknách Otázky kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). Otvorí sa nový projekt s vyskakujúcim oknom Nový projekt.

V okne „Nový projekt“ zadajte názov projektu ako „**3D_SS_EX_Lab1_BRGADJ**“, vyberte **Kopírovať****existujúci** **projekt**, kliknite na **Prehľadať**, vyhľadajte **projekt** „**3D_SS_EX_Lab1**“ a v okne Nový projekt kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). Projekt „3D_SS_EX_Lab1“ sa skopíruje do projektu „3D_SS_EX_Lab1_BRGADJ“ spolu so všetkými nastaveniami.

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0012.jpg' | relative_url }})

Nový projekt pre laboratórium na nastavovanie dĺžky ložísk

Prejdite na stránku **Die![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Kontrolné body ložiska matice**.

V tomto laboratórnom cvičení skrátime dĺžku vnútorného oporného úseku profilu D2, aby sme urýchlili tok materiálu na tejto strane, a predĺžime dĺžku vonkajšieho oporného úseku profilu D3, aby sme spomalili tok materiálu na tej strane.

Na stránke **Die****Bearing****Control****Points** vyberte ložiskovú plochu 1 (v okne zobrazenia je zvýraznená zelenou farbou) a definujte 3 kontrolné body kliknutím na vstupnú hranu ložiska v polohách vnútornej strany, stredu a vonkajšej strany. Potom môžeme v tabuľke kontrolných bodov upraviť ich súradnice a mierky dĺžky. Vyberte bod 1 v tabuľke, zmeňte jeho súradnice na (0,31,5,0) a zmeňte jeho mierku dĺžky na „0,55“. Vyberte bod 2 v tabuľke, zmeňte jeho súradnice na (13,5; 45; 0) a dĺžkové mierky ponechajte na hodnote „1“. Vyberte bod 3 v tabuľke, zmeňte jeho súradnice na (0; 58,5; 0) a dĺžkové mierky ponechajte na hodnote „1“. Vidíme, že tvar ložiska a dĺžka ložiska pre povrch 1 sa zmenili (pozri obr. SSEXTL1.13.).

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0013.jpg' | relative_url }})

Nastavenie kontrolných bodov opornej plochy 1

Vyberte ložiskovú plochu 3 (v okne zobrazenia zvýraznenú zelenou farbou) a definujte 3 kontrolné body kliknutím na vstupnú hranu ložiska v polohách vnútornej strany, stredu a vonkajšej strany. Následne môžete v tabuľke kontrolných bodov upravovať ich súradnice a mierky dĺžky. Vyberte bod 1 v tabuľke, zmeňte jeho súradnice na (31,0,0), mierku dĺžky ponechajte na hodnote „1“. Vyberte bod 2 v tabuľke, zmeňte jeho súradnice na (45,14,0), mierku dĺžky ponechajte na hodnote „1“. Vyberte bod 3 v tabuľke, zmeňte jeho súradnice na (59,0,0) a zmeňte jeho mierku dĺžky na „1,5“. Vidíme, že tvar a dĺžka nosníka pre plochu 3 sa zmenili (pozri obr. SSEXTL1.14.).

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0014.jpg' | relative_url }})

Nastavenie kontrolných bodov opornej plochy 3

Kliknite na stránku „Die Bearing Control Points“, otočte objekt v okne „Display“ – upravenú geometriu formy môžete vidieť na obr. SSEXTL1.15.

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0015.jpg' | relative_url }})

Geometria matice po nastavení dĺžky ložiska

Prejdite na stránku **Kontrola krokov**, v dialógovom okne **Kritériá zastavenia** kliknite na stránku **ALE****Steady****State**, **zrušte zaškrtnutie** políčka „**Zapnúť riadenie zastavenia v ustálenom stave**“ (pozri obr. SSEXTL1.6.).

### Vytvoriť databázu

Potom prejdite na stránku „Generate DB“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali, či sa pri nastavení na niečo nezabudlo, a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) na vytvorenie databázy. Pozrite si správu na karte „Message“, ktorá informuje o stave vytvárania databázy.

### Spustenie simulácie

Po vytvorení databázy prejdite do simulačného režimu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. SSEXTL1.16. Použite predvolenú voľbu **Pokračovať****Spustiť** na výber možnosti „**Pokračovať od posledného kroku**“ (od kroku -1) a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Ak chcete nastaviť parametre MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}). Rozbalí sa okno „Run Options“, v ktorom sa zobrazia možnosti na nastavenie parametrov MPI pre simuláciu (maximálny počet procesorov, ktorý je možné nastaviť, závisí od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0016.jpg' | relative_url }})

Spustiť okno simulácie

Priebeh simulácie môžete sledovať na kartách „Simulation Message“ a „Simulation Log“; uistite sa, že je zaškrtnutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Počas simulácie, keď sa proces posúva k zadanému kroku, si používateľ môže v grafickom zobrazení simulácie prezrieť proces extrudovania.

## Porovnanie výsledkov simulácií

Po dokončení simulácie upravenej ložiskovej plochy môžeme výsledky simulácie porovnať v postprocesore.

V okne **DEFORM GUI Main** označte súbor „**3D_SS_EX_Lab1.DB**“ a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_post_processor_gui_link.jpg' | relative_url }}), aby sa súbor „**3D_SS_EX_Lab1.DB**“ otvoril v postprocesore.

V programe Post-processor kliknite v hornom paneli ponúk na položku **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Open**, vyberte súbor „**3D_SS_EX_Lab1_BRGADJ.DB**“ a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}).

V hornom paneli ponúk kliknite na **Windows**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})******Usporiadať vertikálne**. Vidíme, že v postprocesore sú otvorené súbory „**3D_SS_EX_Lab1.DB**“ aj „**3D_SS_EX_Lab1_BRGADJ.DB**“. Vďaka tomu môžeme porovnať výsledky simulácie oboch databáz v jednom okne.

V okne zobrazenia kliknite pravým tlačidlom myši a zaškrtnite políčka „**DB Info**“ aj „**Title**“, aby sa zobrazil názov databázy a krok simulácie.

Najskôr porovnáme styčné body obrobku v poslednom kroku. Je zrejmé, že po úprave dĺžky opory vidíme odlišné styčné body v okrajových profiloch D2 a D3 (pozri obr. SSEXTL1.17.).

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0017.jpg' | relative_url }})

Porovnanie kontaktov obrobku v poslednom kroku

Následne porovnáme posuny. Porovnanie posunu v smere X obrobku v poslednom kroku je znázornené na obr. SSEXTL1.18. Vidíme, že prevládajúci posun v smere X, označený hodnotou Min, sa po úprave dĺžky ložiska znížil na 20 %.

Porovnanie posunutia obrobku v smere Y v poslednom kroku je uvedené na obr. SSEXTL1.19. Vidíme, že prevládajúce posunutie v smere Y, označené hodnotou Min, sa po úprave dĺžky ložiska znížilo na 40 %.

Nastavenie dĺžky ložiska je teda účinnou metódou na zmenu rovnováhy toku materiálu pri extrudovaní v režime ALE aj v ustálenom stave.

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0018.jpg' | relative_url }})

Porovnanie posunu X obrobku v poslednom kroku

![]({{ '/assets/images/labs/extrusion_labs/steady_state_extrusion_lab1/image0019.jpg' | relative_url }})

Porovnanie posunu v smere Y obrobku v poslednom kroku
