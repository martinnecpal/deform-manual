---
lang: en
title: "57.6. DEFORM Data Analytics Data Modeling"
---

# 57.6. DEFORM Data Analytics Data Modeling

57.6.1. Data modeling overview

57.6.2. Linear model

57.6.3. Quadratic model

57.6.4. Cubic model

57.6.5. Gaussian model

57.6.6. Neural network model

57.6.7. Deep neural network model

57.6.8. Equation fit model

57.6.9. Piecewise Linear model

57.6.10. Validating a model

57.6.11. Expressions are used to calculate new values from a trained model

## Data modeling overview

Models establish relationships between columns of data in a data table. Models are defined (trained) by providing a model type and training data. The Training data consists of one or more inputs and one output from other columns in the data table. Once a model has been trained, it can be used to calculate (predict) output values for new input values. Fig. 57.6.1. and Fig. 57.6.2. illustrate this process.

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0001.jpg' | relative_url }})

Training a model

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0002.jpg' | relative_url }})

Making predictions from a trained model

  
DEFORM Data Analytics supports the following model types:

**Linear** : Fits a straight line/plane to the data

**Quadratic** : Fits a 2nd order polynomial to the data

**Cubic** : Fits a 3rd order polynomial to the data

**Gaussian** : Fits the data to a gaussian process

**Neural Network** : Uses a neural network to fit the data

**Deep Neural Network (DNN):** Uses a neural network to fit the data

**Equation****Fit** : Fits the data to a used provided equation

**Piecewise****Linear** : Connects the dots (data points) with straight lines

The model type and input/output columns are selected from the property page for the model column as shown in Fig. 57.6.3. The list on this property page contains the other columns in the data table. The 3 columns in this list labeled I (input), O (output), and N (not used) are for selecting the input and output columns to be used to train the data. The type menu selects the model type. Once the inputs, the output and the model type are selected, the train button can be clicked to train the model. Once the model is trained, the cells under this column will be filled with values computed by the model for the input columns.

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0003.jpg' | relative_url }})

