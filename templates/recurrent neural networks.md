# Recurrent Neural Networks

Sometimes the data we have is connected to each other; suppose we have a sentence, and we want to be able to predict the next word given the current word, for example:

_I met Mum in the living room_

If I read the word ‘I’, we would know that the next word would probably be a verb, and then if we know ‘met’ we would expect the next word to be a noun. Now if we got the word ‘Mum’, we might be confused!

if we did not know the first part of the sentence ‘I met, we might predict the sentence to be ‘Mum is’ doing something, which is not what we want! 

However, if we know the first part as well, so we have ‘I met mum’, we would know that the next word can not be ‘is‘, so we have a different set of options.

Using previous information, and not only the current one, is what a Recurrent Neural Network does.


***Training recurrent neural networks***

The same way normal neural networks use the difference between what it expected to get and what it predicted to update its values, recurrent neural networks use the same trick, with the only difference being that since we are using previous information as well, we need to send the difference back in time to update previous values as well, this is called _Backpropagation Through Time (BPTT)_.
