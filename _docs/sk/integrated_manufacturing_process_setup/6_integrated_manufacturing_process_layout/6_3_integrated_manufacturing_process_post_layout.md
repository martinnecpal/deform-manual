---
lang: sk
title: "6.3. Integrated Manufacturing Process Post-processor layout"
---

# 6.3. Integrated Manufacturing Process (MO) Post layout

6.3.1. Step browser

  * Step Tools

  * Step list magnifier

  * Step Selection options

  * Right Mouse button step browser options

6.3.2. Graphics window

6.3.3. Post Tools

  * State variables

  * Tools

6.3.4. Output tree

Integrated Manufacturing Process (MO) Post mode is used to review the results. Post mode GUI layout (See Fig. 6.3.1.) is divided into Graphics window, Post Tools, Output Tree and Step browser regions. 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_3_integrated_manufacturing_process_post_layout/6_3_image001.jpg' | relative_url }})

MO Post mode GUI layout

  
**Graphics window** will display graphical representation of objects. The graphics window can be used for displaying the contour plots, graphs, grain flow, etc.

**Post Tools** are used to plot different state variables, point track the variables, studying the grain flow using flownet, extract the data, plot summary graphs, create the animation, etc.

**Output Tree** lists the objects and controls their display.

**Step browser** is used to select and play the simulated steps.

## Step browser

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_3_integrated_manufacturing_process_post_layout/6_3_image002.jpg' | relative_url }})

Step browser

  
Step browser (See Fig. 6.3.2.) is used to select steps to review, selected step objects will display in the graphics window. Different step selection options, step tools for quick step selection and playing steps options are available in step browser.

**Step Tools**

Step tools (See Fig. 6.3.3.) are used to navigate across the steps and operations in DB.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_3_integrated_manufacturing_process_post_layout/6_3_image003.jpg' | relative_url }})

Step tools

  
![]({{ '/assets/icons/post_icons/mo_first_step_icon.jpg' | relative_url }}) First step: Rewind the step list back to the first saved step.

![]({{ '/assets/icons/post_icons/mo_last step_icon.jpg' | relative_url }}) Last step: Fast forward to the last saved step in the step list.

![]({{ '/assets/icons/post_icons/mo_next_step_icon.jpg' | relative_url }}) Next step: Move to the next saved step in the step list.

![]({{ '/assets/icons/post_icons/mo_prevoius_step_icon.jpg' | relative_url }}) Previous step: Rewind the step list back to one saved step.

![]({{ '/assets/icons/post_icons/mo_play_button.jpg' | relative_url }}) Play forward: Displays the steps one by one until the last step is displayed from the current selected step.

![]({{ '/assets/icons/post_icons/mo_play_backward_icon.jpg' | relative_url }}) Play backward: Displays the steps one by one in reverse order until the first step is displayed from the current selected step.

![]({{ '/assets/icons/post_icons/mo_stop_button.jpg' | relative_url }}) Stop playing: Stops the playing (forward or backward) of steps.

**Step list magnifier**

Steps list can be magnified by using the Step list magnifier slide bar as shown in Fig. 6.3.2.

**Step Selection options**

Different step selection types are available like, outline, brief, auto, all and user (also available in ![]({{ '/assets/icons/pre_icons/mo_step_list.jpg' | relative_url }}) Step list), these can be used to select the required steps easily.

  
![]({{ '/assets/icons/pre_icons/mo_outline_button.jpg' | relative_url }}): When selected displays only the first and last step of the operations in the step editor

![]({{ '/assets/icons/pre_icons/mo_auto_button.jpg' | relative_url }}): When selected displays only first, last and one intermediate saved step of the operations in the step editor.

![]({{ '/assets/icons/pre_icons/mo_brief_button.jpg' | relative_url }}): When selected displays steps that are selected by system automatically for display in the step list.

![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) : When selected displays all saved steps of the all operations in the step editor.

![]({{ '/assets/icons/pre_icons/mo_step_list.jpg' | relative_url }}) : This will provide more detailed information of all saved steps like Simulation number, Mesh number, Time, Stroke of primary die, Dimension, Version number and Fold (for 3D). It also list the operations sequence on the left side window and provides more step selection option on right side window.

