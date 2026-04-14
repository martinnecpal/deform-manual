---
lang: sk
title: "Report Generation Lab in MO"
---

# Report Generation Lab in MO

In this lab Report generation feature is explained in both interactive and batch post mode for Spike_Forging lab Project.

1.1.1. Copy the Existing Project

1.1.2. Add Report Generation operation

1.1.3. Add Chapters

1.1.4. Define First Chapters

1.1.5. Define second chapter

1.1.6. Define Third Chapter

1.1.7. Define Fourth Chapter

1.1.8. Define Fifth Chapter

1.1.9. Define Sixth chapter

1.1.10. Simulate Project

1.1.11. Review the Report

## Report generation in Batch post mode

If 3D MO basic labs: lab [03 Spike Forging](/docs/sk/labs/basic_labs/3d_labs/lab03_spike_forging/) is already practiced, then open the Spike Forging project in MO by selecting the project file from DEFORM GUI Main and clicking on ![]({{ '/assets/icons/pre_icons/mo_integrated_manufacturing_proc.jpg' | relative_url }}). Otherwise copy the project file available in installation path as explained below.

### Copy the Existing Project

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and "**English** " radio button in unit field as shown in Fig. RGL1.1.

Define Problem Name as "**Spike_Forging** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Integrated Manufacturing Process.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0001.jpg' | relative_url }})

Open New Problem from DEFORM GUI Main

Multiple operation wizard will open, select Copy Existing Project radio button. Browse the project file for previously saved project and open the Spike_Forging.moproj file or browse from installation path **/3d/LABS/Spike_Forging/Spike_Forging.moproj** (See Fig. RGL1.2.). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to copy and open the project.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0002.jpg' | relative_url }})

Copy existing Spike_Forging project

Select the **Heat Transfer operation** in operation editor and select Generate DB in operation tree to Generate DB as shown in Fig. RGL1.3. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0003.jpg' | relative_url }})

Generate Database for 1st operation

### Add Report Generation operation

Add the Report Generation operation from the MO operation explorer as shown in Fig. RGL1.4.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0004.jpg' | relative_url }})

Add Report Generation operation

Click on report operation in operation editor to open the report generation operation as shown in Fig. RGL1.5.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0005.jpg' | relative_url }})

Opening Report generation operation

### Add Chapters

In Report property window user can add more than one chapter and chapter name can be changed by double clicking in title field.

These chapters are helpful to generate the different operations or different operations range results report separately as new chapters. In this lab we add 6 chapters so click ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add chapter) button five times in addition to the default one chapter. . First 4 chapters will be used to cover each of the 4 operations, fifth chapter to plot the temperature summary from first to last operation and sixth chapter to plot the load stroke curve for 2 forming operations. The chapter names are auto updated depending on the operation range selected in the respective chapter or user can define custom name. For first 4 chapters in this lab, the chapter name will be updated as we select operation range in the respective chapter. We will define custom name for 5th chapter as **"Temperature Summary from all operations"** and 6th chapter as "**Continuous Load stroke curve forming operations** " instead of operations range. Then Report window looks as shown in Fig. RGL1.6.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0006.jpg' | relative_url }})

Report window with 6 chapters

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define added chapters.

### Define First Chapters

For first chapter, select **Air Convection** **operation** as starting and ending operation and check only the State variable check box for sections as shown in Fig. RGL1.7.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0007.jpg' | relative_url }})

Chapter-1 settings

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define state variable section. Accept the state variable section title steps selected and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to add the state variable outputs. (See Fig. RGL1.8.).

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0008.jpg' | relative_url }})

State variable section basic settings

Click on ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) button once to add temperature state variable and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (See Fig. RGL1.9.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0009.jpg' | relative_url }})

State variable output selection window

Select the objects as Workpiece and viewport as User Defined and adjust the viewport as required using display modification options pan, zoom, rotate and magnify. (See Fig. RGL1.10.) User also have a Viewport options like different axis views like +X,-X,+Y etc, Isometric, contour type selection, contour range, color bar type and Auto view. Select PDF layout as 9 as shown in Fig. RGL1.10.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0010.jpg' | relative_url }})

State variable Temperature settings window

Check the **Include 3D Model** **(3D PDF)** checkbox at the bottom of the window to include the 3D model in PDF file. (See Fig. RGL1.10.)

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the second chapter.

### Define second chapter

Similar to the first chapter, select only "**H****eat Resting** " operation (2nd operation) for second chapter and add temperature state variable with only 3 steps as shown in Fig. RGL1.11 and Fig. RGL1.12.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0011.jpg' | relative_url }})

State variable settings

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and click on ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) button once to add temperature state variable.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0012.jpg' | relative_url }})

