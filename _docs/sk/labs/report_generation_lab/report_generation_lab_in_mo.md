---
lang: sk
title: "Laboratórium generovania správ v MO"
---

# Laboratórium generovania správ v MO

V tejto funkcii generovania laboratórnych správ je vysvetlená v interaktívnom aj dávkovom post režime pre Spike_Forging Lab Project.

1.1.1. Skopírujte existujúci projekt

1.1.2. Pridajte operáciu generovania hlásení

1.1.3. Pridať kapitoly

1.1.4. Definujte prvé kapitoly

1.1.5. Definujte druhú kapitolu

1.1.6. Definujte tretiu kapitolu

1.1.7. Definujte štvrtú kapitolu

1.1.8. Definujte piatu kapitolu

1.1.9. Definujte šiestu kapitolu

1.1.10. Simulovať projekt

1.1.11. Preskúmanie správy

## Generovanie hlásení v režime dávkového postu

Ak sa už praktizuje 3D MO Basic Labs: Lab [03 Spike Forging]({{ '/docs/sk/labs/basic_labs/3d_labs/lab03_spike_forging/' | relative_url }}), potom otvorte projekt Spike Forging v MO výberom súboru projektu z Deform GUI Main a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_integrated_manufacturing_proc.jpg' | relative_url }}). V opačnom prípade skopírujte súbor projektu, ktorý je k dispozícii v inštalačnej ceste, ako je vysvetlené nižšie.

### Skopírujte existujúci projekt

