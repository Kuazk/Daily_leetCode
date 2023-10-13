





def reorderLogFiles(logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        return sorted(logs,key = sortfun)
def sortfun(s):
    _id, rest = s.split(' ', maxsplit=1)

    return (0,rest,_id) if rest[0].isalpha() else (1,)

logs =["a1 9 2 3 1","g2 act car","zo4 4 7","g1 act car","a8 act zoo"]
print(reorderLogFiles(logs))