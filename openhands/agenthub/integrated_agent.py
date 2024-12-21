from openhands.agenthub.codeact_agent.agent import CodeActAgent
from openhands.agenthub.planner_agent.agent import PlannerAgent

class IntegratedAgent:
    def __init__(self, llm, config):
        self.codeact_agent = CodeActAgent(llm, config)
        self.planner_agent = PlannerAgent(llm, config)

    def step(self, state):
        # Use the planner agent to plan the next action
        planned_action = self.planner_agent.step(state)

        # If the planned action is an AgentFinishAction, return it
        if isinstance(planned_action, AgentFinishAction):
            return planned_action

        # Otherwise, use the codeact agent to execute the planned action
        return self.codeact_agent.step(state)