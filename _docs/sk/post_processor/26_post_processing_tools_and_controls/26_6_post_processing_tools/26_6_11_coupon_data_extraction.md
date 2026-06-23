---
lang: sk
title: "26.6.11. Extrakcia údajov z kupónov"
---

# 26.6.11. Extrakcia údajov z kupónov ![]({{ '/assets/icons/post_icons/mo_coupon_data_extraction_icon.jpg' | relative_url }})

Kvalifikácia dielov si vyžaduje podrobné vyhodnotenie kritických miest z hľadiska mikrostruktúry a zmien mechanických vlastností. Priemysel potrebuje identifikovať kritické oblasti v diele na základe výsledkov modelovania tvárnenia a tepelného spracovania. Pre tieto identifikované kritické oblasti bola v programe DEFORM vyvinutá funkcia na uľahčenie procesu extrakcie stavových premenných z modelovania, nazývaná „Extrakcia údajov z vzoriek“ alebo „Vzorky“.

Na získanie údajov z kupónov musí používateľ postupovať podľa nižšie uvedených krokov,

  1. V stromovej štruktúre objektov vyberte objekt, ku ktorému chcete pridať kupón.

  2. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať), aby ste pridali kupóny. (Pozri obr. 26.6.11.1.)

  3. Vyberte každý kupón a pomocou geometrického tvaru a parametrov určte kritické oblasti v objekte. (Pozri obr. 26.6.11.1.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_11_coupon_data_extraction/image001.jpg' | relative_url }})

Príklad extrakcie údajov z kupónov pre 2D

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_11_coupon_data_extraction/image002.jpg' | relative_url }})

Príklad extrakcie údajov z kupónov pre 3D

  
Kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }}) (Nastavenia) vyberte výstupy, ktoré chcete extrahovať. (Pozri obr. 26.6.11.2.)

V okne Nastavenia vyberte stavové premenné a kliknite na OK. (Pozri obr. 26.6.11.3.)

Kliknite na ![]({{ '/assets/icons/post_icons/mo_extract_varaibles_button.jpg' | relative_url }}). (Pozri obr. 26.6.11.2.)

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_11_coupon_data_extraction/image003.jpg' | relative_url }})

Okno nastavení výberu premenných stavu extrakcie údajov z kupónov

  
Sledujte výsledky a v prípade potreby ich môžete uložiť do súboru CSV, ktorý je kompatibilný s programom Excel. (Pozri obr. 26.6.11.4. a obr. 26.6.11.5.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_11_coupon_data_extraction/image004.jpg' | relative_url }})

Okno s výsledkami extrakcie údajov z kupónov pre 2D 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_11_coupon_data_extraction/image005.jpg' | relative_url }})

Okno s výsledkami extrakcie údajov z kupónov pre 3D 

  
Výsledky obsahujú hodnoty stavových premenných v stredových bodoch a hodnoty Min~Max v rámci vzorky, ako je znázornené na obr. 26.6.11.4.
