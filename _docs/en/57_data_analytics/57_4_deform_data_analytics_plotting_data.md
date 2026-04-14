---
lang: en
title: "57.4. DEFORM Data Analytics Plotting Data"
---

# 57.4. DEFORM Data Analytics Plotting Data

57.4.1. Plotting overview

57.4.2. Scatter plot

57.4.3. Line plot

57.4.4. Bar plot

57.4.5. Histogram plot

57.4.6. Tornado plot

57.4.7. Sensitivity plot

57.4.8. 3d response surface plot

57.4.9. Contour response surface plot

## Plotting overview

Plots can be used to visualize data and determine if a relationship exists between columns of data in a data table. Plots can also be used to visually compare data, and check if a trained model correctly models the data. Multiple pots can be shown in the work area at the same time.

DEFORM Data Analytics offers the following several plot types. These include scatter plot, line plot, bar plot, tornado plot, sensitivity plot, histogram plot and 3d and contour response surface plots.

All plots can be saved to image files in the Portable Network Graphics (PNG) format. There are options for specifying the image size as shown in Fig. 57.4.1.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0001.jpg' | relative_url }})

Plot image export options

## Scatter plot ![]({{ '/assets/icons/post_icons/doe_post_scatter_plot_button.jpg' | relative_url }})

Scatter plots show pairs of data as points on a 2d graph. This can be useful for visually determining if a pair of data is dependent or independent. Independent data will display as a random cloud of points. Dependent data will closely follow a line or curve. Real world data is rarely 100% dependent. There is usually noise or measurement uncertainty in the data. So, dependent/independent is not binary, there is a continuum between to two. Fig. 57.4.2. show this.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0002.jpg' | relative_url }})

Data Dependence

  
Visually inspecting data on a scatter plot can also provide clues as to that the relationship between pairs of data is (i.e., linear, exponential, quadratic, etc). ( See Fig. 57.4.3.)

  
![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0003.jpg' | relative_url }})

Examples of data relationships

  
The data to be plotted and several plot options are available in the properties area when the plot is the active window. Data is selected in the data tab of the plot properties. The first column of the Y-Axis list specifies the column to plot on the Y-axis. The second column specifies the column to determine the point locations on the X-axis. The label for the X-axis is specified in the X-Axis label field. The name of an existing column can be used (from the drop down menu) or any text can be typed in for the label. Fig. 57.4.4. shows plotting a single pair of columns. Fig. 57.4.5. shows plotting 2 pairs of columns.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0004.jpg' | relative_url }})

Selecting data for scatter plot

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0005.jpg' | relative_url }})

Comparing data in a scatter plot

  
The data on a scatter plot can be plotted on a linear scale or logarithmic scale as shown in Fig. 57.4.6.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0009.jpg' | relative_url }})

Plotting with a logarithmic scale

  
A line of best fit can also be shown on a scatter plot as shown in Fig. 57.4.7.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0010.jpg' | relative_url }})

Line of best fit option

DEFORM Data Analytics offers several display options for scatter plots. These include point color, point shape, point size, line (of best fit) color, line style, and line thickness as shown in Fig. 57.4.9.). To set these options, select a Y-axis variable from the Y-axis drop down menu. Any display options changes will be applied to the display that data (see Fig. 57.4.8.). Fig. 57.4.10. shows data from multiple columns displayed with different display options.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0011.jpg' | relative_url }})

Selecting column data for display change  

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0012.jpg' | relative_url }})

Display options

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0013.jpg' | relative_url }})

Data from multiple column with different display options

  
If a column of data has error ranges defined, these can be shown in the scatter plot as error bars as shown in Fig. 57.4.11.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0014.jpg' | relative_url }})

Option to display error bars

## Line Plot ![]({{ '/assets/icons/post_icons/data_analytics_curve_plot_button.jpg' | relative_url }})

Line are similar to scatter plots except the points are connected by line segments. Column selection and display options are the same as for the scatter plot (section 57.4.2).

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0012.jpg' | relative_url }})

Selecting data for line plot

  
Once a model has been trained, a line plot can be used to visually determine how well a model fits the training data. If the output column used to train the model has error ranges, error bars can be shown. The line will be drawn from the trained mode. And points will show the positions of the training data. To display this, select a model in the project tree (see Fig. 57.4.13.), the click on the line plot icon. Fig. 57.4.14. shows line plots for a model with 1 input and a model with 3 inputs.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0013.jpg' | relative_url }})

Selecting model for line plot

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0014.jpg' | relative_url }})

Validating a model with a line plot

## Bar plot ![]({{ '/assets/icons/post_icons/data_analytics_bar_chart_button.jpg' | relative_url }})

