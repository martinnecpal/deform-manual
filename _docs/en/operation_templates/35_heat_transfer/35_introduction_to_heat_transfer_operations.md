---
lang: en
title: "35. Introduction to Heat Transfer Operations"
---

# 35\. Introduction to Heat Transfer Operations

Heat Transfer operation will help the user to simulate various heating/cooling operations in forming process which involve temperature change and deformation. The operations are customized to setup only heat transfer process during forming like heating workpiece, transferring workpiece form furnace to press, resting workpiece on die (before forming) and dwelling after forming. Appropriate selection of heat transfer type (heating, transfer, resting or dwelling) will add related settings windows and guide the user to quickly setup the heat transfer operations during hot/warm forging operations.

There are four types of heat transfer operations available in both 2D and 3D,

  1. Heat in Furnace

  2. Transfer through Air

  3. Rest on die and

  4. Dwell on die

**Heat in Furnace:** In heating or heat furnace operation, heating of billet in a furnace is modelled. The default process settings will be added suited to heating operation (See [Table. 35.1.](35_introduction_to_heat_transfer_operations.htm#Table_35_1_Default_process_settings_\(heat_condition\)_and_object_temperatures_for_different_heating_types)), changes can be made to the default setting while defining the particular operation.

**Transfer through Air:** In Transfer through Air operation, heat transfer or heat loss to environment while transferring workpiece/billet to the die is modelled. By default one object, workpiece, will be added to the project tree for this operation. The default process settings for Transfer through Air are as shown in [Table. 35.1.](35_introduction_to_heat_transfer_operations.htm#Table_35_1_Default_process_settings_\(heat_condition\)_and_object_temperatures_for_different_heating_types)

**Rest on die:** In Rest on die operation, heat transfer or heat loss to environment and die from workpiece/billet while resting on die before the top die makes contact with the workpiece/billet is modelled. By default workpiece, top and bottom die objects will be added to the project tree. Default process settings for Rest on die operation is as shown in [Table. 35.1.](35_introduction_to_heat_transfer_operations.htm#Table_35_1_Default_process_settings_\(heat_condition\)_and_object_temperatures_for_different_heating_types)

**Dwell on die:** In this operation, heat transfer or heat loss to environment and die from workpiece/billet after deformation (after the dies retract from the workpiece) is modelled. By default workpiece, top and bottom die objects will be added to the project tree. Default process settings for Dwell on Die operation is as shown in [Table. 35.1.](35_introduction_to_heat_transfer_operations.htm#Table_35_1_Default_process_settings_\(heat_condition\)_and_object_temperatures_for_different_heating_types)

**Heating type** |  **Workpiece Temperature** **(C or F)** |  **Dies Temperature** **(C or F)** |  **Process Time** **(sec)** |  **Env ironment Temperature** **(C or F)** |  **Convection coefficient** **(N/sec/mm/C or Btu/sec/in^2/F)**  
---|---|---|---|---|---  
Heat in Furnace |  1232 C or 2250 F |  NA |  3600 |  1200 C or 2250 F |  0.02 N/sec/mm/C or 7.7e-6 Btu/sec/in^2/F  
Transfer through Air |  1232 C or 2250 F | NA |  15 |  20 C or 68 F |  0.02 N/sec/mm/C or 7.7e-6 Btu/sec/in^2/F  
Resting |  1232 C or 2250 F |  20 C or 68 F |  4 |  20 C or 68 F |  0.02 N/sec/mm/C or  
7.7e-6 Btu/sec/in^2/F  
Dwelling |  1232 C or 2250 F |  20 C or 68 F |  4 |  20 C or 68 F |  0.02 N/sec/mm/C or 7.7e-6 Btu/sec/in^2/F  
  
Default process settings (heat condition) and object temperatures for different heating types

For more information about the all four heat transfer operations setup refer the [35.1. 2D Heat Transfer Operation]() and [35.2. 3D Heat Transfer Operation]().
