---
lang: sk
title: "Štúdia napätia v 2D s jedným krokom"
---

# Laboratórna úloha 1: Analýza napätí v 2D pomocou štúdie napätí v jednom kroku 

Analýzu napätia v lisovacej forme je možné nastaviť pomocou štúdie „Die Stress“ alebo operácie „Die Stress“. Operácia „Die Stress“ slúži na nastavenie analýzy napätia v lisovacej forme v dávkovom režime; táto operácia pre analýzu preberá posledný krok z predchádzajúcej operácie.

Na nastavenie analýzy napätia v lisovacích formách použijeme projekt „Stub Shaft“, ktorý bol vytvorený počas cvičenia [Lab 25 Stub Shaft]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/' | relative_url }}) v rámci laboratórnych cvičení MO Basic. V tomto cvičení budeme vykonávať analýzu napätia v lisovacích formách v kroku, v ktorom pozorujeme maximálne zaťaženie pri operáciách „Cone“ a „Head“. Keďže potrebujeme analyzovať dve rôzne fázy z dvoch rôznych operácií, pre každú z nich použijeme analýzu napätia v lisovacích nástrojoch samostatne. Pri typickej simulácii napätia v lisovacích nástrojoch sa obrobok odstráni a sily, ktoré obrobok pôsobí na lisovacie nástroje, sa interpolujú na nástroje. 

1.1. Nastavenie projektu „Nominal“

1.2. Nastavenie analýzy napätia v lisovacej forme1

1.2.1. Pridanie analýzy napätia v lisovacej forme

1.2.2. Výber kroku

1.2.3. Definícia objektov pre štúdiu napätia v matrici 1

1.2.4. Definícia úderu

1.2.4.1. Definícia objektu „Punch“

1.2.4.2. Vytvorenie siete pre Punch

1.2.4.3. Priradenie materiálu k dierovaču

1.2.4.4. Priradenie okrajových podmienok k výrezu

1.2.4.5. Interpolácia sily z polotovaru

1.2.5. Definícia spodnej matrice

1.2.5.1. Definícia objektu „spodná matrica“

1.2.5.2. Vytvorenie siete pre spodnú formu

1.2.5.3. Priradenie materiálu pre spodnú matricu

1.2.5.4. Priradenie okrajových podmienok spodnej formy

1.2.5.5. Interpolácia sily z polotovaru

1.2.6. Definovanie ovládacích prvkov simulácie

1.2.7. Vytvorenie databázy

1.2.8. Spustenie simulácie

1.2.9. Následné spracovanie výsledkov simulácie v rámci štúdie napätí v lisovacej forme1

1.3. Nastavenie analýzy napätia v matrici 2

1.3.1. Pridanie druhej analýzy napätia v matrici

1.3.2. Výber kroku

1.3.3. Definícia objektov pre analýzu napätia v lisovacej forme 2

1.3.4. Definícia úderu

1.3.4.1. Definícia objektu „Punch“

1.3.4.2. Vytvorenie siete pre Punch

1.3.4.3. Priradenie materiálu pre dierovačku

1.3.4.4. Priradenie okrajových podmienok k výrezu

1.3.4.5. Interpolácia sily z polotovaru

1.3.5. Definícia spodnej matrice

1.3.5.1. Definícia objektu „spodná matrica“

1.3.5.2. Vytvorenie siete pre spodnú formu

1.3.5.3. Priradenie materiálu pre spodnú formu

1.3.5.4. Priradenie okrajových podmienok spodnej formy

1.3.5.5. Interpolácia sily z polotovaru

1.3.6. Definovanie ovládacích prvkov simulácie

1.3.7. Vytvorenie databázy

1.3.8. Spustenie simulácie

1.3.9. Následné spracovanie výsledkov simulácie v rámci štúdie napätí v lisovacej forme 2

## Nastavenie projektu „Nominal“

