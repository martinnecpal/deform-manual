---
lang: sk
title: "10.1.3.5. Hillov kvadratický model (polykryštalický model plasticity)"
---

# 10.1.3.5. Hillov kvadratický model (model polykryštalickej plasticity)

Pre model Hillovej kvadratickej (polykryštalickej plasticity) anizotropnej funkcie klzu (pozri nižšie Obr. 10.1.3.5.1.) je potrebné v dialógovom okne Materiál definovať informácie o textúre (typ kryštálu, typ textúry). V každom materiálovom bode objektu sa vyhodnotia orientačné distribučné funkcie (ODF) na základe sieťovaného rodriguesovho priestoru.

![]({{ '/assets/images/pre-processor/10_material_data/10_1_plastic_data/10_1_3_yield_models/10_1_3_5_hill’s_quadratic_\(polycrystalline\)/10_1_3_5_image001.jpg.jpg' | relative_url }})

Kvadratický kopec (model polykryštalickej plasticity)

TXTODF špecifikuje ODF v každom hmotnom bode objektu. Ak má materiál viacero fáz, TXTODF uvádza ODF po jednotlivých fázach v závislosti od definície postupnosti fáz materiálu. V prípade jednofázového materiálu, keď sa na reprezentáciu textúry používa Rodriguesov priestor, sa počet ODF rovná nezávislým uzlom sieťovaného Rodriguesovho priestoru. V prípade viacfázového materiálu sa počet ODF rovná súčtu nezávislých uzlov sieťovaného Rodriguesovho priestoru všetkých fáz.

[10.1.3.1. Von Mises](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_3_yield_models/10_1_3_1_von_mises/)

[10.1.3.2. Hill’s quadratic (FGHLMN)](10_1_3_2_hill’s_quadratic_\(fghlmn\).htm)

[10.1.3.3. Hill’s quadratic (R)](10_1_3_3_hill’s_quadratic_\(r\).htm)

[10.1.3.4. Lankford coefficient (R value)](10_1_3_4_lankford_coefficient_\(r_value\).htm)

[10.1.3.6. User's routine](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_3_yield_models/10_1_3_6_user_s_routine/)
