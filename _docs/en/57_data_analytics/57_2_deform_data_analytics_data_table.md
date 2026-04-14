---
lang: en
title: "57.2. DEFORM Data Analytics Data Table"
---

# 57.2. DEFORM Data Analytics Data Table

57.2.1. Data table overview

57.2.2. Column/variable properties

57.2.3. Entering data 

57.2.4. Adding/removing tables

57.2.5. Adding/removing columns 

57.2.6. Adding/removing rows

57.2.7. Hide/Show columns

57.2.8. Excluding rows

57.2.9. Column statistics

## Data table overview

The data table is where data is entered and modeled within DEFORM Data Analytics. The data table is organized as rows and columns of values. The columns represent variables and the rows represent samples (individual values of a variable).

The data table consists of 2 sections as shown in Fig. 57.2.1. These are the data section and the variable definition area.

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0001.jpg' | relative_url }})

Data table

## Column/variable properties

At the top of the data table is the variable definition section. This contains 3 rows which are 3 column properties required to define the data within a column. These 3 properties are column/variable name, usage and data type.

  
The name is the name of the variable. This will be used later to define models and supply inputs to expressions.

  
The usage defines how the data us created or used. It can be one of these types:

**Data** : The data is entered by the user and is used to train models or as inputs to expressions.

**Model definition** : This is a column that is used to create, define and train a model. The values in this column will be computed from the trained model.

**Expression** : This is a column the defines and evaluated an expression. The values in this column are computed from a user defined equation.

The data type specified the type of data stored in the column. It can be one of 3 types:

**Number** : This specifies a numeric value.

**Text** : This specifies a text string value. They are typically used to apply meaningful label to rows of data. These columns cannot be used to train models or as inputs to expressions.

**Function** : This specifies that the values in the column are not single values. Function data is composed of inputs, one output and a model.

Additional column properties can be set within the properties area for the selected column (see Fig. 57.2.2.). A column can be selected by clicking on a cell within the column, clicking on the column header, or clicking the column name in the project tree. These properties include:

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0002.jpg' | relative_url }})

Additional column properties

  
**Description** : This is an optional textual description of the column data. 

The following properties apply only to the number data type:

**Expected range** : This optionally specifies the minimum and maximum expected values of the column data.

**Format** : This controls the display of the data. This can either be Normal or Exponent. 

**Precision** : This specifies the number of digits to the right of the decimal point. Fig. 57.2.3. shows that format and precision options.

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0003.jpg' | relative_url }})

Additional column properties

Table 57.2.1 shows the effect of the precision and format options on the value 253.824:

|  Format  
---|---  
Precision |  Normal |  Exponent |  Best  
0 |  254 |  3e+02 |  254  
1 |  253.8 |  2.5e+02 |  253.8  
2 |  253.82 |  2.54e+02 |  253.52  
3 |  253.824 |  2.538e+02 |  253.524  
4 |  253.8240 |  2.5382e+02 |  253.5240  
  
Data formatting

**Units** : This specifies the units of the data. The units will be shown in the data table column header under the column name and in parenthesis as shown in Fig. 57.2.4.

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0004.jpg' | relative_url }})

Units display in column headers

  
**Error ranges** : Some data is provided with a range. This is to reflect tolerances, or measurement error, or some other uncertainty with the data. Checking Use error bounds will create additional columns under a variable for this data (see Fig. 57.2.5.). There are several ways these errors can be represented:

  
+/- a fixed value

+/- a percentage

Standard Deviation

Variance

Multiple of the Standard Deviation (i.e. 3 times the Standard Deviation is referred to as 3 sigma (3σ))

Upper and Lower value  

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0005.jpg' | relative_url }})

Error ranges

There are also other properties that are dependent on the usage.

## Entering data

Data can be entered into the data table by clicking on a cell and typing. The return key will complete the edit and move to the next cell in the column.

  
**Copy/paste**

