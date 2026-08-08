from agents.agent import Agent
from game.state import State
from game.action import Action
import random

class QLearningAgent(Agent):
    def __init__(
        self,
        alpha: float,
        epsilon: float,
        gamma: float,
    ):
        self.q_table: dict[State, dict[Action, float]] = {}
        self.alpha: float = alpha
        self.epsilon: float = epsilon
        self.gamma: float = gamma

    def choose_action(self, state: State, actions: list[Action]) -> Action:
        if (random.random() < self.epsilon):
            return random.choice(actions)

        q_values = self._get_q_values(state)
        max_q_value = max(
            q_values.get(action, 0.0)
            for action in actions
        )

        best_actions = [
            action
            for action in actions
            if q_values.get(action, 0.0) == max_q_value
        ]

        return random.choice(best_actions)

    def update(
        self,
        state: State,
        action: Action,
        reward: float,
        next_state: State,
        next_actions: list[Action],
        done: bool,
    ) -> None:
        q_values = self._get_q_values(state)

        current_q = q_values.get(action, 0.0)

        if done:
            target = reward
        else:
            max_next_q = self._max_q_value(next_state, next_actions)
            target = reward + self.gamma * max_next_q

        q_values[action] = current_q + self.alpha * (
            target - current_q
        )

    def _max_q_value(
        self,
        state: State,
        actions: list[Action],
    ) -> float:
        q_values = self._get_q_values(state)

        return max(
            (q_values.get(action, 0.0) for action in actions),
            default=0.0,
        )

    def _get_q_values(self, state: State) -> dict[Action, float]:
        if state not in self.q_table:
            self.q_table[state] = {}

        return self.q_table[state]
