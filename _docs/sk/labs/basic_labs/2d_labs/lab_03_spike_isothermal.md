---
lang: sk
title: "Laboratórna úloha 03: Izotermická krivka Spike"
---

# Laboratórna úloha 03: Izotermická krivka špičky

3.1. Vytvorenie nového problému

3.2. Pridanie operácie tvarovania – hrot

3.3. Izotermický blok Spike

3.4. Ukončenie sprievodcu MO

V tomto cvičení nastavíme 2 operácie v interaktívnom režime.

**Operácia 1**: Spike – jednoduchá deformačná operácia.

**Operácia 2**: Blok – Výmena hornej matrice.

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené nižšie (obr. L3.1.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno grafického rozhrania programu DEFORM

Vytvorte nový problém buď výberom položky **Súbor****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. L3.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek vyberte „**Angličtina**“ pomocou prepínača. Názov úlohy zadajte ako „**Spike_Isothermal**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak toto políčko nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s použitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom „Nový projekt“ (pozri obr. L3.3.), v tomto bode bude používateľ vyzvaný, aby zadal názov projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názov tejto relácie. V tejto relácii použijeme ako názov projektu „**Spike_Isothermal**“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0001.jpg' | relative_url }})

Sprievodca MO – Nový projekt

Používateľ môže tiež zmeniť systém jednotiek (v ponuke Súbor sa ako predvolený vyberie systém jednotiek, ktorý bol zvolený v ponuke Súbor) a pridať operáciu výberom z roletového zoznamu „Prvá operácia“ a zaškrtnutím príslušného políčka (pozri obr. L3.4.). Pomocou možnosti „Kopírovať existujúci projekt“ môžeme importovať predtým uložené projekty ako nové projekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0002.jpg' | relative_url }})

Priradenie názvu problému

## Pridanie formovacej operácie – hrot

Otvorí sa sprievodca viacerými operáciami s novým projektom s názvom Spike_Isothermal, v ktorom nastavíte zadanie úlohy. Zoznamu operácií v Průzkumníku pridajte operáciu 2D Forming. Operáciu je možné pridať kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie 2D Forming (pozri obr. L3.5.) alebo ju môžete pridať aj pretiahnutím do oblasti Editor operácií.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0003.jpg' | relative_url }})

Do editora operácií bola pridaná operácia 2D tvárnenia

### Typ geometrie

V tomto cvičení budeme používať osovo symetrické geometrie, preto na stránke s typmi geometrií vyberte voľbu **2D osovo symetrická**, ako je znázornené na obr. L3.6., a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0004.jpg' | relative_url }})

Výber typu osovo symetrickej geometrie

###  Ovládacie prvky simulácie

V tomto laboratórnom cvičení ukážeme, ako nastaviť jednoduchú izotermickú úlohu. V okne „Simulation controls“ (Ovládacie prvky simulácie) teda zrušte zaškrtnutie políčka „Heat transfer mode“ (Režim prenosu tepla) (pozri obr. L3.7.). Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0005.jpg' | relative_url }})

Okno riadenia simulácie

### Priradenie materiálu k obrobku

V okne so zoznamom materiálov načítajte materiál „**AISI-1035, COLD**“ z knižnice materiálov DEFORM v kategórii Oceľ pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To je možné vykonať tak, ako je znázornené nižšie, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}), ako je znázornené na obr. L3.8.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0006.jpg' | relative_url }})

Okno knižnice materiálov

Materiál je možné priradiť aj zo zoznamu materiálov v prehliadači kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky AISI-1035,COLD[70–400 °F (20–200 °C)], alebo ho môže pridať pomocou funkcie drag and drop do oblasti zoznamu materiálov (pozri obr. L3.9.). Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka objektu.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0007.jpg' | relative_url }})

Zoznam materiálov pre Explorer

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0008.jpg' | relative_url }})

Stránka so zoznamom materiálov

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0009.jpg' | relative_url }})

Stránka s vlastnosťami materiálov

### Pridávanie objektov

Na túto operáciu potrebujeme tri objekty. Ak tam ešte nie sú, pridajte ich kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}). Tieto tri objekty budú pomenované ako „Obrobok“, „Horná matrica“ a „Spodná matrica“ (pozri obr. L3.12.), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0010.jpg' | relative_url }})

Okno na pridávanie objektov

###  Obrobok

V okne „Workpiece“ (Obrobok) zmeňte názov objektu na **Billet** a ako typ objektu vyberte **Plastic**, ako je znázornené na obr. L3.13. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0011.jpg' | relative_url }})

