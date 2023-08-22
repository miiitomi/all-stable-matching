from agents import Man, Woman
from deferred_acceptance import deferred_acceptance
from dfs import find_all_cycles

def join_irreducible_matching(rotation: list[tuple[Man,Woman]], men_list: list[Man], women_list: list[Woman]) -> dict:
    """Return the join-irreducible stable matching corresponding to given rotation.

    Parameters
    ----------
    rotation : list[tuple[Man,Woman]]
        A rotation.
    men_list : list[Man]
        A list of Man.
    women_list : list[Woman]
        A list of Woman.
    
    Returns
    -------
    dict
        The join-irreducible stable matching corresponding to given rotation.
    """
    matching = deferred_acceptance(men_list, women_list, True)

    min_idx = rotation.index(min(rotation, key=lambda t: t[0].id))
    given_rotation = rotation[min_idx:] + rotation[:min_idx]
    rotations = []

    while True:
        rotations = []
        G = [[] for _ in range(len(men_list))]

        for m in men_list:
            woman_prefer_m_list = [w for w in women_list if w.rank(m) < w.rank(matching[w])]
            next_dict_m = m.best_agent(woman_prefer_m_list)
            if next_dict_m is not None:
                G[m.id].append(matching[next_dict_m].id)

        all_cycles = find_all_cycles(G)

        for cycle in all_cycles:
            rotation = []
            for man_idx in cycle:
                rotation.append((men_list[man_idx], matching[men_list[man_idx]]))
            rotations.append(rotation)

        if rotations == [given_rotation]:
            break

        rotation = rotations[0]
        if rotation == given_rotation:
            rotation = rotations[1]
        
        for i, pair in enumerate(rotation):
            m = pair[0]
            matching[m] = rotation[(i+1)%len(rotation)][1]
            matching[matching[m]] = m
    
    return matching

