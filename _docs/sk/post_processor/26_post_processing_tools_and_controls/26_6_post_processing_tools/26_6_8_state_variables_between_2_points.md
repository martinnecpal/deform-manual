---
lang: sk
title: "26.6.8. Stavové premenné medzi dvoma bodmi"
---

# 26.6.8. Stavové premenné medzi dvoma bodmi

  * Priamka

  * Podľa hranice

  * Kruhový vzor

  
**Priamka [2D, 3D]:** Táto funkcia umožňuje používateľovi určiť dva body a vykresliť dané rozloženie stavovej premennej medzi týmito dvoma bodmi. Rozloženie stavovej premennej je možné medzi týmito dvoma bodmi objektu lineárne interpolovať. (Obr. 26.6.8.1., Obr. 26.6.8.2. a Obr. 26.6.8.3.)

  
**Vzorkovacie body**: Pomocou tohto posuvníka môže používateľ nastaviť počet vzorkovacích bodov.

**Sledovať objekt**: Zaškrtnutím tohto políčka sa začiatok a koniec vzorkovacích bodov budú prispôsobovať obrobku.

**Rozloženie plochy**: Zaškrtnutím tohto políčka sa vypočíta plocha pokrytá vzorkovacími bodmi medzi počiatočným a koncovým bodom na objekte.

**Sledovať obrys**: Zaškrtnutím tohto políčka sa body budú prispôsobovať obrysu objektu.

**Graf**: Kliknutím na toto tlačidlo ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) sa vypočítajú stavové premenné a zobrazí sa graf.

**Kapela** : 

**Postup:**

**Krok 1:** Kliknite na tlačidlo „SV distribution“ v postprocesore.

**Krok 2:** Vyberte body, ktoré chcete interpolovať pozdĺž priamky.

**Krok 3:** Vyberte dva body na objekte, ktoré chcete interpolovať.

**Krok 4:** Kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}).

  
Ak nie je vybraná žiadna stavová premenná, zobrazia sa len body. Po výbere stavovej premennej z okna stavových premenných sa kliknutím na tlačidlo ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) zobrazí graf rozdelenia medzi týmito dvoma bodmi.(Pozri obr. 26.6.8.1., obr. 26.6.8.2. a obr. 26.6.8.3.) 

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_8_state_variables_between_2_points/image001.jpg' | relative_url }})

Zobrazenie grafu rozdelenia SV medzi dvoma bodmi pre priamku

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_8_state_variables_between_2_points/image002.jpg' | relative_url }})

Zobrazenie grafu rozdelenia SV medzi dvoma bodmi pre priamku bez plošného rozdelenia

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_8_state_variables_between_2_points/image003.jpg' | relative_url }})

Zobrazenie grafu rozdelenia SV medzi dvoma bodmi pre priamku s plošným rozdelením

**Podľa hranice [2D, 3D]:** Táto funkcia umožňuje používateľovi určiť body pozdĺž hranice objektu, aby sa znázornilo rozloženie danej stavovej premennej medzi počiatočným a koncovým bodom. (Pozri obr. 26.6.8.4. a obr. 26.6.8.5.)

  
**Postup:**

**Krok 1**: V postprocesore kliknite na tlačidlo „SV distribution“.

**Krok 2**: Vyberte body, ktoré sa majú interpolovať a ktoré majú kopírovať obrys objektu.

**Krok 3**: V prípade 2D vyberte dva body na objekte, medzi ktorými sa má vykonať interpolácia.

V prípade 3D výberu označte počiatočný, stredný a koncový bod na objekte, ktorý sa má interpolovať

**Krok 4**: Kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}).

Ak nie je vybraná žiadna stavová premenná, zobrazia sa iba body. Po výbere stavovej premennej z okna stavových premenných sa kliknutím na tlačidlo ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) zobrazí graf rozdelenia medzi týmito dvoma bodmi. (Pozri obr. 26.6.8.4. a obr. 26.6.8.5.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_8_state_variables_between_2_points/image004.jpg' | relative_url }})

Zobrazenie grafu rozloženia SV medzi dvoma bodmi nasledujúcej hranice pre 2D

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_8_state_variables_between_2_points/image005.jpg' | relative_url }})

Zobrazenie grafu rozloženia SV medzi dvoma bodmi nasledujúcej hranice v 3D

**Kruhový vzor** [3D]: Táto funkcia umožňuje používateľovi definovať body v kruhovom vzore tak, že určí bod, os a uhol, okolo ktorých sa má vykresliť rozloženie danej stavovej premennej. (Pozri obr. 26.6.8.6.)

  
**Postup:**

Krok 1: Kliknite na tlačidlo „SV distribution“ v postprocesore.

Krok 2: Vyberte kartu „Kruhový vzor“.

Krok 3: Vyberte bod na objekte, ktorý chcete interpolovať, a určte uhol a smer osi.

Krok 4: Kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}).

  
Kliknutím na tlačidlo ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) sa zobrazí graf rozdelenia medzi týmito dvoma bodmi. (Pozri obr. 26.6.8.6.)

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_8_state_variables_between_2_points/image006.jpg' | relative_url }})

Zobrazenie grafu rozloženia premennej stavu medzi dvoma bodmi pre kruhovú hranicu
