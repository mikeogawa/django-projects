from filters import BaseFilterSet, StringFilter, IntFilter, IntListFilter

class GetObj:
    
    def __init__(self, value):
        self.value = value

    def get(self, k):
        v = self.value.get(k)
        if isinstance(v, list):
            return v[-1]
        else:
            return v
    
    def getlist(self, k):
        v = self.value.get(k)
        if isinstance(v, list):
            return v
        elif v is not None:
            return [v]

class Request:
    def __init__(self, data):
        self.GET = GetObj(data)

class CustomFilterSet(BaseFilterSet):
    a = StringFilter()
    b = IntFilter()
    c = IntListFilter(required=False)

class CustomFilterSet2(BaseFilterSet):
    a = StringFilter()
    b = IntFilter()
    c = IntListFilter(required=True)

if __name__=="__main__":
    r=Request({"a":"string","b":3})
    c=CustomFilterSet(r)
    print(c.data)

    r=Request({"a":"string","b":3, "c": [1,2,3,4,5]})
    c=CustomFilterSet(r)
    print(c.data)
    
    r=Request({"a":"string","b":3, "c": 1})
    c=CustomFilterSet(r)
    print(c.data)

    try:
        r=Request({"a":"string","b":3})
        c=CustomFilterSet2(r)
    except Exception as e:
        print(e)

