---
lang: sk
title: "24. Introduction to Post Processor"
---

# 24\. Introduction to Post Processor

The DEFORM Post-Processor is used to review the simulation results. This is an integrated post processor provide with new user friendly GUI with the most of the existing post-processing functions and new features.

DEFORM Post-Processor provides an environment with new features for the user to generate 3D PDF reports of simulation results,[ coupon data extraction](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_11_coupon_data_extraction/), interpret results across database using [PIP](../26_post_processing_tools_and_controls/26_1_file_operations_in_post_processor.htm#26_1_1_Working_with_DB_in_PIP_mode), plot results in region of interest, [CA microstructure modelling](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_10_ca_model_setup/) and post processing [report generation](/docs/sk/post_processor/28_report_generation/28_report_generation/) (.pdf and .ppt file formats) with pre defined user settings.

Post-Processor with a variety of features and graphics allows engineers to check the model results and present them in a way to understand the model results in an efficient manner. This section gives brief details of the system and the available features.

With every release the system is being enhanced to meet the industry requirement and specific user demands.

Information which is available from the post-processor includes:

  * Deformed geometry, including tool movements and deformed mesh at each saved step.

  * [Contour plots](../26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_3_state_variables.htm#Display_options): Line and shaded contours display the distribution of any state variables, including stress, strain, temperature, damage and others.

  * [Vector plots](../26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_3_state_variables.htm#Display_options): Displacement and velocity vectors indicate magnitude and direction of displacement or velocity for every node at each step throughout the process.

  * Graphs of key variables such as press loads, volumes, temperature, atom content, hardness and point tracked state variables.

  * [Point tracking](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_9_point_tracking/) to show how material moves and plots graphs of state variables behavior at these points.

  * [Flow net](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/) showing material flow patterns on a uniform grid. Generally a very good predictor of grain flow patterns in the finished part.

  * A [histogram](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_3_state_variables/) plot of any state variable can be made to view the distribution of any given state variable throughout a body.

  * [3D View Mode](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_20_3d_setup/) can be used to visualize 2D in 3D either by revolving or extruding.

  * Interactive Slicing of 3D object to understand internal features and state variable distribution.

  * [Coupon data extraction](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_11_coupon_data_extraction/) for cut-up evaluation of critical locations for microstructure and mechanical property response.

  * Results can be plot in region of interest by defining an arbitrary shape, used to get min/max state variable values from specific part of an object.

  * Interactive post processing results can be brought to the reports (.pdf and .ppt) files with pre defined user settings.

  * Cellular Automata (CA) models are synchronous algorithms that describe the discrete spatial and temporal evolution of complex systems by applying local (or mesoscopic, mid-range) deterministic or probabilistic transformation rules to lattice cells with local connectivity to predict grain size.

  * [Multi viewports](../26_post_processing_tools_and_controls/26_2_handeling_viewports_and_windows_iin_post_processor.htm#Multi_Viewports), [Database comparison](../26_post_processing_tools_and_controls/26_2_handeling_viewports_and_windows_iin_post_processor.htm#Fig_26_2_3_DB_comparison), Link/Sync options for Multiple window display are newly added and these options can be used for viewing multiple DB’s at a time in NG post.

State variables, geometry and image data can also be extracted in a number of neutral formats for use with other programs.

## Opening DB for Post-processing

When the problem folder contains the database then the ![]({{ '/assets/icons/pre_icons/2d_3d_post_label.jpg' | relative_url }}) option will be shown in GUI main. To open the simulated database in Post processor from GUI Main, we need to click on![]({{ '/assets/icons/pre_icons/2d_3d_post_label.jpg' | relative_url }})under Post-Processor or by clicking on ![]({{ '/assets/icons/pre_icons/2d_3d_post_icon.jpg' | relative_url }}) in tool bar list as shown in Fig. 24.1.

![]({{ '/assets/images/post_processor/24_introduction_to_post_processor/image001.jpg' | relative_url }})

Opening Post-processor from GUI main

**Related Topics:**

[25\. Post Processor Layout](/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/)

[26\. Post Processor Features](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_post_processor_features/)

[28\. Report Generation](/docs/sk/post_processor/28_report_generation/28_report_generation/)
