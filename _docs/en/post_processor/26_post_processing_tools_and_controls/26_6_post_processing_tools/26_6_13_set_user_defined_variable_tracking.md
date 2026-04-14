---
lang: en
title: "26.6.13. Set User Defined Variable Tracking"
---

# 26.6.13. Set User Defined Variable Tracking ![]({{ '/assets/icons/post_icons/mo_set_user_defined_state_variable_tracking_icon.jpg' | relative_url }})

This allows the user to post process the user defined post variables defined in the post processor user routines. This is done by selecting the DLL file generated from the user routine, routine number (See Fig. 26.6.3.1.) in User defined variable tracking window and Clicking ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}) allows the user to select object and calculation type (See Fig. 26.6.13.2.) Clicking on ![]({{ '/assets/icons/post_icons/mo_flownet_track_data_button.jpg' | relative_url }}) will track the state variables. After tracking the variables, they will be available for display in state variables dialog under User group. (See Fig. 26.6.13.3.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_13_set_user_defined_variable_tracking/image001.jpg' | relative_url }})

User defined variables Library properties window

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_13_set_user_defined_variable_tracking/image002.jpg' | relative_url }})

User defined variables Tracking properties window

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_13_set_user_defined_variable_tracking/image003.jpg' | relative_url }})

User defined post variables accessing from State variables window

Once tracking the variables for particular DB is completed, it will generate the PDB in the problem directory, so in the next sessions of post processing user can select the existing PDB from the Tracking tab and then directly plot the user variables.  
The Post processor user routine is available in the standard installation location,  
C:\Program files\SFTC\DEFORM\v*_*\UserRoutine\PostProcessor\PC_pstusr23.f (where *_* is version number of deform) for PC. For more details on post processor user routines refer the [Chapter 56. User routine.](/docs/en/user_routines/56_user_routines_in_deform/56_user_routines_in_deform/)
