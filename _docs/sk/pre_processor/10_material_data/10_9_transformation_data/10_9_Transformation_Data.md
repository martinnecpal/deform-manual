---
lang: sk
title: "10.9. Transformačné údaje"
---

# 10.9. Transformačné údaje

10.9.1 Medziproduktové údaje
10.9.2. Transformačný vzťah (PHASTF)

  * Kinetický model (TTTD)

  * Latentné teplo a objem(PHASLH)

  * Latentné teplo

  * Zmena objemu vyvolaná transformáciou (PHASVL)

  * Transformačná plasticita (TRNSFP)

  * Ostatné

  * Tepelný smer

  * Rovnovážny objemový podiel

  * Model výberu variácií

  * Rozhranie Energia

## Údaje o materiáli

Účelom medziproduktových údajov je definovať vzťahy medzi jednotlivými fázami zmesi. Ako je definované v materiálových údajoch, zmes definuje používateľ ako súbor fáz. Vzťahy medzi fázami sú definované v zmysle nasledujúcich transformačných charakteristík:

  * Model kinetiky transformácie
  * Latentné teplo premeny
  * Transformáciou vyvolaná zmena objemu
  * Plasticita transformácie

Cieľom tejto časti je poskytnúť používateľovi informácie o tom, ako správne definovať transformačný vzťah medzi dvoma fázami. V tejto časti sa vysvetlí, ako DEFORM spracúva uvedené pojmy. Transformácia je kľúčový pojem pri tvárnení a tepelnom spracovaní kovov. [Fig. 1.3.1.](../../../About_DEFORM/1_Introduction_to_DEFORM/1_3_Capabilities.htm#Fig._1.3.1._Relationship_between_various_DEFORM_modules) znázorňuje väzbu medzi teplotou, deformáciou, transformáciou a obsahom uhlíka. Transformácia sa modeluje definovaním objemového podielu pre každú možnú fázu v každom prvku sieťovaného objektu. V prípade objektu z nízkouhlíkovej ocele môže každý prvok obsahovať rôzne objemové podiely martenzitu, bainitu, perlitu alebo austenitu. Každá fáza je definovaná vlastným súborom materiálových vlastností. Tieto materiálové vlastnosti definujú plastické správanie sa fázy, tepelné vlastnosti fázy a prípadne (ak sa používa elasticko-plastický matriál) aj pružné vlastnosti fázy.

Vzťah medzi transformáciami z jednej fázy do druhej je deinovaný medziproduktovými údajmi. Tento vzťah je definovaný v zmysle kinetického modelu (s cieľom určiť rýchlosť fázovej premeny) a niekoľkých vzťahových vlastností, ako je latentné teplo a zmena objemu.

## Transformačný vzťah (PHASTF)

V programe DEFORM sa transformácia definuje pomocou transformačných vzťahov ([PHASTF](/docs/sk/Keyword_Documentation/P/PHASTF/)). Základnou jednotkou transformačných vzťahov sú fázy. Fázy sa môžu zoskupiť, aby sa definovala zmes. Zmes zodpovedá materiálu, ako je AISI-1045 alebo Ti-6Al-4V. Pre každú definovanú fázu môže existovať transformačný vzťah k akejkoľvek inej definovanej fáze. Napríklad v prípade nízkouhlíkovej ocele má austenit vzťah k perlitu, pretože austenit môže pri vhodných podmienkach chladenia vytvoriť perlit. Pri vhodných podmienkach zahrievania sa perlit môže tiež premeniť na austenit. Ak teda chcete v programe DEFORM určiť vzťah premeny austenitu na perlit, musíte vybrať austenit ako materiál 1 a perlit ako materiál 2 a potom kliknúť na vzťah Fáza 1 Fáza 2. To potom umožní používateľovi definovať kinetiku premeny, latentné teplo premeny, objemovú zmenu premeny atď. (Pozri [Fig. 1.3.1.](../../../About_DEFORM/1_Introduction_to_DEFORM/1_3_Capabilities.htm#Fig._1.3.1._Relationship_between_various_DEFORM_modules)).

  
Údaje o materiáloch zmesí možno vytvoriť zadaním materského materiálu a jeho fáz a definovaním všeobecných údajov o materiáloch a vzájomných údajov o materiáloch alebo transformáciách, ako je uvedené nižšie (pozri obr. 10.9.1).

  1. Kliknutím na tlačidlo ![](../../../../assets/Icons/Pre_icons/MO_Add_Icon2.jpg) vytvorte materiál (pozri **1.1** na obr. 10.9.1.), potom zaškrtnite políčko Mixture material (Materiál zmesi), aby sa pridaný materiál stal materiálom zmesi (pozri **1.2** na obr. 10.9.1.), stane sa materským materiálom materiálu zmesi.
  2. Vyberte materský materiál (pozri **2.1** na obr. 10.9.1.) a kliknite na tlačidlo ![](../../../../assets/Icons/Pre_icons/MO_Add_Phase_button.jpg) (pozri **2.2** na obr. 10.9.1.), čím sa pridajú jeho fázy, tiež pridané fázy možno odstrániť pomocou tlačidla ![](../../../../assets/Icons/Pre_icons/MO_Remove_phase_button.jpg) výberom fáz.
  3. Krok**2** zopakujte toľkokrát, koľko je fáz (pozri **3** na obr. 10.9.1.).
  4. Definujte všeobecné materiálové údaje pomocou ikon Plastický, Pružný atď. (pozri **4.1** na obr. 10.9.1.) pre materský materiál a ostatné fázy, potom kliknite na ikonu Transformácia (pozri **4.2** na obr. 10.9.1.), aby ste definovali transformačné údaje medzi podradenými fázami. Ak chce používateľ definovať údaje o zhrubnutí, vyberte ikonu Zhrubnutie.
  5. Vyberte vzťah premeny fáz Mother to Child (pozri **5.1** a **5.2** na obr. 10.9.1.) a potom kliknite na tlačidlo ![](../../../../assets/Icons/Pre_icons/MO_Add_Icon2.jpg) (pozri 5.3 na obr. 10.9.1.) a definujte kinetiku premeny, latentné teplo, objemovú zmenu, plasticitu premeny a ďalšie údaje (pozri 5.4 na obr. 10.9.1.).
  6. Zopakujte krok 5 pre transformácie ostatných fáz.

**Poznámka** :  
Údaje modelu zrna pre materiály zmesi možno definovať len pre fázy výberom Fázy pomocou tlačidla Zrno.

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_Image001.jpg)

Vytvorenie materiálu zmesi

  * **Kinetický model (TTTD)**

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_Image002.jpg)

Okno definície kinetiky transformácie

Kinetický model ([TTTD](/docs/sk/Keyword_Documentation/T/TTTD/)) je funkcia, ktorá definuje podmienky a spôsob, akým sa jedna fáza môže premeniť na druhú. Množstvo potrebných údajov je často značné, ako v prípade úplného diagramu TTT, takže ak to nie je nevyhnutné, často stačí použiť koeficienty funkcie. Model definuje len jeden vzťah, takže mnoho vzťahov je potrebných v takých prípadoch, ako je oceľ, kde môže vzniknúť veľa fáz. Existujú dve klasifikácie kinetických modelov, transformácie difúzneho typu a transformácie menej difúzneho typu. Systém je určený pre železné aj neželezné kovy. Na príklade uhlíkovej ocele sa zmeny štruktúry austenit-ferit a austenit-perlit a naopak riadia transformáciou difúzneho typu. Transformácia je riadená difúznymi procesmi v závislosti od teploty, histórie napätia a obsahu uhlíka. Difúzne menej výrazná transformácia z austenitu na martenzit zahŕňa šmykový proces, ktorý závisí od teploty, napätia a obsahu uhlíka. Ďalšie informácie o kinetickom modeli nájdete na stránke [Chapter 10.9.1.Transformation Kinetics Models.](/docs/sk/pre_processor/10_material_data/10_9_transformation_data/10_9_1_Transformation_Kinetics_Models/)

  * **Latentné teplo a objem (PHASLH)**

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_Image003.jpg)

