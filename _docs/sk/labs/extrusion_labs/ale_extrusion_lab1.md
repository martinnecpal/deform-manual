---
lang: sk
title: "Laboratórium extrudovania ALE 1"
---

# Laboratórium extrudovania ALE 1

V tomto laboratórnom cvičení nastavíme prevádzku extrudéra ALE. V rámci tohto cvičenia tiež predstavíme aktualizáciu stavových premenných pomocou akcelerácie a porovnáme výsledky simulácie s výsledkami bez tejto aktualizácie.

V rámci tohto laboratórneho cvičenia sa z veľkého valcového polotovaru vytlačia 5 malých valcových dielov. Model obrobku je znázornený na obr. ALEEXL1.1. Priemer D0 je 140 mm. Priemer D1 je 26 mm. Priemery D2 a D4 sú 27 mm. Priemery D3 a D5 sú 28 mm. Vzhľadom na to, že model je symetrický, v tomto cvičení použijeme na simuláciu štvrtinový model.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0001.jpg' | relative_url }})

Model obrobku

1.1. Vytvorenie nového problému 

1.2. Pridať operáciu

1.3. Nastavenie simulácie

1.4. Zoznam materiálov

1.5. Matrice

1.6. Ram

1.7. Kontajner

1.8. Zomrieť

1.9. Obrobok

1.10. Ovládacie prvky

1.11. Kontakt

1.12. Ovládacie prvky krokov

1.13. Vytvorenie databázy

1.14. Spustenie simulácie

1.15. Aktualizácia premenných stavu pri zrýchlení

1.16. Následné spracovanie

## Vytvorenie nového problému 

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené na obrázku ALEEXL1.2.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0002.jpg' | relative_url }})

Hlavné okno programu DEFORM GUI

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. ALEEXL1.3. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte systém jednotiek pomocou prepínača „**SI**“. Zadajte názov úlohy ako „****3D_ALE_EX_Lab1****“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili novú úlohu s použitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0003.jpg' | relative_url }})

Stránka „Nový problém“

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom „Nový projekt“, kde bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**3D_ALE_EX_Lab1**“. V tomto cvičení pridáme operáciu Extrúzia zo zoznamu operácií v Průzkumníku, preto v dialógovom okne „Nový projekt“ nezaškrtávajte políčko „Prvá operácia“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

## Pridať operáciu

Pridajte operáciu 3D extrudovanie zo zoznamu operácií v Průzkumníku. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ktoré sa nachádza vedľa položky 3D Extrusion, alebo ju môžete pridať aj pretiahnutím do editora operácií (pozri obr. ALEEXL1.4.). Po pridaní operácie Extrusion sa štandardne otvorí okno nastavení procesu.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0004.jpg' | relative_url }})

Pridanie operácie 3D extrudovania

## Nastavenie simulácie

V dialógovom okne Nastavenie simulácie vyberte ako Metódu simulácie prepínač **Extrúzia ALE**. Nastavte Tepelný výpočet na **Iba obrobok (neizotermický)** a Typ modelu formy na **S podmienkou symetrie**. Zaškrtnite políčka **Aktualizácia deformácie** aj **Aktualizácia teploty** a v poli **Zrýchlenie** nastavte hodnotu **1** na krok, čo znamená, že v tejto simulácii nedochádza k aktualizácii zrýchlenia. Nastavenie simulácie vyzerá tak, ako je znázornené na obr. ALEEXL1.5. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku Zoznam materiálov.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0005.jpg' | relative_url }})

Nastavenia simulačného prostredia

## Zoznam materiálov

V dialógovom okne „Materiál“ kliknite na možnosť „Načítať údaje o materiáli z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})“. Načítajte materiál „**ALUMINUM-6061[70-1000F(20-550C)]**“ z kategórie **Hliník**, ako je znázornené na obr. ALEEXL1.6., a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím prejdete na stránku „Matrice“.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0006.jpg' | relative_url }})

Zoznam materiálov

## Matrice

