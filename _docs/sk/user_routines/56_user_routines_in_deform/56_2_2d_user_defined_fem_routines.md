---
lang: sk
title: "56.2. 2D User Defined FEM Routines"
---

# 56.2. 2D User Defined FEM Routines

56.2.1. Summary of subroutines and calling structure of user-defined FEM routines

56.2.2. Passing data to user routines from the Preprocessor

56.2.3. 2D User Defined FEM routines

56.2.3.1. User defined flow stress routines (USRMTR)

56.2.3.2. User defined movement control (USRDSP)

56.2.3.3. User defined node and element value (USRUPD)

56.2.3.4. User defined damage models (USRDMG)

56.2.3.5. User defined material models (USRMAT)

56.2.3.6. User defined nodal boundary conditions (USRBCC)

56.2.3.7. User defined lubricant heat transfer (USRBCC2)

56.2.3.8. User defined general routine (USRMSH)

56.2.4. Compiling user routines for Linux platforms

56.2.5. Compiling user routines on Windows

56.2.6. Running the modified FEM engine for Linux platforms

56.2.7. Running the modified FEM engine for Windows platforms

This section contains a description of the different FEM user routines available in the current release of DEFORM-2D. The skeletal code for user routines is stored in a set of FORTRAN files included with the system pack that have the FORTRAN functions that the FEM engine calls if a user routine is to be used. The user routines calculate the specified values and returns output values back to the FEM engine. User should avoid external file read/write from these routines, which could potentially slowdown the run time performance of FEM engine.

#### **User defined FEM routines**

User-Defined FEM Routines are FORTRAN subroutines in which the user can change internal routines within the DEFORM FEM engine to perform very specialized functions during a simulation. These subroutines can then be compiled and linked to provided object code to generate a custom built FEM engine.

Based on the functionality, available user routines are grouped in to these set of source files. These are 14 files as listed here,

def_usr.f, usr_bcc.f, usr_crp.f, usr_dmg.f, usr_dsp.f, usr_mat.f, usr_msh.f, usr_mtr.f, usr_pm.f, usr_tranfkine.f, usr_upd.f, usr_wear.f, usr_zrt.f, usr_upd_s.f, (in case of Linux def_usr.f is named differently as DEF_USR.FOR)

These are text format files containing all the available FORTRAN subroutines. To compile this file, run the script file DEF_INS.COM on Linux or build_def_sim_usr_Absoft110.bat for PC (using Absoft compiler) or build-FEM-USR-PC-64bit-intel-compiler-2022.bat for PC (using Intel Fortran compiler). At this point, the user supplied FORTRAN file/s will be compiled and linked to the object code named DEF_SIM.OBJ in Linux while in Windows, the user supplied FORTRAN file/s will be compiled and linked to the object code named DEF_SIM_USR64_LIB.lib in case of Absoft FORTRAN compiler or DEF_SIM_USR64_INTEL_LIB.lib in case of Intel FORTRAN based compiler. This will then generate a new FEM engine, named DEF_SIM_64.EXE. For PC environment, the build structure is shown in [Fig. 56.2.1.](56_2_2d_user_defined_fem_routines.htm#Fig_56_2_1_Description_on_how_to_compile/link_a_new_32_bit_FEM_engine_in_PC_Environment) In the case of Linux platforms, this building process is shown in [Fig. 56.2.2.](56_2_2d_user_defined_fem_routines.htm#Fig_56_2_2_Description_on_how_to_compile/link_a_new_FEM_engine_in_Linux_environment)

![]({{ '/assets/images/user_routines/56_2_2d_user_defined_fem_routines/image0001.jpg' | relative_url }})

Description on how to compile/link a new 64 bit FEM engine in PC Environment

![]({{ '/assets/images/user_routines/56_2_2d_user_defined_fem_routines/image0002.jpg' | relative_url }})

Description on how to compile/link a new FEM engine in Linux environment

In the Linux environment, build_fem script may or may not automatically catch all the necessary details specific variant of a given operating system. User can also directly use the script DEF_INS.COM with the following guidelines. 

For the initial prompts on machine selection available options are

centos5_32bit_linux, centos6_32bit_linux, suse11_32bit_linux 

specific details of these machine options being

  1. centos5_32bit_linux for Centos 5.10 (2.6.18-371Equivalent to REL 5) using Absoft Fortran90 v11.0 (64 bit version).

  2. centos6_32bit_linux for Centos 6.5 (2.6.32-431 x86-64 Equivalent to REL 6) using Absoft Fortran90 v11.0 (64 bit version of the compiler).

  3. suse11_32bit_linux for Suse Enterprise Linux Desktop (3.0.101-0.18-36 Equivalent to Suse11 sp3) using Absoft Fortran90 v11.0 (64 bit version).

DEF_INS.COM requires two arguments, first one for machine operating system and the second flag indicates output. (1 for user defined FEM engine, 2 for user defined post processor SL file or 3 for user defined microstructure library)

After the machine selection is made, select the appropriate prompt to build DEF_SIM.

In PC Win7 environment the DEF_SIM system is built using Absoft Fortran90 v11.0. However the DEF_SIM object files for the earlier version of Absoft Fortran90 v9.0 are also built and released as a part of release pack. It was noted that the code generated using Absoft Fortran90 v11.0 is faster compared to the earlier versions of the same compiler.

Currently user routines exist for flow stress definition, movement control, calculation of specialized nodal values ([USRNOD](/docs/sk/keyword_documentation/u/usrnod/)), calculation of element values ([USRELM](/docs/sk/keyword_documentation/u/usrelm/)), and many other capabilities. For example, there are many different methods for a user to control the movement of a rigid body within DEFORM, e.g. constant velocity, mechanical press, hammer press movement, speed as a function of time. However, there are some cases where a slightly more specialized movement control is required, such as movement based on variation of state variables of the workpiece. This can be performed using user-routines since these variables are available when the movement of the rigid die is calculated.

## Summary of subroutines and calling structure of user-defined FEM routines

Here is a list of the different subroutines available to the user. With each, routine is a brief description of its purpose and the frequency of it being used by DEFORM.

  1. **USRMAT**(available in **_usr_mat.f_**)

**Description** : This routine allows the user to calculate stress, plastic strain and tangent modulus at the end of the step increment for linear elastic materials.

  1. **USRDSP**(available in **_usr_dsp.f_**)

**Description** : This routine allows the user to calculate the die speed of a rigid object that has movement defined as a user model. This routine is called at the beginning of each step.

  1. **USRUPD**(available in **_usr_upd.f_**)

**Description** : This is the user defined nodal and element variable subroutine. This routine allows the user to calculate special state variables and store them for each node and element. These variables can be viewed in the Post-Processor or be used during the simulation in flow stress calculation. User Nodal variables are updated only at the end of a converged step. User Element variables are updated at the beginning of each iteration and at the end of a converged step. The purpose for this is that the most current user element variable can be fed into the user-defined flow stress routine.

  1. **USRDMG** (available in**_usr_dmg.f_**)

**Description** : This routine allows the user to calculate damage of a material. This routine is called at once every step.

  1. **USRZRT**(available in **_usr_zrt.f_**)

**Description** : This routine is implemented to allow the user to define a Z-strain rate in a different manner than currently available within the standard program. See the section above on generalized plane strain for a description of Z-strain rate.

  1. **USPM**(available in **_usr_pm.f_**)

This subroutine allows the user to specify parameters for densification of a porous material model. This routine is called before stiffness matrix generation at the beginning of each iteration.

  1. **USRCRP**(available in **_usr_crp.f_**)

**Description** : This routine is used to define creep rate and its derivative as a routine. This routine is available for only elasto-plastic materials. This is called at the beginning of each iteration.

  1. **USRBCC**(available in **_usr_bcc.f_**)

**Description** : This routine is used to allow the user to specify special boundary condition settings to a given object such as defining a different friction routine. This is called upon the beginning of each iteration.

  1. **USRMTR**(available in **_usr_mtr.f_**)

**Description** : This routine is used to allow the user to compute user defined flow stress, and it’s derivatives with respect to strain and strain rates. This routine gets called for each integration point of every element and for every iteration.

  1. **USRMSH**(available in **_usr_msh.f_**)

**Description** : This routine is used as a general purpose routine that has access to many internal variables within DEFORM. This routine is advocated when other routines cannot satisfy the needs of the user. This routine is called at the beginning and end of each step.

  1. **USRBCC2**(available in **_usr_bcc.f_**)

**Description** : This routine is used to allow the user to specify special boundary condition settings to a given object. This is called upon the beginning of each iteration.

  1. **USRWEAR**(available in **_usr_wear.f_**)

**Description** : This routine allows the user to compute custom defined wear rate and wear variables at the die nodes in contact with the deforming work piece. Interface temperature, sliding velocity, contact pressure, shear stress, nodal area and time step are available for this purpose. This routine is called upon the end of each step.

  1. **USR_TRNF_KINE**(available in **_usr_tranfkine.f_**)

**Description** : This routine allows the user to compute custom defined transformation kinetics such as change in volume fraction and updated incubation time. Available variables include temperature, stress, strain, current volume fractions of child and parent phases, incubation time and time increment. This routine is called upon the end of each step.

  1. **USRUPD_S**(available in _**usr_upd_s.f**)_

**Description** : This is rotuine works same as USRUPD(usr_upd.f) except that it has additional information about remeshing step and restarting step in the FEM run.

**Recent changes in DEFORM v11.1 to the user routine related functionality in 2D:**

******usr_bcc.f** (from v11.0 to v11.0.1)

COMMON/MSNODE/MSNODE1,MSNODE2 is added, carries master side element edge node numbers, and no further change in v11.1)

