---
lang: sk
title: "3D Machining Distortion Lab1"
---

# 3D Machining Distortion Lab1

1.1. Creating a New problem

1.2. Adding operation

1.3. Object window

1.4. Workpiece

1.5. Setting up the fixtures

1.6. Defining the initial machining pass

1.7. Controls window:

1.8. Scheduled Positioning

1.9. Contact

1.10. Simulation Preview

1.11. Simulation control

1.12. DB generation

1.13. Starting the Simulation

1.14. Post processing the results

## Creating a New problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear, as shown in [Fig. 3DMDL1.1.](../heat_treatment_labs/3d_heat_treatment_wizard_lab.htm#Fig_3DHTWL1_1_DEFORM_GUI_main_window)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI main window

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 3DMDL1.2. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as "******3D_Machining_Distortion******" and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problem type selection window

Integrated Manufacturing Process will open, At this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**3D_Machining_Distortion** ’ as the project name (see Fig. 3DMDL1.3.). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0003.jpg' | relative_url }})

New project window

## Adding operation

Multiple Operation wizard will open. Add 3D **Machining Distortion** operation from the Explorer Operations list. Operation can be added by clicking on 3D Machining Distortion operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor (see Fig. 3DMDL1.4.).

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0004.jpg' | relative_url }})

Adding 3D Machining Distortion

## Object window

In the object window, along with workpiece, 4 fixtures and 1 pass is required for this lab. So, define the**Number of fixtures** as **4** and Number of passes **as** 1 and click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button to add Fixtures and Pass objects (see Fig. 3DMDL1.5.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0005.jpg' | relative_url }})

Object window

## Workpiece

In workpiece page, load the object information by selecting ![]({{ '/assets/icons/pre_icons/mo_import_object.._button.jpg' | relative_url }}) option. User can browse for the database file. Load the file ‘**CoolingModel.DB** ’ from Deform Installation path \3d\**LABS** \**Machining_Distortion** and select the appropriate step number (last step for this lab) and object (this model has only one object) (see Fig. 3DMDL1.6.). For this lab two files are provided. One keyword file and one database file for a typical cooling simulation. The keyword file provided here was run to generate the database file.

Once the object is loaded user can change the name of the object and turn on ‘init displacement’ so that the distortion due to the material removal alone can be properly recorded. click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0006.jpg' | relative_url }})

Workpiece Importing window

In boundary conditions window, observe the Fixed Velocity BCC in all directions and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

In Initialize window, few state variables that are commonly used such as Temperature, strain, stress, damage, velocity, Displacement, etc.., are made available for initialization. User can initialize these State variable value by defining the value in input field and clicking on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) button. In this lab we will not be initializing any data. So, use default values from simulated database and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0007.jpg' | relative_url }})

Initialize Window

## Setting up the fixtures

In Object window, Number of fixtures added as four, this lab uses all four fixtures. Two near the axis and two near the far end. They can be loaded (or defined) in any sequence. Once loaded, user can check the geometry and edit the same if needed.

### Fixture 1

In fixture 1 window, define the fixture name (if need different from the default one), and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to load/define the fixture geometry. (see Fig. 3DMDL1.8.) Fixture geometry can be defined using the primitives, (which can also be edited interactively if needed) or load an existing geometry file. For this lab,( see Fig. 3DMDL1.9.) we load the fixture 1 as bottom left one **(lb_fixture.GEO**) from Installation path \3d\LABS\Machining_Distortion.

### Fixture 2

Similarly as Fixture 1, for Fixture 2 load upper left one (**lu_fixture.GEO**) from Installation path \3d\LABS\Machining_Distortion path.

### Fixture 3

Similarly as Fixture 1, for Fixture 3 load bottom one (**rb_fixture.GEO**) from Installation path \3d\LABS\Machining_Distortion path.

### Fixture 4

Similarly as Fixture 1, for Fixture 4 load right top one (**ru_fixture.GEO**) from Installation path \3d\LABS\Machining_Distortion path.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0008.jpg' | relative_url }})

Fixture 1 window

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0009.jpg' | relative_url }})

Geometry window

## Defining the initial machining pass

