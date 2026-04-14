---
lang: sk
title: "Flow Stress Fitting Lab"
---

# Material Suite Lab for fitting material parameters in Flow stress model

## Introduction of flow stress data fitting facility 

In Material Suite, we provide a convenient tool to convert experimental data (load-stroke curves or stress-strain curves) to tabular flow-stress data in DEFORM. The program can consider adiabatic correction for experimental data. The program will provide fitted material parameters in the flow stress model, graphic comparison between original experimental data and model data. User can easily save the fitted flow stress data into keyword file for FEM simulation.

## Launch Flow Stress Model in material suite

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button, select DEFORM-v12.xxx (.xxx indicates version number E.g. v14.0.2 and select DEFORM GUI Main v1x.xx from the menu. The DEFORM GUI Main window will appear. From GUI Main click on **Material Suite** under “Post Processor” to open Material Suite module. User can also double click "**DEF_GUI_MAT.exe** " in the installation directory of DEFORM software to launch material suite. After the main window for material suite pops up, expand "properties" item and click "Flow stress model" icon, the new task item "Flow stress" is added to the task tree (See Fig. FSL1.1.). Follow each tree item to prepare Flow stress model data in the property data window (right-bottom window).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0001.jpg' | relative_url }})

Launch Flow Stress model in material suite.

Click "**Config** " to open the window to specify Working directories as shown in below Fig. FSL1.2\. Specify the working directory where the computed Flow stress data will be stored.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0010.jpg' | relative_url }})

Config window to define Working directory

## Define Units and initial specimen geometry

In the "Flow stress" task tree, click "**units and initial specimen geometry** " item. Under "units and initial specimen geometry", choose **SI** unit. The initial height and initial cross section area are used for the data conversion between load-stroke data and stress-strain data, the unit is mm for SI unit and inch for English unit. We can click the “**Import Project** ” button to import the project data, after importing the defined data for each tree item will be automatically filled. User can also prepare the project data from scratch. After defining data in any tree item page, we can return to this “units and initial specimen geometry” page and click the “**Save Project** ” button to save all defined data. In this lab we choose 100 for initial height and 10 for initial cross section area (see Fig. FSL1.3.) .

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0002.jpg' | relative_url }})

Units and Initial specimen geometry page

## Define Testing type and Conditions

In the "Flow stress" task tree, click "**Testing type and Conditions** " item. Choose "**Tension** " as Testing type, "**Constant strain rate** " as Rate Control type as shown in Fig. FSL1.4.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0003.jpg' | relative_url }})

Testing type and Conditions page

## Define Testing temperature and rates

In the "Flow stress" task tree, click "**T******e** sting temperature and rates**" page. Input three test temperatures: 200, 500 and 700 and three test strain rates: 0.1, 0.5 and 1 as shown in Fig. FSL1.5. In the next page, we are going to input 9 sets of flow stress data as a function of strain for each temperature and strain rate combinations.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0004.jpg' | relative_url }})

Testing Temperature and rates page

## Define Experimental Data

In the "Flow stress" task tree, click "**Experimental data** " page. Select Flow stress data radio button in Raw data type ( see Fig. FSL1.6.) and click on ![]({{ '/assets/icons/pre_icons/material_suite_delete_button.jpg' | relative_url }}) button and Input flow stress data for each cell. An empty file icon (“![]({{ '/assets/icons/pre_icons/material_suite_empty_file_icon.jpg' | relative_url }}) ”) denotes that the cell data has not been defined yet. After clicking an undefined cell, the cell image changes to a loading file icon (“![]({{ '/assets/icons/pre_icons/mo_import_file_icon2.jpg' | relative_url }})”), and the window for function definition pops up in the display window. The stress-strain data can be manually input, copied and pasted, or loaded from an existing function data file. After data input is completed, click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to close the function definition window. The cell image changes to a defined file icon (“![]({{ '/assets/icons/pre_icons/material_suite_defined_file_icon.jpg' | relative_url }})”). For this lab, import the data of each cell from "3D\LABS\Material_Suite_Flow_stress_data" folder inside the installation path,

For Temperature 200 - Strain rate 0.1 cell, load " Temp_200_Strain_rate_0.1.dat " file.

For Temperature 200 - Strain rate 0.5 cell, load " Temp_200_Strain_rate_0.5.dat " file.

For Temperature 200 - Strain rate 1 cell, load " Temp_200_Strain_rate_1.dat " file.

For Temperature 500 - Strain rate 0.1 cell, load " Temp_500_Strain_rate_0.1.dat " file.

For Temperature 500 - Strain rate 0.5 cell, load " Temp_500_Strain_rate_0.5.dat " file.

For Temperature 500 - Strain rate 1 cell, load " Temp_500_Strain_rate_1.dat " file.

For Temperature 700 - Strain rate 0.1 cell, load " Temp_700_Strain_rate_0.1.dat " file.

For Temperature 700 - Strain rate 0.5 cell, load " Temp_700_Strain_rate_0.5.dat " file.

For Temperature 700 - Strain rate 1 cell, load " Temp_700_Strain_rate_1.dat " file, after defining data click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to Close.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0005.jpg' | relative_url }})

Experimental data page

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0006.jpg' | relative_url }})

After defining Flow stress data for each cells

## Define Heat Capacity correction

In the "Flow stress" task tree, click "**Experimental data** " page. If we consider the heat capacity effect by choosing "**Yes** " on this page, the flow stress data will be corrected based on the adiabatic heating effect. The temperature will be adjusted by ![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/eq_1.jpg' | relative_url }}) , and the corresponding flow stress data will be adjusted. For this lab we will not be using Heat Capacity correction hence, select "**NO** " radio button.

## Define Sampling data

In the "Flow stress" task tree, click "**Sampling** " page. input "**10** " as number of strain, **0.1** as **Minimum****strain** , **1** as **Maximum****strain** and **0** as **Zero****strain****offset**. Choose "**Plot sampled flow stress curves** " then click "**Sampling** " button. The program will display the flow stress curve in the defined strain range.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0007.jpg' | relative_url }})

Sampling controls page

## Conversion of Flow Stress model

In the "Flow stress" task tree, click "**Conversion of flow stress model** " page. On the "**Conversion of flow stress model** " page, user can choose which flow stress model he/she wants to fit, in this lab we will choose **Johnson-Cook** equation:

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/eq_2.jpg' | relative_url }})

For fitting method, choose "**quasi least square method** ", input initial guess parameter, click "**Fit** " to generate the fitted parameters as well as the flow stress curve using the fitted parameters. For each parameter, user can decide to fit it or to fix it without fitting. There is also a slider bar available for each parameter which allows user to modify values of parameters and display the parametric study results. In the following graphic display, the original experimental data is represented by points and model data is represented by solid lines (see Fig. FSL1.9.).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0008.jpg' | relative_url }})

Conversion of Flow stress model page

## Output

Click “**Output** ” in the task tree, define "**Material NO** " and "**Material Name** " as shown in Fig. FSL1.10. to save the output into keyfile and use it in FEM. Click “**Save keyword for flow stress** ” button to save the keyword files in the directory specified by file path. Two keyfiles will be saved inside the directory specified, **FSTRES.KEY** and **FSTRES_SAMPLED_TABULATE.KEY** files.

**FSTRES.KEY** will have the selected Flow stress model data.

**FSTRES_SAMPLED_TABULATE.KEY** will have Sampling data (Tabular data format Flow stress model).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/flow_stress_fitting_lab/image0009.jpg' | relative_url }})

Flow stress Output Page
