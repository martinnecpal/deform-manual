---
lang: en
title: "41.1. Report Generation"
---

# 41.1. Report Generation

41.1.1. Report

Report Hierarchy

41.1.2. Chapter

Chapter title

Operation range selection

41.1.3. Sections

  * Simulation Input summary

  * Metal Flow

  * Summary

  * Graph (Load-Stroke)

  * State Variable

  * Region of Interest

  * Coupons

  * Point Tracking

  * Flownet

  * Post user variables tracking

  * Custom

## Report

In Report, we can add multiple chapters by clicking on ![]({{ '/assets/icons/post_icons/mo_add_report_section_button.jpg' | relative_url }}) button and by double click on chapter name we can modify the chapter name (by default it will show Operation range ) as shown in Fig. 41.1.1.

Using Import report template to a file ![]({{ '/assets/icons/post_icons/mo_import_button.jpg' | relative_url }}) and Import report template to library****![]({{ '/assets/icons/post_icons/mo_import_form_library_button.jpg' | relative_url }}) options we can import saved (.DS) report template and using Export report template to file ![]({{ '/assets/icons/post_icons/mo_export_report_template_button.jpg' | relative_url }}) and Export report template to library ![]({{ '/assets/icons/post_icons/mo_export_template_to_librart_button.jpg' | relative_url }}) options we can save the report template. 

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image001.jpg' | relative_url }})

Adding Chapters to Report list

### Report Hierarchy

Report is split into Chapters and each Chapter will have Sections and every Section will have selected outputs like graphs, state variable plots etc., see Fig. 41.1.2.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image002.jpg' | relative_url }})

Report Object tree

## Chapter

Chapter contains Sections with various type of outputs such as point tracking, contour plot of state variables, graphs,.. etc and user can change the Chapter title, select operation range that can be added to report as shown in Fig. 41.1.3.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image003.jpg' | relative_url }})

Chapter page

### Chapter title

In chapter list field we can modify chapter name as required. Fig. 41.1.4. shows the Chapter title options available to define Chapter title.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image006.jpg' | relative_url }})

Chapter Title options

### Operation range selection

Operation range selection is available within a chapter, which enables operation-by-operation report generation. User can select the operations range for which report needs to be generated. If user wants to generate report for non successive operations then additional chapters needs to be created for respective operations.

## Sections

In Sections, select the required post tool check box to be added to report and we can notice that respective tools will be added in Object tree (See Fig. 41.1.3.).

Following tools are available for report generation,

  * Simulation Input summary

  * Metal Flow

  * Summary

  * Graph (Load-Stroke)

  * State Variable

  * Region of Interest

  * Coupons

  * Point Tracking

  * Flownet

  * Post user variables tracking

  * Custom

  * **Simulation input summary**

By Turning on Simulation input summary check box if we generate report, we can observe the Contents of each chapter, Summary summary of each operation and object/s data and each section output. Fig. 41.1.5. shows sample of report generated for Simulation input summary.

From v12.0.2., if user don't want the simulation summary in the report PDF file, then we need to turn off the "Simulation input summary" check box in Chapter page.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image004.jpg' | relative_url }}) ![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image005.jpg' | relative_url }})

Simulation summary in PDF Document file

  * **Metal Flow**

Metal flow in each operation can be added to report using Metal Flow section. In Metal flow page, we can select Start step, Middle (we can select upto 7 step) and End step as shown in Fig. 41.1.6. Metal flow displays deformation of the object without any state variable contour at the selected steps of operations. 

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image007.jpg' | relative_url }})

Metal Flow page

Under Controls page, we can select objects to be displayed in Metal Flow, Type of Viewport, Contact type display and PDF layout for Metal Flow output (See Fig. 41.1.7.). Also we can Export Node coordinates and Element connectivity data by checking Export Node coordinates and Element connectivity check box in Controls page. Also we can export the 2D (DXF format) or 3D (STL format) geometry at the last step by checking Geometry check box. Fig. 41.1.8. shows sample of report generated for metal flow.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image008.jpg' | relative_url }})

Metal Flow Controls page

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image009.jpg' | relative_url }})

Generated Report for Metal flow section

  * **Summary**

Summary plot of state variable can be added to report using ![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}) button and selecting the required state variable. We can also export the respective State variable Summary data by checking Export check box. When Export checkbox is turned on the selected Summary output will be saved into Report folder in .CSV format during report generation. (see Fig. 41.1.9.). Then for each selected state variable user need to select objects for which to generate state variable Min/max curves has to been generated in each state variable windows as shown in Fig. 41.1.10. Sample of report generated for Summary is as shown in Fig. 41.1.11.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image010.jpg' | relative_url }})

