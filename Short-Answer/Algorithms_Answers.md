#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Given that the loop checks if a is less than n cubed, while adding n squared to a each iteration of the loop, it would take n times to iterate through the loop entirely, so it has a runtime of O(n).

b) In this function there are two loops, the for loop, which runs n times, and the inner loop which uses a comparison between j and n to determine when to stop. every time the inner loop runs, j doubles, so the breakpoints of when the inner loop would stop are on exponents of 2, therefore the runtime is O(n*log2(n)). log2 is a logarithmic function with a base of 2.

c) This is a simple recursion function that runs itself again while the variable bunnies is over 0, every time it recurses, it decrements bunnies by one, therefore it has a runtime of O(n).

## Exercise II

I would probably use a binary search to determine this, where if the egg in the middle floor breaks, continue with the lower half of the search, and vice versa if it doesn't. Since binary searches have a runtime of O(log2(n)), it would mean that the number of dropped eggs would be decently small regardless of the number of floors. In situations where the middle floor of the binary search falls in between floors, I would have the search round up.

The reason I would have the search round up is in case of a situation where one of the floors that the middle of the search falls in between is the floor I'm looking for. Since I have a 50% chance to guess the right one, it would be better that I pick the higher one and be wrong, since that would mean that the search would use that floor as the new high floor in the search, and my search would be covering floors where eggs do not break when dropped.

Also, I would make it so that if a midpoint was a floor where an egg broke, I would use the floor under it as the high floor for the next search, since it doesn't make sense to test it again. I'd also keep a list of floors that broke eggs and didn't, and as soon as there's a floor where an egg broke right underneath one that did, I'll know that's the floor I'm looking for.

Lets say for example that my building is 100 stories tall and eggs
don't break at floors below floor 20. The search would go as follows:

Floors 1-100, mid = 51, break
Floors 1-50, mid = 26, break
Floors 1-25, mid = 13, safe
Floors 13-25, mid = 19, safe
Floors 19-25, mid = 22, break
Floors 19-21, mid = 20, safe
Floors 20-21, mid = 21, break From here, the search would know that floor 20 is a safe floor, and the floor above it, 21, broke the egg. It would stop searching and declare floor 20 as the floor I'm looking for, with a final score of dropped + broken eggs of 11.

