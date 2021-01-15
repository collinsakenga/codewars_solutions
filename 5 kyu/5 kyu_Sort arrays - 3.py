def sort_me(courses): 
    return sorted(courses, key=lambda x: (int(x.split('-')[1]), x.split('-')[0]))