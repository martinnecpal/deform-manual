---
lang: en
title: "57.3. DEFORM Data Analytics Data Import and Export"
---

# 57.3. DEFORM Data Analytics Data Import and Export

57.3.1. Import overview

57.3.2. Importing a text file or .CSV file

57.3.3. Importing a DEFORM simulation database

57.3.4. Importing a DEFORM DOE database

57.3.5. Importing multiple DEFORM simulation databases

57.3.6. Data export

## Import overview

Data can be imported from text files (.txt or .csv -comma separated values) This file type can be exported from many applications such as spread sheets), DEFORM simulation Databases (.DB), or DEFORM DOE databases (.SDB). Data from different files can be combined into a single table using multiple imports.

  
Prior to adding imported data to the data table, the imported data can be previewed prior to the actual import. The import can be canceled if desired.

## Importing a text file or .CSV file

Text data files (either .txt or .csv) can be imported as long as the file is a text file and the data is arranged in rows and columns with a consistent delimiter between the values.

  
Once a DEFORM Data Analytics project has been created, select a data table and click on ![]({{ '/assets/icons/post_icons/mo_import_icon.jpg' | relative_url }}) button to import a text file. Once a file is opened, an interface will be opened as shown in Fig. 57.3.1. with the preview of the data from the file. The interface consists of the following options:

  
**Delimiter** : This option specifies the character that is used in the file separating values. Commonly used delimiter options such as Comma, Semicolon, Tab and White space are available for selection. If the file uses any other delimiter, select “Other” and specify the delimiter in the field next to it. Sometimes it may be necessary to look at the file in a text editor to determine the delimiter prior to importing it.

**Source****data** : “Import all rows” or “Import a subset of rows” can be used to specify which rows of data to import. If “Import a subset of rows” is selected, a subset of the rows can be selected by dragging mouse over row headers in the preview or by defining the start row and end row as shown in the Fig. 57.3.1.

**Data** **contains****column** **label** : If the imported data has column labels, the checkbox can be selected to import the text of a specified row into the column names. By default, the first row is considered as the column labels. If the labels are in any other row, then the row number can be entered in the “Row” field.

**Transpose****rows****into****columns** : If the data imported is transposed i.e., the column data is displayed as rows, clicking this button will transpose rows into columns before importing into table. Clicking again will undo the transpose.

**Data****Handling** : The data selected for import can be appended as new rows or as new columns to the existing data or Replace the existing data. “Map columns” maps the preview data to existing columns as shown in Fig. 57.3.1. If Map columns is checked, the Import to options on the preview will be enabled. Each column can then be imported to a specified column in the data table, imported to a new column, of not imported.

![]({{ '/assets/images/data_analytics/57_3_deform_data_analytics_data_import_and_export/57_3_image0001.jpg' | relative_url }})

Defining the text import options

## Importing a DEFORM simulation database

State variable values can be imported from DEFORM simulation databases for a selected object at a selected simulation step.

  
Once a DEFORM Data Analytics project has been created, select a data table and click on ![]({{ '/assets/icons/post_icons/mo_import_icon.jpg' | relative_url }}) button to import a DB file. Once a file is opened, an interface will be opened as shown in Fig. 57.3.2.. After selecting object, step, and some state variables, clicking Update preview will fill the preview table.

  
Each state variable will be imported in columns, each node/element will be rows. To import state variables from multiple objects or multiple steps, the import will need to be repeated.

  
The interface consists of the following options:

  
**Object** : Selects the object to import the state variables from.

  
**Step** : Selected the simulation step to import the state variables from.

  
**State****Variables** : Selects the state variables to import. the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button will add a state variable to the list below. Selecting an item in the list will display a drop down menu used to select the state variable. The second column of this list selects the component of the state variable.

  
**Update****Preview** : Updated the preview table after object, step, or state variables have been changed.Column names from state variable: Set the column name to the name of the state variable.

  
**Include node/element ids** : Adds a column to the imported data which contains the node/element ids.

  
**Data handling** : This is the same as for importing text files (see Fig. 57.3.2.)

