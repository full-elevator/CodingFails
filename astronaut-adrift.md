# astronaut-adrift.py

One of the earliest projects, this file has the most concentrated noobiness.

## Code crimes

 - Inconsistent styling.
There are too many spaces. I no longer add spaces around keyword arguments in function calls.
On the other hand, the def blocks are not separated by newlines, making it difficult to read the code.
Some lines are very long. For example, line 32 is 111 characters long; it should be split into two lines.
 - Lots of strange syntax.
On lines 18 and 19, I was repeating myself;
Line 20 has a clumsy condition statement.
No parentheses around the returning value. This shows that I have read some horribly outdated Python 2 tutorial online. But where else to get free, professional, and up-to-date tutorials other than the [official website python.org]?
 - The comment on line 13 shows that I didn't even understand the data structure of the Line2D object, or that the statement constructs a 1-tuple; I simply thought that the comma is yet another idiom and copied it down.
 - Strange way of solving problems. I don't understand why past me generated a random number rand between -4π and 0, took its sin/cos and multiplied it by 50.
 - Even so, the problem isn't solved. The generated dots still tend to cluster together and make an ungainly sight.
 - As an extension to the arbitrary RNG, there are many unexplained numbers in the program. To increase readability and ease changes, they should be assigned to constants. 1920 and 1080 might have been intended to simulate my computer's resolution; in my current understanding, they should be assigned to WIDTH and HEIGHT, respectively.
 - Miscellaneous irregularities, such as using fig.add_subplot() for a single-plot graph, or specifying np.float16 for dtype. Don't know where I copied those from...

## Remedies
