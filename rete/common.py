FIELDS = ['id', 'attr', 'val']

class WME:
    """
    from p.41
    type fields : [1..3] array 형태로 (id ^attr val)의 triple을 나타냄
    type amems : 본 wme가 포함된 alpha memory 의 list
    type tokens : token list
    type n-join-results : list of negative-join-result
    """
    def __init__(self, id, attr, val):
        self.id = id
        self.attr = attr
        self.val = val

class ReteNode:
    """
    type : "beta-memory", "join-node", or "p-node", or other node types
    children : list of ReteNode itself
    parent : ReteNode itself
    """
    def __init__(self, children=None, parent=None):
        self.children = children if children else []
        self.parent = parent

class Token:
    pass

class NegativeJoinResult:
    def __init__(self, owner, wme):