Objekt „Billet“ – Okno

#### Načítavanie geometrie polotovaru

V okne Geometria načítajte geometrický súbor **Spike_Billet.IGS** z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) alebo ho môžete importovať aj pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru), ako je znázornené na obr. L3.14. Geometria sochoru sa nachádza v inštalačnom priečinku DEFORM v adresári \2D\LABS.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0012.jpg' | relative_url }})

Okno „Geometria polotovaru“

Možnosť ![]({{ '/assets/icons/pre_icons/mo_show_geometry_inside_mark_radio_button.jpg' | relative_url }}) slúži na kontrolu orientácie geometrie pri jej importe zo súboru. V predvolenom nastavení je zaškrtnuté políčko „Zobraziť geometriu vnútri značky“; ak nie je, zaškrtnite ho. 

Body definujúce importovanú geometriu je možné zobraziť alebo upraviť kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}). Pri načítaní súborov .IGS sa údaje importujú do programu DEFORM vo formáte Line-Arc, ktorý definuje geometriu pomocou čiar a oblúkov. Ak si chcete prezrieť formát XYR tejto geometrie, kliknite na tlačidlo **XYR**, ako je znázornené na obr. L3.15.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0013.jpg' | relative_url }})

Geometrické údaje

Pri každom importe geometrie je potrebné skontrolovať jej orientáciu a správnosť. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a následne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}), aby ste geometriu skontrolovali a opravili. Týmto spôsobom nielenže odstránite prípadné problémy s geometriou, ale v prípade potreby aj opravíte jej orientáciu. Pozrite si obr. L3.16, kde sa pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) opravila orientácia – geometria zmenila smer otáčania z hodinových ručičiek na protismer.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0014.jpg' | relative_url }})

Skontrolujte a opravte geometriu

#### Vytvorenie siete pre sochársky blok

Radi by sme na polotovar vytvorili počiatočnú sieť s väčším počtom prvkov v pravom hornom rohu, kde spočiatku dôjde k najväčšej deformácii. To môžete urobiť buď pomocou okien pre sieť, alebo pomocou užívateľsky definovaných hodnôt siete. V rámci tohto cvičenia použijeme užívateľsky definované hodnoty na vytvorenie počiatočnej siete na polotovare.

Ak ste v režime s návodom, prejdite do režimu pre pokročilých kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Prejsť do režimu pre pokročilých), ktorá sa nachádza na paneli nástrojov v hornej časti okna. Režim pre pokročilých ponúka viac možností pre podrobné nastavenia. Na stránke „Mesh“ vyberte ![]({{ '/assets/icons/pre_icons/mo_user_defined_radio_button.jpg' | relative_url }}). Chceme, aby pravý horný roh polotovaru mal sieť, ktorá je štyrikrát jemnejšia ako sieť v ostatných troch rohoch. Aby sme toho dosiahli, priradíme veľkosť siete 1 pravému hornému rohu a veľkosť siete 4 ostatným rohom.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0015.jpg' | relative_url }})

Výber bodov pre užívateľsky definovanú sieť

Nastavte veľkosť prvku na 1 a kliknite na pravý horný roh polotovaru, potom nastavte veľkosť prvku na 4 a kliknite na ostatné tri rohy (pozri obr. L3.17.). Nastavte počet prvkov na 400 a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Pre sochoru sa vygeneruje približne 412 sieťových prvkov, ako je znázornené na obr. L3.18. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0016.jpg' | relative_url }})

Okno z mriežky z hliníkového bloku

Keďže na definovanie počiatočnej siete používame užívateľsky definovanú sieť, váhové faktory sa nezohľadňujú. Užívateľsky definované hodnoty sa však dajú použiť iba na definovanie počiatočnej siete. Ak je počas simulácie potrebné prepočítať sieť, na definovanie novej siete sa použijú váhové faktory.

Chceme nastaviť ešte jeden parameter súvisiaci s vytvorením siete. Existuje niekoľko kritérií, ktoré počas simulácie spustia prepočítanie siete polotovaru. Jedným z nich je tzv. hĺbka kolízie, čo je vzdialenosť, do ktorej môže nástroj preniknúť do obrobku.