A bar plot shows the values of each cell in a column as a bar. The length of the bar represents the value of the of a variable. The X-axis is the row number from the data table. Multiple columns can be selected for display. The bars will be shown next to each other in different colors to facilitate visually comparing the data. Fig. 57.4.15. shows a bar plot with 2 columns selected.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0015.jpg' | relative_url }})

Bar plot

## Histogram plot ![]({{ '/assets/icons/post_icons/doe_post_histogram_button.jpg' | relative_url }})

Histogram plots show how often values of a variable occur within a range of values. These ranges are called bins. This plot only shows the histogram for a single column at a time. A histogram can be used as an approximation of the probability that a variable will take a value in a certain range. A bin with a high count indicates that the probability that a random value of the variable is more likely to fall within that bin that into a bin with a low count. The x-axis of a histogram represents the values of the variable (cells in the column). The y-axis represents the count of those values in each bin.The x-axis covers the range of the data in the column. The histogram properties provide selection of the column and the number of bins. As the number of bins increases the size of the range of each bin decreases. Fig. 57.4.16 shows a histogram plot.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0016.jpg' | relative_url }})

Histogram plot

## Tornado plot ![]({{ '/assets/icons/post_icons/doe_post_tornado_chart.jpg' | relative_url }})

A tornado plot shows the relative strengths of dependency (by computing the correlation coefficient) of columns of data to another column of data. The length of the bar shows the strength of the dependency. Longer bars indicate a stronger dependency. Bars to the left of the center line indicate an inverse dependency (as one variable increases in value, the other decreases). The bars of this plot are ordered from strongest dependency to weakest dependency. Fig. 57.4.17 shows a basic tornado plot. Fig. 57.4.18 shows a tornado plot with direct and inverse dependencies. The output column indicates the column that the input columns will be compared with. This is usually the column that will be used as the output for training a model. This can be useful for determining which inputs have the most effect on the output. Weak inputs can usually be excluded from the model.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0017.jpg' | relative_url }})

Tornado plot

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0018.jpg' | relative_url }})

Tornado plot with a mix of direct and inverse dependencies

## Sensitivity plot ![]({{ '/assets/icons/post_icons/doe_post_sensitivity_plot_button.jpg' | relative_url }})

The sensitivity plot is essentially the same as the tornado plot. Instead of representing the strength of the dependency as bars, the sensitivity represents them as slopes of lines. The steeper the slope, the stronger the dependency. Negative slopes indicate an inverse dependency. Fig. 57.4.19. shows a sensitivity plot.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0019.jpg' | relative_url }})

Sensitivity plot

## 3d response surface plot ![]({{ '/assets/icons/post_icons/doe_post_response surface_button.jpg' | relative_url }})

The 3d response surface shows the shape of the surface generated from a trained model of 2 or more inputs. It also shows the positions of the training data so it can be used to visually see how well a model fits the training data. The display types in the tool bar ( ![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }})![]({{ '/assets/icons/pre_icons/mo_wirefrane_mode_icon.jpg' | relative_url }})![]({{ '/assets/icons/pre_icons/mo_shade_wireframe_icon.jpg' | relative_url }})) change the display of the response surface. Fig. 57.4.20. shows a 3d response surface plot.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0020.jpg' | relative_url }})

3d response surface plot

If the model was trained with more than 2 inputs, the X-Axis and Y-Axis drop down menus can be used to select which inputs are used for the axis. Also, the Other input tab will contain sliders which can be used to vary the values of other variables to observe their effect on the response surface (see Fig. 57.4.21.)

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0021.jpg' | relative_url }})

3d response surface plot with more than 2 inputs

If the output column used for training a model includes error ranges, error bars can be shown on the response surface as shown in Fig. 57.4.22.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0022.jpg' | relative_url }})

Error bars on a 3d response surface plot

  
Multiple response surfaces can be shown in a single plot. This can be used to compare the response surfaces of different models or, as shown in Fig. 57.4.23., compare models trained by dropping different input columns with weak dependencies.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0023.jpg' | relative_url }})

Comparing response surfaces

## Contour response surface plot ![]({{ '/assets/icons/post_icons/doe_post_response_contour_button.jpg' | relative_url }})

The 3d response surface shows the shape of the surface generated from a trained model of 2 or more inputs as a contour plot. Only one response surface can be displayed at a time in this plot. Other than that, many of the options for this plot are the same as the 3d response surface plot (section 57.4.8). Fig. 57.4.24. shows a contour response surface plot.

![]({{ '/assets/images/data_analytics/57_4_deform_data_analytics_plotting_data/57_4_image0024.jpg' | relative_url }})

Contour response surface
