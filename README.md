# All stable matching

This repository provides algorithms that return the man/woman-optimal stable matching (DA algorithm), the list of all rotations, the join-irreducible matching that corresponding to a given rotation, the list of all stable matchings, and the generalized median stable matching in the one-to-one stable marriage problem.
It can compute all stable matchings in seconds for $n \simeq 80$ or smaller.

## Requirements
Python 3.10 or later.

## Files
```bash
.
├── LICENSE
├── README.md
├── notebooks
│   └── all_stable_matching.ipynb    # Example usage
└── src
    ├── agents.py    # Agent (Man/Woman) class
    ├── all_rotations.py    # Algorithm that returns all rotations
    ├── all_stable_matching.py    # Algorithm that returns all stable matchings
    ├── deferred_acceptance.py    # DA algorithm
    ├── dfs.py    # DFS that finds cycle(s) for a given directed graph
    ├── join_irreducible.py    # Algorithm that returns a join irreducible matching
    └── median_stable_matching.py    # Algorithm that returns a median stable matching
```

## Usage
Make lists of Man/Woman agents, and set preference lists (strict order).
```python
from agents import Man, Woman
m = [Man(i) for i in range(3)]    # Please provide the index of the instance in the list.
w = [Woman(i) for i in range(3)]
m[0].set_pref([w[0], w[1], w[2]])    # Set the preference list
...
w[0].set_pref([m[2], m[1], m[0]])
...
```
The Man/Woman optimal stable matching can be computed by the DA algorithm.
(Set `man_propose=True` if you want the Man-optimal matching, otherwise `False`.)
```python
from deferred_acceptance import deferred_acceptance
matching = deferred_acceptance(men_list=m, women_list=w, man_propose=True)
```
`all_lotations` returns a list of all rotations of the given instance.
```python
from all_rotations import all_rotations
rotations = all_rotations(men_list=m, women_list=w)
```
`join_irreducible_matching` returns the join-irreducible matching corresponding to the given rotation.
```python
from join_irreducible import join_irreducible_matching
matching = join_irreducible_matching(rotation=rotation, men_list=m, women_list=w)
```
`all_stable_matching` returns a list of all stable matchings of the given instance.
```python
from all_stable_matching import all_stable_matching
all_stable_matchings = all_stable_matching(men_list=m, women_list)
```
`median_stable_matching` returns the k-th median stable matching of the given set of stable matchings.
```python
from median_stable_matching import median_stable_matching
median_matching = median_stable_matching(men_list=m, women_list=w, stable_matchings=all_stable_matchings, k=1)
```
See `notebooks/all_stable_matching.ipynb` for details.

## Reference
"Online and Matching-Based Market Design" (edited by Federico Echenique,  Nicole Immorlica, Vijay V. Vazirani, 2023, Cambridge University Press), Chaprer 1.

## License
MIT License. See `LICENSE` for details.
