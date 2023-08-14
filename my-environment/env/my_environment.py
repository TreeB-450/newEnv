from pettingzoo.utils.env import ParallelEnv
from core import Agent, Target, Obstacle
import numpy as np

class MyEnvironment(ParallelEnv):
    metadata = {
        "name": "my_environment_v0",
    }

    def __init__(self):
        self.word = World()


    def reset(self, seed=None, options=None):
        num_agents = 2
        num_targets = 2
        num_obstacles = 2
        # 添加智能体
        self.word.agents = [Agent() for i in range(num_agents)]
        for i, agent in enumerate(self.word.agents):
            agent.name = f"agent_{i}"
            agent.size = 0.15
            agent.color = np.array([188, 200, 222])  # 蓝色
        # 添加目标
        self.word.targets = [Target() for i in range(num_targets)]
        for i, target in enumerate(self.word.targets):
            target.name = f"target_{i}"
            target.size = 0.15
            target.color = np.array([255, 209, 224])  # 粉色

        # 添加障碍物
        self.word.obstacles = [Obstacle() for i in range(num_obstacles)]
        for i, obstacle in enumerate(self.word.obstacles):
            obstacle.name = f"obstacles_{i}"
            obstacle.size = 0.15
            obstacle.color = np.array([0, 0, 0])  # 黑色

        # 随机设置所有物体的位置, 不能重合
        for agent in self.word.agents:
            agent.pos = np.random.uniform(-1, +1, 2)
        for target in self.word.targets:
            target.pos = np.random.uniform(-1, +1, 2)
        for obstacle in self.word.obstacles:
            obstacle.pos = np.random.uniform(-1, +1, 2)

        observations = {
            a: (

            )
            for a in self.agents
        }
        return observations, {}

    def step(self, actions):
        for i, agent in enumerate(self.word.agents):
            i = int(i)
            if actions[i] == 0:
                agent.pos[0] += 0
            elif actions[i] == 1:
                agent.pos[0] += 1
            elif actions[i] == 2:
                agent.pos[0] += -1
            elif actions[i] == 3:
                agent.pos[1] += 1
            elif actions[i] == 4:
                agent.pos[1] += -1



    def render(self):
        pass

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]



class World:  # multi-agent world
    def __init__(self):
        self.agents = []  # 智能体集合
        self.targets = []  # 目标
        self.obstacles = []  # 障碍物
