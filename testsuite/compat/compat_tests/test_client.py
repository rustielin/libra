#!/usr/bin/env python3
# Copyright (c) The Libra Core Contributors
# SPDX-License-Identifier: Apache-2.0
#
# A test client for CompatNet that given JSON RPC and Faucet URLs, runs
# a simple test workload against the cluster.
#
# For example:
# FAUCET_URL=http://faucet.compat-0.aws.hlw3truzy4ls.com
# JSON_RPC_URL=http://client.compat-0.aws.hlw3truzy4ls.com
#

import sys
import time
from secrets import token_bytes
from pylibra import AccountKeyUtils
from . import API, mint_and_wait

def test_mint() -> None:

    private_key_hex: str = token_bytes(32).hex()
    private_key_bytes: bytes = bytes.fromhex(private_key_hex)
    addr_hex: str = AccountKeyUtils.from_private_key(private_key_bytes).address.hex()
    authkey_hex: str = AccountKeyUtils.from_private_key(private_key_bytes).authentication_key.hex()

    print(f"Private key at {private_key_hex}")
    print(f"Address at {addr_hex}")

    mint_amount = 1_000_000

    account = API.getAccount(addr_hex)
    if not account:
        mint_and_wait(authkey_hex, mint_amount, "LBR")
        account = API.getAccount(addr_hex)
        if not account:
            raise Exception(f"Could not create vasp account for auth key {authkey_hex}")
        print(f"Minted account balance: {account.balances}")
        assert account.balances['LBR'] == mint_amount
