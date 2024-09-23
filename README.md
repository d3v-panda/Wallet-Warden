# Wallet Warden

A simple Python script that identifies duplicate wallet addresses from a list.

## Overview

Wallet Warden uses Python's `collections.Counter` to efficiently find and list duplicate wallet addresses. It is designed to handle large datasets and provides accurate results.

## Author

[PANDA](https://github.com/d3v-panda)  
Role: Software Developer with a focus on data processing and automation.

## Features

- Efficiently counts occurrences of addresses.
- Identifies duplicates in a clear and concise manner.
- Easy to customize and extend.
- No external libraries required (uses standard library).

## Usage/Examples

Add your addresses to the addresses list in warden.py:

```
addresses = [
    "wallet_address_1",
    "wallet_address_2",
    "wallet_address_1",
    "wallet_address_3",
    "wallet_address_2"
]
```

Run the script:

```
python warden.py
```

After running the script, it will output:
```
Duplicates found: ['wallet_address_1', 'wallet_address_2']

```