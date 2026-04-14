---
lang: en
title: "2D Nitriding Lab"
---

# 2D Nitriding Labs

Gas nitriding is a surface hardening process, where nitrogen is added to the surface of steel parts using dissociated ammonia as the source. Gas nitriding develops a very hard case in a component at relatively low temperature, without the need for quenching.

This lab will demonstrate how to use MO template to prepare a Nitriding simulation. The thickness of compound layers formed on the surface of pure iron during the nitriding process was analytically calculated. Two separate equations were applied for predicting the thickness of the binary compound layers; epsilon (![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/epsilon.jpg' | relative_url }})) and gamma prime (![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/ghamma prime.jpg' | relative_url }})), in terms of the nitriding process parameters.

1.1. Creating a New Problem 

1.2. Adding Operation

1.3. Selecting Geometry Type

1.4. Simulation Controls

1.5. Adding Material to the Project

1.6. Define workpiece

1.7. Name the Object

1.7.1. Create Geometry

1.7.2. Assign Material for Workpiece

1.7.3. Mesh the Workpiece

1.8. Initialize Volume Fraction

1.9. Boundary Conditions

1.10. Stopping Controls

1.11. Step Controls

1.12. Generate Database

1.13. Running Simulation

1.14. Post Processing

## Creating a New Problem 

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear as shown in Fig. 2DNL1.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI Main window

Create a new problem either by selecting **File**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DNL1.2. Select " **Integrated Manufacturing Process** " radio button and unit system as "**SI** " radio button in unit field. Define Problem Name as " **2D_Nitrding_Lab1** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image014.jpg' | relative_url }})

New Problem page

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "**2D_Nitrding_Lab1** " as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding Operation

Add 2D Forming operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to 2D Forming or can also be added by drag and drop into the Operation editor (See Fig. 2DNL1.3.). When we add the 2D Forming operation, process settings Window will open by default.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0003.jpg' | relative_url }})

Adding 2D Forming operation

Click on the operation item the name tag, change it from ‘Forming’ to ‘**Nitriding** ’.

## Selecting Geometry Type

Turn on ‘**2D Plane strain** ’ radio button in geometry type page (See Fig. 2DNL1.4.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation controls.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0004.jpg' | relative_url }})

Geometry type selection

## Simulation Controls

In this lab, we will be demonstrating how to setup Nitriding process which requires some advanced options here, Switch to ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) mode in ‘Simulation controls’ window make sure ‘**Diffusion** ’ and ‘**Transformation** ’ models under ‘**Heat********transfer** ’ are checked (See Fig. 2DNL1.5.). Then click on ![]({{ '/assets/icons/pre_icons/mo_process_conditions.jpg' | relative_url }}) ‘**Process********conditions** ’ page.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0005.jpg' | relative_url }})

Simulation controls window

Nitriding is a heat treating process that diffuses nitrogen into the surface of a metal to create a case-hardened surface, so in this lab, we will deal only with atom – nitrogen. Click on "Process condition" then ‘**Diffusion** ’ tab, change the atom’s name from ‘carbon’ to ‘**Nitrogen** ’ (See Fig. 2DNL1.6.). Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) in popup.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0006.jpg' | relative_url }})

Modify atom’s name in simulation control window

## Adding Material to the Project

Compound layers (![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/ghamma prime.jpg' | relative_url }})+![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/epsilon.jpg' | relative_url }})) will form on the surface of pure iron (![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/alpha.jpg' | relative_url }})). In this lab, we need to add material ‘Iron’ and its transformation relationships. On ‘Material list’ window click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) to add a new material, rename it to ‘**Iron** ’. Check ‘Multiphase' ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) '**Mixture****material** ’ and then add three phases: **Alpha** , **Gamma** -**prime** , and **Epsilon**(See Fig. 2DNL1.7.).

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0007.jpg' | relative_url }})

Material List Window

In the nitriding of iron, when the nitrogen concentration exceeds the solubility limit, extra nitrogen atoms make stoichiometric compounds with iron atoms. The surface composition of the nitrided iron can be predicted by considering the Fe-N binary phase diagram. In this lab demonstration, the surface structure of the nitrided iron includes ![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/alpha.jpg' | relative_url }})\- Fe (N) diffusion zone (solid solution of nitrogen in ![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/alpha.jpg' | relative_url }})\- Fe), ' and ![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/epsilon.jpg' | relative_url }}) compound layers. The nitrogen contents (solubility limits) at the material interface are listed in Table 1.

