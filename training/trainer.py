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
            player = self.game.current_player
            agent = self.agents[player]

            state = self.game.state()
            actions = self.game.legal_actions()

            action = agent.choose_action(state)

            self.game.play(action)

            next_state = self.game.state()
            next_actions = self.game.legal_actions()
            done = self.game.is_over()

            agent.update(
                state = state,
                action = action,
                reward = 0.0,
                next_state = next_state,
                next_actions = next_actions,
                done = done
            )


        return self.game.winner()
        

        
        