**usr_msh.f** (changes from v11.0 to v11.1)

Arrays for tensors Stress (STS), Strain rate (EPS), Creep rate (DCRP) and Strian components (TSRS), all are now indexed as (NUMSTS, NUMEL) with integer NUMSTS indicating total number of components made available in a new common block IDIMEN.

NUMSTN : TOTAL NUMBER OF STRAIN COMPONENTS PER ELEMENT 

Ex) "Elastic","Plastic", and "Thermal" strains are selected for strain output 

NUMSTN = NUMSTS + NUMSTS + 1 = 9 => TSRS(9,*)

Please note that handling integration point definitions combined with different strain components has not been implemented yet in v11.1 to support corresponding parts of user routines.

**Recent changes in DEFORM v11.1.1 to the user routine related functionality in 2D:**

Object level data for Induction heating models is now available in the common block COMMON/INDCTUSR/RINHUSR(200), INHUSRFLAG, which is available in the user subroutine USRMSH.

The available variables being

C INHUSRFLAG :0=coil input defined in DB, (default), 1=current density, 2=power, 3=voltage drop

C RINHUSR(KOBJ) : Input value for induction heating.

**usr_tranfkine.f**(changes from v11.0 to v11.1)

Subroutine USR_TRNF_KINE now carries additional argument IELE, i.e the current element number (global)

**Recent changes in DEFORM v11.2 to the user routine related functionality in 2D:**

**usr_msh.f** (changes from v11.1.1 to v11.2)

Fixed a bug in USRMSH. Now, the tool wear data in 2D usrmsh consistent with 3D)

**Recent changes in DEFORM v11.3 to the user routine related functionality in 2D:**

**usr_upd_s.f** (changes from v11.2 to v11.3)

Add new 2d usr subroutine which has additional remeshing and restarting step information compared to original USRUPD subroutine.

Please note that .atools files and .amake files need to be updated to compile DEF_SIM correctly since v11.3 release.

## Passing data to user routines from the Preprocessor

The user defined data ([USRDEF](/docs/sk/keyword_documentation/u/usrdef/)) field in the pre-processor can be used to store data that can be used to specify parameters for the user-routines. The purpose for importing data for user routines through this method is that this data can be stored within a keyword file or a database and can be made unique to an individual simulation. This data can be defined and accessed in the Simulation Controls, Advanced Controls menu as shown in Fig. 56.2.3. Ten data lines are assigned for user defined data. Each data should be separated by space and user can input as many of data in each lines with in 80 columns. In the user-routines inserting the following code lets the user access the [USRDEF](/docs/sk/keyword_documentation/u/usrdef/) values common block through the variable IUSRVL.

CHARACTER*80 IUSRVL

COMMON /IUSR/ IUSRVL(10)

To read and write data to the USRDEF variable the following sections of code can be used.

C TO READ DATA (10 RESERVED LINES)

READ(IUSRVL(LINE NUMBER),*) DATA1,DATA2,.....

C TO WRITE DATA (10 RESERVED LINES)

WRITE(IUSRVL(LINE NUMBER),*) NEWDATA1, NEWDATA2, .....

The screen where this information can be set is seen in the Fig. 56.2.3.

![]({{ '/assets/images/user_routines/56_2_2d_user_defined_fem_routines/image0003.jpg' | relative_url }})

User Defined Variables dialog in simulation Controls

## 2D User Defined FEM routines

This chapter explains the various user routines available in the DEFORM system in the FEM (Finite Element Method) engine and the post-processor. Examples on how to use each type of routine, how to compile the code, and how to run the modified FEM engine and post-processor are also covered.

### User defined flow stress routines (USRMTR)

If the flow stress models supported in DEFORM system are not applicable for a process, a user can define his own flow stress model to compute the flow stress and it’s derivatives to be used during the simulation. The flow stress can be a function of strain, strain rate, temperature, and user node and user element variables. The flow stress subroutine should return the following information:

1\. The flow stress of the element at the current state condition.

2\. The derivative of the flow stress with respect to total effective plastic strain.

3\. The derivative of the flow stress with respect to total effective plastic strain rate.

A maximum of 100 flow stress routines can be defined in this program. In the pre-processor Material Properties the flow stress ([FSTRES](/docs/sk/keyword_documentation/f/fstres/)) type selected should as User routine (as shown in Fig. 56.2.4.) and a routine number can be specified by selecting the icon to the right of the User routine line. This routine number (NPTRTN) is passed to the user defined flow stress subroutine to control branching to the specified UFLOW routine. (as listed in the file usr_mat.f).

![]({{ '/assets/images/user_routines/56_2_2d_user_defined_fem_routines/image0004.jpg' | relative_url }})

Specifying flow stress as a user-defined model from material dialogs in MO

An example of using the user defined flow stress subroutine is given below. Note that only the additional code to the skeleton of the routines is shown in order to save space in the text (except for example1). Recall that only three values need to be returned as mentioned above, YS (yield stress), FIP (derivative of flow stress as a function of strain rate) and YPS (derivative of flow stress as a function of strain):

The following flow stress example routine depends on the strain rate sensitivity index (PEM) and on the effective strain rate (EFEPS).

C********************************************************************

SUBROUTINE UFLOW1(YS,YPS,FIP,TEPS,EFEPS,TEMP)

C********************************************************************

IMPLICIT REAL*8 (A-H,O-Z), INTEGER*4 (I-N)

C **** USER DEFINED VARIABLES ****

CHARACTER*80 IUSRVL

COMMON /IUSR/ IUSRVL(10)

C TO READ DATA (10 RESERVED LINES)

C READ(IUSRVL(LINE NUMBER),*) DATA1,DATA2,DATA3...

C TO WRITE DATA (10 RESERVED LINES)

C WRITE(IUSRVL(LINE NUMBER),*) NEWDATA1, NEWDATA2, NEWDATA3 ...

C THIS ROUTINE IS USED TO DEMONSTRATE THE IMPLEMENTATION OF

C MATERIAL ROUTINE. ALL THE REAL VARIABLES SHOULD BE DOUBLE

C PRECISION. THE DEFINITION OF ARGUMENTS ARE DESCRIBED AS FOLLOWS:

C INPUT :

