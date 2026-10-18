---
lang: sk
title: "Štúdia napätia v 2D s viacerými krokmi"
---

# Lab2: Štúdia napätia v 2D pri viacerých krokoch operácie 

2.1. Nastavenie projektu „Nominal“

2.2. Pridanie analýzy napätia v lisovacej forme

2.3. Výber kroku

2.4. Definícia objektov pre analýzu napätia v lisovacom nástroji

2.5. Definícia úderu

2.5.1. Definovanie údajov objektu „Punch“

2.5.2. Vytvorenie siete pre Punch

2.5.3. Priradenie materiálu k dieru

2.5.4. Priradenie okrajových podmienok k výrezu

2.5.5. Interpolácia sily z polotovaru a plánovanie interpolácie

2.6. Definícia spodnej formy

2.6.1. Definovanie údajov objektu spodnej formy

2.6.2. Vytvorenie siete pre spodnú formu

2.6.3. Priradenie materiálu k spodnej matrici

2.6.4. Priradenie okrajových podmienok spodnej matrici

2.6.5. Interpolácia sily z polotovaru a plánovanie interpolácie

2.7. Definovanie ovládacích prvkov simulácie

2.8. Vytvorenie databázy

2.9. Spustenie simulácie

2.10. Následné spracovanie výsledkov simulácie

V tomto laboratórnom cvičení budeme používať nástroj „Die Stress Study“ na analýzu napätí v lisovacích formách v rôznych fázach operácie. V súčasnosti by mali všetky fázy analýzy napätí pochádzať z tej istej operácie. Pri typickej simulácii napätí v lisovacích formách sa obrobok odstráni a sily, ktoré obrobok pôsobí na lisovacie formy, sa interpolujú na nástroje. 

V tomto laboratórnom cvičení budeme používať modul „Die Stress Study“ na analýzu napätí v lisovacích formách v rôznych fázach operácie. V súčasnosti by mali všetky fázy analýzy napätí pochádzať z tej istej operácie. Pri typickej simulácii napätí v lisovacích formách sa obrobok odstráni a sily, ktoré obrobok pôsobí na lisovacie formy, sa interpolujú na nástroje.  
Ak použijeme možnosť viacerých krokov, nastavíme analýzu napätia v lisovacej forme pre prvý krok zo zvolených krokov a pre nasledujúce kroky analýzy napätia v lisovacej forme naplánujeme interpoláciu síl pôsobiacich na obrobok. Údaje o objektoch, ovládacie prvky simulácie a ďalšie nastavenia sa prenesú z prvého kroku analýzy napätia v lisovacej forme. Od verzie v13.1.1 boli na stránke objektov zavedené dve nové možnosti na umiestnenie lisovacích foriem v nasledujúcich krokoch, pozri obr. 2DDSL2.1.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0021.jpg' | relative_url }})

Možnosti umiestnenia formy pre ďalšie kroky v štúdii namáhania formy

  
**Umiestnenie lisovacej formy v ďalších krokoch viacstupňovej analýzy namáhania lisovacej formy:**

V prípade viacstupňovej analýzy napätia v lisovacej forme, ak objekt vyžaduje polohovanie, musí používateľ určiť, ako má byť objekt polohovaný v nasledujúcich krokoch, a to zaškrtnutím políčka „Potreba polohovania“ na stránke objektu, ako je znázornené na obr. 2DDSL2.1.

  * Ak je objekt súčasťou nominálnej konfigurácie a vyžaduje sa jeho polohovanie, musí používateľ zaškrtnúť políčko „Vyžaduje sa polohovanie“ a z nominálnej konfigurácie vybrať príslušný objekt ako „Nasledujúci objekt“.

  * Ak objekt nie je súčasťou nominálnej konfigurácie, ale nachádza sa v ohraničujúcom obdĺžniku objektu nominálnej konfigurácie a vyžaduje polohovanie, musí používateľ zaškrtnúť políčko „Vyžaduje polohovanie“ a z nominálnej konfigurácie vybrať príslušný objekt, v ktorého ohraničujúcom obdĺžniku sa aktuálny objekt nachádza, ako „Nasledujúci objekt“. Zaškrtávacie políčko „Nie je pôvodný objekt“ by sme nemali zaškrtávať, aby sa na aktuálny objekt mohla uplatniť funkcia „Vynútiť interpoláciu z nominálnej konfigurácie“.

  * Ak objekt nie je súčasťou nominálnej konfigurácie, nenachádza sa v ohraničujúcom obdĺžniku žiadneho z objektov nominálnej konfigurácie a vyžaduje polohovanie, musí používateľ zaškrtnúť políčko „Vyžaduje polohovanie“ a vybrať objekt z nominálnej konfigurácie, s ktorým je aktuálny objekt v kontakte, alebo ho určiť ako „Nasledujúci objekt“. Mali by sme tiež zaškrtnúť políčko „Nie je pôvodný objekt“. Ak používateľ zaškrtne políčko „Nie je pôvodný objekt“ pre daný objekt, na tento objekt sa nebude vykonávať interpolácia sily.

  
