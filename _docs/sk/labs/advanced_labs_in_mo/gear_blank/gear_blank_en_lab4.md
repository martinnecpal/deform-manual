---
lang: sk
title: "Polotovar na ozubené kolesá – EN Lab 4"
---

# Laboratórna práca č. 4. 3D neizotermický proces prenosu vzduchu

V programe DEFORM vytvorte nový projekt s názvom **Gear_t** podľa pokynov uvedených v [Lab1.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/' | relative_url }}#Lab1_2D_upset_operation). Ide o simuláciu dvoch operácií. Operácia 1 zahŕňa iba prenos tepla a znázorňuje pohyb obrobku z ohrievača k nástrojom. Operácia 2 je kovanie s povolenými výpočtami teploty.

### Operácia pridania a pomenovania

Pridajte operáciu **3D prenos tepla** z karty Explorer, ako je znázornené na obr. L4.1.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0001.jpg' | relative_url }})

Pridanie operácie 3D prenosu tepla a výber typu prenosu tepla

Potvrďte voľbu „Prenos vzduchom“ v okne „Prenos tepla“. V editore operácií zmeňte názov operácie na „**Prenos****z****ohrievača**“, ako je znázornené na obr. L4.2.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0002.jpg' | relative_url }})

Pomenovanie operácie ako „Prenos z ohrievača“

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite do okna objektu. V tejto operácii sa bude pracovať len s jedným objektom, preto kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a definujte obrobok.

### Definovanie podmienok procesu

Nastavte čas prenosu na **15** sekúnd (pozri obr. L4.3.), čo zodpovedá 15-sekundovému prenosu z pece (alebo indukčných cievok) do nástroja. Zachovajte predvolenú hodnotu teploty okolitého vzduchu **Environment****temperature****68** °F a **koeficient konvekcie****7,7e-06** Btu//s/in²/F a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno objektu. V tejto operácii sa bude spracovávať len jeden objekt, preto kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali obrobok.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0003.jpg' | relative_url }})

Okno nastavení prevádzkových podmienok

### Definovanie všeobecných údajov o obrobku

Nastavte teplotu na **2250** °F a skontrolujte, či je typ objektu nastavený na **Plast**, ako je znázornené na obr. L4.4.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0004.jpg' | relative_url }})

Okno so všeobecnou definíciou objektu obrobku

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste vytvorili geometriu z primitívu.

### Vytvorenie 3D primitívnej geometrie

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), aby ste vytvorili obrobok. Zo zoznamu ikon vľavo vyberte **Valec**. Nastavte **priemer** (2R) obrobku na hodnotu **5,00** ” a **výšku** (H) na hodnotu **8,15** ”, pričom **polomer rohu** (r) nastavte na hodnotu **0,10** ”. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pre vytvorenie geometrie. (Pozri obr. L4.5.) 

_Všimnite si, že smer výšky primitívu je **Z**._

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0005.jpg' | relative_url }})

Okno s 3D geometrickými primitívami

Akonáhle bude geometria k dispozícii, v okne geometrie budú dostupné nástroje na prácu s geometriou, ako napríklad „Check“, „Fix“, „Scale“, „Reverse“ atď., ako je znázornené na obr. L4.6.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0006.jpg' | relative_url }})

Možnosti okna „Geometria“

Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka so sieťou.

### Vytvorenie siete pre obrobok

V okne stránky „Mesh“ zmeňte režim nastavení preprocesora na „Expert“ pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (prepnutie do režimu Expert) na paneli nástrojov. Režim „Expert“ ponúka viac možností pre podrobné nastavenia. Nastavte cieľový počet prvkov na **20 000** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Vyberte typ **Absolute****mesh**, nastavte pomer **veľkostí** prvkov siete na hodnotu **2,5**, ako je znázornené na obr. L4.7., aby sa pri opätovnom vytváraní siete použil typ Absolute mesh.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0007.jpg' | relative_url }})

Pokročilé nastavenia siete

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste priradili materiál.

