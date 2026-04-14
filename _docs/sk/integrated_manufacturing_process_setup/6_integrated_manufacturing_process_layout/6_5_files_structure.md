---
lang: sk
title: "6.5. File Structure"
---

# 6.5. File structure

6.5.1. Normal Integrated Manufacturing process (MO) Project Structure  
6.5.2. DOE Project File structure  
6.5.3. Die Stress Project File Structure  
6.5.4. Report Generation  
6.5.5. Integrated Manufacturing process (MO) Wizard and Operation specific Files  
6.5.6. Operation Specific Important Files

The primary data storage structure is the database (DB) file. The database file stores a complete set of simulation data, including object data, simulation controls, material data, and inter-object relations, both from the original input, and from selected solution steps. More information on Basic File structure of DEFORM refer chapter [1.10. Basic File system.](/docs/sk/about_deform/1_introduction_to_deform/1_10_basic_file_system/)

  
**Database (DB) files:**

The database file contains the complete simulation data set for input data and each saved simulation step. The information is stored in a compressed, machine readable format, and is accessible only through the DEFORM pre- and post-processors. As the simulation runs, data for each step is written to the end of the database file. If the step being written is specified as a step to be saved, information for the next step will be appended after the current data step. If the step is not specified to be saved, and a solution is found for the next step, the data for the current step will be overwritten by the data for the next step.

  
**Keyword (KEY) files:**

Keyword files contain specific problem definition data which is read by the pre-processor and used to create an input database file. A keyword file may contain a complete problem definition, or it may contain only specific information about, for example, a specific object or material. The information is stored in ASCII format, and can be read and edited with any text editor, such as Notepad, VI, or Emacs. A keyword reference is available which describes the data format for each keyword.

  
In Integrated Manufacturing process (MO) Projects along with DB file one of the important file called Multiple Simulation template (MST) file. MST file is created to support the concept of setting up multiple operation once by saving all the operations data separately in different keyword files and reading all these files along with project and supporting files respectively to append/generate data base necessary for each operation simulation.

## Normal Integrated Manufacturing process (MO) Project Structure

Integrated Manufacturing process (MO) project name is used as problem ID, under the main project folder directly DB, MST and other common supporting files will gets created. Other sub folders like Operations, Objects, Materials, Equipments and Lubricants folder will create inside the project folder as shown in Fig. 6.5.1.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_5_file_structure/6_5_image001.jpg' | relative_url }})

Normal Integrated Manufacturing process (MO) project structure

Operation folder contains the different Task folders for each operations naming as the order of the operation in sequence like Task00001, Task00002, ….. Task0000n where n is the maximum number of the operations added. These Task folders contain Inter-object, Mesh settings, Simulation controls and Thermal stopping controls keyword files and wizard specific files if any. Objects, Material and Lubricants folders contains the keyword file for each operations, materials and lubricants added in the MO project.  
Equipment folder contains the equipment keyword files for each operation objects even the read from DB object type will have the separate Equipment keyword file. So that user can change movement controls data for the read from DB objects and this data gets saved in and retrieved back from equipment folder.

In DOE, Optimization and Die stress MO projects the respective additional folders will create and all data files related those studies get saved in those files.

## DOE Project File structure

Adding DOE study for MO project will create DoeStudies folder, under that DOE study projects individual folders will create with name as DoeStudy1, DoeStudy2,..etc as user can add more than one DOE study projects. Doestudy data stored in three important folders those are Control, Output and Solutions. Control folder contains the Regions of interest regions Keyword file. DOE results will be automatically prepared and saved in Output folder SDB file. SDB file is mandatory to DOE post to study DOE results and user can open the DOE post from Main GUI only after selecting the SDB. (See Fig. 6.5.2.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_5_file_structure/6_5_image002.jpg' | relative_url }})

DOE Project structure

## Die Stress Project File Structure

In Die Stress Study Project similar to the DOE project DieStress folder created under Main project and this folder contains all data related to Die Stress study. Also the Die stress operation Task folder creates under Operations folder in which Die Stress wizard file DieStress.wzd will create. (See Fig. 6.5.3.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_5_file_structure/6_5_image003.jpg' | relative_url }})

Die Stress project file structure

## Report Generation

Adding Report Generation for MO project will create the Post Report Generation session DS file in project main folder directly. After simulating the report get saved in a DEF_REPORT file created under the Project folder, which contains the folder with Problem_ID containing reports in PDF and PPT formats. Also images used in the report are stored separately in Images folder at same level. (See Fig. 6.5.4. )

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_5_file_structure/6_5_image004.jpg' | relative_url }})

Report generation file structure example

## Integrated Manufacturing process (MO) Wizard and Operation specific Files

Different MO Wizards like Cogging, Heat treatment, Die Stress and Machining Distortion will create respective wizard files under those operation Task folders. These wizard files contain the wizard specific data and used during the DB generation for that wizard operation. MO wizard files are tabulated as shown in Table 6.5.1.

**Sl. No.** | **MO Wizard/Operation** | **Wizard File**  
---|---|---  
1 | Cogging | Cogging.MDT  
2 | Heat Treatment | HeatTreatWizard.HTWZ  
3 | Die Stress | DieStress.Wzd  
4 | Machining Distortion | MachDistortion.MDWZ  
  
MO wizard Files

## Operation Specific Important Files

In MO for operators like 2D to 3D convertor, Boolean and Cycle and Report generation will save these operators data in the respective operation task0000n folders. These will be called during the DB generation and simulation of the respective operations. MO Operation specific files are as shown in below [Table 6.5.2.](6_5_files_structure.htm#Table_6.5.2._MO_Operation/Operator_specific_files)

**Sl. NO.** | **MO Operations Specific files** | **Operation/Operator specific files** | **File Path**  
---|---|---|---  
1 | Report Generation | <PROBLEM_ID>.DS | Under Project main folder directly  
2 | 2D to 3D Convertor | M23_INPUT.KEY and M23_OUTPUT.KEY | Under Operation Task0000n folder  
3 | Boolean | Boolean.BWZ | Under Operation Task0000n folder  
4 | Cycle | Cycle.CWZ | Under Operation Task0000n folder  
  
MO Operation/Operator specific files

**Related Topics:**

[1.10. Basic File system.](/docs/sk/about_deform/1_introduction_to_deform/1_10_basic_file_system/)

[Appendix XVII: Data Files](/docs/sk/appendices/appendix_xvii_data_files/)
