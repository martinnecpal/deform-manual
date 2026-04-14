---
lang: en
title: "26.4. Simulation Step Display Controls"
---

# 26.4. Simulation Step Display Controls

26.4.1. Step Menu and Step tools

26.4.2. Steps Selection options

26.4.3. Step list

26.4.4. Relative Motion

Step browser (See Fig. 26.4.1.) is used to select simulated steps for review, object of selected step objects will display in the graphics window. Step view window has options for selecting different steps & operations and step tools for quick step selection & playing steps. Step view window also displays information like simulation title, operation name, stroke, time, selected step and operation number. (See Fig. 26.4.1.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_4_simulation_step_display_controls/image001.jpg' | relative_url }})

Step view window

## Step Menu and Step tools 

The various options available for quick step selection, playing the steps and operations selection are explained below. Even under **Step menu** we are having below options as shown in Fig. 26.4.2.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_4_simulation_step_display_controls/image006.jpg' | relative_url }})

Post processor Step menu

**First step** ![]({{ '/assets/icons/post_icons/mo_first_step_icon.jpg' | relative_url }}) : Rewind the step list back to the first saved step.

**Last step** ![]({{ '/assets/icons/post_icons/mo_last step_icon.jpg' | relative_url }}): Fast forward the step list to the last saved step.

**One step forward** ![]({{ '/assets/icons/post_icons/mo_next_step_icon.jpg' | relative_url }}) : Move to the next saved step in the step list.

****One step backward** **![]({{ '/assets/icons/post_icons/mo_prevoius_step_icon.jpg' | relative_url }}): Rewind the step list back to one saved step.

**Play forward**![]({{ '/assets/icons/post_icons/mo_play_button.jpg' | relative_url }}) : Displays the steps one by one until the last step is displayed from the current selected step.

**Play backward![]({{ '/assets/icons/post_icons/mo_play_backward_icon.jpg' | relative_url }})** : Displays the steps one by one in reverse order until the first step is displayed from the current selected step.

**Pause**![]({{ '/assets/icons/post_icons/mo_stop_play_backward_icon.jpg' | relative_url }}) : Stops the playing of steps.

**Op******e** ration forward ![]({{ '/assets/icons/post_icons/mo_next_oprn_icon.jpg' | relative_url }})**: Move to the current operation last saved step or next operation first saved step in the step list.

****Op******e** ration backward ** **![]({{ '/assets/icons/post_icons/mo_prev_oprn_icon.jpg' | relative_url }}): Move to the previous operation last saved step or current operation first saved step in the step list.

**Simulation**forward** ![]({{ '/assets/icons/post_icons/mo_next_oprn_icon.jpg' | relative_url }})**: Move to the current simulation last saved step or next simulation first saved step in the step list.

****Simulation******backward**** **![]({{ '/assets/icons/post_icons/mo_prev_oprn_icon.jpg' | relative_url }}): Move to the previous simulation last saved step or current simulation first saved step in the step list.

## Steps Selection options

User can select the required steps from the stored steps in the DB for display. Different step selection types are available like, outline, brief, auto, all and user (also available in Step list ![]({{ '/assets/icons/post_icons/mo_step_list_icon.jpg' | relative_url }})).

**Auto** : When this option is selected, the steps for display are selected by system automatically.

**First** : When this option is selected, only the first step of all operations is displayed.

**Last** : When this option is selected, only the last step of all operations is displayed.

**All** : When this option is selected, all saved steps of the all operations in the step editor are displayed.

**Brief** : When this option is selected, only first, last and one intermediate saved step of the operations in the step editor are displayed.

**User****defined** : When this option is selected, steps that are selected for display from the ![]({{ '/assets/icons/post_icons/mo_step_list_icon.jpg' | relative_url }}) (step list) are displayed. Using this user can select the required steps to display.

## Step list ![]({{ '/assets/icons/post_icons/mo_step_list_icon.jpg' | relative_url }})

This will provide more detailed information of all saved steps like Simulation number, Mesh number, Time, Stroke of primary die, Dimension, Version number and Fold (for 3D). It also lists the operations sequence on the left side window and provides more step selection options on right side window (see Fig. 26.4.3.). For more information on step selection types and step list options refer section [6.1.6. Step Editor](../../integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout.htm#6.1.6._Step_Editor).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_4_simulation_step_display_controls/image002.jpg' | relative_url }})

Step List step selection options

## Relative Motion [3D] ![]({{ '/assets/icons/post_icons/mo_relative_motion_button.jpg' | relative_url }})

For the benefit of improving numerical errors resulting from positioning, geometry updates, etc., the simulation model sometimes requires users to move / rotate object(s) artificially. The new “relative motion” function allows users to view the simulation result that is identical to the actual processes (See Fig. 26.4.4.). User can select the reference object and the stationary axis along with the movement type. The reference object is an object that is stationary in actual process while for numerical purpose movement is applied. Once the selection is done user can click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button, then the user can observe that all other objects will move relatively with the reference object while reference object stays stationary as per the defined conditions.

**Applications:**

Cogging

Spinning

Flowforming

Etc.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_4_simulation_step_display_controls/image003.jpg' | relative_url }})

Relative motion window

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_4_simulation_step_display_controls/image004.jpg' | relative_url }})

Translation type relative motion window

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_4_simulation_step_display_controls/image005.jpg' | relative_url }})

Rotation type Relative motion window

**Related Topics:**

[26\. Post Processor Features](/docs/en/post_processor/26_post_processing_tools_and_controls/26_post_processor_features/)

[26.2. Viewport and Windows menu](/docs/en/post_processor/26_post_processing_tools_and_controls/26_2_handeling_viewports_and_windows_iin_post_processor/)
