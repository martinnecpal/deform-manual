---
lang: sk
title: "2D Inverse Heat Lab2"
---

# 2D Inverse Heat Lab 2 : Oil Quenching of Disk

  
**Problem Summary:**

This lab will demonstrate how to use the Inverse Heat Transfer Wizard to determine heat transfer coefficients of a disk quench process. Experimentally measured temperature data is needed. Heat transfer coefficients can be functions of temperature or time. Multiple Zones of heat-transfer coefficients are assigned to the disk.

2.1. Starting a new problem

2.2. Set Geometry type and mode

2.3. Setting Process Conditions

2.4. Defining Material

2.5. Defining Workpiece Object

2.6. Import geometry

2.7. Generate mesh

2.8. Assigning Material

2.9. Generating Structured Mesh

2.10. Temperature Measurement Points

2.11. Defining Time Zones

2.12. HT Zone Partitioning

2.13. Defining Heat Transfer Zones

2.14. Defining Step controls

2.15. Optimization control

2.16. Database Generation

2.17. Optimization

2.18. Optimization results

## Starting a new problem

Start a new Inverse Heat Transfer Wizard problem with problem ID **DISK_INVHEAT**. You can do so by clicking the ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) button and choose “**2D Inverse Heat** ”, enter Problem name as ****DISK_INVHEAT** ** and choose “**English** ” for "Unit System" (see Fig. 2DINVL2.1.). You can select the directory under Location filed and then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to open Inverse Heat wizard.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab1/image0001.jpg' | relative_url }})

Problem Setup window

## Set Geometry type and mode

As the 2D Inverse Heat wizard opens, you should see a window as shown in Fig. 2DINVL2.2. Set “**Geometry****Type** ” as “**Axisymmetric** ”. If user is interested in calculating transformations or atom content due to diffusion then user can turn on respective check boxes under “Mode” tab. In this lab we will not turn on any check box as we will be calculating only heat transfer co-efficients. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0002.jpg' | relative_url }})

Initialization Window

## Setting Process Conditions

In this page user can set the environment conditions. If the process involves Quenching and heat transfer then respective check boxes can be turned on to define the environment conditions. Our process involves only quenching and environment temperature is constant, hence **turn********on** “**Quench** ” check box and define **environment** **temperature** as **68** °F (see Fig. 2DINVL2.3.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0003.jpg' | relative_url }})

Setting up Process conditions

## Defining Material

In page “**Material** **list** ”, choose ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) and in the material library, choose "**Super alloy** " category and load “**INCONEL-718- 11[1700-2050F (925-1120C)]** ” as shown in Fig. 2DINVL2.4. (Note that the temperature ranges are only for the plastic data). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until “Workpiece” page.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0004.jpg' | relative_url }})

Loading Material data from library

## Defining Workpiece Object

In workpiece page define “Object Temp.” as**2000****°F** as shown in Fig. 2DINVL2.5. Make sure the object type is **plastic** and Primary Die check box is checked. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to geometry page.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0005.jpg' | relative_url }})

Workpiece Object Definition

## Import geometry

In **Geometry** page, click on “Load Geometry from File” ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) icon and import geometry file “**INVHEAT_DISK****.****GEO** ” from ‘2D/LABS’ directory as shown in Fig. 2DINVL2.6. Turn on “Show geometry inside mark” check box and click on ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) label to check and correct the geometry, see Fig. 2DINVL2.6.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0006.jpg' | relative_url }})

Geometry window

Click on ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) and then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to geometry correction pop-up and then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to come out of Geometry Correction page, see Fig. 2DINVL2.7. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0007.jpg' | relative_url }})

Check and Correct Geometry window

## Generate mesh

While user is in “Mesh” page, expert mode can be used to access the advanced mesh options. Click on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) icon in tool bar to change to expert mode and then enter **800** as **T******a** rget number of elements** in “**General** ” tab for unstructured mesh, see Fig. 2DINVL2.8. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button, Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page to assign material.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0008.jpg' | relative_url }})

Defining unstructured mesh

## Assigning Material

Select material “**INCONEL****-718- 11[1700-2050F (925-1120C)]** ” from the material list to assign to workpiece as shown in Fig. 2DINVL2.9.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0009.jpg' | relative_url }})

Assigning Material

