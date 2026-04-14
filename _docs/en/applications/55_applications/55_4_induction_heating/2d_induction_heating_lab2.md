---
lang: en
title: "2D Induction Heating Lab2"
---

# 2D Induction Heating Lab2

**Induction Heating Surface of 30mm Radius Bar BEM Scanning :**

This Induction Heating lab will show how to set up an induction heating of a bar with a top (preheat) and bottom (heat) copper coils. The lab will allow the user to add the necessary material properties to conduct the electro-magnetic portion of the calculations, with spray quenching and phase transformation.

2.1. Creating a New Problem

2.2. Adding Operation

2.3. Selecting Geometry Type

2.4. Simulation Controls

2.5. Material list

2.6. Adding Objects

2.7. Workpiece

2.8. Top Coil

2.9. Bottom Coil

2.10. Workpiece Boundary Condition

2.11. Generate DB

2.12. Running Simulation

2.13. Post Processing

## Creating a New Problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear, as shown in Fig. 2DINDL2.1.

![]({{ '/assets/images/applications/55_2_arc_welding/image0001.jpg' | relative_url }})

DEFORM GUI Main window

Create a new problem either by selecting **File**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in [Fig. 2DINDL2.2.]() Select " **Integrated Manufacturing Process** " radio button and unit system as "**SI** " radio button in unit field. Define Problem Name as " **IH_Lab_2DFEM2** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

New Problem page

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "**IH_Lab_2DFEM1a** " as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding Operation

Add **2D****Forming** operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to 2D Forming Operation or user can also add by drag and drop into the Operation Editor. When we add the 2D Forming operation, process settings window will open by default (see Fig. 2DINDL2.3.).

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0003.jpg' | relative_url }})

Adding 2D Forming operation

## Selecting Geometry Type

In this lab we will be using Axisymmetric geometries, so select **2D Axisymmetric** radio button from geometry type page as shown in Fig. 2DINDL2.4., then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0004.jpg' | relative_url }})

Geometry type selection

## Simulation Controls

Switch to **Expert****mode** by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) icon, Enter Operation name as "**Initial Heat Up** " and be sure that **Deformation** , **Heat****transfer** , **Transformation** and **Heating** are checked with the **Enthalpy****type** for **Solidification** and **Induction****(BEM)** method as Heating from drop boxes as shown in Fig. 2DINDL2.5.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0005.jpg' | relative_url }})

Simulation controls - Main page

Click on **Simulation****Steps![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }})** , enter the **Number** **of****simulation****steps** as **1500** and keep **Step****increment****to****save** as **10** as shown in Fig. 2DINDL2.6.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0006.jpg' | relative_url }})

Simulation controls -Simulation steps page

Click on **Step increment** ![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}), under the **General** tab, select the Solution step definition as **Temperature** and define **Initial****time****step** as **0.1** sec, **Max****temperature****change** as **5** °C, **Min****time****step** as **0.0001** sec and **Max** **Time****Step** as **0.25** sec as shown in Fig. 2DINDL2.7.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0007.jpg' | relative_url }})

Simulation controls - Step increment page

Click on **Stopping****criteria![]({{ '/assets/icons/pre_icons/mo_stopping_criteria.jpg' | relative_url }}) **and enter **Process****duration** as **25** sec as shown in Fig. 2DINDL2.8.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0008.jpg' | relative_url }})

Simulation controls - Stopping criteria page

Click on **Advanced options** ![]({{ '/assets/icons/pre_icons/mo_advanced_options.jpg' | relative_url }}), under **Frequency** tab for **Maxwell****equation** solving select **User- defined** using drop-down list and define **every****5** step(s) as shown in Fig. 2DINDL2.9., this is done so that electro-magnetic calculations are done for every 5 steps instead of each step. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material Page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0009.jpg' | relative_url }})

Simulation controls - Advanced option Frequency page

## Material list

