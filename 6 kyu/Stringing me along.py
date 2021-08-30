class create_message(str):
    def  __call__(self, s=""):
        return create_message((self+" "+s).rstrip())