---
lang: en
title: "Gear Blank EN Lab 12"
---

# Lab 12 Die Stress analysis - Hot Forging

The objective of this lab is to run a die stress analysis. When the stress analysis is being done on only one tool, a one step simulation is sufficient to get accurate stresses. When the stress analysis is being done on die assemblies where there is interaction between the tools, more than one step is typically needed for the die stack to come to a state of equilibrium under the applied load.

In a typical die stress simulation, the workpiece is removed and the forces exerted onto the dies by the workpiece are interpolated onto the tools. 

Open Previously simulated Gear.moproj file in DEFORM MO by clicking on![]({{ '/assets/icons/pre_icons/mo_integrated_manufacturing_proc.jpg' | relative_url }}). MO pre- processor will open.

### Add Die stress Study

At top Left corner of the Display window, Left mouse click on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button and select Add **Die****stress****Study** operation as shown in Fig. L12.1.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0001.jpg' | relative_url }})

Adding Die stress Study

To perform Die stress operation,select last step in Step selection page as shown in Fig. L12.2. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0002.jpg' | relative_url }})

Selecting step list

### Define Top Die general data

Assign Top Die Temperature as **300** °F. By default, the object type of rigid objects from the loaded step will be changed to elastic. Keep the object type as elastic for the Top Die object. From v13.1.1, two new options have been introduced in the object page to position the dies in future steps for Multiple steps die stress analysis, we need not use these options for single step die stress analysis, hence, keep the Need positioning check box turned off as shown in Fig. L12.3.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0003.jpg' | relative_url }})

Top Die window

### Generate Top die Mesh

In Mesh page, enter target number of mesh elements as **40000** , then click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button as shown in Fig. L12.4. to generate mesh.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0004.jpg' | relative_url }})

Mesh window

### Interpolate Forces for Top die

In Force interpolation page, click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) action label to interpolate forces as shown in Fig. L12.5. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0005.jpg' | relative_url }})

Force interpolation of Top Die

### Assign Material for Top die

In material window, assign **AISI-H-13** material from material library and Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

###  Assign Boundary Conditions for Top die

Assign **Vx=Vy=Vz=0** Velocity boundary condition on the top surface of the Top Die. This boundary condition prevents the die from flying off when the forces are applied. (See Fig. L12.6.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0006.jpg' | relative_url }})

Boundary Conditions window

Select **Bottom****die** from operation tree to define Bottom die object and its properties as there is no more variables to be initialized for Top die.

### Define Bottom Die general data

Assign Temperature of Bottom Die as **300** °F. We will keep the object type as Elastic for the Bottom Die and turn off Need positioning check box as shown in Fig. L12.7.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0007.jpg' | relative_url }})

Bottom Die Window

### Generate Bottom Die Mesh

In Mesh page, Enter target number of mesh elements as **50000** , then click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button as shown in Fig. L12.8. to generate mesh.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0008.jpg' | relative_url }})

Mesh window

### Interpolate Forces for Bottom die

In Force interpolation page, click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) action label to interpolate forces as shown in Fig. L12.9. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0009.jpg' | relative_url }})

Force Interpolation Window

### Assign Material for Bottom die

In material window, select **AISI-H-13** material and assign it to the bottom die and Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Assign Boundary Conditions for Bottom die

Assign **Vx=Vy=Vz=0** Velocity boundary condition on the Bottom surface of the Bottom Die. (See Fig. L12.10.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0010.jpg' | relative_url }})

Assigning BCC for Bottom Die

Click on **Simulation****Controls** branch in operation tree, as we need not need to initialize variables and the setup does not require positioning or contact generation.

### Define Simulation Controls

Set **Number****of****Simulation****Steps** to **1** and the **Step****Increment****to****Save** to**1**. Set the **Max**. **elapsed****process****time****per****step** as **1** sec. (See Fig. L12.11.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0011.jpg' | relative_url }})

Simulation Controls window

### Generate Database and Run a Simulation

By selecting the **File****menu![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Export** option, Save a keyword file for the problem as "Diestress".

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label and check for any issues in setup. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

Once the database has been generated switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree.

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. L12.12. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0012.jpg' | relative_url }})

Run Simulation popup window

After completing simulation click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) mode button to review results.

### Review Results

Using the ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) (State Variables) option, plot **Effective****stress** and **Max****Principal****stress** , two of the most important variables in die stress simulations. (See Fig. L12.13. and Fig. L12.14.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0013.jpg' | relative_url }})

Stress Effective contour plot; (a) For Top Die (b) For Bottom Die

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0014.jpg' | relative_url }})

Max Principle stress contour plot; (a) For Top Die (b) For Bottom Die

* * *

### Optional exercise – add a shrink ring to the bottom die

\- Open Project “**Gear** ” in DEFORM MO from DEFORM GUI Main.

\- Add 2nd **Die stress study** and add Die Stress operation as shown in Lab 12: [12.1 Add Die Stress Study.](gear_blank_en.htm#12_1_Add_Die_stress_Study)

\- Keep the selected last step, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and add an additional object from objects window (See Fig. L12.15.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0015.jpg' | relative_url }})

Added additional object

\- Continue **Top** and **Bottom****die** setup as per **Lab 12** **until****section** **12.11**.

Define Case general data

\- Rename additional Object 3 to **Case** and confirm the object temperature is set to **68** °F. We will select object type as **elastic** and turn off Need positioning check box.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0022.jpg' | relative_url }})

Case object page

  * Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and import geometry “**gear_die_case_ENG****.****STL** ” from library.

  * Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and generate mesh with **50,000** elements.

  * Force interpolation is not required. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and assign **AISI-H-13** material.

  * Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and assign Vy=0 to bottom face as shown in Fig. L12.17.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0016.jpg' | relative_url }})

Fix the bottom face velocity in Y direction

Apply a**0.020** ’’ interference (per side) **Shrink****Fit** to ID in **Y** direction – vector is in the **Y** direction as shown in Fig. L12.18.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0017.jpg' | relative_url }})

Shrink fit to the internal dia of the shrink ring perpendicular to the axis Y direction

When you perform a shrink fit, DEFORM will ask if you would like the nodes of the case to be offset by the same amount as the shrink fit tolerance (See Fig. L12.18.). Most of the time, as it is in this lab, you will position your tooling to make contact and then apply the shrink fit. In this case you want to answer **No**. This will prevent the nodes from being displaced. If you import your tooling geometry in such a way that the interference is shown by a overlap between the die and case then clicking **Yes** is the correct option and will displace the nodes of the case so contact can be defined.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0018.jpg' | relative_url }})

Move object nodal coordinates popup for Shrink BCC

-No variable initialization is required and objects are correctly positioned, so click on **Contact** branch in operation tree to generate contact between bottom die and shrink ring.

  * Click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button, select Maser as Case object and Slave as Bottom Die object. Define friction value as 0.08. 

  * Click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact. (See Fig. L12.19.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0019.jpg' | relative_url }})

Inter-object relations window

\- Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and Change the **number of simulation steps** to **5** steps and **save****every****5**.

\- Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and write database.

\- Click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode button and run simulation.

\- After simulation click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) to enter the post processor and compare the stress values at the stress concentration on the bottom die between load cases with the ring and without a shrink ring (Lab 12 results) as shown in Fig. L12.21. and Fig. L12.22.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0020.jpg' | relative_url }})

Bottom die effective stress with and without Shrink ring

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0021.jpg' | relative_url }})

Bottom die maximum principal stress with and without Shrink ring