Position |  N Content (At. Pct. N)  
---|---  
Surface |  26.34  
![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/epsilon.jpg' | relative_url }})/ ![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/ghamma prime.jpg' | relative_url }}) |  23.59  
![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/ghamma prime.jpg' | relative_url }})/ ![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/epsilon.jpg' | relative_url }}) |  19.923  
![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/ghamma prime.jpg' | relative_url }}) / ![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/alpha.jpg' | relative_url }}) |  19.479  
![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/alpha.jpg' | relative_url }}) / ![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/ghamma prime.jpg' | relative_url }}) |  0.365  
  
Nitrogen content

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), comes to the first defined Iron’s material page. In this Nitriding lab, properties like phase transformation and diffusion coefficient need to be specified.

**Transformation**

To add the phase transformation relationships for Iron, click ![]({{ '/assets/icons/pre_icons/mo_transformation_icon.jpg' | relative_url }}). Then from the mother phase choose ‘**Alpha** ’, and child phase ‘**Gamma** -**prime** ’, click ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) to add the relationship. Under ‘**Kinetics** ’ tab, select ‘**Diffusion****(Solubility curve)** ’ from the pull-down list to specify the model for this transformation (See Fig. 2DNL1.8.). 

The nitrided layer thickness growth of ![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/epsilon.jpg' | relative_url }}), ![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/ghamma prime.jpg' | relative_url }}) follow the parabolic law, select the following model for the ![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/ghamma prime.jpg' | relative_url }}) layer (**Alpha**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Gamma-prime)**

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/eqn1.jpg' | relative_url }})

and type in 0.6 for the correction factor K. At 0.365, the solubility of nitrogen, Alpha starts transforming to Gamma-prime. In the end, the nitrogen content will reach 19.479, and Gamma-prime forms totally. So at Alpha/Gamma-prime interface, define nitrogen content ‘Start’ value of 0.365, and ‘End’ value 19.479 (See Fig. 2DNL1.8.). 

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0008.jpg' | relative_url }})

'Material Editor' - transformation definition 1

Add another transformation by choosing mother phase as Gamma Prime and Child phase as Epsilon. Choose the layer growth model listed below for ![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/epsilon.jpg' | relative_url }}) (**Gamma-prime**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Epsilon**), set K to 0.3. And define the solubility of nitrogen starting from 19.923 to the end 23.59 as Gamma-prime transferring to Epsilon. (See Fig. 2DNL1.9.). 

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/eqn2.jpg' | relative_url }})

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0009.jpg' | relative_url }})

Material Editor - transformation definition 2

**Diffusion Coefficient**

The diffusion coefficients for the defined phases are listed in table. 2, click the Diffusion ![]({{ '/assets/icons/pre_icons/mo_diffusion_icon.jpg' | relative_url }}) icon on the material page to define them for the corresponding materials.

Nitriding Temperature [°C] |  570  
---|---  
Diffusion Coefficient of Nitrogen [10 -8 mm2/s ] |  Epsilon (![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/epsilon.jpg' | relative_url }})) |  3.4  
Gamma -prime (![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/ghamma prime.jpg' | relative_url }})) |  18.1  
Alpha (![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/alpha.jpg' | relative_url }})) |  983.3  
  
Diffusion coefficient of nitrogen

**Thermal Properties**

Thermal properties are not necessary because the object’s temperature is constant and same as the environment temperature in this lab. But they are still required for DB generation. For Iron, type in 30 for thermal conductivity, 5.5 as heat capacity, 0.7 as emissivity and 7.85e-09 as density, see Fig. 2DNL1.10. Then Type in the same values for all the child materials.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0010.jpg' | relative_url }})

Thermal Properties Page

## Define workpiece

Click on the ‘**Object** ’ item from the operation tree, go to object list page. From the list, delete all the other objects except the ‘Workpiece’.

## Name the Object

Click on the ‘Workpiece’ item from the operation tree , go to define the object. Type in '**Cold-rolled slab specimen** ' as object name, set the temperature to **570** °C, leave all others as default (See Fig. 2DNL1.11.). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) go to the 'Geometry' definition page.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0011.jpg' | relative_url }})

Workpiece definition page

### Create Geometry

In 'Geometry' page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), on the following page choose '**Bar** ', and give 9 mm as width, and 0.8 mm as height (See Fig. 2DNL1.12.), the object geometry is also previewed at the central graphic window area. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to accept all the changes, and it will come back to the 'Geometry' definition, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page to assign material.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0012.jpg' | relative_url }})

Geometry primitive to create the specimen part

### Assign Material for Workpiece

Assign "**Iron** " material from list for workpiece and click on ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) to Mesh page.

### Mesh the Workpiece

In this lab simulation, the total thickness of the compound layer is about 23m![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/micron.jpg' | relative_url }}) (5![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/micron.jpg' | relative_url }})m γ' + 18**![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/micron.jpg' | relative_url }})**m![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/epsilon.jpg' | relative_url }}) ), coating mesh is recommended to represent the compound layer. And mesh window is also used to create finer surface mesh layer.

On ‘**General** ’ mesh page, keep default 'System setup' option, put 1600 in 'Target number of Elements' (See Fig. 2DNL1.13.). Then click on 'Weighting Factors', increase the weight of ‘**Mesh****windows** ’ to **0.8** , See Fig. 2DNL1.14.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0013.jpg' | relative_url }})

General Mesh page

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0014.jpg' | relative_url }})

Weighting Factors

Next click on '**Mesh Windows** ', create two rectangle mesh windows. The first window is put inside the object with relative element size of 1, and second window covers the entire workpiece with the relative element size of 0.1,(see Fig. 2DNL1.15.), this will result into finer surface mesh layer.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0015.jpg' | relative_url }})

Mesh Windows Defined for Workpiece

Next to define coating layer, click on 'Coating', add 12 coating layers of varied thickness as shown in Fig. 2DNL1.16.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0016.jpg' | relative_url }})

Coating Layers for Workpiece

Now click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) to generate the mesh. Click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) on the pop-up window to continue. The mouse icon on the screen turns to busy and then back to normal, which indicates that the mesh has been generated, the results are also plotted on the central graphic area, see Fig. 2DNL1.17.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0017.jpg' | relative_url }})

