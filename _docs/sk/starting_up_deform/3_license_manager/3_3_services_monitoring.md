---
lang: sk
title: "3.3. Services Monitoring"
---

# 3.3. Monitoring Services

In DEFORM system, we are having 3 services for license and queuing the simulations. These are DeformLicenseServer, DeformSimServer and DeformBatchQueue server.

License server controls all the DEFORM license dependent products and options based on the license password provided by SFTC. This includes 2D or 3D module, different DEFORM wizards, number of simulations, queueing the simulations and multiple processor  
simulations. 

Batch queue server is used to submit the batch of jobs in queue. User can submit one or more jobs to run in queue based on the licenses available and number of simultaneous simulations allowed from simulation server. When queueing the jobs, Simulation server must be running in the machine where jobs need to be run.

**Start, Stop and Restart the services:**

User can Start and Stop the services from Task manager, but running the services from Windows Administrative tools Service will provide more options like Run as any of the User or Run as System. User needs to open the Services as administrator.

  
**Checking Services Status:**

Services status can be checked from the Task Manager Processes tab in Windows-XP by observing the server executable files status, in case of Windows7, Windows 8 and Windows 10 machine the status can be checked from the Services tab.  
This can also be checked from the Windows Administrative tools Services by observing its status.

Restarting the system will automatically start all 3 DEFORM services, in sever machine running the batch queue service and simulation service in client machine where jobs need to be run is must to submit the jobs in queue. So user must check these services status before submitting the jobs in queue. This can also be checked from DEFORM Main GUI Run options dialog Check Server option.

In case of any license related issues, user can observe the License Log file for any specific error messages for the services start or stop.

**Related Topics:**

[3.1. DEFORM License Setup](/docs/sk/starting_up_deform/3_license_manager/3_1_deform_license_setup/)

[3.2. License Monitoring](/docs/sk/starting_up_deform/3_license_manager/3_2_license_monitoring/)

[3.4. Trouble Shooting License Issues](/docs/sk/starting_up_deform/3_license_manager/3_4_trouble_shooting_license_issues/)
