---
lang: en
title: "2D Cutting Lab"
---

# 2D Cutting Lab

1.1 Problem Summary

1.2. Creating New Problem

1.3. Define Machining Process data

1.4. Loading Cutting tool Coating material

1.5. Defining Cutting Edge geometry

1.6. Coating Definition

1.7. Assign Tool material

1.8. Generating Tool mesh

1.9. Tool Boundary conditions

1.10. Set the Workpiece geometry data

1.11. Assigning Workpiece material

1.12. Generating Mesh for Workpiece

1.13. Workpiece Boundary condition page

1.14. Tool Positioning

1.15. Tool wear setting

1.16. Contact page

1.17. Step control page

1.18. Generate Database

1.19. Running Simulation

1.20. Post Processing

## Problem Summary

This lab will briefly demonstrate how to use the machining template to prepare model data representing orthogonal cutting conditions (cutting edge is orthogonal/perpendicular to the cutting direction) to simulate chip formation process. Interactive definition of the process conditions, cutting edge, coating, material, steady state and tool stress related features are discussed here. Brief description of the orthogonal cutting conditions and how the process parameters are related to the modeling domain are indicated as shown in the [Fig. 2DCL1.1.]()

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0001.jpg' | relative_url }})

Relationship between the process data and analysis domain

## Creating New Problem

**We can open 2D Cutting wizard in two ways:**

**a.** Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New****Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select " **Integrated Manufacturing Process** " radio button and Unit system as "**SI** " using radio button. Define Problem Name as "**2D_CUTTING** " and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Integrated Manufacturing Process. Multiple Operation wizard will open, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "**2D_CUTTING** " as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation. Integrated Manufacturing Process will open, add 2D Cutting operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to 2D Cutting or by drag and drop into the Operation editor.

**b.** Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New****Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**2D Cutting"** radio button and Unit system as "**SI** " using radio button as shown in Fig. 2DCL1.2.. Define Problem Name as " **2D_CUTTING** " and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem with 2D Cutting operation in MO wizard.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0002.jpg' | relative_url }})

Problem Setup Page

## Define Machining Process data

Under the ‘**Process** ’ menu, Select **Simulation****type** as '**Transient****Analysis** ', enter the **Environment Heat Transfer temperature** as **22.5** °C and use default Convection coefficient **0.02** N/sec/mm/C. Select the ‘**surface****speed** as **250****m/min** and **feed****rate** as **0.15 mm/rev** ’ (see Fig. 2DCL1.3.). Alternatively user can also specify rotational speed of the workpiece and part diameter instead of surface speed. Then click on![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0003.jpg' | relative_url }})

Process page

## Loading Cutting tool Coating material

Load '**Coating-TiN** ' and '**Coating-Al2O3** ' Material from **Tool_Material** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) buton for assigning to Tool coating. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Tool page.

## Defining Cutting Edge geometry

In ‘**Tool** ’ page, enter the tool temperature as **20** °**C**. We can import the cutting edge geometry from a previously defined simulation keyword file or a database file using ![]({{ '/assets/icons/pre_icons/mo_import_object_button.jpg' | relative_url }}) option. For this lab we will define the cutting edge geometry using the primitives available with the system. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to enter the ‘**Insert Geometry** ’ menu (see Fig. 2DCL1.4.) and click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Select **#** 3 **geometry** in Primitive page and click on ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) to Create geometry. Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to come out of the ‘Geometry Primitive’ menu and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0004.jpg' | relative_url }})

Define Primitive Window

## Coating Definition

Assign ‘**Coating****Material** ’ and thickness in Coating material table, add (![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }})) two layers of coating. For the **outer layer** select **10****microns** as coating thickness and ‘**TiN** ’ as the material and for the **inner****layer** select **10** microns as the coating thickness and ‘**Al2O3** ’ as the coating layer (see Fig. 2DCL1.5.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0005.jpg' | relative_url }})

Coating layer and Material Definition

## Assign Tool material

In Material Window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) to Load material data from Library and load '**WC** ' material from ‘**Tool_Material** ' category by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button as shown in Fig. 2DCL1.6. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate Mesh for the Tool.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0006.jpg' | relative_url }})

Loading Tool material from Material Library

## Generating Tool mesh

