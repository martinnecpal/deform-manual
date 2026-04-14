---
lang: en
title: "Tool Life Study Lab1"
---

# Tool Life Study Lab1

1.1. Introduction

1.2. Creating a New problem

1.2.1. Adding Tool life study

1.2.2. Objects definition

1.2.2.1. Top Die

1.2.2.2. Bottom Die

[1.2.3. SS Temperature/Wear](tool_life_study_lab1.htm#1_2_3_SS_Temperature/Wear)

1.2.3.1. Data Extraction

1.2.3.2. Curve fitting

1.2.3.3. Simulation Controls

1.2.4. Fatigue

1.2.4.1. Cycle selection

1.2.4.2. Simulation controls

1.2.5. Generate Database

1.2.6. Running simulation

1.2.7. Post Processing

1.2.7.1 Tool Life Post

## Introduction

Tool life impacts manufacturing cost. It is determined by many factors such as tool temperature, tool wear, tool fatigue and so on. In the Tool Life Module, we perform steady-state temperature, tool wear prediction and multi-step die stress calculation in the preprocessor which will be used for fatigue analysis in the postprocessor.

In this lab, we will be copying already simulated 2D Spike project that has a forming operation simulated over 5 cycles with tool wear calculation for dies.

## Creating a New problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button, select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. TLSL1.1. Select "**Integrated Manufacturing Process** " radio button and **Unit** system as "**SI** " using radio button. Define Problem Name as "**2D_Tool_Life_Study** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0001.jpg' | relative_url }})

Problem type selection window

  
Multiple operation wizard will open with the New Project dialog as shown in Fig. TLSL1.2., at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use ‘**2D_Tool_Life_Study** ’ as the project name. We will import already simulated 2D project “2D_Tool_Life_Study” from 2D/LABS/ installation folder using “Copy existing Project” option. 

Select “**Copy existing project** ” radio button in New Project dialog, then click on Source location and browse the “**2D_Tool_Life_Study.moproj** ” file from 2D\LABS\2D_Tool_Life_Study installation folder using ![]({{ '/assets/icons/pre_icons/mo_browse_button.jpg' | relative_url }}) button. Turn on “**Copy database file** ” check box as shown in Fig. TLSL1.2. so that database file is copied along with the project file. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation. The loaded MO project is as shown in Fig. TLSL1.3.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0002.jpg' | relative_url }})

MO wizard New Project with Copy existing project option

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0003.jpg' | relative_url }})

Copied 2D_Tool_Life_Study project Loaded in MO wizard

### Adding Tool life study

Click on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) (Add new study) button and select “**Add Tool Life Study** ” option as shown in Fig. TLSL1.4. Added Tool life study is as shown in Fig. TLSL1.5.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0004.jpg' | relative_url }})

Adding Tool life study

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0005.jpg' | relative_url }})

Added Tool life study operation in MO.

The die objects are loaded from Forming operation. There are three options in Task Item,

  * Steady state temperature, 

  * Tool Wear and 

  * Fatigue

  
The first two options, Steady state temperature and Tool Wear, will predict the steady-state temperature and tool wear based on the history data from Forming operation. The Fatigue option will activate multiple step die stress study and use the stress data to perform Fatigue analysis in the post processor. In this example, we will select all the three options. Notice that as we update the task item options, the operation tree will be also updated, as shown in Fig. TLSL1.6.

  
In Task Item, make sure Steady state temperature, Tool Wear and Fatigue check boxes are in checked status and then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object page.

  
**Note** :   
• The dies which are studied for Steady-State temperature and Tool wear must be meshed in nominal setup, for Fatigue-only task mesh in nominal setup is not required.

• “Define model to calculate tool wear” checkbox must be turned on in inter-object relations of nominal setup for dies whose tool wear will be studied.

• Tool life study can be executed only for one forming operation and that forming operation must be in cycle in nominal setup to execute Tool life study.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0006.jpg' | relative_url }})

Task Item Update

### Objects definition

We will use all dies object from “Forming” operation for tool life study in this lab, so click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top Die page.

#### Top Die