C TEPS = EFFECTIVE STRAIN

C EFEPS = EFFECTIVE STRAIN RATE

C TEMP = TEMPERATURE

C OUTPUT :

C YS = FLOW STRESS

C YPS = DERIVATIVE OF FLOW STRESS W.R.T. TEPS

C FIP = DERIVATIVE OF FLOW STRESS W.R.T. EFEPS

C

COMMON /ELMCOM/ RZE(2,4),URZE(2,4),STSE(6),EPSE(6),EFEPSE,EFSTSE,

\+ TEPSE,RDTYE,TEMPE(4),DTMPE(4),DAMAGE,

\+ USRE1(1500),USRE2(1500),

\+ USRNE(1500,4),NODEE(4),KELE,KELEL,KGROUP

C EXAMPLE :

C PEM = STRAIN_RATE SENSITIVITY INDEX

C YS = MATERIAL_CONSTANT * (STRAIN)**PEN* (STRAIN_RATE)**PEM

C PEN = STRAIN SENSITIVITY INDEX

C FIP = MATERIAL_CONSTANT * PEM * (STRAIN_RATE)**(PEM-1.)

C YPS = 0.

C STRAIN CAN COME FROM ONE OF THE THREE SOURCES

C (1) FROM THE INPUT ARGUMENT "TEPS"

C (2) FROM THE ELEMENT COMMON BLOCK "TEPSE"

C (3) FROM THE USER DEFINED STATE VARIABLES (SEE THE ROUTINE "USRST1")

C THE FOLLOWING EXAMPLE IS WRITTEN BASED ON THE USED DEFINED STATE

C VARIABLE

IF (STRAIN.LE.0.) STRAIN = 1.E-5

EFEPS=EFEPSE

PEN = 0.15

PEM = 0.1

YS0= 1.0

YS = 10. * STRAIN**PEN* (EFEPS)**PEM+YS0

FIP = 10. * STRAIN**PEN* PEM * (EFEPS)**(PEM-1.)

YPS = 10. * PEN * STRAIN**(PEN-1.) * (EFEPS)**PEM

IF(STRAIN.EQ.1.E-5) YPS=0.0

RETURN

END

C********************************************************************

**Discussion:**

In this very simple model illustrated, the flow stress is merely a function of strain rate. The three lines of added code can be seen using the comments in the code. This creates a very simple equation for the derivative with respect to strain rate and the derivative with respect to strain is zero. Every time a flow stress value for an element is required, this routine is called. It then computes the flow stress for the element and the derivatives and returns the values as PEM, YS and FIP.

The flow stress depends on the strain index (PEN), strain rate sensitivity index (PEM), the effective strain (STRAIN) and the effective strain rate (EFEPS). The value of effective strain can be the element strain or from a user defined state variable. In the example given below the effective strain comes from a user defined state variable that stores the current strain. This routine also has access to all the element level variables as stored in the common block ELMCOM including user defined state variables such as USRE1 and USRE2.

### **User defined movement control (USRDSP)**

DEFORM supports control of the die movement control (routine samples available for user implementation are in the file usr_dsp.f) for machines which cannot be controlled using the movement mechanisms or press controls given in the DEFORM system. The die movement can be a function of the following variables:

C INPUT :

C NSPD = USER SUPPLIED ROUTINE NUMBER 

C TIME = THE SIMULATED PROCESS TIME 

C PDIS = PRIMARY DIE DISPLACEMENT 

C VX = DIE SPEED IN X DIRECTION 

C VY = DIE SPEED IN Y DIRECTION 

C STRKX = THE CURRENT DIE STROKE IN X DIRECTION

C STRKY = THE CURRENT DIE STROKE IN Y DIRECTION

C FRZX = DIE FORCE IN X DIRECTION 

C FRZY = DIE FORCE IN Y DIRECTION 

C AVGSRT = AVERAGE STRAIN RATE 

C SRTMX = MAXIMUM STRAIN RATE 

C TMPMX = MAXIMUM TEMPERATURE 

C DTIME = CURRENT TIME STEP (I/O)

C OUTPUT :

C UPDV = THE UPDATED DIE SPEED IN THE SPECIFIED DIRECTION

C UPDF = THE UPDATED DIE FORCE IN THE SPECIFIED DIRECTION

C DTIME = DESIRED TIME STEP (I/O ) 

C

It is important to note that either UPDV or UPDF need to be defined but both cannot be defined at the same instance. The reason for this is that defining the force determines the die speed through how fast the moving die can press the work piece. Conversely, defining the die speed determines the amount of force required to push the work piece a given distance at a given speed.

The die speed routines are functions which are called from the USRDSP subroutine based on the function number specified in the Object, Movement controls window as indicated in Fig. 56.2.5.

![]({{ '/assets/images/user_routines/56_2_2d_user_defined_fem_routines/image0005.jpg' | relative_url }})

Specifying speed using a user routine in MO

To use the values for AVGSRT, STRMX the primary work piece has to be specified as the object whose average and max strain rate are required. The reason for this is that many different objects can be deforming at different rates at a given step. This is the keyword PDIE(2) in Simulation Controls, Advanced Controls in the pre-processor.

**Example Case #1**

The die speed routine in DIESP1 controls the speed based on a user specified value for the average strain rate. The value of the average strain rate is specified using the USRDEF fields.

C

C THE DIE SPEED OF THIS ROUTINE IS DETERMINED BY:

C

C WHERE SR IS THE APPROXIMATED STRAIN RATE DURING

C AN UPSETTING PROCESS

C HI IS THE INITIAL BILLET HEIGHT STORED IN USER DEFINED DATA IN

C SIMULATION CONTROLS IN PRE PROCESSOR (Figure Fig. 56.2.3.)

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

In the case of a screw press, the rotational energy is converted to translational motion to form a part. The process ends when the energy stored in the flywheel runs out or when the clutch on the drive mechanism is disengaged. Each step, the amount of energy may change due to energy being consumed by deforming the work piece. The total energy is an initial condition and the change in the current energy needs to be computed each step by,

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

### **User defined node and element value (USRUPD)**

The user can implement subroutines that can calculate nodal and elemental values (up to 1500) during the simulation for each node/element of the objects in the simulation. The inputs are all state variables and the outputs are the values for [USRNOD](/docs/sk/keyword_documentation/u/usrnod/) and [USRELM](/docs/sk/keyword_documentation/u/usrelm/).The variables can also be used in the flow stress routines to model flow stress as a function of new state variables.

The subroutine USRUPD is called to calculate the nodal and element values. This in turn calls USRSV1, USRSV2, etc based on the value of NPRTRN the material group number of the current element. If nodal values are being calculated the branching based on the material group number will not work if an object is composed of more than one material group.

The advantage of using these variables instead of doing the same procedure using user defined post-processing is that these values are calculated for each step in the database whereas user defined post-processing is only for the steps that are stored in the database.

Data that is passed to the user variable subroutine are stored in COMMON blocks as detailed below: (the available routines can be seen in the file usr_upd.f)

COMMON /USRCTL/ KOBJ,ISTATUS,KSTEP,KSSTEP

C COMMON /USRCTL/

C KOBJ : Object number

C KSTEP : Step number (N)

C ISTATUS : 0 - the beginning of the step

C 1 - the end of the step

C WHEN (ISTATUS.EQ. 1) --> USRE2/USRN2 should be updated here

C KELE > 0 --> Element data is active

C INODE > 0 --> Node Data is active

C

COMMON /CLOK/ CURTIM

C CURTIM: CURRENT TIME

C 

COMMON /SSTU/ DTMAXC

C DTMAXC: CURRENT TIME STEP SIZE

C 

COMMON /ELMCOM/ RZE(2,4),URZE(2,4),STSE(6),EPSE(6),EFEPSE,EFSTSE,

\+ TEPSE,RDTYE,TEMPE(4),DTMPE(4),DAMAGE,

\+ USRE1(1500),USRE2(1500),