V predvolenom nastavení sa do prevádzky pridajú 2 matrice, v tomto cvičení však potrebujeme 3 matrice. Kliknite teda na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}), aby ste nastavili počet matríc na 3 (pozri obr. ALEEXL1.7.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Top Die“ (Horná matrica).

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0007.jpg' | relative_url }})

Pridané matrice

## Ram

Zmeňte názov objektu „Top Die“ na **Ram**. Nastavte **teplotu** formy na **400** °C, typ objektu ponechajte ako **Rigid** a zrušte zaškrtnutie políčka „Assign Bearing surface“. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Geometry“.

### Geometria berana

Kliknite na „Importovať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a **načítajte súbor Ram_Geo.stl** zo zložky 3D/LABS, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Symetria“. V dialógovom okne „Symetria“ definujte pre Ram **plánovú symetriu** na symetrických rovinách, ako je znázornené na obr. ALEEXL1.8. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Pohyb“.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0008.jpg' | relative_url }})

Geometria berana

### Pohyb berana

V **dialógovom okne „Pohyb“** nastavte **rýchlosť** na hodnotu **4** mm/s, ako je znázornené na obr. ALEEXL1.9. Kliknite na stránku „![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom Die“.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0009.jpg' | relative_url }})

Stránka hnutia Ram

## Kontajner

Zmeňte názov spodnej formy na **Container**. Nastavte **teplotu** formy na **350** °C, typ objektu ponechajte ako **Rigid** a zrušte zaškrtnutie políčka „Assign Bearing surface“. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Geometry“.

### Geometria kontajnera

Kliknite na položku „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a načítajte súbor **Container_Geo.stl** zo zložky 3D/LABS, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). V dialógovom okne „Symetria“ nastavte pre kontajner **rovinnú symetriu** na symetrických rovinách, ako je znázornené na obr. ALEEXL1.10. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Pohyb“.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0010.jpg' | relative_url }})

Geometria kontajnera

### Preprava kontajnerov

V dialógovom okne „Pohyb“ ponechajte hodnotu **Rýchlosť** na **0** mm/s. Kliknite na stránku „![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) do objektu 4“.

## Zomrieť

Zmeňte názov objektu 4 na **Die**. Nastavte teplotu formy na **350** °C. Typ objektu ponechajte ako **Rigid** a zaškrtnite políčko **Assign Bearing Surface** pre extrudovanie ALE (pozri obr. ALEEXL1.11.). Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku Geometry.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0011.jpg' | relative_url }})

Nastavenie lisovacej formy

### Geometria lisovacej formy

Kliknite na „Importovať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a načítajte súbor **Die_Geo.stl** zo zložky 3D/LABS, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). V dialógovom okne Symetria nastavte pre maticu **Rovinnú symetriu** na symetrických rovinách, ako je znázornené na obr. ALEEXL1.12. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Bearing Surface“ (Oporná plocha).

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0012.jpg' | relative_url }})

Geometria matrice

### Oporná plocha

Na stránke „Bearing Surface“ (Oporné plochy) definujeme oporné plochy a pridáme ich do zoznamu oporných plôch. Pre tento objekt formy existujú 3 oporné plochy. V ľavom stĺpci ponechajte režim **Select** (Výber). Na definovanie opornej plochy vyberieme všetky výplne súvisiace s ložiskom a klikneme na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}). Po definovaní prvej ložiskovej plochy sa do zoznamu pridá zvýraznená ložisková plocha s **ID <1>**. Potom podobným spôsobom definujeme druhú a tretiu ložiskovú plochu. Kompletný zoznam ložiskových plôch je zobrazený na obr. ALEEXL1.13. Prvá, druhá a tretia ložisková plocha sú v zobrazení geometrie matrice zvýraznené žltou, červenou, resp. oranžovou farbou. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Bearing Control Points (Kontrolné body ložísk).

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0013.jpg' | relative_url }})

Oporná plocha

### Kontrolné body ložiska

Po definovaní ložiskovej plochy sa vygeneruje virtuálne ložisko a rozloženie jeho dĺžky na účely definovania kontrolných bodov ložiska (pozri obr. ALEEXL1.14.). V „**3D_SS_EX_Lab1**“ predstavíme, ako definovať kontrolné body ložiska na úpravu dĺžky ložiska. V tomto cvičení nebudeme dĺžku ložiska upravovať, preto nie je potrebné definovať kontrolné body ložiska. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na ďalšiu stránku.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0014.jpg' | relative_url }})

