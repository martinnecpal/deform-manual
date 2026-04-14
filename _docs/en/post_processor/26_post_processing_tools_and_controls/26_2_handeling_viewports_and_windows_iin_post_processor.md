---
lang: en
title: "26.2. Handling Viewport and Windows in Post-Processor"
---

# 26.2. Handling Viewport and Windows in Post-Processor

26.2.1. Viewport menu

26.2.2. Windows menu

## Viewport menu

Fig. 26.2.1. shows the Post-processor Viewport menu option, user has plot Multi-viewport, Database comparison for selected database, Link database, Link step, Sync view, Sync state variable and sync X-Y plot option with Database comparison, Refresh, Fit View, View back, Iso view, Screen upward, Load Viewport, Save viewport and Lighting options. 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_2_viewports/image001.jpg' | relative_url }})

Post-processor Viewport menu 

  * **Multi Viewports** ![]({{ '/assets/icons/post_icons/mo_multi_viewport_icon.jpg' | relative_url }}): By default the Display window is in single viewport mode but this can be divided into maximum of 8 viewports. This option helps the user to compare different state variables contour, graphs of the same DB at a time. (See Fig. 26.2.2.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_2_viewports/image002.jpg' | relative_url }})

Multiple view port

  * **Link Database** ![]({{ '/assets/icons/post_icons/mo_link_database_icon.jpg' | relative_url }}): 

**Link on** : shows same step in multiple databases

**Link off** : shows different step in multiple databases

  * **Link Step** ![]({{ '/assets/icons/post_icons/mo_link_steps_icon.jpg' | relative_url }}):

**Link Database** : Link on : shows same step in multiple databases

**Link off** : shows different step in multiple databases

  * **Sync view** ![]({{ '/assets/icons/post_icons/mo_sync_view_icon.jpg' | relative_url }}):

**Sync on** : use (sync) same viewport (pan/zoom/rotate), object selection in multiple viewports

**Sync off** : use independent viewport (pan/zoom/rotate) , object selection in multiple viewports

  * **Sync state variable** ![]({{ '/assets/icons/post_icons/mo_sync_state_variable_icon.jpg' | relative_url }}):

**Sync on** : use (sync) same state variable in multiple viewports

**Sync off** : use independent state variable in multiple viewports

  * **Sync X-Y Plot![]({{ '/assets/icons/post_icons/mo_sync_x-y_plot_icon.jpg' | relative_url }})** :

**Sync on** : use (sync) same action in multiple viewports

**Sync off** : use independent action in multiple viewports.

Actions will include slicing / load-stroke graph / summary graph.

  * **Database compassion** ![]({{ '/assets/icons/post_icons/mo_database_comparison_icon.jpg' | relative_url }}): It provides tools to link different databases based on link range, link method and link type for comparison. (See Fig. 26.2.3.).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_2_viewports/image003.jpg' | relative_url }})

DB comparison

**Relative link method** : Link is done using normalized step, stroke and time within the selected range.

  * **Refresh (F5)** ![]({{ '/assets/icons/pre_icons/mo_refresh_icon.jpg' | relative_url }}) : The refresh icon redraws the screen, removing any measurement marks, and updating any changes made to the color pallet.

  * **Fit View (F3) :** Fits all displayed objects or graphs inside the current viewport.

  * **View back (F4) :** Resets objects to the previously viewed display position.

  * **Iso view** ![]({{ '/assets/icons/pre_icons/mo_iso_view_icon.jpg' | relative_url }}) : This will show the isometric view of the current viewport. This option is not available for 2D systems. This options are not available in 2D mode, as this are not applicable for 2D mode.

  * **Screen upward** : ****[3D]: This option shows the isometric view in 3D, such that the selected axis will be pointing in the upward direction. For example, if the user selects positive Z-axis from the screen upward option as shown in Fig. 26.2.4. and then select isometric view option, Z-axis will be pointing upwards in the isometric view. This is not applicable for 2D mode.

  
![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image005.jpg' | relative_url }})

Screen upward viewport menu options

  * ******Viewport Menu****![]({{ '/assets/icons/pre_icons/mo_plus_x_view_icon.jpg' | relative_url }}) ,**![]({{ '/assets/icons/pre_icons/mo_minus_x_view_icon.jpg' | relative_url }}),![]({{ '/assets/icons/pre_icons/mo_plus_y_view_icon.jpg' | relative_url }}) ,![]({{ '/assets/icons/pre_icons/mo_minus_y_view_icon.jpg' | relative_url }}),![]({{ '/assets/icons/pre_icons/mo_plus_z_icon.jpg' | relative_url }}),![]({{ '/assets/icons/pre_icons/mo_minus_z_icon.jpg' | relative_url }}) : ****The below Fig. 26.2.5. shows the Viewport menu options using these options or icons in tool bar user can refresh or fit the view, switch to Iso or any directional view, set the upward axis, save and load the viewports and viewport lighting settings can be varied. 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image011.jpg' | relative_url }})

Different view selection options

  * **Load and Save viewport :** The user can move or change the views of the geometries by using display tools such as pan, dynamic zoom and box zoom in the display window. These views can be saved using save option provided under viewport tab as shown in Fig. 26.2.6.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image013.jpg' | relative_url }})

Save view port Menu options

If the view is saved as a local viewport, this view gets saved for the current working project only and can be viewed using load option as shown in Fig. 26.2.7. If the view is saved as a global viewport the set views becomes the default views for any project, for global viewports to get activated for the projects, the user has to exit from current project. The user can copy global viewports as a local viewports under load option and local viewports to global viewports under save option.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image012.jpg' | relative_url }})

Load view port Menu options

  * **Lighting** : This allows the user to change the brightness and color of the graphics window lighting, can also add more light switches and control its positions as shown in Fig. 26.2.8., Fig. 26.2.9. and Fig. 26.2.10.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image014.jpg' | relative_url }})

Lighting General properties window

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image015.jpg' | relative_url }})

Lighting Settings properties window

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image016.jpg' | relative_url }})

Light Advanced Properties window

Refer Chapter[ 8\. Pre-Processor Layout](/docs/en/pre_processor/8_pre_processor_layout/8_pre-processor_layout/) section [Set Lighting Property](../../pre_processor/8_pre_processor_layout/8_pre-processor_layout.htm#Set_Lighting_Property).

## Windows Menu

Fig. 26.2.11. shows the Post-Processor Windows menu, Detach, Testify, Tile, Tile Horizontally and Tile Vertically options are available under Windows list. THis options will works when we open two or more databases in Post processor.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_2_viewports/image004.jpg' | relative_url }})

Post-processor Windows menu 

  * **Detach** : When Detach option is selected under Windows menu, display window of each databases list will be displayed independently and not fitted inside the display window.

  * **Testify** : When Testify option is selected under Windows menu, display window of each databases list will be shown with tab list.

  * **Tile** : When Tile option is selected under Windows menu, display window of each databases will be shown in tile view.

  * **Tile Horizontally** : When Tile Horizontally option is selected under Windows menu, display window of each databases will be arranged horizontally.

  * **T******ile** Vertically**: When Tile Horizontally option is selected under Windows menu, display window of each databases will be arranged vertically.

**Related Topics:**

[8\. Pre-Processor Layout](/docs/en/pre_processor/8_pre_processor_layout/8_pre-processor_layout/)
