---
lang: sk
title: "6.6.3. Editing Operations"
---

# 6.6.3. Editing Operations

The operations added to the project can be edited by select the operations to edit from Operation Editor, the selected operation contents will reflect in operation tree or property editor as shown in Fig. 6.6.3.1. Using operation tree or property editor user can sequentially edit the operations.

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_1_connecting_operations/6_6_1_image004.jpg' | relative_url }})

Selecting operation for editing

  
If the user would like to modify the existing setup of already simulated DB then user has to switch to Pre tab and use Step Editor option to select the appropriate step to modify the setup and continue simulation. Step editor tab is available in same session in Pre mode only if DB is having atleast one positive step or new session is opened after DB generation, steps available for selection in Step Editor is shown in Fig. 6.6.3.2. Once the appropriate step is selected the operation tree or property editor will reflect the contents of the operation at the selected step. (See Fig. 6.6.3.3.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_3_editing_operations/6_6_3_image001.jpg' | relative_url }})

Step editor

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_3_editing_operations/6_6_3_image002.jpg' | relative_url }})

Step editor with intermediate step selected for editing

For more details on property editor setting of typical forming operation refer the chapter [Forming Operation Setup](/docs/sk/operation_templates/33_forming/33_introduction_to_forming/).

![]({{ '/assets/icons/pre_icons/mo_outline_button.jpg' | relative_url }}): When selected displays only the first and last step of the operations in the step editor

![]({{ '/assets/icons/pre_icons/mo_auto_button.jpg' | relative_url }}): When selected displays only first, last and one intermediate saved step of the operations in the step editor.

![]({{ '/assets/icons/pre_icons/mo_brief_button.jpg' | relative_url }}): When selected displays steps that are selected by system automatically for display in the step list.

![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) : When selected displays all saved steps of the all operations in the step editor.

![]({{ '/assets/icons/pre_icons/mo_step_list.jpg' | relative_url }}) : This will provide more detailed information of all saved steps like Simulation number, Mesh number, Time, Stroke of primary die, Dimension, Version number and Fold (for 3D). It also list the operations sequence on the left side window and provides more step selection option on right side window.

For more information on step selection types and step list options refer the section [6.1.7 Step Editor.](../6_1_integrated_manufacturing_process_preprocessor_layout.htm#Step_Editor)

**Related Topics:**

[6.1. Integrated Manufacturing Porcess (MO) Pre-processor Layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

[Forming Operation ](/docs/sk/operation_templates/33_forming/33_introduction_to_forming/)