Pôvodné nastavenia dosadacích plôch

### Pohyb matrice

V dialógovom okne „Pohyb“ ponechajte hodnotu **Rýchlosť** na **0** mm/s. Prejdite na ďalšiu stránku kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

## Obrobok

Názov objektu „Workpiece“ ponechajte v predvolenom znení **Workpiece**. Nastavte **teplotu** objektu „Workpiece“ na **400** °C a typ objektu ponechajte ako **Plastic**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Geometry“.

### Geometria obrobku

Kliknite na „Importovať geometriu z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a načítajte súbor **ALE_Workpiece_Geo.stl** zo zložky 3D/LABS, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). V dialógovom okne **Symetria** nastavte pre obrobok **Rovinnú symetriu** na **symetrických rovinách**, ako je znázornené na obrázku (pozri obr. ALEEXL1.15.). V tomto laboratórnom cvičení je dĺžka extrudátu 120 mm, dĺžka v kontajneri je 150 mm. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku typu generovania siete.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0015.jpg' | relative_url }})

Geometria obrobku

### Typ generovania siete obrobku

Na stránke **Typ generovania siete** sú k dispozícii dve možnosti generovania siete pre obrobok ALE. Jednou z nich je **Nástroj na extrudovanie siete** a druhou je **Bežné vytváranie siete**.

V predchádzajúcich verziách pre simulácie ALE a extrudovania v ustálenom stave sa sieť generovala pomocou **Regular Meshing** (generátor sietí DEFORM-3D). Generátor sietí najprv vytvorí povrchovú sieť a následne vygeneruje nestruktúrovanú tetraedrálnu objemovú sieť.

V tomto laboratórnom cvičení si ukážeme, ako vytvoriť extrudovanú sieť pomocou nástroja **Mesh Extruding Utility**.

Pri simuláciách extrudovania metódami ALE a v ustálenom stave môžeme obrobok považovať za súbor troch rôznych oblastí: oblasti kontajnera, oblasti extrudátu a oblasti deformácie. Oblasť kontajnera a oblasť extrudátu sú jednoduché extrudované tvary, zatiaľ čo oblasť deformácie je oveľa zložitejšia.

Nástroj **Mesh Extruding Utility** umožňuje používateľom najprv vytvoriť sieť iba pre komplexnú deformovateľnú oblasť pomocou generátora sietí DEFORM-3D. Následne je možné vytvoriť vytlačenú sieť pre oblasť kontajnera a oblasť výlisku pridaním vrstiev prvkov v týchto oblastiach.

Vyberte položku **Mesh Extruding Utility** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). Systém vám ponúkne šablónu na vytvorenie siete pre tri oblasti.

V kontextovom menu v oblasti zobrazenia vyberte možnosť „**Zobraziť pravítka**“, ako je znázornené na obr. ALEEXL1.16, čím sa zobrazia pravítka, ktoré nám pomôžu pri umiestňovaní jednotlivých oblastí.

Predvolené nastavenie týchto troch oblastí vychádza z prierezových plôch obrobku v smere osi Z. Rozdelenie oblastí je znázornené na obr. ALEEXL1.17.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0016.jpg' | relative_url }})

Nástroj na extrudovanie sietí

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0017.jpg' | relative_url }})

Rozdelenie podľa regiónov

V tomto cvičení nastavíme parametre v nástroji **Mesh Extruding Utility**.

Najskôr upravíme deformačnú oblasť. Deformačná oblasť (poddoména) medzi hornou a dolnou červenou čiarou sa použije na vytvorenie pravidelnej siete pomocou generátora sietí DEFORM-3D. Hustotu siete teda môžeme určiť bežným spôsobom, podobne ako pri nastavení v okne „Mesh Window“.

Nechajte 3 zóny a pretiahnite čiary zón do požadovaných polôh. Hornú červenú čiaru pretiahnite približne na Z = 25 mm, druhú červenú čiaru na Z = 5 mm, tretiu červenú čiaru na Z = -15 mm a spodnú červenú čiaru na Z = -25 mm.

