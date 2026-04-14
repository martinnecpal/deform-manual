---
lang: sk
title: "55.2. Arc Welding"
---

# Arc Welding

In this lab we will demonstrate how to setup simple Arc welding operation.

1.1. Creating a New Problem

1.2. Adding Forming Operation

1.3. Simulation Controls

1.4. Material list

1.5. Object

1.5.1. Workpiece

1.5.1.1. Bottom Plate Geometry

1.5.1.2. Bottom Plate Mesh

1.5.1.3. Bottom Plate Material

1.5.1.4. Bottom Plate Boundary condition

1.5.1.5. Initialize Volume fraction for Bottom Plate

1.5.2. Top Die

1.5.2.1. Top Plate Geometry

1.5.2.2. Top Plate Mesh

1.5.2.3. Top Plate Material

1.5.2.4. Top Plate Boundary condition

1.5.2.5. Initialize Volume fraction for Top Plate

1.5.3. Bottom Die

1.5.3.1. Bead 1 Geometry

1.5.3.2. Bead 1 Mesh

1.5.3.3. Bead 1 Material

1.5.3.4. Bead 1 Boundary condition

1.5.3.5. Initialize Volume fraction and Additive manufacturing for Bead 1

1.6. Contact

1.7. Stopping Controls

1.8. Step Controls

1.9. Generate DB

1.10. Running Simulation

1.11. Post Processing

## Creating a New Problem 

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear, as shown in Fig. AWL1.1.

![]({{ '/assets/images/applications/55_2_arc_welding/image0001.jpg' | relative_url }})

QT4 GUI Main window

  
Create a new problem either by selecting **File**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. AWL1.2. Select " **Integrated Manufacturing Process** " radio button and unit system as "**SI** " radio button in unit field. Define Problem Name as " **ARC_WELDING_LAB** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

New Problem page

  
Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "**ARC_WELDING_LAB** " as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

##  Adding Forming Operation

Add 3D Forming operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to [3D] Forming or can also be added by drag and drop into the Operation editor (See Fig. AWL1.3.). When we add the Forming operation, process settings window will open by default.

![]({{ '/assets/images/applications/55_2_arc_welding/image0003.jpg' | relative_url }})

Adding 3D Forming operation from Explorer

## Simulation Controls

Check "**Deformation** ", "**Heat Transfer** " and "**Transformation** " mode check boxes as show in Fig. AWL1.4. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0004.jpg' | relative_url }})

Simulation Controls - Guided mode

## Material list

Using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button import material from " **ARC_Welding_Material.key** " file from**/3D/ LABS / Arc_Welding** folder path. Imported material is displayed as shown in below Fig. AWL1.5. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until object page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0005.jpg' | relative_url }})

Material list

## Object

For this lab we need three objects, in the list keep all three objects, Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece page.

### Workpiece

In Workpiece page, change the object name to "**Bottom Plate** ", object type as "**Elasto-Plastic** " and select "**Mixed (Tet mesh)** " option from drop - down menu. Keep the object temperature as **20°C** as shown in Fig. AWL1.6.

![]({{ '/assets/images/applications/55_2_arc_welding/image0006.jpg' | relative_url }})

Bottom Plate General page

#### Bottom Plate Geometry

In Geometry page, using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button import **Bottom_Plate.stl** file from **/3D/ LABS/Arc_Welding** folder (see Fig. AWL1.7.), after importing geometry use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) action label to check the Geometry and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close the popup. 

![]({{ '/assets/images/applications/55_2_arc_welding/image0007.jpg' | relative_url }})

Bottom Plate Geometry page

  
Click on **Symmetry planes** , add planar symmetry plane on **+X** direction surface of Bottom Plate, similarly add**-X** Direction surface and **-Y** direction surface as shown in Fig. AWL1.8. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the symmetry planes and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0008.jpg' | relative_url }})

Symmetry planes page

#### Bottom Plate Mesh

Define the **Number of Elements** as **35000** and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) and click **Yes** in "Default Boundary Conditions" popup to assign default boundary condition for Bottom plate. Generated mesh for Bottom plate looks like as shown in Fig. AWL1.9. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0009.jpg' | relative_url }})

Bottom Plate Mesh page

#### Bottom Plate Material

Assign "**S45C-JAPAN** " material from list for Bottom Plate as shown in Fig. AWL1.10. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary Condition page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0010.jpg' | relative_url }})

Bottom Plate Material page

#### Bottom Plate Boundary condition

Observe the default Symmetry BCC data assigned to Bottom plate while generating mesh, Symmetry BCC will be assigned to +X direction, -X direction and -Y direction surfaces as we defined in Geometry - Planar symmetry page (See Fig. AWL1.11..)

![]({{ '/assets/images/applications/55_2_arc_welding/image0011.jpg' | relative_url }})

