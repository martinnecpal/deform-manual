---
lang: en
title: "1.8. Creating Input data"
---

# 1.8. Creating Input data

There are several ways to enter data into the DEFORM [Pre-Processor](/docs/en/pre_processor/7_introduction_to_pre-processor/). Depending on the requirements of a particular problem, a combination of the following methods will frequently be used.

**Manual input**

The [pre-processor](/docs/en/pre_processor/7_introduction_to_pre-processor/) menus contain input fields for nearly every possible data input in DEFORM. The user can enter, view, or edit any of these values. Discussions of each field are contained in the reference section of this manual.

**Keyword file input**

Most of the data fields in the DEFORM pre-processor correspond directly to a DEFORM keyword. Individual keywords describe very specific information about a particular object characteristic, [simulation control](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/), [material characteristic](/docs/en/pre_processor/10_material_data/10_material_data/), or [inter object](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) relationship. Keyword data can be saved in a keyword (.KEY) file. A keyword file is a human readable (ASCII) representation of DEFORM simulation data.

The typical format of a keyword is: 

[Keyword name] [Keyword parameters] [Default data]

[Data]

[Data]...

A keyword file may contain a complete simulation data set, or it may contain only one or a few specific keywords.

**Assembling keyword files**

When a keyword file is read into the pre-processor, only the specific data fields listed in that keyword are changed; the remainder is unchanged. Thus, it is possible to assemble a complete set of problem data by loading one keyword file that contains only data for one object, another keyword file that contains material data, etc.

To save specific elements of a keyword file, it is necessary to save the entire file, then use a text editor such as Notepad, VI, Emacs, or equivalent to delete unwanted information. The keyword file load and save features on the main pre-processor menu load or save an entire data set. To load partial keyword files, use Import or Import keyword option from the [File menu.](../../pre_processor/8_pre_processor_layout/8_pre-processor_layout.htm#8.1.1._File_Menu)

**Other file inputs**

Various data types, particularly part[ geometries](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/) and [material data](/docs/en/pre_processor/10_material_data/10_material_data/) can be read from appropriate format files.

**Modifying problem data**

Solution or input step data from any stored step in a database file can be read into the pre-processor, modified, and either appended to an existing database, or written to a new database file.

**Viewing specific problem data**

Most problem data stored in the database file is accessible in the [post-processor](/docs/en/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/). However, certain specific information such as[ boundary conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/) or [inter-object contact](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) conditions is displayed differently in the [pre-processor](/docs/en/pre_processor/7_introduction_to_pre-processor/). When debugging a problem which is not running properly, it is sometimes useful to use the pre processor data display to view this information.

**Related Topics:**

[Pre-Processor](/docs/en/pre_processor/7_introduction_to_pre-processor/)

[Keyword Documentation](/docs/en/keyword_documentation/deform_keywords_list/)

[Database Generation](/docs/en/pre_processor/21_database_generation/21_database_generation/)

[Post-processor](/docs/en/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)