Zóna 1 určí hustotu siete v blízkosti oblasti kontajnera. Zóna 2 určí hustotu siete v blízkosti vstupu ložiska. Zóna 3 určí hustotu siete v blízkosti oblasti extrudátu. V dialógovom okne **Nastavenie siete v oblasti deformácie** vyberte typ „**Absolútny**“ a nastavte **Minimálnu veľkosť prvku** na „**2** mm“. V tabuľke Oblast' deformácie nastavte Veľkosť prvku pre Zónu 1 na „6 mm“, pre Zónu 2 na „2 mm“ a pre Zónu 3 na „3 mm“. Ak je oblasť deformácie oveľa zložitejšia, mali by sme pridať zóny kliknutím na „![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }})“ a definovať ich vhodné hustoty siete.

Potom v časti „Container Region“ odstráňte 1 zónu kliknutím na „![]({{ '/assets/icons/pre_icons/mo_delete_symmetry_icon.jpg' | relative_url }})“. V zóne 1 nastavte počet vrstiev na „10“.

V oblasti extrudátu ponechajte 2 zóny a presuňte čiaru zóny (modrá čiara) na hodnotu Z = -50 mm. Nastavte počet vrstiev na hodnotu „10“ v zóne 1 a na hodnotu „12“ v zóne 2.

Nastavenia upravených parametrov v nástroji **Mesh Extruding Utility** sú znázornené na obr. ALEEXL1.18.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0018.jpg' | relative_url }})

Nastavenie parametrov pre nástroj na extrudovanie siete

Na obr. ALEEXL1.18 vidíme v spodnej časti widgetu tri tlačidlá – **Predvolené nastavenie**, **Náhľad** a **Vytvoriť**. Tlačidlo **Predvolené nastavenie** obnoví všetky parametre siete na predvolené hodnoty. ****Náhľad** vytvorí geometriu subdomény a vygeneruje povrchovú sieť pre deformovanú oblasť. **Vytvoriť** vygeneruje objemovú sieť pre deformovanú oblasť a pridá vrstvené prvky do kontajnerovej a extrudovanej oblasti. Ak predtým nebolo kliknuté na **Náhľad**, tlačidlo **Vytvoriť** vykoná všetky úlohy postupne.

Kliknutím na tlačidlo **Generovať** vygenerujete sieť obrobku. Vygenerovaná sieť obrobku je znázornená na obr. ALEEXL1.19. Jasne vidíme pravidelnú sieť v oblasti deformácie a extrudovanú sieť v oblastiach nádoby a extrudátu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Materiál.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0019.jpg' | relative_url }})

Vytvorená sieť obrobku

### Materiál obrobku

Ako materiál pre obrobok zadajte **ALUMINUM-6061[70-1000F(20-550C)]** a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s okrajovými podmienkami.

### Okrajová podmienka obrobku

Systém po vytvorení siete automaticky priradil obrobku rovinu symetrie BCC (pozri obr. ALEEXL1.20.).

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0020.jpg' | relative_url }})

Symetria BCC obrobku

Pri extrudovaní metódou ALE a v ustálenom stave je potrebné na konci extrudátu definovať voľnú plochu. V dialógovom okne **Okrajové** **podmienky** kliknite na **Voľná****povrch** v stromovej štruktúre, otočte obrobok tak, aby ste videli spodnú časť extrudátu, vyberte spodnú plochu a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}), aby ste pridali okrajovú podmienku voľného povrchu (pozri obr. ALEEXL1.21.).

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0021.jpg' | relative_url }})

BCC voľného povrchu obrobku

Systém po vytvorení siete automaticky priradil obrobku výmenu tepla s okolím typu BCC. V prípade extrudovania ALE a v ustálenom stave by sa voľná plocha nemala priradiť k výmene tepla s prostredím BCC, preto by sme mali odstrániť existujúcu výmenu tepla s prostredím BCC na voľnej ploche kliknutím na „**Definované**“ a ![]({{ '/assets/icons/pre_icons/mo_delete_bcc_button.jpg' | relative_url }}). Predefinujeme výmenu tepla s prostredím BCC. V ľavom výberovom paneli kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}), aby ste vybrali všetky povrchy, potom kliknite na voľný povrch a symetrické povrchy, aby ste zrušili ich výber. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}), aby ste pridali výmenu tepla s prostredím BCC. Definovaná výmena tepla s prostredím BCC je znázornená na obr. ALEEXL1.22. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Control“.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0022.jpg' | relative_url }})

