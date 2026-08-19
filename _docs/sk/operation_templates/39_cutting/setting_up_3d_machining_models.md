---
lang: sk
title: "Nastavenie 3D modelov pre obrábanie"
---

# Nastavenie 3D modelov pre obrábanie

Definícia siete je najdôležitejším faktorom ovplyvňujúcim výkonnosť simulácie. Cieľom je prispôsobivo zjemniť sieť tak, aby sa zachovali malé prvky v oblastiach, kde sú potrebné na zachovanie geometrie alebo stavových premenných. Zároveň sa snažíme udržať celkový počet prvkov v simulácii na minimálnej úrovni.

Najvýznamnejším vylepšením programu DEFORM je lokálne prekresľovanie siete – namiesto úplného prekreslenia siete, ako tomu bolo v predchádzajúcich verziách programu DEFORM, sa prvky jednoducho rozdeľujú alebo zlučujú s cieľom zlepšiť kvalitu a prispôsobiť sa požiadavkám na veľkosť prvkov v danej oblasti. Prvky, ktoré spĺňajú miestne požiadavky na veľkosť a kvalitu, sa nemenia.

Hlavnými výhodami tejto novej funkcie sú to, že sa takmer (ak nie úplne) podarilo odstrániť problém s vymazaním prvku v dôsledku dotyku čipu s okrajom obrobku a že sa podstatne znížila zmena tvaru ostrých zákrut, ako je napríklad prvok polomeru špičky.

Bola implementovaná nová interpolačná schéma, ktorá využíva aproximáciu metódou najmenších štvorcov na základe okolitých prvkov a znižuje vyhladzovanie stavových premenných pri opakovanom prekresľovaní siete. Keďže definícia veľkosti prvkov siete vychádza z týchto stavových premenných (najmä deformácie), zmenilo sa aj správanie generovania siete.

V závislosti od toho, či sa používateľ zameriava predovšetkým na čip alebo na obrobok, sú vhodné rôzne prístupy k vytváraniu siete. Oba prístupy sú opísané nižšie.

_**A) Na zachytenie geometrie čipu**_

  * Tieto nastavenia zabezpečia dobré rozlíšenie v čipe, avšak môžu spôsobiť stratu alebo zjemnenie informácií o teplote, zvyškovom napätí a mikrostruktúre v obrobku.

  * Nie je potrebné používať okná pre vytváranie sietí. Takmer vo všetkých prípadoch správne definované adaptívne vytváranie sietí spoľahlivo poskytne kvalitnú sieť s podstatne menším počtom prvkov, ako je možné dosiahnuť pomocou okien pre vytváranie sietí.

  * Použite absolútnu veľkosť prvku. Nastavte minimálnu veľkosť prvku na približne 1/3 alebo ¼ hrúbky nesrezaného čipu. Hodnota ¼ poskytne lepšie výsledky, avšak doba spracovania bude výrazne dlhšia. 

  * Nastavte pomer veľkostí v rozmedzí od 10 do 15.

  * Použiť lokálne prečlenenie: v časti Mesh![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Kritériá prečlenenia![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Metóda prečlenenia ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) vyberte možnosť „Lokálny objemový model“

  * Nastavte posuvníky váhových koeficientov siete na 50 % deformácie, 50 % rýchlosti deformácie, všetky ostatné hodnoty = 0.

  * Generátor siete zvyčajne určuje zjemnenie siete na základe gradientu stavových premenných. Inými slovami, oblasť, v ktorej sa stavové premenné (deformácia alebo rýchlosť deformácie) rýchlo menia, bude mať relatívne jemné prvky, zatiaľ čo oblasti s vysokými konštantnými hodnotami budú mať relatívne hrubú sieť. Pri obrábaní potrebujeme jemné prvky v trieske (vysoká konštantná deformácia) a v primárnej zóne šmyku (vysoká rýchlosť deformácie). Ak chcete generátor siete nastaviť tak, aby to urobil, na karte „Váha“ zaškrtnite políčka „Rozloženie deformácie – Použiť gradient“ a „Rozloženie rýchlosti deformácie – Použiť gradient“.

**Zhrnutie**: (tieto nastavenia zachovajú geometriu čipu, avšak môžu spôsobiť stratu stavových premenných v obrobku)

  * Absolútna veľkosť prvku – minimálna veľkosť 1/3 až ¼ hrúbky nerezaného čipu. Pomer veľkostí 10 až 15.

  * Miestna pevná látka

  * Posuvník s váhou 50 % deformácie, 50 % rýchlosti deformácie

  * Na karte „Váhový faktor“ zaškrtnite políčka „Rozloženie deformácie – Použiť gradient“ a „Rozloženie rýchlosti deformácie – Použiť gradient“.

**B) Na zaznamenávanie vlastností obrobku**

