---
lang: en
title: "3.4. Trouble Shooting License Issues"
---

# 3.4. Trouble Shooting License Issues

3.4.1. Identifying License Server v12.1 Problem

3.4.2. Solving License Server v12.1 Problem: Specific Topic Issues

3.4.3. Miscellaneous Service Related Notes

## Identifying License Server v12.1 Problem

**Step 1**

Check whether the License Server is running by opening the “services” tab in Task Manager. If DeformLicenseserver appears as a running service, then it is running.

  * If it is running, go to Step 2 (A) explained below.

  * If it is not running, go to Step 2 (B) explained below.

  
**Step 2**

(A) This is likely a password or hardware key problem. There are three ways to check:

  * View the most recent log file [usually in C:\Program Files\SFTC\License Manager\log\<year>\\].

  * Run the diagnostics tool from INSIDE the License Manager folder [usually located at C:\Program Files\SFTC\License Manager\Defdiag.exe], and click the Get Information… button. The resulting .dgf file will help support team to diagnose the issue.

  * If in DEFORM Setup, clicking the ![]({{ '/assets/icons/pre_icons/mo_syncronize_button.jpg' | relative_url }}) button results in “license server is terminated”: hardware key problem.

If log file is used to check for errors:

  * If the log file indicates the hardware key is invalid: hardware key problem. Please send the .dgf file to [support@deform.com](mailto:support@deform.com)

  * If the log file says “no password” or “no available password”: password problem. Please contact [support@deform.com](mailto:support@deform.com). Please note that if you have received a new password file to replace an expired password file, it is important to restart the License Manager Service or reboot the License Manager Server machine.

(B) An old license server is running, register service problem or installation problem:

If the log file [usually in C:\Program Files\SFTC\License Manager\log\<year>\\] says “old license server (v2.1) may be running”, problem identified: old license server is running.

  * Please open DEFORMSetup and visit Services tab. In Services tab click on “Open DEFORM Service for local DEFORM computer”. We should be seeing an error mark as shown in [Fig. 3.1.21.](3_1_deform_license_setup.htm#Fig._3.1.21._Updating_Simulation_services_files_in_DEFORM_Services_window)(a). The error mark ![]({{ '/assets/icons/pre_icons/error_status_icon.jpg' | relative_url }}) indicates that Local DEFORM computer is not using the same version of the License Manger as that of the DEFORM License server system hence click on ![]({{ '/assets/icons/pre_icons/mo_deform_setup_update_icon.jpg' | relative_url }}) icon to update the Local DEFORM Computer services. Once the services are updated, we can notice ![]({{ '/assets/icons/pre_icons/mo_deform_setup_valid_sucess_icon.jpg' | relative_url }}) icon next to the Local DEFORM Computer. DEFORMsetup can be closed and DEFORM GUI can be launched from Start ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Programs.

If problem is still not identified, please contact [support@deform.com](mailto:support@deform.com).

## Solving License Server v12.1 Problem: Specific Topic Issues

### Password problem

Copy the correct v*_* (where *_* is the version number of the DEFORM) DEFORM.PWD to the license server directory (C:\Program Files\SFTC\License Manager). A reboot or service restart is required to load/activate the new password file.

### Hardware key problem check list

  * It is important to uninstall Sentinel driver versions 7.5 or older. Please remove the hardware key, uninstall the old driver(s) and install the new driver.
  * Check whether the user installed Sentinel driver version 7.6.3 (being an option in the installation process). If not, please install the new driver.
  * Check whether the USB port is inactive. Switch the USB key to another USB port and try to restart the service and server.
  * If an error message of “Failed to add Sentinel64.cat file” occurs while installing the Sentinel driver on Windows 7, and you are using a USB hardware key, this error can be safely ignored.

### Old license is running

User needs to uninstall the old license server (v2.1) or disable it.

### Service startup problem

This may happen occasionally, particularly if the user swaps the USB key between computers. Following methods can be used to start the DeformLicenseServer service when it shows up in the Windows service list and is also stopped. 

  * Reboot the License Server computer.

  * Open the Services management console (not Task Manager) and manually start the service.

  * Open DEFORMSetup and visit services tab, if license server is on local system then select “Open DEFORM Service for local DEFORM computer” else select “Open DEFORM Service for all DEFORM computers” and enter pass code. Click on![]({{ '/assets/icons/pre_icons/run_action_icon.jpg' | relative_url }}) button next to License Server under “Actions” column to start the service.

## Miscellaneous Service Related Notes

**Notes on Services in Windows Vista and later**  
Elevated administrator permission via Windows User Access Control [UAC] is required to register, start or unregister service. This is needed even if the user already has administrative privileges on the computer. Service management can be performed in the Services management console or by using “Run as administrator” with DEFORM service start menu shortcuts.

**Related Topics:**

[3.1. DEFORM License Setup](/docs/en/starting_up_deform/3_license_manager/3_1_deform_license_setup/)

[3.2. License Monitoring](/docs/en/starting_up_deform/3_license_manager/3_2_license_monitoring/)

[3.3. Services Monitoring](/docs/en/starting_up_deform/3_license_manager/3_3_services_monitoring/)
