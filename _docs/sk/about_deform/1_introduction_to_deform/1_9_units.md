---
lang: sk
title: "1.9. Jednotky"
---

# 1.9. Jednotky

Údaje DEFORM sa môžu poskytovať v ľubovoľnej sústave jednotiek, pokiaľ sú všetky premenné konzistentné (t. j. merania dĺžky, sily, času a teploty sú v rovnakých jednotkách a všetky odvodené jednotky - napríklad rýchlosť - sú odvodené z rovnakých základných jednotiek). Túto úlohu možno zjednodušiť použitím britskej sústavy alebo sústavy SI pre predvolenú sústavu jednotiek (pozri nasledujúcu tabuľku 1.9.1.).

**Premenné** | **SI** | **Eng** | **Konverzný faktor
(SI ****→****Eng)**
---|---|---|---
**Plocha** | **mm^2** | **in^2** | 0,001550003
**Hustota sily telesa/hmotnosť (![]({{ '/assets/icons/pre_icons/rho_symbol.jpg' | relative_url }}) *g)** | **N/mm^3** | **klbf/in^3** | 3,684
**Modul pevnosti** | **MPa** | **ksi** | 0,145037681
**Ostredivá sila (![]({{ '/assets/icons/pre_icons/rho_symbol.jpg' | relative_url }}) *Ω^2 )** | **N/mm^4** | **klbf/in^4** | 93,5725
**Hrubosť povlaku** | **mikróny** | **mikróny** | ****
**Koeficient konvekcie** | **N/sec/mm/°C** | **Btu/sec/in^2/°F** | 0,000339789
**Hustota prúdu** | **A/mm^2** | **A/in^2** | 645,16
**Koeficient difúzie** | **mm^2/sekundu** | **in^2/sekundu** | 0,001550003
**Vzdialenosť / dĺžka** | **mm** | **in** | 0,039370079
**Intenzita elektrického poľa** | **V/mm** | **V/in** | 25,4
**Elektrický výkon 1** | **W** | **W** |
**Elektrická permitivita** | **farad/mm** | **farad/in** |
**Elektrický odpor (materiálu)** | **ohm-mm** | **ohm**-** in** | 0,039370079
**Elektrický odpor rozhrania** | **ohm-mm^2** | **ohm-in^2** | 0,001550003
**Intenzita magnetického poľa** | **A/mm** | **A/in** |
**Magnetická permeabilita** | **H/mm** | **H/in** |
**Relatívna magnetická permeabilita** | **magnetická permeabilita / magnetická permeabilita vákua** |
**Relatívna elektrická permitivita** | **elektrická permitivita / elektrická permitivita vákua** |
**Sila** | **N** | **klbf** | 0.000224809
**Frekvencia** | **Hz** | **Hz** |
**Veľkosť zrna** | **mikróny** | **mikróny** |
**Tepelná kapacita** | **N/mm^2/°C** | **Btu/in^3/°F** | 0,008628872
**tepelná energia** | **N-mm** | **Btu** | 9,47867E-07
**Rýchlosť tepelného toku** | **N/mm/sek** | **Btu/in^2/sek** | 1635,3
**Koeficient prestupu tepla na rozhraní** | **N/sec/mm/°C** | **Btu/sec/in^2/°F** | 0,000339789
**Hmotnosť** | **N**-** s^2/mm** | **klbf-s^2/in** | 0,005710148562313
**Hustota hmotnosti (![]({{ '/assets/icons/pre_icons/rho_symbol.jpg' | relative_url }}))** | **ton/mm^3** | **klbf-s^2/in^4** | 93,5725
**Masové merné teplo** | **N**-** mm/tonu-°C ** | **Btu**-** in/klbf**-** s^2**-°** F ** | 9,2216E-5
**Mechanická energia** | **N-mm** | **klbf-in** | 8,84956E-06
**Tlak; napätie; Youngov modul** | **MPa** | **Ksi** | 0,145037681
**Relatívna hustota** | **hustota materiálu / hustota úplne hustého materiálu** | 1
**Dĺžka ťahu** | **mm/mm** | **in/in** | 1
**Rýchlosť ťahu** | **(mm/mm)/sekundu** | **(in/in)/sekundu** | 1
**Teplota** | **°C** | **°F** | (°C * 1,8) + 32
**Tepelná vodivosť** | **N/sec/°C** | **Btu/sec/in/°F** | 1,33754E-05
**Koeficient tepelnej rozťažnosti** | **1/°C** | **1/**°** F** | 0,555556
**čas** | **sek** | **sek** | 1
**krútiaci moment** | **N-mm** | **klb-in** | 8,85075E-06
**Univerzálna plynová konštanta** | **J/(mol-K)** | **J/(mol-°F)** | 0,555556
**Rýchlosť** | **mm/sec** | **in/sec** | 0,039370079
**Napätie** | **V** | **V** | ****
**Objem** | **mm^3** | **in^3** | 6,1024E-05
  
Systém jednotiek DEFORM

Na začiatku simulácie je dôležité vybrať jednotkový systém. Po zadaní číselných hodnôt v predprocesore zostane číselná hodnota nezmenená, aj keď sa zmení označenie jednotkovej sústavy.

Postprocesor bol vybavený funkciou na konverziu jednotiek pre zobrazenie databázy (pozri [Fig. 26.5.6.](../../post_processor/26_post_processing_tools_and_controls/26_5_post_processing_options.htm#Fig_26_4_6_Unit_Conversion) ). Používateľ má k dispozícii štyri možnosti prepočtu jednotiek. Ak je zvolený konverzný faktor Default (Predvolené), potom sa jednotky vyberú automaticky v závislosti od toho, či je databáza anglická alebo SI. Keďže nie je potrebný žiadny prevod, všetky konverzné faktory sú v tomto stĺpci nastavené na 1,0. V prípadoch konverzie z angličtiny na SI alebo konverzie zo SI na angličtinu sa konverzné faktory a jednotky vyberú z dialógového okna a hodnoty sa prepočítajú a zobrazia v postprocesore. Štvrtá možnosť dáva používateľovi možnosť zobraziť údaje z databázy v jednotkách, ktoré nie sú anglické alebo SI. Používateľ môže voľne zadať konverzné faktory a jednotky zodpovedajúce konverzným faktorom.

Pre teplotu neexistuje žiadny používateľský typ prevodu jednotiek, pretože prevod teploty nie je jednoduchým násobením.

Pri práci s hustotou sa musí zachovať jednotnosť jednotiek. V nasledujúcej tabuľke sú uvedené rôzne jednotky, ktoré sa zhodujú s rôznymi definíciami hustoty.

| **JEDNOTKA1** | **JEDNOTKA2** | **JEDNOTKA3** | **JEDNOTKA4**
---|---|---|---|---
**Dĺžka** | m | mm | m | in
**Sila** | N | kN | Klbf
**Mass** | kg | kg | tona | (klbf)(s^2)/ in
**Napätie** | Pa | MPa | kPa | (ksi)
**Hustota** | kg/m^3 | tona/mm^3 | tona/m^3 | (klbf)(s^2)/ in^4
**Energia** | J | mJ | kJ | (in)(klbf)
  
Dôležité konštanty na nastavenie simulácie indukčného ohrevu:

**Magnetická priepustnosť vzduchu / vákua**

4 ![]({{ '/assets/images/about_deform/1_9_units/pi_symbol.jpg' | relative_url }})E-7 (1,26E-6 ) Henry/m

1,26E-9 Henry/mm

3,19E-8 Henryho/inch

**Prepustnosť vzduchu / vákua**

1E-9 /(36 ![]({{ '/assets/images/about_deform/1_9_units/pi_symbol.jpg' | relative_url }})) (8,85E-12 ) Farad/m

8,85E-15 Farad/mm

2,25E-13 Farad/palec

Dôležité konštanty jednotky v mobilite hraníc zrna a mikroštruktúry:

**Koeficient pohyblivosti na hranici zrna (M0)** mikrón^2/Joule

**Aktivačná energia (Q)** Joule
**Energia** Joule

**Energia rozhrania** Joule

****1** Elektrický výkon** sa uvádza vo wattoch (N-m/s) kvôli pohodliu v porovnaní s priemyselnými štandardnými jednotkami. Odchyľuje sa od štandardného systému jednotiek DEFORM (N-mm/s).

**Súvisiace témy:**

[Unit System Selection Pre-Processor](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.3._Units)

[Material Units Converter Pre-Processor](../../pre_processor/10_material_data/10_material_data.htm#Fig._10.7._Material_Unit_Convertor_window)

[Units Converter Post-Processor](../../post_processor/26_post_processing_tools_and_controls/26_5_post_processing_options.htm#26_5_6_Unit_Conversion)

[10.3.4. Mass Density](../../pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data.htm#Mass_Density)
