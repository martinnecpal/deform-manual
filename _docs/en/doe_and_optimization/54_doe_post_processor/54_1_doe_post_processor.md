---
lang: en
title: "54.1. DOE Post Processor"
---

#  54.1. DOE Post Processor

54.1.1. Starting DOE Post- Processor

54.1.2. DOE Post- Processor Graphical Layout

54.1.2.1. Display Window

54.1.2.2. Workspace

54.1.2.3. Property Editor Space

54.1.2.4. Graphical Display utilities

[54.1.2.5. DOE Output/Optimization Results Tree](54_1_doe_post_processor.htm#54_1_2_5_DOE_Output/Optimization_Results_Tree)

Evaluation (DOE Study)

Objective function (Optimization Study)

Adding new output variable in DOE Output

Operation Min/Max

Summary Min/ Max

State Variable Min/ Max

Location Specific

Probe Output

Global Min/ Max

54.1.2.6. DOE Output Display Utilities

54.1.2.7. DOE Output Graphical Utilities

54.1.3. DOE Post-Processor Menu Bar

54.1.3.1. File Menu

54.1.3.2. Viewport Menu

54.1.3.3. Display Menu

54.1.3.4. Mouse Menu

54.1.3.5. Tool Menu

54.1.3.6. Options Menu

54.1.3.7. Dock Widgets

54.1.3.8. Help Menu

54.1.3.9. Monte-Carlo

54.1.4. DOE Output Utilities in DOE Post-Processor

54.1.4.1. DOE Output Display Utilities

54.1.4.2. DOE Output Graphical Utilities

Table View

Model View

Summary Plot

3D Response Surface Plots

2D Response Contour Plot

Tornado Chart

Sensitivity Plot

Scatter Plot

Histogram Plot

## Starting DOE Post- Processor

DOE Post can be opened from the Post-Processor tab of Integrated Manufacturing Process template when the user is in DOE Study/ Optimization Study tab as shown in Fig. 54.1.1. DOE Post can also be opened from DEFORM GUI Main using DOE Post link that gets activated when DOE Study folder is selected as shown in Fig. 54.1.2. If DOE Post is already opened previously then in GUI Main, we can observe the display of the plots in workspace from the last session.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0001.jpg' | relative_url }})

DOE Post integrated opening link

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0002.jpg' | relative_url }})

DOE Post GUI opening link

  
**Note** : DOE/ Optimization Study simulated in V11.3 and lower versions must be opened in V12.0+ versions and output must be extracted using “Extract” in DOE output operation for proper display of outputs.

## DOE Post- Processor Graphical Layout

The DOE Post when opened with a .SDB looks like as shown in Fig. 54.1.3.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0003.jpg' | relative_url }})

DOE Post Processor

### Display Window

It displays the models and graphs based on the user selection from graphical utilities and DOE Output Tree. In DOE Post user can modify Graphical display layout using “Change Layout”. If a display window is empty either in workspace or viewport then we can observe DOE output Graphical utilities tool bar as we roll mouse into the display area, see Fig. 54.1.4.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0004.jpg' | relative_url }})

DOE output Graphical utilities

  
Whenever any plot is displayed then a floating icon according to the plot are available to manipulate the display, the options are:

**Maximize View** : If display area has more than one viewport then Maximize view ![]({{ '/assets/icons/post_icons/doe_post_maximize_view.jpg' | relative_url }}) can be used to maximize the viewport and to restore it back. 

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0005.jpg' | relative_url }})

Maximize view

  
**Lock output** : Lock output can be used to lock the display content from being modified as the user navigates to different DOE output variables in the DOE output tree, if the “Lock output” is not used then the display content is updated according to the DOE output variable selected in DOE Output tree. Once the viewport display is locked the icon changes to and can be unlocked by clicking on it. 

**Zoom in** ![]({{ '/assets/icons/post_icons/doe_post_zoom in.jpg' | relative_url }}) : When a viewport has multiple items displayed then user can use this option to Zoom in specific run.

**Zoom out** ![]({{ '/assets/icons/post_icons/doe_post_zoom out.jpg' | relative_url }}) : User can use this option to Zoom out of the specific run and display other runs.

**Zoom Fit**![]({{ '/assets/icons/post_icons/doe_post_zoom fit_button.jpg' | relative_url }}) : When a viewport has multiple items displayed then user can use this option to fit all the runs into display area. 

**Close** ![]({{ '/assets/icons/post_icons/mo_close view.jpg' | relative_url }}) : User can use this option to delete the Graphical plot/ table/ model from the display.

**Interactive Mode** : When a viewport has multiple items displayed then user can double click on any run and launch interactive mode to view only that run.

### Workspace

DOE Post provides 4 independent workspaces as shown in Fig. 54.1.6. and Fig. 54.1.7. which allows the user to analyze the DOE results from different perspectives by switching between workspaces without deleting the Display area content. The workspaces display information is automatically saved while closing the .SDB file and restored during reopening of the respective .SDB file. 

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0006.jpg' | relative_url }})

Workspace 1

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0007.jpg' | relative_url }})

Workspace 2

### Property Editor Space

Depending on the selection of the items from the DOE Output Tree and DOE Output variable plot type respective properties or controls that are available to make necessary changes are displayed in Property Editor space. Fig. 54.1.8. shows properties of response surface for output.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0008.jpg' | relative_url }})

Property Control window

### Graphical Display utilities

Graphical display utilities as shown in Fig. 54.1.9. are used to manipulate the display content in the display area like zoom, rotate, pan, fit view, Etc. These utilities are available only when we plot Response Surface, Response contour and Model view in interactive mode. For more information on these graphical utilities please refer [graphical utilities](../../pre_processor/8_pre_processor_layout/8_pre-processor_layout.htm#8.1._Graphic_Utilities_Window).

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0009.jpg' | relative_url }})

Graphical display utilities

### DOE Output/Optimization Results Tree

Depending on whether the .SDB is generated from DOE Study or Optimization Study the output variables and their status will be shown as shown in Fig. 54.1.10. If it is a DOE Study simulation, then we can observe “Evaluation” criteria in the tree and for an Optimization Study simulation we will be observing “Objective function”. The DOE Study is also having the Monte-Carlo options beside the DOE Output tab.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0010.jpg' | relative_url }})

Tree view

####   
Evaluation (DOE Study):

It is used to display the each run status (Pass or Fail) based on the evaluation criteria defined in DOE study setup in pre-processor. (See Fig. 54.1.11.)

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0011.jpg' | relative_url }})

Evaluation plot

####   
Objective function (Optimization Study):

It will show the objective function details and run which has optimized result based on the objective function defined along with the constraints and inputs used as shown in the Fig. 54.1.12.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0012.jpg' | relative_url }})

Objective function window

####   
Adding new output variable in DOE Output

DOE Output tree displays different categories of outputs defined in DOE Study setup for each operation. If necessary, user can add additional output variables by selecting respective output category and adding the required available variable by clicking on ![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}) button which will add new variable with status as “Not Available”. After adding the new variable user can click on “Extract Variable” button as shown in Fig. 54.1.13. then data for the variable is extracted from the simulated DBs and a new .SDB is created and status in DOE Output tree is changed to “Available” as shown in Fig. 54.1.13. It is always advised to close and Reopen the SDB in DOE Post after the extraction to see the updated data. For more information on different DOE Output Categories please refer DOE Pre output.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0013.jpg' | relative_url }})

Extracting Newly Added DOE variable

####   
Operation Min/ Max:

Displays the state variable minimum or maximum value based on the selection of all the steps within that operation. (See Fig. 54.1.14.)

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0014.jpg' | relative_url }})

Response surface plot for operation Min/Max variable

####   
Summary Min/ Max:

Displays the state variable minimum or maximum value based on the selection from the last step of the selected operation and object. (See Fig. 54.1.15.)

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0015.jpg' | relative_url }})

Tornado chart for summary Min/Max variable

#### State Variable Min/ Max:

Displays the state variable minimum or maximum value based on the selection from the last step of the selected operation and object. User can also use ROI/ Probe from the list for selected object. (See Fig. 54.1.16.)

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0016.jpg' | relative_url }})

Scatter plot for state variable Min/Max output

####   
Location Specific:

In DOE Study it displays the state variable value based on the Region of Interest defined and the selected object. Whenever user plots the location specific then a new interactive display window is opened with plot of selected object if user is not in model view. Region of interest and state variable looks like as shown in Fig. 54.1.17.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0017.jpg' | relative_url }})

3D Location specific view with Table view plot

#### Probe Output: 

Displays the state variable value based on the location of the selected Probe defined in DOE Setup in Integrated Manufacturing Process Template.

####   
Global Min/ Max: 

Displays the state variable minimum or maximum value based on the selection across all steps in all Operations.

### DOE Output Display Utilities

DOE Output Display utilities as shown in Fig. 54.1.18. are used to modify the workspace to plot different type of Graphs/ Tables to interpret the output variables from DOE/ Optimization Study. For more information on these options refer 54.1.4.1. DOE Output Display Utilities.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0018.jpg' | relative_url }})

Display utilities

### DOE Output Graphical Utilities

DOE Output Graphical utilities are used to plot tables or Graphs. DOE Output Graphical utilities available in DOE Post-Processor are shown in Fig. 54.1.19. We have Table View ![]({{ '/assets/icons/post_icons/doe_post_table_view.jpg' | relative_url }}) , Model View ![]({{ '/assets/icons/post_icons/doe_post_model_view_button.jpg' | relative_url }}), Summary plot ![]({{ '/assets/icons/post_icons/doe_post_summary_plot_button.jpg' | relative_url }}), 3D Response surface ![]({{ '/assets/icons/post_icons/doe_post_response surface_button.jpg' | relative_url }}), 2D Response contour ![]({{ '/assets/icons/post_icons/doe_post_response_contour_button.jpg' | relative_url }}), Tornado Chart ![]({{ '/assets/icons/post_icons/doe_post_tornado_chart.jpg' | relative_url }}), Sensitivity plot ![]({{ '/assets/icons/post_icons/doe_post_sensitivity_plot_button.jpg' | relative_url }}), Scatter plot ![]({{ '/assets/icons/post_icons/doe_post_scatter_plot_button.jpg' | relative_url }}) and Histogram ![]({{ '/assets/icons/post_icons/doe_post_histogram_button.jpg' | relative_url }}). For more information on how to use these utilities refer 54.1.4.2. DOE Output Graphical Utilities.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0019.jpg' | relative_url }})

Graphical utilities

## DOE Post-Processor Menu Bar

### File Menu

Options available under File Menu are shown in Fig. 54.1.20. File menu is used to perform actions like open the old projects, open the working directory or recently worked projects, close the project, quit the DOE Post- Processor. Etc.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0020.jpg' | relative_url }})

File Menu  

  
**Open Project (Ctrl + O)** ![]({{ '/assets/icons/post_icons/mo_import_button.jpg' | relative_url }}): We can open the simulated .SDB file in DOE Post using open project option, when no other SDB file is opened in current DOE Post.

  
**Folder options** : User can open the directory of the current .SDB file in windows explorer using **Folder** options![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Open working folder. (See Fig. 54.1.21.)

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0021.jpg' | relative_url }})

Folder Menu

**Image setup (CTRL+M**) : It is used to setup the settings to be used while capturing the image from current display window or the workspace, the image setup settings available are as shown in Fig. 54.1.22.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0022.jpg' | relative_url }})

Image Setup

**Capture image (CTRL+I)![]({{ '/assets/icons/pre_icons/mo_capture_screen_image_to_file_icon.jpg' | relative_url }})** : Depending on the settings in Image Setup an image is captured and saved into a file in specified image format.

**Capture Image to clipboard (Ctrl + Shift +I)** ![]({{ '/assets/icons/pre_icons/mo_capture_screen_to_clip_board_icon.jpg' | relative_url }}): Depending on the settings in Image Setup an image is captured onto clipboard which can be used later until clipboard is overwritten.

**Recent Projects** : This option lists the .SDB files that were opened. 

**Close (Ctrl + W)** : Currently opened .SDB file can be closed using this option. 

**Quit (Ctrl + Q)![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }})** : User can quit DOE Post-Processor using this option.

