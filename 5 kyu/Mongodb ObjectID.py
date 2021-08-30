from datetime import datetime
dict={j:i for i,j in enumerate("0123456789abcdef")}
class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        if (not (isinstance(s, str))) or len(s)!=24 or any(i for i in s if i not in dict):
            return False
        return True
    @classmethod
    def get_timestamp(cls, s):
        if not cls.is_valid(s):
            return False
        return datetime.utcfromtimestamp(sum(dict[j]*(16**(7-i)) for i,j in enumerate(s[:8])))