\+ USRNE(1500,4),NODEE(4),KELE,KELEL,KGROUP

C RZE : Four corner coordinates

C URZE : Velocity

C STSE : Stress

C EPSE : Strain rate

C EFEPSE : effective strain rate

C EFSTSE : Effective stress

C TEPSE : Total effective strain

C RDTYE : Density

C TEMPE : Temperature

C DAMAGE : Damage value

C DTMPE : Temperature rate

C USRE1 : Element user state variable 1

C USRE2 : Element user state variable 2

C USRNE : Nodal user state variables 1,2 at 4 nodes

C NODEE : Connectivity

C KELE : Global element number

C KELEL : Local element number

C KGROUP : Material group number

C

COMMON /ELMCOM2/ STRNE(4),NBCDE(2,4),INTNALE(4)

C STRNE : Strain Components

C INTNALE = 0 : Edge exposed to outside world

C 1 : Internal

C NBCDE : Boundary Condition of four corners

C

COMMON /ELMCOM3/ TEPS_NE(4),EFEPS_NE(4),DAMG_NE(4),STS_NE(4,4)

C TEPS_NE : Nodal eff. strain

C EFEPS_NE : Nodal eff. strain rate

C DAMG_NE : Nodal damage factor

C STS_NE : Nodal stress components (elastoplastic object)

COMMON /ELMCOM4/ YLDTRNE (6)

C YLDTRNE : Element backstress

C

C Please note that the common blocks ELMCOM, ELMCOM2, ELMCOM3

C are one set of element data for the element KELE of the object

C KOBJ. For this element KELE, having the nodal connectivity

C indicated in the array NODEE, nodal strain and strain rate

C values of each node (for the element KELE) are available

C in the array TEPS_NE and EFEPS_NE provided nodal option

C of these variables is turned on in the Pre Processor >

C Simulation Controls > Advanced > Output control.

C

COMMON /NODCOM/ RZN(2),URZN(2),DRZN(2),TEMPN,DTMPN,USRN1(1500),

\+ USRN2(1500),KNODE

C 

C RZN : Nodal point coordinates

C URZN : Nodal point velocities

C DRZN : Nodal point displacement

C TEMPN : Nodal point temperature

C USRN1 : User defined state variables (Input : At the beginning of Step N)

C USRN2 : User defined state variables (Output: At the end of Step N)

C KNODE : Node number

C

COMMON /NODCOM2/ AREAN, TMPNEB, SLDVEL, PRESR(2), INTNAL

C

C AREAN : Nodal area

C TMPNEB : The corresponding temperature at contacting surface

C SLDVEL : Sliding velocity

C PRESR(2) : Traction in tangential (friction) and normal (pressure)

C INTNAL : 0 - External surface node, 1 - Internal node

C

COMMON /NODCOM3/ EFEPS_NN,TEPS_NN,DAMG_NN,STS_NN(4),IELMNOD(3)

C

C EFEPS_NN : Nodal effective strain rate

C TEPS_NN : Nodal effective strain

C DAMG_NN : Nodal damage factor

C STS_NN : Nodal stress components (elastoplastic object)

C ELMNOD(K) = 0: Element definition

C > 0: Node+element definition

C

C K = 1,2,3 -- REFERRING TO DAMAGE, EFF. STRAIN AND STRESS

C COMPONENTS, RESPECTIVELY

C Please note that the common blocks NODCOM, NODCOM2, NODCOM3

C are one set of nodal data for the node KNODE of the object

C KOBJ. For this node KNODE, nodal strain and strain rate

C values of (for the node KNODE) are available

C in the variable TEPS_NN and EFEPS_NN provided nodal option

C of these variables is turned on in the Pre Processor >

C Simulation Controls > Advanced > Output control.

C 

COMMON /DEFGRA/ DFDX(3,3,2)

C This common block stores deformation gradient information

C Last digit if 1 is for dx/dX at x=n, and X=0

C Last digit if 2 is for dx/dX at x=n+1, and X=0

C Gradient computed is with respect to the original

C configuration (X=0)

C This True for every meshed 2D object and computed at the end of the step.

COMMON /VELGRDIPC/ DVDXIPC(2,2,5)

C DVDXIPT: Velocity gradients dv/dx at integration points and element center

C dv/dx(I,J,IPC)=dv(J)/dx(I) at point IPC

The variable USRN1 stores the nodal variables at the beginning of the step (the current value). After computing a new value for the user defined variables the results should be stored in USRN2 at the end of each step. For the element variables, USRE1 stores the values at the beginning of the step and the updated value must be stored in USRE2. If the variables are not being calculated, then the value stored in USRN1 and USRE1 must be copied to USRN2 and USRE2 respectively.

Examples of using the user defined nodal and element variables:

**Example 1:**

The maximum principal stress is stored in the first user element value(USRE2(1)) and the second element variable is not used in this example.

IF (ISTATUS.EQ.1.AND.KELE.GT.0) THEN

USRE2(1)=USRE1(1)

CALL USR_MAXPRN(STSE,PRNSTS)

IF (USRE2(1).LT.PRNSTS) USRE2(1) = PRNSTS

ENDIF

In this example the average cooling rate (F/min) from 1300 F to 600 F is approximately calculated and the result stored in the second user nodal variable (USRN2(2)). At first starting time is marked when TEMPN is between AMAXTEMP and AMINTEMP. When TEMPN is less than AMINTEMP ending time is marked and elapsed time is calculated by difference of them. The cooling rate is calculated as the temperature difference divided by the elapsed time. Here CURTIM is the current time in the simulation which can be accessed from the COMMON block CLOK.

COMMON /USER_DATA/ AMAX_TEMP, AMIN_TEMP, ADIF_TEMP

DATA AMAX_TEMP, AMIN_TEMP, ADIF_TEMP /1300,600, 700/

IF (ISTATUS.EQ.1.AND.KNODE.GT.0) THEN

IF (TEMPN.LT.AMAX_TEMP.AND.USRN1(1).EQ.0.AND.TEMPN.GT.AMIN_TEMP) THEN

USRN2(1) = CURTIM

USRN2(2) = 0

ELSE IF (TEMPN.LT.AMIN_TEMP.AND.USRN1(2).EQ.0) THEN

USRN2(1) = CURTIM - USRN2(1)

USRN2(2) = ADIF_TEMP/((CURTIM-USRN1(1))/60)

ELSE

USRN2(1) = USRN1(1)

USRN2(2) = USRN1(2)ENDIF

ENDIF

ENDIF

**Example 2:**

In many situations the flow stress may be a function of a user defined variable. In the example given below the value of strain is stored in the user variable and can then be used in the USRMTR routines to calculate the flow stress of the material.

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

IF (ISTATUS.EQ.1.AND.KNODE.GT.0) THEN

USRN2(1)=USRN1(1)

USRN2(2)=USRN1(2)

RETURN

ENDIF

### **User defined damage models (USRDMG)**

User defined damage models can be implemented for calculating damage or for use with the fracture module of DEFORM where elements can be deleted when their damage values exceeds a certain value. To use the damage model select the fracture mode ([FRCMOD](/docs/sk/keyword_documentation/f/frcmod/)) as User Routines in Materials Properties, Advanced and specify the user routine number to be called in the subroutine (See Fig. 56.2.6.) USRDMG. (the available routines can be seen in the file usr_dmg.f) The damage routines are functions USRDM1 onwards with the inputs being as follows: Element variables from ELMCOM block are also available here.

C INPUT :

C NRT = DAMAGE MODEL NUMBER

C STS = STRESS

C EFSTS = EFFECTIVE STRESS

C EFEPS = EFFECTIVE STRAIN RATE

C DAMAG = PREVIOUS ACCUMULATED DAMAGE

C STRLMT = STRAIN LIMIT

C DTIME = TIME INCREMENT

C OUTPUT

C DAMAG = NEW VALUE OF ACCUMULATED DAMAGE

The routine USRDM1 has an example on how the above routine is to be used.

