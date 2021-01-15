def count_if(values,criteria):
    return len(helper(values,criteria))
    
def sum_if(values,criteria):
    return sum(helper(values,criteria))
    
def average_if(values,criteria):
    return sum(helper(values,criteria))/len(helper(values,criteria))
def helper(values,criteria):
    if isinstance(criteria, str) and criteria.startswith("<="):
        return [i for i in values if i<=float(criteria[2:])] 
    elif isinstance(criteria, str) and criteria.startswith(">="):
        return [i for i in values if i>=float(criteria[2:])] 
    elif isinstance(criteria, str) and criteria.startswith("<>"):
        return [i for i in values if i!=float(criteria[2:])] 
    elif isinstance(criteria, str) and criteria.startswith("<"):
        return [i for i in values if i<float(criteria[1:])] 
    elif isinstance(criteria, str) and criteria.startswith(">"):
        return [i for i in values if i>float(criteria[1:])] 
    return [i for i in values if i==criteria] 