# The Basics of Neural Networks

***Definition and motivation***

Consider the problem of identifying handwritten digits automatically. The typical approach of programming explicit rules in a computer is infeasible due to the sheer variety of handwriting styles, fonts, and capturing devices characteristics. A more promising approach is to use machine learning, which works by letting the computer automatically learn discriminating rules based on “features”. For instance, given features like number of loops, number of corners, the orientation of corners, etc, it can learn to associate that a digit with two loops is an eight, a digit with one loop and nothing else is a zero and a digit with one loop and a curve at the bottom is a nine. While this might work perfect for some problems like spam classification where features, like count of various words, are easy to calculate in a computer, it might be challenging in case of images. Images are typically captured as an array of numbers representing intensity values of pixels. Even this information is not amenable to be converted to features like loops and corners using a computer program. This is where a neural network comes in the picture which can take raw pixel values as input and automatically learn a hierarchy of discriminating features to classify images automatically. This means that we don’t have to worry about feature engineering anymore. A neural network has a hierarchy of neuron layers, each specializing in solving a particular subtask. The initial layers specialize to solve simpler tasks like identifying edges from the background. The later layers takes the edge information as input and learn to identify more abstract concepts like number of  loops, corners, etc. These concepts are taken as features and   finally used for solving the main problem. There is growing evidence that this is precisely how a human mind works to identify images.

***Training***

Now how do we get this neural network to learn?

Put simply: If you are thinking about a number (x), that you want to multiply by 2 to get 8, so:

`2 * x = 8`

What would this number be? 

You might try 3, the result will be 2 * 3 = 6, but this is 8 - 6 = 2 less than what you wanted, so you try something larger, say 5: 2 * 5 = 10, but this is 8 - 10 = -2, that is 2 more than what you wanted, so you decrease your guess again to 4: 2 * 4 = 8, which is what you were looking for!

So you used the difference between what you were looking for and the result you got to go back and update the number you were looking for, this is called **backpropagation**. Neural networks use this way to find the best values based on the data we already have an answer for, as in the example in which we knew that the result should be 8, then these values could be used on new data: if we use 3 * x = 3 * 4 = 12.

If we had many more data to learn from, say:

`2 * x = 8`

`3 * x = 12`

`4 * x = 16`

Then we used all these examples to learn that the ‘x’ that we are looking for is actually 4, this is called Batch Learning, because we used all the data together. On the other hand, if we used one example at a time, this is called Online Learning, so we are updating our guess on the go.

Why would we use online learning and not just simply use all the data at once?

Because we do not always have all the data! If we are receiving more data with time we might want to use them as they arrive.

***Applications***

Neural networks are widely used today. For example, they are used to classify medical images or to predict weather conditions.
