---
lang: en
title: "56.1. Introduction to User Routines"
---

# 56.1. Introduction to User Routines

  
This chapter explains the various user routines available in the DEFORM system in the FEM (Finite Element Method) engine and the post-processor. Examples on how to use each type of routine, how to compile the code and how to run the modified FEM engine and post-processor are also covered.

DEFORM V13.1 brings with it a few important changes in its support for Fortran compilers. Historically, SFTC has relied upon the Absoft Fortran compiler for DEFORM release and user routine code compiling. The Absoft Corporation closed their business in late 2022, ending sales and support for the Absoft Fortran Pro compiler. SFTC has committed to continuing to support the Absoft compilers for a period of time as the Absoft compiler is phased out.

DEFORM V13.1 introduces support for Intel® Fortran Compiler. The free Intel compiler represents a computing upgrade, as it is designed for modern hardware. Testing has shown that it generally provides improved performance over the older Absoft compiler.

  
For instructions on how to download and install Intel® Fortran Compiler, please refer [Appendix XXI: FEM User routine support](/docs/en/appendices/appendix_xxi_fem_user_routine_support/).

**Prerequisites:**

The user should have at least a rudimentary understanding of the FORTRAN language. This section is not meant to be an introduction into the FORTRAN language rather it is meant to explain how to build the user routines and how to implement them within DEFORM. For more information on the FORTRAN language, please refer to many books or the documentation that was included with your compiler or on the web.

**Overview:**

There are two different types of user routines available:

  1. User-Defined FEM Routines

  2. User-Defined Post-Processing Routines

The two different types of User Routines will be outlined below as to their purpose and how they are implemented. Later in this chapter, each one of these routines is explained in greater detail on how to implement each subroutine. To implement the user routines user must have a FORTRAN compiler installed on your system. The build scripts are provided with the system installation. 64 bit FEM support is available for 3D and 2D FEM.

**Note:**

The manner in which the User-Routines are compiled and linked is slightly different between Windows and Linux platforms. These differences are outlined in detail later in this chapter.

From v13.1 onwards, DEFORM® supports both static linked library (which builds DEF_SIM.EXE) and dynamic linked library (which builds DLL file) for user-defined FEM Routines.

Supported Machine and Compiler related details are,

  1. Centos 5.10 (2.6.18-371 x86-64 Equivalent to Redhat Enterprise Linux 5) using Absoft Fortran90 v11.0 (64 bit version of the compiler).

  2. Centos 6.5 (2.6.32-431 x86-64 Equivalent to Redhat Enterprise Linux 6) using Absoft Fortran90 v11.0 (64 bit version of the compiler).

  3. Suse Enterprise Linux Desktop (3.0.101-0.18 x86-64 Equivalent to Suse11 sp3) using Absoft Fortran90 v11.0 (64 bit version of the compiler).

  4. PC Win7, Win8, Win10 using Absoft Fortran90 v11.0 and Intel Fortran compiler (64 bit version of the compiler).

In PC Win10 environment the DEF_SIM system is built using Absoft Fortran90 v11.0 and Intel Fortran compilers. However the DEF_SIM object files for the earlier versions of Absoft Fortran90 v9.0 (has only 32bit support) is also built and released as a part of official release pack. It was noted that the code generated using Absoft Fortran90 v11.0 is faster compared to the earlier versions of the same compiler. (Support for Absoft v7.0 and Absoft v7.5 compilers has been dropped from DEFORM v10.2 release).

From DEFORM v13.0, support for 32bit User-Defined FEM Routines and User-Defined Post-Processing Routines has been dropped.

**Related Topics:**

[56.2. 2D User Defined FEM Routines](/docs/en/user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines/)

[56.3. 3D User Defined FEM Routines](/docs/en/user_routines/56_user_routines_in_deform/56_3_3d_user_defined_fem_routines/)

[56.4. User-Defined Post-Processing Routines](/docs/en/user_routines/56_user_routines_in_deform/56_4_user-defined_post-processing_routines/)
