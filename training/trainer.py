from agents.agent import Agent
from game.game import Game, Player, Action, State

class Trainer:
    def __init__(self, game: Game, x_agent: Agent, o_agent: Agent):
        self.game: Game = game
        self.agents = {
            Player.X: x_agent,
            Player.O: o_agent
        }

    def run_episode(self) -> Player | None:
        self.game.reset()

        while not self.game.is_over():
            agent = self.agents[self.game.current_player]
            state: State = self.game.state()
            action: Action = agent.choose_action(state)
            try:
                self.game.play(action)
            except ValueError:
                continue

        return self.game.winner()
        

        
        