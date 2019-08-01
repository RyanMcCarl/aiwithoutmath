# Clustering

If we have a group of people that we do not really know and we are trying to learn more about them, one of the ways to do this would be to put them into groups based on things they have in common, for example we can have a group of people who are living in the city of Edmonton, and another group for people living outside this city. But what if we do not know which are the things they have in common?

Well, we then need to divide them based on how many things they have in common with one of them.

Say we want to have three groups at the end, so we pick three people, and start to compare the others to them:

1. Noura: lives in Canada, works at a hospital.
2. Adam: lives in  Canada, works at a school.
3. Anne: lives in the United States, works at a university.

Then we picked one other person who lives in Germany and works at a hospital, so we can put her in the group of Noura because they have more in common she does with Adam or Anne, and so on until we have all people in groups.

Now we discover that the group of Noura is now as follows: most of the people live in Germany and work at a hospital, so maybe the person representing this group  is not really Noura, because she lives in Canada, and thus most of the people have only the place of work in common with her, but not the country. So we pick another person, who lives in Germany and works at a hospital to be the new representer of the group and now we have the following groups:

1 - Manfred: lives in Germany, works at a hospital.
2 - Adam: lives in  Canada, works at a school.
3 - Anne: lives in the United States, works at a university.

And then we go again and reassign all the people to the groups, because now that we have changed the person representing the first group, they might be people who live in Germany who were previously assigned to other groups.

We repeat this operation until we have reasonable groups.

Dividing people into groups based on things they have in common is called Clustering, because we are dividing things/people into different clusters/groups, and this way of clustering is called K-Means algorithm, because we decide first the number of groups we need, which is K, and then we try to find  the element that represents this group in the best way, which is the mean.