Copying data is performed by selecting one or more contiguous cells in the table and either selecting Copy from right click menu or using ctrl-c key shortcut. Pasting data is performed by selecting a cell as the location of the first item in the table and either selecting Paste from right click menu or using ctrl-v key shortcut. New rows and columns will be added as needed.

  
Data can be copied from one location in a table and pasted into another location

  
Data can be copied from one table to another

  
Data can be copied from other applications (like a spread sheet) and pasted into a Data Analytics table. Data can be copied from a Data analytics table and pasted into other applications (like a spread sheet).

  
Data can be copied from a text editor as long as the data is organized in rows and columns with each row separated by a new line and each column separated by a single tab character. Data can be pasted into a text editor. The pasted data will be organized in rows and columns with each row separated by a new line and each column separated by a single tab character. Fig. 57.2.6. and Fig. 57.2.7 show the copy and paste context menus

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0006.jpg' | relative_url }})

Copy

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0007.jpg' | relative_url }})

Paste

## Adding/removing tables

A single DEFORM Data Analytics project can contain multiple data tables. Tables can be added or removed from the project tree or from the tab bar under the table view.

To add a data table from the project tree, click on the project icon (with the project name). An Add analytics table button will appear at the bottom of the tree. Click this ![]({{ '/assets/icons/post_icons/data_analytics_add_analytics_table_button.jpg' | relative_url }}) button to add a table. To remove a table from the project tree, select the table in the tree. A Delete analytics table will appear at the bottom of the tree. Click this ![]({{ '/assets/icons/post_icons/data_analytics_delete_analytics_table_button.jpg' | relative_url }}) button to delete the selected table. See Fig. 57.2.8. and Fig. 57.2.9

To Add a data table from the tab bar, press the blue ![]({{ '/assets/icons/post_icons/data_analytics_add_table_icon.jpg' | relative_url }}) button on the tab bar. To remove a table from the tab bar, select the table to delete, then click the orange ![]({{ '/assets/icons/post_icons/data_analytics_delete_table_icon.jpg' | relative_url }}) button. See Fig. 57.2.10.

  
Tables can also be renamed. Each table has a name and description which can be edited by selecting the table (either from the project tree or the tab bar). The property area will show the name and description fields for the table. See Fig. 57.2.11.

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0008.jpg' | relative_url }})

Add table from project tree

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0009.jpg' | relative_url }})

Remove table from project tree

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0010.jpg' | relative_url }})

Add and remove tables from tab bar

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0011.jpg' | relative_url }})

Table properties

## Adding/removing columns

Generally columns will not need to be added to a data table. There will always be at least one extra column to enter data into. To remove a column, right click on the column header and select Remove column (see Fig. 57.2.12.).

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0012.jpg' | relative_url }})

Removing a column

## Adding/removing rows

Generally rows will not need to be added to a data table. There will always be at least one extra row to enter data into. To remove a row, right click on the row header and select Remove row (see Fig. 57.2.13.).

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0013.jpg' | relative_url }})

Removing a column

## Hide/Show columns

To compact the data table, columns can be hidden and later reshown. This is done using the check box under the ![]({{ '/assets/icons/pre_icons/mo_visible.jpg' | relative_url }}) icon in the project tree (see Fig. 57.2.14.).

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0014.jpg' | relative_url }})

Show/hide columns

## Excluding rows

Rows with missing data are not used in training a model (if the column with the missing data is defined as an input or output of the model). Other rows can be marked to exclude from training (see Fig. 57.2.15.). This could be to exclude outliers.

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0015.jpg' | relative_url }})

Excluding/including rows

## Column statistics

To obtain statistics from a column of data, hover the mouse over the column header. The statistics will appear as a tool tip (see Fig. 57.2.16.). Using the right click context menu on the column header, the statistics can be printed to the message area (see Fig. 57.2.17.) where they can be copied and pasted into another document. The statistics include:

Average

Median

Standard Deviation

InterQuartile Range (IQR)

Minimum

Maximum

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0016.jpg' | relative_url }})

Column statistics as a tool tip

![]({{ '/assets/images/data_analytics/57_2_deform_data_analytics_data_table/57_2_image0017.jpg' | relative_url }})

Column statistics printed to message area
