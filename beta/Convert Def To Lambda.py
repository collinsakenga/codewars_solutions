def convert_def_to_lambda(string):
    name=string[string.index(" ")+1:string.index("(")]
    args=string[string.index("(")+1:string.index(")")]
    statement=string[string.index("return ")+7:]
    return f"{name} = lambda {args}: {statement}"