Na nastavenie analýzy napätia v matrici v niekoľkých krokoch budeme používať projekt „Stub Shaft“, ktorý bol vytvorený počas cvičenia [Lab 25 Stub Shaft]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/' | relative_url }}) v rámci laboratórnych cvičení z jazyka MO Basic.

## Nastavenie projektu „Nominal“

Nastavte [Lab 25 Stub Shaft]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/' | relative_url }}) v prostredí MO Basic Labs. Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}). (Pozri obr. 2DDSL2.2.)

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0001.jpg' | relative_url }})

Simulačný monitor zobrazujúci koniec laboratórnej simulácie hriadeľa „Stub Shaft“.

##  Pridanie analýzy napätia v matici

V ľavom hornom rohu okna „Display“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) a vyberte operáciu „Add Die stress Study“, ako je znázornené na obr. 2DDSL2.3. V zobrazovacej oblasti sa pridá karta operácie Štúdia napätia čipu a dlaždica operácie Napätie čipu bude k dispozícii v editore operácií v rámci novej karty, ako je znázornené na obr. 2DDSL2.4.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0002.jpg' | relative_url }})

Pridanie operácie „Analýza napätia v lisovacej forme“.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0003.jpg' | relative_url }})

Zobrazenie operácie „Analýza napätí v lisovacej matrici“.

## Výber kroku

Keďže chceme analyzovať napätia vo viacerých krokoch operácie, vyberte ako typ výberu napätia v lisovacej forme prepínač „**Viac krokov**“. Vyberte rádio tlačidlo „**Načítať kroky z databázy**“, aby sa načítali údaje o objekte z prvého kroku vybraných krokov, a pomocou rádio tlačidla „**Definované používateľom**“ vyberte kroky 10, 25, 45, 65, 85 a 96 operácie „Cone“ na stránke výberu krokov, aby ste mohli analyzovať napätia v týchto krokoch, ako je znázornené na obr. 2DDSL2.5. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0004.jpg' | relative_url }})

Výber viacerých krokov operácie „Cone“ na analýzu napätí v lisovacích formách.

## Definícia objektov pre analýzu napätia v matrici

Keďže analýzu napätia v lisovacej forme musíme vykonať len na razníku a spodnej matrici, zvyšné objekty odstránime. Na stránke s objektmi odstráňte objekt „Ejector“, ako je znázornené na obr. 2DDSL2.6. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0005.jpg' | relative_url }})

Odstránenie nepotrebných objektov na stránke „Objekty“.

## Definícia pojmu „punch“ 

### Definovanie údajov objektu Punch

V predvolenom nastavení sa typ tuhých objektov z načítaného kroku zmení na pružný. Pre objekt Punch ponechajte typ objektu ako pružný. Keďže tento objekt existuje v nominálnej prevádzke a vyžaduje polohovanie v budúcich krokoch, zaškrtnite políčko Potrebné polohovanie a z roletového menu vyberte objekt Punch z nominálnej prevádzky ako Nasledujúci objekt, ako je znázornené na obr. 2DDSL2.7. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka Sieť.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0019.jpg' | relative_url }})

Stránka objektu „Punch“

