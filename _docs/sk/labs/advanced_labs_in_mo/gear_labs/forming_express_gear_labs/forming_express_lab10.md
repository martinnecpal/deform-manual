---
lang: sk
title: "Forming Express Lab10"
---

# Lab 10. Die stress

### Open Project

Open the Project **FE_Gear_LargerBillet**.

### Add Die stress study

In this lab, we will preform Die stress operation for the dies using Die stress study operation, so click on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button and select Die stress study from the list (See Fig. L10.1.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab10_image0001.jpg' | relative_url }})

Adding Die stress study from list

### Step selection

Select the **last****step** in step list for die stress analysis (See Fig. L10.2.), then Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until top die general page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab10_image0002.jpg' | relative_url }})

Step selection window

### Define Top die data

Verify the Top die temperature is **300** °F. By default, the object type of rigid objects from the loaded step will be changed to elastic. Keep the object type as elastic for the Top Die object. From v13.1.1, two new options have been introduced in the object page to position the dies in future steps for Multiple steps die stress analysis, we need not use these options for single step die stress analysis, hence, keep the Need positioning check box turned off. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until mesh page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab10_image0009.jpg' | relative_url }})

Top Die page

#### Generate Top die mesh

Set the target number of elements to **1000** and generate mesh. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

#### Assign Top die Material

In Material window, assign **AISI-H-13** material from material library's, from Die_material catagory and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to BCC page.

#### Assign BCC for Top die

In BCC page, check the default assigned Deformation BCC for Left side of the Top die in X-Direction, then Apply Vy = 0 Velocity boundary condition on the Top surface of the Top Die (See Fig. L10.4.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Force interpolation page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab10_image0004.jpg' | relative_url }})

Top die BCC window

#### Interpolate Force for top die 

In Force interpolation page, click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) action label to interpolate forces as shown in Fig. L10.5. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom Die page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab10_image0003.jpg' | relative_url }})

Top die Force interpolation window

### Bottom die data

Verify the Bottom die temperature is **300** °F. We will keep the object type as Elastic for the Bottom Die and turn off Need positioning check box. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until mesh page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab10_image0010.jpg' | relative_url }})

Bottom Die page

#### Generate Bottom die mesh

Set the **target number of elements** to **1000** and generate mesh. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

#### Assign Bottom die Material

In Material window, **AISI-H-13** material from material library and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to BCC page.

#### Assign BCC for Bottom die

In BCC page, check the default assigned Deformation BCC for Left side of the Bottom die in X-Direction, then Apply **Vy = 0** Velocity boundary condition on the Bottom surface of the Bottom Die (See Fig. L10.7.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab10_image0006.jpg' | relative_url }})

Bottom die BCC page

#### Interpolate Force for Bottom die 

In Force interpolation page, click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) action label to interpolate forces as shown in Fig. L10.8. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab10_image0005.jpg' | relative_url }})

Bottom die Force interpolation window

### Generate DB

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

Save the project and click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue****Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

### Review the results

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

In the Post-processor, click on the positive step in the step list.

Plot **Effective****stress** state variable (See Fig. L10.9.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab10_image0007.jpg' | relative_url }})

Effective stress State variable Plot

Go to the Set up ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) dialog, and display **Max****principal****stress**(See Fig. L10.10.) and other stress components.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab10_image0008.jpg' | relative_url }})

Max Principal Stress state variable plot

Switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode and add another Die stress study to add Shrink Fit. Click [Lab 11. Die stres with a press fit.](/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab11/) to continue Shrink fit lab.
