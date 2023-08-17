from agents import Man, Woman
from deferred_acceptance import deferred_acceptance
from dfs import find_cycle

def all_rotations(men_list: list[Man], women_list: list[Woman]):
    """Return all rotations.
    """
    matching = deferred_acceptance(men_list, women_list, True)
    bottom = deferred_acceptance(men_list, women_list, False)
    rotations = []

    while matching != bottom:
        G = [[] for _ in range(len(men_list))]
        for m in men_list:
            woman_prefer_m_list = [w for w in women_list if w.rank(m) < w.rank(matching[w])]
            next_dict_m = m.best_agent(woman_prefer_m_list)
            if next_dict_m is not None:
                G[m.id].append(matching[next_dict_m].id)
        cycle = find_cycle(G)
        rotation = []
        for men_idx in cycle:
            m = men_list[men_idx]
            rotation.append((m, matching[m]))
        rotations.append(rotation)
        for i, pair in enumerate(rotation):
            m = pair[0]
            matching[m] = rotation[(i+1)%len(cycle)][1]
            matching[matching[m]] = m

    return rotations


if __name__ == '__main__':
    m = [Man(i) for i in range(10)]
    m_0 = m[0]
    m_1 = m[1]
    m_2 = m[2]
    m_3 = m[3]
    m_4 = m[4]
    m_5 = m[5]
    m_6 = m[6]
    m_7 = m[7]
    m_8 = m[8]
    m_9 = m[9]
    w = [Woman(i) for i in range(10)]
    w_0 = w[0]
    w_1 = w[1]
    w_2 = w[2]
    w_3 = w[3]
    w_4 = w[4]
    w_5 = w[5]
    w_6 = w[6]
    w_7 = w[7]
    w_8 = w[8]
    w_9 = w[9]

    m[0].set_pref([w_3, w_9, w_1, w_5, w_4, w_2, w_0, w_7, w_8, w_6])
    m[1].set_pref([w_7, w_2, w_6, w_9, w_8, w_0, w_4, w_5, w_1, w_3])
    m[2].set_pref([w_4, w_8, w_6, w_3, w_0, w_5, w_2, w_9, w_1, w_7])
    m[3].set_pref([w_9, w_3, w_5, w_7, w_4, w_2, w_0, w_1, w_8, w_6])
    m[4].set_pref([w_3, w_5, w_0, w_8, w_7, w_2, w_6, w_1, w_9, w_4])
    m[5].set_pref([w_6, w_2, w_4, w_7, w_9, w_3, w_1, w_0, w_8, w_5])
    m[6].set_pref([w_5, w_3, w_0, w_2, w_9, w_8, w_1, w_6, w_4, w_7])
    m[7].set_pref([w_6, w_8, w_2, w_1, w_3, w_4, w_9, w_5, w_7, w_0])
    m[8].set_pref([w_7, w_6, w_0, w_2, w_4, w_5, w_3, w_1, w_8, w_9])
    m[9].set_pref([w_6, w_2, w_1, w_0, w_3, w_5, w_8, w_4, w_9, w_7])
    w[0].set_pref([m_3, m_5, m_1, m_9, m_2, m_4, m_7, m_6, m_0, m_8])
    w[1].set_pref([m_5, m_1, m_0, m_3, m_4, m_9, m_2, m_7, m_8, m_6])
    w[2].set_pref([m_5, m_8, m_9, m_1, m_7, m_2, m_4, m_6, m_3, m_0])
    w[3].set_pref([m_4, m_6, m_7, m_5, m_2, m_3, m_1, m_9, m_8, m_0])
    w[4].set_pref([m_0, m_7, m_8, m_1, m_5, m_2, m_3, m_9, m_4, m_6])
    w[5].set_pref([m_1, m_2, m_9, m_4, m_3, m_8, m_5, m_7, m_0, m_6])
    w[6].set_pref([m_1, m_3, m_9, m_4, m_8, m_2, m_0, m_5, m_6, m_7])
    w[7].set_pref([m_0, m_4, m_5, m_1, m_2, m_7, m_9, m_3, m_6, m_8])
    w[8].set_pref([m_9, m_7, m_3, m_6, m_8, m_2, m_5, m_0, m_4, m_1])
    w[9].set_pref([m_0, m_6, m_7, m_5, m_2, m_1, m_8, m_9, m_3, m_4])

    man_optimal_matching = deferred_acceptance(m, w, True)
    print(man_optimal_matching)
    woman_optimal_matching = deferred_acceptance(m, w, False)
    print(woman_optimal_matching)

    print(all_rotations(m, w))
