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
        --base-dir <base-dir>  The base directory is where the nodes, client and wallet configuration and state is stored. This value can also be set via `NAMADA_BASE_DIR` environment variable, but the argument takes precedence, if specified. Defaults to `$XDG_DATA_HOME/namada` (`$HOME/.local/share/namada` where `XDG_DATA_HOME` is unset) on Unix,`$HOME/Library/Application Support/Namada` on Mac,and `%AppData%\Namada` on Windows.
        --shielded             List keys / addresses of the shielded pool only.
        --keys                 List keys only.
        --wasm-dir <wasm-dir>  Directory with built WASM validity predicates, transactions. This value can also be set via `NAMADA_WASM_DIR` environment variable, but the argument takes precedence, if specified.
        --addr                 List addresses only.
        --pre-genesis          Dispatch pre-genesis specific logic.
        --decrypt              Decrypt keys that are encrypted.
        --unsafe-show-secret   UNSAFE: Print the secret / spending keys.
        """
        return os.system("namada wallet list")