### Viewport Menu

Viewport menu is activated wherever it is applicable like **Response surface, Response contour and Model view in interactive mode**. Viewport menu is used to manipulate display content in the workspace. Options available under viewport are shown in Fig. 54.1.23.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0023.jpg' | relative_url }})

Viewport Menu

### Display Menu 

Display menu is activated wherever it is applicable like **Response surface, Response contour and Model view in interactive mode**. Display menu is used to render the objects / graph in the Workspace. Options available under Display menu are shown in Fig. 54.1.24.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0024.jpg' | relative_url }})

Display Menu

### Mouse Menu

Mouse menu is activated wherever it is applicable like Response surface, Response contour and Model view in interactive mode. Mouse menu is used to perform actions like measure, pick a point, rotate, pan, zoom, Etc using mouse. Options available under Mouse menu are shown in Fig. 54.1.25.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0025.jpg' | relative_url }})

Mouse Menu

### Tool Menu

Tool Menu is Currently disabled in DOE Post-processor. 

### Options Menu

Options menu is used to set DEFORM Environment settings and Preferences. Options menu looks like as shown in Fig. 54.1.26. For more information on these options refer [Environment](../../pre_processor/8_pre_processor_layout/8_pre-processor_layout.htm#Environment) and [Preference](../../pre_processor/8_pre_processor_layout/8_pre-processor_layout.htm#Preferences).

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0026.jpg' | relative_url }})

Options Menu

### Dock Widgets

Dock Widgets menu is used to turn on or off the display of the Property Editor control space (displays current viewport display property name) and Tree view. Options under Dock widgets are shown in Fig. 54.1.27.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0027.jpg' | relative_url }})

Dock Widgets

### Help Menu

Help menu has options to access the DEFORM HTML manual using F1, Context help using (Shift+F1), About SFTC and About DOE Post-Processor version and build details. Options under help are shown in Fig. 54.1.28.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0028.jpg' | relative_url }})

Help Menu

### Monte-Carlo

Monte-Carlo methods are used to extrapolate the results based on the DOE/Optimization study output by modifying range and distribution of the input variables. See Fig. 54.1.29. and Fig. 54.1.30.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0029.jpg' | relative_url }})

Monte-Carlo input definition page

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0030.jpg' | relative_url }})

Monte-Carlo output for defined runs

## DOE Output Utilities in DOE Post-Processor

### DOE Output Display Utilities

#### Change Layout

User can study a DOE Output variable using different types of Graphical options simultaneously in a workspace by creating multiple viewports in display. When user clicks on ![]({{ '/assets/icons/post_icons/mo_change_layout_icon.jpg' | relative_url }}),a pulldown menu is displayed to select the display layout as shown in Fig. 54.1.31. Viewports are created based on the grid selection. User can plot different output types like Response surface, Table view, Tornado Chart, Sensitivity plot etc. simultaneously as shown in Fig. 54.1.32. When particular run is selected in any view port then selection of the run in other viewports Table, graphs such as Response surface, Scatter plot,.. and Model view will be updated to the same run as shown in Fig. 54.1.32. unless they are not locked.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0031.jpg' | relative_url }})

Change Layout

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0032.jpg' | relative_url }})

Synchronized view

####   
Filter Data 

Using this option user can selectively display the cases / runs that are of interest to study. The selected Run will be highlighted in blue color as shown in Fig. 54.1.33. From Fig. 54.1.34. we can observe that when DOE Study involves Case variables then Average value of all cases for each run is also calculated.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0033.jpg' | relative_url }})

Filter data for DOE variables

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0034.jpg' | relative_url }})

Filter data for DOE having CASE variables

### DOE Output Graphical Utilities

#### Table View ![]({{ '/assets/icons/post_icons/doe_post_table_view.jpg' | relative_url }})

When user opens an .SDB file for the first time, DOE Study/ Optimization Study results are shown in Table view mode. Table View plot as shown in Fig. 54.1.35. displays information about DOE input variables and their values, DOE output variables, Evaluation criteria value in case of DOE Study or Objective Function value in case of Optimization study (See Fig. 54.1.36.), Variable constraints status along with Global constraint status and Global Min/Max values. DOE Table when DOE study includes CASE variables is shown in Fig. 54.1.37., we can see an additional row of Average values of all the cases for that Run being displayed along with CASE Variable runs. Column colors for different variables displayed in table (see Fig. 54.1.37) are,

**DOE Input Variables columns** – Green

**Constraints** \- Pink

**Evaluation** – Yellow

**Operation Min/ Max output** – Blue

**Summary Min/ Max output** \- Orange

**State Variable Min/ Max output** – Purple

**Probe output** – Light Blue

**Global Min/ Max output** – Grey color

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0035.jpg' | relative_url }})

Table view for DOE variable

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0036.jpg' | relative_url }})

Table view for OPT variable

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0037.jpg' | relative_url }})

Table view for DOE CASE variable

  
Constraints status in table is displayed as Global constraint and Variable constraint. A Variable constraint status is displayed as passed ![]({{ '/assets/icons/post_icons/doe_post_passed_status_icon.jpg' | relative_url }}) or as failed ![]({{ '/assets/icons/post_icons/doe_post_failed_status_icon.jpg' | relative_url }})based on the output of the respective variable value. If the DOE Study/ Optimization Study has just one constraint, then Global Constraint will be same as that of the Variable constraint. If user is having multiple variable constraints in an DOE Study and one of the variable constraints is failed for a Run, then the Global constraint status will be displayed as Failed for the Run and if all the defined variable constraints has Pass status only then the Global constraint status will be displayed as Pass for the Run shown in Fig. 54.1.38. below 

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0038.jpg' | relative_url }})

Single Variable Constraint

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0039.jpg' | relative_url }})

Multiple Variable Constraint

  
  
The Control window for Table view is shown in Fig. 54.1.40. User can select / deselect the check boxes of respective columns to control the display of columns in Table view mode. “Auto Apply changes” check box can be turned on so that changes made to the display of columns are automatically applied else user has to use ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button to see the changes in columns display after turning them off/on. User can turn on “Real values” check box to display the actual values of DOE input variables or turn off to display the Normalized values. The values from the table can be saved into an .CSV file using button ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}).

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0040.jpg' | relative_url }})

