# P1: Python practice 

**Assigned**: Jan 31, 2025

**Due**: Feb 7, 2025 2:59PM

**Late deadline**: Feb 10th, 2025 11:59PM

## Description

You will be implementing some basic functions in Python as practice, including using iterators and built-in functions.

## Setup

Make sure Python 3.12 is installed on your computer.

You should work on this project (and the other projects in this course) in a virtual environment.
Navigate to the root of a directory you will use for this class. You should use the same environment
for all projects in this course; you don't need more than one.
To create and activate one, enter the following commands in your terminal:

For Mac/Linux:
```bash
$ python3 -m venv venv        # creates environment
$ source ./venv/bin/activate  # enters environment
```
To activate the venv in the future, run 
```bash
$ source /#PATH-TO-VENV#/venv/bin/activate  # enters environment
```

For Windows:
```bash
$ py -m venv venv             # creates environment
$ ./venv/Scripts/activate     # enters environment
```
To activate the venv in the future, run 
```bash
$ /#PATH-TO-VENV#/venv/Scripts/activate  # enters environment
```

These instructions can also be found in the Week 1 slides.

Testing this project with our public tests requires a package called `pytest`.
To install it, run either of the following in your terminal while in your virtual environment:
```bash    
$ pip3 install -r requirements.txt
```
```bash
$ pip3 install pytest
```
Again, you **must** be in your virtual environment when installing packages with pip.

## Project

In `practice.py`, implement the following functions:

1. `hello_world()`

   Return the string `Hello, World!`

2. `sum_unique(l)`

   Given a sequence of integers, return the sum of the integers, not counting duplicates, i.e. 
   if you have two or more copies of an integer, it should be added to the final sum once.

   Examples:
   ```python
   >>> sum_unique([])
   0
   >>> sum_unique([4, 4, 5])
   9
   >>> sum_unique([4, 2, 5])
   11
   >>> sum_unique([2, 2, 2, 2, 1])
   3
   ```

3. `palindrome(x)`

    Given an integer or a string *x*, determine if *x* has the same value as *x* reversed.

    Examples:
    ```python
    >>> palindrome(1331)
    True
    >>> palindrome('racecar')
    True
    >>> palindrome(1234)
    False
    >>> palindrome('python')
    False
    ```

4. `sum_multiples(num)`

    Given a positive integer `num`, find the sum of all multiples of 3 and 5 upto and not including `num`.

    Examples:
    ```python
    >>> sum_multiples(10) # Multiples: [3, 5, 6, 9]
    23
    >>> sum_multiples(3) # Multiples: []
    0
    >>> sum_multiples(5) # Multiples: [3]
    3
    >>> sum_multiples(16) # Multiples: [3, 5, 6, 9, 10, 12, 15]
    60
    ```

5. `num_func_mapper(nums, funs)`

    Given a sequence of numbers `nums` and a sequence of functions `funs`, 
    apply each function to `nums` and store the result in a list.
    Return the list of results. 
    
    *Hint*: The list of results should be the same length as `funs`.

    Example:
    ```python
    >>> f_list = [sum_unique, sum]
    >>> num_list = [2, 2, 2, 4, 5]
    >>> num_func_mapper(num_list, f_list)
    [11, 15]
    ```

6. `height_sort(names, heights)`

    You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
    For each index i, names[i] and heights[i] denote the name and height of the ith person.
    Return names sorted in descending order by the people's heights.

    Example 1:
    ```python
    >>> names = ["Mary","John","Emma"]
    >>> heights = [180,165,170]
    ["Mary","Emma","John"]
    # Explanation: Mary is the tallest, followed by Emma and John.
    ```

    Example 2:
    ```python
    >>> names = ["Alice","Bob","Bob"]
    >>> heights = [155,185,150]
    ["Bob","Alice","Bob"]
    # Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
    ```
7. `custom_sort(lst)`

   Use Python's built-in `sort` function to sort the list so that the odd numbers (in the same order as in the original list) come first, and then the even numbers (also in the same order).
   
   Examples:
   ```python
   >>> custom_sort([1, 2, 3, 4, 5])
   [(1, 3, 5, 2, 4)]
   ```
   (Hint: use a lambda function)



## Testing

Navigate into the `p1/` directory and run the command `pytest`.
You should see your test results in the terminal.

## Submission & Grading

We'll be using Github Classroom for this project and all other projects in this class.

> [!IMPORTANT]
> Log into your Gradescope account and go to your account settings. Scroll down to the `Linked Accounts` section. If you do not already
> have your GitHub account linked here, click the `Link a GitHub account` button and log into your GitHub account.

Whenever you want to submit your project to Gradescope, you will need to push your latest version to your repo. Follow these steps to do so:

First, make sure all your changes are pushed to GitHub using the git add, git commit, and git push commands.

Next, to submit your project, you can run `submit` from your project directory.
> [!NOTE]
> you will need to have `opam` package `gradescope-submit` installed. If you don't have it on your system from 330, you can use the UI on Gradescope to link your Github repository or you can look at the 330 project0 readme for [installation instructions](https://github.com/cmsc330fall23/cmsc330fall23/blob/main/projects/project0.md#windows).

The submit command will pull your code from GitHub, not your local files. If you do not push your changes to GitHub, they will not be uploaded to Gradescope.


There are **130** possible points: 13 public tests worth 10 points each.
