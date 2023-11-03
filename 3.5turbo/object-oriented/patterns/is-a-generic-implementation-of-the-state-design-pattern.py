class Context:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def perform_operation(self):
        if self.state is not None:
            self.state.do_operation(self)


class State:
    def do_operation(self, context):
        pass


class ConcreteStateA(State):
    def do_operation(self, context):
        print("Performing operation A")
        # Update context state if necessary
        context.set_state(ConcreteStateB())


class ConcreteStateB(State):
    def do_operation(self, context):
        print("Performing operation B")
        # Update context state if necessary
        context.set_state(ConcreteStateA())


# Usage example
if __name__ == '__main__':
    context = Context()

    # Setting initial state to ConcreteStateA
    context.set_state(ConcreteStateA())

    # Performing operations
    for _ in range(5):
        context.perform_operation()
