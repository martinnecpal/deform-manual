---
lang: en
title: "28. Report Generation"
---

# 28\. Report Generation

28.1. Chapter

28.2. Sections

28.2.1. Simulation input summary

28.2.2. Metal flow

28.2.3.Summary

28.2.4. Graph (Load-Stroke)

28.2.5. State Variable

28.2.6. Region of Interest

28.2.7. Coupons

28.2.8. Point Tracking

28.2.9. Flownet

28.2.10. Post user variables tracking

28.2.11. Custom

Generating Report

In Report tab we can add multiple chapters by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and by double click on chapter name we can modify the chapter name (by default it will show Database name) as shown in Fig. 28.1.

![]({{ '/assets/images/post_processor/28_report_generation/image001.jpg' | relative_url }})

Adding Chapters to Report list

**Report Hierarchy:**

Report is split into Chapters and each Chapter will have Sections and every Section will have selected outputs like graphs, state variable plots etc., as shown in Fig. 28.2.

![]({{ '/assets/images/post_processor/28_report_generation/image002.jpg' | relative_url }})

Report Object tree

## Chapter

Chapter contains Sections with various type of outputs such as point tracking, contour plot of state variables, graphs,.. etc and user can select operation range that can be added to report as shown in Fig. 28.3. For more information related to Editing chapter Refer [28.2. Editing Chapters](/docs/en/post_processor/28_report_generation/28_1_editing_chapters/).

![]({{ '/assets/images/post_processor/28_report_generation/image003.jpg' | relative_url }})

Chapter page

### Database selection

Under Database selection list we can select database required to generate report.

### Chapter title

Under chapter list we can modify chapter name as required.

### Operation range selection

Operation range selection is available within a chapter, which enables operation-by-operation report generation. User can select the operations range for which report needs to be generated. If user wants to generate report for non successive operations then additional chapters needs to be created for respective operations.

## Sections

In Sections, select the required post tool check box to be added to report and we can notice that respective tools will be added in Object tree. (See Fig. 28.3.)

Following tools are available for report generation,

  * Simulation input summary

  * Metal flow

  * Summary

  * Graph (Load-Stroke)

  * State Variable

  * Region of Interest

  * Coupons

  * Point Tracking

  * Flownet

  * Post user variables tracking

  * Custom

### **Simulation input summary**

By Turning on Simulation input summary check box if we generate report, we can observe the Contents of each chapter, Summary summary of each operation and object/s data and each section output. Fig. 28.4. shows sample of report generated for Simulation input summary.

From v12.0.2., if user don't want the simulation summary in the report PDF file, then we need to turn off the "Simulation input summary" check box in Chapter page.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image004.jpg' | relative_url }}) ![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image005.jpg' | relative_url }})

Simulation summary in PDF Document file

### Metal Flow

Metal flow in each operation can be added to report using Metal Flow section. In Metal flow page, we can select Start, middle (we can select upto 7 step) and end step as shown in Fig. 28.5. Metal flow displays deformation of the object without any state variable contour at the selected steps of operations. We can Export Node coordinates and Element connectivity data by checking Export Node coordinates and Element connectivity check box. Also we can export the 2D (DXF format) or 3D (STL format) geometry at the last step by checking Geometry check box. Fig. 28.6. shows sample of report generated for metal flow.

![]({{ '/assets/images/post_processor/28_report_generation/image004.jpg' | relative_url }})

Metal Flow page

![]({{ '/assets/images/post_processor/28_report_generation/image005.jpg' | relative_url }})

Generated Report for Metal flow section

### Summary

Summary plot of state variable can be added to report using ![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}) button and selecting the required state variable (as shown in Fig. 28.7.). We can also export the respective State variable Summary data by checking Export check box. When Export checkbox is turned on the selected Summary output will be saved into Report folder in .CSV format during report generation. The selected state variable Min/max curves will be generated for the selected object and operation range as shown in Fig. 28.8.

![]({{ '/assets/images/post_processor/28_report_generation/image006.jpg' | relative_url }})