Výmena tepla s okolitým prostredím v objemovej bunke (BCC) obrobku

## Ovládacie prvky

Na stránke „Ovládanie“ môžeme pomocou ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) nastaviť polohy objektov.

Všetky súčasti formy boli naimportované zo súborov .stl. Kontajner aj forma sa nachádzali na správnych miestach. Závit je vzdialený od obrobku. Preto musíme posunúť závit nadol, aby sa dotýkal obrobku.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) a zadajte polohu ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Ako polohovací objekt vyberte **Ram** a ako referenčný bod **Obrobok**. Skontrolujte, či je smer priblíženia **–Z**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) a potom na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Kontakt.

## Kontakt

Pri vstupe na stránku „Vzťahy medzi objektmi“ sa zobrazí okienko (pozri obr. ALEEXL1.23.), v ktorom sa používateľ opýta, či chce použiť špeciálny algoritmus na generovanie kontaktov na vytvorenie úplného kontaktu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0023.jpg' | relative_url }})

Vyskakovacie okno FULL CONTACT GENERATION

Na stránke „Kontakt“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}), aby ste vytvorili všetky vzťahy obrobku s ostatnými objektmi. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}), aby ste vygenerovali úplný kontakt obrobku s ostatnými objektmi. Následne upravíme nastavenie parametrov pre kontaktné vzťahy obrobku.

Vyberte vzťah **Ram – Obrobok** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Nastavte oddeliteľnosť kontaktu na „**Neoddeliteľné**“, trenie **šmykové** na „**1,0**“ a koeficient prenosu tepla na „**11,0**“.

Vyberte vzťah **Kontajner – Obrobok** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Nastavte oddelenie kontaktov na hodnotu „**Neoddeliteľné**“, trenie **šmykové** na hodnotu „**1,0**“ a koeficient prenosu tepla na hodnotu „**11,0**“.

Vyberte vzťah **Matrica – Obrobok** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Definujte oddelenie kontaktov ako „**Neoddeliteľné**“, trenie **šmykové** ako „**0,4**“ a koeficient prenosu tepla ako „**11,0**“ (pozri obr. ALEEXL1.24.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na ovládacie prvky krokov.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0024.jpg' | relative_url }})

Úplný kontakt s obrobkom

## Ovládacie prvky krokov

Kliknutím na položku „![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})“ v hornom paneli ponúk prejdete do expertného režimu na ovládanie krokov.

### Kroky simulácie

V dialógovom okne Simulačné kroky ![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }}) nastavte **Počet simulačných krokov** na hodnotu „**2000**“ a **Krok****Prírastok****na****uloženie** na hodnotu „**100**“. Nastavte **Primárny výlisok** na hodnotu „**2 – Ram**“ (pozri obr. ALEEXL1.25.).

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0025.jpg' | relative_url }})

Nastavenie simulačného kroku

Pri simulácii extrudovania metódou ALE, keďže medzi obrobkom a nádobou nie je žiadna medzera, môžeme použiť konštantný krok. Pri simulácii extrudovania metódou ALE však musíme pri nastavení časového kroku zohľadniť obmedzenia vyplývajúce z minimálnej veľkosti prvkov a rozmerov obrobku.

  1. V tomto laboratórnom cvičení je minimálna veľkosť prvku 2 mm. Podľa súboru „3D_Lagrangian_EX_Lab1“ je rýchlosť pohybu extrudátu 21,16 mm/s, takže vhodný čas na jeden krok piestu by mal byť 0,03 s/krok.

  2. Materiál by mal aspoň úplne vytekať z celého extrudátu. V tomto laboratórnom cvičení je dĺžka extrudátu 120 mm, minimálny čas potrebný na to, aby materiál vytekol z voľnej plochy (konca extrudátu), je 5,67 (120/21,16) s. Ak chceme simulovať 2000 krokov, minimálny prírastok časového kroku by mal byť 0,00284 s/krok.

  3. Materiál nemôže z nádoby vytekať úplne. V tomto laboratórnom experimente je dĺžka v nádobe 150 mm, rýchlosť pohybu piestu je 4 mm/s, maximálny čas potrebný na úplné vytečenie materiálu z nádoby je 37,5 (150/4) s. Ak chceme simulovať 2000 krokov, maximálny prírastok časového kroku by mal byť 0,01875 s/krok.

