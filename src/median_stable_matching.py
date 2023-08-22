from agents import Man, Woman

def median_stable_matching(men_list: list[Man], women_list: list[Woman], all_stable_matchings: list[dict], k: int) -> dict:
    """Return the k-th median stable matching among the set of all stable matchings.
    
    Parameters
    ----------
    men_list : list[Man]
        A list of Man.
    women_list : list[Woman]
        A list of Woman.
    all_stable_matchings : list[dict]
        The list of all stable matchings.
    k : int
        The index of the median stable matching. 1 <= k <= len(all_stable_matchings).
    
    Returns
    -------
    dict
        The median stable matching among the set of all stable matchings.
    """
    matching = {a : None for a in men_list+women_list}

    for m in men_list:
        tmp_list = []
        for matching in all_stable_matchings:
            tmp_list.append(matching[m])
        tmp_list.sort(key=lambda w: m.rank(w))
        matching[m] = tmp_list[k-1]
    
    for m in men_list:
        w = matching[m]
        matching[w] = m
    
    return matching