Nastavte [ Lab 25 Stub Shaft]({{ '/docs/sk/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/' | relative_url }}) v programe MO Basic Labs. Prejdite na ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) a vykreslite krivku zaťaženia v závislosti od zdvihu (pozri obr. 2DDSL1.1); môžeme pozorovať, že zaťaženie dosahuje maximum v poslednom kroku operácií „Cone“ a „Head“. Teraz vykonáme analýzu napätia v matrici v poslednom kroku operácie „Cone“. Prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) a pridajte operáciu „Die Stress study“ (Analýza napätia v matrici). 

  
![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0001.jpg' | relative_url }})

Graf zaťaženia a zdvihu pri operáciách s kužeľom a hlavou z projektu „Stub Shaft“

## Nastavenie analýzy napätia v matrici 1

### Pridanie analýzy napätia v matrici

V ľavom hornom rohu okna zobrazenia kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) a vyberte operáciu „Add Die Stress Study“, ako je znázornené na obr. 2DDSL1.2. Do zobrazovacej oblasti sa pridá karta operácie „Die Stress Study“ a dlaždica operácie „Die Stress“ bude k dispozícii v editore operácií na novej karte, ako je znázornené na obr. 2DDSL1.3.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0002.jpg' | relative_url }})

Pridanie operácie „Analýza napätia v matrici“.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0003.jpg' | relative_url }})

Zobrazenie operácie „Analýza napätia v lisovacej matrici“.

###  Výber kroku

Keďže potrebujeme analyzovať napätie v matrici iba v poslednom kroku operácie „Cone“, vyberte typ výpočtu napätia v matrici „**One step**“ a zaškrtnite políčko „**Load step from DB**“, aby sa načítali objekty z vybraného kroku. Na stránke Výber kroku vyberte posledný krok operácie „Cone“, ako je znázornené na obr. 2DDSL1.4. Údaje všetkých objektov z vybraného kroku sa načítajú do zobrazenia. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0004.jpg' | relative_url }})

Krok výberu pre analýzu napätia v lisovacej forme 1.

### Definícia objektov pre štúdiu napätia v matrici 1

Keďže analýzu napätia v lisovacej forme musíme vykonať len na razníku a spodnej forme, odstránime ostatné objekty. Na stránke s objektmi odstráňte objekt „Ejector“, ako je znázornené na obr. 2DDSL1.5. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0005.jpg' | relative_url }})

Odstránenie nepotrebných objektov na stránke „Objekty“.

### Definícia pojmu „punch“

#### Definícia objektu „Punch“

V predvolenom nastavení sa typ tuhých objektov z načítaného kroku zmení na pružný. Pre objekt „Punch“ ponechajte typ objektu ako pružný. Od verzie v13.1.1 boli na stránke objektov zavedené dve nové možnosti na umiestnenie matíc v budúcich krokoch pre analýzu napätia matíc vo viacerých krokoch; pre analýzu napätia matíc v jednom kroku tieto možnosti nemusíme používať, preto nechajte políčko „Need positioning“ (Potreba umiestnenia) nezaškrtnuté, pozri obr. 2DDSL1.6. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Mesh“ (Sieť).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0028.jpg' | relative_url }})

Stránka objektu „Punch“

#### Vytvorenie siete pre Punch

Nastavte cieľový počet prvkov na 2500, ako je znázornené na obr. 2DDSL1.7, a vytvorte sieť pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Potom klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Material“.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0006.jpg' | relative_url }})

Nastavenia siete pre nástroj „Punch“.

#### Priradenie materiálu k stroju Punch

Načítajte materiál AISI-D3 z knižnice materiálov. Zo zoznamu vyberte **AISI-D3**, aby ste tento materiál priradili k dierovaču, ako je znázornené na obr. 2DDSL1.8. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Okrajové podmienky“.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0007.jpg' | relative_url }})

Priradenie materiálu k programu Punch.

#### Priradenie okrajových podmienok k výrezu