Na základe vyššie uvedených troch aspektov môžeme ako veľkosť kroku zvoliť **0,01** s/krok. V dialógovom okne **Step****increment![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}) **nastavte definíciu kroku riešenia na **Čas**. Nastavte ovládací prvok „Krok“ na hodnotu „Konštanta“ a definujte ho ako „**0,01**“ s/krok (pozri obr. ALEEXL1.26.).

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0026.jpg' | relative_url }})

Nastavenie krokového prírastku

###  Kritériá na ukončenie

V dialógovom okne **Kritériá zastavenia** ![]({{ '/assets/icons/pre_icons/mo_stopping_criteria.jpg' | relative_url }}) kliknite na kartu **ALE****Steady****State** a zrušte zaškrtnutie políčka „**Zapnúť riadenie zastavenia v ustálenom stave**“, ak ešte nie je odškrtnuté (pozri obr. ALEEXL1.27.).

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0027.jpg' | relative_url }})

Ovládanie zastavenia

### Nastavenia dvojitých obmedzení

V prípade extrudovania metódou ALE a v ustálenom stave systém pri simulácii automaticky vygeneruje dvojité obmedzenia.

## Vytvoriť databázu

Potom prejdite na stránku „Generate DB“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali, či sa pri nastavení na niečo nezabudlo, a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) na vytvorenie databázy. Pozrite si správu na karte „Message“, ktorá informuje o stave vytvárania databázy.

## Spustenie simulácie

Po vytvorení databázy prejdite do simulačného režimu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. ALEEXL1.28.Použite predvolenú možnosť **Pokračovať****Spustiť** na výber možnosti „**Pokračovať od posledného kroku**“ (od kroku -1) a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Ak chcete nastaviť parametre MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}). Rozbalí sa okno „Run Options“, v ktorom sa zobrazia možnosti na nastavenie parametrov MPI pre simuláciu (maximálny počet procesorov, ktorý je možné nastaviť, závisí od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0028.jpg' | relative_url }})

Spustiť okno simulácie

Priebeh simulácie môžete sledovať na kartách „Simulation Message“ a „Simulation Log“; uistite sa, že je zaškrtnutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Používateľ môže sledovať proces extrudovania na simulačných grafoch v priebehu simulácie až do dosiahnutia zadaného kroku.

## Zrýchlená aktualizácia stavových premenných

Po dokončení vyššie uvedenej simulácie uložte projekt kliknutím na ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) v šablóne extruzie. Nastavenie simulácie a výsledky simulácie tohto projektu by sme si mali uchovať a vykonať simuláciu zrýchlenia v rámci iného projektu.

### Simulácia postupného zvyšovania zrýchlenia

V ponuke Súbor ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) kliknite na **Nový**![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) a v oboch vyskakujúcich oknách s otázkou kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}); otvorí sa nový projekt s oknom Nový projekt.

V okne „Nový projekt“ zadajte názov projektu ako „**3D_ALE_EX_Lab1_ACC**“, zaškrtnite políčko **Kopírovať existujúci projekt**, kliknite na **Prehľadávať**, vyhľadajte projekt „3D_ALE_EX_Lab1“ a v okne Nový projekt kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), ako je znázornené na obr. ALEEXL1.29.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0029.jpg' | relative_url }})

Nový projekt na urýchlenie modernizácie laboratória

V dialógovom okne **Nastavenie simulácie** zmeňte hodnoty **Aktualizácia deformácie****** a **Aktualizácia teploty****** v položke „Zrýchlenie“ na **50** na krok, čo znamená, že v nasledujúcej simulácii sa aktualizácia zrýchlenia vykoná 50-krát. Ostatné nastavenia parametrov ponechajte bez zmien. Nastavenie simulácie je znázornené na obr. ALEEXL1.30.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0030.jpg' | relative_url }})