The default damage model in DEFORM is the normalized Cockcroft and Latham model in which damage is computed as given below.

C PRNSTS = Maximum principal stress

C New value of damage is found by accumulating damage using the unmodified Cockcroft &

C Latham model

DNT = DSQRT((STS(1)-STS(2))**2 + 4. * STS(4)**2)

S1 = ((STS(1) + STS(2)) + DNT) * 0.5

S2 = ((STS(1) + STS(2)) - DNT) * 0.5

C Calcualte principal stress

PRNSTS = S1

IF(PRNSTS .LT. S2) PRNSTS = S2

C Calculate value of damage ..total

DAMAG = DAMAG + (PRNSTS*EFEPS*DTIME)

C

![]({{ '/assets/images/user_routines/56_2_2d_user_defined_fem_routines/image0006.jpg' | relative_url }})

Specifying user defined damage model in MO

### **User defined material models (USRMAT)**

The user defined material model (USRMAT, sample routine available in usr_mat.f file) can be used to define a unique constitutive model. This will provide flexibility for models which require constitutive equations different than those provided by the default material models. For example, in the case of molten glass or polymers, the constitutive models for rigid-plastic or elasto-plastic models are not sufficient in certain process conditions. This routine allows the user the flexibility to apply a constitutive model to capture instances where the built-in material models don't capture the correct behavior of the process. In the pre-processor or MO, as indicated in Fig. 56.2.7. , user can select object type as user-defined Rigid Plastic objects or user-defined Elasto-Plastic object.

![]({{ '/assets/images/user_routines/56_2_2d_user_defined_fem_routines/image0007.jpg' | relative_url }})

Specifying user defined material model in Preprocessor

**User Defined (Plastic)****[2D] [3D]**

User has been provided with an option to customize the plastic material behavior. User can customize the material behavior using **usr_mat.f**. by defining an unique constitutive model. Only one object with such definition is allowed hence no need to pass any routine number. This object type can be used to simulate rigid-plastic material model. From v12 this new implementation replace the UMAT.DAT function in previous versions. In current v12 DEFORM, SP solver is suggested for user-defined elasto-plastic object problems.

The inputs and output to the USRMAT subroutine are:

C

C INPUT

C DSTRAN(4) : Total strain increment (at t=n+1/2 and rotated by ROT1)

C DFGR0(2,2) : Deformation gradient F(t=n) w.r.t. t=0

C DFGR1(2,2) : Deformation gradient F(t=n+1) w.r.t. t=0

C ROT1(2,2) : Rotation tensor at time n+1/2

C STRESS(4) : Stress at the start of increment

C EPX : Effective plastic strain at the start of increment

C TOLDG : Temperature at the previous increment

C TNEWG : Temperature at the current increment

C TREF : Reference temperature

C

C OUTPUT

C STRESS(4) : Stress at the end increment

C DSAVE(4,4) : Tangent modulus at the end of increment

C EPX : Effective plastic strain at the end of increment

C

The user may also use user-defined elemental values for this constitutive routine.

The user-material routine is responsible to compute the stress components and tangent modulus at the end of the time increment for the Newton-Raphson solution procedure. If the user changes the effective plastic strain as an internal variable, it can be updated using variable EPX. The stress tensor is made up of four independent values. In the case of an axisymmetric simulation, the first value is the radial stress, the second value is the axial stress, the third is the hoop stress and the fourth value is the in-plane shear stress. The tangent modulus is a 4x4 tensor that maps the relationship between stress and strain. This relation can be seen in tensor notation below. Note that the tangent modulus is the tensor Cijkl.

• STRESS(4): Stress at the end increment

• DSAVE(4,4): Tangent modulus at the end of increment

• EPX: Effective plastic strain at the end of increment

The routine USRMAT has an example on how the above routine is to be used.

**Example 1:**

This example shows the user-material routine applied to a elastic constitutive model. Notice that tangent modulus, stress components and plastic strain were updated in this subroutine.

YM=1000

PV=0.3

THIRD=-1./3.

C Elastic tangent modulus

S1=(1.+PV)*(1.0-2.0*PV)

S2=(1.-PV)/S1

S3=YM/(1.+PV)

S4=S3/2.

S5=S3/(1.-2.*PV)

S6=S5*PV

S7=S5-S6

C

C Store elastic tangent modulus in DSAVE

C

DSAVE(1,1)=S7

DSAVE(1,2)=S6

DSAVE(1,3)=S6

DSAVE(2,1)=S6

DSAVE(2,2)=S7

DSAVE(2,3)=S6

DSAVE(4,4)=S4

DSAVE(3,1)=S6

DSAVE(3,2)=S6

DSAVE(3,3)=S7

DSAVE(4,1)=0.

DSAVE(1,4)=0.

DSAVE(4,2)=0.

DSAVE(2,4)=0.

DSAVE(4,3)=0.

DSAVE(3,4)=0.

C Total stain increment

H1=DSTRAN(1)

H2=DSTRAN(2)

H3=DSTRAN(3)

H4=DSTRAN(4)

C

C Calculate elastic stress

C

T1=STRESS(1)+S7*H1+S6*H2+S6*H3

T2=STRESS(2)+S6*H1+S7*H2+S6*H3

T3=STRESS(3)+S6*H1+S6*H2+S7*H3

T4=STRESS(4)+S4*H4

C

C new stress at the end of increment

C

STRESS(1)=T1

STRESS(2)=T2

STRESS(3)=T3

STRESS(4)=T4

C

C No effective plastic strain

C

EPX=0.0

Since the above routine is an elastic material, the tangent modulus is the standard formulation for the generalized Hooke's law. Also, note that the plastic strain is not incriminated since this is a purely elastic material. The stress is computed as,

![]({{ '/assets/equations/user_routines/56_2_2d_user_defined_fem_routines/eq_image0007.jpg' | relative_url }}) |   
---|---  
  
### **User defined nodal boundary conditions (USRBCC)**

User defined nodal boundary conditions (USRBCC) can be implemented to model special boundary conditions not available in standard DEFORM. The routines are available in the file usr_bcc.f. The inputs to the routine are seen below which allow the user to make use of various quantities including nodal temperature and user-defined node variables. If any quantity is not provided in this group, the user can always compute it in user-defined nodal variables and import it into this subroutine.

C Input :

C

C NODE1, NODE2 : edge node number

C MSNODE1,MSNODE2: edge node numbers (master side)

C IELEM : element number it belong

C NBCD(NURZ,2) : boundary condition code

C NDIE : contact condition

C 0 : non-contact

C n : contact to n object

C RZ(2,2) : coordinate of nodes

C DRZ(NURZ,2) : displacement of nodes 

C USRNOD(NUSRN,I) : user defined node variables

C I : node number, user node1 and node2 to get the

C values

C NUSRN : number of user definde node variables

C ENVTEM : environmental temperature or film temperature

C TEMO(2) : previous step temperature

C TEMC(2) : current step temperature 

C CURTIM : current time

As in the other user-defined routines, the user can write an arbitrary number of subroutines so long as the subroutines are defined and the call statements are defined. In each boundary condition window in DEFORM, the user can define a function number which allows the user to use a special subroutine for any type of boundary condition (the only exception is in the case where contact would exist). For example, if the user would want to write a routine to define the heat flux over a certain portion of the boundary, the user would select a portion of the boundary to have heat flux condition. The user would give the heat flux a function number and when the heat flux is computed for that section of the boundary, this routine would be called and the user would need to provide a heat flux value. As seen below, when the heat flux is computed, the subroutine number is found and when heat flux is computed (ITYPE=4), the user can compute heat flux. All the values below can be computed except for friction coefficient.

C MODEL : subroutine number (function number)

C IMODE : simulation type

C 1 : deformation

C 2 : heat transfer

C 3 : diffusion

C ITYPE : output type

C IMODE = 1

C 1 : pressure

C 2 : friction coefficient 

C IMODE =2

C 1 : environmental temperature

