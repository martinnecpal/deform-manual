---
lang: sk
title: "26.6.23. Presentation Editor"
---

# 26.6.23. Presentation Editor and Presentation Player

26.6.23.1. Presentation Editor

26.6.23.1.1.Launching the Presentation Editor from Post

26.6.23.1.2. Presentation Editor Main View

26.6.23.1.3. Frames tab

26.6.23.1.4. Quick start tab

26.6.23.1.5. Export tab

26.6.23.2. Presentation Player

26.6.23.2.1. Presentation settings

26.6.23.2.2. Presentation play options

## Presentation Editor

### Launching the Presentation Editor from Post

In QT4 GUI Main, we can open the Presentation Editor using the ![]({{ '/assets/icons/pre_icons/mo_presentation_editor_link.jpg' | relative_url }}) link and Presentation Player using the ![]({{ '/assets/icons/pre_icons/mo_presentation_player_link.jpg' | relative_url }})link.

After a presentation file (.pre) has been created in NG post, "Edit in Presentation Editor" ![]({{ '/assets/icons/pre_icons/mo_presentation_editor_icon.jpg' | relative_url }}) and “Play in Presentation Player” ![]({{ '/assets/icons/pre_icons/mo_presentation_player_icon.jpg' | relative_url }}) buttons will be enabled. When we click on the ![]({{ '/assets/icons/pre_icons/mo_presentation_editor_icon.jpg' | relative_url }}) button it will launch the Presentation Editor (see Fig. 26.6.23.3..). Clicking on![]({{ '/assets/icons/pre_icons/mo_presentation_player_icon.jpg' | relative_url }}) button will launch the Presentation player (see Fig. 26.6.23.10.) to play the animation that was created. We can also launch the Presentation editor from Windows Start menu by selecting "DEFORM Presentation Editor v*" (see Fig. 26.6.23.2.).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_23_presentation_editor/image0001.jpg' | relative_url }})

Launching Presentation editor from Animation setup page 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_23_presentation_editor/image0002.jpg' | relative_url }})

Launching Presentation editor Windows Start menu 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_23_presentation_editor/image0003.jpg' | relative_url }})

Presentation Editor UI

### Presentation Editor Main view

The Presentation Editor is used to create and edit presentation files (.pre) and quick start files (.qst). Presentation files contain information for displaying images in an animation. Quick start files contain information about one or more presentation files.  
The main view allows for adding, removing, and reordering of frames (see Fig. 26.6.23.4.). The top row of buttons includes options for creating, opening, saving and playing presentations.

**New presentation** (![]({{ '/assets/icons/post_icons/mo_new_file_button.jpg' | relative_url }})): It creates a new presentation or quick start file.

**Open presentation** ( ![]({{ '/assets/icons/post_icons/mo_import_button.jpg' | relative_url }})): It opens an existing presentation or quick start file.

**Import presentation** (![]({{ '/assets/icons/post_icons/mo_import_icon.jpg' | relative_url }}) ): It adds an existing presentation to the open quick start file. If a quick start file isn’t open when a presentation is imported, the Presentation Editor automatically creates a quick start file, which acts as a container for the presentation files.

**Recently opened presentations** (![]({{ '/assets/icons/post_icons/presentation_editor_recently opened_icon.jpg' | relative_url }}) ): It displays a list of previously opened files.

If a .qst file is loaded, its name will be displayed next to the Quick start file field and active presentation file is displayed in Active presentation file field. In main view, all the presentation files from quick start file and their associated frames will be displayed. Frames can be selected and acted upon using either the context menu or the buttons below main view.

**Save presentation file**(![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }})): It will save the active presentation file along with the settings into a presentation file.

**Save quick start as**(![]({{ '/assets/icons/post_icons/presentation_editor_save_qst_as_icon.jpg' | relative_url }})): It will save the settings from the quick start tab and the presentation files along with the settings into .qst file.

The following buttons can be used to modify the presentation file,

![]({{ '/assets/icons/post_icons/presentation_editor_add_icon.jpg' | relative_url }}) \- add new frame to the active animation file. 

![]({{ '/assets/icons/post_icons/presentation_editor_remove_icon.jpg' | relative_url }}) \- remove selected frames from the active animation file. 

![]({{ '/assets/icons/post_icons/presentation_editor_frame_up_icon.jpg' | relative_url }}) \- move selected frames up in an active animation file. 

![]({{ '/assets/icons/post_icons/presentation_editor_frame_down_icon.jpg' | relative_url }}) \- move selected frames down in an active animation file. 