Table View Control window

####   
Model View ![]({{ '/assets/icons/post_icons/doe_post_model_view_button.jpg' | relative_url }})

User can click on Model view for graphical display of the objects and setup as thumbnail images. Model View displays the objects and setup for all runs in matrix form as shown in Fig. 54.1.41. If DOE Study/ Optimization Study does not include Case Variables, then the models for each run are displayed continuously as shown in Fig. 54.1.41. If DOE Study/ Optimization Study includes Case variables then Case variables output for the respective DOE Variable are displayed in columns and DOE Variables are displayed as rows as shown in Fig. 54.1.42., user can pick model for respective DOE Variable run and Case variable. 

When a DOE Study/ Optimization study has more runs and thumbnail images become clumsy then user can use to Zoom in ![]({{ '/assets/icons/post_icons/doe_post_zoom in.jpg' | relative_url }}) into the display and to Zoom out ![]({{ '/assets/icons/post_icons/doe_post_zoom out.jpg' | relative_url }}). User can use Zoom Fit ![]({{ '/assets/icons/post_icons/doe_post_zoom fit_button.jpg' | relative_url }}) to fit the images into display area. 

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0041.jpg' | relative_url }})

3D Model View for DOE Variable 

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0042.jpg' | relative_url }})

Model View for DOE with Case variable

  
User can plot state variable plot using the icons available in the control window. The state variable output is updated automatically for all runs. If DOE Study/ Optimization Study has multiple operations, then user can select required operation from the pulldown list as shown in Fig. 54.1.43. and model view loads the last step of that operation into the display area. If DOE Study has location specific variables then user can click on “Common mesh” tab and select location specific output item from the DOE Output Tree to display location specific variable output in display area, when user selects Location specific output model view then system launches interactive mode for that Run automatically.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0043.jpg' | relative_url }})