Summary Output

![]({{ '/assets/images/post_processor/28_report_generation/image007.jpg' | relative_url }})

Preview of selected state variable

### Graph (load-Stroke)

In Graph output page, Multiple x-y plots such as load-stroke, speed-time, stroke-energy, ..etc can be defined, using ![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}) button as shown in Fig. 28.9. We can also export the respective Load - Stroke data by checking Export check box. When Export checkbox is turned on the selected Summary output will be saved into Report folder in .CSV format during report generation. Respective graph will be generated for the selected object and operation range, Fig. 28.10. shows load-stroke plotted.

![]({{ '/assets/images/post_processor/28_report_generation/image008.jpg' | relative_url }})

Graph output plot selection

![]({{ '/assets/images/post_processor/28_report_generation/image009.jpg' | relative_url }})

Preview of Load Stroke Graph output

### State Variable

State variable contour plot can be added to report from State variable output. Depending on the requirement user can select the Start step, Middle steps (up to 7) and End step in State variable page to be included into report as shown in Fig. 28.11. , contour plot will be generated for selected steps and added to report.

![]({{ '/assets/images/post_processor/28_report_generation/image010.jpg' | relative_url }})

State variable step selection page

In output page, user can select the State variable for which contour plot needs to be added into report using ![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}) variables button and we can also export the respective State variable data by checking Export check box as shown in Fig. 28.12., 

![]({{ '/assets/images/post_processor/28_report_generation/image011.jpg' | relative_url }})

State variable output list

For each state variable, user can select the objects for which the contour plot has to be generated into report, viewport type, Contour type, Contour range and Color bar type. A 3D model with contour plot can be included into pdf by turning on Include 3D Model (PDF) check box as shown in Fig. 28.13. Generated. Under Models folder 3D PDF file for each state variable will be generated.

![]({{ '/assets/images/post_processor/28_report_generation/image012.jpg' | relative_url }})

Object and Viewport selection for respective output variable window

PDF and PPT generated by report generation is shown below Fig. 28.14. to Fig. 26.16.

![]({{ '/assets/images/post_processor/28_report_generation/image013.jpg' | relative_url }})

Generated PDF of 9 saved step of an operation (as multiple images)

![]({{ '/assets/images/post_processor/28_report_generation/image014.jpg' | relative_url }})

Generated 3D PDF for Operation 4

![]({{ '/assets/images/post_processor/28_report_generation/image015.jpg' | relative_url }})

Generated 3D PDF for Stress Effective State variable

### Region of Interest

Region of Interest (ROI) is an arbitrary shape (2d or 3d) which defines an area from which system gathers information about state variables for selected object and displays Min and Max value for selected state variable.

In Region of Interest selection page, we can add regions using ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button. For the added region we can create geometry using primitives or we can import the geometry file using import options (See Fig. 28.17.),

![]({{ '/assets/images/post_processor/28_report_generation/image016.jpg' | relative_url }})

Region of Interest selection page

In Outputs page, we can add the required output state variable and under Region column we can select the region across which state variable data needs to be extracted from pull down menu list as shown in Fig. 28.18.

![]({{ '/assets/images/post_processor/28_report_generation/image017.jpg' | relative_url }})

Region of Interest output page

### Coupon

Qualification of parts require cut-up evaluation of critical locations for microstructure and mechanical property response and industry needs to identify critical areas in the part based on forming and heat treatment modeling results. For those critical areas identified, we need to extract modeling state variables. Coupon capability in DEFORM can be used for this process.

In coupon selection page, add the coupon region to extract state variables data in the coupon region (See Fig. 28.19.).

![]({{ '/assets/images/post_processor/28_report_generation/image018.jpg' | relative_url }})

Coupon selection page

In Coupon Output page, we can add the required output state variables for which data needs to be extracted. ( See Fig. 28.20.) .

![]({{ '/assets/images/post_processor/28_report_generation/image019.jpg' | relative_url }})

Coupon Output state variable selection

Report generated for coupons sections is shown below Fig. 28.21.