![]({{ '/assets/icons/post_icons/presentation_editor_frame_top_icon.jpg' | relative_url }}) \- move selected frames to the top of an active animation file.

![]({{ '/assets/icons/post_icons/presentation_editor_frame_bottom_icon.jpg' | relative_url }}) \- move selected frames to the bottom of an active animation file. 

When editing a Quick Start file, 

![]({{ '/assets/icons/post_icons/presentation_editor_frame_qst_up_icon.jpg' | relative_url }}) \- presentation files can be moved up. 

![]({{ '/assets/icons/post_icons/presentation_editor_frame_qst_down_icon.jpg' | relative_url }}) \- presentation files can be moved down. 

![]({{ '/assets/icons/post_icons/presentation_editor_total_icon.jpg' | relative_url }}) \- will display the total time of all animations in Quick Start file.

![]({{ '/assets/icons/post_icons/presentation_editor_seconds_button.jpg' | relative_url }}) \- animation time unit can be changed between seconds and milliseconds using the drop-down menu.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_23_presentation_editor/image0004.jpg' | relative_url }})

Presentation editor Main page

### Frames tab

The **Frames tab** is used to change the delay of frames (see Fig. 26.6.23.5.). It shows a preview and details of the selected frame.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_23_presentation_editor/image0005.jpg' | relative_url }})

Frames tab

  
**Delay calculator**( ![]({{ '/assets/icons/post_icons/presentation_editor_delay_calculator_button.jpg' | relative_url }})): The **Delay calculator** button opens the Delay calculator dialog as shown in Fig. 26.6.23.6. The calculator allows to enter delays in fractions of a seconds. The delay is converted to decimal when leaving the dialog.

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_23_presentation_editor/image0006.jpg' | relative_url }})

Delay Calculator window

  
**Delay wizard** ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) : The **Delay wizard** button opens the Delay wizard dialog as shown in Fig. 26.6.23.7. This wizard allows to adjust the delay before start and delay after end frame as well as the delay for each frame in-between. Adjusting the total play time will dynamically adjust the delay between steps.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_23_presentation_editor/image0007.jpg' | relative_url }})

Delay wizard window

### Quick start tab

The Quick Start tab has options for editing quick start files as shown in Fig. 26.6.23.8. These options affect how the quick start file will be displayed in the DEFORM Presentation Player. Each presentation file in the quick start file is displayed as a thumbnail. 

  * The **Background color** is the color that fills the screen behind the thumbnails. 

  * The **Border color** and border size define the border around each thumbnail. 

  * The **Description color** is the color used for the text descriptions below each thumbnail.

  * The **Thumbnail display size** can be defined as either a dynamic size or a specific width in pixels. A dynamic size (small, medium and large) will use an appropriate size regardless of the screen resolution. User can also set custom size.

  * The **Presentation looping** option defines how many times the presentation will loop when playing it.

  * The **Font** options define how the description below the thumbnails will be displayed.

  * The **Presentation file** **settings** include options that are defined for each presentation file. Select an active presentation here to define its settings.

  * The **Description** is the text that shows below each thumbnail.

  * The **Presentation thumbnail** is the frame in the presentation that will be used as the thumbnail. User can select any frame from the active presentation or by importing the image to use as its thumbnail.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_23_presentation_editor/image0008.jpg' | relative_url }})

Quick Start tab

### Export tab

The**Export tab** has similar options to the Export tab in Animation Setup.

In **Export** tab, user can export the animation as PowerPoint or Video file as shown in Fig. 26.6.23.9.

**Output Directory** : User can select the directory to which the files need to be exported.

**Video File** : User should turn on Video file check box to export the video file. User can define the video size and format to export. Video formats supported are WMV (Version 9) and MP4 (H.264). The output file name for video file can be set in Output file name field.

**MS PowerPoint** : User should turn on PPT file check box to export PowerPoint file. The PowerPoint file can be exported as new or append to existing file. Each frame can be exported as separate slide when Multiple slides option is chosen, or all frames can be exported to a single slide when One slide option is chosen. Template for PowerPoint file can be chosen using ![]({{ '/assets/icons/pre_icons/mo_browse_button.jpg' | relative_url }}) button next to Template field. The output file name for PowerPoint file can be set in Output file name field.

Clicking the ![]({{ '/assets/icons/post_icons/mo_export_button.jpg' | relative_url }}) button will generate the files specified.

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_23_presentation_editor/image0009.jpg' | relative_url }})

Export tab

## Presentation Player