### Vytvorenie siete pre Punch

Na vytvorenie siete nastavte cieľový počet prvkov na 2500, ako je znázornené na obr. 2DDSL2.8, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Material“ (Materiál).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0006.jpg' | relative_url }})

Nastavenia siete pre nástroj „Punch“.

### Priradenie materiálu k dieru

Naimportujte materiál AISI-D3 z knižnice materiálov. Zo zoznamu vyberte **AISI-D3**, aby ste tento materiál priradili k dielu „Punch“, ako je znázornené na obr. 2DDSL2.9. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Okrajové podmienky“.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0007.jpg' | relative_url }})

Priradenie materiálu k programu Punch.

### Priradenie okrajových podmienok k výrezu

Musíme na teleso „Punch“ aplikovať okrajové podmienky, aby neodletelo do vesmíru, keď naň pôsobia zaťaženia pri tvárnení. V predvolenom nastavení sú pri osovo symetrickom výrobku všetky uzly pozdĺž osi x na stredovej línii pevné; ak tomu tak nie je, uistite sa, že smer okrajovej podmienky je nastavený na X, a potom kliknite na stredovú líniu pomocou tlačidla „By edge ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }})“ z možností výberu. Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) z možností výberu môžeme pridať BCC ku všetkým uzlom/prvkom na hrane. Vyberte bod na stredovej osi dielu Punch a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). Mali by ste vidieť, že všetky uzly na stredovej osi sú zafixované v smere X. 

  
Teraz, aby ste nastavili okrajovú podmienku v smere osi Y, vyberte hornú plochu razníka pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) z možností výberu, čím zafixujete všetky uzly v smere osi Y, a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). (Pozri obr. 2DDSL2.10.) Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) otvoríte stránku „Vynútiť interpoláciu“.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0008.jpg' | relative_url }})

Priradenie okrajových podmienok k programu Punch.

### Interpolácia sily z polotovaru a plánovanie interpolácie

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) vykonajte interpoláciu síl pôsobiacich na matrice zo strany polotovaru; po dokončení interpolácie by sa mala na stránke „Interpolácia síl“ zobraziť správa porovnávajúca sily pôsobiace zo strany polotovaru s novými silami pôsobiacimi na razník, ako je znázornené na obr. 2DDSL2.11. Tieto sily by mali byť relatívne blízko seba. 

Keďže simulujeme viacero krokov, musíme naplánovať interpoláciu síl z polotovaru. Na to zaškrtnite políčko vedľa položky „Interpolácia sily“ a hodnotu tolerancie ponechajte na „0“, aby sa tolerancia pre interpoláciu vypočítala automaticky. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali spodnú maticu.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0009.jpg' | relative_url }})

Interpolované sily pôsobiace na razník zo surového materiálu.

## Definícia spodnej formy

### Definovanie údajov objektu spodnej matrice

Pre spodnú matricu ponecháme typ objektu „Elastic“. Zaškrtnite políčko „Need positioning“ a z roletového menu „Following object“ vyberte „Bottom Die“ z objektov nominálnej databázy, ako je znázornené na obr. 2DDSL2.12. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Mesh“, a vygenerujte sieť.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0020.jpg' | relative_url }})

Stránka objektu „Spodná matrica“

### Vytvorenie siete pre spodnú formu

Nastavte cieľový počet prvkov na 2500, ako je znázornené na obr. 2DDSL2.13, a vygenerujte sieť; potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Material“.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0010.jpg' | relative_url }})

Nastavenia sieťoviny pre spodnú matricu.

### Priradenie materiálu k spodnej matrici

Na stránke „Materiál“ vyberte zo zoznamu položku „AISI-D3“, čím priradíte materiál pre spodnú formu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Okrajové podmienky“.

###  Priradenie okrajových podmienok spodnej formy

Ďalej musíme na spodnú matricu aplikovať okrajové podmienky, aby neodletela do vesmíru, keď na ňu pôsobia formovacie zaťaženia.

