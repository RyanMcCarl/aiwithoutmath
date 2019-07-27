# The machine learning process

We can provide a holistic view, that generally explains ML. Then connect specific topics to that holistic view.

All AI methods/processes look like the following:

1.	Formalize the function you want to learn. This involves defining the inputs and outputs.
e.g., predictor where input observations and output prediction about temperature in 10 days
e.g., policy where input observations and outputs an action (or distribution over actions)

2.	Define the data representation
e.g., embeddings of text, into Euclidean space
e.g., transformation of inputs to Fourier basis (I know this is too technical, so need to make this a layman description)

3.	Define the algorithms (or even more simply the loss) to learn that function
e.g., imputation losses (matrix completion)
e.g., squared error for regression

4.	Specify the training scenario
offline batch of data
continual stream of data

5.	Evaluation of models

The failings of each method can be identified by considering failings in each of these steps.