For more information of step selection types and step list options refer the [section 6.1.7 Step Editor](6_1_integrated_manufacturing_process_preprocessor_layout.htm#Step_Editor).

**Right Mouse button step browser options**

Right mouse click on step browser listed steps will give the options for step selection, display stroke or time at each step and plot few graphs like load, speed, volume and energy in step browser. (See Fig. 6.3.4.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_3_integrated_manufacturing_process_post_layout/6_3_image004.jpg' | relative_url }})

Step browser RMB option

  
**Show all steps:** This will list all steps in step browser, even those which are not saved in database.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_3_integrated_manufacturing_process_post_layout/6_3_image005.jpg' | relative_url }})

Step browser with all steps

  
**Show stored steps:** This will list all the stored steps which can be loaded and reviewed with all post features. Stored steps are highlighted by an orange dot in the step browser as shown in Fig. 6.3.5.

  
**Show selected steps:** This will list only those steps which were selected by using the ![]({{ '/assets/icons/pre_icons/mo_step_list.jpg' | relative_url }}) (step list) option.

  
**Display step:** This will display the step number in step browser for the steps which are displayed in step browser. (See Fig. 6.3.5..)

  
**Display stroke:** This will display the primary die stroke in step browser for the steps which are displayed in step browser. (See Fig. 6.3.6.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_3_integrated_manufacturing_process_post_layout/6_3_image006.jpg' | relative_url }})

Step browser displaying primary die stroke

  
**Display time:** This display the process time in step browser for the steps which are displayed in step browser. (See Fig. 6.3.7.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_3_integrated_manufacturing_process_post_layout/6_3_image007.jpg' | relative_url }})

Step browser displaying primary die time

  
**Load/Speed/Volume/energy graph** : This will plot the Load, Speed graphs in the selected direction in step browser. Volume and energy graphs can also be plotted as shown in Fig. 6.3.8.

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_3_integrated_manufacturing_process_post_layout/6_3_image008.jpg' | relative_url }})

Step browser displaying Energy, Volume, Speed and Load graphs

  
**Operation Info:** Right mouse click on the operation in the step browser gives the information about operation like dimension, number of objects, primary die number, range of step numbers, process time, primary die stroke.

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_3_integrated_manufacturing_process_post_layout/6_3_image009.jpg' | relative_url }})

Operation information for 3D operation

## Graphics window

Graphics window displays the graphical representation of the objects. This will display state variables contours over objects, graphs, histograms, flownet and die fill (contact nodes). (See Fig. 6.3.1.)

Right mouse click on the graphics window will provide few options to display the simulation information, set the viewport, measure dimension and change background theme. For more information about these options refer the [6.1.8. Graphics window RMB options.](6_1_integrated_manufacturing_process_preprocessor_layout.htm#Graphics_window_RMB_options)

## Post Tools

Post tools can be used to plot state variables contour plot, summary graphs, point tracking graphs, flownet for material flow analysis, mirroring the symmetry portions, animation file creation for presentation, 3d view mode for 2d objects and slicing operations for 3d objects. (See Fig. 6.3.10.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_3_integrated_manufacturing_process_post_layout/6_3_image010.jpg' | relative_url }})  
(a) 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_3_integrated_manufacturing_process_post_layout/6_3_image011.jpg' | relative_url }})

(b)

Post Tools window; (a) For 2D (b) For 3D

**State variables**

Some of the most commonly used state variables like ![]({{ '/assets/icons/post_icons/mo_disp_sv_icon.jpg' | relative_url }}) Total displacement, ![]({{ '/assets/icons/post_icons/mo_vel_sv_icon.jpg' | relative_url }}) (Total Velocity), ![]({{ '/assets/icons/post_icons/mo_strain_sv_icon.jpg' | relative_url }}) (Effective strain), ![]({{ '/assets/icons/post_icons/mo_strain_rate_sv_icon.jpg' | relative_url }}) (Effective strain rate), ![]({{ '/assets/icons/post_icons/mo_eff_stress_sv_icon.jpg' | relative_url }}) (Effective stress), ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) (Temperature) and ![]({{ '/assets/icons/post_icons/mo_damage_sv_icon.jpg' | relative_url }}) (Damage) shortcut icons can be used to view contour plot for the objects displaying on the graphics window. ![]({{ '/assets/icons/post_icons/mo_clear_sv_icon.jpg' | relative_url }}) (Clear State Variable) icon can be used to clear the selected state variable for the objects.

  
More state variables can be accessed using ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) (State variables setup) post tool bar icon as shown in Fig. 6.3.11. For more information on state variables different state variable groups and there plot options refer section [26.6.3. State Variables](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_3_state_variables/) [.](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_3_state_variables/)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_3_integrated_manufacturing_process_post_layout/6_3_image012.jpg' | relative_url }})

State variables window

**Tools**

MO post provides post processor tools (See Fig. 6.3.10.) like Point tracking, Flownet, Summary graphs, Load-Stroke graphs, Animation setup, 3D viewer (for 2D only), Mirroring (for 3D only) and slicing (for 3D only). These tools can be used to track the state variables variation at specific key locations, study the material flow behavior, know the important state variables min, max values variation throughout the simulation, predict the load, studying the lap areas and presentation.

  * **Summary**![]({{ '/assets/icons/post_icons/mo_summary_icon.jpg' | relative_url }}) [2D,3D]: Gives the Summary graphs for important state variables verses simulation time. For Detailed information refer the section [26.6.6. Summary.](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_6_summary/)

  * **Load** -**Stroke**![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) [2D,3D]: 

Gives the options to plot the Load, Speed, Torque, Angular velocity, Energy and Volume verses Time, Stroke, Step and Force. For Detailed information refer the section [26.6.7. Load Stroke.](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_7_load_stroke/)

  * **Point tracking**![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }}) [2D,3D]:

Using this state variable variation at any particular fixed or moving location in the objects can be tracked. For detailed information refer the section [26.6.9. Point Tracking.](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_9_point_tracking/)

  * **Flownet**![]({{ '/assets/icons/post_icons/mo_flownet_icon.jpg' | relative_url }}) [2D,3D]:

Using this user can create a grid pattern across the deforming object and observe the irregularities in the grain structure and surface defects such as folds. For detailed information refer the section [26.6.12. Flownet Tracking.](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/)

  * **Animation setup** ![]({{ '/assets/icons/post_icons/mo_animation_setup_icon.jpg' | relative_url }})[2D,3D]: 

Using this user can create simulation animation files in HTML, WMV, AVI and PPT formats. It also provides different options to change animation saving settings. For detailed information refer the section [26.6.19. Animation Setup](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_19_animation_setup/).

  * **3D viewer**![]({{ '/assets/icons/post_icons/mo_3d_view_icon.jpg' | relative_url }})[3D]:

Using this user can view the revolved or extruded 3d view of the 2d objects. For detailed information refer the section [26.6.20. 3D Viewer.](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_20_3d_setup/)

  * **Mirroring**![]({{ '/assets/icons/post_icons/mo_3d_mirroring_icon.jpg' | relative_url }})[3D]:

Using this user can visualize the full part in case of symmetric problem simulation. For detailed information refer the section [26.6.15. Mirroring Symmetry.](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_15_mirror_symmetry/)

  * **Slicing**![]({{ '/assets/icons/post_icons/mo_slice.jpg' | relative_url }})[3D]:

Using this user can section the objects at various depths and observe the state variable contours and defects in the cut area. For detailed information refer the section [26.6.16. Slicing.](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/)

## Output tree

The objects and its display information (such as objects visibility, geometry, mesh, transparency, slice plane, point tracking and Flownet information) is available in this window as shown in Fig. 6.3.12.

  
User can select the object to be visible display in graphics window by left click on the particular object in the tree and change its display modes. Point tracking and Flownet can be hidden or deleted by RMB click on the point tracking/Flownet tracking link in the output tree. 

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_3_integrated_manufacturing_process_post_layout/6_3_image013.jpg' | relative_url }})

Output Tree

  
**Operation tree tool bar options:** Using these options user can switch on or off the object, geometry, mesh, transparency, backface and contacts display. For detailed information refer the section [6.1.4. Operation Tree Tool Bar options](6_1_integrated_manufacturing_process_preprocessor_layout.htm#Operation_Tree_Tool_bar_options) from [Chapter 6.1. Intergrated Manufacturing process (MO) Pre-processor Layout.](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

**Database tab:**

This list the number of DB's available in the current project folder, it will be only one for the all MO operations except in case where Diestress study, DOE and Optimization has been carried over, in these cases the project folder will have more than one DB.

**Related Topics:**

[Post -processor](/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/)

[26.6.6.. Simulation summary](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_6_summary/)

[26.6.3. State Variables](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_3_state_variables/)

[26.6.7. Load Stroke](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_7_load_stroke/)

[26.6.9. Point Tracking](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_9_point_tracking/)

[26.6.12.. Flownet](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/)

[26.6.8. State variables distribution b/w two points](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_8_state_variables_between_2_points/)

[26.6.15. Mirroring](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_15_mirror_symmetry/)

[26.6.17. Data Extraction](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_17_data_extraction/)

[26.6.16. Slicing](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/)

[26.6.19. Animation controls and saving](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_19_animation_setup/)

[Operation Tree Tool Bar options](6_1_integrated_manufacturing_process_preprocessor_layout.htm#Operation_Tree_Tool_bar_options)