Teraz nastavte smer okrajovej podmienky na os Y, vyberte spodný okraj spodnej formy, aby ste zafixovali všetky uzly v smere osi Y. (Pozri obr. 2DDSL2.14.) a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). Keďže ide o osovo symetrickú konfiguráciu, smer X je už obmedzený; ak nie je, obmedzte uzly stredovej línie v smere X podobne ako v smere Y na spodnom okraji. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Force interpolation“ (Vynútiť interpoláciu).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0011.jpg' | relative_url }})

Priradenie okrajových podmienok spodnej formy.

### Interpolácia sily z polotovaru a plánovanie interpolácie

Po vytvorení siete je potrebné interpolovať formovacie zaťaženia zo sochoru na spodnú matricu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}). Po interpolácii síl by sa na stránke Interpolácia síl mala zobraziť správa porovnávajúca sily pôsobiace na sochársku surovinu s novými silami pôsobiacimi na spodnú formu, ako je znázornené na obr. 2DDSL2.15. Tieto sily by mali byť relatívne blízko pri sebe. 

Ak chcete naplánovať interpoláciu sily pre nasledujúce kroky analýzy napätia v lisovacej forme, zaškrtnite políčko vedľa položky „Interpolácia sily“ a hodnotu „Tolerancia“ ponechajte na „0“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno Ovládacie prvky simulácie.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0012.jpg' | relative_url }})

Interpolované sily pôsobiace na spodnú matricu zo sochoru 

## Definovanie ovládacích prvkov simulácie

Nastavte počet krokov na hodnotu 2 a ostatné nastavenia ponechajte v predvolenom stave, ako je znázornené na obr. 2DDSL2.16. Tieto nastavenia sa budú používať aj v ďalších krokoch analýzy napätia čipu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0015.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre analýzu napätia v výlisku

## Vytvorenie databázy

Na stránke „DB Generation“ skontrolujte, či v nastaveniach nie sú chyby, a vygenerujte databázu. Po vygenerovaní databázy prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

## Spustenie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spustení) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) sa spustí simulácia.

Po dokončení simulácie všetkých krokov analýzy napätia v lisovacej forme sa v súbore protokolu zobrazí správa „MULTIPLE OPERATION COMPLETED“, ako je znázornené na obr. 2DDSL2.17. Pre zobrazenie výsledkov prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0016.jpg' | relative_url }})

Protokolový súbor zobrazujúci koniec simulácie pre všetky vybrané kroky analýzy napätia v matrici

## Následné spracovanie výsledkov simulácie

Každý vybraný krok sa zobrazí ako samostatná operácia s názvom „Od kroku XX“ (XX je číslo vybraného kroku). Hlavnými premennými, na ktoré je potrebné pri simulácii napätia v výlisku venovať pozornosť, sú efektívne napätie a maximálne hlavné napätie.  
  
Efektívne napätie sa používa na zistenie, či v niektorej časti formy došlo k plastickej deformácii. Ak má akákoľvek oblasť formy efektívne napätie blízke medze tečnosti materiálu formy alebo ju prekračujúce, hrozí v tejto oblasti plastická deformácia. (Pozri obr. 2DDSL2.18.)  
  
Maximálne hlavné napätie sa používa na zistenie, ktoré oblasti matrice sú v stave stlačenia a ktoré v stave ťahu. Maximálne hlavné napätie je mimoriadne dôležité pri určovaní, či na matrici dôjde k prasknutiu v dôsledku únavy materiálu. Ak chcete zobraziť maximálne hlavné napätie, kliknite na tlačidlo „Nastaviť“ pre stavovú premennú ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) a potom zo zoznamu vyberte možnosť Napätie – Maximálne hlavné. (Pozri obr. 2DDSL2.19.)

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0017.jpg' | relative_url }})

Rozloženie efektívneho napätia na konci posledného kroku analýzy napätia v matrici pri operácii „Cone“

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0018.jpg' | relative_url }})

Rozloženie maximálneho hlavného napätia na konci posledného kroku analýzy napätí v matrici pri operácii „Cone“

[2D Die Stress Study with Single step]({{ '/docs/sk/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/' | relative_url }})

[49.1. 2D Die Stress Study]({{ '/docs/sk/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/' | relative_url }})