### Načítanie a priradenie materiálu k obrobku

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice), ako je znázornené na obrázku [Fig. L1.6.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab1/' | relative_url }}#Fig_L1_6_Loading_material_from_library). Vyberte kategóriu **Steel_at_Extended_Temperatures**, potom **AISI-8620[1550–2200 °F (850–1200 °C)]** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}).

Kliknite na **AISI-8620[1550–2200 °F (850–1200 °C)]**, aby ste obrobku priradili materiál. Potvrďte priradenie v stromovej štruktúre objektov, kde sa názov materiálu zobrazuje vedľa položky „materiál“ a v texte „Informácie o priradenom materiáli“ nad zoznamom materiálov, ako je znázornené na obrázku [Fig. L1.11.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/' | relative_url }}#Fig_L1_11_Object_Material_Assigning_window).

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali okrajovú podmienku.

### Definovanie okrajovej podmienky

Pre obrobok definujte okrajovú podmienku „Výmena tepla s okolím“. Predvolené okrajové podmienky sú už priradené; ak nie, kliknite na vetvu „Výmena tepla s okolím“. Vyberte celý povrch obrobku kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Vybrať všetko) v okne „Výber uzlov“ (vľavo na paneli nástrojov pod prehliadačom). Po výbere uzlov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) (pridať okrajovú podmienku). Kliknite na vetvu **Defined**, aby ste sa uistili, že je okrajová podmienka definovaná. (Pozri obr. L4.8.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0008.jpg' | relative_url }})

Potvrdenie definície okrajovej podmienky výberom vetvy „Defined“

Kliknite na **krok****vetvu** v strome operácií, aby ste definovali ovládacie prvky kroku.

### Nastavenie ovládacích prvkov kroku

Nastavte **počet krokov** na **60**, **krok****prírastok** na **5** krokov a **definíciu kroku****riešenia******na** **0,25** s pre **operáciu prenosu tepla** (pozri obr. L4.9.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0009.jpg' | relative_url }})

Ovládacie prvky krokov v režime s navádzaním

### Vytvoriť databázu a odoslať na simuláciu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) a skontrolujte informácie o overovaní údajov. Uistite sa, že v definícii údajov nie sú žiadne chyby. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}). Uistite sa, že bola vygenerovaná databáza, a spustite simuláciu.

Kliknutím na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustíte simuláciu.

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spustení) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Simuláciu môžete sledovať v oknách „Simulačná grafika“ a „Simulačné správy“. V poslednom riadku súboru správ a protokolu bude uvedené, že simulácia bola dokončená. Kliknutím na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“ si môžete prezrieť výsledky.

### Prehľad výsledkov leteckého prevozu

Po dokončení simulácie skontrolujte teplotné straty v obrobku, najmä v rohoch.

Kliknite na ikonu stavovej premennej ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) (Zobraziť teplotu) v nástrojoch grafu. Kliknite pravým tlačidlom myši s kurzorom umiestneným nad farebným pruhom a vyberte možnosť „Typ farebného pruhu / Teplota“, čím dosiahnete realistickejší výber farieb, ako je znázornené na obr. L4.10.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0010.jpg' | relative_url }})

Graf premennej „Teplota“ s farebným stĺpcovým grafom typu „Teplota“

Kliknite na ikonu „Súhrn“ ![]({{ '/assets/icons/post_icons/mo_summary_icon.jpg' | relative_url }}). Prejdite na kartu ![]({{ '/assets/icons/post_icons/mo_thermal_sv_icon.jpg' | relative_url }}) (Teplotné) a zadajte ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) maximálne a minimálne teplotné hodnoty. Tým sa v každom kroku vykreslia najvyššia a najnižšia teplota kdekoľvek v obrobku, ako je znázornené na obr. L4.11.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0011.jpg' | relative_url }})

Graf s prehľadom teplôt

Kliknutím na tlačidlo režimu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) prejdete do režimu Pre, aby ste mohli pokračovať v postupnom tvárnení v režime [Lab 5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab5/' | relative_url }})

Kliknite na [Lab 5. 3D Non-isothermal Forming operation]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab5/' | relative_url }}), aby ste nastavili postupné tvárnenie.
