---
lang: sk
title: "3D analýza napätia v čipe s viacerými krokmi"
---

# Laboratórna práca č. 3: Štúdia 3D napätí v lisovacej matrici v rôznych fázach operácie 

V tomto laboratórnom cvičení budeme používať nástroj „Die Stress Study“ na analýzu napätí v lisovacích formách v rôznych fázach operácie. V súčasnosti by mali všetky fázy analýzy napätí pochádzať z tej istej operácie. Pri typickej simulácii napätí v lisovacích formách sa obrobok odstráni a sily, ktoré obrobok pôsobí na lisovacie formy, sa interpolujú na nástroje. 

  
Ak použijeme možnosť viacerých krokov, nastavíme analýzu napätia v lisovacej forme pre prvý krok zo zvolených krokov a pre nasledujúce kroky analýzy napätia v lisovacej forme naplánujeme interpoláciu síl pôsobiacich na obrobok. Údaje o objektoch, ovládacie prvky simulácie a ďalšie nastavenia sa prenesú z prvého kroku analýzy napätia v lisovacej forme. Od verzie v13.1.1 boli na stránke objektov zavedené dve nové možnosti na umiestnenie lisovacích foriem v nasledujúcich krokoch, pozri obr. 3DDSL3.1.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0021.jpg' | relative_url }})

Možnosti umiestnenia foriem pre ďalšie kroky v štúdii namáhania foriem

**Umiestnenie formy v nasledujúcich krokoch pri viacstupňovej analýze napätia formy:**  
V prípade viackrokového posúdenia namáhania formy, ak objekt vyžaduje polohovanie, musí používateľ určiť, ako má byť objekt v nasledujúcich krokoch umiestnený, a to zaškrtnutím políčka „Potreba polohovania“ na stránke objektu, ako je znázornené na obr. 3DDSL3.1.

  * Ak je objekt súčasťou nominálnej konfigurácie a vyžaduje sa jeho polohovanie, musí používateľ zaškrtnúť políčko „Vyžaduje sa polohovanie“ a z nominálnej konfigurácie vybrať príslušný objekt ako „Nasledujúci objekt“.

  * Ak objekt nie je súčasťou nominálneho nastavenia, ale nachádza sa v ohraničujúcom obdĺžniku objektu nominálneho nastavenia a vyžaduje polohovanie, musí používateľ zaškrtnúť políčko „Potreba polohovania“ a z nominálneho nastavenia vybrať príslušný objekt, v ktorého ohraničujúcom obdĺžniku sa aktuálny objekt nachádza, ako „Nasledujúci objekt“. Zaškrtávacie políčko Nie je pôvodný objekt by sme nemali zaškrtávať, aby bolo možné na aktuálny objekt uplatniť funkciu Vynútiť interpoláciu z nominálnej konfigurácie.

  * Ak objekt nie je súčasťou nominálnej konfigurácie, nenachádza sa v ohraničujúcom obdĺžniku žiadneho z objektov nominálnej konfigurácie a vyžaduje polohovanie, musí používateľ zaškrtnúť políčko „Vyžaduje polohovanie“ a vybrať objekt z nominálnej konfigurácie, s ktorým sa aktuálny objekt dotýka, alebo ho určiť ako „Nasledovaný objekt“. Mali by sme tiež zaškrtnúť políčko „Nie je pôvodný objekt“. Ak používateľ zaškrtne políčko „Nie je pôvodný objekt“ pre daný objekt, na tento objekt sa nebude vykonávať interpolácia síl.

Na nastavenie analýzy napätí v matrici v niekoľkých krokoch budeme používať projekt „Stub Shaft“, ktorý bol vytvorený počas cvičenia [Lab 05 Stub Shaft]({{ '/docs/sk/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/' | relative_url }}) v rámci laboratórnych cvičení MO Basic.

  
3.1. Nastavenie projektu „Nominal“

3.2. Pridanie analýzy napätí v lisovacej forme