## Generating Structured Mesh

The structured surface mesh helps provide better thermal solution accuracy with less computing time. Hence click ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) from Material page. We will use **2 layers** of structured surface mesh using coating mesh with thickness of **818****Microns** and **1116****microns** for layer 1 and 2 respectively with “**INCONEL****-718- 11[1700-2050F (925-1120C)]”** material and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button as shown in Fig. 2DINVL2.10. Do not use “Generate Coating” button. Click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) button for the pop-up “Do you want generate coating mesh?”. After generating mesh Zoom into the top left corner of the object and check generated mesh for structured layers. Meshed object looks as shown in Fig. 2DINVL2.11. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until “Temperature Measurement Points” page as default assigned BCC are fine for this lab.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0010.jpg' | relative_url }})

Structured mesh generation using Coating mesh

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0011.jpg' | relative_url }})

Meshed Workpiece After Generating Structured Mesh

## Temperature Measurement Points

In “Temperature Measurement Points” page, click the button ![]({{ '/assets/icons/pre_icons/mo_import_file_icon2.jpg' | relative_url }}) (as indicated in Fig. 2DINVL2.12.) and load the file "**InvHeat_Disk_Meas_Pnts.DAT** ” from **/2D/LABS**. You should see points in the graphical window as shown below in Fig. 2DINVL2.12. We can notice that 13 temperature measurement points are loaded onto the workpiece from the file.

Thermal history data for each point can be defined by clicking on the ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_define_button.jpg' | relative_url }}) button in the last column of the table. Click on ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_define_button.jpg' | relative_url }}) and load “InvHeat_Disk_Thermal_History_P1” file for point 1 using “Load” button from the /2D/Labs folder and click![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button (see Fig. 2DINVL2.13.)), similarly load for points 2 to 13 from respective files “InvHeat_Disk_Thermal_History_P2” to “InvHeat_Disk_Thermal_History_P13” available in /2D/LABS folder. “Define” button in the last column of the table will change into ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_edit_button.jpg' | relative_url }}) after you had defined the Thermal History Data for the point. We can use ![]({{ '/assets/icons/pre_icons/mo_exam_ all_button.jpg' | relative_url }}) button (see Fig. 2DINVL2.13.) to verify the data defined for all points. Fig. 2DINVL2.14. shows the temperature defined for all points. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0012.jpg' | relative_url }})

Temperature measurement Points

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0013.jpg' | relative_url }})

Thermal History Data window for Point 1

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0014.jpg' | relative_url }})

Thermal History Data defined for all 13 points

## Defining Time Zones

In time zones page user can define time zones for Quenching and Transfer. Since in this lab we had opted to simulate only “Quench”, only “Quench” time zone definition is available. We would like to simulate the process for 600 sec as the last point of temperature measurement is available from thermal history is at 600 sec. So enter **Start****time** as **0****sec** and **End****time** as **600** sec. Thermal History graph of all the points within the specified time can be seen in display area, see Fig. 2DINVL2.15. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0015.jpg' | relative_url }})

Quench Time Definition in Time Zone Page

## HT Zone Partitioning

In page “HT Zone Partioning” we can see that system has automatically generated zones based upon temperature points defined, Turn on “Display Zone” check box to verify the zones created. For this lab we will create five zones manually. Inner Radius as Zone1, bottom edge as Zone2, Outer radius and top surface until end point of step fillet as Zone 3, step fillet as Zone4 and Top surface from the inner radius up to start of step fillet as Zone5.

We will delete the already defined zones using “Delete All” button. By default entire outer surface edges will be considered as one zone. After deleting points, we will pick the start point of inner radius as first point, end point of inner radius as second point, bottom edge corner point as third point, end point of step fillet as fourth point and start point of step fillet as fifth point as shown in Fig. 2DINVL2.16. Click on “Generate Zone” to generate zones. Zones are created between the pair of points selected, see Fig. 2DINVL2.16. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0016.jpg' | relative_url }})

HT Zone Partitioning Window

## Defining Heat Transfer Zones

In “Heat Transfer Zones” page, we can see that 5 zones are created. Selected zone in the table will display respective zone on the object, see Fig. 2DINVL2.17.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0017.jpg' | relative_url }})

Displaying Zone1

