---
lang: sk
title: "56.4. User-Defined Post-Processing Routines"
---

# 56.4. User-Defined Post-Processing Routines

56.4.1. User defined post-processing (USRVAR)

56.4.2. Compiling user routines on Linux

56.4.3. Compiling user routines on Windows

56.4.4. Running the modified post-processor in LINUX

56.4.5. Running the modified post-processor in Windows

In the post-processor, user defined post-processing routines can be used to calculate field variables using the steps stored in the database. The manner in which these values are computed is based on creating a shared library file to compute variables based on the variables stored in the database. To implement user-defined post-processing variables,

  1. The user defined post processor source file is available on in the $DEFORM_DIR/USR subdirectory of DEFORM install folder on Linux. In case of PC this file is available in the installation folder (such as c:\Program Files\SFTC\DEFORM\v11.1\UserRoutine\PostProcessor). User should make a local copy of this folder and the file PSTUSR23.FOR (Linux) or pstusr23.f (on Windows ) can be edited to compute the user defined post variables.

  2. After editing, this file can be compiled and linked as a shared object file (LINUX) or a dynamically-linked library (Windows).

  3. This shared library can be called by going to the User Variable dialog from the post processor. User can browse for the compiled dll file (Windows) or SL file (Linux) and select the library that was built. After this, go back to the tracking window and press the Track Data button.

  4. After the data has been tracked, go to the State Variables window and select the USR tab and then the state variables can be plotted to User Variables.

**Note** :

User-defined Post-Processor routines can only use data that was saved in the database. If a very coarse step increment was made, variables having a cumulative effect can have considerable error.

**User defined post-processing routines:**

User defined post-processing can be used to generate plots of user variables after running a simulation. It uses the steps that are stored in the database and any type of variable can be plotted in the post-processor for these steps. The calculation of this variable is done using a FORTRAN program PSTUSR23.FOR which is stored in the $DEFORM_DIR/USR directory. It is important to note that these variables do not affect the results of the simulation.

There are 10 user defined routines, each of these can be used to calculate 20 different user variables.

Some applications of user variables are to evaluate the micro-structure after the simulation, to predict the hardness, yield strength of different regions of the forged part, to evaluate failure using a critical damage value, calculate the cooling rate, etc.

## User defined post-processing (USRVAR)

The user defined post-processing routines have to be written using FORTRAN in the file PSTUSR23.FOR. When user variable tracking is done the functions in this FORTRAN program are called for the steps that have been selected in the post-processor. The user function is evaluated at each node/element of the object for which the variables are tracked. The user subroutine is called at the beginning of tracking to get the variable names, then at the first step to get the initial values for all variables and then called for all the steps present in the database being tracked. There are three phases in the tracking process:

**PHASE 1**

The user variable function is called with the INIT flag set to to "0". This is done once before tracking is started. During this phase the variables names (VNAME) should be defined so that they can be displayed in plots on the screen. The variables for which "VNAME" is defined are tracked.

For easier identification purpose, it is recommended that proper name or descriptions be assigned to "VNAME". This can be done when the user subroutine is called with INIT = 0 as shown below :

IF(INIT.EQ.0) THEN

VNAME(1) = 'User Example-1'

VNAME(2) = 'User Example-2'

VNAME(3) = 'User Example-3'

VNAME(4) = 'User Example-4'

VNAME(5) = 'User Example-5'

RETURN

ENDIF

**PHASE 2**

The user variable function is then called with INIT flag set to "1". This is the second phase in which all user variables have to be initialized to their starting values. This is called at the first step in the list of steps which are being tracked (ISTEP equals to the starting step) for each node/element in the object.

IF(INIT.EQ.1) THEN

VAR2(1)= (STS(1)+STS(2)+STS(3))/3.

VAR2(2)=EFEPS

VAR2(3)=0.0

VAR2(4)=0.0

VAR2(5)=0.0

RETURN

ENDIF

If the initial value of a variable is zero the this is defined using the following code (Here variable 5 is used)

VAR2(5) = 0.

If the maximum value of a variable is being tracked (for example temperature) then this value can be set to (Here variable 5 is used).

VAR2(5) = -10000

and then checked and increased if temperature at any step is greater than this.

**PHASE 3**

The user variable function is called with the INIT flag set to "2" in the phase in which all calculations of the user variables are done. This function is called for all steps for each node/element of the object and the user is expected to update the values of the state variables based on the inputs passed to this program. The inputs to the function (pstusr2.f, subroutine USRVAR) are:

C *** INPUT ***

C

C TNOW : Current time

C DTMAX : Max time step when set in simulation controls

C : TNOW between successive steps can also be

C : used to compute time step size.

C RZ : Element center coord.

C TEMP : Temperature

C EFEPS : Effective strain rate

C TEPS : Total accumulated strain

C EFSTS : Effective stress

C DAMGE : Damge factor

C RDTY : Relative density

C STS : Stress tensor

C EPS : Strain rate tensor

C TSR : Strain tensor

C WEAR(5) : WEAR(1)=Interface temperature on master object nodes

C : WEAR(2)=Sliding velocity on master object nodes

C : WEAR(3)=Interface pressure on master object nodes

C

C ATOM : Dominating Atom Contents

C NTMATR : Number of Material Phases

C VF : Volume Fraction

C VFN : Transformation Starting Volume Fraction

C

C VAR1(1-95) : Initial state variables

C VAR2(1-95) : Updated state variables

C VNAME(1-95) : Name for each variables

C ISTEP : Step number

C INIT : Flag for Different Operations

C 0 - Define characteristic of the subroutine

C 1 - Initialize User Defined Variables

C (Initial Step)

C 2 - Calculate User Defined Variables

C (Subsequent Steps)

C IOBJ : Object number in current object