Fig. TLSL1.7. shows the object page of top die. For each object, we also have three options – steady state temperature, tool wear and fatigue. This allows us to choose if a specific analysis is needed/excluded for the current object. In this lab, we will keep the default selection and perform all the three tasks for each die object. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until BCC page.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0007.jpg' | relative_url }})

Top Die object page

##### Top Die Boundary Conditions

Apply Velocity boundary condition (Vy=0) for Top die on Top surface as shown in Fig. TLSL1.8. Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0008.jpg' | relative_url }})

Assigned Velocity (Vy=0) boundary condition for Top die

#### Bottom Die

In this lab, we will keep the default selection and perform all the three tasks for each die object. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until BCC page.

##### Bottom Die Boundary conditions

Apply Vx=0 velocity boundary condition on the symmetry surface and Vy=0 velocity boundary condition for Bottom die on Bottom surface as shown in Fig. TLSL1.9. Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until SS Temperature/Wear page.

  
![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0009.jpg' | relative_url }})

Assigned Velocity boundary condition for Bottom die

### SS Temperature/Wear

Now we are going to setup the steady state temperature and tool wear simulation. The idea is to extract heat flux/wear from the contact area with workpiece and fit the data using exponential functions. And then, impose the fitted data on the die objects and run heat transfer simulation for a sufficiently longer period until the convergence of thermal state.

#### Data Extraction

Click on **Data Extraction** from Operation tree, click on ![]({{ '/assets/icons/pre_icons/mo_extract_data_button.jpg' | relative_url }}) button to start extracting heat flux/wear from the contact area with workpiece. The progress bar in Data Extraction page shows the progress of extracting heat flux and wear from the contact area of the die objects. Once the extraction and fitting are complete, we can see the fitted coefficients in the curve fitting page. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Curve Fitting page.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0010.jpg' | relative_url }})

Data Extraction page

#### Curve fitting

We can check the contacted area and the fitted curve by clicking on the ![]({{ '/assets/icons/pre_icons/mo_visible.jpg' | relative_url }}) icon as shown in Fig. TLSL1.11. Meanwhile, Intermediate and final result files will be generated and saved in Operations/Task00004 directory, which includes two subfolders – HeatFlux and ToolWear storing the results for heat flux extraction and tool wear extraction respectively, and OutputForPredict.KEY which is the object keyword file containing the fitted coefficients. 

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0011.jpg' | relative_url }})

Curve Fitting page

#### Simulation Controls

We set up the simulation control parameters for steady state temperature prediction, which involves heat transfer simulation on the die objects with heat flux BCC using the fitted coefficients. As shown in Fig. TLSL1.12. we only need to define three parameters - # of cycles to predict (total time will be calculated automatically based on process time of the forming operation which is in cycle), either time step or total steps and step increment. The default # of cycles to predict is set to be 10 times of the number of cycles in the forming operation, which is 50 in this case. In this lab, we will use **# of cycles** to predict as **50** with **time****step** as **0.0100093** sec/step and **step increment** as **1** as shown in Fig. TLSL1.12.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0012.jpg' | relative_url }})

Temp Simulation controls page

### Fatigue

The final task in the preprocessor is Fatigue, which is essentially setting up die stress calculation at multiple steps from cycle operation. The first step is to select cycles from the forming operation to perform die stress calculation (see Fig. TLSL1.13.). We can either select the last cycle from the database, all cycles or select cycles incrementally. We will also need to set up simulation control parameters for die stress calculation (see Fig. TLSL1.14.). 

#### Cycle selection

Select “**Cycle********Selection** ” under Fatigue from Operation tree, make sure by default “**Last****cycle** ” is selected as shown in Fig. TLSL1.13. If not selected, then select “**Last****cycle** ” radio button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Simulation controls page. 

  
![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0013.jpg' | relative_url }})

Cycle selection page

#### Simulation controls

In Simulation controls, we will use default **Number of simulation steps** as **1** , **Step increment to save** as **1** and **Time per step** as **1e-06** as shown in Fig. TLSL1.14. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0014.jpg' | relative_url }})

Fatigue- Simulation controls page

### Generate Database

As we click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB, we will get Data Extraction popup while loading generate DB page as shown in Fig. TLSL1.15. Select ![]({{ '/assets/icons/pre_icons/mo_no_button.jpg' | relative_url }}) in the popup since we had already done the data extraction.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0015.jpg' | relative_url }})

Data Extraction popup

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check if there are any errors or warnings that would stop DB generation. Generate the database if there are no errors or warnings by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label (see Fig. TLSL1.16.). 

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0016.jpg' | relative_url }})

Generate Database window

### Running simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. TLSL1.17. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0017.jpg' | relative_url }})

Run Options Popup

The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. If ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

  
The Message file provides information about which simulation step the simulation is currently on and information regarding how well the simulation is running as shown in Fig. TLSL1.18.

  
![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0018.jpg' | relative_url }})

Simulation mode

### Post Processing

After the simulation is completed, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab to visit MO post processor. The simulated results can be seen in Post ( Fig. TLSL1.19.). It contains two parts, one is the temperature history from running heat transfer with imposed heat flux BCC and the other is the die stress. 

  
The steady state heat transfer analysis and tool wear analysis steps are grouped under simulation name SS Temp. Here the simulation name **Fatigue-Step52** means the die stress result from step 52 in the forming operation. There is a highlighted toolbox used for fatigue analysis based on the calculated die stress data. Fig. TLSL1.19. summarizes the simulation results of temperature and die stresses from SS Temperature prediction and multi-step die stress study. We take the last step from heat transfer simulation as the steady-state temperature and impose it on the die objects while running die stress calculation. Note that if we select fatigue as the only task, we will impose the temperature profile from the corresponding steps from the forming operation as initial temperature.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0019.jpg' | relative_url }})

MO Post – Fatigue -Step52 

Click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button in Step browser, then Play animation from first step with Temperature State Variable to observe the die temperature as they approach steady state. 

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0020.jpg' | relative_url }})

Simulation Results 

#### Tool Life Post

Tool Life Post is used for analysis of steady-state temperature and tool wear results, as well as fatigue life prediction of dies. From MO post, we can access Tool life post by clicking on ![]({{ '/assets/icons/post_icons/mo_tool_life_post_icon.jpg' | relative_url }}) button as shown in Fig. TLSL1.19. Tool life post is opened as shown in Fig. TLSL1.21

  
**SS Temp & Wear**: By selecting this option, we can plot the results for SS Temp & Wear operation (See Fig. TLSL1.21.). Under this option, we can plot Tool temperature, Tool wear depth, tool wear rate and Worn geometry output for selected Cycle no. 

  
We can select the different cycle number under **Cycle section** by dragging sliding bar or by entering the respective cycle number in input field. Once you enter the cycle number, user can select one of tool wear results to view the results in display, Fig. TLSL1.22 shows Tool Wear depth at Cycle 40. 

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0021.jpg' | relative_url }})

Tool life results for SS Temp & Wear

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0022.jpg' | relative_url }})

Tool wear rate result at Cycle 40

  
**Fatigue** : By selecting this option, we can plot the results for Fatigue operation (See Fig. TLSL1.23.). Initially there will not be any fatigue model in the list. We can add fatigue model by clicking the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button. The model named “**AISI****-1025:****SNSD_CONST** ” is added, where AISI-1025 stands for the material name and SNSD_CONST stands for the stress-based standard model. We can observe that a Stress-based standard model is selected as Model type. We can define the model parameters by clicking the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button and a function editor will pop up. The parameters we defined for this model can be found in Fig. TLSL1.24. The other way to add fatigue model is by loading model files from a user directory or Fatigue library. Note that we need to be in Fatigue page to enable the load buttons (see Fig. TLSL1.25.). The model file has the same format as keyword file, where the keyword is followed by its value. 

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0023.jpg' | relative_url }})

Tool Life post – Fatigue output 

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0024.jpg' | relative_url }})

Fatigue model definition

  
![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0025.jpg' | relative_url }})

Loading model file

Once the model is defined, we can see the fatigue life prediction plot by selecting either Absolute Max principal or Signed Von Mises or Signed Shear as the combination method with model and clicking the ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) button. The result is shown in Fig. TLSL1. 26.

![]({{ '/assets/images/labs/tool_life_study_lab/tool_life_study_lab1/image0026.jpg' | relative_url }})

Fatigue Life Plot
