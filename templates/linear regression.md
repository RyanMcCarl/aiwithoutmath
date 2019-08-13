# Linear Regression

## What is linear regression?

Linear Regression is a way of predicting an output variable (“Y”) based on one or more input variables (“Xs”). For example, a linear regression system might attempt to predict house prices (an output variable) based on input variables such as number of rooms, school district, and proximity to the ocean.

Input variables (Xs) are also called explanatory variables because they attempt to “explain” the reasons for the output variable. In the housing prices example, the input variables “explain” why each house is sold at a certain price.

## When should you use linear regression?

Linear regression should be used when (1) your target output variable is a numerical value, and (2) you can predict a linear relationship between the input variables and the output variable. A linear relationship means that if the input variable (e.g., number of rooms) goes up, the output variable (e.g., housing price) should go up as well.

## How does linear regression work?

A linear regression model works by fitting a line (when there is one input variable) or a plane (when there are two or more input variables). “Fitting” means that the system predicts the line or plane which best explains the output variable.

The image below shows a linear regression model with a line fit between one input variable (X) and one output variable (Y). The x-axis shows the value of a single input variable (such as a neighborhood’s safety rating); the dots show the value of different output variables (such as house prices). The linear regression model determines the fit between these variables by finding a line which minimizes the distance between the line and the data points.

![Figure 1.a) Predicting Y using one input variable X results in a linear model (Image source:Wikipedia.org)](../static/img/lr_x.png)

## What are some of the business use cases for regression?

- Given past prices and economic indicators, should we expect copper prices to rise or fall?
- How might sales change if, instead of investing $100k in TV advertising, $50K is invested in TV advertising, and $50K is invested in social media advertising?
- If we hire additional doctors, how much can we decrease patient wait time?
- What are the top five factors that can cause a customer to default on their loan payment?

## Related resources

- <li><a href="{{ url_for('dynamicpath', page='mlprocess') }}">Machine learning process</a></li>
