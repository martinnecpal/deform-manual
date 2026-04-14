---
lang: sk
title: "56.3. 3D User Defined FEM Routines"
---

# 56.3. 3D User Defined FEM Routines

56.3.1. Summary of subroutines and calling structure of user-defined FEM routines

56.3.2. 3D User defined FEM routines

56.3.2.1. User defined data (USRDEF)

56.3.2.2. User defined flow stress routines (USRMTR)

56.3.2.3. User defined movement control (USRDSP)

56.3.2.4. User defined node and element value (USRUPD)

56.3.2.5. User defined damage models (USRDMG)

56.3.2.6. User defined general routine (USRMSH)

56.3.3. Compiling user routines on Linux

56.3.4. Compiling user routines on Windows

56.3.5. Running the modified FEM engine for Linux platforms

56.3.6. Running the modified FEM engine for Windows platforms

This chapter explains the various user routines available in the DEFORM system for both the FEM engine and the post-processor. Examples on how to use each type of routine, how to compile the code and how to run the modified FEM engine and post-processor are also covered.

In FEM engine user defined routines can be used for many different purposes during a simulation. Currently user routines exist for flow stress definition, movement control, calculation of user nodal values ([USRNOD](/docs/sk/keyword_documentation/u/usrnod/)), calculation of user element values ([USRELM](/docs/sk/keyword_documentation/u/usrelm/)), damage models and many other specialized needs. In the post-processor, user defined post-processing routines can be used to calculate field variables using the steps stored in the database. To implement the user routines user must have a FORTRAN compiler installed on the system where DEFORM system is running.

**User-Defined FEM Routines:**