Assigned Symmetry plane BCC on +X direction surface

We will fix the bottom surface of the Bottom plate, this can be done by selecting Velocity option from BCC tree and **Z** Direction radio button with 0 mm/sec velocity. Click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) to finish the assignment. Assigned Velocity BCC is displayed as shown in Fig. AWL1.12.

![]({{ '/assets/images/applications/55_2_arc_welding/image0012.jpg' | relative_url }})

Assigned Velocity BCC on Bottom surface of the Bottom Plate

By default, Heat Exchange with environment BCC will be assigned to entire outer surface except symmetry plane as during meshing as shown in Fig. AWL1.13. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0013.jpg' | relative_url }})

Assigned Heat exchange with Environment BCC on Bottom surface of the Bottom Plate

#### Initialize Volume fraction for Bottom Plate

Click on ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) to access the element dialog to initialize the volume fraction. On the item list window click ‘Microstructure’ ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ‘Phase’ and then choose ‘**Pearlite** ’ and click on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) to ‘Initialize Element Data’. Enter 1 in value field with default settings, then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) and close the window. Click on ![]({{ '/assets/icons/pre_icons/mo_plot_icon.jpg' | relative_url }}) and observe the assigned Pearlite phase for all elements (See Fig. AWL1.14.). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Element dialog. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0014.jpg' | relative_url }})

Element Dialog – Initialization of Phase Volume for Bottom Plate

### Top Die

In Top die page, change the object name to "**Top Plate** ", select object type as "**Elasto-Plastic** " and select "**Mixed (Tet mesh)** " option from drop - down menu. Keep the object temperature as **20°C** as shown in Fig. AWL1.15.

![]({{ '/assets/images/applications/55_2_arc_welding/image0015.jpg' | relative_url }})

Top Plate General page

#### Top Plate Geometry

In Geometry page, using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button import **Top_Plate.stl** file from **/3D/ LABS/Arc_Welding** folder, after importing geometry, use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) action label to check the Geometry and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close Check geometry popup. Click on **Symmetry planes** , add button at planar symmetry plane on +X direction surface of Top Plate, similarly add **-X** direction surface and **-Y** direction surface as shown in Fig. AWL1.16. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Symmetry planes and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0016.jpg' | relative_url }})

Top Plate Geometry page

#### Top Plate Mesh

Define the **Number of Elements** as **35000** and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), click **Yes** in "Default Boundary Conditions" popup to assign default boundary condition for Top plate. Generated mesh for Top Plate looks like as shown in Fig. AWL1.17. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0017.jpg' | relative_url }})

Top Plate Mesh page

#### Top Plate Material

Assign "**S45C-JAPAN** " material from list for Top Plate. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary Condition page.

#### Top Plate Boundary condition

Observe the default **Symmetry BCC** data assigned to Top plate while generating mesh, Symmetry BCC will be assigned to +X direction, -X direction and -Y direction surfaces as we defined in Geometry - Planar symmetry page (See Fig. AWL1.18.). 

![]({{ '/assets/images/applications/55_2_arc_welding/image0018.jpg' | relative_url }})

Assigned Symmetry plane BCC on +X direction surface

By default, Heat Exchange with environment BCC will be assigned to entire outer surface except symmetry planes during remesh as shown in Fig. AWL1.19. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0019.jpg' | relative_url }})

Assigned Heat Exchange with environment BCC on the Top Plate

#### Initialize Volume fraction for Top Plate

Click on ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) to access the element dialog to initialize the volume fraction. On the item list window click ‘Microstructure’ ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ‘Phase’ and then choose ‘**Pearlite** ’ and click on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) to ‘Initialize Element Data’. **Type 1** in value field with default settings, then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), then close the window. Click on ![]({{ '/assets/icons/pre_icons/mo_plot_icon.jpg' | relative_url }}) and observe the assigned Pearlite phase for all elements (See Fig. AWL1.20.). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Element dialog. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0020.jpg' | relative_url }})

Element Dialog – Initialization of Phase Volume for Top Plate

### Bottom Die

In Bottom Die page, change the object name to "**Bead 1** ", select object type as "**Elasto-Plastic** " and select "**Mixed (Tet mesh)** " option from drop - down menu. Keep the object temperature as **20°C** as shown in Fig. AWL1.21.

![]({{ '/assets/images/applications/55_2_arc_welding/image0021.jpg' | relative_url }})

Bead 1 General page

#### Bead 1 Geometry

In Geometry page, using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button import **Bead1.stll** file from **/3D/ LABS/Arc_Welding** folder. After importing geometry use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) action label to check the Geometry and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close Check geometry popup. Click on **Symmetry planes** , add planar symmetry plane on **+X** direction surface of Bead 1, similarly add **-X** Direction surface as shown in Fig. AWL1.22. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Symmetry planes and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0022.jpg' | relative_url }})