C 2 : convection coefficient for free surface

C or lubricant coefficient for contact surface

C 3 : radiation coefficient

C 4 : heat flux

C IMODE = 3

C 1 : environmental atom content

C 2 : surface reaction coefficient

C 3 : atom flux

C NURZ : number of degree of freedom in velocity and displacement

C 2 : for axisymmetric and plane strain 

C 3 : for axisymmetric with angular velocity

C

C Output :

C 

C Variable : user defined boundary coefficient or value depending upon IMODE and ITYPE

C

The user needs to specify the function number as a negative value anytime a user-defined boundary condition routine is used. The output variable for each different combination of output type and mode corresponds to the list above. For example, if heat exchange with the environment is defined (IMODE=2, ITYPE=1), the user would need to supply environmental temperature as the output variable.

**Note:**

If the user desires the use of the relative velocity values in the contact area (SLDVEL) or the normal pressure variable (PRESS), make sure to make the die object an elastic object as these values are not computed for rigid objects.

**Example 1: Friction Factor**

To set a simulation to use a friction user routine, go to the inter-object data definition window as seen in Fig. 56.2.8. The user can set two independent values for the friction:

Friction type

Value

The friction type is one of three friction models supported in DEFORM: constant shear, Coulomb and constant tau (or constant shear).The value is the coefficient value for each individual model. This presents a plethora of capabilities for the user. Here is a listing of the values returned for the various model types:

**Constant shear friction:**

The friction law is governed by the following relationship,

t = m * k

Where

t = shear stress

m = constant shear coefficient

k = shear strength of the slave material

The return value for the user routine in this case is the constant shear coefficient

**Coulomb friction:**

The friction law is governed by the following relationship,

t = m * p

Where

t = shear stress

m = coefficient of friction

p = normal pressure at interface

The return value for the user routine in this case is the coefficient of friction

**Constant tau friction:**

The friction law states that the shear stress at the interface is governed by this value. This can be quite useful for generating a general-purpose law for defining friction behavior.

**Example Case: Norton's friction law**

Norton's friction law has been proposed to be an appropriate law for hot rolling processes. This law is defined by the following equation:

t = b * |Δv|f

Where

t = shear stress

b = constant value

Δv = relative velocity

f = constant value

This can be modeled quite easily using the constant tau model with a user routine. Setting the friction model to constant tau and to a user routine is all that is required from the graphical interface. The user routine also needs to be changed in the following way.

C USER DEFINED FRICTION FACTOR

C

IF (ITYPE.EQ.2) THEN

C

C Norton's law

beta = 0.1

f = 0.1

rel_vel = ABS(SLDVEL)

FRIC = beta * rel_vel ** f

VARIABLE = FRIC

ENDIF

ENDIF

C

Note that there are two tests to enter this portion of the code, IMODE = 1 and ITYPE = 2.When the program is ready to calculate the friction, these two values will be set to this to enter this part of the code. The friction value is then returned by writing the shear stress value to VARIABLE. Note that values for f and b are just for example purposes and not actual material data.

![]({{ '/assets/images/user_routines/56_2_2d_user_defined_fem_routines/image0008.jpg' | relative_url }})

Setting a friction user routine from inter object data in Pre processor

### **User defined lubricant heat transfer (USRBCC2)**

This user routine is the same as USRBCC except that it applies only for the coefficient of lubricant heat transfer. The input variables are (code snippet):

C

C Input :

C

C NODE1, NODE2 : edge node number

C IELEM : element number it belong

C NBCD(NURZ,2) : boundary condition code

C NDIE : contact condition

C 0 : non-contact

C n : contact to n object

C

C RZ(2,2) : coordinate of nodes

C DRZ(NURZ,2) : nodal displacement 

C URZ(NURZ,2) : nodal velocity 

C USRNOD(NUSRN,I) : user defined node variables

C I : node number, use node1 and node2 to get the

C values

C NUSRN : number of user definde node variables

C USRELE(NUSRE,IELEM) : user defined element variables

C I : element number, use IELEM to get the values

C NUSRE : number of user definde element variables

C STRAN(LSTSR,IELEM) : strain components

C LSTSR : number of strain components

C PRESS : nodal pressure

C CONCDS : conductivity for slave (workpiec)

C HICAPAS : heat capacity for slave (workpiece)

C CONCDM : conductivity for master ( die )

C HICAPAM : heat capacity master (die )

C ENVTEM : environmental temperature or film temperature

C TEMO(2) : previous step temperature

C TEMC(2) : current step temperature 

C CURTIM : currunt time

C MODEL : subroutine number (function number)

C IMODE = 2 : simulation type heat transfer

C ITYPE = 2 : output type lubricant coefficianet

C NURZ : number of degree of freedom in velocity and displacement

C 2 : for axisymmetric and plane strain 

C 3 : for axisymmetric with angular velocity

C

C /USRCTL/ KOBJ,ISTATUS,KSTEP,KSSTEP

C

C KSTEP : number of step

C KSSTEP : negative step indicator -1 for negative step or 1

C

C Output :

C 

C Variable : user defined boundary coefficient or value

C

**Simple example case #1**

This simple case is meant to demonstrate how to set the lubricant heat transfer value within a user routine.

![]({{ '/assets/images/user_routines/56_2_2d_user_defined_fem_routines/image0009.jpg' | relative_url }})

Setting the lubricant heat transfer coefficient to a user routine in Preprocessor

  1. Set the lubricant heat transfer coefficient to use a user routine. This can be done as seen in Fig. 56.2.9.

  2. Define the user routine to the specifications desired for the lubricant heat transfer coefficient. In this example case, the keyword UPSET.KEY from the DATA directory was used and half of the top area of the work piece-tool interface was set to no heat transfer and the other half was set to a value of 5. This was done in the following code:

IF(RZ(1,1).gt.19.05) THEN

VARIABLE = 5.0

ELSE

VARIABLE = 0.0

ENDIF

If the radial value of the node coordinate was greater than half of the radius of the part, the heat transfer coefficient was set to 5 and otherwise it was set to zero.

  1. Compile the routine and place it where it can be run as the current engine.

### **User defined general routine (USRMSH)**

This user routine is recommended when no other routine will accomplish what is desired. The flexibility of this routine makes this a very powerful option but often other routines will accomplish the same task in much less effort. This routine is called once at the beginning and end of each step. Also, it is called once for each object in the simulation. For example, if there are 3 objects in a simulation, this routine will be called three times (once for each object) at the beginning of each step and three times at the end of each step.

A list of the input variables is taken from the code and is listed as follows:

C

C************************************************************

C All FIELD VARIABLES CAN BE CHANGED!

C IMPROPER CHANGE MADE IN THIS ROUTINE WILL CAUSE PROBLEMS

C IN THE ANALYSIS. PLEASE USE THIS ROUTINE WITH CAUTION!!

C************************************************************

C

C This routine will be called at the beginning of the step and

C at the end of the step

C

C Object with FEM mesh will be passed to this Routine

C

C REAL*8 arrays

C

C RZ(2,NUMNP): Nodal Coordinateis

C DRZ(2,NUMNP): Nodal displacemnts

C URZ(2,NUMNP): Nodal Velocities

C TEMP(NUMNP) : Nodal temperatures

C DTMP(NUMNP) : Nodal temperature change for the step

C FRZA(2,NUMNP): Nodal Point external forces

C FRZB(2,NUMNP): Nodal point reaction forces

C EFSTS(NUMEL): Effective stress

C EFEPS(NUMEL): Effective strain rate

C TEPS(NUMEL) : Total plastic strain

C RDTY(NUMEL) : Element Densities

C STS (4,NUMEL): Stress tensors

C EPS (4,NUMEL): Strain rate tensors

C DCRP(4,NUMEL): Creep rate tensors

C TSRS(4,NUEML): Strain Components

C DAMG(NUMEL) : Damages

C USRVE(NUSRVE,NUMEL): User Defined Element Variables

