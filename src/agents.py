from copy import copy

class Agent:
    def __init__(self, id: int, pref: None | list = None) -> None:
        self.id = id
        self.pref = copy(pref) if pref else []
        self.rank_dict = {a: i for i, a in enumerate(pref)}

    def set_pref(self, pref: list) -> None:
        self.pref = copy(pref)
        self.rank_dict = {a: i for i, a in enumerate(pref)}

    def rank(self, a) -> int:
        if a is None:
            return int(1e+9)
        return self.rank_dict[a]

    def best_agent(self, agent_list):
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