Bead 1 Geometry page

#### Bead 1 Mesh

Switch to Expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) icon, define the Number of Element as **40000** and Size ratio as 1 then click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) and click **Yes** in "Default Boundary Conditions" popup to assign default boundary condition for Bead 1. Generated mesh for Bead 1 is displayed as shown in Fig. AWL1.23. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0023.jpg' | relative_url }})

Bead 1 Mesh page

#### Bead 1 Material

Assign "**S45C-JAPAN** " material from list for Bead 1. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary Condition page.

#### Bead 1 Boundary condition

Observe the default **Symmetry BCC** data assigned to Bead 1 while generating mesh, Symmetry BCC will be assigned to +X direction and -X direction surfaces as we defined in Geometry - Planar symmetry page (See Fig. AWL1.24.). 

![]({{ '/assets/images/applications/55_2_arc_welding/image0024.jpg' | relative_url }})

Assigned Symmetry plane BCC on +X direction surface

By default, Heat Exchange with environment BCC will be assigned to entire outer surface except symmetry planes as shown in Fig. AWL1.25. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0025.jpg' | relative_url }})

Assigned Heat Exchange with environment BCC for Bead 1

#### Initialize Volume fraction and Additive manufacturing for Bead 1

Click on ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) to access the element dialog to initialize the volume fraction. On the item list window click ‘**Microstructure** ’ ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ‘Phase’. Choose ‘**Pearlite** ’ and then click on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) to ‘Initialize Element Data’. Type 1 in value field with default settings, then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) and close the pop-up window. Click on ![]({{ '/assets/icons/pre_icons/mo_plot_icon.jpg' | relative_url }}) and observe the assigned Pearlite phase for all elements (See Fig. AWL1.26.). 

![]({{ '/assets/images/applications/55_2_arc_welding/image0026.jpg' | relative_url }})

Element Dialog – Initialization of Phase Volume for Bead 1

On the list click "**Additive Manufacturing** ", click on Element layer ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) to ‘Initialize Layer ID’. Enter 1 in value field with default settings, then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) and close the window. Click on ![]({{ '/assets/icons/pre_icons/mo_plot_icon.jpg' | relative_url }}) and observe the assigned **Layer ID** for all elements (See Fig. AWL1.27.). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Element dialog. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0027.jpg' | relative_url }})

Element Dialog – Initialization of layer ID

## Contact 

In **Contact** page, add three relations by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button, select first relation and then select Bottom plate as Master and Top plate as Slave. Click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}), under **Thermal** tab define **Heat Transfer Coefficient** as **1000** and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Now select second relation and select Bead 1 as Master and Bottom plate as Slave, click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}), under **Thermal** tab define **Heat Transfer Coefficient** as **1000** and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Now select last relation and select Bead 1 as Master and Top plate as Slave, click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}), under **Thermal** tab define **Heat Transfer Coefficient** as **1000** and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Turn on Sticking condition check box in all relations, click the ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) to determine an intelligent contact tolerance. Click ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact and click " **Yes** " in Sticking condition pop-up, generated contact is as shown in the Fig. AWL1.28. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0028.jpg' | relative_url }})

Contact page

## Stopping Controls

Switch to Expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) button, define the **Process Duration** as **100** sec as shown in Fig. AWL1.29. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0029.jpg' | relative_url }})

Stopping Controls (Expert mode)

## Step Controls

Switch to Guided mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}), define the **Number of Step** s as **10000** , **Step increment** as **10** and **Time****per step** as **0.1** sec as shown in Fig. AWL1.30.

![]({{ '/assets/images/applications/55_2_arc_welding/image0030.jpg' | relative_url }})

Step - Guided mode

Switch to Expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) button, under ![]({{ '/assets/icons/pre_icons/mo_solver_settings.jpg' | relative_url }})**Solver settings** click on **Deformation** tab, select **MUMPS** solver and **Iteration****method** as **Newton****-****Raphson** as shown in Fig. AWL1.31.

![]({{ '/assets/images/applications/55_2_arc_welding/image0031.jpg' | relative_url }})

Solver Settings -Deformation tab

Under **Solver settings** \- **Thermal** tab select **MUMPS** solver as shown in Fig. AWL1.32.

![]({{ '/assets/images/applications/55_2_arc_welding/image0032.jpg' | relative_url }})

Solver Settings -Thermal tab

  
Select **Advanced****Process Condition**![]({{ '/assets/icons/pre_icons/mo_advanced_process_conditions.jpg' | relative_url }}) , under **Additive Manufacturing** tab, enter the following data:

Select **Process type** as "**Arc Welding** ", 

**Activation size** as **9** (for more information refer Activation size in Additive Manufacturing Lab),

**Initial density** as **1** , 

**Initial temperature** as **20** ,

