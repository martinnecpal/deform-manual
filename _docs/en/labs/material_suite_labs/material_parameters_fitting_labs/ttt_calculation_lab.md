---
lang: en
title: "TTT Calculation Lab"
---

# Lab 1. Material Suite Lab for calculation of TTT Diagram

1.1. Introduction of TTT calculation theory in DEFORM

1.2. Launch TTT Calculation in material suite

1.3. Define Working Directory

1.4. Define TTT Input

## Introduction of TTT calculation theory in DEFORM

The TTT calculation program is based on Kirkaldy’s diffusive and martensitic models [1]. The original model has been transformed into a state-variable model to allow volume fraction transformation kinetics calculations. The aim of the program is to model volume fraction transformation kinetics of ferrite, pearlite, bainite and martensite for quenching of austenite; ignoring detailed distinction by phase morphology. Major assumptions include simple phase scaling for multiple phase formation, additivity rule for CCT, ferrite and pearlite do not occur at the same time scale, pearlite does not occur below Bs temperature. etc. The program will generate TTT diagram based on user's input alloy composition, grain size as well as other parameters. The program demonstrated reasonable prediction of TTT diagram for low alloy steels (<0.6 wt% C, <2 wt% Mn, <5 wt% Ni, <2 wt% Cr, <1 wt% Si).

Below is a comparison of calculated TTT and CCT diagrams using DEFORM with experimental measured diagrams for three different steels: AISI 1035, AISI5140 and AISI1050. The top three figures are from experimental measurements and the bottom figures are calculated from this program. Overall, the computed diagram agrees very well with experiments.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/ttt_calculation_lab/image0001.jpg' | relative_url }})

Comparison of calculated TTT and CCT diagrams using DEFORM with experimental measured diagrams

## Launch TTT Calculation in material suite

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button, select DEFORM-v12.xxx (.xxx indicates version number E.g. v14.0.2 and select DEFORM GUI Main v1x.xx from the menu. The DEFORM GUI Main window will appear. From GUI Main click on **Material Suite** under “Post Processor” to open Material Suite module. User can also double click "DEF_GUI_MAT.exe" in the installation directory of DEFORM software to launch material suite. After the main window for material suite pops up, expand "properties" item and click "**TTT Calculation** " icon, the new task item "**TTT Diagram** " is added to the task tree (See Fig. TTTL1.2.). Follow each tree item to prepare TTT diagram in the property data window (right-bottom window).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/ttt_calculation_lab/image0002.jpg' | relative_url }})

Launch TTT Calculation in material suite

## Define Working Directory

In the "TTT Diagram" task tree, click "**Config** " to open the window to specify Working directories as shown in below Fig. TTTL1.3. Specify the working directory where the computed TTT data will be stored.

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/ttt_calculation_lab/image0003.jpg' | relative_url }})

Config window to define Working directory

## Define TTT Input

In the "**TTT Diagram** " task tree, click "**TTT Input** " to specify TTT input.

At TTT input page, we allow user to input the following information:

  1. Materials Chemistry or the compositions of carbon and major alloy elements including Mn, Si, Ni, Cr, Mo, Cu, V and Nb.

  2. Grain size (in ASTM number)

  3. Starting and Ending of volume fraction (e.x.,1% starting and 99% ending)

  4. Martensite and Austenite transformation temperature: user can input these temperatures as input if information is available, otherwise clicking "Auto" will make program automatically compute these values.

In this lab, we chose **AISI 3120** as example and the following parameters are inputted: **C(0.17%), Mn (0.88%), Si(0.22%), Ni(0.86%), Cr(0.59%), Mo(0.05%), Cu (0), V(0), Nb(0), grain size 7, starting volume fraction 1%, ending 99%** , Martensite and Austensite transformation temperature is computed by program. After all the parameters are inputted, click "**Calculate** " to compute the TTT diagram. After the calculation is done, the following two files will be generated in the working directory:

**TTT.KEY**

**CCT.DAT**

The calculated TTT data is included in the file "**TTT.KEY** ". The "**Plot** " button in the GUI is also activated to display the calculated results. To do this, user can choose the designed transformation kinetics in the menu near the "**Plot** " button, then click "**Plot** ".

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/ttt_calculation_lab/image0004.jpg' | relative_url }})

TTT Input page

In this example, the TTT transformation data for austenite to pearlite, austenite to bainite and austenite to ferrite are displayed below (See Fig. TTTL1.5., Fig. TTTL1.6. and Fig. TTTL1.7.).

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/ttt_calculation_lab/image0005.jpg' | relative_url }})

Calculated TTT transformation data for austenite - pearlite transformation (Curve1)

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/ttt_calculation_lab/image0006.jpg' | relative_url }})

Calculated TTT transformation data for austenite - bainite transformation (Curve1)

![]({{ '/assets/images/labs/material_suite_labs/material_parameters_fitting_labs/ttt_calculation_lab/image0007.jpg' | relative_url }})

Calculated TTT transformation data for austenite - ferrite transformation (Curve1)

Reference:

[1] "Prediction of microstructure and hardenability in low-alloy steels" J. S Kirkaldy, D. Venugopalan - Phase Transformations in ferrous alloys, 1983
