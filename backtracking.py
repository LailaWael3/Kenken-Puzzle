class CSP ():
    def __init__(self, variables, domains, neighbors, constraints):

        variables = variables or list(domains.keys())
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.curr_domains = None
        self.nassigns = 0

    def choices(self, var):
        return (self.curr_domains or self.domains)[var]   

    def conflicts(self, var, val, assignment):
        def conflict(var2):
            return (var2 in assignment and
                    not self.constraints(var, val, var2, assignment[var2]))       
        for v in self.neighbors:
            if(conflict(v)):
                return True
        return False  

    def assign(self, var, val, assignment):
        assignment[var] = val
        self.nassigns += 1          

    
    def support_pruning(self):
        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}

    def suppose(self, var, value):
        self.support_pruning()
        removals = [(var, a) for a in self.curr_domains[var] if a != value]
        self.curr_domains[var] = [value]
        return removals    

    def restore(self, removals):
        for B, b in removals:
            self.curr_domains[B].append(b)    

    def unassign(self, var, assignment):
        if var in assignment:
            del assignment[var]        

    def prune(self, var, value, removals):
        self.curr_domains[var].remove(value)
        if removals is not None:
            removals.append((var, value))  

    def goal_test(self, state):
        assignment = dict(state)
        return (len(assignment) == len(self.variables)
                and all(self.conflicts(variables, assignment[variables], assignment) == False
                        for variables in self.variables))  

def select_unassigned_variable(assignment, csp):
    for var in csp.variables :
        if var not in assignment:
            return var
    return None



def order_domain_values(var, csp):
    return csp.choices(var)

def no_inference(csp, var, value, assignment, removals):
    return True

def backtracking_search(csp,inference=no_inference):

    def backtrack(assignment):
        if len(assignment) == len(csp.variables):
            return assignment
        var = select_unassigned_variable(assignment, csp)
        for value in order_domain_values(var, csp):
            if csp.conflicts(var, value, assignment) == False:
                csp.assign(var, value, assignment)
                removals = csp.suppose(var, value)
                if inference(csp, var, value, assignment, removals):
                    result = backtrack(assignment)
                    if result is not None:
                        return result
                csp.restore(removals)
        csp.unassign(var, assignment)
        return None

    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result   

def forward_checking(csp, var, value, assignment, removals):
    csp.support_pruning()
    for B in csp.neighbors[var]:
        if B not in assignment:
            for b in csp.curr_domains[B][:]:
                if not csp.constraints(var, value, B, b):
                    csp.prune(B, b, removals)
            if not csp.curr_domains[B]:
                return False
    return True



def remove_incosistant_values(csp, Xi, Xj, removals):
    removed = False
    for x in csp.curr_domains[Xi][:]:
        if all(not csp.constraints(Xi, x, Xj, y) for y in csp.curr_domains[Xj]):
            csp.prune(Xi, x, removals)
            removed = True
    return removed


def AC3(csp, var, value, assignment, removals):
    queue = [(Xi, Xk) for Xi in csp.variables for Xk in csp.neighbors[Xi]]
    csp.support_pruning()
    while queue:
        (Xi, Xj) = queue.pop()
        if remove_incosistant_values(csp, Xi, Xj, removals):
            if not csp.curr_domains[Xi]:
                return False
            for Xk in csp.neighbors[Xi]:
                if Xk != Xj:
                    queue.append((Xk, Xi))
    return True