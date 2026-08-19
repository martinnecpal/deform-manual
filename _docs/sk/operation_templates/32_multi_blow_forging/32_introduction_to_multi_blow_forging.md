---
lang: sk
title: "32. Úvod do kladiva s viacnásobným úderom"
---

# 32\. Úvod do viacnásobného kovania

Systém kovania zahŕňa všetky vstupné premenné, ako sú sochor alebo polotovar (geometria a materiál), nástroje (geometria a materiál), podmienky na rozhraní nástroj/materiál, mechanika plastickej deformácie, použité zariadenia, vlastnosti konečného výrobku a napokon aj prostredie závodu, v ktorom sa proces vykonáva.

Operácia viacnásobného kovania sa používa na nastavenie úlohy, pri ktorej dochádza k postupným úderom buď kladivom, alebo skrutkovým lisom. V rámci tejto operácie môže používateľ nastaviť úlohu kovania bez nutnosti ručného reštartovania každého cyklu a v tabuľke úderov môže definovať počet úderov. Pre každý úder je možné definovať percentuálnu hodnotu úderu, energiu, opätovné zahrievanie a samostatnú dobu výdrže. V novej verzii MO V11.0 sú k dispozícii pokročilé funkcie, ako napríklad adaptívne riadenie procesu, možnosť definovať účinnosť úderu ako funkciu, a sú dostupné všetky simulačné modely (transformácia, karburácia, rekryštalizácia atď.).

  
**Ako pridať operáciu kovania s viacerými údermi**

Operáciu viacnásobného kovania je možné otvoriť prostredníctvom sprievodcu MO, ktorý je dostupný z hlavného grafického rozhrania. Operáciu viacnásobného kovania je možné pridať v sprievodcovi MO na karte „Explorer“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky „2D Multi blow Forging“. Užívateľ ju môže pridať aj pomocou funkcie drag and drop do Editoru operácií, ako je znázornené na obr. 32.1.

  
![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_introduction_to_multi_blow_forging/image001.jpg' | relative_url }})

Do editora operácií bola pridaná operácia 2D viacnásobného kovania

Nižšie sú uvedené kroky na nastavenie operácie viacnásobného výkovu v sprievodcovi MO:

  * Definovať podrobnosti procesu

  * Definovať tabuľku výdychov

  * Typ geometrie

  * Ovládacie prvky simulácie

  * Načítať materiál objektu

  * Zadajte počet objektov

  * Vytvorte geometriu objektov a vygenerujte sieť pre tieto objekty

  * Nastaviť materiálové a okrajové podmienky

  * Nastavte pohyb hornej matrice (počet úderov)

  * Ovládacie prvky zastavenia a krokové ovládacie prvky

  * Vytvoriť databázu

  * Spustenie simulácie.

**Súvisiace témy:**

[6.1. Integrated Manufacturing Process Pre- Processor Layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

[6.2. Integrated Manufacturing Process.Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Proces Post - Processor layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[32.1. 2D Multi Blow Forging](/docs/en/operation_templates/32_multi_blow_forging/32_1_2d_multi_blow_forging_setup/)

[32.2. 3D Multi Blow Forging setup](/docs/en/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/)