Vhodná hodnota pre hĺbku interferencie je približne jedna tretina najmenšej veľkosti prvku deformovaného objektu. Zväčšite pravý horný roh polotovaru pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) a potom pomocou ![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) zmerajte dĺžku hrany malého prvku. Hodnota pre hĺbku interferencie bude približne 0,013 (0,038 / 3) a túto hodnotu je potrebné nastaviť na karte Kritériá pregenerovania siete (pozri obr. L3.19.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0017.jpg' | relative_url }})

Okno s kritériami pre výpočet novej siete

####  Nastaviť materiál obrobku

Na priradenie materiálu k obrobku vyberte v okne materiálov materiál **AISI-1035, COLD[70–400 °F (20–200 °C)]**. Postupujte podľa obrázku L3.20 nižšie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0018.jpg' | relative_url }})

Okno na výber materiálu

#### Obrobok BCC

Na stránke BCC zaškrtnite predvolenú deformáciu BCC pre ľavú stranu obrobku v smere osi X; predvolené hodnoty BCC sa priradia automaticky na základe výberu typu úlohy ako osovo symetrickej (pozri obr. L3.21). Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top die“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0019.jpg' | relative_url }})

Okno BCC z hliníkového bloku

### Horná matrica

Na stránke „Top die“ (pozri obr. L3.22.) vyberte typ objektu **Rigid** a zaškrtnite políčko „Primary die“, keďže hornej matrici bude priradená definícia pohybu, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0020.jpg' | relative_url }})

Na začiatok stránky

#### Načítavanie geometrie hornej matrice

V okne Geometria načítajte geometrický súbor **Spike_TopDie.IGS** z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) alebo ho môžete importovať aj pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru), ako je znázornené na obr. L3.23. Geometria sa nachádza v inštalačnom priečinku DEFORM v adresári \2D\Labs. Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top die movement“ (Pohyb hornej matrice).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0012.jpg' | relative_url }})

Hlavná stránka „Geometria lisovacích foriem“

#### Priradiť pohyb k hornej kocku

Pre toto laboratórne cvičenie nastavte **rýchlosť** **2** palce za sekundu v smere **-Y** (pozri obr. L3.24.). Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Bottom Die“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0021.jpg' | relative_url }})

Na začiatok stránky „Pohyb foriem“

### Spodná matrica

Na stránke „Bottom die“ vyberte ako typ objektu **Rigid** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (pozri obr. L3.25.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0022.jpg' | relative_url }})

Stránka spodnej matrice

#### Načítanie geometrie spodnej matrice

V okne Geometria načítajte súbor geometrie **Spike_BottomDie.IGS** z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) alebo ho môžete importovať pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru). Geometria sa nachádza v inštalačnom priečinku DEFORM v adresári \2D\Labs. Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Positioning“ (Polohovanie).

### Polohovanie

Objekt je možné umiestniť na stránke „Umiestnenie“, kde sú k dispozícii dve možnosti na umiestňovanie objektov: „Automatické umiestnenie“ a „Umiestniť objekty“.

**Automatické polohovanie** ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}): Pri automatickom polohovaní sa objekty automaticky umiestnia vzhľadom na smer polohovania a smer pohybu primárnej formy. Túto možnosť je možné použiť len v prípade, ak operácia zahŕňa iba 3 objekty: obrobok, hornú formu a spodnú formu.

**Poloha objektov** ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}): K dispozícii sú nasledujúce metódy určovania polohy:

![]({{ '/assets/icons/pre_icons/mo_drag_radio_button.jpg' | relative_url }}) |  Objekty je možné pomocou myši presúvať určitým smerom.  
---|---  
![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }}) |  Objekty je možné presunúť o definovanú vzdialenosť buď zadaním vektora vzdialenosti, alebo zadaním počiatočného a koncového bodu presunu.  
![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) |  Pri polohovaní na základe interferencie sa polohovaný objekt posunie tak, aby sa veľmi mierne prekrýval s referenčným objektom.  
![]({{ '/assets/icons/pre_icons/mo_rotational_radio_button.jpg' | relative_url }}) |  Objekty je možné otáčať o definovaný uhol okolo definovaného stredového bodu.  
![]({{ '/assets/icons/pre_icons/mo_flip_radio_button.jpg' | relative_url }}) |  Objekty je možné otočiť okolo osi X, Y alebo akejkoľvek inej definovanej osi.  
  
**Polohovanie posunu:**

****Posuňme spodnú matricu pomocou polohovania s posunom. Vyberte a zmeňte objekt polohovania na spodnú matricu. Zložky vzdialenosti je možné zadať buď pomocou klávesnice, alebo výberom vzdialenosti myšou. Chceme umiestniť matricu tak, aby sa posunula nahor a doprava od polotovaru. Pri vybranom vektore vzdialenosti kliknite myšou na počiatočný a koncový bod zobrazené nižšie. Príslušná vzdialenosť sa zadá do polí vektora vzdialenosti. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) posuňte spodnú matricu (pozri obr. L3.26.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0023.jpg' | relative_url }})

Polohovanie s posunom

Ak chcete spodnú matricu vrátiť do pôvodnej polohy, zmeňte hodnoty vektora „Distance“ z kladných na záporné a potom opäť kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}).