Objemové a latentné tepelné okno vyvolané transformáciou

  * **Latentné teplo :****Latentné teplo** ([PHASLH](/docs/sk/Keyword_Documentation/P/PHASLH/)) predstavuje čistý zisk alebo stratu energie pri zmene fázy z jednej na druhú. Latentné teplo môže mať konštantnú hodnotu, môže byť funkciou teploty alebo funkciou obsahu dominantného atómu (pozri obr. 10.9.3.) Uvoľnenie energie v dôsledku latentného tepla môže predĺžiť čas premeny. Kladné znamienko na hodnote latentného tepla znamená, že premena pôsobí ako zdroj tepla, a záporné znamienko znamená, že premena pôsobí ako chladič tepla. Jednotky pre túto veličinu sú Btu/in3 pre anglické jednotky a N/mm2 pre jednotky SI.

  * ******T****zmena objemu vyvolaná transformáciou ([PHASVL](/docs/sk/Keyword_Documentation/P/PHASVL/)) : **Zmena objemu môže byť výsledkom fázovej transformácie. Táto zmena objemu ([PHASVL](/docs/sk/Keyword_Documentation/P/PHASVL/)) môže vyvolať napätie v transformujúcom sa objekte a určite ovplyvní konečné rozmery po spracovaní. Zmena objemu môže byť konštantná hodnota, funkcia teploty, obsahu dominantného atómu alebo teploty a obsahu dominantného atómu. Zmena objemu v dôsledku transformácie je vyvolaná zmenou mriežkovej štruktúry kovu. Transformačná deformácia sa používa najmä na zohľadnenie zmeny štruktúry počas transformácie a má tvar:

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/EQ_10_9_1.JPG) |
---|---
  
  
Kladné znamienko v zmene objemu znamená, že došlo k nárastu zmeny objemu a záporné znamienko znamená, že došlo k poklesu objemu počas transformácie. Táto premenná je bez jednotiek.

  * **Transformačná plasticita (TRNSFP)**

