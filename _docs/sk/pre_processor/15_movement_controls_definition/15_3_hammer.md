---
lang: sk
title: "15.3. Kladivo"
---

# 15.3. Kladivo

15.3.1. Kladivo typu kovadlina

15.3.2. Protiúderové kladivo

**[2D, 3D]** : Kovanie kladivom sa riadi energiou. Počas pracovného zdvihu deformácia prebieha dovtedy, kým sa celková kinetická energia nerozptýli plastickou deformáciou materiálu a pružnou deformáciou barana a kovadliny, keď sa čelá zápustky a barana navzájom dotýkajú. (Pozri obr. 15.3.1 a obr. 15.3.2).

![]({{ '/assets/images/pre-processor/15_movement_controls/15_3_hammer/15_3_image001.jpg' | relative_url }})

2D okno ovládania pohybu stlačenia kladiva

![]({{ '/assets/images/pre-processor/15_movement_controls/15_3_hammer/15_3_image002.jpg' | relative_url }})

Okno ovládania pohybu 3D Hammer Press

Počas kovania kladivom sa na plastickú deformáciu obrobku využíva len časť kinetickej energie barana. Zvyšok energie sa stráca cez kovadlinu a rám stroja.

Účinnosť fúkania ![]({{ '/assets/equations/pre_processor/15_movement_controls/eta_b.jpg' | relative_url }}) je definovaná takto:

![]({{ '/assets/equations/pre_processor/15_movement_controls/eq_15_3_1.jpg' | relative_url }}) |
---|---
  
Tieto hodnoty môžete nastaviť v okne ovládania pohybu.

V zásade existujú dva typy kladív. Prvým je kladivo s kovadlinou a druhým protiúderové kladivo. Formulácie a predpoklady použité pre tieto dva typy kovacích kladív sú uvedené nižšie:

## Kladivo typu kovadlina [2D, 3D]

Pri kovadlinkovom kladive je obrobok spolu so spodnou súpravou matrice umiestnený na kovadlinke, ktorá je nehybná. V jednoduchom gravitačnom kladive je baran zrýchľovaný gravitáciou a akumuluje energiu.

Preto sa energia úderu ![]({{ '/assets/equations/pre_processor/15_movement_controls/et.jpg' | relative_url }}) vypočíta podľa:

![]({{ '/assets/equations/pre_processor/15_movement_controls/eq_15_3_2.jpg' | relative_url }}) |
---|---
  
V kladive s poklesom výkonu je baran okrem gravitácie urýchľovaný aj tlakom pary, studeného alebo horúceho vzduchu.

Celková energia úderu je daná:

![]({{ '/assets/equations/pre_processor/15_movement_controls/eq_15_3_3.jpg' | relative_url }}) |
---|---
  
Rýchlosť barana ![]({{ '/assets/equations/pre_processor/15_movement_controls/vt.jpg' | relative_url }}) sa vypočíta podľa:

![]({{ '/assets/equations/pre_processor/15_movement_controls/eq_15_3_4.jpg' | relative_url }}) |
---|---
  
Energia plastickej deformácie počas malého časového prírastku ![]({{ '/assets/equations/pre_processor/15_movement_controls/delta_t.jpg' | relative_url }}) sa vypočíta podľa:

![]({{ '/assets/equations/pre_processor/15_movement_controls/eq_15_3_5.jpg' | relative_url }}) |
---|---
  
Po zvýšení sa energia úderu upraví o:

![]({{ '/assets/equations/pre_processor/15_movement_controls/eq_15_3_6.jpg' | relative_url }}) |
---|---
  
Táto úprava zohľadňuje stratu elastickej energie. Simulácia sa opakuje, kým sa energia úderu ![]({{ '/assets/equations/pre_processor/15_movement_controls/et.jpg' | relative_url }}) nestane nulovou.

Charakteristické hodnoty kladív typu Anvil sú uvedené v nasledujúcej tabuľke 15.3.1.

**Typ kladiva** | ****| **E, KN-m (ft-lbf)** | **nB** | **Vs, m/s (ft/s)** | **nB, min-1** | **nH**
---|---|---|---|---|---|---
Kladivo na voľný pád | Opasok | 40(29,440) | 0,3-0,6 | 4-5(13-16,4) | 40 | 0,2-0,3
| Rada | 16(11 780) | 0,3-0,6 | 4-5(13-16,4) | 35 | 0,2-0,3
| Reťazec | 100(73 600) | 0,3-0,6 | 4-5(13-16,4) | 55 | 0,5
| Piston | 63(46,370) | 0,3-0,6 | 4-5(13-16,4) | 60 | 0,5
Výkonné kladivo | Pneumatické | 50(36 800) | 0,8-0,9 | 5-8(16,4-26,3) | 80-250 | 0,45-0,55
| Otvorená forma, jeden rám | 40(29,440) | 0,8-0,9 | 5-8(16,4-26,3) | 450 | 0,45-0,55
| Open-die, double frame | 250(184 000) | 0,8-0,9 | 5-8(16,4-26,3) | 55-240 | 0,5
| Zápustkové kovanie | 100(73 600) | 0,3-0,6 | 5-8(16,4-26,3) | 55-240 | 0,5
  
Charakteristické hodnoty kladív typu Anvil

## Kladivo na protiúder [2D, 3D]

Protiúderové kladivo sa definuje zadaním zaškrtávacieho políčka Protiúderové kladivo pre jednu matricu, ako je znázornené na obr. 15.3.3 a obr. 15.3.4. Celková energia by sa mala definovať pre prvú výlisok (spravidla primárny výlisok). Hmotnosť každej raznice by sa mala priradiť k príslušnej raznici.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_3_hammer/15_3_image003.jpg' | relative_url }})

2D Nastavenia protiúderového kladiva

![]({{ '/assets/images/pre-processor/15_movement_controls/15_3_hammer/15_3_image004.jpg' | relative_url }})

3D Nastavenia lisu s kladivom proti úderu

DEFORM predpokladá, že hybnosť je v protibežných kladivách vyrovnaná. To znamená, že M1* V1 = M2* V2, kde M a V sú hmotnosť a rýchlosť príslušných razníkov. Program DEFORM automaticky rozdelí energiu medzi obe raznice a vypočíta rýchlosť každej raznice. Vstupy sú zhrnuté v tabuľke 15.3.2.

| Die 1 | Die 2
---|---|---
Energia | Celková energia | 0
Hmotnosť | Hmotnosť matrice 1 | Hmotnosť2
Účinnosť | Účinnosť úderu | Zdedené z Die 1
Rýchlosť | Sqrt (2*E*M2/((M1+M2)*M1)) | V1*M1/M2
  
Zhrnutie vstupných údajov o pohybe kladiva

**Súvisiace témy:**

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)

[15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/).
