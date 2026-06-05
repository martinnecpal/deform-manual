---
lang: sk
title: "10.4. Difúzne údaje"
---

# 10.4. Difúzne údaje

10.4.1. Difúzny koeficient (DIFCOE)

  * Metóda 1

  * Metóda 2

  * Metóda 3

  * Metóda 4

  * Metóda 5

![]({{ '/assets/images/pre-processor/10_material_data/10_4_diffusion_data/10_3_image001.jpg' | relative_url }})

Okno vlastností difúzneho materiálu

DEFORM umožňuje používateľovi modelovať difúziu dominantného atómu (v tomto bode uhlíka) v objekte. (Pozri obr. 10.4.1.) Používateľ musí zadať iba koeficient difúzie pre difúziu. Na simuláciu procesu nauhličovania, ktorý sa zvyčajne vykonáva pred kalením,
Pre difúzny model sa používa Laplaceova rovnica:

![]({{ '/assets/equations/pre_processor/10_material_data/10_4_diffusion_data/eq_10_4_1.jpg' | relative_url }}) |
---|---
  
Poznámka:
Tehlové prvky majú tendenciu poskytovať krajšie výsledky ako štvorstenné prvky, pretože priemerná difúzna vzdialenosť je zvyčajne oveľa menšia ako priemerná dĺžka hrany prvku. To spôsobí, že výsledky tetraedrických prvkov vyzerajú trochu nejednotne kvôli ich všeobecne nerovnomernej dĺžke hrán (odkaz na vytvorenie MO siete Brick).

## **Difúzny koeficient (DIFCOE)**

Difúzny koeficient ([DIFCOE](/docs/sk/keyword_documentation/d/difcoe/)) možno definovať nasledujúcimi metódami:

  * **Metóda 1**

********Konštantná hodnota koeficientu difúzie.

  * **Metóda 2**

****Difúzny koeficient je funkciou obsahu atómov a teploty (maticový formát).

![]({{ '/assets/equations/pre_processor/10_material_data/10_4_diffusion_data/eq_10_4_2.jpg' | relative_url }}) |
---|---
  
  * **Metóda 3**

Difúzny koeficient je funkciou teploty a obsahu atómov (tabuľkový formát).

![]({{ '/assets/equations/pre_processor/10_material_data/10_4_diffusion_data/eq_10_4_3.jpg' | relative_url }}) |
---|---
  
  * **Metóda 4**

Difúzny koeficient je funkciou teploty a obsahu atómov (tabuľkový formát).

![]({{ '/assets/equations/pre_processor/10_material_data/10_4_diffusion_data/eq_10_4_4.jpg' | relative_url }}) |
---|---
  
  * **Metóda 5**