C NUSRVE: Number of User Defined Element Variables

C (Must be declared in the Pre-Processor)

C USRVN(NUSRND,NUMEL): User Defined Nodal Variables

C NUSRND: Number of User defined Node variables

C (must be declared in the Pre-processor)

C

C ATOM(NUMNP): Dominating Atom Contents

C HEATND(NUMNP): Nodal Heat Source

C

C EPRE(NEDGE): Pressure on the boundary edges

C (based on the boundary node list:NBDRY)

C (Positive - tension, Negative-compressive)

C

C VOLT(NUMNP): Voltage at Node (vailable Only for Heating Module)

C

C WEAR(5,NUMNP): Die wear related Data

C WEAR(1): Interface temperature (in Deg. Absolute)

C WEAR(2): Sliding velocity

C WEAR(3): Interface pressure 

C WEAR(4): wear rate

C WEAR(5): integrated wear depth (upto the current step) 

C Note:

C WEAR(1:5,N) are computed

C for rigid meshed die nodes when

C tool wear models are turned on in Pre processor

C in the inter object data definition.

C

C MICRO-STRUCTURE RELATED VARIABLE

C

C Available ONLY for HT application

C

C HDNS(2,*) : Hardness

C VF(NTMATR,*) : Volume Fraction

C VFN(NTMATR,*) : Transformation Starting Volume Fraction

C DVF(NTRELN,*) : Transformation Volume Fraction Change Ammount

C TICF(NTRELN,*) : Incubation Time

C GRAIN(NGRNVAL,*): Grain Size

C

C REAL*8 Variables

C

C CURTIM : Current Time

C DTMAXC : Time Step

C AVGSRT : Average strain rate

C SRTLMT : Limiting Strain rate

C

C Integer*4 Integer Arrays

C

C NBCD(2,NUMNP): Nodal Boundary Condition

C 0- Traction specified => FRZA

C 1- prescribed Velocity => URZ

C 2- Pressure Specified => EPRE

C NBCDT(NUMNP): Temperature Boundary Condition

C 0- Prescribed Nodal heat

C 1- Prescribed Nodal Temperature

C

C NOD(4,NUMEL): Element Connectivity (global node numbering)

C MATR(*) : Material Group Number:

C NBDRY(NEDGE): Boundary Node list (Global node numbering)

C

C Interger*4 Integer Variables

C

C KOBJ : Current Object number

C

C NUMEL: Total Number of Elements of KOBJ

C NUMNP: Total Number of Nodes of KOBJ

C NDSTART: Starting Node Number of KOBJ

C NDEND : Ending Node Number of KOBJ

C

C NEDGE: Total Number of Boundary edges of KOBJ

C NTMATR: Total Number of Materials

C NTRELN: Total Number of Inter-materail relations

C NGRNVAL: Number of Grain-related Variables

C NROUTINE: User Controlled Routine Number

C

C ISTATUS: 0 -> Called at the beginning of each step prior to the analysis

C 1 -> Called at the end of each step prior to writing to database

C

C AXMT : material axis rotation

C

C NODAL DEFINITION OPTIONS

C IELMNOD(K) = 0 : Element definition

C > 0 : Node+element definition

C K = 1,2,3 -- REFERRING TO DAMAGE, EFF. STRAIN AND STRESS

C COMPONENTS (ELASTOPLASTIC OBJECT), RESPECTIVELY

C EFEPS_NP(NUMNP) : Nodal eff. strain rate

C TEPS_NP(NUMNP) : Nodal eff. strain

C DAMG_NP(NUMNP) : Nodal damage factor

C STS_NP(NUMNP) : Nodal stress components (elastoplastic object) 

C

C For example for a given meshed object (either plastic or

C elasto-plastic) once user turns on option to compute

C the nodal strains (in the Pre Processor > Simulation controls >

C Advanced > Output control) the stored values of the nodal strain

C strain rates can be extracted from the arrays TEPS_NP and

C EFEPS_NP. For example the following statement assigns

C nodal effective strain for the node 123 to the variable RN123

C RN123 = TEPS_NP(123)

C

No output is required for this routine.

**Example #1: Calculating wear at a tooling interface**

In this example, we will calculate the tool wear at the interface nodes for a rigid object. The reason that USRMSH is the correct routine for this requirement is that five useful parameters are passed to this routine in the array WEAR:

**Nodal area**

****(This is an average area represented by a node. In axisymmetric mode this is an annular

region and it is a rectangular area in plane strain mode)

**Contact temperature**

****(the temperature at the node)

**Sliding velocity**

****(the relative velocity between the two surfaces at the contact node).Note that this is a signed quantity based on the direction of sliding so the user should be cautious to apply an absolute value when necessary for wear calculations.

**Shear stress**

****This is the shear stress at the contact node.

**Contact pressure**

****This is the normal pressure at the contact node. A negative quantity indicates compression and a positive quantity indicates tension.

The USRMSH routine can be edited in the following manner:

C Check for beginning of step and if so, return and do nothing

IF (ISTATUS.EQ.0) RETURN

C

C Loop over all nodes in a given object

DO 100 NODE=NDSTART,NDEND

C

IF (KOBJ.EQ.3) THEN

C

IF (ABS(WEAR(3,NODE)).GT.1.E-10) THEN

C

C The node is contacting with other object

C

USRVN(1,NODE) = USRVN(1,NODE) +(WEAR(3,NODE) * WEAR(5,NODE))/45.0

ENDIF

ENDIF

100 CONTINUE

The first IF statement checks whether it is the beginning or end of a step. If it is the beginning of a step, return and don't do anything. If it is at the end of a step, the next portion of code is executed. The DO loop after this loops over all the nodes in the current object. The variables NDSTART and NDEND are the starting and ending node numbers for the current object based on the global node numbering. In the case of the first object, this will be a loop over the first node to the last node in the first object. For the second object, this is be the over the last node number for the first object plus one to the sum of the first two object node numbers. Inside this DO loop, the object number is tested. If the current object is the third object, then proceed within the loop, otherwise do nothing. After this, each node is tested whether there is a non-zero sliding velocity. If the sliding velocity is non-zero, then proceed, otherwise do nothing. At this time, the first user node has measure of wear defined as function of sliding velocity and contact pressure. This can then be plotted in the post-processor. The users can insert their own routine here.

### **USRUPD_S** :

A new subroutine Fortran file usr_upd_s.f has been added from v11.3. This user routine is similar to usr_upd.f except that it has additional information regarding remeshing and restarting step.

Additional part in usr_upd_s.f compared to that of usr_upd.f is as below (for information regarding usr_upd.f refer section 56.2.3.3. User defined node and element value (USRUPD)),

C .. RESTARTING/ REMESHING FLAG for INTERNAL USER'S VARIABLES

C

C IREMSH : (=2;restaring step),(=1;remeshing step),(=0;regular step)

C NUMELM : number of total elements

COMMON /USRFLG/IREMSH,NUMELM

C

**Example 1: In this example** ,

At remeshing step we are printing the text as "Remeshing step" and Number of elements at remeshing step.

At restarting step we are printing the text as "Restarting step" and Number of elements at restarting step. Please see Fig. 56.2. 10.

C .. RESTARTING/ REMESHING FLAG for INTERNAL USER'S VARIABLES

C

C IREMSH : (=2;restaring step),(=1;remeshing step),(=0;regular step)

C NUMELM : number of total elements

COMMON /USRFLG/IREMSH,NUMELM

C

C

IF(IREMSH.EQ.1)THEN

C .. REMESHIN STEP: WRITE THE INTERNAL VARIABLES ON THE FILE

write(*,*) 'Remeshing step',NUMELM

ELSEIF(IREMSH.EQ.2)THEN

C .. RESTARTING STEP: READ THE INTERNAL VARIABLES FROM THE FILE

write(*,*) 'Restarting step',NUMELM

ENDIF

![]({{ '/assets/images/user_routines/56_2_2d_user_defined_fem_routines/image0010.jpg' | relative_url }})

