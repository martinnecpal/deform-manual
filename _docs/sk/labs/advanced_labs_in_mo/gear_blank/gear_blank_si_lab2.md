---
lang: sk
title: "Gear Blank SI Lab 2"
---

# Lab 2 . 2D to 3D Conversion to sequence 3D operation after 2D operation

The next simulation will be continued in 3D mode. So to start preprocessing in 3D mode, load the results from the previous 2D simulation and convert the workpiece to 3D as described in this lab.

### Add Convertor operator

To convert the workpiece results of previous 2D operation, 2D to 3D convert operator must be added after 2D operation. Click on the ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 2D to 3D Convertor under Simulation Operators list from **Explorer![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Operations** tab as shown in [Fig. L2.1.](gear_blank_si_lab2.htm#Fig_l2_1_Adding_2D_to_3D_Convertor_Operator)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab2_image0001.jpg' | relative_url }})

Adding 2D to 3D Convertor Operator

### Select Converter Setting

Select the 2D to 3D convertor operator from operation editor to open the convertor operator. Select the ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}) button for Setup type popup (see [Fig. L2.2.](gear_blank_si_lab2.htm#Fig_L2_2_Setup_type_popup_for_operation_2_2D_to_3D_converter)) to setup the problem in batch mode.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab2_image0002.jpg' | relative_url }})

Setup type popup for operation 2 2D to 3D converter

Select **Y** is up radio button, confirm the **revolution****angle** is **360** and **start****angle** is **0** as shown in [Fig. L2.3.](gear_blank_si_lab2.htm#Fig_L2_3_Configuration_settings_window) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to select the objects to convert.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab2_image0003.jpg' | relative_url }})

Configuration settings window

### Select Conversion Objects

Opening operator will pass all objects. As top and bottom dies need to change for next operation, retain only Workpiece object. So select Top die object and click on ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) (Delete Object) button to delete the Top die. Similarly delete Bottom die object as shown in [Fig. L2.4.](gear_blank_si_lab2.htm#Fig_L2_4_Object_selection_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab2_image0004.jpg' | relative_url }})

Object selection window

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for objects and also workpiece windows as no changes required in workpiece window.

### Generate Workpiece 3D geometry

Check output geometry and confirm that geometry type is Solid, accept default number of sections and click on ![]({{ '/assets/icons/pre_icons/mo_3d_preview_button.jpg' | relative_url }}) button to generate the 3D geometry (see [Fig. L2.5.](gear_blank_si_lab2.htm#Fig_L2_5_Geometry_conversion_window)). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate the mesh for 3D geometry.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab2_image0005.jpg' | relative_url }})

Geometry conversion window

### Generate Workpiece 3D mesh

Select tetrahedron mesh type and change the Target number of elements to **20,000**. Click the ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) button to generate 3D mesh (see [Fig. L2.6.](gear_blank_si_lab2.htm#Fig_L2_6_Mesh_conversion_window)).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab2_image0006.jpg' | relative_url }})

Mesh conversion window

If geometry or mesh or both not converted in respective windows then in **Convert** window user can convert the geometry, mesh or both for all objects at a time using ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) button as per the selections status displayed in the table as shown in [Fig. L2.7.](gear_blank_si_lab2.htm#Flg_l2_7_Convert_window_to_convert_both_geometry_and_mesh_at_a_time)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab2_image0007.jpg' | relative_url }})

Convert window to convert both geometry and mesh at a time

### Generate Database after conversion

Select the Generate DB in operation tree and click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate DB required for the 3D operation.

The workpiece at this point will be the input for the second operation. Factors such as accurate shape, strain (work hardening), damage, metal flow, temperature distribution (when calculated) and other information will be retained.

Click on [Gear Blank SI Lab 3](/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/) to continue the sequential 3D operation.