V prípade simulácií, pri ktorých sú dôležité vlastnosti povrchu obrobku (zvyškové napätie, mikrostruktúra, teplota), ale geometria špánia nie je dôležitá. Pri týchto simuláciách môže byť užitočné použiť okno siete, aby sa zachovala veľkosť ok na reznom povrchu. Vhodné môže byť aj vytváranie siete na základe deformácie. Používateľ môže vyskúšať oba prístupy, aby zistil, ktorý z nich poskytuje lepšie výsledky.

**S oknami so sieťkou:**

  * Použite absolútnu veľkosť prvku. Použite pomer veľkosti 1 a nastavte globálnu veľkosť prvku tak, aby bola približne 5-krát väčšia ako očakávaná hrúbka povrchovej vrstvy. Na spresnenie siete v povrchovej vrstve sa použijú okná.

  * Vymedzte okno s mriežkou tak, aby začínalo tesne pred hrotom nástroja a rozprestieralo sa smerom dozadu. Nastavte pohyb okna tak, aby sledovalo rezací nástroj. Okno sa môže rozprestierať značne za obrobkom, takže s postupom nástroja pokrýva čoraz väčšiu časť povrchu obrobku.

  * Veľkosť prvkov v okne nastavte približne na 30–70 % veľkosti očakávaného efektu povrchovej vrstvy. Inými slovami, ak sa zmeny zvyškového napätia vyskytujú v hĺbke 0,01 mm, minimálna veľkosť prvku by mala byť približne 0,005 mm. Uvedomte si, že vždy bude existovať náročná rovnováha medzi primeraným rozlíšením a prijateľnou dĺžkou výpočtu.

  * Pomer veľkostí medzi prvkami vo vnútri okna a prvkami mimo okna by nemal presiahnuť približne 5:1. V prípade potreby by sa mali použiť vnořené okná, pričom medzi susednými oknami by sa mal zachovať pomer 5:1. Najmenšie prvky (najvnútornejšie okno) by mali byť uvedené ako prvé v zozname okien.

  * Posuvné lišty by mali byť nastavené buď tak, aby sa okná úplne zosúladili, alebo približne na 80 % zosúladenia okien, pričom zvyšných 20 % by sa malo rozdeliť medzi deformáciu a rýchlosť deformácie.

  * Lokálne prečlenenie siete lepšie zachová stavové premenné. Použite lokálne prečlenenie siete: v časti Mesh![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Kritériá prečlenenia siete![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Metóda prečlenenia siete vyberte možnosť „Local Solid“.

**Bez sieťových okien:**

  * Použite absolútnu veľkosť prvku, pričom minimálna veľkosť prvku by mala predstavovať 30–70 % očakávanej hrúbky povrchovej vrstvy.

  * Použite pomer veľkostí 10

  * Použiť miestny pevný materiál

  * Nový interpolačný algoritmus dokáže dobre zachovať deformáciu na reznom povrchu obrobku, takže ho možno použiť ako kľúčový parameter vytvárania siete. Nastavte posuvníky na 80 % deformácie a 20 % rýchlosti deformácie.

  * Zaškrtnite políčko „Skontrolovať rozloženie deformácie – Použiť gradient“. Tým sa zabezpečí, že generátor siete zachová jemnú sieť v oblastiach s vysokou deformáciou (t. j. na reznom povrchu). Obsah súboru je ľubovoľný.

**Súvisiace témy:**

[Object Mesh Data](/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/)
