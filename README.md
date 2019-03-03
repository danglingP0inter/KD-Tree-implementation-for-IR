# KD-Tree-implementation-for-IR

KNN  search has O(N) time complexity for each query where N= Number of data points. 
For KNN with K neighbor search, the time complexity will be O(log(K)*N) only if we maintain a priority queue to return the closest K observations. 
So, for a dataset with millions of rows and thousands of queries, KNN is computationally very demanding.

KD Tree is an algorithm which uses a mixture of Decision trees and KNN to calculate the nearest neighbour(s). 
KD-trees are a specific data structure for efficiently representing our data. 
In particular, KD-trees helps organize and partition the data points based on specific conditions. More about KD trees is available here

https://en.wikipedia.org/wiki/K-d_tree

and here

https://www.analyticsvidhya.com/blog/2017/11/information-retrieval-using-kdtree/

For the implementation of KD Tree, we will use the most common form of IR i.e. Document Retrieval. Based on the current document, document retrieval returns the most similar document(s) to the user.

We will use the dataset which consists of articles on famous personalities. We would implement KD Tree to help us retrieve articles most similar to that of the “Barack Obama”.

You can download the dataset in the form of csv from here 

https://drive.google.com/file/d/1quiVJqTHnDzCxFT6xgJqhkNpj48rz-49/view?usp=sharing