Summary Output

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image011.jpg' | relative_url }})

Object selection for respective state variable output

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image012.jpg' | relative_url }})

Generated Report for Summary section

  * **Graph (Load-Stroke)**

In Graph output page, Multiple x-y plots such as load-stroke, speed-time, stroke-energy, ..etc can be defined, using ![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}) button as shown in Fig. 41.1.12. We can also export the respective Load - Stroke data by checking Export check box. When Export checkbox is turned on the selected Summary output will be saved into Report folder in .CSV format during report generation. Then for each output type user need to select object for which graph has to be generated in Graph output page, Fig. 41.1.13. Sample of report generated for Graph is as shown in Fig. 41.1.14.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image013.jpg' | relative_url }})

Graph output plot selection

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image014.jpg' | relative_url }})

Object selection for Load Time Graph output

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image015.jpg' | relative_url }})

Generated Report for Graph section

  * **State Variable**

State variable contour plot can be added to report from State variable output. Depending on the requirement user can select the Start step, Middle steps (up to 7) and End step in State variable page to be included into report as shown in Fig. 41.1.15., contour plot will be generated for selected steps and added to report.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image016.jpg' | relative_url }})

State variable step selection page

In output page, user can select the State variable for which contour plot needs to be added into report using ![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}) variables button and we can also export the respective State variable data by checking Export check box as shown in Fig. 41.1.16.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image017.jpg' | relative_url }})

State variable output list

For each state variable, user can select the objects for which the contour plot has to be generated into report, viewport, Contour type, Contour range, Color bar type and PDF layout..3D model with contour plot can be included into pdf by turning on Include 3D Model (PDF) check box as shown in Fig. 41.1.17. Now 3D PDF output will be saved under Models folder for each output separately.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image018.jpg' | relative_url }})

Object and PDF layout selection for respective output variable window

PDF and PPT generated by report generation is shown below Fig. 41.1.18. to Fig. 41.1.20.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image019.jpg' | relative_url }})

Generated PDF of 9 saved step of an operation (PDF layout 9)

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image020.jpg' | relative_url }})

Generated 3D PDF for Operation 4

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image021.jpg' | relative_url }})

Generated PPT for Stress Effective State variable

  * **Region of Interest**

Region of Interest (ROI) is an arbitrary shape (2d or 3d) which defines an area from which system gathers information about state variables for selected object and displays Min and Max value for selected state variable.

In Region of Interest selection page, we can add regions using ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button. For the added region we can create geometry using primitives or we can import the geometry file using import options. (See Fig. 41.1.21.)

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image022.jpg' | relative_url }})

Region of Interest selection page

In Outputs page, we can add the required output state variable and under Region column we can select the region across which state variable data needs to be extracted from pull down menu list, see Fig. 41.1.22.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image023.jpg' | relative_url }})

Region of Interest output page

Report generated for coupons sections is shown below Fig. 41.1.23.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image024.jpg' | relative_url }})

Generated Region of Interest result

  * **Coupon**

Qualification of parts require cut-up evaluation of critical locations for microstructure and mechanical property response and industry needs to identify critical areas in the part based on forming and heat treatment modeling results. For those critical areas identified, we need to extract modeling state variables. Coupon capability in DEFORM can be used for this process.