Musíme na teleso „Punch“ aplikovať okrajové podmienky, aby neodletelo do vesmíru, keď naň pôsobia zaťaženia pri tvárnení. V predvolenom nastavení sú pre osovo symetrický výrobok všetky uzly pozdĺž smeru x na stredovej osi fixované; ak tomu tak nie je, uistite sa, že smer okrajovej podmienky je nastavený na X, a potom kliknite na stredovú os pomocou tlačidla „By edge ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }})“ z možností výberu. Vyberte bod na stredovej osi dielu Punch a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). Mali by ste vidieť, že všetky uzly na stredovej osi sú fixované v smere osi X.

  
Teraz, aby ste nastavili okrajovú podmienku v smere osi Y, vyberte hornú plochu razníka pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) z možností výberu, čím zafixujete všetky uzly v smere osi Y, a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). (Pozri obr. 2DDSL1.9.) Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Vynútiť interpoláciu.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0008.jpg' | relative_url }})

Priradenie okrajových podmienok k programu Punch.

#### Vynútená interpolácia z polotovaru

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) vykonajte interpoláciu síl, ktoré na matrice pôsobí sochár, a po dokončení interpolácie by sa mala zobraziť správa porovnávajúca sily pôsobiace zo sochára s novými silami pôsobiacimi na razník na stránke „Interpolácia síl“, ako je znázornené na obr. 2DDSL1.10. Tieto sily by mali byť relatívne blízko pri sebe. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali spodnú matricu.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0009.jpg' | relative_url }})

Interpolované sily pôsobiace na razník zo sochoru.

### Definícia spodnej matrice

#### Definícia objektu „Spodná matrica“

Pre spodnú formu ponecháme typ objektu ako „Elastic“ a zrušíme zaškrtnutie políčka „Need positioning“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Mesh“, kde vytvoríte sieť.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0029.jpg' | relative_url }})

#### Vytvorenie siete pre spodnú formu

Nastavte cieľový počet prvkov na 2500, ako je znázornené na obr. 2DDSL1.11, a vygenerujte sieť. Následne klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Material“ (Materiál).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0010.jpg' | relative_url }})

Nastavenia sieťoviny pre spodnú formu.

#### Priradenie materiálu pre spodnú matricu

Na stránke „Materiál“ vyberte zo zoznamu položku **AISI-D3**, aby ste priradili materiál pre spodnú formu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na okrajové podmienky.

#### Priradenie okrajových podmienok spodnej formy

Na spodnú formu musíme aplikovať okrajové podmienky, aby neodletela do vesmíru, keď na ňu pôsobia formovacie zaťaženia.  
  
Teraz nastavte smer okrajovej podmienky na os Y, vyberte bod na spodnej ploche spodnej formy, čím zafixujete všetky uzly v smere osi Y. (Pozri obr. 2DDSL1.12.) Keďže ide o osovo symetrickú konfiguráciu, smer osi X je už obmedzený. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Interpolácia síl.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0011.jpg' | relative_url }})

Priradenie okrajových podmienok spodnej formy.

#### Vynútená interpolácia z polotovaru

Po vytvorení siete je potrebné interpolovať zaťaženia vznikajúce pri tvárnení zo surového polotovaru na spodnú matricu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}). Po interpolácii síl by sa mala na stránke Interpolácia síl zobraziť správa porovnávajúca sily pôsobiace na sochoru s novými silami pôsobiacimi na spodnú formu, ako je znázornené na obr. 2DDSL1.13. Tieto sily by mali byť relatívne blízko pri sebe. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno „Simulation controls“.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0012.jpg' | relative_url }})

Interpolované sily pôsobiace na spodnú matricu zo sochoru.

### Definovanie ovládacích prvkov simulácie

Nastavte počet krokov na hodnotu 2 a ostatné nastavenia ponechajte v predvolenom stave, ako je znázornené na obr. 2DDSL1.14. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0013.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre štúdiu napätia v matrici 1.

###  Vytvorenie databázy

Na stránke „DB Generation“ skontrolujte, či v nastaveniach nie sú žiadne chyby, a vygenerujte databázu. Po vygenerovaní databázy prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

### Spustenie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spustení) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) sa spustí simulácia. Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

### Následné spracovanie výsledkov simulácie v rámci štúdie napätí v lisovacej forme1

Hlavnými veličinami, na ktoré je potrebné sa zamerať pri simulácii napätia v tvárnici, sú efektívne napätie a maximálne hlavné napätie.  
  