Selection of operation

**Interactive model display**  
User can select Run and double click on it to launch interactive mode, interactive mode displays just that Run in display area as shown in Fig. 54.1.44. For 3D Model it has additional slicing tools as shown in Fig. 54.1.44. User can go back to all Runs model view by closing interactive mode using ![]({{ '/assets/icons/post_icons/mo_close view.jpg' | relative_url }}) . Display settings from interactive mode can be copied to all runs using check box next to “Apply current display settings to other views” as shown in Fig. 54.1.45. and Fig. 54.1.46.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0044.jpg' | relative_url }})

3D Interactive Model view

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0045.jpg' | relative_url }})

3D Apply changes to interactive model

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0046.jpg' | relative_url }})

3D Model view plot after applying changes to other models

#### Summary Plot ![]({{ '/assets/icons/post_icons/doe_post_summary_plot_button.jpg' | relative_url }})

User can select the “Switch to Summary Plot” icon from the tool bar to plot the Summary plot of the DOE Study as shown in Fig. 54.1.47. Summary output must be added as DOE output while setting up in DOE Study in in “Integrated Manufacturing Process” template in order to plot it in DOE Post. Summary plots are displayed in matrix form when DOE study includes Case variables, Case variables output for the respective DOE Variable is displayed in columns and DOE Variables are displayed as rows. User can also plot Summary plot output variable from DOE Output tree view by selecting the output variable below Summary plot. When user selects Summary plot output variable from DOE Output tree, user will be provided with a pop-up to choose whether to change the current display area into Summary plot or not as shown in Fig. 54.1.48. Summary plot of a Run can be maximized to occupy entire view port by double clicking on respective Summary plot as shown in Fig. 54.1.49.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0047.jpg' | relative_url }})