State variable output selection window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and select the Workpiece object, User Defined viewport type and PDF layout as 9. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the third chapter.

### Define Third Chapter

In this chapter, select the "**Forming** " operation (3rd operation ) as starting and ending operation and check the Metal flow, Graph and State variable sections (See Fig. RGL1.13) as this is a forming operation to review the material flow, load stroke graph for primary die and deformation state variables as different steps.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0013.jpg' | relative_url }})

Chapter-3 settings

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and to define metal flow steps. Accept the Metal flow steps selected as 7 and in controls define the PDF layout as 9. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define Load stroke graph. (See Fig. RGL1.14)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0014.jpg' | relative_url }})

Metal Flow settings

Change the Graph section title from **Graph (Load-Stroke)** to **Load Stroke****Graph** as shown in Fig. RGL1.15 and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue graph definition.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0015.jpg' | relative_url }})

Graph section title window

Click on ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) button once to add Load-Stroke as graph variables, select X-Axis variable as Stroke and Y-Axis variable as Z Load as shown in Fig. RGL1.16.

.![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0016.jpg' | relative_url }})

Graph variables definition window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and select the object as Primary die as shown in Fig. RGL1.17.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0017.jpg' | relative_url }})

Graph objects selection window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and to define the state variable. Accept the 7 steps selected for state variables and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to add state variables.

Click on ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) button twice to select Effective strain and Effective stress variables contour as shown in Fig. RGL1.18 . and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define each sate variable contour display settings.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0018.jpg' | relative_url }})

State variables adding window

Select the Objects as only workpiece, viewport as User Defined and PDF layout as 9. Also check the Include 3D model (3D PDF) for getting the 3D model in PDF and adjust the viewport display as required.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the fourth chapter.

### Define Fourth Chapter

Similar to the third chapter, select only last forming operation "****Forging** Blow 2**" for fourth chapter and add sections Metal Flow, Stroke-Z Load Graph and Effective Stress and effective strain state variable contour sections.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the fifth chapter.

### Define Fifth Chapter

For this chapter, select starting operation as **Air convection** and ending operation as **Forging Blow 2** and check Summary, State variable and Point tracking sections. (See Fig. RGL1.19.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0019.jpg' | relative_url }})

Chapter-5 settings

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the sections. Accept the summary section title as Summary and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (See Fig. RGL1.20)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0020.jpg' | relative_url }})

Summary section title window

Click on ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) button once to add Temperature Vs Time curve from first to last operation. So select X-Axis variable as Time and Y-Axis variable as Temperature as shown in Fig. RGL1.21.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0021.jpg' | relative_url }})

Summary graph adding window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and select Workpiece as object as shown in Fig. RGL1.22. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define State variable.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0022.jpg' | relative_url }})

Summary graph object selection window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for State variable number of step selection page keeping 7 steps. Click on ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) button once and add the Temperature state variable. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and select the object as All, viewport as User Defined and PDF layout as 9. For this chapter we will generate the state variable contour without 3D model, so do not check the Include 3D model (3D PDF) checkbox as shown in Fig. RGL1.23.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0023.jpg' | relative_url }})

Temperature state variable settings window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define point tracking section.

Accept the point tracking section title as "**Point track** " as shown in Fig. RGL1.24. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0024.jpg' | relative_url }})

Point tracking section title window

Confirm that Moving points option is selected and click on ![]({{ '/assets/icons/pre_icons/mo_define_button2.jpg' | relative_url }}) button to select the points to track on workpiece.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0025.jpg' | relative_url }})

Point tracking point selection window

Defien three points for point tracking over Workpiece as shown in Fig. RGL1.26. and these points will gets added into the define point table. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the define points window and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0026.jpg' | relative_url }})

Define points window

Click on ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) button once to select temperature state variable and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to point track graph settings.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0027.jpg' | relative_url }})

Point tracking state variable selection window

