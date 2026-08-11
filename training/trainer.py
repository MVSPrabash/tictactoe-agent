from agents.agent import Agent
from game.game import Game, Player, Action, State

class Trainer:
    def __init__(self, game: Game, x_agent: Agent, o_agent: Agent):
        self.game: Game = game
        self.x_agent = x_agent
        self.o_agent = o_agent
        self.agents = {
            Player.X: x_agent,
            Player.O: o_agent
        }

    def run_episode(self) -> Player | None:
        self.game.reset()

        while not self.game.is_over():
            x_state = self.game.state()
            x_action = self.x_agent.choose_action(x_state, self.game.legal_actions())

            self.game.play(x_action)

            if self.game.is_over():
                reward = 0
                winner = self.game.winner()

                if winner == Player.X:
                    reward = 1
                elif winner == Player.O:
                    reward = -1

                self.x_agent.update(
                    x_state,
                    x_action,
                    reward = reward,
                    next_state=self.game.state(),
                    next_actions=[],
                    done=True
                )
                continue

            o_state = self.game.state()
            o_action = self.o_agent.choose_action(o_state, self.game.legal_actions())

            self.game.play(o_action)

            x_next_state = self.game.state()

            self.x_agent.update(
                x_state,
                x_action,
                reward = 0,
                next_state=x_next_state,
                next_actions=self.game.legal_actions(),
                done=self.game.is_over()
            )



        return self.game.winner()
        

        
        