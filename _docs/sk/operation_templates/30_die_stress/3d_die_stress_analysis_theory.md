---
lang: sk
title: "Teória 3D analýzy napätí v čipe"
---

# Teória analýzy napätí v 3D formách

1\. Význam analýzy napätí

2\. Druhy porúch lisovacích foriem

3\. Stav stresu

4\. Analýza napätí – efektívne napätie

5\. Analýza napätí a únavové zlyhanie

6\. Príklad s maticou Stress – nízka zložitosť

7\. Príklad s Die Stress – stredná zložitosť

8\. Príklad stresového testu – vysoká zložitosť

9\. Analýza napätí v spojených čipoch

## Význam analýzy napätí

  * Kovanie spôsobuje vysoké namáhanie nástrojov a foriem.

  * Simulácia procesov sa už desaťročia využíva na analýzu porúch priemyselných foriem

  * Úspory v hodnote miliónov dolárov sa pripisujú využitiu analýzy napätia v lisovacích formách v spojení s kvalitným inžinierstvom a riadením procesov.

  * Popredné spoločnosti po celom svete optimalizujú výkonnosť nástrojov a foriem ešte predtým, ako dôjde k poruchám!

  * Prečo – cena formy priamo súvisí s jej životnosťou!

## Druhy porúch lisovacích foriem

  * Katastrofálna porucha

  * Plastická deformácia

  * Vysoká úroda

  * Lokálne tvárnenie / lisovanie

  * Únava pri nízkom počte cyklov (LCF)

  * Mechanická únava

  * Tepelná únava

  * Opotrebenie

## Stresový stav

Stav napätia v matrici a jeho zložky sú znázornené na obr. 1 a obr. 2.

![]({{ '/assets/images/operation_templates/30_die_stress/3d_die_stress_analysis_theory/image0001.jpg' | relative_url }})

Stav stresu

![]({{ '/assets/images/operation_templates/30_die_stress/3d_die_stress_analysis_theory/image0002.jpg' | relative_url }})

Zložky napätia

## Analýza napätí – efektívne napätie

  * Efektívne napätie je číselná veličina, ktorá sa používa pri prevode trojrozmerného napäťového stavu na jednorozmerné údaje na účely analýzy.

![]({{ '/assets/images/operation_templates/30_die_stress/3d_die_stress_analysis_theory/eq_1.jpg' | relative_url }})

  * Efektívne napätie je „indikátor“, ktorý signalizuje začiatok plastickej deformácie (medza tečenia).

  * Medza tečenia materiálu sa stanovuje pomocou ťahovej skúšky.

## Analýza napätí a únavové zlyhanie

  * Únava pri nízkom počte cyklov (LCF) je bežným spôsobom poruchy čipu.

  * Poruchy sa vyskytujú v štyroch fázach:

  * Začiatok zlomeniny

  * Pomaly postupujúca trhlina

  * Zrýchlená rýchlosť šírenia trhlín

  * Rýchla zlomenina

  * Maximálne hlavné napätie je dôležité, pretože k poruchám spôsobeným únavou (LCF) nemôže dôjsť bez cyklického ťahového napätia.

## Príklad „Die Stress“ – nízka zložitosť

Aby ste mohli lepšie určiť, kde by sa matrica plasticky deformovala, použite medzu tečnosti ako minimálne napätie vo vašom grafe – všetko, čo je vyfarbené, už dosiahlo medzu tečnosti, ako je znázornené na obr. 3.

![]({{ '/assets/images/operation_templates/30_die_stress/3d_die_stress_analysis_theory/image0003.jpg' | relative_url }})

Modely s nízkou zložitosťou

Maximálne hlavné napätie ukazuje, kde je výlisok vystavený ťahu alebo tlaku. Oblasti vystavené ťahu sú ohrozené únavovým zlyhaním. (Pozri obr. 4)

![]({{ '/assets/images/operation_templates/30_die_stress/3d_die_stress_analysis_theory/image0004.jpg' | relative_url }})

Maximálne hlavné napätie

## Príklad hry „Die Stress“ – stredná zložitosť

Pri použití tlakových spojov je možné získať cenné informácie vykonaním dvoch simulácií napätia v lisovacej matrici – jednej len s tlakovým spojom a druhej s tlakovým spojom aj s formovacím zaťažením. (Pozri obr. 5.)

![]({{ '/assets/images/operation_templates/30_die_stress/3d_die_stress_analysis_theory/image0005.jpg' | relative_url }})

Tepelné sťahovanie a tvarovacie zaťaženie

## Príklad Die Stress – vysoká zložitosť

Elastické výseky je potrebné prepojiť tak, aby bola sieť najjemnejšia v strede a smerom von sa zosilňovala. Na vytvorenie kontaktu medzi všetkými objektmi je potrebné definovať dvadsaťšesť vzťahov medzi objektmi. Práve to robí túto simuláciu oveľa zložitejšou. (Pozri obr. 6 a obr. 7)

![]({{ '/assets/images/operation_templates/30_die_stress/3d_die_stress_analysis_theory/image0006.jpg' | relative_url }})

Model s vysokou zložitosťou

![]({{ '/assets/images/operation_templates/30_die_stress/3d_die_stress_analysis_theory/image0007.jpg' | relative_url }})

Vysoko komplexný model s montážou za tepla a tvárnením

## Analýza napätí v prepojených čipoch

  * Analýza napätia v matrici bez zohľadnenia vplyvu okolných faktorov (jednokroková) sa ukázala ako veľmi účinná pri predpovedaní porúch nástrojov.

  * Pri niektorých výkovkoch dochádza k najvyššiemu namáhaniu v strede zdvihu. 

  * Zlyhanie výseku v dôsledku ťahového namáhania je znázornené pomocou analýzy napätia v matrici s úzkou väzbou.

![]({{ '/assets/images/operation_templates/30_die_stress/3d_die_stress_analysis_theory/image0008.jpg' | relative_url }})

Analýza únavovej pevnosti párov

**Súvisiace témy:**

[Coupled Die Stress analysis](/docs/en/operation_templates/30_die_stress/coupled_die_stress_analysis/)

[Die Stress Lab](/docs/en/labs/die_stess_study_labs/die_stess_labs_across_single_steps_main_pg/)