Summary Plot

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0048.jpg' | relative_url }})

Switching to Summary plot

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0049.jpg' | relative_url }})

Summary Plot

**Super Impose Summary Plots**

User can superimpose Summary plots using ![]({{ '/assets/icons/post_icons/mo_superimpose_icon.jpg' | relative_url }}) for interpreting the results of all runs in a single graph. User can turn on super imposing by turning on ![]({{ '/assets/icons/post_icons/mo_superimpose_icon.jpg' | relative_url }}) icon then Summary plot of all runs are overlapped into one graph as shown in Fig. 54.1.50.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0050.jpg' | relative_url }})

Super Impose

  
**3D Response Surface Plots** ![]({{ '/assets/icons/post_icons/doe_post_response surface_button.jpg' | relative_url }})

Response surface explores the relationships between DOE study input variables and respective output variables across all DOE runs. So, using this user can easily estimate the interested output variables response against DOE study variables variation and based on the sensitivity of output response optimum response can be selected for future optimization. From the output tree user needs to select the required output variable for which response surface needs to be plotted and then click on ![]({{ '/assets/icons/post_icons/doe_post_response surface_button.jpg' | relative_url }}) (Switch to response surface mode) icon to display 3D response surface plot or click on ![]({{ '/assets/icons/post_icons/doe_post_response_contour_button.jpg' | relative_url }}) (Switch response contour mode) icon to display 2D response contour plot as shown in Fig. 54.1.51.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0051.jpg' | relative_url }})

