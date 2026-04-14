---
lang: sk
title: "36. Intorduction to Heat Transfer Express Operations"
---

# 36\. Introduction to Heat Transfer Express Operations

Heat transfer is energy in transit due to temperature difference. Whenever there exist a temperature difference in a medium or between media, heat transfer must occur. Heat transfer mechanisms can be grouped into 3 broad categories:

**Conduction** : Heat transfer through a solid material by contact of one molecule to the next. Heat flows from a higher-temperature area to a lower-temperature one. 

  
**Convection** : A heat transfer process involving motion in a fluid (such as air) caused by the difference in density of the fluid and the action of gravity.

  
**Radiation** : The transfer of heat in the form of electromagnetic waves from one separate surface to another. The energy radiated is either transmitted, absorbed, reflected or a combination of all three.

  
In Multiple operations Heat transfer Express operations will simulate only heat transfer by conduction and convection modes.

  
Heat Transfer Express operations are customized to setup only heat transfer process during forging like heating workpiece, transferring workpiece form furnace to press, resting workpiece on die (before forming) and workpiece dwell on die after forming. Using these operation user can setup the multiple operations to replicate the real life hot or warm forging process in one go. Appropriate selection of heat transfer type (heating, transfer, resting or dwelling) will add related settings windows and guide the user to quickly setup the heat transfer operations during hot/warm forging operations only in guided mode.

There are four heating types or heat transfer operations available in both 2D and 3D Heat Transfer Express operation those are (See [Fig. 36.1]().),

  1. Heating

  2. Transfer

  3. Rest on die and

  4. Dwell on die

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/image001.jpg' | relative_url }})

2D and 3D Process settings window

  
**Heating** : In heating or heat furnace operation, heating of billet in a furnace is modeled. Only one object is allowed for this operation and that object will be added automatically. The default process settings will be added suited to heating operation (See Table. 36.1.), changes can be made to the default setting while defining the particular operation.

**Transfer** : In heat transfer operation, heat transfer or heat loss to environment before workpiece/billet is placed on the die is modeled. By default one object, workpiece, will be added to the project tree for this operation. The default process settings for heat transfer is as shown in Table. 36.1.

**Rest on die** : In heat resting operation, heat resting on the die prior to deformation is modeled. By default workpiece, top and bottom die objects will be added to the project tree. Default process settings for heat resting operation is as shown in Table. 36.1.

**Dwell on die** : In heat dwell operation, heat transfer after deformation (after the dies retract from the workpiece) is modeled in this operation. By default workpiece, top and bottom die objects will be added to the project tree. Default process settings for heat resting operation is as shown in Table. 36.1.

**Heating type** |  **Workpiece Temperature** **(C or F)** |  **Dies Temperature** **(C or F)** |  **Process Time** **(sec)** |  **Env ironment Temperature** **(C or F)** |  **Convection coefficient** **(N/sec/mm/C or Btu/sec/in^2/F)**  
---|---|---|---|---|---  
Heating |  1200 C or 2250 F |  NA |  3600 |  1200 C or 2250 F |  0.0226611 N/sec/mm/C or 7.7e-6 Btu/sec/in^2/F  
Transfer |  1200 C or 2250 F | NA |  15 |  20 C or 68 F |  0.0226611 N/sec/mm/C or 7.7e-6 Btu/sec/in^2/F  
Resting |  1200 C or 2250 F |  150 C or 300 F |  4 |  20 C or 68 F |  0.0226611N/sec/mm/C or 7.7e-6 Btu/sec/in^2/F  
Dwelling |  1200 C or 2250 F |  150 C or 300 F |  4 |  20 C or 68 F |  0.0226611 N/sec/mm/C or 7.7e-6 Btu/sec/in^2/F  
  
Default process settings (heat condition) and object temperatures for different heating types

Default process settings (heat condition) and object temperatures for different heating types

  
For more information about the all four heat transfer operations setup refer the [2D Heat Transfer Express Operation](/docs/sk/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/) and [3D Heat Transfer Express Operation](/docs/sk/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/).

**Related Topics:**

[36.1. 2D Heat Transfer Express Operation](/docs/sk/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/)

[36.2. 3D Heat Transfer Express Operation](/docs/sk/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/)
