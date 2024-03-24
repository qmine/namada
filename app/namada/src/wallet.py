import os

class Wallet(object):
    """docstring for Wallet"""
    def __init__(self, node='', *args, **kwargs):
        super(Wallet, self).__init__(*args, **kwargs)
        self.node = node

    def list():
        """
        --chain-id <chain-id>  The chain ID.
        --transparent          List transparent keys / addresses only.
        --base-dir <base-dir>  The base directory is where the nodes, client and wallet configuration and state is stored.
        --shielded             List keys / addresses of the shielded pool only.
        --keys                 List keys only.
        --wasm-dir <wasm-dir>  Directory with built WASM validity predicates, transactions.
        --addr                 List addresses only.
        --pre-genesis          Dispatch pre-genesis specific logic.
        --decrypt              Decrypt keys that are encrypted.
        --unsafe-show-secret   UNSAFE: Print the secret / spending keys.
        """
        return os.system("namada wallet list")

