from agents import Man, Woman
from all_rotations import all_rotations
from join_irreducible import join_irreducible_matching
from deferred_acceptance import deferred_acceptance

def is_larger_matching(matching1: dict, matching2: dict, men_list: list[Man]) -> bool:
    """Return True if matching1 is weakly larger than matching2.

    Parameters
    ----------
    matching1 : dict
        A matching.
    matching2 : dict
        A matching.
    men_list : list[Man]
        A list of man agents.
    
    Returns
    -------
    bool
        True if matching1 is weakly larger than matching2.
    """
    for m in men_list:
        if m.rank(matching1[m]) > m.rank(matching2[m]):
            return False
    return True


def join_irreducibles_graph(join_irreducibles: list[dict], men_list: list[Man]) -> list[list[int]]:
    """Return the directed graph that represents the order of join-irreducible matchings.

    Parameters
    ----------
    join_irreducibles : list[dict]
        A list of join-irreducible matchings.
    men_list : list[Man]
        A list of man agents.
    
    Returns
    -------
    list[list[int]]
        A directed graph that represents the order of join-irreducible matchings.
        G[i] is the list of indices of join-irreducible matchings that are lower than join_irreducibles[i].
    """
    G = [[] for _ in range(len(join_irreducibles))]

    for i, matching1 in enumerate(join_irreducibles):
        for j, matching2 in enumerate(join_irreducibles):
            if i == j:
                continue
            if is_larger_matching(matching1, matching2, men_list):
                G[i].append(j)
    
    return G


def join_matching(S: int, join_irreducibles: list[dict], men_list: list[Man], women_list: list[Woman]) -> dict:
    """Returns the join matching among the set S of join-irreducible matchings.

    Parameters
    ----------
    S : int
        The set of join-irreducible matchings. S is represented as a bit string.
    join_irreducibles : list[dict]
        All join-irreducible matchings.
    men_list : list[Man]
        A list of men.
    women_list : list[Woman]
        A list of women.
    
    Returns
    -------
    dict
        The join matching among the set S of join-irreducible matchings.
    """
    matching = {a : None for a in men_list+women_list}

    for i, tmp_matching in enumerate(join_irreducibles):
        if S & (1 << i):
            for m in men_list:
                matching[m] = min([matching[m], tmp_matching[m]], key=lambda w: m.rank(w))

    for m in men_list:
        w = matching[m]
        matching[w] = m
    
    return matching


def all_stable_matching(men_list : list[Man], women_list : list[Woman]) -> list[dict]:
    """Return the all stable matchings.

    Parameters
    ----------
    men_list : list[Man]
        A list of men.
    women_list : list[Woman]
        A list of women.
    
    Returns
    -------
    list[dict]
        The all stable matchings.
    """
    rotations = all_rotations(men_list, women_list)
    join_irreducibles = []
    for rotation in rotations:
        join_irreducibles.append(join_irreducible_matching(rotation, men_list, women_list))

    G = join_irreducibles_graph(join_irreducibles, men_list)
    res = []

    set_int = set()
    for _s in range(1, (1 << len(join_irreducibles))):
        S = _s
        for i in range(len(join_irreducibles)):
            if not (S & (1 << i)):
                continue
            for j in G[i]:
                S = S | (1 << j)
        if S in set_int:
            continue
        set_int.add(S)
        matching = join_matching(S, join_irreducibles, men_list, women_list)
        res.append(matching)
    
    res.append(deferred_acceptance(men_list, women_list, False))
    return res


if __name__ == "__main__":
    m = [Man(i) for i in range(3)]
    w = [Woman(i) for i in range(3)]

    m[0].set_pref([w[0], w[1], w[2]])
    m[1].set_pref([w[1], w[2], w[0]])
    m[2].set_pref([w[2], w[0], w[1]])
    w[0].set_pref([m[2], m[1], m[0]])
    w[1].set_pref([m[1], m[2], m[0]])
    w[2].set_pref([m[0], m[1], m[2]])

    all_stable_matchings = all_stable_matching(m, w)
    print(len(all_stable_matchings))
    for matching in all_stable_matchings:
        print(matching)
    