**Určovanie polohy na základe interferencie:**

****Vyberte a zmeňte objekt polohovania na hornú matricu. Chceme umiestniť hornú matricu tak, aby sa len minimálne prekrývala s hornou časťou polotovaru. Keďže sa horná matrica musí pohybovať smerom nadol, aby sa dotkla hornej časti polotovaru, zmeňte smer priblíženia na -Y. Predvolené nastavenie kolízie funguje vo väčšine prípadov dobre, preto kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). V okne Zobrazenie si všimnete, že horná matrica sa mierne posunie nadol, takže sa teraz dotýka polotovaru (pozri obr. L3.27.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0024.jpg' | relative_url }})

Určovanie polohy na základe interferencie

**Polohovanie otáčaním:**

Vyberte a zmeňte objekt polohovania na polotovar. Chceme otočiť polotovar o 45 stupňov v smere hodinových ručičiek okolo jeho pravého dolného rohu. Vyberte voľbu „User Defined“, kliknite myšou na pravý dolný roh polotovaru. Pole „Center“ v okne „Object positioning“ sa aktualizuje na práve vybrané súradnice. Zmeňte „Uhol“ na -45 (v smere hodinových ručičiek) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Polotovar sa otočí o 45 stupňov okolo zvoleného bodu. Zmeňte „Uhol“ na 45 a otočte polotovar späť do pôvodnej polohy (pozri obr. L3.28.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0025.jpg' | relative_url }})

Rotačné polohovanie

V tomto nastavení operácie použijeme na umiestnenie objektov možnosť „Automatické umiestnenie“. Na stránke „Umiestnenie objektov“ vyberte smer umiestnenia Z (Y) a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}); objekty sa umiestnia tak, ako je znázornené na obr. L3.29. Následne klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Kontakt“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0026.jpg' | relative_url }})

Objekt som umiestnil pomocou možnosti „Automatické umiestnenie“

### Získavanie kontaktov

Vyberte typ kontaktu „užívateľ“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi polotovarom, hornou matricou a spodnou matricou, ako je znázornené na obr. L3.30. Keďže matrice sú tuhé a polotovar je plastický, horná a spodná matrica sa považujú za hlavné a polotovar za podriadený. S cieľom predpovedať ohyb počas deformácie sa polotovaru priradí vlastný kontakt.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0027.jpg' | relative_url }})

Stránka na získavanie kontaktov

Zvýraznite vzťah medzi hornou matricou a polotovarom a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) upravte podmienky kontaktu. V časti obrazovky venovanej treniu (obr. L3.31.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné procesy tvárnenia.

Keďže táto simulácia prebieha pri izbovej teplote a formy sú oceľové, použite rozbaľovacie menu a zo zoznamu vyberte možnosť „Tvarovanie za studena (oceľové formy)“. Hodnota trenia 0,12 sa vyberie automaticky.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0028.jpg' | relative_url }})

Okno definície údajov medzi objektmi

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna „Inter-Object“. Keďže podmienky trenia sú pre všetky páry objektov rovnaké, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu na všetky ostatné. Po vykonaní tejto operácie budú mať všetky vzťahy definované trenie 0,12. Pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určte vhodnú toleranciu kontaktu (vypočíta sa hodnota približne 0,00126"), potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) na vytvorenie kontaktu. Ak objekty otočíte v grafickom okne, uvidíte, že medzi dvoma objektmi bol vytvorený kontakt. Prejdite na kartu Správa alebo sledujte stavový riadok, aby ste zistili informácie o vytvorených kontaktoch. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno Ovládacie prvky kroku.

### Krok

Zmeňte názov operácie na „**Spike**“, ako je znázornené na obr. L3.32.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0029.jpg' | relative_url }})

Karta „Step Main“ v expertnom režime

Vyberte kartu „Simulačné kroky“ (![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }})), nastavte **Počet simulačných krokov** na **100** a **Krok na uloženie** na **5**. Ak sa to nezvolilo automaticky, nastavte **Hornú matricu** ako **Primárnu matricu**. (Pozri obr. L3.33.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0030.jpg' | relative_url }})

Ovládacie prvky simulácie – karta „Kroky simulácie“ v expertnom režime

Na určenie vhodnej veľkosti kroku vyberte ikonu a zmerajte dĺžku hrany niekoľkých menších prvkov v polotovare. Priemerná dĺžka krátkej hrany je približne 0,035”. Použite **konštantu** posun matrice na krok **0,015** palca/krok, čo je 1/3 tejto dĺžky krátkej hrany, v záložke „Krok“ (![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }})) pre veľkosť kroku ako posun matrice (pozri obr. L3.34) a ostatné nastavenia ponechajte na predvolených hodnotách.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0031.jpg' | relative_url }})