3.3. Výber kroku

3.4. Definícia objektov pre analýzu napätí v matrici

3.5. Definícia úderu

3.5.1. Definovanie údajov objektu „Punch“

3.5.2. Vytvorenie siete pre Punch

3.5.3. Priradenie materiálu k dierovaču

3.5.4. Priradenie okrajových podmienok k výrezu

3.5.5. Interpolácia sily z polotovaru a plánovanie interpolácie

3.6. Definovanie spodnej formy

3.6.1. Definovanie údajov objektu spodnej matrice

3.6.2. Vytvorenie siete pre spodnú matricu

3.6.3. Priradenie materiálu k spodnej matrici

3.6.4. Priradenie okrajových podmienok spodnej matrici

3.6.5. Interpolácia sily z polotovaru a plánovanie interpolácie

3.7. Definovanie ovládacích prvkov simulácie

3.8. Vytvorenie databázy

3.9. Spustenie simulácie

3.10. Následné spracovanie výsledkov simulácie

## Nastavenie projektu „Nominal“

Nastavte [Lab 05 Stub Shaft in MO Basic Labs]({{ '/docs/sk/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/' | relative_url }}). Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}). (Pozri obr. 3DDSL3.2.)

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0001.jpg' | relative_url }})

Simulačný monitor zobrazujúci koniec laboratórnej simulácie v hľavici šachty.

##  Pridanie analýzy napätia v matrici

V ľavom hornom rohu okna zobrazenia kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) a vyberte operáciu „Add Die stress Study“, ako je znázornené na obr. 3DDSL3.3. V zobrazovacej oblasti sa pridá karta operácie Štúdia napätia čipu a dlaždica operácie Napätie čipu bude k dispozícii v editore operácií pod novým tlačidlom, ako je znázornené na obr. 3DDSL3.4.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0002.jpg' | relative_url }})

Pridanie operácie „Analýza napätia v lisovacej forme“.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0003.jpg' | relative_url }})

Zobrazenie operácie „Analýza napätia v lisovacej matrici“.

## Výber kroku

Keďže chceme analyzovať napätia vo viacerých krokoch operácie, vyberte voľbu „**Viac****krokov**“ ako typ výberu napätia formy. Vyberte voľbu „Načítať kroky z databázy“, aby sa načítali údaje objektu z prvého kroku vybraných krokov, a pomocou voľby „****User defined**“ vyberte na stránke výberu krokov kroky 10, 25, 35 a 45 operácie „Cone“, aby ste analyzovali napätia v týchto krokoch, ako je znázornené na obr. 3DDSL3.5. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0004.jpg' | relative_url }})

Výber viacerých fáz prevádzky stroja Cone na analýzu napätí v lisovacích formách.

## Definícia objektov pre analýzu napätí v matrici

Keďže analýzu napätia v matrici musíme vykonať len na razníku a spodnej matrici, odstránime ostatné objekty. Na stránke s objektmi odstráňte objekt „Ejector“, ako je znázornené na obr. 3DDSL3.6. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0005.jpg' | relative_url }})

Odstránenie nepotrebných objektov na stránke „Objekty“.

## Definícia pojmu „punch“ 

### Definovanie údajov objektu Punch

V predvolenom nastavení sa typ tuhých objektov z načítaného kroku zmení na pružný. Pre objekt „Punch“ ponechajte typ objektu ako pružný. Keďže tento objekt existuje v nominálnej operácii a vyžaduje polohovanie v budúcich krokoch, zaškrtnite políčko Potrebné polohovanie a z roletového menu vyberte objekt Punch z nominálnej operácie ako Nasledujúci objekt, ako je znázornené na obr. 3DDSL3.7. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Sieť.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0013.jpg' | relative_url }})

Stránka objektu Punch

### Vytvorenie siete pre Punch

Na vytvorenie siete nastavte cieľový počet prvkov na 40 000, ako je znázornené na obr. 3DDSL3.8, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Material“ (Materiál).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0006.jpg' | relative_url }})

