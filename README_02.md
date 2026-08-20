# College Assignments

This repository contains my college programming assignments, problem statements, and solutions.

## Repository Structure

```text
College_Assignments/
│
├── Assignment_01/
│
├── Assignment_02/
│   └── Assign_02_Solution.py
│
└── README.md
```

## Assignments

### Assignment 01

Contains the programs and solutions for Assignment 01.

### Assignment 02 – The Quickest Way Up

This assignment solves the **Snakes and Ladders – The Quickest Way Up** problem.

The objective is to find the minimum number of dice rolls required to reach square 100.

#### Approach

The problem is solved using **Breadth-First Search (BFS)**.

* Each square on the board is treated as a node.
* Each dice roll from 1 to 6 represents a possible move.
* Ladders move the player upward.
* Snakes move the player downward.
* BFS finds the minimum number of rolls required.
* If square 100 cannot be reached, the program returns `-1`.

#### Language

**Python 3**

#### Files

* `Problem.py` – Problem statement / problem-related file.
* `Assign_02_Solution.py` – Python solution for the problem.

## Sample Output

For the sample input, the program produces:

```text
3
5
```

## Concepts Used

* Python
* Functions
* Lists
* Dictionaries
* Queue
* Breadth-First Search (BFS)
* Graph Traversal
* Problem Solving

## Author

**Shaik Irshad**

---

This repository is created for learning, practicing, and maintaining college programming assignments.