Ovládacie prvky simulácie – karta „Krok“ v expertnom režime

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a uložte súbor s kľúčovými slovami pre daný problém výberom možnosti Export v ponuke Súbor.

### Vytvorenie databázy

Po úplnom nastavení úlohy je posledným krokom vytvorenie databázového súboru. Modul FEM (časť programu DEFORM®, ktorá vypočítava riešenie) používa databázový súbor na ukladanie riešení úlohy metódou konečných prvkov. Pri generovaní databázy v preprocesore DEFORM MO sa všetky informácie definované v preprocesore (napríklad vlastnosti materiálov, riadenie pohybu, geometrie objektov atď.) prenesú do databázového súboru. Od verzie v12.0.2 môžeme v okne Generate DB file vidieť súhrn nastavení simulácie operácie, ako je znázornené na obr. L3.35.

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení úlohy niečo nechýba. Počas kontroly červené hlásenia označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, t. j. po jej vytvorení, prepnite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0040.jpg' | relative_url }})

Vytvoriť stránku databázy

### Spustenie simulácie

Kliknite na označenie akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“ (pozri obr. L3.36). Otvorí sa dialógové okno „Možnosti spustenia“, ako je znázornené na obr. L3.37. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0032.jpg' | relative_url }})

Možnosti simulácie

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0056.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať na karte „Simulation Message“ a v časti „Simulation Graphics“ v oblasti zobrazenia „Graphics“ v režime simulácie. Pokiaľ je na karte „Simulation Message“ zaškrtnutá táto možnosť (čo je predvolené nastavenie), súbor správ sa bude automaticky aktualizovať.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia momentálne nachádza, a tiež informácie o tom, ako dobre simulácia prebieha.

Ak simulácia prebehne bez problémov, na koniec súboru správ sa pridá nasledujúca správa: „NORMAL STOP: Simulácia bola dokončená a zastavená v užívateľom zadanom časovom kroku“. (Pozri obr. L3.38.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0033.jpg' | relative_url }})

Karta „Simulačné správy“

### Následné spracovanie výsledkov

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}), kde si môžete prezrieť výsledky; otvorí sa postprocesor MO. (Pozri obr. L3.39.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0034.jpg' | relative_url }})

Okno postprocesora MO

#### Nástroje pre kroky a výber krokov

Na výber kroku, ktorý sa má zobraziť, slúži stránka prehliadača krokov, ako je znázornené na obr. L3.40. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) v prehliadači krokov sa po kliknutí na tlačidlo „Všetko“ v prehliadači krokov zobrazia všetky uložené kroky. Pomocou ikony ![]({{ '/assets/icons/post_icons/mo_step_list_icon.jpg' | relative_url }}) je možné otvoriť okno Zoznam krokov (pozri obr. L3.40.), ktoré umožňuje používateľovi definovať podrobnejšie nastavenia zobrazenia krokov.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0035.jpg' | relative_url }})

Okno „Zoznam krokov“

Niektoré z najčastejšie používaných stavových premenných si môžete pozrieť na stránke nástrojov pre príspevky. (Pozri obr. L3.41.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0036.jpg' | relative_url }})

Stránka s nástrojmi pre príspevky

#### Stavová premenná

V nástrojoch na príspevky vyberte možnosť „Strain-Effective“, aby ste si prezreli mieru deformácie, ktorú obrobok utrpel. Kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) otvoríte okno „State Variable“ (Stavová premenná), vyberte stavovú premennú **Strain-Effective**, kliknutím na tlačidlo „Solid display“ (Plné zobrazenie) vyberte „Solid shading“ (Plné tieňovanie) a ako možnosť „Scaling“ (Mierka) vyberte ![]({{ '/assets/icons/post_icons/mo_local_scaling_radio_button.jpg' | relative_url }}). Táto voľba použije lokálne minimálne a maximálne efektívne deformácie ako krajné hodnoty na farebnej lište. Nastavenia mierky, tieňovania a ďalších vlastností kontúrového grafu je možné zmeniť aj pomocou možností pravého tlačidla myši na farebnej lište. Prejdite jednotlivými krokmi simulácie a sledujte akumuláciu deformácie. (Pozri obr. L3.42.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0037.jpg' | relative_url }})

Graf znázorňujúci efekt deformácie

Pomocou ikony ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) je možné získať prístup ku všetkým stavovým premenným.

