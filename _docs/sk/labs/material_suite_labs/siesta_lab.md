---
lang: sk
title: "SIESTA Lab"
---

# SIESTA FILE GENERATION

1.1. Introduction to SIESTA

1.2. Launch SIESTA output in Material suite

1.3. Export to SIESTA

## Introduction to SIESTA

DEFORM has developed the facility to export data from database into SIESTA file, a file format required by the DARWIN software developed by Southwest Research Institute. More details about DARWIN can be found here:

  
<http://www.darwin.swri.org/html_files/background/summary.html>

## Launch SIESTA output in Material suite

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button, select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2 and select DEFORM GUI Main v1x.xx from the menu. The DEFORM GUI Main window will appear.

Create database by importing 2D_Example/SI/HeatTreat/ MRX_SRX_2D_SI.KEY with the problem ID as **MRX_SRX_2D_SI** in NG Pre, then simulate it from GUI main using Run. Keep it ready ,we will use this example to demonstrate how to export SIEST output file in Material suite.

  
Now from GUI Main, by selecting **MRX_SRX_2D_SI.DB** file click on Material Suite under “Post Processor” to open Material Suite module as shown in Fig. SIESTAL1.1.

![]({{ '/assets/images/labs/material_suite_labs/siesta_lab/image0001.jpg' | relative_url }})

Opening Material Suite from GUI Main

  
After the main window for material suite is opened, Expand "**Performance** " item and click on "**SIESTA** " icon from Performance list as shown in Fig. SIESTAL1.2., the new task item "SIESTA Output" is added to the task tree.

  
  
![]({{ '/assets/images/labs/material_suite_labs/siesta_lab/image0002.jpg' | relative_url }})

Launching SIESTA output in material suite 

## Export to SIESTA

Click on “**Output** ” tab, select the object in object list and choose the state variables to export (Stress, Temperature, Effective Strain and Grain Size) from State variable Selection list, then choose the step in the database that needs to be exported (here we are selecting the last step). Click on "**Export to SIESTA** " and choose the location to save the file and name of the file. By default, the SIESTA file will be saved with the name "Database+step number.ISO". For example, the database name is MRX_SRX_2D_SI and the step we chose is **717** , the generated SIESTA file will be **MRX_SRX_2D_SI_Step717.sio** as shown in Fig. SIESTAL1.3.

![]({{ '/assets/images/labs/material_suite_labs/siesta_lab/image0003.jpg' | relative_url }})

Exporting SIESTA file in material suite