C NUMNP : Number of nodes in current object (when INIT=1,2)

C NUMEL : Number of elements in current object (when INIT=1,2)

C ICURNE : Current node/element number in object (when INIT=1,2)

C (depending on tracking at node or element)

C*************************************************

C ************ The following variable structure is available only if the definitions

C are set in .als file and point to PC_USRVAR2 routine, these details

C are available in PC_pstusr23.f (…/v11.0/UserRoutine/PostProcessor)

C in the comments section.

C ATOM : Dominating Atom Contents (available in the integrated system only)

C NTMATR:Number of Material Phases (available in the integrated system only)

C VF : Volume Fraction (available in the integrated system only)

C VFN : Transformation Starting Volume Fraction (available in the integrated

C system only)

C*************************************************

C

In the example given below the maximum mean stress is stored in the first variable, the maximum strain rate is stored in the second variable.

IF(INIT.EQ.2) THEN

STSM = (STS(1)+STS(2)+STS(3))/3.

IF(STSM.GT.VAR1(1)) THEN

VAR2(1)=STSM

ELSE

VAR2(1)=VAR1(1)

ENDIF

IF(EFEPS.GT.VAR1(2)) THEN

VAR2(2)=EFEPS

ELSE

VAR2(2)=VAR1(1)

ENDIF

VAR2(3) = VAR1(3)

VAR2(4) = VAR1(4)

VAR2(5) = VAR1(5)

ENDIF

In the statement to check for INIT = 2, each user variable is checked with some criterion, if it meets this then the value is updated, else the new value is set the same as the previous value VAR1. It is very important that if the value is not updated, the value is set to the VAR1 value as this allows tracking of variables across remeshing steps where data is interpolated from an old mesh to a new mesh.

Since this calculation is done for each step and for each node/element the code should be written efficiently. You should not open close files for each subroutine call as this can degrade performance. The /DATA/ statements in FORTRAN can be used to store parameters and the /COMMON/ block fields can be used to hold static data. If files are to be opened then use UNIT numbers from 91..99 for opening these files as opening other unit numbers might clash with files opened in other parts of the program.

The mesh number should always be incriminated when there is a change in the mesh. If a remeshing step has been purged from a database then user-variable tracking will not work with the database.

## Compiling user routines on Linux

After the code has been modified the new TEXT based post-processor and the shared dynamic library for the GUI post-processor have to be generated using the script DEF_INS.COM. If you wish to make a local copy of the code then copy all files from the $DEFORM_DIR/USR directory to your local directory. Then run the script build_pst using the following command:

> build_pst23

(Please note that these build scripts may not work consistently across all the varieties of the operating systems, in the event of any issues with the above indicated scripts, please use the lower level script called 'DEF_INS23.COM' and follow the system prompts to complete this building)

This builds a new copy of the post-processor DEF_PST.EXE in the local directory and also builds DEF_PST23.SL, a shared library that can be used with the GUI post-processor.

After this process is completed then the new variables can be accessed from the text-based and GUI post-processors. In the GUI based post-processor, when tracking of user variables is done, a post-processor database (PDB) is generated for the values of the tracked variables. If the same data is to be viewed again in the post-processor, after loading the database, the post-processor database can be loaded to view the data. This saves the time required to track these variables again.

## Compiling user routines on Windows

Like in the Linux environment, make local copy of the folder PostProcessor (from the install structure e.g c:\Program Files\SFTC\DEFORM\v11.1\UserRoutine) and using the build scripts provided (USR_DEF_PST23.amake or USR_DEF_PST23.atools in the Absoft compiler or using the batch file build_usr_def_pst23_Absoftv110.bat) users locally modified user post processor file pstusr2.f, user can generate the required dll file.

FILES PROVIDED BY SFTC: (in the installation folder … v11.1\UserRoutine\PostProcessor)

  1. Files needed by the project scripts

\- Pstusr23.f

\- PC_pstusr23.f

\- PC_pstusr23.als

\- PC_pstusr23.xps

  1. Project/build files that can be used from the Absoft compiler interface

\- USR_DEF_PST23.amake

or

\- USR_DEF_PST23.atools

or if the Absoft compiler environment is set up

\- build_usr_def_pst23_Absoftv110.bat

##  Running the modified post-processor in LINUX

The GUI post-processor looks for the shared library DEF_PST23.SL first in the current working directory (or can browse for the location of this file from the post processor) then in the users HOME directory under the subdirectory DEFORM and then in the DEFORM_DIR/USR directory. It reads this shared library and displays the list of existing variables which can be tracked. In User Variables dialog the routine number, the object for which tracking is to be done, and the option to track at the node or element can be selected to carry out tracking. Once tracking is carried out all the data is stored in a post-processor database (PDB) file. Variables can then be plotted by selecting the variables in the State Variables menu.

## Running the modified post-processor in Windows

The Post-processor provides the "User Defined Variable Tracking" option to select the dynamic link library DLL file complied from Absoft and generate the post-processor database (PDB) with user defined variables in post user routine. (See Fig. 56.4.1.)

![]({{ '/assets/images/user_routines/56_4_user-defined_post-processing_routines/image0001.jpg' | relative_url }})

Post user variables tracking user interface

For detailed steps to use this user interface refer section [26.6.13. Set User Defined Variable Tracking.](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_13_set_user_defined_variable_tracking/)

**Related Topics:**

[56.1. Introduction to User Routines](/docs/sk/user_routines/56_user_routines_in_deform/56_1_introduction_to_user_routines/)

[56.2. 2D User Defined FEM Routines](/docs/sk/user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines/)

[56 3 3D User Defined FEM Routines](/docs/sk/user_routines/56_user_routines_in_deform/56_3_3d_user_defined_fem_routines/)
