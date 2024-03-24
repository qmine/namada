import os
from wallet import Wallet


class Namada(object):
    status = "Comming soon..."
    node = ''
    alias = ''

    """docstring for Namada Python package"""
    def __init__(self, node='', *args, **kwargs):
        super(Namada, self).__init__(*args, **kwargs)
        self.node = node
        self.wallet = Wallet(self.node)
        
    # def test(self):
    #     return os.system("namada wallet list")

    # def wallet_derive(self, alias):
    #     self.alias = alias
    #     return os.system(f"namada wallet derive --alias {alias}")

    # def wallet_find(self):
    #     return os.system(f"namada wallet find --alias {self.alias}")