Efektívne napätie sa používa na zistenie, či v niektorej časti lisovacej formy došlo k plastickej deformácii. Ak má akákoľvek oblasť lisovacej formy efektívne napätie blízke medze tečnosti materiálu formy alebo ju presahujúce, v tejto oblasti hrozí riziko plastickej deformácie. (Pozri obr. 2DDSL1.15.)  
  
Maximálne hlavné napätie sa používa na zistenie, ktoré oblasti formy sú v stave stlačenia a ktoré v stave ťahu. Maximálne hlavné napätie je mimoriadne dôležité pri určovaní, či na matici dôjde k prasknutiu v dôsledku únavy materiálu. Ak chcete zobraziť maximálne hlavné napätie, kliknite na tlačidlo „Nastaviť“ pre stavovú premennú ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) a potom zo zoznamu vyberte možnosť Napätie – Maximálne hlavné. (Pozri obr. 2DDSL1.16.)

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0014.jpg' | relative_url }})

Rozloženie efektívneho napätia v poslednom kroku pri prevádzke kužeľových lisovacích foriem.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0015.jpg' | relative_url }})

Rozloženie maximálneho hlavného napätia v poslednom kroku operácie „Dies of Cone“.

## Nastavenie štúdie napätia v matrici 2

Po dokončení následného spracovania štúdie napätia v matrici1 prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}).

### Pridanie druhej štúdie o namáhaní čipu

Na konci operácie „Head“ pridáme ďalšiu operáciu „Die Stress Study“ na analýzu napätí v matrici. V ľavom hornom rohu okna zobrazenia kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) a vyberte operáciu „Add Die Stress Study“, ako je znázornené na obr. 2DDSL1.17. V zobrazovacej oblasti sa pridá druhá karta operácie „Die Stress Study“ a v editore operácií na novej karte bude k dispozícii dlaždica operácie „Die Stress“, ako je znázornené na obr. 2DDSL1.17.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0016.jpg' | relative_url }})

Pridanie druhej operácie na analýzu napätia v lisovacej matrici.

### Výber kroku

Ak chcete na konci operácie „Head“ vykonať operáciu „Die stress“, vyberte možnosť „**Načítať krok z databázy**“ a následne na stránke výberu krokov vyberte posledný krok druhej operácie, ako je znázornené na obr. 2DDSL1.18. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0017.jpg' | relative_url }})

Výber kroku pre štúdiu napätia v lisovacej forme 2.

###  Definícia objektov pre analýzu napätia v lisovacej forme 2

Keďže analýzu napätia v lisovacej forme musíme vykonať len na razníku a spodnej forme, ostatné objekty odstránime. Na stránke objektov odstráňte objekt vyhadzovača, ako je znázornené na obr. 2DDSL1.19. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0018.jpg' | relative_url }})

Odstránenie nepotrebných objektov na stránke „Objekty“.

### Definícia pojmu „punch“

#### Definícia objektu „Punch“

Typ objektu „Punch“ je štandardne nastavený na „Elastic“; tento výber ponecháme a zrušíme zaškrtnutie políčka „Need positioning“, ako je znázornené na obr. 2DDSL1.6. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Mesh“.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0028.jpg' | relative_url }})

#### Vytvorenie siete pre Punch

Nastavte cieľový počet prvkov na 2500, ako je znázornené na obr. 2DDSL1.20, vygenerujte sieť a potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Material“.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0019.jpg' | relative_url }})

Nastavenia siete pre operáciu „Punch in Head“.

#### Priradenie materiálu pre dierovačku

Naimportujte materiál formy AISI-D3 z knižnice materiálov. Zo zoznamu vyberte **AISI-D3**, aby ste tento materiál priradili k razníku. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Okrajové podmienky“.

#### Priradenie okrajových podmienok k výrezu

