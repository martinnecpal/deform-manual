---
lang: sk
title: "Appendix III: Running DEFORM in text mode"
---

# Appendix III: Running DEFORM in text mode

  
AIII.1. Assembling input data

AIII.2. Brief Introduction to Keywords

AIII.3. Help For Optimization Users

AIII.4. Running a Simulation

AIII.5. Extracting the Results

DEFORM contains text based modules which can be used to set up and run simulations in automatic mode without going through the graphic user interface (GUI). The text based preprocessor DEF_PRE.EXE can be used to assemble input data and generate a DEFORM database. It contains most of the same functionality of the graphic interface. The job can be submitted by calling the simulation control script DEF_ARM_CTL.COM.

## Assembling input data

The preprocessor can be controlled by redirecting a text input control file to the following program.

C:\Program Files\SFTC\DEFORM\v*_*\3D\DEF_PRE.EXE < DEF_PRE_INP.txt

Where

*_* is the version number of the DEFORM

DEF_PRE_INP.txt contains the following lines:

<CR>

2

1

DEF_COMMANDS.KEY

<CR>

E

E

Y

<CR>

Which are the user inputs if the text based system were run in interactive mode.

The file DEF_COMMANDS.KEY contains a series of “Action Keywords” which trigger the preprocessor to perform a series of options. (The file name is the users choice). Action keywords are documented separately. It also can contain standard keywords to define simulation controls. (time stepping, stopping controls, etc)

An important function of action keywords is to trigger the input of other keyword files, which can include geometry definition, boundary conditions, etc.

Sample contents of the DEF_COMMANDS.KEY file. Contents of an actual file will be defined by the user.

KFREAD

DEFAULT.KEY

CURSIM 1

SIMNAM

Solution

DTMAX 0.001

DTPMAX 10 0.01 100

STPINC 10

KFREAD

DEF_MESH.KEY

KFREAD

DEF_EDGE_BCF.KEY

NDTMP 1 0 70.0

TMAX 10800

ENVTMP 2130

KFREAD

AIR_BC.KEY

USRSUB 1 1

GENDB 2

DEFORM_DEMO.DB

This file:

Reads DEFAULT.KEY which contains default problem settings

Sets the operation number to 1

Sets temperature substepping and save increment

Reads DEF_MESH.KEY

Reads DEF_EDGE_BCF.KEY which contains boundary condition definitions

Sets the temperature of all nodes to 70 degrees

Sets simulation time

Sets environment temperature

Loads AIR_BC.KEY which contains convection coefficients for air

Defines a user subroutine to be used

Generates a database called DEFORM_DEMO.DB.

## Brief Introduction to Keywords

There are two different types of keywords that can be read by the [Preprocessor](/docs/sk/pre_processor/7_introduction_to_pre-processor/): Input keywords and Action keywords. Input keywords contain data that is directly used as data for a simulation. This can be a geometry definition, convection coefficient values, or other such data. Action keywords perform certain operations when the Preprocessor is reading the data. For example, the keyword [KFREAD](/docs/sk/keyword_documentation/k/kfread/) tells the Preprocessor to read the next line into the Preprocessor as a keyword file. This is quite useful for segregating data into different keyword files and being able to load them in a modular manner into the Preprocessor. The most commonly used Action keywords are [KFREAD](/docs/sk/keyword_documentation/k/kfread/) (keyword file reading), [DBREAD](/docs/sk/keyword_documentation/d/dbread/) (database file reading), [GENCTC](/docs/sk/keyword_documentation/g/genctc/) (generate contact based on proximity distance to dies), and [GENDB](/docs/sk/keyword_documentation/g/gendb/) (generate database). All the keywords are referenced with their specification method in the keyword reference.

## Help For Optimization Users

In the case where optimization being performed, many simulations have to be run sequentially. In this case, it means that the input data will have to change each time a simulation is run. This can be done by segregating the data into different keyword files and loading the all together at the initialization phase. For example, consider the case where the heat flux is different between each simulation. As long as that is the only difference between each run, the initial data can be stored in a keyword file and the heat flux data can be stored in another keyword file (or created on the fly by the optimization script).