Pri transformácii sa materiál plasticky deformuje pri napätí nižšom, ako je napätie toku. Tento jav je známy ako transformačná plasticita ([TRNSFP](/docs/sk/Keyword_Documentation/T/TRNSFP/)). Zmena rozmerov súčiastky v dôsledku transformačnej plasticity nastáva v kombinácii so zmenami rozmerov v dôsledku objemovej zmeny vyvolanej transformáciou. V programe DEFORM je rovnica pre transformačnú plasticitu znázornená na obr. 10.9.4 a EQ(10.9.2).

  
![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_Image004.jpg)

Okno plasticity transformácie

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/EQ_10_9_2.jpg) |
---|---
  
Jediný údaj, ktorý musí používateľ pre tento vzťah poskytnúť, je koeficient plasticity transformácie. Ostatné členy sú automaticky vypočítané programom DEFORM. Koeficient plasticity transformácie môže byť funkciou teploty.  
Všeobecný rozsah pre ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/K_ij.jpg) pre oceľ je uvedený nižšie,

  * Austenit - ferit, perlit alebo bainit (4 - 13 *10-5 /MPa)
  * Austenit - martenzit (5 - 21 * 10-5 /MPa)
  * Ferit a perlit - austenit (6 - 21 *10-5 /MPa)

  * Ostatné

  * **Tepelný smer :** Tepelný smer poskytuje simulácii trochu viac informácií, takže transformácia nesprávne nevytvára objemový podiel. Napríklad pri zahrievaní ocele z izbovej teploty na teplotu austenitu sa akýkoľvek bainit časom premení na austenit. Počas ohrevu sa austenit môže premeniť späť na bainit, pretože môže byť definovaný ako možnosť. Táto definícia tomu zabraňuje. Odporúča sa používať ju šetrne. (Pozri obr. 10.9.5 )

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_Image005.jpg)

Okno ostatných vlastností transformácie

  * **Rovnovážny objemový zlomok :** Rovnovážny objemový zlomok definuje maximálne množstvo vytvoreného objemového zlomku fázy počas izotermického stavu.

  * **Model výberu variantov**

  * **Interfejná energia**
