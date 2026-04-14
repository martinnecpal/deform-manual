---
lang: sk
title: "JMAK Parameters Fitting Lab"
---

# Material Suite Lab for fitting material parameters in JMAK model

1.1. Abstract

1.2. Launch JMAK Model in material suite

1.3. Define testing controls and temperature groups

1.4. Fit material parameters in DRX kinetics

[1.5. Fit material parameters in MRX/SRX kinetics](jmak_parameters_fitting_lab.htm#1_5_Fit_material_parameters_in_MRX/SRX_kinetics_The_procedure_to_imp)

1.6. Fit material parameters in grain growth kinetics

1.7. Output the fitting results to keyword file

##  Abstract

JMAK (Johnson-Mehl-Avrami-Kolmogorov) model describes the recrystallization kinetics (evolution of grain size and volume fraction of recrystallized grains) of metals during thermo-mechanical processing. Depending on the specific thermal-mechanical processing conditions, different recrystallization mechanisms may take place, including dynamic recrystallization (DRX) occurring during deformation, meta-dynamic recrystallization (MRX) or static recrystallization (SRX) occurring after deformation, and static grain growth after the recrystallization is completed. JMAK model generally consists of a set of phenomenological or empirical equations, which are functions of strain, strain rate, temperature, time, and the initial grain size. A lot of material parameters are introduced in JMAK model, and it is a tedious and time-consuming task to determine these material parameters from the experimentally measured data. JMAK model in DEFORM Material Suite provides a convenient tool to fit material parameters in JMAK model.

In this lab, the procedures to import experimentally measured data into JMAK module in DEFORM Material Suite and to fit material parameters in JMAK model automatically are demonstrated. 

## Launch JMAK Model in material suite

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button, select DEFORM-v12.xxx (.xxx indicates version number E.g. v14.0.2 and select DEFORM GUI Main v1x.xx from the menu. The DEFORM GUI Main window will appear.

From GUI Main click on Material Suite under “Post Processor” to open Material Suite module. User can also double click "DEF_GUI_MAT.exe" in the installation directory of DEFORM software to launch material suite. After the main window for material suite pops up, expand "properties" item and click "**JMAK Model** " icon, the new task item "JMAK" is added to the task tree (See Fig. JMAKL1.1.). Follow each tree item to prepare JMAK model data in the property data window (right-bottom window).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0001.jpg' | relative_url }})

Launch JMAK model in material suite.

Click "**Config** " to open the window to specify Working directories as shown in below Fig. JMAKL1.2. Specify the working directory where the computed JMAK data will be stored.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0017.jpg' | relative_url }})

Config window to define Working directory

## Define testing controls and temperature groups

In the "**JMAK Model** " task tree, click "Testing controls" item as shown in Fig. JMAKL1.3. In the property window, we have two different ways to start the JMAK project. If there is an existing project saved previously, we can click the “Import Project” button to import the project data, and the defined data for each tree item will be automatically filled. user can also prepare the project data from scratch. After defining data in any tree item page, we can return to this “Testing controls” page and click the “Save Project” button to save all defined data.

In this Lab, define the system of units to represent the experimental results (such as “SI” in this lab). Click “ ![]({{ '/assets/icons/pre_icons/material_suite_add_button.jpg' | relative_url }}) ” or “![]({{ '/assets/icons/pre_icons/material_suite_delete_button.jpg' | relative_url }})” button to add or delete each testing condition. Input the following data, for the initial grain size (in microns): 40 and 100. Input three testing temperatures (in °C) : 900, 1200 and 1400, and two testing strain rates (in mm/mm/s) : 0.2 and 0.5. Each mechanical test is conducted at a constant strain rate and a constant temperature (such as uniaxial uniform compression test).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0002.jpg' | relative_url }})

Definition of mechanical testing controls

In the "JMAK Model" task tree, click "**Temperature groups** " item. In the property data window, click “![]({{ '/assets/icons/pre_icons/material_suite_add_button.jpg' | relative_url }})” or “![]({{ '/assets/icons/pre_icons/material_suite_delete_button.jpg' | relative_url }})” button to define the temperature group name (see Fig. JMAKL1.4.). For each temperature group, select the temperatures included. In each temperature group, the material parameters for recrystallization kinetics are assumed to be constant. The material parameters may change in different temperature groups. As a result, material parameters are defined as function of temperature. In this Lab, define Temperature group as "AA" and assign two temperatures 900°C and 1200°C into the group by selecting them as shown in Fig. JMAKL1.4.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0003.jpg' | relative_url }})

Definition of Temperature groups

## Fit material parameters in DRX kinetics

Expand "Dynamic recrystallization (DRX)" item in task tree and click the first subitem “**DRX peak strain** ”. In the data window, specify a temperature group. For each initial grain size, define the flow stress curves for all temperatures in the group and all strain rates. Each cell in the testing table highlighted by a red rectangular in Fig. JMAKL1.5. defines a flow stress curve at a constant temperature under a constant strain rate.

An empty file icon (“![]({{ '/assets/icons/pre_icons/material_suite_empty_file_icon.jpg' | relative_url }})”) denotes that the cell data has not been defined yet. After clicking an undefined cell, the cell image changes to a loading file icon (“![]({{ '/assets/icons/pre_icons/mo_import_file_icon2.jpg' | relative_url }})”), and the window for function definition pops up in the display window. The stress-strain data can be manually input, copied and pasted, or loaded from an existing function data file. After data input is completed, click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to close the function definition window. The cell image changes to a defined file icon (“![]({{ '/assets/icons/pre_icons/material_suite_defined_file_icon.jpg' | relative_url }})”) and the peak strain is automatically extracted and displayed in the line editor. The value of peak strain in the line editor can be manually edited. We can double click the view icon on the header (“![]({{ '/assets/icons/pre_icons/mo_visible.jpg' | relative_url }}) ”) to plot the flow stress curves at a fixed strain rate or a fixed temperature. It should be noted that, it is not necessary to define data for all cells, but the minimum requirement for fitting the interested parameters must be satisfied. The same method is used to define the cell data in the testing table for each item or subitem in the task tree. In this lab, we will import the data for each cell of AA group from "3D\LABS\MAK_Parameter_fitting_lab_data\DRX_Peak_strain_data folder".

For Grain size 40 - Stain rate 0.2 - Temperature 900 cell, load " 40_0.2_900.dat " file.

For Grain size 40 - Stain rate 0.2 - Temperature 1200 cell, load " 40_0.2_1200.dat " file.

For Grain size 40 - Stain rate 0.5 - Temperature 900 cell, load " 40_0.5_900.dat " file.

For Grain size 40 - Stain rate 0.5 - Temperature 1200 cell, load " 40_0.5_1200.dat " file.

For Grain size 100 - Stain rate 0.2 - Temperature 900 cell, load " 100_0.2_900.dat " file.

For Grain size 100 - Stain rate 0.2 - Temperature 1200 cell, load " 100_0.2_1200.dat " file.

For Grain size 100 - Stain rate 0.5 - Temperature 900 cell, load " 100_0.5_900.dat " file.

For Grain size 100 - Stain rate 0.5 - Temperature 1200 cell, load " 100_0.5_1200.dat " file.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0004.jpg' | relative_url }})

Import flow stress data and extract the peak strain

For a temperature group, after the flow stress data for all initial grain sizes are defined, click the “**Fit** ’ button to fit material parameters in the peak strain equation (see Fig. JMAKL1.6.). The fitted parameters are displayed in the fitting table, and the graphic comparison between the measured data and the predicted data by the fitted material parameters is shown in the display window. For any known parameter, the value can be input directly and check its “Fixed” flag. After fitting, parametric study can be performed by dragging the horizontal slider of a parameter and graphically examine the measured and predicted data.

For each additional temperature group if there is any, repeat this procedure to import its experimental data and fit material parameters.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0005.jpg' | relative_url }})

Fit material parameters in the peak strain equation

Click the “**DRX volume fraction** ” subitem. In the data window, define the available cell data (experimentally measured) of the testing table. In this lab, import each cell data from "3D\LABS\JMAK_Parameter_fitting_lab_data\DRX_volume_fraction" folder.

For Grain size 40 - Stain rate 0.2 - Temperature 900 cell, load " 40_0.2_900.dat " file.

For Grain size 40 - Stain rate 0.2 - Temperature 1200 cell, load " 40_0.2_1200.dat " file.

For Grain size 40 - Stain rate 0.5 - Temperature 900 cell, load " 40_0.5_900.dat " file.

For Grain size 40 - Stain rate 0.5 - Temperature 1200 cell, load " 40_0.5_1200.dat " file.

For Grain size 100 - Stain rate 0.2 - Temperature 900 cell, load " 100_0.2_900.dat " file.

For Grain size 100 - Stain rate 0.2 - Temperature 1200 cell, load " 100_0.2_1200.dat " file.

For Grain size 100 - Stain rate 0.5 - Temperature 900 cell, load " 100_0.5_900.dat " file.

For Grain size 100 - Stain rate 0.5 - Temperature 1200 cell, load " 100_0.5_1200.dat " file.

Each cell data defines the curve of DRX Vf~strain for a constant temperature and a constant strain rate. For each DRX Vf~strain curve, it is recommended that microstructures for at least 3 strain values should be measured, corresponding to low, medium, and high DRX volume fractions, so that the basic shape of DRX Vf~strain curve can be well described. For each defined curve, the strain for 50% DRX will be automatically extracted and displayed in the line editor of its cell. If the extracted strain for 50% DRX is not reasonable or desirable, it can be manually modified. In the display window after fitting, for each mechanical testing condition, the experimental data is displayed by solid dots, and the predicted data by the fitted parameters is displayed as a solid line with the same color (as shown in Fig. JMAKL1.7.).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0006.jpg' | relative_url }})

Fit material parameters in the DRX volume fraction

Click “**DRX grain size** ” subitem in the task tree. For each available cell data of the testing table, define the curve of DRX grain size versus strain. Import each cell data from "3D\LABS\JMAK_Parameter_fitting_lab_data\DRX_grain_size" folder.

For Grain size 40 - Stain rate 0.2 - Temperature 900 cell, load " 40_0.2_900.dat " file.

For Grain size 40 - Stain rate 0.2 - Temperature 1200 cell, load " 40_0.2_1200.dat " file.

For Grain size 40 - Stain rate 0.5 - Temperature 900 cell, load " 40_0.5_900.dat " file.

For Grain size 40 - Stain rate 0.5 - Temperature 1200 cell, load " 40_0.5_1200.dat " file.

For Grain size 100 - Stain rate 0.2 - Temperature 900 cell, load " 100_0.2_900.dat " file.

For Grain size 100 - Stain rate 0.2 - Temperature 1200 cell, load " 100_0.2_1200.dat " file.

For Grain size 100 - Stain rate 0.5 - Temperature 900 cell, load " 100_0.5_900.dat " file.

For Grain size 100 - Stain rate 0.5 - Temperature 1200 cell, load " 100_0.5_1200.dat " file.

After data definition is finished for the selected temperature group, click “**Fit** ” button to fit material parameters in the DRX grain size equation as shown in Fig. JMAKL1.8.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0007.jpg' | relative_url }})

Fit material parameters in the DRX grain size

Fig. JMAKL1.9. illustrates the definition of strain rate boundary. Its definition is based

on user’s empirical rule on the working material. We don’t fit the parameters in the equation for strain rate boundary. We include this page in order that we can output the keyword file for a complete JMAK model after we finish fitting material parameters. Import Strain_rate_boundary.dat file from "3D\LABS\JMAK_Parameter_fitting_lab_data" folder.

Strain rate boundary, together with the average deforming strain rate and the critical strain, is used to determine whether static or meta-dynamic recrystallization should be activated when deformation stops.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0008.jpg' | relative_url }})

Definition of material parameters in strain rate boundary equation

## Fit material parameters in MRX/SRX kinetics

The procedure to import MRX experimental data and fit its material parameters is the same as the procedure for SRX. Only the procedure to fit material parameters in MRX kinetics is introduced here.

The pre-deformed strain is an important controlling factor in MRX/SRX experimental test. The mechanical tests are terminated at the pre-deformed strains, then the specimens are hold at the same temperature for different times, followed by quenching for microstructure measurement. At least two pre-deformed strains should be employed. For MRX tests, the pre-deformed strains are large than the critical strain but less than the 100% DRX strain. For SRX tests, the pre-deformed strains should be less than the critical strain (thus DRX has not occurred yet). The definition of pre-deformed strains is shown in Fig. JMAKL1.10.

In the task tree, click “**Meta-dynamic recrystallization (MRX)** ” item. In the data window, input two pre-deformed strains, 0.1 and 0.2.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0009.jpg' | relative_url }})

Definition of pre-deformed strain for MRX kinetics

Click the “**MRX volume fraction** ” subitem in the task tree. In the data window, specify a temperature group. For each initial grain size and pre-deformed strain, for each available cell in the testing table, define the curve of MRX volume fraction versus time. Import each cell data from " 3D\LABS\JMAK_Parameter_fitting_lab_data\MRX_volume_fraction" folder.

For Grain size 40 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 900 cell, load " 40_0.1_0.2_900.dat " file.

For Grain size 40 - Predeformed Strain 0.1 - Stain rate 0.5 - Temperature 900 cell, load " 40_0.1_0.5_900.dat " file.

For Grain size 40 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 1200 cell, load " 40_0.1_0.2_1200.dat " file.

For Grain size 40 - Predeformed Strain 0.1 - Stain rate 0.5 - Temperature 1200 cell, load " 40_0.1_0.5_1200.dat " file.

For Grain size 40 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 900 cell, load " 40_0.2_0.2_900.dat " file.

For Grain size 40 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 900 cell, load " 40_0.2_0.5_900.dat " file.

For Grain size 40 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 1200 cell, load " 40_0.2_0.2_1200.dat " file.

For Grain size 40 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 1200 cell, load " 40_0.2_0.5_1200.dat " file.

For Grain size 100 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 900 cell, load " 100_0.1_0.2_900.dat " file.

For Grain size 100 - Predeformed Strain 0.1 - Stain rate 0.5 - Temperature 900 cell, load " 100_0.1_0.5_900.dat " file.

For Grain size 100 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 1200 cell, load " 100_0.1_0.2_1200.dat " file.

For Grain size 100 - Predeformed Strain 0.1 - Stain rate 0.5 - Temperature 1200 cell, load " 100_0.1_0.5_1200.dat " file.

For Grain size 100 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 900 cell, load " 100_0.2_0.2_900.dat " file.

For Grain size 100 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 900 cell, load " 100_0.2_0.5_900.dat " file.

For Grain size 100 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 1200 cell, load " 100_0.2_0.2_1200.dat " file.

For Grain size 100 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 1200 cell, load " 100_0.2_0.5_1200.dat " file.

After the curve of a cell is defined, the time for 50% MRX will be extracted automatically and filled in the line editor. This time for 50% MRX can be manually edited. After data definition is completed, click “**Fit** ” button to fit material parameters in the MRX volume fraction equation (see Fig. JMAKL1.11.).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0010.jpg' | relative_url }})

Fit material parameters for MRX volume fraction equation

Click the “**MRX grain size** ” subitem in the task tree. Fitting the material parameters for MRX grain size equation is shown in Fig. JMAKL1.12. For each available cell in the testing table, the measured MRX grain size is input. It is assumed that MRX grain size depends on the initial grain size and pre-deformation conditions, but does not vary with the time of MRX process. In this lab, define the values using below Table1 and Table 2 data. After data definition is completed, click “**Fit** ” button to fit the material parameters in the MRX grain size equation.

**Temperature** |  **Initial grain size 40** |  **Initial grain size 100**  
---|---|---  
Strain rate 0.2 |  Strain rate 0.5 |  Strain rate 0.2 |  Strain rate 0.5  
900 |  68.0606 |  65.1158 |  100.715 |  96.3075  
1200 |  93.952 |  89.8477 |  139.463 |  133.32  
  
For Predeformed Strain 0.1 value

**Temperature** |  **Initial grain size 40** |  **Initial grain size 100**  
---|---|---  
Strain rate 0.2 |  Strain rate 0.5 |  Strain rate 0.2 |  Strain rate 0.5  
900 |  44.208 |  42.3313 |  65.0177 |  62.2092  
1200 |  60.708 |  58.0924 |  89.711 |  85.7966  
  
For Predeformed Strain 0.2 value

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0011.jpg' | relative_url }})

Fit material parameters for MRX grain size equation

In the task tree, click “**Static- recrystallization (SRX)** ” item. In the data window, input two pre-deformed strains, 0.1 and 0.2 as shown in Fig. JMAKL1.13.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0012.jpg' | relative_url }})

Definition of pre-deformed strain for SRX kinetics

Click the “**SRX volume fraction** ” subitem in the task tree. In the data window, specify a temperature group. For each initial grain size and pre-deformed strain, for each available cell in the testing table, define the curve of SRX volume fraction versus time. Import each cell data from " 3D\LABS\\\JMAK_Parameter_fitting_lab_data\SRX_volume_fraction" folder.

For Grain size 40 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 900 cell, load " 40_0.1_0.2_900.dat " file.

For Grain size 40 - Predeformed Strain 0.1 - Stain rate 0.5 - Temperature 900 cell, load " 40_0.1_0.5_900.dat " file.

For Grain size 40 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 1200 cell, load " 40_0.1_0.2_1200.dat " file.

For Grain size 40 - Predeformed Strain 0.1 - Stain rate 0.5 - Temperature 1200 cell, load " 40_0.1_0.5_1200.dat " file.

For Grain size 40 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 900 cell, load " 40_0.2_0.2_900.dat " file.

For Grain size 40 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 900 cell, load " 40_0.2_0.5_900.dat " file.

For Grain size 40 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 1200 cell, load " 40_0.2_0.2_1200.dat " file.

For Grain size 40 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 1200 cell, load " 40_0.2_0.5_1200.dat " file.

For Grain size 100 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 900 cell, load " 100_0.1_0.2_900.dat " file.

For Grain size 100 - Predeformed Strain 0.1 - Stain rate 0.5 - Temperature 900 cell, load " 100_0.1_0.5_900.dat " file.

For Grain size 100 - Predeformed Strain 0.1 - Stain rate 0.2 - Temperature 1200 cell, load " 100_0.1_0.2_1200.dat " file.

For Grain size 100 - Predeformed Strain 0.1 - Stain rate 0.5 - Temperature 1200 cell, load " 100_0.1_0.5_1200.dat " file.

For Grain size 100 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 900 cell, load " 100_0.2_0.2_900.dat " file.

For Grain size 100 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 900 cell, load " 100_0.2_0.5_900.dat " file.

For Grain size 100 - Predeformed Strain 0.2 - Stain rate 0.2 - Temperature 1200 cell, load " 100_0.2_0.2_1200.dat " file.

For Grain size 100 - Predeformed Strain 0.2 - Stain rate 0.5 - Temperature 1200 cell, load " 100_0.2_0.5_1200.dat " file.

After the curve of a cell is defined, the time for 50% SRX will be extracted automatically and filled in the line editor. This time for 50% SRX can be manually edited. After data definition is completed, click “**Fit** ” button to fit material parameters in the SRX volume fraction equation (see Fig. JMAKL1.14.).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0013.jpg' | relative_url }})

Fit material parameters for SRX volume fraction equation

Click the “**SRX grain size** ” subitem in the task tree. Fitting the material parameters for SRX grain size equation is shown in Fig. JMAKL1.15. For each available cell in the testing table, the measured SRX grain size is input. It is assumed that SRX grain size depends on the initial grain size and pre-deformation conditions but does not vary with the time of SRX process. In this lab define the values using same Table1 and Table 2 data. After data definition is completed, click “**Fit** ” button to fit the material parameters in the SRX grain size equation.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0014.jpg' | relative_url }})

Fit material parameters for SRX grain size equation

## Fit material parameters in grain growth kinetics

In the task tree, click “**Grain growth** ” item. For each temperature group, define the available cell data in the testing table. Each cell defines the curve of grain size versus time measured from grain growth tests. Import each cell data from " 3D\LABS\JMAK_Parameter_fitting_lab_data\Grain growth" folder.

For Grain size 40 - Temperature 900 cell, load " 40_900.dat " file.

For Grain size 40 - Temperature 1200 cell, load " 40_1200.dat " file.

For Grain size 100 - Temperature 900 cell, load "100_900.dat " file.

For Grain size 100 - Temperature 1200 cell, load " 100_1200.dat " file.

After the data input is completed, click “**Fit** ” button to fit the material parameters in the grain growth equation.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0015.jpg' | relative_url }})

Fit material parameters for grain growth kinetics

## Output the fitting results to keyword file

After fitting material parameters for JMAK model is completed, click “**Save keyword file** ” in the task tree, and input necessary data as shown in Fig. JMAKL1.17. to complete the JMAK model definition. Click “**Save keyword** ” button to save the keyword file in the directory specified by file path. The keyword file name in this lab is “JMAK.key”, the data can be viewed under DEFORM keyword “GRNDAT” in the saved keyword file. In FEM model definition, we can import this keyword file for JMAK model definition.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/jmak_parameters_fitting_lab/image0016.jpg' | relative_url }})

Save a keyword file for JMAK model