Používateľ môže zmeniť zobrazenie premennej z kontúry typu „Plná“ na kontúru typu „Čiara“ výberom možnosti „Typ zobrazenia“. K dispozícii je aj niekoľko ďalších možností, ako napríklad „Tienované kontúry“ a „Elementárne kontúry“.

**Vektorové grafy:**

****V prípade premenných, ktoré majú priradený smer, ako napríklad rýchlosť, je možné zobraziť aj vektorový graf. V ponuke „State Variable“ vyberte ako premennú, ktorú chcete znázorniť, rýchlosť „**Total Vel**“ a kliknite na tlačidlo **Vector Plot**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Zobrazí sa vektorový graf rýchlosti uzlov pre sochoru (pozri obr. L3.43.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0038.jpg' | relative_url }})

Graf rýchlostného vektora

#### Graf zaťaženia a zdvihu

Veľkosť zaťaženia potrebného na deformáciu predmetu je dôležitý výsledok, ktorý možno získať zo simulácie.

Kliknite na ikonu ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) – otvorí sa okno „Load Stroke Graph“ (Graf zaťaženia pri zdvihu). V zozname objektov „Plot“ vyberte položku **Top Die**, v roletovom menu **X-Axis** vyberte položku **Stroke** a v roletovom menu **Y-Axis** vyberte položku **Y Load**. Kliknite na kartu „Options“ a zaškrtnite políčko „Step tracer“, potom kliknite na ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}). Graf zaťaženia a zdvihu sa zobrazí na pravej strane okna (pozri obr. L3.44.). Pri výbere iného kroku sa v krivke zaťaženia a zdvihu zvýrazní príslušný krok a v grafe sa zobrazí zodpovedajúce zaťaženie pre tento krok. Okrem toho je možné myšou kliknúť na bod v grafe, pričom zobrazený krok sa automaticky zmení na ten, ktorý zodpovedá danému bodu v grafe.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0039.jpg' | relative_url }})

Graf závislosti zaťaženia od zdvihu

Po dokončení následného spracovania prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) a pridajte operáciu „Blokovať“.

## Izotermický blok Spike

V tejto operácii vymeníme iba hornú formu, aby sme skontrolovali, ako sa vyvíja ohyb, a túto operáciu nastavíme v dávkovom režime.

### Pridanie operácie

Pridajte 2D tvárniacu operáciu zo zoznamu operácií v prehliadači. Potom kliknite na druhú tvárniacu operáciu, aby sa otvorila. Po kliknutí na druhú operáciu sa zobrazí vyskakovacie okno s typom nastavenia; v ňom kliknite na tlačidlo **No-Batch mode**, ako je znázornené na obr. L3.45. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Objekty“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0041.jpg' | relative_url }})

Vyskakovacie okno s typom nastavenia na nastavenie druhej operácie

### Pridávanie objektov

V okne „Objekty“ sa štandardne do zoznamu objektov pridajú tri objekty z predchádzajúcej operácie a prenesú sa údaje o objektoch. Ak tam ešte nie sú tri objekty, pridajte ich kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Obrobok

Na stránke „Obrobok“ vyberte ako typ objektu možnosť „Načítať z databázy“; všetky údaje, ako sú teplota, sieť a BCC objektu, sa preberú z predchádzajúcej operácie (pozri obr. L3.46.). Farba objektu sa zmení na červenú a v editore operácií vidíme, že medzi operáciami pre tieto objekty sa vytvorilo prepojenie. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0042.jpg' | relative_url }})

Okno obrobku

#### Priradenie siete obrobku

Existuje podozrenie, že počas tejto operácie vznikne záhyb, takže ak zapnete funkciu „self contact“, záhyb zostane zachovaný a v postprocesore budete môcť sledovať, ako sa vyvíja.

Na stránke „Sieť obrobku“ zaškrtnite políčko „Definovať nastavenia siete“, ak chcete upraviť existujúcu sieť. Po zaškrtnutí tohto políčka sa aktivujú všetky možnosti nastavenia siete. Zmeňte **Počet prvkov** na **500**, potom kliknite na kartu **Pokročilé nastavenia** a zmeňte **Toleranciu vzdialenosti** na **0,001**. (Pozri obr. L3.47.)