3D Response surface and 2D Response contour

From the control window space user can select the output variable to plot the response in "output" tab, X and Y axis DOE study input variables can be selected from the pull-down menu as shown in Fig. 54.1.52.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0052.jpg' | relative_url }})

Response surface controls window

**Response Surface Type** : User can select response surface fit type from the list available next to “Response Surface Type”, see Fig. 54.1.53. In DOE Post-processor currently we have Linear, Quadratic, Gaussian and Neural Network based response surface generation.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0053.jpg' | relative_url }})

Response Surface Type

  
**X Axis/ Y Axis:** DOE Study input variables are listed in X Axis and Y Axis. User can pick input variable for X and Y axis from this list to study selected DOE Output variable response with respect to these input variables.

**Input:** In input tab of the Response Surface Control window, we can observe all other inputs except that of X Axis and Y Axis are displayed. Next to each of the input variable we can observe a sliding bar which can be used to adjust the weight of that input towards response surface or enter the value manually into the box next to it, as the user adjusts the weights, Response Surface is automatically modified and displayed. (See Fig. 54.1.54.)

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0054.jpg' | relative_url }})

Response plot input controls

**Advanced** : The graph scale for Response Surface by default is defined based on the state variable minimum and maximum value across all runs. If user wants to build the Response within specified range of Output Variable value, then user can do so by selecting “User” radio button and specifying the Minimum and Maximum value as shown in Fig. 54.1.55. If the value needs to be applied across multiple graphs in display, then![]({{ '/assets/icons/post_icons/doe_post_apply_to_all_button.jpg' | relative_url }})button can be used.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0055.jpg' | relative_url }})