The Presentation Player is used to playback presentation files (.pre) and quick start files (.qst), see Fig. 26.6.23.10.

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_23_presentation_editor/image0010.jpg' | relative_url }})

Presentation Player

![]({{ '/assets/icons/post_icons/mo_import_button.jpg' | relative_url }}) \- Open Presentation or quick start files.  
![]({{ '/assets/icons/post_icons/presentation_editor_recently opened_icon.jpg' | relative_url }}) \- Open from recently opened files.  
![]({{ '/assets/icons/post_icons/mo_play_button.jpg' | relative_url }}) \- Loaded presentations and quick start files can be played with “Play presentation”.

### Presentation settings

The Presentation settings button (![]({{ '/assets/icons/post_icons/presentation_editor_settings icon.jpg' | relative_url }})) opens the Presentation settings dialog as shown in Fig. 26.6.23.11.

The **Playback icon size** settings sets the size of the onscreen playback controls. The sizes are dynamic based on the screen resolution.

When a frame in a presentation has a lower resolution than the screen, how it is displayed is in the “**If image is lower resolution than the screen** ” option. For example, if the frame is 640x480 and the screen is 1920x1080, if the “Display image at actual size” option is selected, the frame will be shown at 640x480 in the middle of the screen. If the “Fit image to screen size” option is selected, the frame will be scaled to a horizontal resolution of 1080 pixels; the frame will maintain its original aspect ratio.

The **Playback controls** sets whether the onscreen playback controls should display on the top or bottom of the screen.

The **Loop presentation** continuously option allows for overriding the playback settings set in the quick start file.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_23_presentation_editor/image0011.jpg' | relative_url }})

Presentation settings

### Presentation play options

When displaying a quick start file, a thumbnail for each presentation file will be displayed as shown in Fig. 26.6.23.12. Clicking on a thumbnail will open the presentation file for playback as shown in Fig. 26.6.23.13.  
**Play all button**( ![]({{ '/assets/icons/post_icons/mo_play_button.jpg' | relative_url }})) (space key): It will play back all the included presentations in order.  
**Close quick start button**( ![]({{ '/assets/icons/post_icons/presentation_editor_close_presentation_icon.jpg' | relative_url }})) (escape key): It closes the quick start screen and returns to the main screen.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_23_presentation_editor/image0012.jpg' | relative_url }})

Player showing quick start file

  
When playing a presentation file, the below icons will be displayed. 

**Play backwards button** (![]({{ '/assets/icons/post_icons/mo_play_backward_icon.jpg' | relative_url }}) ) (shift + space key): It plays the presentation in reverse order.

**Play button** ( ![]({{ '/assets/icons/post_icons/mo_play_button.jpg' | relative_url }})) (space key): It plays the presentation in order. 

**Stop button** (![]({{ '/assets/icons/post_icons/mo_stop_button_2.jpg' | relative_url }})) (space key): It stops playback and remains on the current frame. The space key will toggle between playing forward and stopping.

**First slide** (![]({{ '/assets/icons/post_icons/mo_first_step_icon.jpg' | relative_url }}) ) (home key): It jumps to the first frame of the presentation.

**Last slide buttons** (![]({{ '/assets/icons/post_icons/mo_last step_icon.jpg' | relative_url }}) ) (end key): It jumps to the last frame of the presentation.

**Previous slide** (![]({{ '/assets/icons/post_icons/mo_prev_oprn_icon.jpg' | relative_url }})) (left arrow key): It jumps to the previous slide.

**Next slide buttons**(![]({{ '/assets/icons/post_icons/mo_next_oprn_icon.jpg' | relative_url }}) ) (right arrow key): It jumps to the next slide.

**Previous presentation** (![]({{ '/assets/icons/post_icons/mo_prevoius_step_icon.jpg' | relative_url }})) (page up key): It will jump to the previous presentation. This button is only active when all presentations are played in a quick start file. 

**Next presentation buttons** (![]({{ '/assets/icons/post_icons/mo_next_step_icon.jpg' | relative_url }})) (page down key): It will jump to the next presentation. This button is only active when all presentations are played in a quick start file. 

**Close presentation button** (![]({{ '/assets/icons/post_icons/presentation_editor_close_presentation_icon.jpg' | relative_url }}) ) (escape key): It will close the presentation screen and return to the main screen as shown in Fig. 26.6.23.12. If a presentation is playing when the escape key is hit, the presentation will stop playing.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_23_presentation_editor/image0013.jpg' | relative_url }})

Player showing presentation file