![]({{ '/assets/images/post_processor/28_report_generation/image020.jpg' | relative_url }})

Generated Coupon result

### Point Tracking

User can add graphs to understand the behavior of a particular state variable at selected points using point tracking. In Point tracking selection page, select the step, select the points type, which could be Moving or Fixed, and select points for point tracking in Define window as shown in Fig. 28.22.

![]({{ '/assets/images/post_processor/28_report_generation/image021.jpg' | relative_url }})

Point tracking selection page

In Point tracking output page, select the state variable for which a graph needs to be plotted and check Export check box if point tracking state variable data need to be exported (See Fig. 28.23.).

![]({{ '/assets/images/post_processor/28_report_generation/image022.jpg' | relative_url }})

Point tracking output state variable selection

For each output state variable page, user can select the objects to be included for point tracking and also can select whether to plot contour and graph or graph alone from Display options as shown in Fig. 28.24.

![]({{ '/assets/images/post_processor/28_report_generation/image023.jpg' | relative_url }})

Output State variable window

The generated report for Point tracking section is as shown in Fig. 28.25.

![]({{ '/assets/images/post_processor/28_report_generation/image024.jpg' | relative_url }})

Shows sample of the generated report for Point tracking 

### Flownet

In order to include flow net of an object into report, from Flownet page select the step at which flownet to be added into report, currently Start step or End step or Start and End Step are available and they can be used by turning on respective check box, see Fig. 28.26.

![]({{ '/assets/images/post_processor/28_report_generation/image025.jpg' | relative_url }})

Flownet page

In Object selection page select object for which Flownet needs to be plotted, select pattern type and configure the pattern parameters as show in Fig. 28.27. Sample of Flownet from a generated report is shown in Fig. 28.28.

![]({{ '/assets/images/post_processor/28_report_generation/image026.jpg' | relative_url }})

Configuring Flownet pattern

![]({{ '/assets/images/post_processor/28_report_generation/image027.jpg' | relative_url }})

Generated PPT file for simple operation

### Post user variables tracking

This allows the user to generate the report for the user defined post variables defined in the post processor user routines.

In Library page, select the DLL file generated from the user routine in Library field and select the routine number from routine pull down list as shown in Fig. 28.29.

![]({{ '/assets/images/post_processor/28_report_generation/image028.jpg' | relative_url }})

Library and Routine selection page

In Tracking page, select Tracking variables radio button in Method type if no PDB file is available, then select Calculation type as Nodes or Elements type and then click on Track data, Once tracking the variables for particular DB is completed a PDB file will be generated in the problem directory, so in the next sessions of post processing user can select the existing PDB from the Tracking tab and then directly plot the user variables. (See Fig. 28.30.)

![]({{ '/assets/images/post_processor/28_report_generation/image029.jpg' | relative_url }})

Tracking data page

In Output page, add State variables by selecting State variable type as Post user var in pull down list and select state variables in component column and we can also export the respective State variable data by checking Export check box as show in Fig. 28.31. For each state variable user can select object, viewport, Contour type, Contour range and Color bar type as shown in Fig. 28.32., then generate Report in Generate report page.

![]({{ '/assets/images/post_processor/28_report_generation/image030.jpg' | relative_url }})

Output selection page

![]({{ '/assets/images/post_processor/28_report_generation/image031.jpg' | relative_url }})

Objects and Viewport selection page

### Custom

In custom page, post tools options will get active and most of post-processing work can be saved, such as object selection, display mode and step selection.

**Example** :

In this example we are generating report for simple 2D Spike DB using Graph (Load-Stroke), State variable, Point tracking and Flownet post tools.

Open Solved 2D Spike DB in Next gen post, click on Report tab. In Chapter page, turn on Graph (Load- Stroke), State variable, Point tracking and Flownet section checkboxes as shown in Fig. 28.33. Click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/post_processor/28_report_generation/image032.jpg' | relative_url }})

Selected post tools in Chapter page

**Graph (Load Stroke):**