Response plot advanced controls

**Legend** : In DOE Post-processor all runs are indicated by dots in plots and graphs, color of the dots indicate the runs response to the variable and fill constraints. In Legend tab we can observe the legend used to mark various runs based on the status of constraints. Legends used in Response Surface are shown in Fig. 54.1.56.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0056.jpg' | relative_url }})

Response plot Legends control

**Manipulating 3D Response Surface display** : User can rotate the 3D response surface by holding the scroll button or CTRL+LMB short key and rolling the mouse.

  
**Exclude Failed constraint runs** ![]({{ '/assets/icons/post_icons/mo_check_box.jpg' | relative_url }}): At any moment user can use this check box to exclude runs in which the constraints are failed.

  
**Include Penalty** ![]({{ '/assets/icons/post_icons/mo_check_box.jpg' | relative_url }}): User also have an option to include the penalty in output variables for failed runs by considering its constraints status, so user can compare the runs which are more optimal.

**Output** : In output, user has options to select the output variable for which response surface needs to be generated. In Output tab, by turning on Composite check box user can plot Composite Response surface as shown in Fig. 54.1.57.

**Composite Response surface** : From separate response surface views, it is difficult to visualize where a “best” location is on all surfaces for specific input variations. So composite response surface which compares the different output variable response based on few limiting values or weights or user defined equations are generated to find such best location on all surfaces. User needs to check the "Composite" check box in output tab and select the composite types like Pass/Fail, Weighted Sum, Penalized Weighted Sum or Equation and then define respective parameters.

**Pass/Fail Composite** : In this composite response surface type user needs to define the "Acceptable limit" or "Reference value" of output state variables and then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button, a new response surface is generated across the DOE runs output based on the values defined to find the best response as shown in below Fig. 54.1.58.

**Weighted Sum** : User need to set the weights based on the importance of the state variables and then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button, a new response surface is generated across the DOE runs output based on the weights defined to find the best response as shown in below Fig. 54.1.59.

**Penalized Weighted Sum** : This provides combination of both pass / fails based on defined acceptable value and weights based on the importance of the state variables as shown in below Fig. 54.1.60. User can set the Reference value and also Weight for the output state variable and then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button, a new response surface is generated across the DOE runs output by considering both Weights and Reference value criteria.