Restarting and Remeshing step with Number of Elements information in Message file

## Compiling user routines for Linux platforms

The user routines are called for each node/element for every step during the simulation and efficient coding practices should be followed to minimize simulation time. Do not open or close data files during each subroutine call as this can degrade performance significantly. The USRDEF field in the pre-processor can be used to store a limited number of parameters. If you require more space than what is available in USRDEF then open the data files in the user subroutines and store a static variable in a COMMON block so that the file does not have to read each time the user subroutine is called.

Typically user is expected to make a copy of /USR folder from the installed folder available at $DEFORM_DIR/USR (default location being /usr/local/SFTC/DEFORM/v11.1/2d/USR). After the FORTRAN code has been modified a new local FEM engine can be build using the script build_fem or DEF_INS.COM which are available in /USR folder.

This builds a new copy of the FEM engine DEF_SIM.EXE in the local directory. After this process is completed, simulations using the new user defined routines can be run using the local copy of the FEM engine.

## Compiling user routines on Windows

Like in the Linux environment, make local copy of the folder 2D\UserRoutine\DEF_SIM (from the install structure e.g c:\Program Files\SFTC\DEFORM\v13.1).

  
The “<DEFORM install path>\v13.1\2D\UserRoutine” folder contains subfolders for static and dynamic linking methods.

  1. The first folder is called “**DEF_SIM** ”, which allows for compiling of an FEM executable (.exe) via a static link library. This folder contains static link batch (.bat) files for the Absoft and Intel compilers. Build scripts provided along with release pack, 

  * For Absoft - DEF_SIM_USR_Absoftv110.amake or DEF_SIM_USR_Absoftv110.atools in the Absoft compiler or using the batch file build_def_sim_usr_Absoftv110.bat

  * For Intel FORTRAN Compiler – using he batch file build-FEM-USR-PC-64bit-intel-compiler-2022.bat

  
Using the build scripts provided, users locally modified FORTRAN subroutines will be compiled and linked to the object code named DEF_SIM_USR64_LIB.lib (Absoft) or DEF_SIM_USR64_INTEL_LIB.lib (Intel) found in this directory. This will then generate a new FEM engine, named DEF_SIM_64.EXE. The released DEF_SIM_64.EXE should be replaced with the customized DEF_SIM_64.EXE, after first making a copy of the released executable.

![]({{ '/assets/images/user_routines/56_2_2d_user_defined_fem_routines/image0011.jpg' | relative_url }})

UserRoutine DEF_SIM folder

  1. The second folder is called “**DEF_SIM_DLL** ”, which allows for compiling of user routines as _dynamic link library_ (.dll) files. This folder contains dynamic link batch files, Absoft_build_all_dll_command.bat for the Absoft and Intel_build_all_dll_command.bat for the Intel FORTRAN compilers.

When the preferred batch file is executed, .dll files will be compiled with the Fortran (.f) user routine files found within this directory. The resulting .dll files and the Intel DEF_SIM_64.EXE (located in “<2D>\DEF_SIM_64\Intel_modern”) should be copied to a new folder. DEF_SIM_DIR.DAT should then be edited to specify the new folder as the location for the customized DEFORM implementation. Please note that either Absoft or Intel compiled .dll files may be linked with the Intel DEF_SIM_64.EXE.

![]({{ '/assets/images/user_routines/56_2_2d_user_defined_fem_routines/image0012.jpg' | relative_url }})

UserRoutine DEF_SIM_DLL folder

**Note** :

User needs to specify the version number of Microsoft Visual Studio installed on their computer before compiling the program using the **build-FEM-USR-PC-64bit-intel-compiler-2022.bat** or **Intel_build_all_dll_command.bat** file. The Visual Studio version is set to 2019 in the example .bat file provided using the following command:

  
call "C:\Program Files (x86)\Intel\oneAPI\setvars.bat" intel64 vs2019

  
User should update this command to match the version of Visual Studio that has been installed on the computer. For example, if Visual Studio 2022 is installed, user would update the command as follows:

  
call "C:\Program Files (x86)\Intel\oneAPI\setvars.bat" intel64 vs2022

## Running the modified FEM engine for Linux platforms

**Option.1**   
If the FEM engine is built in the DEFORM directory with user routines, all users have access to the same user routines. If a local copy of the FEM engine is to be built and run, then the DEF_ARM.COM script must be copied to the local directory and the calls to DEF_SIM.EXE must be modified to call the local copy of the program. In place of the calls,

$DEFORM_DIR/EXE/DEF_SIM.EXE

replace it with

./DEF_SIM.EXE

where

./DEF_SIM.EXE is the local copy of the FEM engine.

When simulation jobs are submitted using the GUI or text based main program, the alias DEF_ARM is used to start the script DEF_ARM_CTL.COM which in turn runs DEF_ARM.COM.

When using a local copy of the FEM engine, copy DEF_ARM_CTL.COM to a local directory and change the alias for DEF_ARM to point to the local copy of DEF_ARM_CTL.COM. This alias is defined in the $DEFORM_DIR/CONFIG.COM and a line in the .cshrc after the

source $DEFORM_DIR/CONFIG.COM redefining the alias should work.

In the .cshrc file the following modifications can be made. (indicating the installation path as carried out by the user)

setenv DEFORM_DIR '/usr/local/SFTC/DEFORM/v11.1/2d'

source $DEFORM_DIR/CONFIG.COM

#

# Old alias

#

alias DEF_ARM $DEFORM_DIR/COM/DEF_ARM_CTL.COM

#

# New alias which is a local copy of DEF_ARM_CTL.COM

#

alias DEF_ARM $HOME/DEF_ARM_CTL.COM

Also in the local copy of DEF_ARM_CTL.COM the following calls should be replaced.

$DEFORM_DIR/COM/DEF_ARM.COM

with the local version of

$HOME/DEF_ARM.COM

After this has been done simulations can be run using the local copy of the FEM engine and jobs can be started using the user-interface.

One problem that can occur is that if the .cshrc has an exit for non-interactive shells and the new definitions are after this, then they will never be defined when running a simulation. Place the new command to run the local copy of DEF_ARM just after the definitions for the regular version of DEFORM.

**Option.2**   
From DEFORM v11.1 in Linux environment a new facility is available to run the user routines without disturbing the installed copy of FEM engine. In the problem folder (having DB), user can simply place a text file called DEF_SIM_DIR.DAT containing the full path to this local FEM engine compiled for user routines. Execution of the model itself can be done from the GUI. Once the model running scripts see the local FEM path defined in the DAT file as indicated, model picks up local FEM engine at the run time.

## Running the modified FEM engine for Windows platforms

**For Static Link built DEF_SIM_64.EXE**

**Option.1**

If the FEM engine has been built for Windows, one way in which to run it is to swap (first backup original file) it with the current FEM engine. The current FEM engine which can be located with the current installation of DEFORM-2D usually in a directory such as C:\Program Files\SFTC\DEFORM\v13.1\2d. If it is not there, look for a file named DEF_SIM_64.EXE if installation is done in a different folder.

**Option.2**

From DEFORM v11.0 in Windows environment a new facility is available to run the user routines without disturbing the installed copy of FEM engine. In the problem folder (having DB), user can simply place a text file called DEF_SIM_DIR.DAT containing the full path to this local FEM engine compiled for user routines. Execution of the model itself can be done from the GUI. Once the model running scripts see the local FEM path defined in the txt file as indicated, model picks up local FEM engine at the run time.

**For Dynamic link DLL files**

In the problem folder (having DB), user can simply place a text file called DEF_SIM_DIR.DAT containing the full path to the folder having the compiled dll files along with Intel FORTRAN compiled DEF_SIM_64.EXE original file from “<2D>\DEF_SIM_64\Intel_modern” folder.

**Related Topics:**

[56.3. 3D User Routine](/docs/sk/user_routines/56_user_routines_in_deform/56_3_3d_user_defined_fem_routines/)
