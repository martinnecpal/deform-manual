---
lang: sk
title: "6.6.5. Adding Cycles"
---

# 6.6.5. Adding Cycles

  * Introduction to Add cycles

  * Add Cycles

  * Delete Cycles

  * Changing the number of cycles

  * Change the name of the cycle operation

  * Moving operations (Drag and Drop)

  * Examples

**Introduction to Add cycles**

Add cycles to am operation performs same operations repetitively in cycle. User needs to select the operations to repeat and the number of times to repeat (See Fig. 6.6.5.1.). To add cycle to operation, the first operation in cycle must have read from DB object. To analyze the die stress and temperatures after the multiple components manufacturing is an example where user can use the cycles, user can add as number of cycles as components produced.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image018.jpg' | relative_url }})

Extent to use the add cycles

**Add Cycles**

All the operations to be cycled must be selected by using the Left mouse button (LMB) and Ctrl button from Keyboard and then RMB click on any of the selected operation will give option to select Add Cycles as shown in Fig. 6.6.5.2.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_5_adding_cycles/6_6_5_image006.jpg' | relative_url }})

(a)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_5_adding_cycles/6_6_5_image007.jpg' | relative_url }})

(b)

Add cycles from Operation editor; (a) Before adding the cycle (b) After adding the cycle

The other option to cycle operations is by adding the cycle operator from operations explorer 'Simulation operator" as shown in Fig. 6.6.5.3.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_5_adding_cycles/6_6_5_image008.jpg' | relative_url }})

Adding cycle operator from Operations explorer

After adding the cycle an orange color outline appears in operation editor around the operations that are cycled (See Fig. 6.6.5.2b) and Add cycles property window opens in property editor. In add cycles property window user has can enter the required number of cycles and select button to update the changes as shown in Fig. 6.6.5.4. The text on the outline of the operations that are cycled indicates the number of cycles as shown in Fig. 6.6.5.5.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_5_adding_cycles/6_6_5_image009.jpg' | relative_url }})

Add cycles property window

**Delete Cycles**

Added cycles can be removed easily from RMB click options on the orange outline around cycled operations in operation editor and selecting option Delete cycle as shown in Fig. 6.6.5.5.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_5_adding_cycles/6_6_5_image010.jpg' | relative_url }})

Delete added cycle option

**Changing the number of cycles**

By clicking on the border (orange outline) around the cycled operations in the operation editor cycles property editor window will open, in this window user can change the number of cycles and click apply to apply changed number of cycles as shown in Fig. 6.6.5.6.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_5_adding_cycles/6_6_5_image001.jpg' | relative_url }})

Changing number of cycles

**Change the name of the cycle operation**

By default cycle operation is named by "cycle (number of cycles)" on the outline around cycled operations. Cycle operation name can be changed by clicking on the cycle default name on the orange outline and after changing the name press the enter button from keyboard as shown in Fig. 6.6.5.7.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_5_adding_cycles/6_6_5_image002.jpg' | relative_url }})

Changing the cycle operation name

**Moving operations (Drag and Drop)**

After adding cycles by selecting a set of operations, user can move operations into or out of cycles by drag and dropping the operation into and out of cycle in operation editor as shown in Fig. 6.6.5.8.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_5_adding_cycles/6_6_5_image003.jpg' | relative_url }})

Moving operations into and out of the cycle

**Examples**

**Example1** : Steady state thermal behavior of the dies for multiple hits can be setup by adding the cycles to the operation in which keeping the same die set from previous forming operation and changing the workpiece. This changes the workpiece in each forming cycle by keeping the same dies with previous hits thermal history. The operation editor for such cycle operation looks like as shown in Fig. 6.6.5.9.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_5_adding_cycles/6_6_5_image004.jpg' | relative_url }})

Operation editor for example1

**Example2:** In extrusion simulation computational efficiency can be increased by removing the material outside the area of interest. This is done by breaking down the extrusion into multiple cycles and cutting the workpiece in each cycle with boolean operation. The operation editor for such cycle operation looks like as shown in Fig. 6.6.5.10.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_5_adding_cycles/6_6_5_image005.jpg' | relative_url }})

Operation editor for example2

**Related Topics:**

[6.1. Integrated Manufacturing Porcess (MO) Pre-processor Layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)