Vytvorte nový problém buď výberom * * Súbor * *![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Problem Setup (Nastavenie problému). Vyberte prepínač „**Integrovaný výrobný proces** “ a prepínač „**Angličtina** “ v poli jednotky, ako je znázornené na obr. RGL1.1.

Definujte názov problému ako "**Spike_Forging** " a uistite sa, že je zapnuté začiarkavacie políčko "Zobraziť dialógové okno možností" (ak nezapneme začiarkavacie políčko "Zobraziť dialógové okno možností", potom nedostaneme dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0001.jpg' | relative_url }})

Otvoriť nový problém z hlavného DEFORMAČNÉHO grafického rozhrania

Otvorí sa sprievodca viacerými operáciami a vyberte prepínač Kopírovať existujúci projekt. Prehľadajte súbor projektu pre predtým uložený projekt a otvorte súbor Spike_Forging.moproj alebo prejdite z inštalačnej cesty **/3d/LABS/Spike_Forging/Spike_Forging.moproj* * (pozri obr. RGL1.2.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) skopírujte a otvorte projekt.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0002.jpg' | relative_url }})

Skopírujte existujúci projekt Spike_Forging

Vyberte operáciu **Heat Transfer ** v editore operácií a vyberte Generate DB in operation tree to Generate DB, ako je znázornené na obr. RGL1.3. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0003.jpg' | relative_url }})

Vytvoriť databázu pre 1. operáciu

### Pridať operáciu generovania hlásení

Pridajte operáciu generovania správy z prieskumníka operácie MO, ako je znázornené na obr. RGL1.4.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0004.jpg' | relative_url }})

Pridať operáciu generovania správy

Kliknutím na operáciu správy v editore operácií otvoríte operáciu generovania správy, ako je znázornené na obr. RGL1.5.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0005.jpg' | relative_url }})

Operácia generovania otváracej správy

### Pridať kapitoly

V okne vlastností správy môže používateľ pridať viac ako jednu kapitolu a názov kapitoly je možné zmeniť dvojitým kliknutím na pole názvu.

Tieto kapitoly pomáhajú generovať správy o výsledkoch rôznych operácií alebo rôznych rozsahov operácií samostatne ako nové kapitoly. V tomto laboratóriu pridávame 6 kapitol, takže okrem predvolenej kapitoly kliknite päťkrát na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať kapitolu). Prvé 4 kapitoly budú použité na pokrytie každej zo 4 operácií, piata kapitola na vykreslenie súhrnu teploty od prvej do poslednej operácie a šiesta kapitola na vykreslenie krivky záťažového zdvihu pre 2 tvarovacie operácie. Názvy kapitol sa automaticky aktualizujú v závislosti od rozsahu operácií zvoleného v príslušnej kapitole alebo používateľ môže definovať vlastný názov. Pre prvé 4 kapitoly v tomto laboratóriu sa názov kapitoly aktualizuje, keď v príslušnej kapitole vyberieme rozsah operácií. Vlastný názov pre 5. kapitolu definujeme ako **„Zhrnutie teploty zo všetkých operácií“** a 6. kapitolu ako „** Operácie tvárnenia krivky nepretržitého zaťaženia ** “ namiesto rozsahu operácií. Potom okno správy vyzerá tak, ako je znázornené na obr. RGL1.6.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0006.jpg' | relative_url }})

Okno správy so 6 kapitolami

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujete pridané kapitoly.

### Definujte prvé kapitoly

Pre prvú kapitolu vyberte ** Konvekcia vzduchu ** **prevádzka** ako spustenie a ukončenie prevádzky a začiarknite iba políčko Stavová premenná pre sekcie, ako je znázornené na obr. RGL1.7.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0007.jpg' | relative_url }})

Nastavenia kapitoly 1

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujete stavovú variabilnú časť. Prijmite zvolené kroky názvu stavovej premennej sekcie a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre pridanie stavových premenných výstupov. (Pozri obr. RGL1.8.).

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0008.jpg' | relative_url }})

Základné nastavenia stavovej variabilnej sekcie

Jedným kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) pridáte premennú stavu teploty a kliknete na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (Pozri obr. RGL1.9.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0009.jpg' | relative_url }})

Okno výberu stavového variabilného výstupu

Vyberte objekty ako obrobok a záber ako definované používateľom a upravte záber podľa potreby pomocou možností úpravy zobrazenia posúvaním, priblížením, otočením a zväčšením. (Pozri obr. RGL1.10.) Používateľ má tiež možnosti záberu, ako sú rôzne zobrazenia osí, ako napríklad +X,-X,+Y atď., Izometrické, výber typu obrysu, rozsah obrysu, typ farebného pruhu a automatické zobrazenie. Vyberte rozloženie PDF ako 9, ako je znázornené na obr. RGL1.10.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0010.jpg' | relative_url }})

Okno stavových premenných nastavení teploty

Začiarknite políčko **Zahrnúť 3D model* ** *(3D PDF)** v dolnej časti okna, ak chcete zahrnúť 3D model do súboru PDF. (Pozri obr. RGL1.10.)

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujete druhú kapitolu.

### Definujte druhú kapitolu

Podobne ako v prvej kapitole vyberte pre druhú kapitolu iba operáciu „** H ** ** eat Resting * * * “ (2. operácia) a pridajte premennú teplotného stavu iba v 3 krokoch, ako je znázornené na obr. RGL1.11 a obr. RGL1.12.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0011.jpg' | relative_url }})

Nastavenia premennej stavu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a raz kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}), aby ste pridali premennú stavu teploty.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0012.jpg' | relative_url }})

Okno výberu stavového variabilného výstupu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vyberte objekt obrobku, typ zobrazenia definovaný používateľom a rozloženie PDF ako 9. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujete tretiu kapitolu.

### Definujte tretiu kapitolu

V tejto kapitole vyberte operáciu „**Formovanie** “ (3. operácia ) ako spustenie a ukončenie operácie a skontrolujte sekcie Metal flow, Graph a State variable (pozri obr. RGL1.13), pretože ide o tvarovaciu operáciu na kontrolu toku materiálu, grafu zaťaženia zdvihu pre primárnu matricu a premenných stavu deformácie ako rôznych krokov.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0013.jpg' | relative_url }})

Nastavenia kapitoly 3

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a definujte kroky kovového toku. Prijmite kroky Metal flow vybrané ako 7 a v ovládacích prvkoch definujte rozloženie PDF ako 9. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujete graf záťažového zdvihu. (Pozri obr. RGL1.14)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0014.jpg' | relative_url }})

Nastavenia prietoku kovu

Zmeňte názov sekcie grafu z **grafu (zdvih zaťaženia)** na ** zdvih zaťaženia * ***grafu**, ako je znázornené na obr. RGL1.15 a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pokračujte v definícii grafu.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0015.jpg' | relative_url }})

Okno s názvom sekcie grafu