Click on ![]({{ '/assets/icons/pre_icons/mo_iniitialize_htc_button.jpg' | relative_url }}) button to define control points and limits, make sure HTC function is based on temperature. By default system will add some control points, we will delete them for this lab and use eight points. Click on ![]({{ '/assets/icons/pre_icons/mo_delete_all_button2.jpg' | relative_url }}) button and then enter eight values **70, 600, 900, 1200, 1400, 1600, 1800,** and **2000** , see Fig. 2DINVL2.18. Make sure interpolation method is Linear. We will use **1e-3 for** the **initial****guess** , and use **7e-5** and **5e-3** for **lower** and **upper****bounds**. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Initializing Window.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0018.jpg' | relative_url }})

Deleting Unwanted Zone #3

Control points and limits settings can be set for each zone separately using ![]({{ '/assets/icons/pre_icons/mo_edit..._button.jpg' | relative_url }}) button next Zone in “Heat Transfer Zones” page, see Fig. 2DINVL2.17. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until “Step” page. 

## Defining Step controls

In “Step” page, change “**Temperature****change per step** ” to**5.0** and leave other values to defaults as shown in Fig. 2DINVL2.19. Click on .![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0019.jpg' | relative_url }})

Defining Step controls

## Optimization control

In “Optimization Control” page as shown in Fig. 2DINVL2.20., all default settings are fine and make sure that **BFGS** is **checked****on** , click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0020.jpg' | relative_url }})

Optimization control Window

## Database Generation

In DB Generation page, click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) to verify the set up for errors and warnings, you should see a message “Data Valid!” if there are no errors. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) to generate Database.

## Optimization

After Database is generated switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab above the object tree and click on ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) to start the optimization, see Fig. 2DINVL2.21. You can see a message “MULTIPLE OPERATION COMPLETED.” at the end of Simulation Log file after optimization is completed.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0021.jpg' | relative_url }})

Running Optimization

## Optimization results

To view optimization results click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab. In Tools” page under “Tools” you can see two icons (see Fig. 2DINVL2.22.),

![]({{ '/assets/icons/pre_icons/mo_inverse_heat_optimal_htc.jpg' | relative_url }}) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) To view Optimized HTC values.

![]({{ '/assets/icons/pre_icons/mo_inverse_heat_local_objective_button.jpg' | relative_url }}) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) To view simulated temperature values at Temperature Measurement Points.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0022.jpg' | relative_url }})

Post Tools to view Optimization Results

Click on ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_optimal_htc.jpg' | relative_url }}) to view optimized HTC values for each zone, a Heat Transfer Zone window will open as shown in Fig. 2DINVL2.23. Select each zone and click on ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_view_thermal_icon.jpg' | relative_url }}) to view optimized HTC values, see Fig. 2DINVL2.24. for Zone #1 optimized HTC values. 

![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) can be used to view objective value history, see Fig. 2DINVL2.25.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0023.jpg' | relative_url }})

Heat Transfer Zones Window in Post Tab

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0024.jpg' | relative_url }})

Optimized HTC values for Zone #1

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0025.jpg' | relative_url }})

Objective Value History

The local objective optimization result can be viewed using ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_local_objective_button.jpg' | relative_url }}), it gives the comparison between the experimental temperature and the simulated temperature values when the optimized heat transfer coefficient values are used. These values can be saved if necessary using ![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) button (see Fig. 2DINVL2.26.). User can select a point (See Fig. 2DINVL2.28.) and click on ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_view_thermal_icon.jpg' | relative_url }}) to plot the comparison between the experimental temperature and the simulated temperature values, Fig. 2DINVL2.27. shows the comparison between the experimental temperature and the simulated temperature values for Point 1. ![]({{ '/assets/icons/pre_icons/mo_inverse_heat_view_all_button.jpg' | relative_url }}) (see Fig. 2DINVL2.26.) can be used to plot comparison between the experimental temperature and the simulated temperature values for all points, see Fig. 2DINVL2.28.

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0026.jpg' | relative_url }})

Temperature Measurement Points in Post

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0027.jpg' | relative_url }})

Local Objective Optimization Result for Point 1

![]({{ '/assets/images/labs/inverse_heat_labs/2d_inverse_heat_lab2/image0028.jpg' | relative_url }})

Local Objective Optimization Result for all Points
