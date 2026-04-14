---
lang: en
title: "Gear Blank EN Lab 10"
---

# Lab 10 Gear Blank Symmetry Operation

Open DEFORM and create a new project named **Gear_sym** to setup the isothermal symmetry workpiece forming of gear blank.

### Add operation and objects

Add the **3D forming operation** in operation editor from **explorer**.

In the Simulation controls branch in operation tree uncheck the Heat transfer mode from simulation control main tab as this is an isothermal simulation. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

Load the **AISI-8620[1550-2200F(850-1200C)]** material from the **Steel_at_Extended_Temperatures** library.

Click **Objects** branch in operation tree to add objects and continue setup. Add three objects (if they don't already exist) and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define workpiece.

### Define Symmetry workpiece

Set Temperature to **2250** ° F and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to create Geometry.

**Create workpiece Geometry**  
Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) to create a workpiece from a primitive **cylinder** with **5** ” diameter, **0.1** ” corner **radii** , **8.15** “ tall and **30** ° revolve angle with **30** sections. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close menu.

As the dies upward direction is Y Workpiece must be rotated to align with the dies upward direction. So click on **Positioning** branch in operation tree and rotate workpiece 90° about the –X axis and center (0,0,0) using ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) option, as was the case in [Lab5](/docs/en/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab5/).

Go back to Workpiece Geometry window by clicking **Geometry** branch in operation tree to define symmetry planes.

Click on ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}) button. Select Planar symmetry branch, using left side tool bar (below explorer) pick the symmetrical planes from graphics window as shown in Fig. L10.1., one at a time.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab10_image0001.jpg' | relative_url }})

Symmetry surfaces

Once you have selected a plane, click on the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add) button to add planar symmetry planes.

Note:

Symmetry will assist the mesh generator in determining edges to protect during meshing.

Added symmetry surfaces appears under Planar symmetry branch as shown in Fig. L10.2. Confirm the symmetry planes by selecting the added branches under planar symmetry and observing the highlighted plane in graphics window.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab10_image0002.jpg' | relative_url }})

Added symmetry planes

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and generate mesh with **10000** elements. Deform will ask if you would like to use the geometries symmetric definition in the mesh BCC. Click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). (See Fig. L10.3.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab10_image0003.jpg' | relative_url }})

Generating Mesh BCC from Geometry BCC popup

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and select the **AISI-8620** material in material list.

Go to the **Workpiece****Boundary****condition** window in operation tree and confirm the 2 symmetry planes. (See Fig. L10.4.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab10_image0004.jpg' | relative_url }})

Generated mesh symmetry BCC from geometry symmetry BCC

Click on **Top****die** in operation tree to import dies.

### Importing dies

Click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) to import the top die object from the first step of the forge operation (op 2) of “**Gear_t.DB**.”

Click on **Bottom****die** in operation tree.

Similarly import object for bottom die at first step of operation 2 (from **Gear_t****.DB**).

### Generate inter-object relations

In Contact page, add three relations using ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button. For first relation, select Workpiece as Master and Slave to model self-contact, for second relation select Top Die as Master and Workpiece as Slave and for last relation select Bottom Die as Master and Workpiece as Slave. Click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) and define Shear friction as 0.3, to assign same friction to all relations click on ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), then click on ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) button to calculate tolerance value and click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define **stopping** and **simulation** controls.

### Define stopping and Simulation controls

Set the **Stopping criteria** to create a flash thickness of **0.20** inches.

As the dies distance between objects stopping controls reference points are also imported with object in stopping controls window check the Distance between objects check box and select the object 1 as Top die and object 2 as Bottom die. This will read the top and bottom die imported reference points and display the same in graphics window. Define**0.2** inches in data field and Y as distance direction.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define simulation controls.

Setup the Step controls in Simulation Controls. Use **300** steps for this operation. Measure the distance between the tools to determine an appropriate die displacement value. Divide the total distance (8.0) by the number of steps (300) to get a die displacement of (**0.02667**). Save every **10** steps.

### Generate database and run the simulation

Check and Generate database and click on the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode button (above the operation tree) to start the simulation.

Run simulation, after completion of simulation click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) mode button to review results.

### Review Results

In MO post processor, use the mirroring tool ![]({{ '/assets/icons/post_icons/mo_3d_mirroring_icon.jpg' | relative_url }}) from post tools to create a full 360 degree workpiece. In the mirroring mode, you can click on one of the workpiece symmetry planes to mirror it. It will take 11 clicks to get the full workpiece. You can switch to the delete mode and click on the mirrored objects to delete them from the display. (See Fig. L10.5.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab10_image0005.jpg' | relative_url }})

Mirrored symmetry object with pointer mirroring on symmetry plane
