def convert_lambda_to_def(string):
    args=string[string.index("lambda ")+7:string.index(":")]
    name=string[:string.index(" ")]
    cal=string[string.index(":")+2:]
    return f"def {name}({args}):\n    return {cal}"