Mesh Generation

## Initialize Volume Fraction

At this moment, click on ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) to access to the element dialog to initialize the volume fraction. On the item list window click ‘Microstructure’ ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ‘Phase’. Then choose ‘**Alpha** ’ and click on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) to ‘**Initialize****Element****Data** ’. Type in **1** , then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), then close the window. click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until BCC page.

## Boundary Conditions

**Heat Exchange with Environment**

It can be seen that ‘Heat Exchange with Environment’ BCC has been already defined on the entire object surface when mesh was generated. Click on "**Defined** " , then "Environment" to change the ‘Environment temperature’ to **570** °C, which is same as the object temperature ( Fig. 2DNL1.18.).

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0018.jpg' | relative_url }})

Heat Exchange with Environment Definition

**Diffusion BCC**

Constant Nitrogen contents on the workpiece are assumed in this Nitriding Lab simulation, to do so click on '**Atom content** '. Then type in **26.34** for the ‘Atom Pct.’. Select the entire object surface by clicking on ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) on the picking dialog, then click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) to finish the assignment. The BCC definition can be seen in Fig. 2DNL1.19. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Stopping controls page.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0019.jpg' | relative_url }})

Constant Nitrogen Surface Content

## Stopping Controls

Go to define the process duration. Make sure the system is in ‘Expert’ mode, if not, click on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) will switch the system to the expert mode. Then type in **36000** in the ‘**Process****duration** ’ field, see Fig. 2DNL1.20. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to ‘Step’ controls page.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0020.jpg' | relative_url }})

Stopping Controls (Expert Mode)

## Step Controls

Switch back to the ‘Guide’ mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}), since process duration has been defined simulation will stop accordingly,, type **999999** into ‘Number of steps’ field. Set **5** as ‘Step increment’ and **20** sec. as the time per step (see Fig. 2DNL1.21.). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to ‘Generate DB’ page.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0021.jpg' | relative_url }})

Step Controls (Guide Mode)

## Generate Database

In 'Generate DB' page, click ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) to see if anything was missed in the setup and then click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. Observe the message in Message tab informing database generation status.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DNL1.22. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0022.jpg' | relative_url }})

Run Simulation Window

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. User can view the Nitriding process as the simulation proceeds to the specified Step definition from Simulation graphics.

## Post Processing

After the simulation is finished, open the DB in Next Gen post - processor.

**Nitrogen Profiles**

‘State variables between two points’ function is a great tool to exam nitrogen concentration profile (vs. depth below the surface).

Click on ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}), Under **Diffusion**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Dominant****atom** , select " **Nitrogen** " State variable and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) to plot and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

Go to last step, then click on State variables between two points ![]({{ '/assets/icons/post_icons/mo_state_variable_between_2_points_icon.jpg' | relative_url }}) to generate nitrogen profile. Define Start and End points and click on ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }})(see Fig. 2DNL1.23.).

![]({{ '/assets/images/applications/55_nitriding_labs/2d_nitriding_labs/image0023.jpg' | relative_url }})

SV between 2 Points: Atom-Nitrogen