Define **Number of layers** as**1** , **Current** **layer** as **1** , **Start****layer** as **1** and **End****layer** as **1** as shown in the Fig. AWL1.33.

![]({{ '/assets/images/applications/55_2_arc_welding/image0033.jpg' | relative_url }})

Process Condition - Additive Manufacturing 

  
Under **Heat Source** tab, click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add Heat source. Select **Double Ellipsoid** and define value of **Qf** as 1000, **Qr** as 1000, **Cf** as 0.04, **Cr** as 0.01, **Cy** as 0.04 and **Cz** as 0.01 as shown in Fig. AWL1.34.

![]({{ '/assets/images/applications/55_2_arc_welding/image0034.jpg' | relative_url }})

Process Condition - Heat Source page

In this lab we will define the Path and Orientation data using Auto Extract option. Click on ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) to Extract path and Orientation from geometry automatically, select weld bead as " Bead 1" under object list as shown in Fig. AWL1.35.

![]({{ '/assets/images/applications/55_2_arc_welding/image0035.jpg' | relative_url }})

Weld bead object selection

  
Since the bead geometry is Extruded type select **Geometry type** as Extruded radio button, then click ![]({{ '/assets/icons/pre_icons/mo_free_surface_button.jpg' | relative_url }}) button and select **inclined surface** as Free surface as shown in Fig. AWL1.36. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close the Free surface page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0036.jpg' | relative_url }})

Selecting Free surface 

  
Click on ![]({{ '/assets/icons/pre_icons/mo_starting_surface_button.jpg' | relative_url }}) button and select Starting surface as **+X direction** surface of Bead 1 as shown in Fig. AWL1.37. and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/applications/55_2_arc_welding/image0037.jpg' | relative_url }})

Selecting Extruded Starting surface

  
Similarly, click on ![]({{ '/assets/icons/pre_icons/mo_ending_surface_button.jpg' | relative_url }}) button and select **Ending****surface** as **-X direction** surface of **Bead 1** and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close. Now to extract Path and Orientation from geometry click on ![]({{ '/assets/icons/pre_icons/mo_extract_button.jpg' | relative_url }}) button with default settings as shown in Fig. AWL1.38. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close the Auto Extract page. User can define “Initial time”, “Speed” and “Interval between extracted points” which will be used to define the function data.

![]({{ '/assets/images/applications/55_2_arc_welding/image0038.jpg' | relative_url }})

Extracting path and orientation using Extract button

  
After extracting the path and orientation, click on ![]({{ '/assets/icons/pre_icons/mo_path..._button.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_orientation..._button.jpg' | relative_url }}) button and observe the extracted path and orientation data. (See Fig. AWL1.39. and Fig. AWL1.40.)

![]({{ '/assets/images/applications/55_2_arc_welding/image0039.jpg' | relative_url }})

Extracted Path data

![]({{ '/assets/images/applications/55_2_arc_welding/image0040.jpg' | relative_url }})

Extracted Orientation data

  
Click on ![]({{ '/assets/icons/pre_icons/mo_define_magnitude..._button.jpg' | relative_url }}) button, select Heat source as **On/off** , add two rows by clicking on ![]({{ '/assets/icons/pre_icons/mo_insert_row_icon.jpg' | relative_url }}) button and define the Magnitude. In this lab we are defining constant magnitude as shown in Fig. AWL1.41. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Magnitude window

![]({{ '/assets/images/applications/55_2_arc_welding/image0041.jpg' | relative_url }})

Magnitude window

  
We can preview the movement by clicking on ![]({{ '/assets/icons/pre_icons/mo_preview_movement_button.jpg' | relative_url }}) button and play the animation. We can vary the movement preview speed and Arrow size using respective sliding bar as shown in Fig. AWL1.42. As the simulation preview progresses user can observe the arrow following the welding path. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Magnitude window and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page.

![]({{ '/assets/images/applications/55_2_arc_welding/image0042.jpg' | relative_url }})

Movement Preview window

## Generate DB

In **Generate DB** page, click ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) to see if anything was missed in the setup and then click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. Observe the message in Message tab informing database generation status.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. AWL1.43. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_2_arc_welding/image0046.jpg' | relative_url }})

Run Simulation Window

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. 

## Post Processing

When the simulation is completed, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.

Play through the steps using animation option and observe the Bead 1 formation (See Fig. AWL1.44. and Fig. AWL1.45.).

![]({{ '/assets/images/applications/55_2_arc_welding/image0043.jpg' | relative_url }})

Bead 1 formation at the end of step 50 

![]({{ '/assets/images/applications/55_2_arc_welding/image0044.jpg' | relative_url }})

Bead 1 formation at last step

  
Plot Temperature state variable and observe the temperature distribution (See Fig. AWL1.46.).

![]({{ '/assets/images/applications/55_2_arc_welding/image0045.jpg' | relative_url }})

Temperature Distribution at last step
