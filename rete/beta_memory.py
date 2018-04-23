from rete.common import ReteNode, Token

class BetaMemory(ReteNode):
    """
    p.22~23
    """

    def __init__(self, children=None, parent=None, items=None):
        """
        :param children:
        :param parent:
        :param items: list (list of tokens)
        """
        super(BetaMemory, self).__init__(children=children, parent=parent)
        self.node_type='beta-memory'
        self.items=items if items else []

    def activate_from_left(self, token, wme):
        """
        :param token:
        :param wme:
        :return:
        """
        new_token = Token(token, wme, node=self)
        self.items.append(new_token)
        for child in self.children:
            child.activate_from_left(new_token)