![]({{ '/assets/images/data_analytics/57_3_deform_data_analytics_data_import_and_export/57_3_image0002.jpg' | relative_url }})

Defining the DEFORM database import options

## Importing a DEFORM DOE database

Data collected from a DEFORM DOE (Design Of Experiments) simulation can be imported into DEFORM Data Analytics by importing the DOE SDB file.

  
The data in an SDB file is a collection of tables which relate to the DOE extraction options in MO.Once a DEFORM Data Analytics project has been created, select a data table and click on ![]({{ '/assets/icons/post_icons/mo_import_icon.jpg' | relative_url }}) button to import a SDB file.

Once a file is opened, an interface will be opened as shown in Fig. 57.3.3. After selecting an SDB table, the preview table will be filled with data from that table.

  
To import data from multiple SDB tables, the import will need to be repeated for each SDB table.

The interface consists of the following options:

**SDB Table** : The table in the SDB file to import the data from.

**Source Data** : This is the same as for importing text files (see Fig. 57.3.1.)

**Use column Names from Table** : Import the column names from the SDB table.

  
I **mport Input columns** : Import the DOE variable values which were varied during the DOE simulations.

**Data handling** : This is the same as for importing text files (see Fig. 57.3.3.)

![]({{ '/assets/images/data_analytics/57_3_deform_data_analytics_data_import_and_export/57_3_image0003.jpg' | relative_url }})

Defining the DEFORM DOE database import options

## Importing multiple DEFORM simulation databases

State variable data can be imported from multiple deform simulation databases by clicking the ![]({{ '/assets/icons/pre_icons/mo_import_multiple_dbs_icon.jpg' | relative_url }}) button in the toolbar. The data from each DB will be imported into a row of the data analytics table. Each variable will be imported into a column. Only the minimum/maximum values of a state variable are imported.

  1. Importing data from multiple DBs is a multi-step process. These steps include:

  2. Select DB files to import

  3. Select operation (step) to import data from

  4. Select Data to import

  5. Assign data to Data Analytics table columns

  
These steps are shown in the step list of the import interface. Fig. 57.3.4. – Fig. 57.3.10. show this import process.

![]({{ '/assets/images/data_analytics/57_3_deform_data_analytics_data_import_and_export/57_3_image0004.jpg' | relative_url }})

Import multiple DBs user interface

![]({{ '/assets/images/data_analytics/57_3_deform_data_analytics_data_import_and_export/57_3_image0005.jpg' | relative_url }})

Adding DEFORM database files 1

![]({{ '/assets/images/data_analytics/57_3_deform_data_analytics_data_import_and_export/57_3_image0006.jpg' | relative_url }})

Adding DEFORM database files 2

![]({{ '/assets/images/data_analytics/57_3_deform_data_analytics_data_import_and_export/57_3_image0007.jpg' | relative_url }})

Ordering files

![]({{ '/assets/images/data_analytics/57_3_deform_data_analytics_data_import_and_export/57_3_image0008.jpg' | relative_url }})

Select the operation or end of simulation

![]({{ '/assets/images/data_analytics/57_3_deform_data_analytics_data_import_and_export/57_3_image0009.jpg' | relative_url }})

Define state variables to import

![]({{ '/assets/images/data_analytics/57_3_deform_data_analytics_data_import_and_export/57_3_image0010.jpg' | relative_url }})

Map imported data to the data table

## Data export

Data can be exported from a data table to a csv (or txt (text)) file. In the exported text file, each row is a separate line and each column is separated by a delimiting character selected in the dialog shown in Fig. 57.3.1.

  
Data is exported by selecting **Export…** from the file menu (see Fig. 57.3.11.), specifying a file name in the standard file selection dialog, then selecting a delimiter (see Fig. 57.3.12.).

![]({{ '/assets/images/data_analytics/57_3_deform_data_analytics_data_import_and_export/57_3_image0011.jpg' | relative_url }})

Exporting data

![]({{ '/assets/images/data_analytics/57_3_deform_data_analytics_data_import_and_export/57_3_image0012.jpg' | relative_url }})

Export options
