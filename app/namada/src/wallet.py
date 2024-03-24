import pexpect

class Wallet(object):
    """docstring for Wallet"""
    def __init__(self, rpc='', *args, **kwargs):
        super(Wallet, self).__init__(*args, **kwargs)
        self.rpc = rpc

    def list(self):
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
        command = 'namada wallet list'
        child = pexpect.spawn(command, encoding='utf-8')
        child.logfile_read = sys.stdout
        # child.expect('Enter your decryption password:')
        # child.sendline(settings.ACCOUNT_PASSWORD)
        return child.before

