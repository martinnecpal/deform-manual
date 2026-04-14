---
lang: sk
title: "46.1. Copy Mirroring"
---

# 46.1. Copy/Mirroring

46.1.1. How to add Copy/Mirroring Operation

[46.1.2. Adding Copy/Mirroring Operation](46_1_copy_mirroring.htm#46_1_2_Adding_Copy/Mirroring_Operation)

46.1.3. Objects Page

46.1.4. Object Page

46.1.5. Mirroring Parameters Page

46.1.5.1. For Batch mode

46.1.5.2. Mirroring/Copying in Interactive mode

46.1.6. Generate DB

46.1.7. Continue with subsequent operation

46.1.8. Post Processing results for Copy/Mirroring Operation

## How to add Copy/Mirroring Operation

Copy/Mirroring operation will be added as subsequent operation to an operation having symmetry models in multiple operations to mirror the symmetry object along the symmetry plane. Copy/Mirroring operation can also be added as first operation and import symmetry objects to continue the multiple operations setup. Copy/ Mirroring operation is explained in this manual using Spike_ForgingBlow1.key file which consists of symmetry setup. The keyword file consists of 90 degree symmetry setup which will be copied to generate 180 degree model.

Before adding the Copy/Mirroring operation we need to set up forming operation using the Sipke_ForgingBlow1.Key file, so we will open the MO wizard in SI units > add 3D forming operation > import the Spike_ForgingBlow1.KEY as shown in Fig. 46.1.1. > Continue till generate DB and run the simulation.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0001.jpg' | relative_url }})

Importing the 3D Spike key file

## Adding Copy/Mirroring Operation

After Running the first Forming operation simulation, we can add the Copy/Mirroring operation from explorer’s Simulation operator group as shown in [Fig. 46.1.2.](46_1_copy_mirroring.htm#Fig_46_1_2_Adding_Copy/Mirroring_Operation) Click on Copy/Mirroring operation, we will get the “Setup type” pop-up as shown in Fig. 46.1.3.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0002.jpg' | relative_url }})

Adding Copy/Mirroring Operation

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0003.jpg' | relative_url }})

Setup type Pop-up

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0004.jpg' | relative_url }})

Copy/Mirroring Operation in Batch Mode

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0005.jpg' | relative_url }})

Copy/Mirroring Operation in Interactive Mode

## Objects Page

We can add objects using the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and if we want to delete any object, we need select the respective object and click on ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) button as shown in the Fig. 46.1.6. We can retain the objects which are to be mirrored and delete other objects and user can also add new objects and import data from other keyword/ database or geometry files.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0006.jpg' | relative_url }})

Objects Page

## Object Page

If the user is in batch mode setup than all the objects will be of Read from DB object type except newly added objects. If set up type is “Interactive” then user can change the object type. (See Fig. 46.1.7.)

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0007.jpg' | relative_url }})

Workpiece Object Page

## Mirroring Parameters Page

### For Batch mode 

The user can add the Mirroring by selecting the ![]({{ '/assets/icons/pre_icons/mo_add_mirroring_radio_option.jpg' | relative_url }}) option in the Edit mode tab of “Mirroring Parameters” and if we want to delete the added mirroring, we need to select the ![]({{ '/assets/icons/pre_icons/mo_delete_mirroring_radio_option.jpg' | relative_url }}) option in the Edit mode tab of “Mirroring Parameters”. The user can also define the tolerance value for the mirroring object as shown in the Fig. 46.1.8. The Mirror plane data will be updated during DB Generation.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0008.jpg' | relative_url }})

Mirroring Parameters Page (For Batch Mode)

### Mirroring/Copying in Interactive mode 

The user can add the Mirroring by selecting the ![]({{ '/assets/icons/pre_icons/mo_add_mirroring_radio_option.jpg' | relative_url }}) option in the Edit mode tab of “Mirroring Parameters” and if we want to delete the added mirroring, we need to select the ![]({{ '/assets/icons/pre_icons/mo_delete_mirroring_radio_option.jpg' | relative_url }}) option in the Edit mode tab of “Mirroring Parameters”. User can also define the tolerance value for the mirroring object. After selecting the required edit mode and defining the tolerance value, user need to click on ![]({{ '/assets/icons/pre_icons/mo_merge_button.jpg' | relative_url }}) button to generate the object, see Fig. 46.1.9. that shows mirrored object.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0009.jpg' | relative_url }})

Mirroring Parameters Page (For Interactive Mode)

## Generate DB

If the first operation simulation is completed then during the Copy/Mirroring DB Generation, the Mirrored objects are automatically updated as shown in the Fig. 46.1.10. In case if previous operation is not simulated then it shows the preview with objects without simulation output.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0010.jpg' | relative_url }})

DB Generation

## Continue with subsequent operation

After completing the Copy/Mirroring Setup we can add the 3D Forming Operation from Explorer as shown in the Fig. 46.1.11.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0011.jpg' | relative_url }})

Adding 3D Forming Operation after Copy/Mirroring Operation

  
Now we can define the 2nd forming operation setup data after mirroring the objects as shown in the [Fig. 46.1.12.](46_1_copy_mirroring.htm#Fig_46_1_12_3D_Forming_Operation_after_Copy/Mirroring_Operation_Batch_Mode) and Fig. 46.1.13.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0012.jpg' | relative_url }})

3D Forming Operation after Copy/Mirroring Operation (Batch Mode)

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0013.jpg' | relative_url }})

3D Forming Operation after Copy/Mirroring Operation (Interactive Mode)

## Post Processing results for Copy/Mirroring Operation

From MO Post, user can review the Copy/Mirroring Operation. Selection of the Copy/Mirroring Operation step will load the respective step with mirror object. It will be having only one negative step where Mirroring model is available as shown in Fig. 46.1.14.

![]({{ '/assets/images/operation_templates/46_copy_mirroring/46_1_copy_mirroring/image0014.jpg' | relative_url }})

Copy/Mirroring Operation Post Mode
