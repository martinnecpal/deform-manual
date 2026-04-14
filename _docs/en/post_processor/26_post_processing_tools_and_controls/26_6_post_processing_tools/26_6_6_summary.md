---
lang: en
title: "26.6.6. Summary"
---

# 26.6.6. Summary

[2D, 3D]: In simulation summary window, the step can be selected from the step list and then the object can be selected using the pull down arrow button in the object field. After changing the object, if the step changes object does not change. Certain characteristic data, such as press loads, primary die velocities and maximum and minimum values of state variables are stored for every simulation step, whether data is stored for every step or not in the DB. This summary data vs time graphs for all the saved steps can be viewed in the graphics window by selecting the state variable in the list and clicking on button at the bottom of the window. (See Fig. 26.6.6.1. and [Fig. 26.6.6.2.](26_6_2_object_elements.htm#Fig_26_6_2_2_Object_Elements_window_for_3D)).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_6_summary/image001.jpg' | relative_url }})

State variables summary window

Clicking on a point on the graph will load the nearest saved step from the database into display as shown in [Fig. 26.6.6.2.](26_6_2_object_elements.htm#Fig_26_6_2_2_Object_Elements_window_for_3D)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_6_summary/image002.jpg' | relative_url }})

Temperature state variable summary graph

The step list in summary window can be used to select the step. When Load Step check box is checked and step is selected from step list, then the selected step will be loaded into the graphics window and state variable values at that step into summary window. It also displays the simulation information like simulation number, step number, time, primary die stroke, mesh number (changes when there is a remesh), fold occurrence, dimension of the operation and version number.

State variables are grouped under different categories which are, ![]({{ '/assets/icons/post_icons/mo_analysis_icon.jpg' | relative_url }}) (General), ![]({{ '/assets/icons/post_icons/mo_deformation_icon.jpg' | relative_url }}) (Deformation), ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) (Thermal), ![]({{ '/assets/icons/post_icons/mo_heating_sv_icon.jpg' | relative_url }})(Heating), ![]({{ '/assets/icons/post_icons/mo_prop_sv_icon.jpg' | relative_url }}) (Heat treat) and ![]({{ '/assets/icons/post_icons/mo_user_sv_icon.jpg' | relative_url }})(User) and these can be accessed using icons as sown in [Fig. 26.6.6.2.](26_6_2_object_elements.htm#Fig_26_6_2_2_Object_Elements_window_for_3D)

Using ![]({{ '/assets/icons/post_icons/mo_show_all_sv_button.jpg' | relative_url }}) (Show all) icon all the state variable groups can be displayed. ![]({{ '/assets/icons/post_icons/mo_clear_sv_icon.jpg' | relative_url }})(Clear) icon is used to clear all the state variables groups selection.

By double clicking on the state variable value in the summary window user can copy the Min and Max value at that step, user can also export the summary graph data plotted on the graphics window using right click option Export graph data. Graph properties like, titles and its font, values range, number of decimals and display style and legend on/off can also be changed using right click option Set graph properties.

For 3D problem if there is any fold it can be located by using the Locate fold button at the bottom of the window, it will turn on the fold display automatically in the graphics window for the selected object.
