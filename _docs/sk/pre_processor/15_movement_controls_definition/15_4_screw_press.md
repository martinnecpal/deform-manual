---
lang: sk
title: "15.4. Skrutkovací lis"
---

# 15.4. Skrutkovací lis

**[2D, 3D]:** Jedinečnou vlastnosťou skrutkového lisu je spôsob jeho pohonu. Motor poháňa zotrvačník, ktorý je buď priamo pripojený, alebo môže byť pripojený k vretenu skrutky. Skrutkové vreteno prenáša rotáciu cez závity, ktoré majú uhol stúpania zvyčajne medzi 13 a 17 stupňami, na lineárny pohyb hlavného barana. Pri kontakte s obrobkom sa celá kinetická energia zotrvačníka a barana transformuje na užitočnú prácu (práca na obrobku) a straty (práca pri pružnej deformácii v obrobku a v ráme konštrukcie a trenie). Výsledkom pružnej deformačnej práce je reakčná sila vo všetkých častiach lisu ležiacich v dráhe prenosu sily.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_4_screw_press/15_4_image001.jpg' | relative_url }})

2D okno ovládania pohybu skrutky

![]({{ '/assets/images/pre-processor/15_movement_controls/15_4_screw_press/15_4_image002.jpg' | relative_url }})

Okno ovládania pohybu 3D skrutkovacieho lisu

Metóda energie skrutkového lisu napodobní pohyb skrutkového lisu na vybranej matrici. Pri skrutkovom lise sa zotrvačník uvedie do danej rýchlosti a zapne sa spojka. Po zapnutí spojky začne skrutkový lis čerpať energiu na pohon skrutky zo zotrvačníka. Po vyčerpaní energie zotrvačníka sa zdvih skončí a pohyb sa zastaví. Pohyb riadený skrutkou sa môže špecifikovať len pre tuhé objekty alebo deformujúce sa objekty s aplikovanou okrajovou podmienkou pohybu. Pohyb, ktorý je riadený parametrami lisovania skrutiek, možno aplikovať len v smeroch +X, +Y, +Z, -X, -Y alebo -Z (v prípade DEFORM-2D v smeroch X, Y, -X alebo -Y).

Nastavenie pohybu lisu na skrutky nájdete na obr. 15.4.1 a obr. 15.4.2.

Údaje potrebné na spustenie nástroja poháňaného skrutkovým lisom sú:

  * **Energia** : Blow Energy je miera celkovej energie, ktorú bude zotrvačník obsahovať po dosiahnutí požadovaných otáčok a pred zopnutím spojky. Jednotky pre blow energy v anglických jednotkách sú klb-in a v jednotkách SI sú N-mm.

  * **Účinnosť fúkania** : Účinnosť fúkania predstavuje podiel celkovej energie, ktorá sa premení na deformačnú energiu. Zvyšok energie sa absorbuje prostredníctvom spojkového mechanizmu, trenia a rámu stroja. Pre túto veličinu nie sú stanovené žiadne jednotky.

  * **Moment zotrvačnosti** : Moment zotrvačnosti je moment zotrvačnosti zotrvačníka. Anglické jednotky zotrvačnosti sú klb*in*s2 a jednotky SI sú N-mm*s2. Hmotnostný moment zotrvačnosti pre kruhový disk s osou Z kolmou na stred je I = 2 ET /ω2 , kde ET je celková energia zotrvačníka a ω je uhlová rýchlosť v radiánoch za sekundu.

  * **Posunutie ramena alebo rozstup olovenej skrutky** : Posunutie barana udáva vzdialenosť, ktorú skrutka prejde za jednu otáčku zotrvačníka. Pomáha pri určovaní lineárnej rýchlosti barana. Anglické jednotky pre Ram Displacement sú inch/otáčku, zatiaľ čo jednotky SI sú mm/otáčku. Ak je známy len uhol stúpania a priemer vretena, posunutie ramena možno vypočítať pomocou πdsin(θt), kde d je priemer vretena a θt je uhol stúpania vretena.

Poznámka:

Viacnásobný priechod možno nastaviť pre operácie kladiva, skrutkovacieho lisu a valcovania pomocou možnosti ponuky nástrojov v paneli ponúk okna predprocesora.

**Súvisiace témy:**

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.5. Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/).