From the model point of view, the machining pass information is also a geometry data. when pass geometry overlapping with the billet, it decides the location and the extent of the material set for removal. Hence this is also a geometry data that can be defined/loaded in the same manner as the fixtures done in the last step. Using the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Import Geometry) ( Fig. 3DMDL1.11.) option load the file ‘**pass1.GEO** ’ from Installation path \3d\LABS\Machining_Distortion. User can check this geometry.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0010.jpg' | relative_url }})

Pass window

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0011.jpg' | relative_url }})

Geometry window

## Controls window

In this operation, we position the fixtures with respect to the billet. Select ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) option to enter the ‘Object Positioning’ dialog. Here select the ‘Interference’ mode of positioning. From the object list select ‘Billet’ as the reference object, and sequentially select fixtures 1 to 4 for positioning. (Fig. 3DMDL1.13.) For each pair correct approach direction should be selected for positioning. Approach direction for bottom fixtures should be ‘Z’ and top fixtures ‘-Z’. User can use the default interference value, and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) to carry out the positioning for each fixture.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0012.jpg' | relative_url }})

Controls window

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0013.jpg' | relative_url }})

Object Positioning window

## Scheduled Positioning

Schedule positioning allows the user to define the positioning of objects in MO setup for successive operations for which DB is not generated. So that, the objects are positioned before generation of DB while running simulation in batch mode. For this lab we are not using the scheduled positioning.

## Contact

In this stage, we define ‘4’ pairs of master-slave objects. In the ‘Inter Object’ dialog (Fig. 3DMDL1.14.) , select user type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button four times to define four pairs of object relations. For each pair, sequentially select one fixture as master and billet as slave. or

User can directly click on the ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) to add the all default relations and use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance

For this lab, we do not define any friction conditions. (user can enter ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Edit) option to define friction conditions if needed) Click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate the contact conditions. At this stage, contact nodes will be highlighted in the display area. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0014.jpg' | relative_url }})

Contact window

## Simulation Preview

Simulation Preview provides an overview of the operation to be executed based on the process definition and pass. We have two Boolean methods for 3D Object,

  * **Geometry based (new method)** : Using Geometry based option if we do Boolean operation, it will execute Boolean operation and then followed by local remeshing of the new surface generated after boolean operation as per the defined remeshing settings. This will generate smooth mesh as shown in Fig. 3DMDL1.15.

  * **Solid mesh based (old method)** : Using Solid mesh method if we do Boolean operation, it will perform boolean operation of the object and then generate new mesh for the new surface, new surface may not be smooth hence mesh generated also will not look smooth as shown in Fig. 3DMDL1.15.

In this lab, we will use Geometry based method for boolean with default local remesh settings so, select **Geometry based (new method)** radio button and observe the simulation preview. In Simulation preview window, by clicking the ![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) button animation would be played and shows the object that was removed after the pass (see Fig. 3DMDL1.16.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0015.jpg' | relative_url }})

3D Boolean methods output

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0016.jpg' | relative_url }})

Simulation preview window

## Simulation control

Last step of the model data generation is to set up the simulation controls where we define starting step as ‘-1’, number of steps as ‘2’ saving every step, and ‘1 sec’ time per step as shown in Fig. 3DMDL1.17. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to enter the database generation page.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0017.jpg' | relative_url }})

Simulation control window

## DB generation

In Generate DB page, Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

## Starting the Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label under the simulation tab, Run Options dialog will open. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

When the simulation is finished we can observe that the following message is added to the end of the Message file:

******Message*******

Simulation is completed and stopped at the user specified time step.

## Post processing the results

After the simulation is complete, user can enter ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) to see the model results. Typical sequence is to first select the step number, and then the state variables to be displayed. Some important state variables can be selected directly from post tools and the rest can be accessed through ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) table (by selecting). Fig. 3DMDL1.18. indicates the effective stress distribution after the machining pass and Fig. 3DMDL1.19. indicates maximum principal stress distribution after machining pass.

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0018.jpg' | relative_url }})

Effective stress distribution and distorted billet after the machining pass

![]({{ '/assets/images/labs/machining_distortion_labs/3d_machining_distortion_lab1/image0019.jpg' | relative_url }})

Max. Principal stress distribution and distorted billet after the machining pass
