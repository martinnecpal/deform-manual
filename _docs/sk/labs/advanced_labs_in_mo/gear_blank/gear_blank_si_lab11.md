---
lang: sk
title: "Polotovar na ozubené kolesá SI Lab 11"
---

# Cvičenie č. 11. Vyhodnocovanie výsledkov

Prezrite si projekt **Gear_t** v hlavnom okne DEFORM GUI a vyberte DB. Kliknutím na odkaz „![]({{ '/assets/icons/pre_icons/2d_3d_post_label.jpg' | relative_url }}) Post Processor“ ho otvoríte v programe Next Gen Post.

**Prejdite si jednotlivé kroky**

Kliknite na ![]({{ '/assets/icons/post_icons/mo_play_button.jpg' | relative_url }}) „Prehrať kroky dopredu“ a sledujte, ako obrobok vyplňuje nástrojovú súpravu. Nastavte jednoduchý pohľad bez siete ![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}) a zapnite kontakt ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}). Prehrávajte proces krok za krokom (použite tlačidlá „Ďalší“ ![]({{ '/assets/icons/post_icons/mo_next_step_icon.jpg' | relative_url }}) a „Predchádzajúci“ ![]({{ '/assets/icons/post_icons/mo_prevoius_step_icon.jpg' | relative_url }})) a sledujte, ako sa obrobok dotýka hornej a spodnej matrice. (Pozrite si [Fig. L11.1.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab11/' | relative_url }}#Fig_L11_1_Workpiece_contact_with_tools_as_it_fill_the_tooling))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab11_image0001.jpg' | relative_url }})

Kontakt obrobku s nástrojmi pri vkladaní do upínacieho zariadenia

Program FLOWNET možno použiť na vytvorenie vzoru na obrobku na začiatku kováčskej operácie a na sledovanie deformácie prostredníctvom simulácie. Vypnite premenné poľa a kliknite na ikonu FLOWNET ![]({{ '/assets/icons/post_icons/mo_flownet_icon.jpg' | relative_url }}), čím otvoríte okno definície FLOWNET. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vyberte vzor **Polygon grid**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a definujte rezací rovinu v strede obrobku. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a ako počet polygónov zadajte hodnotu 4. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}), aby ste vygenerovali predvolený kruhový vzor, ktorý si môžete prezrieť postupným prechádzaním zoznamu krokov. Ak chcete sledovať deformáciu vzoru spolu s obrobkom, zapnite obrobok a potom ho rozrežte tak, aby ste videli sieť a FLOWNET, ako je znázornené na obrázku [Fig. L11.2.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab11/' | relative_url }}#Fig_L11_2_Workpiece_at_last_step_with_polygon_grid_pattern_with_sliced_plane)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab11_image0002.jpg' | relative_url }})

Obrobok v poslednom kroku s mriežkovým vzorom a rozrezanou rovinou

Otvorte súbor „**Gear_sym****.****DB**“ v programe Next Gen Post tak, ako bolo vysvetlené v prípade súboru Gear_t.DB. Model DEFORM disponuje vylepšenou sieťou posunov, ktorá pomáha predpovedať vznik záhybov. Prejdite na príspevok, rozrežte objekt a sledujte, ako sa tvorí záhyb. Prejdite na posledný krok, kliknite pravým tlačidlom na ikonu skladania v strome a vyberte **Zobraziť skladanie**. Tým sa zobrazia oblasti, kde sa obrobok preložil a dotkol sa sám seba. DEFORM tieto oblasti odstráni, aby pomohol konvergencii.

Použite sieť Offset flownet, ktorá slúži na vyhľadávanie záhybov. Táto sieť dokáže odhaliť tendenciu k tvorbe záhybov, ktorá sa v sieti neobjavuje. Prejdite na posledný krok a zobrazte si sieť flownet. Uvidíte, že záhyb pretrváva, hoci bol zo siete obrobku odstránený.

* * *

Voliteľné cvičenie – ak to čas dovolí – PIP (obraz v obraze) / Animácia

\- Na paneli nástrojov prejdite na Súbor/Importovať databázu (PIP) a importujte tú istú databázu. V grafickom okne máte teraz dva obrázky, s ktorými môžete pracovať. V hornom zobrazení môžete s obrobkom otáčať, posúvať ho a približovať. Zaznamenajte deformáciu a prehrajte simuláciu.

\- Vytvorte graf zaťaženia a zdvihu na jednom obrázku. Prehrajte simuláciu.

\- Na paneli nástrojov kliknite na ![]({{ '/assets/icons/post_icons/mo_animation_icon.jpg' | relative_url }}) (Nastavenie animácie). Prezrite si nižšie uvedené nastavenia a kliknite na Uložiť. Spustite animačný súbor.

  * **Záložka Všeobecné:** Názov súboru je názov animácie. Súbory animácií sa uložia do priečinka DEF_ANIM v aktuálnom adresári simulácie (štandardne).

  * **Karta Nastavenia:** slúži na nastavenie časového kroku medzi jednotlivými snímkami, ako aj na začiatku a na konci animácie

  * **Karta Export:** Vyberte súbor WMV, aby ste vytvorili animáciu vo formáte WMV, ktorú je možné prehrať takmer na každom počítači.

* * *

Voliteľné cvičenie – ak to čas dovolí – Čistenie

\- Otvorte zoznam krokov ![]({{ '/assets/icons/post_icons/mo_step_list_icon.jpg' | relative_url }}). Modro zvýraznené kroky sú vybrané. Zvýraznené kroky sa zobrazujú počas prehrávania simulácie. Môžete kliknúť na ľubovoľný krok alebo kliknúť a ťahať po viacerých krokoch, čím vyberiete alebo zrušíte výber jedného alebo viacerých krokov. Na pravej strane sa nachádzajú aj nástroje, ktoré vám pomôžu vybrať požadované kroky.

\- Kliknite na „None“, potom do poľa „Increment“ zadajte hodnotu 50 a stlačte klávesu Enter. Kliknite na tlačidlo „Remeshing“.

\- Prejdite do časti „Očistenie databázy“ a kliknite na „Uložiť vybrané kroky“. Tým sa vytvorí nová databáza s názvom Gear_sym_PUR.DB. Nová databáza bude obsahovať iba kroky, ktoré ste vybrali. Všetky nevybrané kroky budú odstránené (vyčistené). Výsledkom je menšia databáza, ktorú je jednoduché archivovať.

* * *