In coupon selection page, add the coupon region to extract state variables data in the coupon region (See Fig. 41.1.24.).

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image025.jpg' | relative_url }})

Coupon selection page

In Coupon Output page, we can add the required output state variables for which data needs to be extracted. ( See Fig. 41.1.25.)

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image026.jpg' | relative_url }})

Coupon Output state variable selection

Report generated for coupons sections is shown below Fig. 41.1.26.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image028.jpg' | relative_url }})

Generated Coupon result in PDF

  * **Point Tracking**

User can add graphs to understand the behavior of a particular state variable at selected points using point tracking. In Point tracking selection page, select the step, select the points type, which could be Moving or Fixed and select points for point tracking in Define window as shown in Fig. 41.1.27.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image027.jpg' | relative_url }})

Point tracking selection page

In Point tracking output page, select the state variable for which a graph needs to be plotted (See Fig. 41.1.28.) and check Export check box if point tracking state variable data need to be exported.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image029.jpg' | relative_url }})

Point tracking output state variable selection

For each output state variable page, user can select the objects to be included for point tracking and also can select whether to Plot contour + Graph or Graph plot or Contour only from Display options as shown in Fig. 41.1.29.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image030.jpg' | relative_url }})

Output State variable window

The generated PDF report for Point tracking section is as shown in Fig. 41.1.30.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image031.jpg' | relative_url }})

Shows sample of the generated PDF report for Point tracking with Contour+ Graph plot 

  * **Flownet**

In order to include flow net of an object into report, from Flownet page select the step at which flownet to be added into report, currently Start step or End step or Start and End Step are available and they can be used by turning on respective check box, see Fig. 41.1.31.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image032.jpg' | relative_url }})

Flownet page

In Object selection page select object for which Flownet needs to be plotted, select pattern type and configure the pattern parameters as show in Fig. 41.1.32. Sample of Flownet from a generated report is shown in Fig. 41.1.33.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image033.jpg' | relative_url }})

Configuring Flownet pattern

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image034.jpg' | relative_url }})

Generated PPT file for simple operation

  * **Post user variables tracking**

This allows the user to generate the report for the user defined post variables defined in the post processor user routines (See Fig. 41.1.34.). Depending on the requirement user can select the Start step, Middle steps (up to 7) and End step in State variable page to be included into report.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image035.jpg' | relative_url }})

Post user variable page

In Library page, select the DLL file generated from the user routine in Library field and select the routine number from routine pull down list. (See Fig. 41.1.35.)

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image036.jpg' | relative_url }})

Library and Routine selection page

In Tracking page, select Tracking variables radio button in Method type if no PDB is available, then select Calculation type as Nodes or Elements type and then click on Track data, Once tracking the variables for particular DB is completed a PDB file will be generated in the problem directory, so in the next sessions of post processing user can select the existing PDB from the Tracking tab and then directly plot the user variables. (See Fig. 41.1.36.)

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image037.jpg' | relative_url }})

Tracking data page

In Output page, add State variables by selecting State variable type as Post user var in pull down list and select state variables in component column and we can also export the respective State variable data by checking Export check box as show in Fig. 41.1.37. For each state variable user can select object, viewport, Contour type, Contour range, PDF layout and Color bar type as shown in Fig. 41.1.38.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image038.jpg' | relative_url }})

Output selection page

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image039.jpg' | relative_url }})

Objects and Viewport selection page

  * **Custom**

In custom page, we can save the current object display which is display window on custom page will be saved in report.

**Related Topics:**

[41\. Introduction ot Report Generation](/docs/en/operation_templates/41_report_generation/41_introduction_to_report_generation/)

[28.1. Editing Chapters](/docs/en/post_processor/28_report_generation/28_1_editing_chapters/)

[28\. Report Generation in Post-Processor](/docs/en/post_processor/28_report_generation/28_report_generation/)

[Report Generation lab in MO](/docs/en/labs/report_generation_lab/report_generation_lab_in_mo/)
