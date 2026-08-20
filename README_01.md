# LeetCode 1791 – Find Center of Star Graph

## Problem

You are given an undirected star graph with `n` nodes and `n - 1` edges. A star graph has one center node that is connected to every other node.

Given the edges, return the center node of the star graph.

## Example

### Input

```text
[[1,2],[2,3],[4,2]]
```

### Output

```text
2
```

### Explanation

Node `2` is connected to every other node, so `2` is the center of the star graph.

## Approach

The center node must appear in both of the first two edges.

For example:

```text
[1, 2]
[2, 3]
```

The common node is `2`, so `2` is the center.

## Complexity

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`

## Language

Python

## LeetCode

Problem 1791 – Find Center of Star Graph
