

class ConstantTestNode:
    """
    Ref from p.14
    field-to-test : "identifier", "attribute", "value", or "no-test"
    output-memory : alpha-memory or nil
    children : list of constant-test-node itself (can be empty)
    """
    def __init__(self, field_to_test=None, output_mem=None, field_must_equal=None, children=None):
        self.field_to_test = field_to_test
        self.output_mem=output_mem
        self.field_must_equal=field_must_equal
        self.children=children if children else []

    def activate(self, wme):
        if self.field_to_test != 'no-test':
            v=getattr(wme, self.field_to_test) ## Q. wme.~~ 대신 getattr를 쓰는 이유는?
            if v != self.field_must_equal:
                return False
        if self.output_mem:
            self.output_mem.activate(wme)
        for child in self.children:
            child.activate(wme)

class AlphaMemory:
    """
    Ref from p.21
    items : list of WME
    successors : list of rete-node(attached join nodes)
    """
    def __init__(self, items=None, successors=None):
        self.items = items if items else []
        self.successors = successors if successors else []

    def activate(self, wme):
        if wme in self.items: ## Q. 단순히 in 으로 검색하는것이 젤 빠른가?
            return
        self.items.append(wme) ## Q. 논문에서는 head에 넣는다고 했는데, append는 다르지않은가?
        ## Q. GNaive 코드에서는 여기서 wme에 해당 wme가 어떤 alpha memory 에 들어가는지를 list로 저장하도록 하고 있다. 왜? 쓸모있는가?
        for child in self.successors: ##Q. GNaive 코드에서는 여기서 reversed 된 순서로 하도록 했다. 왜 아래쪽부터 하는게 좋은가?
            child.activate_from_right(wme)

