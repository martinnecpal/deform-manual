---
lang: sk
title: "23.5. Setting up MPICH"
---

# 23.5. Registering MPICH (applicable to v11.1.1 and below versions)

## Registering 64 bit 3D FEM engine in PC

As part of DEFORM v*_* (where *_* is the version number of the DEFORM) installation, user will be prompted with an option to install 'MPICH2 64bit'. On 64 bit machines this installation is required to run 64 bit 3D FEM engine. This part of the installation also requires the following post installation procedures to ensure 64 bit run time environment,

From DEFORM v11.0 the following MPICH2 64bit setup requirements are completely handled during the system installation itself. The following steps can also be used to trouble shoot MPICH2 related issues if any that come up at a later stage for any other reason.

  1. Open command window as administrator and change the directory to MPICH2 folder _'cd c:\Program Files\MPICH2\bin'_ and execute two commands one by one ‘s _mpd.exe -install', 'smpd.exe -restart'_.

  2. Open command window as administrator and change the directory to MPICH2 folder '_cd c:\Program Files\MPICH2\bin'_ and execute _'mpiexec.exe -register'_ with user name and password.

  3. For SimulationServer services, user needs to go to the system services, select the running '_DeformSimServer_ ' and select 'Properties' with a right mouse click and set user account name and password for the user from the 'Log On' tab.

## Running 64 bit 3D FEM engine in Linux/PC

  * From the 3D / 2D3D GUI select the problem and go to Run options and select the 64 bit option. Click on Start to start the 64 bit simulation.

  * Flag file '64bit.DAT' is required in the problem folder to start 64 bit FEM run from GUI Main. This '64bit.DAT' file will be created automatically as we select the 64 bit option from the Run options. Without this flag file, regular 32 bit FEM code takes preference.

**Note:**

  1. This 64 bit version can handle large models that require main memory in excess of 2 GB.

  2. 64 bit support is only for the 3D FEM engine.

  3. While building FEM engine with user routines, please use the OS identifier as centos_linux64.

**Related Topics:**

[23.1. Start, Stop and Resume Simulation](/docs/sk/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/)

[23.2. Interactive and batch modes using Run option](/docs/sk/simulator/23_deform_simulator/23_2_interactive_and_batch_mode/)

[23.3. Simulation Graphics](/docs/sk/simulator/23_deform_simulator/23_3_simulation_graphics/)

[23.4. Process Monitor](/docs/sk/simulator/23_deform_simulator/23_4_process_monitor/)
