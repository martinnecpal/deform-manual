---
lang: en
title: "26.6.9. Point tracking"
---

# 26.6.9. Point tracking ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }})

  * Point selection Wizard

  * Point tracking Settings

**[2D, 3D]:** Point Tracking feature can be used to understand the flow of material, track defect and understand the state variable behavior at a point. In point tracking user can track more than 1000 points over the course of a simulation. In order to use point tracking first user has to select the points on the objects from graphics window using mouse left click at the intended locations (See Fig. 26.6.9.1. and Fig. 26.6.9.2.).

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image001.jpg' | relative_url }})

Point tracking points definition for 2D 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image002.jpg' | relative_url }})

Point tracking points definition for 3D 

  
Depending on the requirement user can set settings using ![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }}) button. User can set whether select points type are moving or fixed, saving file format and state variables that needs to be saved. (See Fig. 26.6.9.3.)

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image003.jpg' | relative_url }})

Point tracking settings window

Finally by clicking on ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}) button points are tracked for all DB steps and then state variable plot will be displayed along with the state variable graph for different points selected with reference to time as shown in Fig. 26.6.9.4. and Fig. 26.6.9.5.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image004.jpg' | relative_url }})

Point tracking graphs in graphics window for 2D

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image005.jpg' | relative_url }})

Point tracking graphs in graphics window for 3D

**Adding Points** : Points can be added to track by clicking in the intended location with the left mouse  
button when this button is selected.

**Deleting Points** : Points can be deleted by clicking the icon ![]({{ '/assets/icons/pre_icons/mo_delete_current_row_icon.jpg' | relative_url }}) (Delete the current row from the table) to delete a single row or by using icon ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}) (Delete all rows from the table) to delete all the input data in the Point tracking data window.

  
**Save the points to a file** ![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) : This saves the selected points to a file which can be loaded back into point tracking window at any time for same DB or into other DB’s for point tracking.

  
**Load the points to a file** ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}): Saved points can be loaded into the current object by loading the previously saved point tracking data file.

**Point selection Wizard**![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) : When user clicks on Point selection wizard it directs to “State variable between 2 points” window, where user can define start and end surface/points to generate points either in straight line or follow object boundary or in circular pattern for 3D. After defining points, using generate button points can be generated. After generating if we click ok, it directs to point tracking window where user can see generated points in the table and display window. Click on Track to start point tracking, point tracking graph will be plotted (See Fig. 26.6.9.6. and Fig. 26.6.9.7.). For more details refer [26.6.8. State varaible between 2 points](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_8_state_variables_between_2_points/)

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image006.jpg' | relative_url }})

Point selection wizard with State variables between 2 points options

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image007.jpg' | relative_url }})

Point tracking with Point selection wizard

**Point tracking Settings**![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }})

  * **Tracking :**

  * **Points Option: Moving points:** By selecting this radio button, points defined on the object will move along with material flow.

  * **Fixed points:** By selecting this radio button, points defined on the object will be stationary.

  * **Export:**

  * **Save result to file :** User can save the point tracking result in RST or CSV formats and results can be sorted by point or step by selecting respective check box. By default the results are saved in RST format, if we check the Excel friendly check box then results will be saved in excel friendly CSV format. Checking the Excel friendly check box will provide options to save all state variables or selected state variables from the list available in CSV format. Unchecking the “Save all” check box will activate the options to select state variables to save. User can select the location on the disk to save the point tracking results using browse button.

  * **Display:**

  * **Axis:** From V12.01**,** User have an option to select the X-axis output either Time or Stroke.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_9_point_tracking/image008.jpg' | relative_url }})

Point tracking setting option
