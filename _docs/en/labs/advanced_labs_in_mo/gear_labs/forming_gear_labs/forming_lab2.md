---
lang: en
title: "Forming Lab 2"
---

# Lab 2. Rerun Sequence with a Larger Billet

Click the New ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon in the top left corner of the interface. Click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) to close the current project and save any changes.

Set the Project Name to **Gear_LargerBillet**. Use the Copy existing project option and browse to find PROBLEM **2DGear\2DGear.moproj** (See Fig. L1.1.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab2_image0001.jpg' | relative_url }})

New MO project window

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). The system will copy all the information from the original project into the new **Gear_LargerBillet** folder.

Note: Copying a project using the user interface automatically renames several files and folders in the project. It is much cleaner than copying/pasting the problem folder.

### Change the Billet size

Click on the Upset tile in the Operation Editor to select the 1st operation in the project. The Preprocessor will open for this operation (See Fig. L2.2.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Workpiece Geometry page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab2_image0002.jpg' | relative_url }})

Upset operation selection

### Creating new geometry for Workpiece

Change the workpiece dimensions to 2.5 in radius, 8.267 in height, with 0.1 in corners. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_no_button.jpg' | relative_url }}) in Delete mesh popup to delete mesh popup to delete mesh (See Fig. L2.3.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Workpiece mesh page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab2_image0003.jpg' | relative_url }})

Delete mesh popup

### Generate mesh for new geometry of workpiece

Set the target number of elements as **2000** and click the ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to generate the mesh for workpiece. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until positioning page.

###  Positioning

Use ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) to position the tools to the workpiece. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

### Generating contact

Generate contact using the ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

### Stopping controls

In Stopping controls, change the Primary die displacement stopping control from 6 in. to **6.5** in. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step controls page.

### Step controls

Go to Step and change the **Number** of **simulation** steps to **1000**. Setting the steps high like this guarantees that the simulation will not run out of steps and will instead stop due to the defined stopping criteria. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page

### Generate DB

Generate the database by clicking on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

Because there is no change required in settings for the 2nd operation, we can generate the database and run the simulation.

Click the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) button and then uncheck submit job to the simulation queue. Unchecking this option will make the job run on the local computer. Use the default **Start from last negative step** option. Click the ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to start the simulation.

When the upset operation is completed, DEFORM will automatically import the new tools and start the 2nd operation.

### Review the results

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

Play through all steps. Note that the part completely fill out the die cavity.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab2_image0004.jpg' | relative_url }})

Workpiece shape at last step of second operation