Keďže predpokladáme vznik malého záhybu, chceme sa uistiť, že sieť v blízkosti záhybu túto vadu primerane zachytí. Pri prvej operácii premenovania siete sa použije väčší počet prvkov, čím sa celkový počet prvkov automaticky zvýši zo 400 na 500. Nastavenie „Tolerancia vzdialenosti“ tiež pomôže sieti lepšie určiť záhyb v geometrii. 

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0043.jpg' | relative_url }})

Okienko so sieťkou na obrobok

Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top Die“.

### Horná matrica

V okne „Top die“ vyberte ako typ objektu „Rigid“ a zaškrtnite políčko „Primary Die“, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0044.jpg' | relative_url }})

Stránka „Top Die“

#### Vytvoriť geometriu novej hornej matrice

Na stránke „Geometria hornej matrice“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) odstráňte existujúcu geometriu a pridajte nasledujúce body vo formáte **XYR**, ako je znázornené na obr. L3.49.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0046.jpg' | relative_url }})

Údaje o geometrii hornej matrice

Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili okno „Edit“, a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s pohybmi.

#### Priradiť pohyb k hornej kocku

Nastavte rýchlosť 2 palce/sekundu v smere -Y a nastavte aktuálnu hodnotu zdvihu na (0,0). Potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Bottom Die“.

### Spodná matrica

V okne „Bottom Die“ vyberte typ objektu „Read from DB“ a potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno „Scheduled Positioning“.

### Plánované nastavenie polohy hornej matrice

Na stránke plánovaného polohovania kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a vyberte prepínač ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte polohovací objekt na hornú matricu a referenčný bod na polotovar. Zmeňte smer priblíženia na -Y a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). (Pozrite obr. L3.50.) Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Kontakt.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0045.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

### Stránka s kontaktnými údajmi

Vyberte typ kontaktu „užívateľ“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi polotovarom, hornou maticou a spodnou maticou, ako je znázornené na obr. L3.51. Keďže matrice sú tuhé a polotovar je plastický, horná a spodná matrica sa považujú za hlavné a polotovar za podriadený. S cieľom predpovedať ohyb počas deformácie sa polotovaru priradí vlastný kontakt.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0055.jpg' | relative_url }})

Stránka na získavanie kontaktov

Zvýraznite položku **Vzťah medzi hornou matricou a polotovarom** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) upravte podmienky kontaktu. V časti obrazovky venovanej treniu (pozri obr. L3.52.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné procesy tvárnenia.

Keďže táto simulácia prebieha pri izbovej teplote a formy sú oceľové, použite rozbaľovacie menu a zo zoznamu vyberte možnosť „Tvarovanie za studena (oceľové formy)“. Hodnota trenia 0,12 sa vyberie automaticky.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0028.jpg' | relative_url }})

Okno definície údajov medzi objektmi

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna „Inter-Object“. Keďže podmienky trenia sú rovnaké pre všetky páry objektov, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných. Po vykonaní tejto operácie budú mať všetky vzťahy definované trenie 0,12. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Step“.

### Krok

Zmeňte názov operácie na „**Block**“, zrušte zaškrtnutie políčka „Režim prenosu tepla“, nastavte **počet simulačných krokov** na **100** a **krok ukladania** na **5**. Ako primárnu matricu vyberte „Top Die“ a v časti „Krok prírastku“ nastavte položku „S **konštantným posunom matrice**“ na hodnotu **0,01**". Na karte **Zastaviť** – **Parametre procesu** nastavte hodnotu **Posun primárnej matrice** na (**0**, **0,5**) palca, ako je znázornené na obr. L3.53. Tým sa simulácia zastaví po tom, čo sa horná matrica posunie o 0,5" v smere -Y. Potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0047.jpg' | relative_url }})

Karta „Stop“ v okne „Step Controls“ v expertnom režime

### Vytvoriť databázu

Uložte súbor s kľúčovými slovami pre danú úlohu výberom možnosti „Exportovať“ v ponuke „Súbor“.

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či sa pri nastavení úlohy na niečo nezabudlo.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Akonáhle program dokončí zapisovanie databázy, prejdite na kartu a spustite simuláciu.

### Spustenie simulácie

Simuláciu spustíte kliknutím na akčný popisok ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), pomocou predvolenej možnosti **Pokračovať v behu** vyberte možnosť „**Pokračovať od posledného kroku**“ a následne nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu. Po dokončení simulácie môžeme pozorovať, že na koniec súboru správ bola pridaná nasledujúca správa:

