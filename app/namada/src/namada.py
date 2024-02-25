class Namada(object):
    """docstring for Namada Python package"""
    def __init__(self, node, *args, **kwargs):
        super(Namada, self).__init__(*args, **kwargs)
        self.node = node
        self.status = "Comming soon..."
        print(self.status)
        