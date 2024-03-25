# Python package for Namada
A package for Namada.

## Install
```sh
pip install namada
```

## How to use
_After installing the package use following import:_ <br>
```sh
from namada import Namada
client = Namada()
```

## Blocks:
```sh
from namada import Namada
client = Namada()
client.get_latest_block()
client.get_block_height(height)
client.get_block_height_transactions(height)
client.get_block_height_signatures(height)
client.get_block_list_records(records)
client.get_block_list_records_to_block(records, to_block)
```

## Transactions:
```sh
from namada import Namada
client = Namada()
client.get_latest_tx()
client.get_tx_hash(tx_hash)
client.get_tx_list_records(records)
client.get_tx_list_records_to_block(records, to_block)
```

## Validators:
```sh
from namada import Namada
client = Namada()
client.get_validator_list()
client.get_validator_address(address)
client.get_validator_latest_block(address)
client.get_validator_latest_signatures(address)
```