User-Defined FEM Routines are FORTRAN subroutines in which the user can change internal routines within the DEFORM FEM engine to achieve very specialized functions within DEFORM. These subroutines can then be compiled and linked to provide object code to generate a custom built FEM engine. The user subroutines are grouped in to different fortran source files based on their functionality. These are text files containing all the available FORTRAN subroutines including all the common blocks with all the variables explained in comments. To compile this file, run the script file DEF_INS.COM (on Linux), select the routine (fem or user defined post) you would like build, and select the platform (like linux version etc..) for which you would like to build for. At this point, the FORTRAN files will be compiled and linked to the object code named DEF_SIM.OBJ (on Linux). This will then generate a new FEM engine, named DEF_SIM.EXE. As shown in [Fig. 56.3.2](56_3_3d_user_defined_fem_routines.htm#Fig_56_3_2_Description_on_how_to_compile/link_a_new_FEM_engine_On_PC) similar structure has been provided for PC environment as well, 32bit support for user-defined FEM has been stopped in Windows from v13.1 hence in PC DEF_SIM_64.EXE file will be built. This whole process is shown in [Fig. 56.3.1](56_3_3d_user_defined_fem_routines.htm#Fig_56_3_1_Description_on_how_to_compile/link_a_new_FEM_engine_On_Linux) for unix and [Fig. 56.3.2](56_3_3d_user_defined_fem_routines.htm#Fig_56_3_2_Description_on_how_to_compile/link_a_new_FEM_engine_On_PC) for PC environments.

Currently user routines exist for flow stress definition, movement control, calculation of nodal values ([USRNOD](/docs/sk/keyword_documentation/u/usrnod/)), calculation of element values ([USRELM](/docs/sk/keyword_documentation/u/usrelm/)), and for other models. For example, there are many different methods for a user to control the movement of a rigid body within DEFORM, e.g. constant velocity, mechanical press, hammer press movement, speed as a function of time. However, there are some cases where a slightly more specialized movement control is required, such as movement based on variation of state variables of the workpiece. This can be performed using user-routines since these variables are available when the movement of the rigid die is calculated.

![]({{ '/assets/images/user_routines/56_3_3d_user_defined_fem_routines/image0001.jpg' | relative_url }})

Description on how to compile/link a new FEM engine on Linux

![]({{ '/assets/images/user_routines/56_3_3d_user_defined_fem_routines/image0002.jpg' | relative_url }})

Description on how to compile/link a new 64 bit FEM engine on PC

**Options for compiling on Linux machines:**

(use the command 'uname -a' in the command window to get these details)

The user routine compilation script DEF_INS.COM needs two arguments, first argument requires the machine/operating system name and the second argument requires output type (1 for user defined FEM engine, 2 for user defined post processor shared library and 3 for user defined microstructure post processor library.

Supported machine and operating system details are listed here,

  1. centos5_32bit_linux for Centos 5.10 (kernel # 2.6.18-371, x86-64, to build 32 bit FEM using 64 bit Absoft f90 v11.0)

  2. centos5_64bit_linux for Centos 5.10 (kernel # 2.6.18-371, x86-64, to build 64 bit FEM using 64 bit Absoft f90 v11.0)

  3. centos6_32bit_linux for Centos 6.5 (kernel # 2.6.32-431, x86-64, to build 32 bit FEM using 64 bit Absoft f90 v11.0)

  4. centos6_64bit_linux for Centos 6.5 (kernel # 2.6.32-431, x86-64, to build 64 bit FEM using 64 bit Absoft f90 v11.0)

  5. suse11_32bit_linux for Suse11 sp3 (kernel # 3.0.101-0.18, x86-64, to build 32 bit FEM using 64 bit Absoft f90 v11.0)

  6. suse11_64bit_linux for Suse11 sp3 (kernel # 3.0.101-0.18, x86-64, to build 64 bit FEM using 64 bit Absoft f90 v11.0)

(Suse11 system support is on Suse Enterprise Linux Desktop operating system)

If user is using any other variations of the kernels, support is subjected to delay and can not be guaranteed.

If user is evaluating kernels different from the above list, please note that compatibility can become an issue. Please contact SFTC for advise.

It is important to work on a local copy of these user routine folders that user has full permission to operate on.

## Summary of subroutines and calling structure of user-defined FEM routines:

Here is a list of the different subroutines available to the user. With each, routine is a brief description of its purpose and the frequency of it being used by DEFORM.

  1. **USRRAT**

**Description** : This routine allows the user to define a routine to calculate incubation time and change of volume.

This routine is called in the transformation algorithm. This routine is called after each converged step. (available in _**usr_tranfkine.f**_ file)

  1. **INCUBT**

**Description** : This routine is added for convenience to complement USRRAT. This routine is called whenever INCUBT is called. (available in _**usr_tranfkine.f**_ file)

  1. **USRMTR**

**Description** : This routine allows the user to calculate flow stress of a material. This routine is called at the beginning of each iteration. (available in **usr_mtr.f** file)

  1. **UFLOW#**

**Description** : This routine is one of the many flow stress calculation routines. This routine allows the user to store many different flow stress routines in the DEF_USR.FOR and specify which routine is called in the Pre-Processor. (available in** _usr_mtr.f_** file). This routine is called each time USRMTR is called.

  1. **USRDSP**

**Description** : This routine allows the user to calculate the die speed of a rigid object that has movement defined as a user model. This routine is called at the beginning of each step. (available in _**usr_dsp.f**_ file)

  1. **DIESP#**

**Description** : This routine is called by USRDSP as a means of segregating movement routines in the same manner as the flow stress functions. This routine is called whenever USRDSP is called. (available in _**usr_dsp.f**_ file)

  1. **USPM**

This subroutine allows the user to specify parameters for densification of a porous material model. This routine is called before stiffness matrix generation which means it's called at the beginning of each iteration. (available in _**usr_pm.f**_ file)

  1. **USRUPD**

**Description** : This is the user defined nodal and element variable subroutine. This routine allows the user to calculate special state variables and store them for each node and element. These variables can be viewed in the Post-Processor or be used during the simulation in flow stress calculation. User Nodal variables are updated only at the end of a converged step. User Element variables are updated at the beginning of each iteration and at the end of a converged step. The purpose for this is that the most current user element variable can be fed into the user-defined flow stress routine. (available in _**usr_upd.f**_ file)

  1. **USRCRP**

**Description** : This routine is used to define creep rate and its derivative as a routine. This routine is available for only elasto-plastic materials. This is called upon the beginning of each iteration. (available in _**usr_crp.f**_ file)

  1. **USRMSH**

**Description** : This routine is used as a general purpose routine that has access to many internal variables within DEFORM. This routine is advocated when other routines cannot satisfy the needs of the user. This routine is called at the beginning and end of each step. (available in _**usr_msh.f**_ file)

  1. **USRDMG**

**Description** : This routine allows the user to define a special damage model. Basic stress components, effective stress and strain rate variables are available for this purpose. Additional state variables can also be made available by inserting element level common blocks. This routine is called at the end of each step once per element. (available in _**usr_dmg.f**_ file)

  1. **USERWEAR**

**Description** : This routine allows the user to compute custom defined wear rate and wear variables at the die nodes in contact with the deforming work piece. Interface temperature, sliding velocity, contact pressure, shear stress, nodal area and time step are available for this purpose. This routine is called upon the end of each step. (available in _**usr_wear.f**_ file)

  1. **USR_TRNF_KINE**

**Description** This routine allows the user to compute custom defined transformation kinetics such as change in volume fraction and updated incubation time. Available variables include temperature, stress, strain, current volume fractions of child and parent phases, incubation time and time increment. This routine is called upon the end of each step. (available in _**usr_tranfkine.f**_ file)

**Recent changes in DEFORM v11.1 to the user routine related functionality in 3D:**

**usr_msh.f**(changes from v11.0 to v11.1)

Two additional arguments are passed on to the subroutine USRMSH. These are ANGB and NANG. For each surface node in contact ANGB stores normal vector and NANG stores pointer to locate address in ANGB array for a given global node number of the surface node. If NBCD(I,J) is –n meaning node J is in contact with die ‘n’, and NANG(J)=k, then ANGB(1:3,I,K) is the normal vector to the contact surface between the workpiece and the die at node J.

(Changes from v11.1 to v11.1sp1)

Object level data for Induction heating models is now available in the common block COMMON/INDCTUSR/RINHUSR(200),INHUSRFLAG, which is available in the user subroutine USRMSH.

The available variables being

C INHUSRFLAG :0=coil input defined in DB, (default), 1=current density, 2=power, 3=voltage drop

C RINHUSR(KOBJ) : Input value for induction heating.

usr_tranfkine.f (changes from v11.0 to v11.1)

Additional variable 'IELE’ is now available which carries current (global) element number

**Recent changes in DEFORM v11.3 to the user routine related functionality in 3D:**

**usr_mat.f** (changes from v11.2 to v11.3)

Fixed a bug about user-defined consititutive model for elasto-plasitc object.

**usr_upd.f**(changes from v11.2 to v11.3)

Add 3D deformation gradient information in the USRUPD subroutine.

## 3D User defined FEM routines

This section contains a description of the different FEM user routines available in the current release of DEFORM-3D. The skeletal code for user routines is stored in different fortran files (see [Fig. 56.3.1](56_3_3d_user_defined_fem_routines.htm#Fig_56_3_1_Description_on_how_to_compile/link_a_new_FEM_engine_On_Linux) and [Fig. 56.3.2](56_3_3d_user_defined_fem_routines.htm#Fig_56_3_2_Description_on_how_to_compile/link_a_new_FEM_engine_On_PC)) which has the FORTRAN functions that the FEM engine calls if a user routine is to be used. The user routines calculates the specified values and returns output values.

### User defined data (USRDEF)

The user defined data ([USRDEF](/docs/sk/keyword_documentation/u/usrdef/)) field in the pre-processor can be used to stored data that can be used to specify parameters for the user-routines. This data can be defined in the Simulation Controls, Advanced Controls menu as shown in Fig. 56.3.3. In the user-routines the following code lets the user access the [USRDEF](/docs/sk/keyword_documentation/u/usrdef/) values common block through the variable IUSRVL. This data can be accessed from any type of user routines. This data is defined for a given model, not specific to an object or object type.

CHARACTER*80 IUSRVL

COMMON /IUSR/ IUSRVL(10)

To read and write data to the USRDEF variable the following sections of code can be used.

C TO READ DATA (10 RESERVED LINES)  
C   
READ(IUSRVL(LINE NUMBER),*) DATA1,DATA2,DATA3...  
C   
C TO WRITE DATA (10 RESERVED LINES)  
C   
WRITE(IUSRVL(LINE NUMBER),*) NEWDATA1, NEWDATA2, NEWDATA3 ...

![]({{ '/assets/images/user_routines/56_3_3d_user_defined_fem_routines/image0003.jpg' | relative_url }})

Preprocessor IUSRVL data definition from simulation controls 

### User defined flow stress routines (USRMTR)

If the flow stress models in DEFORM are not applicable for a process, a user defined flow stress can be calculated during the simulation. The flow stress can be a function of strain, strain rate, temperature, user node and user element variables. The flow stress subroutine should return the following information:

YS = FLOW STRESS  
YPS = DERIVATIVE OF FLOW STRESS W.R.T. TEPS  
FIP = DERIVATIVE OF FLOW STRESS W.R.T. EFEPS

Where

TEPS = EFFECTIVE STRAIN  
EFEPS = EFFECTIVE STRAIN RATE

A maximum of 100 flow stress routines can be defined in this program. In the pre-processor Material Properties the flow stress ([FSTRES](/docs/sk/keyword_documentation/f/fstres/)) type selected should be Advanced and the routine number to be used should be specified for each material group which uses the user routine. (See Fig. 56.3.4.) This routine number (NPTRTN)is passed to the user defined flow stress subroutine USRMTR to control branching to the specified UFLOW module.

![]({{ '/assets/images/user_routines/56_3_3d_user_defined_fem_routines/image0004.jpg' | relative_url }})

Defining user defined flow stress routine information in preprocessor

**Examples of using the user defined flow stress subroutine are given below:**

  1. The flow stress depends on the strain rate sensitivity index (PEM) and on the effective strain rate (EFEPS).

PEM = 0.1  
YS = 10. * (EFEPS)**PEM  
FIP = 10. * PEM * (EFEPS)**(PEM-1.)  
YPS = 0.

  1. The flow stress depends on the strain index (PEN), strain rate sensitivity index (PEM), the effective strain ([STRAIN](/docs/sk/keyword_documentation/s/strain/)) and the effective strain rate (EFEPS). The value of effective strain can be the element strain or from a user defined state variable. In the example given below the effective strain comes from a user defined state variable which stores the current strain. This example also illustrates the concept of using the user defined state variables to calculate flow stress.

STRAIN = USRE1(1)  
IF (STRAIN.LE.0.) STRAIN = 1.E-5  
PEN = 0.15  
PEM = 0.1  
YS = 10. * STRAIN**PEN* (EFEPS)**PEM  
FIP = 10. * STRAIN**PEN* PEM * (EFEPS)**(PEM-1.)  
YPS = 10. * PEN * STRAIN**(PEN-1.) * (EFEPS)**PEM

The UFLOW routine is called 5 or 9 times per iteration for each element (tet or brick, respectively). The calling sequence for a single element is:

  1. Guess the velocity of each node in the element.

  2. At each integation point (4 or 8 for tet or brick) calculate the strain rate.

  3. Evaluate the flow stress at each integration point using the following values.

  * Strain rate at integration point.

  * Temperature at integration point at the beginning of the step.

  * Strain = Strain at beginning of step + (Strain Rate * Time Step).

  1. Evaluate the flow stress at the center of the element using the following values

  * Strain rate at the center of the element.

  * Temperature at the center of the element at the beginning of the step.

  * Strain = Strain at the beginning of the step.

This sequence is repeated for each element. The stiffness matrix is generated and solved using these values. The solution yields a velocity correction vector, (which gives the velocity error norm) and the difference between internal and boundary forces (which gives the force error norm). When these two values have converged, the step data is written to the database, and temperature and microstructure calculations are performed, then the process is repeated from step 1.

User has access to a range of nodal and elemental data in addition to user defined variables. Comments provided in the routines explains all the variables and their meaning. Some of these are indicated here.

C INPUT :

C

C NPTRTN = FLOW STRESS NUMBER

C TEPS = EFFECTIVE STRAIN

C EFEPS = EFFECTIVE STRAIN RATE

C TEMP = TEMPERATURE

C ALSO VARIABLES IN /ELMCOM/

C

C OUTPUT :

C

C YS = FLOW STRESS

C YPS = DERIVATIVE OF FLOW STRESS W.R.T. TEPS

C FIP = DERIVATIVE OF FLOW STRESS W.R.T. EFEPS

C

COMMON /USRCTL/ DTK,KOBJ,ISTATUS,KSTEP

C

C COMMON /USRCTL/

C DTK : TIME INCREMENT

C KOBJ : OBJECT NUMBER

C KSTEP : Step Number (N)

C ISTATUS: 0 - the begain of the step

C 1 - the end of the step

C

COMMON /ELMCOM/ RZE(3,8),URZE(3,8),STSE(6),EPSE(6),EFEPSE,EFSTSE,

\+ TEPSE,RDTYE,TEMPE(8),USRE1(100),USRE2(100),

\+ DTMPE(8),NODEE(8),KELE,KONP

C

C COMMON /ELMCOM/

C RZE : NODAL POINT COORDINATES (four corner nodes)

C URZE : NODAL POINT VELOCITY (four corner nodes)

C STSE : STRESS TENSOR

C EPSE : STRAIN RATE TENSOR

C EFEPSE : EFFECTIVE STRAIN RATE

C EFSTSE : EFFECTIVE STRESS

C TEPSE : TOTAL EFFECTIVE STRAIN

C TEMPE : FOUR NODAL TEMPERATURE

C RDTYE : RELATIVE DENSITY

C USRD1 : USER DEFINED STATE VARIABLES (INPUT: AT the Beginning of STEP N)

C USRD2 : USER DEFINED STATE VARIABLES (OUTPUT: At the End of the STEP N)

C NODEE : CONNECTIVITY OF THE ELEMENT

C KELE : ELEMENT NUMBER

C KONP : NODE NUMBER PER ELEMENT

C

C WHEN (ISTATUS.EQ. 1) --> USRE2/USRN2 should be updated here

C KELE > 0 --> Element data is active

C KNODE > 0 --> Node Data is active

### User defined movement control (USRDSP)

DEFORM supports user definition of the die movement for machines which cannot be controlled using the movement mechanisms given in the DEFORM system. The die speed routines are functions which are called from the USRDSP subroutine based on the function number specified in the Object, Movement controls window as shown in Fig. 56.3.5.

![]({{ '/assets/images/user_routines/56_3_3d_user_defined_fem_routines/image0005.jpg' | relative_url }})

User defined die speed settings in Preprocessor

The die movement can be a function of the following variables :

C INPUT

C

C TIME = THE SIMULATED PROCESS TIME 

C PDIS = PRIMARY DIE DISPLACEMENT 

C VX,VY,VZ = DIE SPEED IN X, Y & Z DIRECTIONS, RESPECTIVELY 

C STRKX,STRKY,STRKZ = CURRENT DIE STROKE IN X, Y & Z DIRECTIONS,

C RESPECTIVELY

C FRZX,FRZY,FRZZ = DIE FORCE IN X, Y & Z DIRECTIONS, RESPECTIVELY

C AVGSRT = AVERAGE STRAIN RATE 

C SRTMX = MAXIMUM STRAIN RATE 

C OUTPUT

C

C UPDV = THE UPDATED DIE SPEED IN THE SPECIFIED DIRECTION 

C UPDF = THE UPDATED DIE FORCE IN THE SPECIFIED DIRECTION

C

C DTIME = CURRENT TIME STEP (I/O)

The output that the user has to provide from the user routine is :

UPDV = THE UPDATED DIE SPEED IN THE SPECIFIED DIRECTION  
UPDF = THE UPDATED DIE FORCE IN THE SPECIFIED DIRECTION  
DTIME = DESIRED TIME STEP

To use the values for AVGSRT, STRMX the primary workpiece has to be specified as the object whose average and max strain rate are required. This is the keyword PDIE(2) in _Simulation Controls, Advanced Controls in the pre-processor._

**Examples of using the user defined die movement subroutine is given below :**

**Example Case #1**

The die speed routine in DIESP1 controls the speed based on a user specified value for the average strain rate. The value of the average strain rate is specified using the USRDEF fields.

C  
C THE DIE SPEED OF THIS ROUTINE IS DETERMINED BY:  
C   
C WHERE SR IS THE APPROXIMATED STRAIN RATE DURING  
C AN UPSETTING PROCESS  
C HI IS THE INITIAL BILLET HEIGHT.  
READ(IUSRVL(1),*) HI  
STRK = STRKX*STRKX + STRKY*STRKY  
STRK = DSQRT(STRK)  
C   
C FIND the Current Height  
C   
WRITE(6,*) TMPMX  
HJ = HI - STRK  
UPDV = AVGSRT * HJ

  
The goal of this routine is to define a die velocity by the following equation:

![]({{ '/assets/equations/user_routines/56_2_2d_user_defined_fem_routines/eq_image0001.jpg' | relative_url }}) |   
---|---  
  
At the beginning of this code, a variable is fetched from our USRDEF fields, the initial height of the billet. 

READ(IUSRVL(1),*) HI

The die displacement can be computed by the following equation:

![]({{ '/assets/equations/user_routines/56_2_2d_user_defined_fem_routines/eq_image0002.jpg' | relative_url }}) |   
---|---  
  
The stroke is computed by the following code:

STRK = STRKX*STRKX + STRKY*STRKY  
STRK = DSQRT(STRK)

  
**Example Case #2**

In the case of a screwpress, the rotational energy is converted to translational motion to form a part. The process ends when the energy stored in the flywheel runs out or when the clutch on the drive mechanism is disengaged. Each step, the amount of energy may change due to energy being consumed by deforming the workpiece. The total energy is an initial condition and the change in the current energy needs to be computed each step by,

![]({{ '/assets/equations/user_routines/56_2_2d_user_defined_fem_routines/eq_image0003.jpg' | relative_url }}) |   
---|---  
  
The change in energy can simply be calculated by the following equation,

![]({{ '/assets/equations/user_routines/56_2_2d_user_defined_fem_routines/eq_image0004.jpg' | relative_url }}) |   
---|---  
  
Based on the current energy, the translational speed of the die can first be computed by calculating the rotational speed of the flywheel,

![]({{ '/assets/equations/user_routines/56_2_2d_user_defined_fem_routines/eq_image0005.jpg' | relative_url }}) |   
---|---  
  
Using the rotational speed, the translational speed can be simply determined by considering how the spindle shaft is threaded,

![]({{ '/assets/equations/user_routines/56_2_2d_user_defined_fem_routines/eq_image0006.jpg' | relative_url }}) |   
---|---  
  
This can be implemented in the following code:

DATA ENERGY/ 10000.0/

eff = 0.2

MI = 10

PI = 3.14159

diam = 1.0;

pitch = 0.1;

C This calculates the change in the energy between steps 

e_change = (FRZY * STRKY) / eff

C This updates the energy value

ENERGY = ENERGY - e_change 

C This makes sure that the energy doesn't go negative

if(ENERGY.LT.0) THEN

ENERGY = 0.0

endif

C This computes the rotational speed based on the current energy

rot_spd = SQRT((2*ENERGY)/MI)

C This converts angular speed to rotations per second

rot_spd = rot_spd / (2 * PI)

C This calculates the tranlational velocity of the screw press

V_out = rot_spd * PI * diam * sin(pitch);

C This updates the value

UPDV = V_out

### User defined node and element value (USRUPD)

The user can implement subroutines which can calculate nodal and elemental values (up to 100) during the simulation for each node/element of the objects in the simulation. The inputs are all state variables and the outputs are the values for [USRNOD](/docs/sk/keyword_documentation/u/usrnod/) and [USRELM](/docs/sk/keyword_documentation/u/usrelm/). The variables can also be used in the flow stress routines to model flow stress as a function of new state variables.

The advantage of using these variables instead of doing the same procedure using user defined post-processing is that these values are calculated for each step in the database whereas user defined post-processing is only for the steps that are stored in the database.

Data that is passed to the user variable subroutine are stored in COMMON blocks as detailed below:

C

COMMON /USRCTL/ DTK,KOBJ,ISTATUS,KSTEP

C DTK : TIME INCREMENT

C KOBJ : OBJECT NUMBER

C KSTEP : Step Number (N)

C ISTATUS: 0 - the begain of the step

C 1 - the end of the step

C

COMMON /ELMCOM/ RZE(3,8),URZE(3,8),STSE(6),EPSE(6),EFEPSE,EFSTSE,

\+ TEPSE,RDTYE,TEMPE(8),USRE1(100),USRE2(100),

\+ DTMPE(8),NODEE(8),KELE,KONP

C RZE : NODAL POINT COORDINATES (KONP corner nodes)

C URZE : NODAL POINT VELOCITIES (KONP corner nodes)

C STSE : STRESS COMPONENTS

C EPSE : STRAIN RATE COMPONENTS

C EFEPSE : EFFECTIVE STRAIN RATE

C EFSTSE : EFFECTIVE STRESS

C TEPSE : TOTAL EFFECTIVE STRAIN

C TEMPE : NODAL TEMPERATURES

C USRE1 : USER ELEMENT VARIABLES (INPUT: AT the Beginning of STEP N)

C USRE2 : USER ELEMENT STATE VARIABLES (OUTPUT: At the End of the STEP N)

C NODEE : CONNECTIVITIES OF THE ELEMENT

C KELE : ELEMENT NUMBER

C KONP : NODES PER ELEMENT

C

COMMON /ELMCOM3/ TEPS_NE(8),EFEPS_NE(8),DAMG_NE(8),STS_NE(6,8)

C TEPS_NE : Nodal eff. strain of the surrounding nodes

C EFEPS_NE : Nodal eff. strain rate of the surrounding nodes

C DAMG_NE : Nodal damage factor of the surrounding nodes

C STS_NE : Nodal stress components of the surrounding nodes

C

COMMON /NODCOM/ RZN(3),URZN(3),DRZN(3),TEMPN,DTMPN,USRN1(100),

\+ USRN2(100),KNODE

C RZN : Nodal Point Coordinates

C URZN : Nodal Point Velocities

C DRZN : Nodal Point Displacement

C TEMPN : Nodal Point Temperature

C DTMPN : Nodal Point Temperature increment from last step to current step

C USRN1 : User Nodal Variables (Input: At the beginning of Step N)

C USRN2 : User Nodal Variables (Output: At the end of Step N)

C KNODE : Node Number

C

COMMON /NODCOM3/ EFEPS_NN,TEPS_NN,DAMG_NN,STS_NN(6),IELMNOD(3)

C EFEPS_NN : Nodal effective strain rate

C TEPS_NN : Nodal effective strain

C DAMG_NN : Nodal damage factor

C STS_NN : Nodal stress components

C IELMNOD(1) = 0: Damage factor, Element definition

C > 0: ditto, Node+element definition

C IELMNOD(2) = 0: Eff. strain rate and strain, Element definition

C > 0: ditto, Node+element definition

C IELMNOD(3) = 0: Stress components (El-plastic): Element definition

C > 0: ditto, Node+element definition

C

C COMMON /ELMCOM3/

C

C WHEN (ISTATUS.EQ. 1) --> USRE2/USRN2 should be updated here or in USRMSH.

C Note:

C If a user chooses to update USRE2/USRN2 in SUB. USRMSH, he/she should also

C copy all of USRE1/USRN1 to USRE2/USRN2 here. When NUSRVE or NUSRND are

C greater than 2, more line should be added below. 

C 

C KELE > 0 --> Element data is active

C KNODE > 0 --> Node Data is active

C

C THE FOLLOWING EXAMPLES ARE:

C TO STORE THE MAX PRICIPAL STRESS IN USRE2(1), AND

C TO STORE THE STRAIN ENERGY IN USRE2(2).

C

C At present NUSRVE and NUSRND are not passed into this routine. However,

C if User Nodal and/or Elemental Variables are in use and NUSRVE or NUSRND

C are greater than 2, USRE1(3..NUSRVE) and/or USRN1(3..NUSRND) should be copied

C to USRE2(3..NUSRVE) and/or USRN2(3..NUSRND) below in the appropriate places.

C

The variable USRN1 stores the nodal variables at the beginning of the step (the current value). After computing a new value for the user defined variables the results should be stored in USRN2 at the end of each step. For the element variables, USRE1 stores the values at the beginning of the step and the updated value must be stored in USRE2.

If the variables are not being calculated, then the value stored in USRN1 and USRE1 must be copied to USRN2 and USRE2 respectively.

**Examples of using the user defined nodal and element variables are given below :**

1\. The maximum principal stress is stored in the second user element value (USRE(2)) and the first element variable is not defined.

IF (ISTATUS.EQ.1.AND.KELE.GT.0) THEN  
USRE2(1)=USRE1(1)  
CALL USR_MAXPRN(STSE,PRNSTS)  
IF (USRE2(1).LT.PRNSTS) USRE2(1) = PRNSTS  
ENDIF 

2\. In this example the average cooling rate (F/min) from 1300 F to 600 F is calculated and the result stored in the second user nodal variable (USRN2(2)). Here CURTIM is the current time in the simulation which can be accessed from the COMMON block CLOK.

COMMON /USER_DATA/ AMAX_TEMP, AMIN_TEMP, ADIF_TEMP

DATA AMAX_TEMP, AMIN_TEMP, ADIF_TEMP

$ / 1300, 600, 700 /

IF (ISTATUS.EQ.1.AND.KNODE.GT.0) THEN

IF (TEMPN.LT.AMAX_TEMP.AND.USRN1(1).EQ.0.AND.

$ TEMPN.GT.AMIN_TEMP) THEN

USRN2(1) = CURTIM

USRN2(2) = 0

ELSE IF (TEMPN.LT.AMIN_TEMP.AND.USRN1(2).EQ.0) THEN

USRN2(1) = CURTIM - USRN2(1)

USRN2(2) = ADIF_TEMP/((CURTIM-USRN1(1))/60)

ELSE

USRN2(1) = USRN1(1)

USRN2(2) = USRN1(2) 

ENDIF

ENDIF

3\. In many situations the flow stress may be a function of a user defined variable. In the example given below the value of strain is stored in the user variable and can then be used in the USRMTR routines to calculate the flow stress of the material.

IF (ISTATUS.EQ.1.AND.KELE.GT.0) THEN

C

C Strain = time increment * strain rate

C

USRE2(1)=USRE1(1) + DTMAXC * EFEPSE

C

C Calculate max principal stress and if greater than current value

C store in the user element value

C

USRE2(2)=USRE1(2)

RETURN

ENDIF

C

IF (ISTATUS.EQ.1.AND.KNODE.GT.0) THEN

USRN2(1)=USRN1(1)

USRN2(2)=USRN1(2)

RETURN

ENDIF

### User defined damage models (USRDMG)

User defined damage models can be implemented for calculating damage or for use with the fracture module of DEFORM where elements can be deleted when their damage values exceeds a certain value. To use the damage model select the fracture mode ([FRCMOD](/docs/sk/keyword_documentation/f/frcmod/)) as User Routines in Materials Properties, Advanced and specify the user routine number to be called in the subroutine USRDMG. (See Fig. 56.3.6.)

![]({{ '/assets/images/user_routines/56_3_3d_user_defined_fem_routines/image0006.jpg' | relative_url }})

Selecting the user defined damage model in Pre processor

The damage routines are functions USRDM1 onwards with the inputs being as follows:

**Input**

C NRT = DAMAGE MODEL NUMBER

C STS = STRESS

C EFSTS = EFFECTIVE STRESS

C EFEPS = EFFECTIVE STRAIN RATE

C DAMAG = PREVIOUS ACCUMULATED DAMAGE

C STRLMT = STRAIN LIMIT

C DTIME = TIME INCREMENT

In addition to the variables passed on as arguments, all the element common block ELMCOM variables (as seen in the USTMTR routines) can be accessed in these routines as well. (user needs to just insert the common block in to his damage routines)

The output is the new value of damage.

**Output**

DAMAG = NEW VALUE OF ACCUMULATED DAMAGE

The routine USRDM1 has an example on how the above routine is to be used. The default damage model in DEFORM is the Freudenthal criterion as follows. Note that after the calculation is made, the computed damage value is returned to the variable DAMAG. The calculation is performed only if two criterion are met:

  1. The effective strain rate is above the limiting strain rate and

  2. The effective stress is greater than zero

Note that if the calculation is skipped, the current step value will be the same as the previous step value.

Here is the sample code included with the DEFORM-3D package:

C This routine calculates the accumulated damage based on

C the Freudenthal criterion for each object.

C

IF (EFEPS.LE.STRLMT) GO TO 10

IF (EFSTS.LT.0.) GO TO 10

C

DAMAG = DAMAG + EFSTS*EFEPS*DTIME

C

10 RETURN

### User defined general routine (USRMSH)

This user routine is recommended when no other routine will accomplish what is desired. The flexibility of this routine makes this a very powerful option but often other routines will accomplish the same task in much less effort. This routine is called once at the beginning and end of each step. Also, it is called once for each object in the simulation. For example, if there are 3 meshed objects in a simulation, this routine will be called three times (once for each object) at the beginning of each step and three times at the end of each step.

A list of the input variables is taken from the code and is listed as follows:

C

C All FIELD VARIABLES CAN BE CHANGED IN THIS ROUTINE!

C

C IMPROPER CHANGE MADE IN THIS ROUTINE WILL CAUSE PROBLEMS

C IN THE ANALYSIS.

C

C PLEASE USE THIS ROUTINE WITH CAUTION!!

C

C This routine will be called at the beginning of the step and

C at the end of the step

C Object with FEM mesh will be passed to this Routine

C REAL*8 array

C RZ(3,NUMNP): Nodal Coordinateis

C DRZ(3,NUMNP): Nodal displacemnts

C URZ(4,NUMNP): Nodal Velocities, and pressures (for tets only)

C TEMP(NUMNP) : Nodal temperatures

C DTMP(NUMNP) : Nodal temperature change in the step

C FRZA(3,NUMNP): Nodal external forces

C FRZB(3,NUMNP): Nodal reaction forces

C PRZB(3,NUMNP): Calculated nodal pressures

C 3rd component is normal pressure

C vector sum of first two components gives traction

C tangential to the surface

C Note: PRZB values for the rigid meshed dies are the

C ---- interpolated values from the contacting workpiece.

C for example traction 'TRACT' at node 'NODE' can be extracted as

C TRACT = DSQRT((PRZB(1,NODE))**2.D0+(PRZB(2,NODE))**2.D0)

C EFSTS(NUMEL): Effective stress

C EFEPS(NUMEL): Effective strain rate

C TEPS(NUMEL) : Total plastic strain

C RDTY(NUMEL) : Relative element Densities

C STS (6,NUMEL): Stress tensor components (Engineering definition)

C EPS (6,NUMEL): Strain rate components (Engineering definition)

C DCRP(6,NUMEL): Creep rate components (Engineering definition)

C TSRS(LSTSR,NUEML): Strain components

C Note) LSTSR is total number of strain components defined by Pre-processor.

C Elastic, Plastic, Creep, Transformation plasticity,total strain- 6 components

C Thermal volumetric, Transformation volumetric - 1 component

C

C Ex1) If elastic and plastic strain components are selected, then LSTSR = 6+6

C Ex1) If elastic,total and thermal volumetric strain components are selected,

C then LSTSR = 6+6+1 = 13

C

C DAMG(NUMEL) : Damages

C USRVE(NUSRVE,NUMEL): User defined Element Variables

C NUSRVE: Number of User defined Element Variables

C (Must be declared in the Pre-Processor)

C USRVN(NUSRND,NUMEL): User defined nodal Variables

C NUSRND: Number of User defined nodal variables

C (must be declared in the Pre-processor)

C

C ATOM(NUMNP): Dominating Atom Contents

C HEATND(NUMNP): Nodal Heat Source

C WEAR(3,NUMNP): nodal wear parameters(for meshed objects)

C WEAR(1,N): Interface temperature (in Deg. Absolute)

C WEAR(2,N): Sliding velocity

C WEAR(3,N): Interface pressure

C Note:

C ---- (WEAR(1:3,N) and PRZB components are computed

C for rigid meshed die nodes when

C tool wear models are turned on in Pre processor

C in the inter object data definition.

C EVOL(NUMEL): Elemental volume

C

C MICRO-STRUCTURE RELATED VARIABLE

C

C Available ONLY for Heat Treat applications

C

C HDNS(2,*): Hardness

C VF(NTMATR,*): Volume Fraction

C VFN(NTMATR,*): Transformation Starting Volume Fraction

C DVF(NTRELN,*): Transformation Volume Fraction Change Ammount

C TICF(NTRELN,*): Incubation Time

C GRAIN(NGRNVAL,*): Grain Size

C

C CURTIM: Current Time

C KSTEP: Current Step Number

C DTMAXC: Time Step

C

C Integer*4 Integer Array

C

C NBCD(3,NUMNP): Nodal Boundary Condition

C 0- Traction specified => FRZA

C 1- Prescribed Velocity => URZ

C 2- Normal pressure Specified => PRZA

C NBCDT(NUMNP): Temperature Boundary Condition

C 0- Prescribed Nodal heat

C 1- Prescribed Nodal Temperature

C

C NONP : Nodes per element (4/8 for each tet/brick)

C NOD(NONP,*): Element Connectivities (global node numbering)

C MATR(NUMEL): Material group number

C NBDRY(4,NUMFAC): Boundary node list (Global node numbering)

C

C Interger*4 Integer Variables

C

C KOBJ : Current Object number

C NUMEL: Total number of elements of KOBJ

C NUMNP: Total number of nodes of KOBJ

C NDSTART: Starting node number of KOBJ

C NDEND : Ending Node Number of KOBJ

C

C NEDGE: Total number of oundary edges of KOBJ

C NTMATR: Total number of Materials

C NTRELN: Total Number of Inter-materail relations

C NGRNVAL: Number of Grain-related Variables

C NROUTINE: User Controlled Routine number (?)

C AVGSRT: Average Strain Rate

C SRTLMT: Limiting Strain Rate

C

C ISTATUS: 0 -> Called at the beginning of each step prior to the analysis

C 1 -> Called at the end of each step prior to writing to database

C

C IUSRFLAG: An integer flag at user's disposal

C NWEAR_CMP : Number of parameters computed for tool wear computations

C

C NODAL DEFINITION FOR DAMAGE FACTPR

C IELMNOD(1) = 0 -- NOT DEFINED

C > 0 -- DEFINED

C DAMG_NP(NUMNP) : Nodal damage factor

C NODAL DEFINITION FOR EFFECTIVE STRAIN

C IELMNOD(2) = 0 -- NOT DEFINED

C > 0 -- DEFINED

C EFEPS_NP(NUMNP) : Nodal eff. strain rate

C TEPS_NP(NUMNP) : Nodal eff. strain

C NODAL DEFINITION FOR STRESSES IN ELASTOPLASTIC OBJECT

C IELMNOD(3) = 0 -- NOT DEFINED

C > 0 -- DEFINED

C DAMG_NP(NUMNP) : Nodal damage factor

C

COMMON /USRFLAG/ IUSRFLAG

C IUSRFLAG: An integer flag at user's disposal

No output is required for this routine.

**Example #1: Applying uniform distributed heating to a meshed object**

In this example, we will apply heat to each element and to make the heating uniform, we will weight the heat to the volume of each element.

Here is an outline of the procedure in which this can be done.

  1. A variable, HHH, is first defined that stores the heat rate per unit volume to be applied. The value in this example is 100. In SI units this is N*mm/mm3. In English units this is klb*in/in3. 

  2. Loop over the elements in the meshed object.

  3. Inside the loop, calculate heat rate per node by multiplying by volume and then dividing by the number of nodes.

  4. Loop over each node for a given element and add the heat rate to each individual node.

Here is the code that performs this:

C

C The following example shows how the NODAL HEAT is added.

C HHH is the heat rate per unit volume provided by the user.

C

HHH = 100.0

DO 500 L = 1, NUMEL

HT = EVOL(L)*HHH/NONP

DO I = 1, NONP

N = NOD(I,L)

HEATND(N) = HEATND(N) + HT

ENDDO

500 CONTINUE

## Compiling user routines on Linux

The user routines are called for each node/element for every step during the simulation and efficient coding practices should be followed to minimize simulation time. Do not open or close data files during each subroutine call as this can degrade performance significantly. The [USRDEF](/docs/sk/keyword_documentation/u/usrdef/) field in the pre-processor can be used to store a limited number of parameters. If you require more space than what is available in [USRDEF](/docs/sk/keyword_documentation/u/usrdef/) then open the data files in the user subroutines and store a static variable in a COMMON block so that the file does not have to read each time the user subroutine is called.

Typically user is expected to make a copy of /USR folder from the installed folder available at $DEFORM_DIR/USR (default location being /usr/local/SFTC/DEFORM/v11.1/3d/USR). After the FORTRAN code has been modified a new local FEM engine can be build using the script build_fem or DEF_INS.COM which are available in /USR folder.

This builds a new copy of the FEM engine DEF_SIM.EXE in the local directory. After this process is completed, simulations using the new user defined routines can be run using the local copy of the FEM engine.

## Compiling user routines on Windows

Like in the Linux environment, make local copy of the folder 3D\UserRoutine\DEF_SIM (from the install structure e.g c:\Program Files\SFTC\DEFORM\v13.1).

  
The “<DEFORM install path>\v13.1\3D\UserRoutine” folder contains subfolders for static and dynamic linking methods.

  1. The first folder is called “**DEF_SIM** ”, which allows for compiling of an FEM executable (.exe) via a static link library. This folder contains static link batch (.bat) files for the Absoft and Intel compilers. Build scripts provided along with release pack, 

  * For Absoft - DEF_SIM_USR_Absoftv110.amake or DEF_SIM_USR_Absoftv110.atools in the Absoft compiler or using the batch file build_def_sim_usr_Absoftv110.bat

  * For Intel FORTRAN Compiler – using the batch file build-FEM-USR-PC-64bit-intel-compiler-2022.bat

Using the build scripts provided, users locally modified FORTRAN subroutines will be compiled and linked to the object code named DEF_SIM_USR64_LIB.lib (Absoft) or DEF_SIM_USR64_INTEL_LIB.lib (Intel) found in this directory. This will then generate a new FEM engine, named DEF_SIM_64.EXE. The released DEF_SIM_64.EXE should be replaced with the customized DEF_SIM_64.EXE, after first making a copy of the released executable.

![]({{ '/assets/images/user_routines/56_3_3d_user_defined_fem_routines/image0007.jpg' | relative_url }})

UserRoutine DEF_SIM folder

  1. The second folder is called “**DEF_SIM_DLL** ”, which allows for compiling of user routines as dynamic link library (.dll) files. This folder contains dynamic link batch files, Absoft_build_all_dll_command.bat for the Absoft and Intel_build_all_dll_command.bat for the Intel FORTRAN compilers.

When the preferred batch file is executed, .dll files will be compiled with the Fortran (.f) user routine files found within this directory. The resulting .dll files and the Intel DEF_SIM_64.EXE (located in <3D>\DEF_SIM_64\Intel_modern”) should be copied to a new folder. DEF_SIM_DIR.DAT should then be edited to specify the new folder as the location for the customized DEFORM implementation. Please note that either Absoft or Intel compiled .dll files may be linked with the Intel DEF_SIM_64.EXE.

![]({{ '/assets/images/user_routines/56_3_3d_user_defined_fem_routines/image0008.jpg' | relative_url }})

UserRoutine DEF_SIM_DLL folder

**Note** :

User needs to specify the version number of Microsoft Visual Studio installed on their computer before compiling the program using the **build-FEM-USR-PC-64bit-intel-compiler-2022.bat** or **Intel_build_all_dll_command.bat** file. The Visual Studio version is set to 2019 in the example .bat file provided using the following command:

  
call "C:\Program Files (x86)\Intel\oneAPI\setvars.bat" intel64 vs2019

  
User should update this command to match the version of Visual Studio that has been installed on the computer. For example, if Visual Studio 2022 is installed, user would update the command as follows:

  
call "C:\Program Files (x86)\Intel\oneAPI\setvars.bat" intel64 vs2022

## Running the modified FEM engine for Linux platforms

**Option 1.**   
If the local FEM engine is built and copied to the DEFORM install /EXE directory, all users have access to the same user routines. If a local copy of the FEM engine is to be built and run then the DEF_ARM.COM script has to be copied to the local directory and the calls to DEF_SIM.EXE have to be modified to call the local copy of the program. In place of the calls

$DEFORM3_DIR/EXE/DEF_SIM.EXE

replace it with

./DEF_SIM.EXE

If the FEM engine is built in the DEFORM directory with user routines, all users have access to the same user routines. If a local copy of the FEM engine is to be built and run then the DEF_ARM.COM script has to be copied to the local directory and the calls to DEF_SIM.EXE have to be modified to call the local copy of the program. In place of the calls

$DEFORM3_DIR/EXE/DEF_SIM.EXE

replace it with

./DEF_SIM.EXE

where ./DEF_SIM.EXE is the local copy of the FEM engine. When simulation jobs are submitted using the GUI or text based main program, the alias DEF_ARM is used to start the script DEF_ARM_CTL.COM which in turn runs DEF_ARM.COM.

When using a local copy of the FEM engine, copy DEF_ARM_CTL.COM to a local directory and change the alias for DEF_ARM to point to the local copy of DEF_ARM_CTL.COM. This alias is defined in the $DEFORM3_DIR/CONFIG.COM and a line in the .cshrc after the source $DEFORM3_DIR/CONFIG.COM redefining the alias should work. In the .cshrc file the following modifications can be made. (based on the installation location)

setenv DEFORM3_DIR '/usr/local/SFTC/DEFORM/v11.0/3d'

source $DEFORM3_DIR/CONFIG.COM

#

# Old alias

#

alias DEF_ARM $DEFORM3_DIR/COM/DEF_ARM_CTL.COM

#

# New alias which is a local copy of DEF_ARM_CTL.COM

#

alias DEF_ARM $HOME/DEF_ARM_CTL.COM

Also in the local copy of DEF_ARM_CTL.COM the following calls should be replaced.

$DEFORM3_DIR/COM/DEF_ARM.COM

with the local version of

$HOME/DEF_ARM.COM

After this has been done simulations can be run using the local copy of the FEM engine and jobs can be started using the user-interface.

One problem that can occur is that if the .cshrc has an exit for non-interactive shells and the new definitions are after this, then they will never be defined when running a simulation. Place the new command to run the local copy of DEF_ARM just after the definitions for the regular version of DEFORM.

**Option 2.**  
Second option which is available from DEFORM v11.1 on Linux is to keep a DAT file DEF_SIM_DIR.DAT in the problem folder (that has the model DB file that needs to run using this local FEM engine) indicating directory path to this local FEM engine. (this local FEM engine folder, which typically is a copy of the released 3d/USR folder with modified FEM engine built in this locally modified user routines). with this option the DAT file (DEF_SIM_DIR.DAT in the problem folder) alone dictates which FEM engine is used for the current model run.

## Running the modified FEM engine for Windows platforms

**For Static Link built DEF_SIM_64.EXE**

  
**Option.1**

If the FEM engine has been built for Windows, one way in which to run it is to swap (first backup original file) it with the current FEM engine. The current FEM engine which can be located with the current installation of DEFORM-3D usually in a directory such as C:\Program Files\SFTC\DEFORM\v13.1\3d. If it is not there, look for a file named DEF_SIM_64.EXE if installation is done in a different folder.

  
**Option.2**

From DEFORM v11.0 in Windows environment a new facility is available to run the user routines without disturbing the installed copy of FEM engine. In the problem folder (having DB), user can simply place a text file called DEF_SIM_DIR.DAT containing the full path to this local FEM engine compiled for user routines. Execution of the model itself can be done from the GUI. Once the model running scripts see the local FEM path defined in the txt file as indicated, model picks up local FEM engine at the run time.

  
**For Dynamic link DLL files**

In the problem folder (having DB), user can simply place a text file called DEF_SIM_DIR.DAT containing the full path to the folder having the compiled dll files along with Intel FORTRAN compiled DEF_SIM_64.EXE original file from “<3D>\DEF_SIM_64\Intel_modern” folder.

**Related Topics:**

[56.1. Introduction to User Routines](/docs/sk/user_routines/56_user_routines_in_deform/56_1_introduction_to_user_routines/)

[56.2. 2D User Defined FEM Routines](/docs/sk/user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines/)

[56 4 User-Defined Post-Processing Routines](/docs/sk/user_routines/56_user_routines_in_deform/56_4_user-defined_post-processing_routines/)