Nastavenia siete pre nástroj „Punch“.

### Priradenie materiálu k dierovaču

Naimportujte materiál AISI-D3 z knižnice materiálov. Zo zoznamu vyberte **AISI-D3**, aby ste tento materiál priradili k razníku, ako je znázornené na obr. 3DDSL3.9. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Okrajové podmienky“.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0007.jpg' | relative_url }})

Priradenie materiálu k programu Punch.

### Priradenie okrajových podmienok k výrezu

Musíme na nástroj Punch aplikovať okrajové podmienky, aby neodletel do vesmíru, keď naň pôsobia tvárniace zaťaženia. Na stránke BCC v časti Deformácia vyberte možnosť Rýchlosť, nastavte rýchlosť na 0, vyberte prepínač „All“ na fixáciu všetkých smerov a potom vyberte hornú plochu razníka pomocou ![]({{ '/assets/icons/pre_icons/mo_bcc_surface_patch_icon.jpg' | relative_url }}) z možností výberu a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) na aplikovanie rýchlosti BCC, ako je znázornené na obr. 3DDSL3.10. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Vynútená interpolácia.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0008.jpg' | relative_url }})

Priradenie okrajových podmienok k programu Punch.

### Interpolácia sily z polotovaru a plánovanie interpolácie

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) vykonajte interpoláciu síl pôsobiacich na matrice zo strany polotovaru. Po dokončení interpolácie by sa mala na stránke „Interpolácia síl“ zobraziť správa porovnávajúca sily pôsobiace zo strany polotovaru s novými silami pôsobiacimi na razník, ako je znázornené na obr. 3DDSL3.11. Tieto sily by mali byť relatívne blízko pri sebe. 

Keďže simulujeme viacero krokov, musíme naplánovať interpoláciu síl z polotovaru. Na to zaškrtnite políčko vedľa položky „Interpolácia sily“ a nastavte toleranciu na hodnotu 0,0271477. Toleranciu môžeme ponechať na hodnote „0“, čím sa tolerancia pre interpoláciu vypočíta automaticky. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujte spodnú matricu.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0009.jpg' | relative_url }})

Interpolované sily pôsobiace na razník zo sochoru.

##  Definícia spodnej matrice

### Definovanie údajov objektu spodnej matrice

Pre spodnú matricu ponecháme typ objektu „Elastic“. Zaškrtnite políčko „Need positioning“ a z roletového menu „Following object“ vyberte „Bottom Die“ z objektov nominálnej databázy, ako je znázornené na obr. 3DDSL3.12. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Mesh“, a vygenerujte sieť.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0014.jpg' | relative_url }})

Stránka objektu „Spodná matrica“

### Vytvorenie siete pre spodnú formu

Nastavte počet prvkov na **40000**, ako je znázornené na obr. 3DDSL3.13, a vygenerujte sieť. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Material“.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0010.jpg' | relative_url }})

Nastavenia sieťoviny pre spodnú matricu.

### Priradenie materiálu k spodnej matrici

Na stránke „Materiál“ vyberte zo zoznamu položku „AISI-D3“, aby ste priradili materiál pre spodnú formu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Okrajové podmienky“.

### Priradenie okrajových podmienok k spodnej forme

Musíme na spodnú matricu aplikovať okrajové podmienky, aby neodletela do vesmíru, keď na ňu pôsobia zaťaženia pri tvárnení. Na stránke BCC v časti „Deformation“ vyberte položku „Velocity“, nastavte rýchlosť na 0, vyberte rádio tlačidlo „All“ na fixáciu všetkých smerov a potom vyberte spodnú plochu spodnej matrice pomocou ![]({{ '/assets/icons/pre_icons/mo_bcc_surface_patch_icon.jpg' | relative_url }}) z možností výberu a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) na aplikovanie BCC, ako je znázornené na obr. 3DDSL3.14. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Vynútená interpolácia“.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0011.jpg' | relative_url }})

