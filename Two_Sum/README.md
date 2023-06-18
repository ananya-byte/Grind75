## Notes

### Two Sum In Python
#### - Method 1
>This is the brute force method. Using a nested loop where the first loop(x) traverses the list from 0 to the end. The second inner loop(y) traverses the list from x+1 to the 
>end. In this inner loop we also check if **x+y==target**. When true it is appended to an empty list which is returned as final output.

#### - Method 2
>The second method. This algorithm first traverses the list and fins the other missing value needed to fulfill the target. It checks if the calculated value is present in the list and the index at which is found is not equal to the previous number.