Jedným kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) pridáte záťažový zdvih ako premenné grafu, vyberte premennú osi X ako zdvih a premennú osi Y ako záťaž Z, ako je znázornené na obrázku RGL1.16.

.![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0016.jpg' | relative_url }})

Okno definície premenných grafov

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vyberte objekt ako primárnu matricu, ako je znázornené na obr. RGL1.17.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0017.jpg' | relative_url }})

Okno výberu objektov grafu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a definujte stavovú premennú. Prijmite 7 krokov vybraných pre stavové premenné a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre pridanie stavových premenných.

Dvakrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) a vyberte Efektívne napätie a Efektívne premenné napätia, ako je znázornené na obr. RGL1.18 . a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre definovanie každého nastavenia zobrazenia variabilného obrysu SATE.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0018.jpg' | relative_url }})

Okno pridávania premenných stavu

Vyberte Objekty ako jediný obrobok, záber ako definovaný používateľom a rozloženie PDF ako 9. Tiež skontrolujte Zahrnúť 3D model (3D PDF) pre získanie 3D modelu v PDF a podľa potreby upravte zobrazenie záberu.

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujete štvrtú kapitolu.

### Definujte štvrtú kapitolu

Podobne ako v tretej kapitole vyberte pre štvrtú kapitolu len poslednú tvarovaciu operáciu „** ** Kovanie * * Fúkanie 2 * *“ a pridajte sekcie Metal Flow, Stroke-Z Load Graph a Effective Stress a efektívne deformačné stavy variabilných obrysových rezov.

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujete piatu kapitolu.

### Definujte piatu kapitolu

Pre túto kapitolu vyberte spustenie operácie ako ** Konvekcia vzduchu ** a ukončenie operácie ako **Kovací úder 2** a skontrolujte časti Súhrn, Stavová premenná a Sledovanie bodu. (Pozri obr. RGL1.19.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0019.jpg' | relative_url }})

Nastavenia kapitoly 5

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujete sekcie. Prijmite názov súhrnnej časti ako Súhrn a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (Pozri obr. RGL1.20)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0020.jpg' | relative_url }})

Okno s názvom súhrnnej sekcie

Jedným kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) pridáte časovú krivku teploty Vs od prvej po poslednú operáciu. Takže vyberte premennú osi X ako premennú času a osi Y ako teplotu, ako je znázornené na obr. RGL1.21.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0021.jpg' | relative_url }})

Okno pridania súhrnného grafu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vyberte obrobok ako objekt, ako je znázornené na obr. RGL1.22. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujete stavovú premennú.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0022.jpg' | relative_url }})

Okno výberu objektu súhrnného grafu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre stav premenného počtu krokov na stránke výberu krokov so zachovaním 7 krokov. Raz kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) a pridajte premennú stavu teploty. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vyberte objekt ako Všetky, záber ako User Defined a rozloženie PDF ako 9. Pre túto kapitolu vygenerujeme stavový variabilný obrys bez 3D modelu, preto nezačiarknite políčko Zahrnúť 3D model (3D PDF), ako je znázornené na obr. RGL1.23.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0023.jpg' | relative_url }})

Okno s nastaveniami premennej stavu teploty

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujete sekciu sledovania bodov.

Prijmite názov sekcie sledovania bodov ako „**Bodová stopa** “, ako je znázornené na obr. RGL1.24. a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0024.jpg' | relative_url }})

Okno názvu sekcie sledovania bodov

Potvrďte, že je vybratá možnosť Pohyblivé body, a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button2.jpg' | relative_url }}) vyberte body, ktoré sa majú sledovať na obrobku.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0025.jpg' | relative_url }})

Okno výberu bodu sledovania bodu

Defien tri body pre sledovanie bodu nad obrobkom, ako je znázornené na obr. RGL1.26. a tieto body sa pridajú do tabuľky definovaných bodov. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno definície bodov a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0026.jpg' | relative_url }})

Okno Definovať body

Jedným kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) vyberte premennú stavu teploty a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) ukážte nastavenia grafu stopy.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0027.jpg' | relative_url }})

Okno výberu premennej stavu sledovania bodu

Vyberte objekt obrobku a možnosť zobrazenia iba ako graf, ako je znázornené na obr. RGL1.28.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0028.jpg' | relative_url }})

