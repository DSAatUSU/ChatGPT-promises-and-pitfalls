class Context:
    def __init__(self, initialState):
        self.state = initialState

    def updateState(self, newState):
        self.state = newState

    def doWorkWithState(self):
        self.state.doWork()


class State:
    def doWork(self):
        pass


# Test Code
class MinerState(State):
    def doWork(self):
        print("Mining!")


class ConstructorState(State):
    def doWork(self):
        print("Constructing!")


state = Context(ConstructorState())
state.doWorkWithState()
state.updateState(MinerState())
state.doWorkWithState()
