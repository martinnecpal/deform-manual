---
lang: sk
title: "1.4. Analýza výrobného procesu pomocou programu DEFORM"
---

# 1.4. Analýza výrobného procesu pomocou DEFORM

DEFORM možno použiť na analýzu väčšiny tepelno-mechanických procesov tvárnenia a mnohých procesov tepelného spracovania. Všeobecný prístup spočíva v definovaní geometrie a materiálov počiatočného obrobku v programe DEFORM a potom v postupnej simulácii každého procesu, ktorý sa má na obrobok aplikovať.

Odporúčaná postupnosť pri navrhovaní výrobného procesu pomocou programu DEFORM je:

  * Definujte navrhovaný postup.

  * Konečná geometria kovaného dielu
  * Materiál
  * Progresie nástrojov
  * Počiatočná geometria obrobku/sukna
  * Teploty spracovania, ohrievania atď.

  1. Zhromaždenie požadovaných údajov.

  * Údaje o materiáli

  * Spracovanie údajov o stave.
  * Pomocou predprocesora DEFORM zadajte definíciu problému pre prvú operáciu.
  * Pomocou rozhrania DEFORM MO Interface zadajte definíciu problému, aby ste na začiatku vytvorili postupné operácie a simulovali všetky operácie za sebou bez interakcie používateľa. Obr. 1.4.1. vysvetľuje priebeh procesu v prostredí MO.
  * Odoslanie údajov na simuláciu.
  * Pomocou postprocesora DEFORM skontrolujte výsledky.
  * Pomocou postprocesora Next gen skontrolujte výsledky a vytvorte správu pre požadované stavové premenné/grafy.
  * Opakujte postupnosť pred spracovaním - simulácia - preskúmanie pre každú operáciu v procese.
  * Ak sú výsledky neprijateľné, použite svoje inžinierske skúsenosti a úsudok na úpravu procesu a zopakujte postupnosť simulácie.

![]({{ '/assets/images/about_deform/1_4_analyzing_manufacturing_process_with_deform/1_4_image001.jpg' | relative_url }})

Priebeh procesov v MO ENVIRONMENT

**Súvisiace témy:**

[PRE-PROCESSOR](/docs/sk/pre_processor/7_introduction_to_pre-processor/)

[POST-PROCESSOR](/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)

[Integrated Manufacturing Process](/docs/sk/integrated_manufacturing_process_setup/5_introduction_to_integrated_manufacturinghtm/) (MO)

[Material Data Definition](/docs/sk/pre_processor/10_material_data/10_material_data/)

[Geometry Data](/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/)

[Movement Control Definition](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[Inter-object Data definition](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[Appendix V: The elasto-plastic model](/docs/sk/appendices/appendix_v__the_elasto-plastic_model/)

[Appendix VII: Checking the forming loads results of a simulation](/docs/sk/appendices/appendix_vii__checking_the_forming_loads_of_a_simulation/)
