# -----------------
# User Instructions
# 
# Write a function, subway, that takes lines as input (read more about
# the **lines notation in the instructor comments box below) and returns
# a dictionary of the form {station:{neighbor:line, ...}, ... } 
#
# For example, when calling subway(boston), one of the entries in the 
# resulting dictionary should be 'foresthills': {'backbay': 'orange'}. 
# This means that foresthills only has one neighbor ('backbay') and 
# that neighbor is on the orange line. Other stations have more neighbors:
# 'state', for example, has 4 neighbors.
#
# Once you've defined your subway function, you can define a ride and 
# longest_ride function. ride(here, there, system) takes as input 
# a starting station (here), a destination station (there), and a subway
# system and returns the shortest path.
#
# longest_ride(system) returns the longest possible ride in a given 
# subway system. 

# -------------
# Grading Notes
#
# The subway() function will not be tested directly, only ride() and 
# longest_ride() will be explicitly tested. If your code passes the 
# assert statements in test_ride(), it should be marked correct.

def subway(**lines):
    """Define a subway map. Input is subway(linename='station1 station2...'...).
    Convert that and return a dict of the form: {station:{neighbor:line,...},...}"""
    result = {}
    for line, stations in lines.iteritems():
        result[line] = process_one_line(line, stations)
    for line, processed_stations in result.iteritems():
        for station, neighbours in processed_stations.iteritems():
            # look for this station in other lines
            for l, sts in result.iteritems():
                if l is line:
                    next
                if station in sts.keys():
                    neighbours.update(sts[station])
    res = {}
    for stations in result.values():
        res.update(stations)
    return res
        
def process_one_line(line, stations):
    result = {}
    line_stations = stations.split()
    for index, station in enumerate(line_stations):
        fwd_neighbour = None
        back_neighbour = None
        if index > 0:
            back_neighbour = line_stations[index-1]
        if index < len(line_stations) - 1:
            fwd_neighbour = line_stations[index+1]
        value = {}
        if fwd_neighbour is not None:
            value.update({fwd_neighbour: line})
        if back_neighbour is not None:
            value.update({back_neighbour: line})
        result[station] = value
    return result
    
        
boston = subway(
    blue='bowdoin government state aquarium maverick airport suffolk revere wonderland',
    orange='oakgrove sullivan haymarket state downtown chinatown tufts backbay foresthills',
    green='lechmere science north haymarket government park copley kenmore newton riverside',
    red='alewife davis porter harvard central mit charles park downtown south umass mattapan')

def ride(here, there, system=boston):
    "Return a path on the subway system from here to there."
    start = here
    def is_goal(station):
        return station == there
    def successors(station):
        # return a list of possible stations from given one
        return dict((station,
                     line)
                    for station, line in system[station].items())
    return shortest_path_search(start, successors, is_goal)

def longest_ride(system=boston):
    """"Return the longest possible 'shortest path' 
    ride between any two stops in the system."""
    paths = []
    def successors(station):
        # return a list of possible stations from given one
        return dict((station,
                     line)
                    for station, line in system[station].items())
    for here in system.keys():
        for there in system.keys():
            def is_goal(station):
                return station == there
            paths.append(shortest_path_search(here, successors, is_goal))
    def biggest(item):
        return len(item)
    return max(paths, key=biggest)

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return []

def path_states(path):
    "Return a list of states in this path."
    return path[0::2]
    
def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]

def test_ride():
    #print ride('mit', 'government')
    assert ride('mit', 'government') == [
        'mit', 'red', 'charles', 'red', 'park', 'green', 'government']
    assert ride('mattapan', 'foresthills') == [
        'mattapan', 'red', 'umass', 'red', 'south', 'red', 'downtown',
        'orange', 'chinatown', 'orange', 'tufts', 'orange', 'backbay', 'orange', 'foresthills']
    assert ride('newton', 'alewife') == [
        'newton', 'green', 'kenmore', 'green', 'copley', 'green', 'park', 'red', 'charles', 'red',
        'mit', 'red', 'central', 'red', 'harvard', 'red', 'porter', 'red', 'davis', 'red', 'alewife']
    assert (path_states(longest_ride(boston)) == [
        'wonderland', 'revere', 'suffolk', 'airport', 'maverick', 'aquarium', 'state', 'downtown', 'park',
        'charles', 'mit', 'central', 'harvard', 'porter', 'davis', 'alewife'] or 
        path_states(longest_ride(boston)) == [
                'alewife', 'davis', 'porter', 'harvard', 'central', 'mit', 'charles', 
                'park', 'downtown', 'state', 'aquarium', 'maverick', 'airport', 'suffolk', 'revere', 'wonderland'])
    assert len(path_states(longest_ride(boston))) == 16
    return 'test_ride passes'

print test_ride()