Select the Workpiece object and display option as only Graph Plot as shown in Fig. RGL1.28.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0028.jpg' | relative_url }})

Point tracking plot settings

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the sixth chapter.

### Define Sixth chapter

Select**Starting operation** as **Forming** and **Ending****operation** as ****Forging** Blow 2** and check Graph section as shown in Fig. RGL1.29.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0029.jpg' | relative_url }})

Chapter-6 settings window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define Stroke- Z Load graph for primary die in Forming and Forging blow 2 operation.

Click on ![]({{ '/assets/icons/pre_icons/mo_add_button_2.jpg' | relative_url }}) button once to select X-Axis as Stroke and Y-Axis as Z-Load and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to select object as Primary die.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate report page, check both PDF and PPT Documentation type check boxes.

### Simulate Project

Click on ![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) project icon and select ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode button to run the simulation.

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

### Review the Report

After completion of simulation of all operations prior to report generation, report generation will start to generate report for the selected state variables and graphs. Also generated PPT file will open automatically. Browse the problem directory from explorer and look for DEF_REPORT directory to find the generated PDF and PPT report files.

Open the PPT and PDF files and go through the chapter wise reports.

**Chapter 1:**

For chapter 1 Temperature state variable contour PPT will play all 9 images in single slide, when we click on Slide show (F5). (See in Fig. RGL1.30.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0030.jpg' | relative_url }})

Chapter 1 Temperature state variable PPT slide

PDF will show the 9 images temperature state variable workpiece contour images in a single page as shown in Fig. RGL1.31.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0031.jpg' | relative_url }})

Chapter 1 Temperature state variable PDF page

3D model for temperature state variable will display for air convection operation at last step in PDF as shown in Fig. RGL1.32.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0032.jpg' | relative_url }})

Chapter 1 Temperature state variable 3D model PDF page

User can use the 3d model options mentioned below to rotate, pan, zoom, change image capture area, measure dimensions, put comments, select different views, toggle model tree, different rendering modes, extra light options, change background color and section the object.

3D model PDF options are listed below,

**Rotate![]({{ '/assets/icons/pre_icons/mo_report_pdf_rotate.jpg' | relative_url }}) **: Using this option user can rotate the object about screen center.

**Spin![]({{ '/assets/icons/pre_icons/mo_report_pdf_spin.jpg' | relative_url }}) **: Using this option user can rotate the object about object center.

**Pan**![]({{ '/assets/icons/pre_icons/mo_report_pdf_pan.jpg' | relative_url }}) : Using this option user can move object and adjust display area without changing the size of the object.

**Zoom![]({{ '/assets/icons/pre_icons/mo_report_pdf_zoom.jpg' | relative_url }}) **: Using this user can change the size of the region of object.

**Fly![]({{ '/assets/icons/pre_icons/mo_report_pdf_fly.jpg' | relative_url }}) **: By selecting this option if user holds the left mouse click and roll the mouse then object will move up or fly.

**Camera properties**![]({{ '/assets/icons/pre_icons/mo_report_pdf_cam.jpg' | relative_url }}) :

**3D Measurement Tool**![]({{ '/assets/icons/pre_icons/mo_report_pdf_meassure.jpg' | relative_url }}) : Using this user can measure the dimensions of the object.

**Add 3D Comment** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_3d_comment.jpg' | relative_url }}) : User can add the comments by picking the point on the object.

**Default View**![]({{ '/assets/icons/pre_icons/mo_report_pdf_home.jpg' | relative_url }}) : Using this will display the default object view, in the default view measuring or adding the comment will save as new viewports. User can latter select the Measurement View or 3DCommentView later to observe the measured dimension or added comments. (See Fig. RGL1.33.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0033.jpg' | relative_url }})

View selection field

Added comments or measured dimensions can be deleted or edited by right mouse click options.

User can also select standard view modes like Iso Plus, Iso Minus, X Plus, Y Plus etc.

**Toggle model Tee**![]({{ '/assets/icons/pre_icons/mo_report_pdf_tog.jpg' | relative_url }}) : Using this user will get the model tree towards left side of the PDF page, in that tree it list the 3d model different views and comments. It also give other display options like Previous view or Next view.

**Use Perspective projection** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_proj.jpg' | relative_url }}) : This will project the visible front area of the object.

**Model Render mode** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_render.jpg' | relative_url }}) : This provides different rendering types like Transparent, Illustration, Wire frame, Solid, Shaded.. etc.

**Enable extra lighting** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_light.jpg' | relative_url }}) : Using this user can use can enable different extra lighting settings.

**Background color** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_background.jpg' | relative_url }}) : Using this user can change the background color.

**Toggle cross section** ![]({{ '/assets/icons/pre_icons/mo_report_pdf_section.jpg' | relative_url }}) : Activating this user can section the object section plane properties can be changed by using the pull down button Cross section properties.

**Chapter 2:**

For Chapter 2 Temperature state variable contour, PPT will play all 3 images in single slide, when we click on Slide show (F5). (See in Fig. RGL1.34.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0034.jpg' | relative_url }})

Chapter 2 Temperature state variable PPT slide

PDF will show the 3 images temperature state variable workpiece contour images in a single page as shown in Fig. RGL1.35.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0035.jpg' | relative_url }})

Chapter 2 Temperature state variable PDF page

3D model for temperature state variable will display for Heat resting operation at last step in PDF as shown in Fig. RGL1.36.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0036.jpg' | relative_url }})

Chapter 2 Temperature state variable 3D model PDF page

For 3D model options refer the Chapter 1 results review section 3D Model PDF options.

**Chapter 3 :**

For Chapter 3 Metal flow, PPT will play all 7 saved steps images in single slide as we selected total 9 steps (including 1st and last step) when we click on Slide show (F5). (See in Fig. RGL1.37.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0037.jpg' | relative_url }})

Chapter 3 Metal flow PPT slide

PDF will show all the 7 images of deformed workpiece in a single page as shown in Fig. RGL1.38.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0038.jpg' | relative_url }})

Chapter 3 Metal flow PDF page

For Chapter 3 primary die Z-Load Vs Stroke graph in PPT is as shown in Fig. RGL1.39.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0039.jpg' | relative_url }})

Chapter 3 Z-load vs Stroke graph PPT slide

PDF display the same Z-Load Vs Stroke graph as shown in Fig. RGL1.40.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0040.jpg' | relative_url }})

Chapter 3 Z-load vs Stroke graph PDF page

For Chapter 3 Effective Stress state variable contour, PPT will play all 7 images in single slide, when we click on Slide show (F5). (See in Fig. RGL1.41.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0041.jpg' | relative_url }})

Chapter 3 Effective Stress state variable PPT slide

PDF will show the 7 images Effective Stress state variable workpiece contour images in a single page as shown in Fig. RGL1.42.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0042.jpg' | relative_url }})

Chapter 3 Effective Stress state variable PDF page

3D model for Effective Stress state variable will display for Forming operation at last step in PDF as shown in Fig. RGL1.43.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0043.jpg' | relative_url }})

Chapter 3 Effective Stress state variable 3D model PDF page

For Chapter 3 Effective Strain state variable contour, PPT will play all 7 images in single slide, when we click on Slide show (F5). (See in Fig. RGL1.44.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0044.jpg' | relative_url }})

Chapter 3 Effective Strain state variable PPT slide

PDF will show the 7 images Effective Strain state variable workpiece contour images in a single page as shown in Fig. RGL1.45.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0045.jpg' | relative_url }})

Chapter 3 Effective Strain state variable PDF page

3D model for Effective Strain state variable will display for Forming operation at last step in PDF as shown in Fig. RGL1.46.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0046.jpg' | relative_url }})

Chapter 3 Effective Strain state variable 3D model PDF page

**Chapter 4 :**

For Chapter 4 Metal flow, PPT will play all 3 saved steps images in single slide as we selected total 9 steps (including 1st and last step) when we click on Slide show (F5). (See in Fig. RGL1.47.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0047.jpg' | relative_url }})

Chapter 4 Metal flow PPT slide

PDF will show all the 3 images of deformed workpiece in a single page as shown in Fig. RGL1.48.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0048.jpg' | relative_url }})

Chapter 4 Metal flow PDF page

For Chapter 4 primary die Z-Load Vs Stroke graph in PPT is as shown in Fig. RGL1.49.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0049.jpg' | relative_url }})

Chapter 4 Z-load vs Stroke graph PPT slide

PDF display the same Z-Load Vs Stroke graph as shown in Fig. RGL1.50.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0050.jpg' | relative_url }})

Chapter 4 Z-load vs Stroke graph PDF page

For Chapter 4 Effective Stress state variable contour, PPT will play all 3 images in single slide, when we click on Slide show (F5). (See in Fig. RGL1.51.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0051.jpg' | relative_url }})

Chapter 4 Effective Stress state variable PPT slide

PDF will show the 3 images Effective Stress state variable workpiece contour images in a single page as shown in Fig. RGL1.52.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0052.jpg' | relative_url }})

Chapter 4 Effective Stress state variable PDF page

As we are not selected the Include 3D model checkbox 3D PDF model not available for the Chapter 4.

For Chapter 4 Effective Strain state variable contour, PPT will play all 3 images in single slide, when we click on Slide show (F5). (See in Fig. RGL1.53.)

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0053.jpg' | relative_url }})

Chapter 4 Effective Strain state variable PPT slide

PDF will show the 3 images **Effective Strain** state variable workpiece contour images in a single page as shown in Fig. RGL1.54.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0054.jpg' | relative_url }})

Chapter 4 Effective Strain state variable PDF page

**Chapter 5 :**

For Chapter 5 Temperature summary graph for workpiece, from 1st to last operation in PPT file is as shown in Fig. RGL1.55.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0055.jpg' | relative_url }})

Chapter 5 temperature Summary graph for Workpiece PPT slide

PDF display the summary graph for Temperature for workpiece in all operation as shown in Fig. RGL1.56.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0056.jpg' | relative_url }})

Chapter 5 temperature Summary graph for Workpiece PDF page

For Chapter 5 Temperature state variable contour for all objects will play operation wise in different PPT slides. Air convection temperature contour refer the Fig. RGL1.30. Similarly for the PDF images of temperature contour refer Fig. RGL1.31.

Heat resting temperature contour steps play in PPT refer the Fig. RGL1.57.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0057.jpg' | relative_url }})

Chapter 5 Temperature state variable PPT slide for Heat resting operation

PDF images of temperature contour for heat resting refer Fig. RGL1.58.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0058.jpg' | relative_url }})

Chapter 5 Temperature state variable PDF page for Heat resting operation

Similarly during Forming operation temperature contour steps play in PPT refer the Fig. RGL1.59.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0059.jpg' | relative_url }})

Chapter 5 Temperature state variable PPT slide for Forming operation

PDF images of temperature contour for Forming refer Fig. RGL1.60.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0060.jpg' | relative_url }})

Chapter 5 Temperature state variable PDF page for Forming operation

During Forging Blow 2 operation temperature contour steps play in PPT refer the Fig. RGL1.61.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0061.jpg' | relative_url }})

Chapter 5 Temperature state variable PPT slide for **Forging** Blow 2 operation

PDF images of temperature contour for Forging Blow 2 refer Fig. RGL1.62.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0062.jpg' | relative_url }})

Chapter 5 Temperature state variable PDF page for **Forging** Blow 2 operation

PPT slide for Chapter 5 point tracking graph for workpiece temperature state variable at centre and 2 points on outer Die is as shown in Fig. RGL1.63.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0063.jpg' | relative_url }})

Point tracking graph for workpiece temperature PPT slide

PDF point racking page is shown in Fig. RGL1.64.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0064.jpg' | relative_url }})

Point tracking graph for workpiece temperature PDF page

**Chapter 6 :**

PPT slide for Z-Load Vs Stroke graph for primary die in forming and forging Blow 2 operation is as shown in Fig. RGL1.65.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0065.jpg' | relative_url }})

Primary die Z-Load Vs Stroke graph PPT slide

PDF Z-Load Vs Stroke graph is as shown in Fig. RGL1.66.

![]({{ '/assets/images/labs/report_generation_lab/report_generation_lab_in_mo/image0066.jpg' | relative_url }})

Primary die Z-Load Vs Stroke graph PDF page

For details on using other sections of the [Report generation](/docs/sk/operation_templates/41_report_generation/41_1_report_generation/) refer the related topics.

**Related Topics:**

[28\. Report Generation](/docs/sk/post_processor/28_report_generation/28_report_generation/)

[41\. Report Generation](../../../assets/images/operation_templates/41_report_generation/41_introdcution_to_report_generation)