Priradenie okrajových podmienok spodnej formy.

### Interpolácia sily z polotovaru a plánovanie interpolácie

Po vytvorení siete je potrebné interpolovať tvárniace zaťaženia zo surového polotovaru na spodnú matricu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}). Po interpolácii síl by sa na stránke Interpolácia síl mala zobraziť správa porovnávajúca sily pôsobiace na sochoru s novými silami pôsobiacimi na spodnú matricu, ako je znázornené na obr. 3DDSL3.15. Tieto sily by mali byť relatívne blízko seba. 

Ak chcete naplánovať interpoláciu síl pre nasledujúce kroky analýzy napätia v lisovacej forme, zaškrtnite políčko vedľa položky „Interpolácia síl“ a hodnotu tolerancie ponechajte na „0“, aby sa tolerancia pre interpoláciu vypočítala automaticky. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno „Ovládacie prvky simulácie“.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0012.jpg' | relative_url }})

Interpolované sily pôsobiace na spodnú matricu zo sochoru

## Definovanie ovládacích prvkov simulácie

Nastavte počet krokov na hodnotu 2 a ostatné nastavenia ponechajte v predvolenom stave, ako je znázornené na obr. 3DDSL3.16. Tieto nastavenia sa budú používať aj v nasledujúcich krokoch analýzy napätia v čipe. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0015.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre analýzu napätia v výlisku

## Vytvorenie databázy

Na stránke „DB Generation“ skontrolujte, či v nastaveniach nie sú žiadne chyby, a vygenerujte databázu. Po vygenerovaní databázy prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

##  Spustenie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia). Použite predvolenú možnosť **Continue Run** (Pokračovať v spustení) na výber možnosti „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) sa spustí simulácia.

Po dokončení simulácie všetkých krokov analýzy napätia v forme sa v súbore protokolu zobrazí správa „MULTIPLE OPERATION COMPLETED“, ako je znázornené na obr. 3DDSL3.17. Pre zobrazenie výsledkov prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0016.jpg' | relative_url }})

Protokolový súbor zobrazujúci koniec simulácie pre všetky vybrané kroky analýzy napätí v lisovacej forme

## Následné spracovanie výsledkov simulácie

Každý vybraný krok sa zobrazí ako samostatná operácia s názvom „Od kroku XX“ (XX je číslo vybraného kroku). Hlavnými premennými, na ktoré je potrebné sa zamerať pri simulácii napätia v výlisku, sú efektívne napätie a maximálne hlavné napätie.

  
Efektívne napätie sa používa na zistenie, či v niektorej časti formy došlo k plastickej deformácii. Ak má akákoľvek oblasť formy efektívne napätie blízke alebo presahujúce medzu tečnosti materiálu formy, v tejto oblasti hrozí riziko plastickej deformácie (pozri obr. 3DDSL3.18). Pomocou nástroja na rezanie môžeme formy rozrezať na rezy, aby sme mohli zobraziť napätia vo vnútri dutiny formy. 

  
Maximálne hlavné napätie slúži na zistenie, ktoré oblasti matrice sú v stave tlakového namáhania a ktoré v stave ťahového namáhania. Maximálne hlavné napätie je mimoriadne dôležité pri určovaní, či na matrici dôjde k prasknutiu v dôsledku únavy materiálu. Ak chcete zobraziť maximálne hlavné napätie, kliknite na tlačidlo „Set up“ (Nastaviť) pre stavovú premennú a potom zo zoznamu vyberte možnosť „Stress – Max Principal“ (Napätie – Maximálne hlavné napätie). (Pozri obr. 3DDSL3.19)

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0017.jpg' | relative_url }})

Rozloženie efektívneho napätia na konci posledného kroku analýzy napätia v matrici pri operácii „Cone“

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0018.jpg' | relative_url }})

Rozloženie maximálneho hlavného napätia na konci posledného kroku analýzy napätia v matrici pri operácii „Cone“