In Material list Window, click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) to Load material data from DB file.

  * Choose the Database Files(*.db *.DB) option.

  * Navigate to the area where the FEM Induction ran ([Induction Heating Lab1](/docs/en/applications/55_applications/55_4_induction_heating/2d_induction_heating_lab1/)) and choose the IH_Lab_2DFEM1a.DB database and select the first step.

  * Load the **S45C-JAPAN** , the other phases will load automatically and then click .

  * Again, load the **Coil** material from **IH_Lab_2DFEM1a.DB** database.

  * Since the BEM does not require the air to be meshed, this material data is sufficient for this lab. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Objects page.

## Adding Objects

For this lab we need 3 objects, by default 3 objects will be added in list. If not added by default, then add 3 objects to Objects list using ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0010.jpg' | relative_url }})

Objects page

## Workpiece

Click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) and import the Workpiece object from **IH_Lab_2DFEM1a.DB** database (**Induction Heating Lab1**) at **-1** step. Change the object type to **Elasto-plastic** and keep object temperature as **20****°C**. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Boundary condition page (see Fig. 2DINDL2.11.).

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0011.jpg' | relative_url }})

Workpiece Object page

### Workpiece Boundary Condition

In **Boundary****condition** page, click on **Velocity** then choose the ![]({{ '/assets/icons/pre_icons/mo_bcc_one_by_one_icon.jpg' | relative_url }}) (one by one) selection method in picking tool bar and then choose the lower left node, from BCC controls select direction as **Y** with velocity 0 to fix the node in **Y** direction and click the ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}), we can notice that **X** direction on inside edge along the axis is already fixed as it is inside the object and geometry type is Axi-symmetric . Added **Velocity BCC (Vy=0)** is as shown in Fig. 2DINDL2.12.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0012.jpg' | relative_url }})

Workpiece Velocity (Vy=0) Boundary Condition page

Click on the **Induction BEM – Heating Surface** , choose ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) (By edge) selection method instead of ![]({{ '/assets/icons/pre_icons/mo_bcc_one_by_one_icon.jpg' | relative_url }}) (one by one) and then select the three outside surfaces and click the ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). Added Induction BEM - Heating surface is as shown in Fig. 2DINDL2.13. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0013.jpg' | relative_url }})

Workpiece Induction BEM - Heating surface Boundary Condition page

## Top Coil

In Top die page, click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) and import the **Lower****Middle****Coil** object from **IH_Lab_2DFEM1a.DB** database ([Induction Heating Lab1](/docs/en/applications/55_applications/55_4_induction_heating/2d_induction_heating_lab1/)) at **-1** step. Change the object name to **Top Coil** and keep object type as **Rigid** and object temperature as **20** °C (see Fig. 2DINDL2.14.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Boundary Condition page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0014.jpg' | relative_url }})

Top Coil General page

### Top Coil Boundary Condition

Click on the Induction BEM – Heating Surface, click on ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) so that all surfaces are selected and click the ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). Added Induction BEM - Heating surface is as shown in Fig. 2DINDL2.15. Also make sure that entire object surface is selected for heat exchange with environment. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement Controls page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0015.jpg' | relative_url }})

Top Coil Induction BEM - Heating surface Boundary Condition page

### Top Coil Movement

