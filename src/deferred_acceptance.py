from agents import Agent, Man, Woman

def deferred_acceptance(men_list: list[Man], women_list: list[Woman], man_propose: bool=True) -> map:
    """Return a stable matching by Deferred Acceptance algorithm.
    
    Parameters
    ----------
    men_list: list[Man]
        List of men.
    women_list: list[Woman]
        List of women.
    man_propose: bool
        If man_propose is True, Man-propose DA algorithm will be conducted.
        Else, Woman-propose DA algorithm will be conducted.

    Returns
    -------
    matching: map
        Matching result.
    """
    matching: dict = {a: None for a in men_list+women_list}

    proposer_list: list[Agent] = men_list if man_propose else women_list
    receiver_list: list[Agent] = women_list if man_propose else men_list

    tmp_proposal: dict[Agent, list[Agent]] = {a: [] for a in receiver_list}
    next_proposal_idx: dict[Agent, int] = {a: 0 for a in proposer_list}
    update: bool = True

    while update:
        update = False

        for a in proposer_list:
            if matching[a] is None and len(a.pref) > next_proposal_idx[a]:
                update = True
                b = a.pref[next_proposal_idx[a]]
                tmp_proposal[b].append(a)
                next_proposal_idx[a] += 1

        for b in receiver_list:
            if len(tmp_proposal[b]) > 0:
                if matching[b] is not None:
                    a = matching[b]
                    tmp_proposal[b].append(a)
                    matching[a] = None
                a = b.best_agent(tmp_proposal[b])
                matching[a] = b
                matching[b] = a
                tmp_proposal[b] = []

    return matching


if __name__ == '__main__':
    m = [Man(i) for i in range(3)]
    w = [Woman(i) for i in range(3)]

    m[0].set_pref([w[0], w[1], w[2]])
    m[1].set_pref([w[1], w[2], w[0]])
    m[2].set_pref([w[2], w[0], w[1]])
    w[0].set_pref([m[2], m[1], m[0]])
    w[1].set_pref([m[0], m[2], m[1]])
    w[2].set_pref([m[1], m[0], m[2]])

    matching = deferred_acceptance(m, w, True)
    print(matching)
    # {m_0: w_0, m_1: w_1, m_2: w_2, w_0: m_0, w_1: m_1, w_2: m_2}
    matching = deferred_acceptance(m, w, False)
    print(matching)
    # {m_0: w_1, m_1: w_2, m_2: w_0, w_0: m_2, w_1: m_0, w_2: m_1}

