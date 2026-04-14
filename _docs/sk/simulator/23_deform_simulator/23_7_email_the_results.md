---
lang: sk
title: "23.7. Email notification of the simulation"
---

# 23.7. Email notification of the simulation

This function allows DEFORM to send an email notification at the start of the simulation and with last 25 lines of Message file and Log file at the end of simulation. Email settings can be accessed from **Options**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Environment** as shown in Fig. 23.7.1. We need to provide SMTP server information, user name and password as shown in Fig. 23.7.2.

![]({{ '/assets/images/simulator/23_deform_simulator/23_7_email_the_results/image001.jpg' | relative_url }})

Environment settings

Emails are sent via SMTP using StartTLS (or no security), so the SMTP server hostname and port are required. Selecting the popup menu to the right of the Port field allows for automatic filling of some settings for some public email services (e.g. Gmail and Outlook). (See Fig. 23.7.2.)

  
Please check with your IT for details on your company SMTP email server settings.

![]({{ '/assets/images/simulator/23_deform_simulator/23_7_email_the_results/image002.jpg' | relative_url }})

Settings for Email notification on simulation status

If your email server requires login (which most do), check the Server requires login checkbox and enter your username and password.  
Notifications can be sent to multiple email addresses; set the destination emails in the **Addresses to send email** fields.  
Once all the settings are filled in, click the **Test email settings** button to verify them. If everything is correct, all the destination addresses will receive a confirmation email. (See Fig. 23.7.3.)

![]({{ '/assets/images/simulator/23_deform_simulator/23_7_email_the_results/image003.jpg' | relative_url }})

Selecting a public email server

For Gmail accounts with 2-Step Verification enabled, please see the link for details on setting up an App Password. _https://www.deform.com/redirects/gmailapppassword.html_

The default port for StartTLS SMTP email servers is 587.