Nastavenia grafu sledovania bodov

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujete šiestu kapitolu.

### Definujte šiestu kapitolu

Vyberte**Spustenie operácie** ako **Tvarovanie** a **Koniec****operácie** ako ***Kovanie * * Fúkanie 2** a skontrolujte sekciu Graf, ako je znázornené na obr. RGL1.29.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0029.jpg' | relative_url }})

Okno nastavení kapitoly 6

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujete graf zaťaženia zdvihu Z pre primárnu matricu v operácii tvárnenia a kovania vyfukovania 2.

Jedným kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) vyberte os X ako zdvih a os Y ako Z-zaťaženie a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vyberte objekt ako primárnu matricu.

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujete stránku správy, začiarknite políčka typu dokumentácie PDF aj ppt.

### Simulovať projekt

Kliknite na ikonu projektu ![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) a vyberte tlačidlo režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) na spustenie simulácie.

Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať z posledného kroku** “ (z kroku -1) a potom vyberte režim simulácie ako prepínač * * Interaktívne * *. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) pre spustenie simulácie.

### Skontrolujte správu

Po ukončení simulácie všetkých operácií pred generovaním správy začne generovanie správy generovať správu pre vybrané stavové premenné a grafy. Automaticky sa otvorí aj vygenerovaný súbor ppt. Prehľadávajte adresár problémov z prieskumníka a vyhľadajte adresár DEF_REPORT, aby ste našli vygenerované súbory správ PDF a ppt.

Otvorte súbory ppt a PDF a prejdite si správy kapitoly Wise.

Kapitola 1

Pre kapitolu 1 Teplota stav variabilný obrys ppt prehrá všetkých 9 snímok na jednej snímke, keď klikneme na Prezentácia (F5). (Pozri obr. RGL1.30.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0030.jpg' | relative_url }})

Kapitola 1 Variabilná snímka stavu teploty ppt

PDF zobrazí 9 obrázkov teplotných stavov variabilných obrysov obrobku na jednej stránke, ako je znázornené na obr. RGL1.31.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0031.jpg' | relative_url }})

Kapitola 1 Premenná stavu teploty na stránke PDF

3D model pre premennú stavu teploty sa zobrazí pre prevádzku konvekcie vzduchu v poslednom kroku v PDF, ako je znázornené na obr. RGL1.32.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0032.jpg' | relative_url }})

Kapitola 1 Variabilný stav teploty 3D model PDF stránka

Používateľ môže použiť nižšie uvedené možnosti 3D modelu na otáčanie, posúvanie, priblíženie, zmenu oblasti snímania obrázkov, meranie rozmerov, vkladanie komentárov, výber rôznych zobrazení, prepínanie stromu modelu, rôzne režimy vykresľovania, možnosti extra svetla, zmenu farby pozadia a sekciu objektu.

Možnosti PDF 3D modelu sú uvedené nižšie,

**Rotate![]({{ '/assets/icons/pre_icons/mo_report_pdf_rotate.jpg' | relative_url }}) **: Pomocou tejto možnosti môže používateľ otočiť objekt okolo stredu obrazovky.

**Spin![]({{ '/assets/icons/pre_icons/mo_report_pdf_spin.jpg' | relative_url }}) **: Pomocou tejto možnosti môže používateľ otáčať objekt okolo stredu objektu.

**Pan** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_pan.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ presunúť objekt a upraviť oblasť zobrazenia bez zmeny veľkosti objektu.

** Zoom![]({{ '/assets/icons/pre_icons/mo_report_pdf_zoom.jpg' | relative_url }})* *: Pomocou tohto používateľa môžete zmeniť veľkosť oblasti objektu.

**Fly![]({{ '/assets/icons/pre_icons/mo_report_pdf_fly.jpg' | relative_url }}) **: Výberom tejto možnosti, ak používateľ podrží ľavé tlačidlo myši a presunie myš, objekt sa presunie nahor alebo bude lietať.

** Vlastnosti fotoaparátu **![]({{ '/assets/icons/pre_icons/mo_report_pdf_cam.jpg' | relative_url }}) :

**3D merací nástroj** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_meassure.jpg' | relative_url }}): Pomocou tohto používateľa môžete zmerať rozmery objektu.

**Pridať 3D komentár** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_3d_comment.jpg' | relative_url }}): Používateľ môže pridať komentáre výberom bodu na objekte.

**Predvolené zobrazenie** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_home.jpg' | relative_url }}): Pomocou tohto sa zobrazí predvolené zobrazenie objektu, v predvolenom zobrazení sa meranie alebo pridanie komentára uloží ako nové zábery. Používateľ môže neskôr vybrať zobrazenie merania alebo 3DCommentView, aby pozoroval nameraný rozmer alebo pridal komentáre. (Pozri obr. RGL1.33.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0033.jpg' | relative_url }})

