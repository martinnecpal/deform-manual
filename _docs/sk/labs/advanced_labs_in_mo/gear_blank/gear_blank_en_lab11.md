---
lang: sk
title: "Polotovar na ozubené kolesá EN Lab 11"
---

# Cvičenie č. 11 – Vyhodnocovanie výsledkov

Prezrite si projekt **Gear_t** v hlavnom okne DEFORM GUI a vyberte DB. Kliknite na odkaz ![]({{ '/assets/icons/pre_icons/2d_3d_post_label.jpg' | relative_url }}) Post Processor, aby sa otvoril v programe Next Gen Post.

**Prejdite si jednotlivé kroky**

Kliknite na ![]({{ '/assets/icons/post_icons/mo_play_button.jpg' | relative_url }}) „Prehrať kroky dopredu“ a sledujte, ako obrobok vyplňuje nástroj. Nastavte jednoduchý pohľad bez siete ![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}) a zapnite kontakt ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}). Prehrávajte proces krok po kroku (použite tlačidlá „Ďalší“ ![]({{ '/assets/icons/post_icons/mo_next_step_icon.jpg' | relative_url }}) a „Predchádzajúci“ ![]({{ '/assets/icons/post_icons/mo_prevoius_step_icon.jpg' | relative_url }})) a sledujte, ako sa obrobok dotýka hornej a spodnej matrice. (Pozri obr. L11.1.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab11_image0001.jpg' | relative_url }})

Kontakt obrobku s nástrojmi pri ich vkladaní do upínacieho zariadenia

Program FLOWNET možno použiť na vytvorenie vzoru na obrobku na začiatku procesu kovania a na sledovanie deformácie prostredníctvom simulácie. Vypnite premenné poľa a kliknite na ikonu FLOWNET ![]({{ '/assets/icons/post_icons/mo_flownet_icon.jpg' | relative_url }}), čím otvoríte okno definície FLOWNET. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vyberte vzor **Polygon grid**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a definujte rezaciu rovinu v strede obrobku. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a ako počet polygónov zadajte hodnotu 4. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) vygenerujte predvolený kruhový vzor, ktorý si môžete prezrieť postupným prechádzaním zoznamu krokov. Ak chcete sledovať, ako sa vzor deformuje spolu s obrobkom, zapnite obrobok ![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}) a potom ho rozrežte tak, aby ste mohli vidieť sieť a flownet, ako je znázornené na obr. L11.2.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab11_image0002.jpg' | relative_url }})

Obrobok v poslednom kroku s mriežkovým vzorom z mnohouholníkov a rezovou rovinou

Otvorte súbor „**Gear_sym****.****DB**“ v programe Next Gen Post podľa pokynov uvedených pre súbor Gear_t.DB. Model DEFORM obsahuje vylepšenú sieť posunov, ktorá pomáha predpovedať vznik záhybov. Prejdite na príspevok, rozrežte objekt a sledujte, ako sa vytvára záhyb. Prejdite na posledný krok, kliknite pravým tlačidlom na ikonu skladania v strome a vyberte **Zobraziť skladanie**. Tým sa zobrazia oblasti, kde sa obrobok preložil a dotkol sa sám seba. DEFORM tieto oblasti odstráni, aby pomohol konvergencii.

Použite sieť Offset flownet, ktorá slúži na vyhľadávanie záhybov. Táto sieť dokáže odhaliť tendenciu k tvorbe záhybov, ktorá sa v sieti neobjavuje. Prejdite na posledný krok a zobrazte si sieť flownet. Uvidíte, že záhyb pretrváva, hoci bol zo siete obrobku odstránený.

* * *

Voliteľné cvičenie – ak to čas dovolí – PIP (obraz v obraze) / Animácia

\- Na paneli nástrojov prejdite na Súbor/Importovať databázu (PIP) a importujte tú istú databázu. V grafickom okne máte teraz dva obrázky, s ktorými môžete pracovať. V hornom zobrazení môžete s obrobkom otáčať, posúvať ho a približovať. Zaznačte deformáciu a prehrajte simuláciu.

\- Vytvorte graf zaťaženia a zdvihu na jednom obrázku. Prehrajte simuláciu.

\- Na paneli nástrojov kliknite na ![]({{ '/assets/icons/post_icons/mo_animation_icon.jpg' | relative_url }}) (Nastavenie animácie). Prezrite si nižšie uvedené nastavenia a kliknite na Uložiť. Prehrajte súbor s animáciou.

  * **Záložka Všeobecné:** Názov súboru je názov animácie. Súbory animácií sa uložia do priečinka DEF_ANIM v aktuálnom adresári simulácie (štandardne).

  * **Karta Nastavenia:** slúži na nastavenie časového kroku medzi snímkami, ako aj na začiatku a na konci animácie

  * **Karta Export:** Vyberte súbor WMV, aby ste vytvorili animáciu vo formáte WMV, ktorú je možné prehrať takmer na každom počítači.

* * *

Voliteľné cvičenie – ak to čas dovolí – Čistenie

\- Otvorte zoznam krokov ![]({{ '/assets/icons/post_icons/mo_step_list_icon.jpg' | relative_url }}). Modro zvýraznené kroky sú vybrané. Práve tieto zvýraznené kroky uvidíte pri prehrávaní simulácie. Môžete kliknúť na ľubovoľný krok alebo kliknúť a pretiahnuť kurzorom cez viacero krokov, čím vyberiete alebo zrušíte výber jedného alebo viacerých krokov. Na pravej strane sa nachádzajú aj nástroje, ktoré vám pomôžu vybrať požadované kroky.

\- Kliknite na „None“, potom do poľa „Increment“ zadajte hodnotu 50 a stlačte klávesu Enter. Kliknite na tlačidlo „Remeshing“.

\- Prejdite do časti „Vyčistenie databázy“ a kliknite na „Uložiť vybrané kroky“. Tým sa vytvorí nová databáza s názvom Gear_sym_PUR.DB. Nová databáza bude obsahovať iba kroky, ktoré ste vybrali. Všetky nevybrané kroky budú odstránené (vyčistené). Výsledkom je menšia databáza, ktorú je jednoduché archivovať.

* * *