In the Tool mesh generation menu select ‘**700** ’ as the target number of elements for the insert and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) (see Fig. 2DCL1.7.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0007.jpg' | relative_url }})

Tool Mesh Page

## Tool Boundary conditions

Next step is to view the thermal boundary conditions generated by the system in the BCC menu. The program generates heat exchange with environment (part of which comes from insert contact region) and the fixed nodal temperature BCC for the surfaces away from the cutting edge (see Fig. 2DCL1.8.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed to the workpiece setup.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0008.jpg' | relative_url }})

Tool Boundary Condition

## Set the Workpiece geometry data

In the ‘Workpiece setup’ define workpiece as a **plastic****object** and **temperature** as **22.5** °C and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed.

Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) label in the ‘Workpiece Geometry’ page. Using the parameters **L = 3** and **H = 1** , click on ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) to create the workpiece geometry (see Fig. 2DCL1.9.). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close this geometry menu and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to Material page.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0009.jpg' | relative_url }})

Defining Workpiece geometry

## Assigning Workpiece material

In ‘**Workpiece****material** ’ page, choose the option ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) ‘import material from library’ option, select ‘**Steel** ’ category and ‘**AISI-1045 (machining)** ’ (see Fig. 2DCL1.10.). ‘Load’ this material and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate Mesh.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0010.jpg' | relative_url }})

Loading Workpiece material form Library

## Generating Mesh for Workpiece

Select **15** as No. of elements through uncut chip thickness for the workpiece and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) to complete mesh generation for the workpiece (see Fig. 2DCL1.11.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to BCC page.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0011.jpg' | relative_url }})

Workpiece mesh page

## Workpiece Boundary condition page

In the ‘View Workpiece BCC’ menu, check the boundary conditions imposed on workpiece by the system (see Fig. 2DCL1.12.), and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Controls page. Note the velocity BCC assigned to the bottom edge away from the cutting surface to prevent workpiece from flying. Heat Exchange with BCC is assigned to all surfaces except bottom edge and to bottom edge temperature BCC is assigned. From V13.0.1, instead of Surface Velocity (Vx) BCC, Movement BCC will be defined to bottom edge of the Workpiece (See Fig. 2DCL1.12.) and movement will be defined in Movement page of the Workpiece. Heat Exchange with BCC is assigned to Top edge and -X (left side) edge. Temperature BCC is assigned to bottom edge and +X (right side) edge. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0012.jpg' | relative_url }})

Boundary Condition for workpiece

##  Tool Positioning

In the ‘Position’ menu, click on ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) position’ (see Fig. 2DCL1.13.). Automatic position will position the objects automatically in simple setup with one cutting tool and workpiece and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0013.jpg' | relative_url }})

Objects after positioning

## Tool wear setting

Select Usui’s model and input coefficients a, b, please note that these (shown next to the equation) are only some typical values that can be obtained from the literature, and user is responsible for accuracy of this data (see Fig. 2DCL1.14.). If user is interested in Tool wear calculation then Turn on "Update worn geometry" check box. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to contact page.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0014.jpg' | relative_url }})

Tool wear setup window

## Contact page

In **Contact** page, use default relations. Click on **Tool - Workpiece** relation ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Edit button) and define **shear****friction** factor as **0.48** and the interface heat transfer coefficient as **39.5****N/sec/mm/C** as shown in Fig. 2DCL1.15., click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step control page.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0015.jpg' | relative_url }})

Contact page

## Step control page

Check the ‘Simulation controls’ and set the **length****of****cut** as ‘**1 mm** ’ and leave the rest as default values as shown in Fig. 2DMDL1.16. and proceed to generate the Database.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0016.jpg' | relative_url }})

Step Control page

## Generate Database

In Generate DB page. Click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. Observe the message in Message tab informing database generation status.

## Running Simulation

Once the database has been generated switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DCL1.17. Use the default **Continue****Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0017.jpg' | relative_url }})

Run Simulation Window

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. User can view the cutting process as the simulation proceeds to the specified cutting length from Simulation graphics.

When the simulation is finished we can observe that the following message is added to the end of the Message file:

"PROGRAM STOPPED!

THE CURRENT TIME 0.0002400

THE CURRENT LOCAL TIME 0.0002400 HAS REACHED THE SPECIFIED LIMIT 0.0002400"

## Post Processing

When the simulation is completed, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.

Play through the steps of the simulation and look how the chip has been formed during cutting process. (see Fig. 2DCL1.18.)

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0018.jpg' | relative_url }})

MO Post mode

Plot the **Effective****Stress** for the workpiece object and observe the plot as shown in below Fig. 2DCL1.19.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0019.jpg' | relative_url }})

Effective stress plot for workpiece object at last step

Plot the **Effective** **Strain** for the workpiece object and observe the plot as shown in below Fig. 2DCL1.20.

![]({{ '/assets/images/labs/machining_labs/2d_cutting_lab/image0020.jpg' | relative_url }})

Effective strain plot for workpiece object at last step
