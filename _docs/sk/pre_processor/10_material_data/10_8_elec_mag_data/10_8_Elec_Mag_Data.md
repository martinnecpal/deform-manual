---
lang: sk
title: "10.8. Údaje Elec_Mag"
---

# 10.8. Elektrické a magnetické údaje

Elektrické a magnetické vlastnosti (pozri obr. 10.8.1.) sa tu zadávajú, ak sa má modelovať elektrické alebo elektromagnetické správanie objektu.

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_8_Elec_Mag_Data/10_8_Image001.jpg)

Okno s údajmi o elektrickom a magnetickom materiáli

## Elektrický odpor (ELRST)

Elektrický odpor je miera toho, ako sa daný materiál bráni (odoláva) toku elektrického prúdu pri aplikovanom rozdiele napätí. Elektrický odpor ([ELRST](/docs/sk/Keyword_Documentation/E/ELRST/)) je veľkosť elektrického odporu na jednotku dĺžky daného materiálu. Hodnota môže byť konštantná alebo funkcia teploty, funkcia obsahu atómov alebo funkcia teploty a obsahu atómov.

Údaje o elektrickom odpore sú potrebné pri modelovaní toku prúdu pri odporovom ohreve, bodovom zváraní, elektrickom rozrušovaní, indukčnom ohreve/tuhnutí a elektromagnetickom tvárnení.

## Relatívna magnetická permeabilita (PMEAB)

Relatívna magnetická permeabilita ([PMEAB](/docs/sk/Keyword_Documentation/P/PMEAB/)) je miera toho, ako daný materiál zvyšuje alebo znižuje hustotu magnetických tokov v objeme v porovnaní s vákuom. Možno ju vypočítať vydelením permeability objektu permeabilitou vákua. Bezrozmerný pomer by mal byť rovnaký v anglickej a SI sústave jednotiek. Hodnota môže byť konštantná alebo funkcia teploty, funkcia hustoty alebo funkcia teploty a intenzity magnetického poľa.

Údaje o relatívnej magnetickej permeabilite sú potrebné pri modelovaní magnetických polí pri indukčnom ohreve/tvrdnutí a elektromagnetickom tvárnení.

Relatívna magnetická permeabilita mnohých kovov je funkciou teploty a intenzity magnetického poľa. Materiály sa často opisujú pomocou ich počiatočných a/alebo maximálnych hodnôt relatívnej magnetickej permeability. Relatívna magnetická permeabilita magnetického materiálu (nízkouhlíková oceľ, legovaná oceľ atď.) klesá na 1 pri Curieho bode kovu, čo je teplota, pri ktorej kov stráca magnetizáciu. Nemagnetické materiály (meď, hliník atď.) a magnetické materiály nad Curieho bodom budú mať relatívnu magnetickú permeabilitu okolo 1. Relatívna magnetická permeabilita zvyčajne klesá smerom k 1 s rastúcou intenzitou magnetického poľa.

Priepustnosť vákua ([ENVMPR](/docs/sk/Keyword_Documentation/E/ENVMPR/)) sa definuje v ponuke Simulation Controls (Simulačné ovládacie prvky) > Process Conditions (Podmienky procesu). Typická hodnota je uvedená nižšie na porovnanie.

1,26 x 10-9 H/mm (SI)
3,20 x 10-8 H/in (anglicky)

## Relatívna elektrická permitivita (PMITT)

Relatívna elektrická permitivita ([PMITT](/docs/sk/Keyword_Documentation/P/PMITT/)) je elektrická polarizovateľnosť materiálu v porovnaní s polarizovateľnosťou vákua. Možno ju vypočítať vydelením permitivity objektu permitivitou vákua. Bezrozmerný pomer by mal byť rovnaký v anglickej a SI sústave jednotiek. Hodnota môže byť konštantná, funkcia teploty alebo funkcia hustoty. Zvyčajne sa odporúča hodnota 0 (ignoruje sa) alebo 1 (totožná s vákuom).

Relatívna elektrická permitivita je k dispozícii, ale používa sa len zriedka.

Priepustnosť vákua ([ENVMPT](/docs/sk/Keyword_Documentation/E/ENVMPT/)) je definovaná v ponuke Simulation Controls (Simulačné ovládacie prvky) > Process Conditions (Podmienky procesu). Typická hodnota je uvedená nižšie na porovnanie.

8,85 x 10-15 F/mm (SI)
2,25 x 10-13 F/in (anglicky)
