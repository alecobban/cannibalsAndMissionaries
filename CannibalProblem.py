class CannibalProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)
        self.total_missionaries = start_state()[0] #total number of missionaries extracted from the tuple
        self.total_canibals = start_state()[1] #total canibals from the start state tuple
        # you might want to add other things to the problem,
        #  like the total number of missionaries (which you can figure out
        #  based on start_state

    # get successor states for the given state
    def get_successors(self, state):
        # you write this part. I also had a helper function
        #  that tested if states were safe before adding to successor list
        return
    # I also had a goal test method. You should write one.

    def goal_test(self, state):
        if state == (0,0,1):
            return True
        else:
            return False
    def is_state_safe(self, state):
        firstBankMissionaries =state[0]
        firstBankCanibals = state[1]
        second_bank_missionaries = self.total_missionaries - firstBankMissionaries
        second_bank_cannibals = self.total_canibals - firstBankCanibals
        if state[0] == 0 or 3:
            return True
        elif (state[0] >= state [1]) and (second_bank_missionaries >= second_bank_cannibals):
            return True

    def __str__(self):
        string =  "Missionaries and cannibals problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = CannibalProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)