Na razník musíme aplikovať okrajové podmienky, aby pri pôsobení tvárniacich síl neodletel do vesmíru. Kliknite na tlačidlo „Podľa hrany“ ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) v ponuke výberu a vyberte bod na hornej ploche razníka, aby ste zafixovali všetky uzly v smere Y, a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). Keďže ide o osovo symetrické usporiadanie, smer X je už obmedzený; ak nie je, obmedzte smer X podobne ako smer Y pozdĺž stredovej osi razníka. (Pozri obr. 2DDSL1.21.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Vynútiť interpoláciu.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0020.jpg' | relative_url }})

Punch – Okrajové podmienky.

#### Vynútená interpolácia z polotovaru

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}). Akonáhle sa sily interpolujú, na stránke „Interpolácia síl“ by sa mala zobraziť správa porovnávajúca sily pôsobiace na polotovar s novými silami pôsobiacimi na razník, ako je znázornené na obr. 2DDSL1.22. Tieto sily by mali byť relatívne blízko pri sebe. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0021.jpg' | relative_url }})

Interpolované sily pôsobiace na razník zo sochoru.

### Definícia spodnej matrice

#### Definícia objektu „Spodná matrica“

Typ objektu „Spodná matrica“ je štandardne nastavený na „Elastický“; tento výber ponecháme a zrušíme zaškrtnutie políčka „Vyžadovať polohovanie“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Mriežka“.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0029.jpg' | relative_url }})

#### Vytvorenie siete pre spodnú maticu

Nastavte cieľový počet prvkov na 2500, ako je znázornené na obr. 2DDSL1.23, a vygenerujte sieť, potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí okno „Material“.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0022.jpg' | relative_url }})

Nastavenia siete pre spodnú formu.

#### Priradenie materiálu pre spodnú matricu

Na stránke „Materiál“ vyberte zo zoznamu položku **AISI-D3**, aby ste priradili materiál pre spodnú formu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Okrajové podmienky“.

####  Priradenie okrajových podmienok spodnej formy

Na spodnú matricu musíme aplikovať okrajové podmienky, aby neodletela do vesmíru, keď na ňu pôsobia tvárniace zaťaženia.  
Teraz nastavte smer okrajovej podmienky na os Y, vyberte bod na spodnej ploche prvku „Bottom“, aby ste zafixovali všetky uzly v smere osi Y, a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). (Pozri obr. 2DDSL1.24.) Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vynúťte interpoláciu.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0023.jpg' | relative_url }})

Okrajové podmienky spodnej formy.

#### Vynútená interpolácia z polotovaru

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}). Po interpolácii síl by sa mala na stránke „Force interpolation“ (Interpolácia síl) zobraziť správa porovnávajúca sily pôsobiace na polotovar s novými silami pôsobiacimi na spodnú maticu, ako je znázornené na obr. 2DDSL1.25. Tieto sily by mali byť relatívne blízko pri sebe. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka ovládacích prvkov simulácie.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0024.jpg' | relative_url }})

Sily prenesené z polotovaru na spodnú formu.

### Definovanie ovládacích prvkov simulácie

Nastavte počet krokov na 2 a ostatné nastavenia ponechajte v predvolenom stave, ako je znázornené na obr. 2DDSL1.26. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0025.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie pre štúdiu napätia v matrici 2.

### Vytvorenie databázy

Skontrolujte údaje a vytvorte databázu. Po vytvorení databázy prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

### Spustenie simulácie

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spustení) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. Po kliknutí na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) sa spustí simulácia. Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}).

### Následné spracovanie výsledkov simulácie v rámci štúdie napätí v lisovacej forme 2

Hlavnými veličinami, ktoré treba zohľadniť pri simulácii napätia v lisovacej matrici, sú efektívne napätie a maximálne hlavné napätie.

Rozloženie efektívneho napätia v lisovacích formách v poslednom kroku analýzy napätia v lisovacích formách je znázornené na obr. 2DDSL1.27.

Rozloženie maximálneho hlavného napätia v lisovacích formách v poslednom kroku analýzy napätia v lisovacích formách je znázornené na obr. 2DDSL1.28.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0026.jpg' | relative_url }})

Rozloženie efektívneho napätia v poslednom kroku operácie lisovania hlavy. 

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0027.jpg' | relative_url }})

Rozloženie maximálneho hlavného napätia v poslednom kroku operácie „Dies of Cone“.

[2D Die Stress Study with Single step]()

[49.1. 2D Die Stress Study]({{ '/docs/sk/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/' | relative_url }})
