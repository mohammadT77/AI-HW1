# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """

        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def Path(parents, node):
    path = []
    while node[1] is not None:
        path.append(node[1])
        node = parents[node]
    return path[::-1]

def __GraphSearch(problem,fringe):
    closed = []
    cn = (problem.getStartState(), None, None)  # current node
    parents = {}
    fringe.push(cn)
    goal = None
    while not fringe.isEmpty():

        cn = fringe.pop()

        # print("CN: "+str(cn)) #TODO trace
        # print("Cost: " + str(len(findPath(parents,cn))))   # TODO trace
        # print("\tFringe:" + str(fringe))  # TODO trace
        # print("\tClosed:" +str(closed)) #TODO trace
        if problem.isGoalState(cn[0]):
            goal = cn
            break
        if cn not in closed:
            closed.append(cn[0])
            for child in problem.getSuccessors(cn[0]):
                # print("\t>" + str(child))  # TODO trace
                if (child[0] not in closed):
                    fringe.push(child)
                    parents[child] = cn

    # """find Path from goal"""
    # pathX = lambda curr_node: [curr_node[1] while (curr_node=parents[curr_node])  in range(2)]
    # if goal is None: return []
    # curr = goal
    # pathX = []
    # while curr[1] is not None:
    #     pathX.append(curr[1])
    #     curr = parents[curr]
    # print
    return Path(parents,goal)


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    return __GraphSearch(problem,util.Stack())
    # fringe = Stack()
    # closed = []
    # cn = (problem.getStartState(), None, None)  # current node
    # parents = {}
    # fringe.push(cn)
    # goal = None
    #
    # while not fringe.isEmpty():
    #     cn = fringe.pop()
    #     # print("CN: "+str(cn)) #TODO trace
    #     # print("\tFringe:" + str(fringe))  # TODO trace
    #     # print("\tClosed:" +str(closed)) #TODO trace
    #     if problem.isGoalState(cn[0]):
    #         goal = cn
    #         break
    #     if cn not in closed:
    #         closed.append(cn[0])
    #         for child in problem.getSuccessors(cn[0]):
    #             # print("\t>" + str(child))  # TODO trace
    #             if (child[0] not in closed) and (child not in fringe.list):
    #                 fringe.push(child)
    #                 parents[child] = cn
    #
    # """find Path from goal"""
    # if goal is None: return []
    # curr = goal
    # path = []
    # while curr[1] is not None:
    #     path.append(curr[1])
    #     curr = parents[curr]
    #
    # return path[::-1]  # return reverse Of path


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return __GraphSearch(problem,util.Queue())
    # fringe = Queue()
    # closed = []
    # cn = (problem.getStartState(), 'Stop', 1)  # current node
    # parents = {}
    # fringe.push(cn)
    # goal = None
    # while not fringe.isEmpty():
    #     cn = fringe.pop()
    #     # print("CN: "+str(cn)) #TODO trace
    #     # print("\tFringe:" + str(fringe))  # TODO trace
    #     # print("\tClosed:" +str(closed)) #TODO trace
    #     if problem.isGoalState(cn[0]):
    #         goal = cn
    #         break
    #     if cn not in closed:
    #         closed.append(cn[0])
    #         for child in problem.getSuccessors(cn[0]):
    #             # print("\t>" + str(child))  # TODO trace
    #             if (child[0] not in closed) and (child not in fringe.list):
    #                 fringe.push(child)
    #                 parents[child] = cn
    #
    # """find Path from goal"""
    # if goal is None: return []
    # curr = goal
    # path = []
    # while curr[1] is not None:
    #     path.append(curr[1])
    #     curr = parents[curr]
    #
    # return path[::-1] #return reverse Of path


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    Gn = lambda Path:len(Path)


    return __GraphSearch(problem,util.PriorityQueueWithFunction(Gn))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