**Equation** : User need to define the valid mathematical equation for output state variables listed using suitable mathematical function from "Functions" list available in pull down button and then click on![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button, a new response surface is generated based on the equation across DOE runs outputs as shown in below Fig. 54.1.61. Each output variable has a specific identifier defined in parenthesis () before the output variable name as shown in Fig. 54.1.61. that need to be used in equation definition to represent that output variable.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0057.jpg' | relative_url }})

Composite response surface control window

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0058.jpg' | relative_url }})

Composite response surface for pass/fail

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0059.jpg' | relative_url }})

Composite response surface for weighted sum

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0060.jpg' | relative_url }})

Composite response surface for penalized weighted sum   

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0061.jpg' | relative_url }})

Composite response surface for user defined equation

#### **2D Response Contour**![]({{ '/assets/icons/post_icons/doe_post_response_contour_button.jpg' | relative_url }})****

In Response contour a 2D response surface is plotted along with coloured contour based on the magnitude of the output variable, color bar indicates magnitude of the output variable. 2D response contour plot can be plotted using icon ![]({{ '/assets/icons/post_icons/doe_post_response_contour_button.jpg' | relative_url }}) and options are similar to 3D response surface except that plot is in 2D along with the contour based on magnitude of the output variable. User can select output variable, X and Y axis DOE input study variable, response surface types and user scale from controls window. Typical 2D response surface with contour is as shown in Fig. 54.1.62., Fig. 54.1.63., Fig. 54.1.64. and Fig. 54.1.65.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0062.jpg' | relative_url }})

Composite response contour for pass/fail

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0063.jpg' | relative_url }})

Composite response contour for weighted sum

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0064.jpg' | relative_url }})

Composite response contour for penalized weighted sum

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0065.jpg' | relative_url }})

Composite response contour for user defined equation

####   
Tornado Chart ![]({{ '/assets/icons/post_icons/doe_post_tornado_chart.jpg' | relative_url }})

Tornado chart shows the Relative Magnitude and Direction of Influence of DOE study variables on the selected output variable. These graphs are variation of a bar graph used to show the relative sensitivity of an output to uncertain (or variable) inputs. They are normally centred over a vertical zero-point axis when sensitivity is measured by a correlation or normalized regression coefficient (See Fig. 54.1.66.). Bars extending to the right indicate a positive relationship with the select output bars extending to the left of the zero-axis indicate a negative relationship.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0066.jpg' | relative_url }})

Tornado Chart

The length of the bars indicates the relative strength of the positive or negative relationship. It is calculated using **Spearman Rank Order Correlation Coefficient (ρ)** as shown in the above Fig. 54.1.66.

The control window for Tornado chart is shown in Fig. 54.1.67. User can select the output variable from drop-down menu or from the DOE Output tree and exclude the failed constraint DOE runs by turning on Exclude Failed constraint Runs checkbox from controls window.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0067.jpg' | relative_url }})

Tornado controls window

####   
  
Sensitivity Plot ![]({{ '/assets/icons/post_icons/doe_post_sensitivity_plot_button.jpg' | relative_url }})

Sensitivity plot shows the effect of each DOE study input variables on selected output variable as slope (See Fig. 54.1.68.). Each curve has a correlation between DOE study variable and selected output variable.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0068.jpg' | relative_url }})

Sensitivity Plot

The Control window for sensitivity plot is shown in Fig. 54.1.69. User can select the output variable from drop-down menu and exclude the failed constraint DOE runs if required by turning on Exclude Failed constraint Runs check box from controls window.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0069.jpg' | relative_url }})

Sensitivity controls window

####   
Scatter Plot ![]({{ '/assets/icons/post_icons/doe_post_scatter_plot_button.jpg' | relative_url }})

Scatter plot (See Fig. 54.1.70.) shows correlation between DOE study input variable and selected output variable by linear regression along with sampling points.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0070.jpg' | relative_url }})

Scatter Plot

  
The control window for Scatter plot is shown in Fig. 54.1.71. User can select the input and output variables from control window and even exclude the failed constraint runs by turning on the Exclude Failed Constraint Runs check box. User defined scale can be used to observe the output state variable in interested range. ![]({{ '/assets/icons/post_icons/doe_post_apply_to_all_button.jpg' | relative_url }}) button can be used to apply the same scale for the output variable to plots in other viewports. User have option to hide/show the selected Run in display window using right click on the specific run on scatter plot display as shown in [Fig. 54.1.72.](54_1_doe_post_processor.htm#Fig_54_1_72_Scatter_plot_Show/hide_selected_Run)

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0071.jpg' | relative_url }})

Scatter plot controls window

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0072.jpg' | relative_url }})

Scatter plot Show/hide selected Run

#### Histogram Plot ![]({{ '/assets/icons/post_icons/doe_post_histogram_button.jpg' | relative_url }})

Histogram plot (See Fig. 54.1.73.) shows the frequency of the DOE runs that fall within small ranges of output variables values. So, histogram displays Number of DOE runs Vs Selected output variable bar graph. 

User can select the output variable from control window "Output" pull down button in property space or from DOE Output tree. User can change the Histogram display by varying "Number of bins" for the wider or smaller variable ranges selection. Even “User defined” scale can be used to observe the state variable in interested range and exclude the failed cases using Check box option as shown in Fig. 54.1.74. ![]({{ '/assets/icons/post_icons/doe_post_apply_to_all_button.jpg' | relative_url }})button can be used to apply the same scale for the output variable to plots in other viewports.

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0073.jpg' | relative_url }})

Histogram Plot

![]({{ '/assets/images/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/image0074.jpg' | relative_url }})

Histogram plot control window