Zobraziť výberové pole

Pridané komentáre alebo merané rozmery je možné odstrániť alebo upraviť pomocou možností kliknutia pravým tlačidlom myši.

Používateľ môže tiež zvoliť štandardné režimy zobrazenia, ako sú Iso Plus, Iso Minus, X Plus, Y Plus atď.

**Prepnúť model Tee** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_tog.jpg' | relative_url }}): Pomocou tohto používateľa sa strom modelu dostane na ľavú stranu stránky PDF, v tomto strome sa zobrazia rôzne zobrazenia a komentáre 3D modelu. Poskytuje aj ďalšie možnosti zobrazenia, ako je predchádzajúce zobrazenie alebo ďalšie zobrazenie.

**Použite perspektívnu projekciu** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_proj.jpg' | relative_url }}): Toto premietne viditeľnú prednú plochu objektu.

** Režim vykresľovania modelu ** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_render.jpg' | relative_url }}) : Toto poskytuje rôzne typy vykresľovania ako Transparent, Illustration, Wire frame, Solid, Shaded.. atď.

**Povoliť dodatočné osvetlenie** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_light.jpg' | relative_url }}): Použitie tohto používateľa môže povoliť rôzne nastavenia dodatočného osvetlenia.

**Farba pozadia ** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_background.jpg' | relative_url }}) : Pomocou tohto používateľa môžete zmeniť farbu pozadia.

**Prepínanie prierezu** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_section.jpg' | relative_url }}): Aktiváciou tohto používateľa môžete zmeniť vlastnosti roviny prierezu objektu pomocou rozbaľovacieho tlačidla Vlastnosti prierezu.

Kapitola 2