In this lab the Top coil will hold for 2 seconds and then move up at a rate of 10mm/sec. Select **Movement****direction** as **+Y** , define **Speed** as **Function****of****Time** and add the following data, click on ![]({{ '/assets/icons/pre_icons/mo_apply_button2.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close Function window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Properties page.

**Time** |  **Speed**  
---|---  
0 |  0  
2 |  0  
2.001 |  10  
100 |  10  
  
### Top Coil Properties

Under **Heating** tab, we will be use **Current frequency** type as **Single** , the **current****frequency** should be **6000****Hz** and the **Current****density** should be a constant **18** A/mm2 as shown in Fig. 2DINDL2.16. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom Die page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0016.jpg' | relative_url }})

Top Coil Properties page

## Bottom Coil

In Bottom die page, click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) and import the **Bottom Coil** object from **IH_Lab_2DFEM1a.DB** database ([Induction Heating Lab1](/docs/en/applications/55_applications/55_4_induction_heating/2d_induction_heating_lab1/)) at **-1** step. Keep the object name to **Bottom Coil** , object type as **Rigid** and **object temperature** as **20****°C** (see Fig. 2DINDL2.17.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Boundary Condition page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0017.jpg' | relative_url }})'

Bottom Coil General page

### Bottom Coil Boundary Condition

Click on the I**nduction BEM** – **Heating****Surface** , click on ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) so that all surfaces are selected and click the ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). Added Induction BEM - Heating surface is as shown in Fig. 2DINDL2.18. Also make sure that the entire object surface are selected for heat exchange with environment. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement Controls page 

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0018.jpg' | relative_url }})

Bottom Coil Induction BEM - Heating surface Boundary Condition page

### Bottom Coil Movement

In this lab for the Bottom coil we will define the same Top coil movement. Select Movement direction as **+Y,** define **Speed** as **Function****of****Time** and add the following data, click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close Function window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Properties page.

**Time** |  **Speed**  
---|---  
0 |  0  
2 |  0  
2.001 |  10  
100 |  10  
  
### Bottom Coil Properties

Under **Heating** tab, we will use **Current Frequency** type as **Single** , the current frequency should be **6000****Hz** and change the **Current****density** to **constant****21** **A/mm 2** as shown in Fig. 2DINDL2.19. Now go back to Workpiece BCC page by clicking on **Workpiece** "**Boundary Condition** " list to define spray quench.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0019.jpg' | relative_url }})

Bottom Coil Properties page

## Workpiece Boundary Condition

Here a spray quench will be added, the spray quench will be a 100mm high spray ring that will follow the coil as it heats and moves up the bar. The conditions will be that of water quench but if data can be found for more appropriate data then that data should replace those we are now using or adjusted accordingly. For now, add the convection window (spray bar).

Click **Heat Exchange with Environment** , click on **Env. Windows** button and click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add window. Then select **Polygon** type and add any four points in a roughly rectangular shape. Then click the ![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}) pencil icon and change the points co-ordinates to these four as shown in below Fig. 2DINDL2.20., then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

20 |  -26  
---|---  
20 |  -126  
35 |  -126  
35 | -26  
  
![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0020.jpg' | relative_url }})

Rectangle window Edit page

Then select **Follow****object** as "**Bottom Coil** ", define **Convection Coefficient** as **Function****of****Temperature** with the below table data in Function window and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button2.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close Function window. Then enter the Environment temperature as **20** °C as shown in Fig. 2DINDL2.22. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Env. Windows page. Click on **Generate DB** in Operation tree to generate DB.

**Temperature** |  **Convection Coefficient**  
---|---  
50 |  0.5  
100 |  1.5  
200 |  5  
300 |  8  
400 |  10  
500 |  7  
600 |  4  
700 |  2  
800 |  0.8  
900 |  0.7  
1000 |  0.6  
1200 |  0.6  
  
![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0021.jpg' | relative_url }})

Convection Coefficient Function window

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0022.jpg' | relative_url }})

Env. Windows page

## Generate DB

In 'Generate DB' page, click ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) and correct any errors. Do not worry that certain material properties are not defined for Material 1 as they should be defined for the individual phases of the mixture. Also do not worry that emissivity is not defined as the convection definition combines the convection with the emissivity. If you have data that you know to be more accurate, then you should use it and define these individually but in this case, this is a second order effect compared to the quench and the numbers as defined will be fine for this lab.

Click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. Observe the message in Message tab informing database generation status.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DINDL2.23. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0023.jpg' | relative_url }})

Run Simulation Window

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. User can view the Induction heating process as the simulation proceeds to the specified Step definition from Simulation graphics.

## Post Processing

When the simulation is completed, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.

In Step Browser click on **All** button, Plot **Temperature****state****variable** , Play the animation by clicking on ![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) and observe the temperature distribution.

At the beginning, the simulation shows the workpiece heating up and then a reasonably steady state temperature following the coil as it goes up until you get to the top of the workpiece. You will see that the temperature distribution on the top gets and stays hot. This will require the heat to be turned off at the top at appropriate points. Also, the temperature is too low. Few iterations may be required to change the temperature profile to give a reasonable heating depth.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab2/image0024.jpg' | relative_url }})

Temperature distribution at the last step

Related Topics:

[2D Induction Heating Lab 1](/docs/en/applications/55_applications/55_4_induction_heating/2d_induction_heating_lab1/)
