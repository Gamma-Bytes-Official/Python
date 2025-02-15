## Insertion Sort

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

### Process

1. **Start with the second element** (index 1) of the array. Assume the first element (index 0) is already sorted.
2. **Compare the current element** (key) with the elements in the sorted portion of the array (to its left).
3. **Shift all elements** in the sorted portion that are greater than the key to the right by one position.
4. **Insert the key** into its correct position in the sorted portion.
5. **Repeat** the process for all elements in the array until the entire array is sorted.

### Example

Consider the array `[12, 11, 13, 5, 6]`:

- Start with the second element `11`. Compare it with `12` and insert `11` before `12`.
- The array becomes `[11, 12, 13, 5, 6]`.
- Move to the next element `13`. It is already in the correct position.
- The array remains `[11, 12, 13, 5, 6]`.
- Move to the next element `5`. Compare it with `13`, `12`, and `11`, and insert `5` at the beginning.
- The array becomes `[5, 11, 12, 13, 6]`.
- Move to the last element `6`. Compare it with `13`, `12`, and `11`, and insert `6` after `5`.
- The final sorted array is `[5, 6, 11, 12, 13]`.

### Code

The implementation of insertion sort in Python can be found in the `insertionsort.py` file.

## Bubble Sort

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

### Process

1. **Start at the beginning** of the array.
2. **Compare the first two elements**. If the first is greater than the second, swap them.
3. **Move to the next pair** of elements, compare them, and swap if necessary.
4. **Continue** this process for each pair of adjacent elements to the end of the array. This completes one pass.
5. **Repeat** the process for the entire array until no swaps are needed, indicating that the array is sorted.

### Example

Consider the array `[64, 34, 25, 12, 22, 11, 90]`:

- Start with the first two elements `64` and `34`. Swap them because `64 > 34`.
- The array becomes `[34, 64, 25, 12, 22, 11, 90]`.
- Move to the next pair `64` and `25`. Swap them because `64 > 25`.
- The array becomes `[34, 25, 64, 12, 22, 11, 90]`.
- Continue this process for the entire array. After the first pass, the largest element `90` is at the end.
- Repeat the process for the remaining elements until the array is sorted.

### Code

The implementation of bubble sort in Python can be found in the `bubblesort.py` file.

## Linear Search

Linear search is a simple search algorithm that checks each element in the array sequentially until the target element is found or the end of the array is reached.

### Process

1. **Start at the beginning** of the array.
2. **Compare the current element** with the target element.
3. **If the current element** matches the target, return the index of the current element.
4. **If the current element** does not match the target, move to the next element.
5. **Repeat** the process until the target element is found or the end of the array is reached.

### Example

Consider the array `[2, 4, 6, 8, 10]` and the target element `6`:

- Start with the first element `2`. It does not match the target.
- Move to the next element `4`. It does not match the target.
- Move to the next element `6`. It matches the target.
- Return the index `2`.

### Code

The implementation of linear search in Python can be found in the `linearsearch.py` file.

## Stack Operations

A stack is a linear data structure that follows the Last In First Out (LIFO) principle. The two primary operations for a stack are `push` and `pop`.

### Push Operation

The `push` operation adds an element to the top of the stack.

**Process:**
1. Take the element to be added.
2. Place it on the top of the stack.

**Example:**
Consider a stack with elements `[1, 2]`. If we push `3` onto the stack, it becomes `[1, 2, 3]`.

### Pop Operation

The `pop` operation removes the top element from the stack.

**Process:**
1. Check if the stack is not empty.
2. Remove the top element from the stack and return it.

**Example:**
Consider a stack with elements `[1, 2, 3]`. If we pop an element from the stack, it becomes `[1, 2]` and the popped element is `3`.

### Code Example

The implementation of the `push` and `pop` operations in Python can be found in the `stack.py` file.

## Queue Operations

A queue is a linear data structure that follows the First In First Out (FIFO) principle. The two primary operations for a queue are `enqueue` and `dequeue`.

### Enqueue Operation

The `enqueue` operation adds an element to the end of the queue.

**Process:**
1. Take the element to be added.
2. Place it at the end of the queue.

**Example:**
Consider a queue with elements `[1, 2]`. If we enqueue `3` to the queue, it becomes `[1, 2, 3]`.

### Dequeue Operation

The `dequeue` operation removes the front element from the queue.

**Process:**
1. Check if the queue is not empty.
2. Remove the front element from the queue and return it.

**Example:**
Consider a queue with elements `[1, 2, 3]`. If we dequeue an element from the queue, it becomes `[2, 3]` and the dequeued element is `1`.

### Code Example

The implementation of the `enqueue` and `dequeue` operations in Python can be found in the `queue.py` file.