This can be done in a few easy steps:

  1. Define the simulation and save it in a keyword without the heat flux definition.

  2. Read the definition of heat flux in the keyword manual (keyword: ECHFLX).

  3. Define a keyword file with the heat flux data. An easy cheat would be to define it in the graphical preprocessor, save it to a keyword file, extract it from the saved keyword, and modify it as necessary during run time.

  4. Run a simple script file as above that loads in both keyword files and generates a database.

## Running a Simulation

(1)**Direct Job Submission** : 

(Note: the following text should be entered in a single line)

“C:\Program Files\SFTC\DEFORM\v12.1.1\DEF_SIMULATION.EXE”

ENV_PROBLEM_ID_TAG=TEST.DB

ENV_RUNNING_DIRCTORY_TAG="C:\Users\deform\Documents\PROBLEM\TEST"

ENV_JOB_DIMENSION_TAG=3 ENV_JOB_TYPE_TAG=E_MO_JOB

(2) **Text line Batch Queue submission** : (from version 11.1 SP1)

(Note: the following text is a single line)

"**C:\Program Files\SFTC\DEFORM\Configuration\SimClient.EXE** " -submit

<PROBLEM_PATH> <PROBLEM_ID> <PROBLEM_TYPE> <PROBLEM_DIMENSION> <SIMULATION_SERVER> <CLIENT_TYPE> <VERSION_NUMBER>

**Problem type can be** : MO, DOE, OPT

**Problem dimension can be** : 2, 3, 23

**Simulation Server** : one or more simulation server names 

(For DOE/OPT, multiple simulation servers can be used)

To specify multiple simulation server, the server name need to be separated with ',' and enclosed with double quote. eg. "SimulationServer1,SimulationServer2".

**Client type can be** : QT3, QT4 

(use QT4 only if the problem has been submitted with Qt4 run option dialog before)

**DEFORM Version number can be** : "11.1", "11.0", "0.0" 

(0.0 for version before 11.0)

(3) **Post-processing with a DEFORM Session (.ds) file**.

(Note: the following text is a single line)

“**C:\Program Files\SFTC\DEFORM\v12.1.1\DEF_GUI_PST.EXE** ” -b FileName.DS -d ProbID.DB

.DS file can be created interactively by post-processor.

## Extracting the Results

There are two ways of performing this action: the text-based [Preprocessor](/docs/sk/pre_processor/7_introduction_to_pre-processor/) and the text-based [Postprocessor](/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/). Which one is used depends on the desired output. The most brute-force but straightforward operation is to open the text-based preprocessor, load the last step of the database and save the data as a keyword file. This keyword file can then be parsed for any required information such as node temperatures (keyword: [NDTMP](/docs/sk/keyword_documentation/n/ndtmp/)). The action keyword that allows the user to read a database file is [DBREAD](/docs/sk/keyword_documentation/d/dbread/) and the action keyword that allows the user to write a keyword file out is [KFWRIT](/docs/sk/keyword_documentation/k/kfwrit/) that is specified the same manner as the [KFREAD](/docs/sk/keyword_documentation/k/kfread/) keyword. The keyword file can be read as in the case of assembling the input data as such:

DBREAD 0

DEFORM_DEMO.DB

KFWRIT

OUTPUT.KEY

The DEF_PRE_INP.txt would be the same where the DEF_COMMANDS.KEY file would contain the four lines above. The last step of the database would be read and stored in the keyword file named OUTPUT.KEY.

**Related Topics:**

1\. [Basic File System](/docs/sk/about_deform/1_introduction_to_deform/1_10_basic_file_system/)

2\. [Preprocessor](/docs/sk/pre_processor/7_introduction_to_pre-processor/)

3\. [Simulation](/docs/sk/simulator/23_deform_simulator/23_introduction_to_deform_simulator/)

4\. [Post Processor](/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)