Pre kapitolu 2 Variabilný obrys teplotného stavu ppt prehrá všetky 3 obrázky na jednej snímke, keď klikneme na Prezentácia (F5). (Pozri obr. RGL1.34.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0034.jpg' | relative_url }})

Kapitola 2 Variabilná snímka stavu teploty ppt

PDF zobrazí 3 obrázky teplotných stavov variabilných obrysov obrobku na jednej stránke, ako je znázornené na obr. RGL1.35.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0035.jpg' | relative_url }})

Kapitola 2 Premenná stavu teploty na stránke PDF

3D model pre premennú stavu teploty sa zobrazí pre prevádzku tepelného pokoja v poslednom kroku v PDF, ako je znázornené na obr. RGL1.36.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0036.jpg' | relative_url }})

Kapitola 2 Variabilný stav teploty 3D model PDF stránka

Možnosti 3D modelu nájdete v časti Výsledky v kapitole 1 Možnosti 3D modelu vo formáte PDF.

Kapitola 3

Pre kapitolu 3 Metal Flow, ppt prehrá všetkých 7 uložených krokov obrázkov na jednej snímke, pretože sme vybrali celkom 9 krokov (vrátane prvého a posledného kroku), keď klikneme na prezentáciu (F5). (Pozri obr. RGL1.37.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0037.jpg' | relative_url }})

Kapitola 3 Posúvač ppt s kovovým prietokom

PDF zobrazí všetkých 7 obrazov deformovaného obrobku na jednej strane, ako je znázornené na obr. RGL1.38.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0038.jpg' | relative_url }})

Kapitola 3 Stránka PDF s kovovým prietokom

Pre kapitolu 3 je graf primárnej matrice Z-Load Vs Stroke v ppt, ako je znázornené na obr. RGL1.39.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0039.jpg' | relative_url }})

Kapitola 3 Z-zaťaženie vs graf zdvihu snímka ppt

PDF zobrazuje rovnaký graf zdvihu Z-Load Vs, ako je znázornené na obr. RGL1.40.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0040.jpg' | relative_url }})

Kapitola 3 Z-load vs Stroke graph PDF page

Pre kapitolu 3 Efektívny stav napätia variabilný obrys, ppt prehrá všetkých 7 obrázkov na jednej snímke, keď klikneme na prezentáciu (F5). (Pozri obr. RGL1.41.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0041.jpg' | relative_url }})

Kapitola 3 Efektívny stav napätia variabilná snímka ppt

PDF zobrazí 7 obrázkov stavov efektívneho napätia variabilných obrysov obrobku na jednej stránke, ako je znázornené na obr. RGL1.42.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0042.jpg' | relative_url }})

Kapitola 3 Premenná stavu efektívneho napätia na stránke PDF

3D model pre premennú Efektívny stav napätia sa zobrazí pre operáciu tvárnenia v poslednom kroku v PDF, ako je znázornené na obr. RGL1.43.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0043.jpg' | relative_url }})

Kapitola 3 Efektívny stav napätia premenná 3D model PDF stránka

Pre kapitolu 3 Efektívny stav deformácie variabilný obrys, ppt prehrá všetkých 7 obrázkov na jednej snímke, keď klikneme na prezentáciu (F5). (Pozri obr. RGL1.44.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0044.jpg' | relative_url }})

Kapitola 3 Efektívny stav napnutia variabilná snímka ppt

PDF zobrazí 7 obrázkov Efektívny stav deformácie variabilných obrysov obrobku na jednej stránke, ako je znázornené na obr. RGL1.45.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0045.jpg' | relative_url }})

Kapitola 3 Efektívny stav napnutia premenná strana PDF

3D model pre premennú Efektívny stav deformácie sa zobrazí pre operáciu tvárnenia v poslednom kroku v PDF, ako je znázornené na obr. RGL1.46.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0046.jpg' | relative_url }})

Kapitola 3 Efektívny stav deformácie premenná 3D model PDF stránka

Kapitola 4

Pre kapitolu 4 Metal Flow ppt prehrá všetky 3 uložené obrázky krokov na jednej snímke, pretože sme vybrali celkovo 9 krokov (vrátane prvého a posledného kroku), keď klikneme na prezentáciu (F5). (Pozri obr. RGL1.47.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0047.jpg' | relative_url }})

Kapitola 4 Posúvač ppt s kovovým prietokom

PDF zobrazí všetky 3 obrazy deformovaného obrobku na jednej strane, ako je znázornené na obr. RGL1.48.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0048.jpg' | relative_url }})

Kapitola 4 Stránka PDF s kovovým prietokom

Pre kapitolu 4 je graf primárnej matrice Z-Load Vs Stroke v ppt, ako je znázornené na obr. RGL1.49.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0049.jpg' | relative_url }})

Kapitola 4 Z-zaťaženie vs graf zdvihu ppt snímka

PDF zobrazuje rovnaký graf zdvihu Z-Load Vs, ako je znázornené na obr. RGL1.50.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0050.jpg' | relative_url }})

Kapitola 4 Z-load vs Stroke graph PDF page

Pre kapitolu 4 Efektívny stav napätia variabilný obrys, ppt prehrá všetky 3 obrázky na jednej snímke, keď klikneme na prezentáciu (F5). (Pozri obr. RGL1.51.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0051.jpg' | relative_url }})

Kapitola 4 Efektívny stav napätia variabilná snímka ppt

PDF zobrazí 3 obrázky Efektívne napätie stav variabilné obrysy obrobku na jednej stránke, ako je znázornené na obr. RGL1.52.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0052.jpg' | relative_url }})

Kapitola 4 Premenná stavu efektívneho napätia strana PDF

Keďže nie sme vybraní, začiarkavacie políčko Zahrnúť 3D model 3D PDF model nie je k dispozícii pre kapitolu 4.

Pre kapitolu 4 Efektívny stav deformácie variabilný obrys, ppt prehrá všetky 3 obrázky na jednej snímke, keď klikneme na prezentáciu (F5). (Pozri obr. RGL1.53.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0053.jpg' | relative_url }})

Kapitola 4 Efektívny stav napnutia variabilná snímka ppt

PDF zobrazí 3 obrázky **Efektívne namáhanie** stavové variabilné obrysové obrázky obrobku na jednej stránke, ako je znázornené na obr. RGL1.54.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0054.jpg' | relative_url }})

Kapitola 4 Efektívny stav napnutia premenná strana PDF

Kapitola 5

Pre kapitolu 5 súhrnný graf teploty pre obrobok je od 1. do poslednej operácie v súbore ppt, ako je znázornené na obr. RGL1.55.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0055.jpg' | relative_url }})

Kapitola 5 graf súhrnu teploty pre snímku obrobku ppt

PDF zobrazí súhrnný graf pre teplotu obrobku vo všetkých prevádzkach, ako je znázornené na obr. RGL1.56.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0056.jpg' | relative_url }})

Kapitola 5 graf súhrnu teploty pre stránku PDF obrobku

Pre kapitolu 5 Teplota stav variabilný obrys pre všetky objekty bude hrať prevádzku múdro v rôznych snímkach ppt. Obrys teploty konvekcie vzduchu je uvedený na obr. RGL1.30. Podobne pre obrázky PDF teplotného obrysu pozri obr. RGL1.31.

Kroky obrysu pokojovej teploty tepla v ppt sú uvedené na obr. RGL1.57.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0057.jpg' | relative_url }})

Kapitola 5 Variabilný stav teploty posúvača ppt pre prevádzku tepelného pokoja

PDF obrázky teplotného obrysu pre tepelný odpočinok pozri obr. RGL1.58.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0058.jpg' | relative_url }})

Kapitola 5 Variabilná stránka PDF s teplotným stavom pre prevádzku tepelného oddychu

Podobne počas operácie tvarovania hrajú kroky obrysu teploty v ppt pozri obr. RGL1.59.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0059.jpg' | relative_url }})

Kapitola 5 Variabilný stav teploty posúvača ppt pre tvarovaciu operáciu

PDF obrázky teplotného obrysu pre tvárnenie pozri obr. RGL1.60.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0060.jpg' | relative_url }})

Kapitola 5 Variabilná stránka PDF s teplotným stavom pre operáciu tvárnenia

Počas kovania Blow 2 prevádzkové teplotné obrysy krokov prehrávania v ppt pozri obr. RGL1.61.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0061.jpg' | relative_url }})

Kapitola 5 Teplotný stav variabilného sklíčka ppt pre **Kovanie** Fúkanie 2

PDF obrázky teplotného obrysu pre kovanie Blow 2 pozri obr. RGL1.62.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0062.jpg' | relative_url }})

Kapitola 5 Variabilná stránka PDF s teplotným stavom pre **kovanie** operáciu vyfukovania 2

Posúvač ppt pre graf bodového sledovania kapitoly 5 pre premennú stavu teploty obrobku v strede a 2 body na vonkajšej matrici, ako je znázornené na obr. RGL1.63.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0063.jpg' | relative_url }})

Graf bodového sledovania pre snímku teploty obrobku PPT

Stránka regálov s bodmi PDF je znázornená na obr. RGL1.64.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0064.jpg' | relative_url }})

Graf bodového sledovania pre stránku PDF s teplotou obrobku

Kapitola 6

Posuvník ppt pre Z-Load Vs Graf zdvihu pre primárnu matricu pri tvárnení a kovaní Operácia vyfukovania 2 je znázornená na obr. RGL1.65.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0065.jpg' | relative_url }})

Primárna matrica Z-Load Vs Graf zdvihu ppt snímka

PDF Z-zaťaženie Vs Graf zdvihu je znázornený na obr. RGL1.66.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0066.jpg' | relative_url }})

Primárna matrica Z-Load Vs Graf zdvihu PDF strana

Podrobnosti o používaní iných častí [Report generation]({{ '/docs/sk/operation_templates/41_report_generation/41_1_report_generation/' | relative_url }}) nájdete v súvisiacich témach.

Súvisiace témy

[28\. Report Generation]({{ '/docs/sk/post_processor/28_report_generation/28_report_generation/' | relative_url }})

[41\. Report Generation]({{ '/docs/sk/operation_templates/41_report_generation/41_introduction_to_report_generation/' | relative_url }})
