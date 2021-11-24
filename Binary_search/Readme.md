# Binary Search

## Definition:
## Binary search is a search algorithm which finds the element by repeatedly dividing an array in half until the search element is found or array’s length  is one and this only works for sorted arrays.

Pseudocode:
Initialize variable start and end
Run while till start and end do not intersect.
Calculated mid index of array
If mid index contains value that was being searched return the index
Otherwise if the value  is less than mid  search in first half of array
If the value is greater than mid then search in the second half of the array.