Nastavenia simulačného prostredia s akceleráciou aktualizácie stavových premenných

Prejdite na stránku **Step****Control**. V dialógovom okne **Simulácia****kroky** nastavte **Počet simulačných** krokov na hodnotu „**40**“ a **Krok prírastku na uloženie** na hodnotu „**2**“ (pozri obr. ALEEXL1.31.).

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0031.jpg' | relative_url }})

Kroky simulácie zrýchlenia

Skontrolujte, či je nastavenie zrýchlenia definované na stránke „Step Control“ (Krokové riadenie) -> v dialógovom okne **Advanced** (Pokročilé) -> na stránke **Frequency** (Frekvencia) (pozri obr. ALEEXL1.32.).

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0032.jpg' | relative_url }})

Nastavenia zrýchlenia v časti „Frekvencia“

Potom prejdite na stránku „Generate DB“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali, či sa pri nastavení na niečo nezabudlo, a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) na vygenerovanie databázy. Pozrite si správu na karte „Message“, ktorá informuje o stave generovania databázy.

### Spustenie simulácie

Po vytvorení databázy prejdite do režimu simulácie výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. ALEEXL1.28.Použite predvolenú možnosť **Pokračovať****Spustiť** na výber možnosti „**Pokračovať od posledného kroku**“ (od kroku -1) a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

## Následné spracovanie

Po dokončení simulácie procesu extrudovania s urýchlením aktualizácie stavových premenných môžeme výsledky simulácie porovnať v postprocesore.

V hlavnom okne grafického rozhrania DEFORM označte súbor „3D_ALE_EX_Lab1.DB“ a potom kliknutím na ![]({{ '/assets/icons/pre_icons/mo_post_processor_gui_link.jpg' | relative_url }}) otvorte súbor „**3D_ALE_EX_Lab1.DB**“ v postprocesore DEFORM.

V programe DEFORM-2D/3D DEFORM Post kliknite v hornom paneli ponúk na položku **Súbor**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Otvoriť**, vyberte súbor „**3D_ALE_EX_Lab1_ACC.DB**“ a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

V hornom paneli ponúk kliknite na **Windows![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Usporiadať vertikálne**. Vidíme, že súbory „3D_ALE_EX_Lab1.DB“ aj „3D_ALE_EX_Lab1_ACC.DB“ sú otvorené v programe DEFORM-2D/3D Post. Takto môžeme porovnať výsledky simulácie z oboch databáz v jednom okne.

Pri simulácii zrýchlenia platí: efektívny krok = simulačný krok × frekvencia zrýchlenia. Napríklad v tomto laboratórnom cvičení je frekvencia zrýchlenia 50, takže efektívny krok je 1000 v simulačnom kroku 20 a efektívny krok je 2000 v simulačnom kroku 40. Efektívny krok simulácie zrýchlenia zodpovedá simulačnému kroku simulácie bez zrýchlenia.

V okne zobrazenia kliknite pravým tlačidlom myši a zaškrtnite políčka „**DB Info**“ aj „**Title**“, aby sa zobrazil názov databázy a krok simulácie.

Porovnania efektívneho deformácie a teploty obrobku v poslednom kroku sú uvedené na obr. ALEEXL1.33 a obr. ALEEXL1.34. Používateľ môže tiež porovnať výsledky simulácie v ďalších príslušných krokoch simulácie.

Z porovnania výsledkov simulácie je zrejmé, že stavové premenné sa v príslušnom simulačnom kroku veľmi dobre zhodujú. Na druhej strane, podľa súborov správ z tohto laboratórneho cvičenia trvá simulácia bez akcelerácie približne 2 hodiny, zatiaľ čo simulácia s akceleráciou trvá približne 20 minút. Aktualizácia stavových premenných pomocou akcelerácie je teda užitočným spôsobom, ako skrátiť čas simulácie pri simulácii extrudovania metódou ALE.

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0033.jpg' | relative_url }})

Efektívne rozdelenie napätia v poslednom kroku

![]({{ '/assets/images/labs/extrusion_labs/ale_extrusion_lab1/image0034.jpg' | relative_url }})

Rozloženie teploty v poslednom kroku
