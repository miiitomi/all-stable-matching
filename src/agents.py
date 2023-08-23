from copy import copy

class Agent:
    def __init__(self, id: int, pref: None | list = None) -> None:
        self.id = id    # Set an index of the agent in the list as an id.
        self.pref = copy(pref) if pref else []
        self.rank_dict = {a: i for i, a in enumerate(pref)} if pref else dict()

    def set_pref(self, pref: list) -> None:
        """Set the preference list of the agent. Please provide a complete list of the opposite side of agents."""
        self.pref = copy(pref)
        self.rank_dict = {a: i for i, a in enumerate(pref)}

    def rank(self, a) -> int:
        """Return the rank of the given agent in the preference list (0-indexed)."""
        if a is None:
            return int(1e+9)
        return self.rank_dict[a]

    def best_agent(self, agent_list):
        """Return the best agent in the given list of agents."""
        if agent_list == []:
            return None
        return min(agent_list, key=lambda a: self.rank(a))


class Man(Agent):
    def __init__(self, id: int, pref: None | list = None) -> None:
        super().__init__(id, pref)

    def __repr__(self) -> str:
        return f"m_{self.id}"


class Woman(Agent):
    def __init__(self, id: int, pref: None | list = None) -> None:
        super().__init__(id, pref)

    def __repr__(self) -> str:
        return f"w_{self.id}"