In Graph page use the default Section title and click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}) . We will plot Load-Stroke Graph for top die, so click on ![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}) . In the added list, for X- axis select Stroke from pull down list and for Y-axis select Y-Load as shown in Fig. 28.34. and click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/post_processor/28_report_generation/image033.jpg' | relative_url }})

Graph Output selection page

In Load-Stroke page, select Primary die as Objects and the preview of the graph will be displayed that will be included in report as shown in Fig. 28.35., then click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }})..

![]({{ '/assets/images/post_processor/28_report_generation/image034.jpg' | relative_url }})

Load-Stroke graph object selection and preview

**State Variable:**

In State variable section page, select Start step, End Step and Middle Step as 7, click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). In Output page ( Fig. 28.36.), add Damage and Strain variables for contour plotting and click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). In Respective variable pages select Objects as Workpiece. Viewport as Auto and leave other fields to default settings. Click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/post_processor/28_report_generation/image035.jpg' | relative_url }})

State variable Output list

**Point Tracking:**

In Point tracking selection page, define the points for Point tracking in Define window as shown in Fig. 28.37., retain default setting and click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/post_processor/28_report_generation/image036.jpg' | relative_url }})

Selecting Points for Point tracking

In output page, add one Output variable and select Temperature as variable for point tracking and click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). In Temperature output window, select Contour+Graph as Display option type and Objects as Workpiece, click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}).

**Flownet:**

In Flownet page, use default Steps type (both Start step and End step), click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). In Object selection page select Workpiece as object and click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). In Grid page select Offset type and click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}), In Grid Definition page define Offset distance value as 0.01in and Click on ![]({{ '/assets/icons/post_icons/mo_preview_button.jpg' | relative_url }}), the offsetted object boundary will be displayed in object tree as shown in Fig. 28.38. Then click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}) until Generate report page.

![]({{ '/assets/images/post_processor/28_report_generation/image037.jpg' | relative_url }})

Offset flownet preview

**Generating Report:**

**PDF report :**

To generated report in PDF report file we need to trun on the PDF check box., and then click on ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}). to generate report. In Generated PDF file user can observe the Content (See Fig. 28.39.), Simulation summary (Fig. 28.40.) and then added sections report (See Fig. 28.28.41. to Fig. 28.44.).

![]({{ '/assets/images/post_processor/28_report_generation/image042.jpg' | relative_url }})

Content page in PDF document file

![]({{ '/assets/images/post_processor/28_report_generation/image043.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/28_report_generation/image044.jpg' | relative_url }})

Simulation summary in PDF document file

From v12.0.2., if user don't want the simulation summary in the report PDF file, then user need to turn off the "Include simulation summary" check box in Chapter page.

  
![]({{ '/assets/images/post_processor/28_report_generation/image039.jpg' | relative_url }})

Load - Stroke Graph plot generated in PPT

![]({{ '/assets/images/post_processor/28_report_generation/image038.jpg' | relative_url }})

Generated Damage State variable plot in PDF

![]({{ '/assets/images/post_processor/28_report_generation/image040.jpg' | relative_url }})

Generated point tracking graph for Temperature State variable in PPT

![]({{ '/assets/images/post_processor/28_report_generation/image041.jpg' | relative_url }})

Offset Flownet plot at last step

**PPT Report:** To generated report in PPT report file we need to trun on the PPT check boxx and click on ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}). The generation of Report will start and after completion of Report. Under PDF and PPT file user can view the output by clcikcing on ![]({{ '/assets/icons/post_icons/mo_view_button.jpg' | relative_url }}) (View )button.

Note: In PPT file 3D PDF output will not generated, except 3D PDF output other output will be saved in PPT file.

**Related Topics:**

[Report Generation Setup in MO Preprocessor](/docs/en/operation_templates/41_report_generation/41_1_report_generation/)

[25\. Post Processor Layout](/docs/en/post_processor/25_post_processor_layout/25_post_processor_layout/)

[27\. Introduction to Report Generation](/docs/en/post_processor/27_introduction_to_report_generation/27_introduction_to_report_generation/)
