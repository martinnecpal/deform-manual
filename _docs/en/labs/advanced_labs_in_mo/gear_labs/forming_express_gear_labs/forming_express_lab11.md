---
lang: en
title: "Forming Express Lab11"
---

# Lab 11.Add a case with a press fit

### Step selection

Select the **last****step** in step list, then Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Objects page.

### Add object

In the Objects table, add a 3rd object. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to New object page.

### Top die and Bottom die

Repeat the same mesh/interpolation/material/BCC procedure as explained in [Lab 10: Die stress](/docs/en/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab10/) for the Top Die and Bottom Die. After completing the setup, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object 4 page.

### Object 4 General page

Change the object name to **Case** and set the temperature to **300** °F. We will select the object type as Elastic for the Case and turn off Need positioning check box. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to geometry page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0010.jpg' | relative_url }})

Case object page

#### Create Case Geometry

Use Define primitive to create a **hollow****cylinder** for case with inside **radius****8.5** in, **Outer radius 14.4** in, and **height** of **5.4** in.( See Fig. L11.2.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0001.jpg' | relative_url }})

Case geometry primitive window

#### Generate Case Mesh

Generate a mesh with **250** elements. Since the workpiece does not contact this case, no force interpolation is required. So, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

#### Assign Material for Case

In Material window, assign **AISI-H-13** material from material library's, from **Die_material** catagory and Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to BCC page.

#### Assign BCC

We will assign a **shrink fit** boundary condition along the ID. Click Shrink Fit in the boundary condition list, and then use the By edge ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) tool to select the ID of the Case. Next, select **User** type and input a value of **0.002** in (See Fig. L11.3.). for both Interference input fields. Choose the x direction as the shrink fit direction. Click ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0002.jpg' | relative_url }})

Selecting the ID to define Shrink fit BCC

Note: The purpose of the two input fields it to allow variable interference along the defined boundary. The arrow near the center line displays the start and end point of the selected boundary. Since we are doing a uniform interference, we chose the same value for both start and end points.

A pop-up window will ask if you want to move nodes by the offset distance. 

If tools are drawn true to size (i.e. overlapping), then we need to move the nodes. In this case, they are already drawn as matching surfaces, so DO NOT MOVE the nodes (i.e. answer **No**) (See Fig. L11.4.). Assigned Shrink fit BCC for Case object is as shown in Fig. L11.5.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0003.jpg' | relative_url }})

Move object Nodal coordinate popup

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0004.jpg' | relative_url }})

Assigned Shrink fit BCC for Case

#### Positioning Case

Go to **Positioning** and **Drag** the **Case** down until the **bottom****surface** of the **Case** and **Bottom****Die** are **aligned**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Contact page.

### Contact

Add one relation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button, select **Maser** as **Case** object and **Slave** as **Bottom****Die** object. Define friction value as **0.1**. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact.(See Fig. L11.6.) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation controls page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0005.jpg' | relative_url }})

Inter object relation windows

### Simulation Controls

Default simulation controls are acceptable for this model. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate DB.

### Generate DB

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

Save the project and click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue****Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

### Review the results

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

In the Post-processor, click on the positive step in the step list, Plot **Effective****stress** state variable (See Fig. L11.7.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0006.jpg' | relative_url }})

Effective stress State variable Plot

Go to the Set up ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) dialog, and display Max principal stress (See Fig. L11.8.) and other stress components.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0007.jpg' | relative_url }})

Max Principal Stress state variable plot

Compare the stress plots between the first and second die stress load cases. (See Fig. L11.9 and [Fig. L11.10.](forming_express_lab10.htm#Fig_L10_10_Max_Principal_Stress_state_variable_plot))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0008.jpg' | relative_url }})

Stress Effective state variable plot of both Die stress study 1(left side) and Die stress study 2 (right side)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0009.jpg' | relative_url }})

Max Principal Stress state variable plot of both Die stress study 1(left side) and Die stress study 2(right side)