Making predictions from a trained model

  
Model training works best if the inputs are independent. Many of the training algorithms rely on matrix inversion and dependent variables can result in matrices that cannot be inverted. So, the training will likely fail or the results may not be the best. If a pair of inputs are dependent, try using only one of them. See scatter plot [section 57.4.2](57_4_deform_data_analytics_plotting_data.htm#57_4_2_Scatter_plot) for a discussion of dependent and independent variables.

## Linear model

Linear models use a simple line equation (for 1 input).

  
_y = Ax+B_

  
Additional inputs add additional terms to the equation.

  
i.e. 3 inputs:  _y = Ax 1+Bx2+Cx3+D_

  
Use a linear model when the data appears to follow a line

  
Linear models can be useful approximations when there are very few data points. Only 2 points are needed to define a line. The minimum number of points for a solution is 1+number of inputs

  
The linear model is not guaranteed to pass through all data points

## Quadratic model

Quadratic models use a 2nd order polynomial equation (for 1 input).

  
_y = Ax 2+Bx+C_

  
Additional inputs add additional terms to the equation.

  
Use a linear model when the data appears to follow a parabola.

  
Quadratic models can be useful approximations when there are very few data points. Only 3 points are needed to define a parabola. The minimum number of points for a solution is 1+2*number of inputs.

  
The quadratic model is not guaranteed to pass through all data points.

## Cubic model

Cubic models use a 3rd order polynomial equation (for 1 input).

  
_y = Ax 3+Bx2+Cx+D_

  
Additional inputs add additional terms to the equation.

  
Use a cubic model when the data appears to follow a more of an ~ shape.

  
The minimum number of points for a solution is 1+4*number of inputs

  
The cubic model is not guaranteed to pass through all data points

## Gaussian model

Gaussian models do not use a simple equation. It is more of a statistical algorithm with parameters.

  
Gaussian models can be used for any shape of the data.

  
Gaussian models can be useful approximations when there are a small number of data points.

  
The minimum number of points for a solution is 2*number of inputs. For a good approximation, 10*number of inputs is recommended

  
Training of the gaussian model will fail if duplicate input points are contained in the data (this causes a divide by 0 in the algorithm since distances between inputs are used in the training of this model).

  
The gaussian model is guaranteed to pass through all data points.

## Neural network model

Neural network models do not use a simple equation. It is more of an algorithm with parameters. A neural network is a computing model whose layered structure resembles the networked structure of neurons in the brain. In general a neural network consists of 3 or more layers of nodes. All nodes are connected to all nodes of the previous layer. This neural network mode has only 3 layers; an input layer, an output, layer and 1 hidden layer (see Fig. 57.6.4.).

  
Neural network models can be used for any shape of the data.

  
Neural network models work best when there are large amounts of data.

  
Training time for a neural network model can be long.

  
The neural network model is not guaranteed to pass through all data points.

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0004.jpg' | relative_url }})

Diagram of a neural network model

## Deep neural network model

Deep neural network (DNN) models do not use a simple equation. It is more of an algorithm with parameters. A neural network is a computing model whose layered structure resembles the networked structure of neurons in the brain. This neural network model allows for a user specified number of hidden layers in addition to the input and output layers. The number of nodes on the hidden layers can also be specified. Thus, the network can become deep as shown in Fig. 57.6.5.

  
Deep neural network models can be used for any shape of the data.

  
Deep neural network models work best when there are large amounts of data.

  
Training time for a deep neural network model can be long.

  
The deep neural network model is not guaranteed to pass through all data points.

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0005.jpg' | relative_url }})

Diagram of a deep neural network model

  
In Fig. 57.6.6., a list of models structures for DNN can be seen in User parameters section. There are four system-defined models, and 6 custom models that users can define number of nodes and layers. By clicking on “Custom” in the “Layers and Nodes” display, custom number of nodes and layers can be defined in the “Data” section. Clicking on apply will finalize the combination and show the custom model in the “Layers and Nodes” display. In the “Advanced” tab shown in Figure 2, users can further control in depth model parameters of deep neural network. There are four controllable factors which are number of iterations and training, error functions and error criteria. Number of iterations determines how many times the model is going to propagate towards the minima. Default value is set to 100. Setting this value too low would not give an accurate result, whereas setting it too high may take excessive time with very little or no improvement of the model. 

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0006.jpg' | relative_url }})

Deep neural network model user interface

  
After model parameters are defined, “Train” button in the left bottom corner of the interface can be clicked to initiate the training process. A progress bar will be shown in Fig. 57.6.7. to display the training process.

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0007.jpg' | relative_url }})

Deep neural network progress

After the training is finished, selected models should display the error representing the accuracy of the model. By clicking on those models, evaluated values are shown in the “Define model” column to compare the values with the reference training data (see Fig. 57.6.8.). 

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0008.jpg' | relative_url }})

Deep neural network completed training

## Equation fit model

Equation fit models use a user provided equation. The training of this model involves determining the parameters of the equation that best fir the data. The solution is not guaranteed to be unique.

  
Parameters of the equation are computed using a simplex search optimization algorithm. Using different search ranges could give different values for the parameters.

  
Equation fit models can be used for any shape that’s appropriate for the given equation.

  
The amount of data needed to solve the equation depends on the number of parameters in the equation. Generally count on needing at least 2 data points per parameter. More is better.

  
The equation fit model is not guaranteed to pass through all data points.

  
Fig. 57.6.9 shows the user interface for training an equation fit model. After selecting the inputs, the output and entering the equation, clicking the parse button will fill the parameters list with the equation parameters. When entering the equation, use the input column (variable) names as variables for the equation. Recursive equations are not supported, so the output column name should not be used in the equation. Any text that is not an input column name or an math symbol/function, will be considered a parameter.

  
The parameters that best fit the data are determined by a searching algorithm. Errors are computed at the end of each search step. The search ends when the error falls below a threshold. Since this is a search algorithm, a search range needs to be specified. Although, the default search range is +/- infinity, this is actually just a very big number. The smaller the search range, the better chance the algorithm has of converging on a correct solution. Once the search ranges are entered, the model is ready for training.

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0009.jpg' | relative_url }})

Equation fit model user interface

## Piecewise Linear model

Piecewise linear connects each data point with a straight line. This can be useful for doing linear interpolations between data points.

  
Piecewise linear models can be used for any shape of the data.

  
A minimum of 2 data points is needed for a solution.

  
The piecewise linear model is guaranteed to pass through all data points.

Fig. 57.6.10. and Fig. 57.6.11. show how some of these models represent some noisy data. Note that the Gaussian and piecewise linear models tend to over fit the data.

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0010.jpg' | relative_url }})

Examples of models with noisy data

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0011.jpg' | relative_url }})

Example of piecewise linear model with noisy data

## Validating a model

Once a model is trained, the model column in the data table is filled with values computed by the model using the trained model. These values can be used to determine how well the model fits the data. If the model perfectly models the data, the values in this column will exactly match the data in the column designated as output for training. Using real world data, it is unlikely that the data will match exactly (unless using one of the model types that pass through all data points such as gaussian and piecewise linear models). So, a simple comparison of the values can determine how well the model fits the data. Fig. 57.6.12. shows a bar graph with the output and model columns. Fig. 57.6.13. shows using a scatter plot to visualize the fit. In this plot, the x axis is the output column and the y axis is the model column. For a perfect fit, this would result in a 45 degree line. How close the points are to a 45 degree line indicates how well the model fits the data.

  
If a large amount of data is available, training could be performed using a subset of the data (i.e. 90% of the data). The remaining data could be copied to new columns and used to predict. The results of the prediction could be compared with the output values from the original data.

  
To get a quantitative value for the goodness of the fit, statistics of the fit are printed in the message area at the completion of training. The message area at the completion of training contains something like the following:

  
Temperature=-7.19e-06*Altitude^2+0.042*Altitude+0.767478 

Temperature:

Maximum Error = 0.514677

Average Error = 0.054183 Error Variance = 0.00371164

Average Absolute Error = 0.054183

RMS Error = 0.0815318

Correlation = 0.996908 R^2 = 0.993783

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0012.jpg' | relative_url }})

Bar plot comparing training output values with predicted output values

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0013.jpg' | relative_url }})

Scatter plot plotting training output values against predicted output values

An expression can also be used to compute difference (error) between the model column and the output column. Any comparison function could be used (i.e. simple subtraction, absolute value of difference, RMS error, etc.). Column statistics for this column could then provide average, minimum, maximum, etc. values for the errors. Fig. 57.6.14. shows an absolute value of difference plotted against the original output value. This gives an visual representation of the magnitude of the errors relative to the data values.

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0014.jpg' | relative_url }})

Line plot plotting error values along with original (training) data

## Expressions are used to calculate new values from a trained model

After a model has been trained, enter the inputs for which the output values are not known into new columns. Create another new column for the expression (set the usage to expression). The model/Expressions menu can be used to select the model to use. Add the new inputs inside the parenthesis for the model in the expression. Click apply. The cells of this column will be filled with the computed values. Fig. 57.6.15. – Fig. 57.6.17. show this procedure.

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0015.jpg' | relative_url }})

Choosing the model for the expression

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0016.jpg' | relative_url }})

Choosing new inputs for the expression

![]({{ '/assets/images/data_analytics/57_6_deform_data_analytics_data_modeling/57_6_image0017.jpg' | relative_url }})

Evaluating the expression
