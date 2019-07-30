# Naive Bayes classification

A Naive Bayes classifier uses probability to classify (categorize) an object.

## What is a classifier?

A classifier is a program that categorizes items as one type of thing or another. For example, a picture might be classified as a “cat picture” or a “dog picture.” If you feed (input) an image into a classifier designed to distinguish cat pictures from dog pictures, it would calculate the probability that the image shows a cat against the probability that it shows a dog.

## Spam filter example

Email systems include “spam filters” that automatically determine whether each incoming email is likely to be spam. They get an input email and output the probability that the email is spam.

Suppose that 45% of emails are spam and 55% are not. (This is called a base rate). If we know that an email arrived but we do not know anything else about it, we should conclude that it is probably not spam. Each time we estimate the probability that a particular email is spam, we should take into consideration the overall probability that an email is spam (45%).

However, each incoming email may have certain features that make it more likely to be spam. For example, every email has a certain number of exclamation points; “number of explanation points” is a feature. We could say that an email containing more than two exclamation points is 80% likely to be spam. We can keep identifying more features and comparing them across the emails we see.

After considering many emails, we will know that some features have certain values for spam emails and other values for non-spam emails. We can then compare the feature values of any new email to these two sets of values and estimate whether the new email is spam or not. 
 
## What makes Naive Bayes different from other classification methods?

In the Naive Bayes algorithm, each feature is considered independently of the others. This _simplifying assumption_ is why the algorithm is called “naive.” In reality, many variables “travel together” and are not independent. For example, if the weather is rainy, it is probably also cloudy. But in a Naive Bayes analysis, “raininess” and “cloudiness” might be treated as two separate and independent features.

# Related resources

_Available articles_

- classifier
- 

_Contributors needed_

- Bayes Theorem
- machine learning