" PROGRAM SA ZASTAVIL!

HODNOTA STROKE -0,5000000 PREKROČILA ŠPECIFIKOVANÝ LIMIT 0,5000000"

### Následné spracovanie výsledkov

Po dokončení simulácie sa po stlačení tlačidla „Switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }})“ otvorí postprocesor MO (pozri obr. L3.54.).

Prejdite jednotlivé kroky a skontrolujte, či sa vytvorí záhyb. Aby ste to lepšie videli, možno budete musieť zväčšiť zobrazenie miesta styku medzi hornou matricou a obrobkom.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0048.jpg' | relative_url }})

Okno postprocesora MO

### Flownet

Teraz sa vráťte k prvému kroku druhej operácie a kliknite na ![]({{ '/assets/icons/post_icons/mo_flownet_icon.jpg' | relative_url }}). V okne Flownet vyberte typ **Offset** flownet (pozri obr. L3.55.) a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0049.jpg' | relative_url }})

Okno Flownet

Ako hodnotu posunu zadajte 0,01 palca a potom kliknite na ![]({{ '/assets/icons/post_icons/mo_preview_button.jpg' | relative_url }}). V náhľade sa zobrazí posunutý okraj polotovaru (pozri obr. L3.56.), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0050.jpg' | relative_url }})

Posunuté okno

Na stránke „Pokročilé nastavenia“ môžeme uložiť počiatočný vzor Flownetu, konečný vzor Flownetu a výsledky. Kliknutím na tlačidlo ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) vygenerujeme Flownet (pozri obr. L3.57). Následne spustíme animáciu kliknutím na tlačidlo „Play“ a pozorujeme hranice sochoru. Môžeme pozorovať, že na sochore bližšie k vonkajšiemu okraju hornej matrice vzniká záhyb, ako je znázornené na obr. L3.58.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0051.jpg' | relative_url }})

Okno „Flownet Generation“

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0052.jpg' | relative_url }})

Posledný krok: Zobrazenie polotovaru

###  Graf zdvihu zaťaženia

V prehliadači krokov prejdite na prvý krok druhej operácie a kliknite na ikonu ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}); otvorí sa okno „Load Stroke Graph“ (Graf zaťaženia pri zdvihu). V zozname objektov „Plot“ vyberte položku „Top Die“ (Horná matrica), z roletového menu osi X vyberte položku „Stroke“ (Zdvih) a z roletového menu osi Y vyberte položku „Y Load“ (Zaťaženie na osi Y). Kliknite na kartu „Options“ a zaškrtnite políčko „Step tracer“, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Graf zaťaženia a zdvihu pre operáciu „Block“ sa vykreslí tak, ako je znázornené na obr. L3.59.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0053.jpg' | relative_url }})

Graf závislosti zaťaženia od zdvihu

Ak chcete vykresliť graf zaťaženia a zdvihu pre obe operácie, vyberte v roletovom zozname „Operácia“ možnosť „Všetko“ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Graf zaťaženia a zdvihu sa vykreslí pre obe operácie, ako je znázornené na obr. L3.60.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0054.jpg' | relative_url }})

Graf závislosti zaťaženia od zdvihu pre všetky prevádzkové režimy

## Zatvoriť sprievodcu MO

Po dokončení následného spracovania uložte projekt a zatvorte sprievodcu MO kliknutím na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }}) Zatvoriť“ alebo výberom možnosti „Ukončiť“ v ponuke „Súbor“.

**Súvisiace témy:**

[12.1. 2D Geometry Data Defining ]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/' | relative_url }})

[12.2. 2D Geometry Data Editing]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/' | relative_url }})

[13.1. 2D Mesh Generation]({{ '/docs/sk/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/' | relative_url }})

[14\. Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/' | relative_url }})

[15\. Movement Controls Settings]({{ '/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/' | relative_url }})

[16\. Object Properties]({{ '/docs/sk/pre_processor/16_object_properties/16_object_properties/' | relative_url }})

[17\. Object Data Initialize]({{ '/docs/sk/pre_processor/17_object_data_initialization/17_object_data_initialize/' | relative_url }})

[19\. Object Positioning]({{ '/docs/sk/pre_processor/19_object_positioning/19_object_positioning/' | relative_url }})

[20\. Inter-Object Data Definition]({{ '/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/' | relative_url }})

[9\. Simulation Controls]({{ '/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/' | relative_url }})

[6.3. Integrated Manufacturing Process Post-processor layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/' | relative_url }})

[25\. Post Processor Layout]({{ '/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/' | relative_url }})
