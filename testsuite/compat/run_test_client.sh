#!/bin/bash
# Copyright (c) The Libra Core Contributors
# SPDX-License-Identifier: Apache-2.0

# Wrapper around simple pylibra test scripts
# Accept COMPAT_CLUSTER environment variable to select which cluster to use for testing

set -euo pipefail
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [ -z "$COMPAT_CLUSTER" ]; then
    echo "Please specify COMPAT_CLUSTER variable"
    exit 1
fi

compat_cluster=$COMPAT_CLUSTER

# for sanity testing against current testnet
if [ "$compat_cluster" = "prod" ]; then
    export FAUCET_URL="http://faucet.testnet.libra.org"
    export JSON_RPC_URL="https://client.testnet.libra.org"
else
    export FAUCET_URL="http://faucet.$compat_cluster.aws.hlw3truzy4ls.com"
    export JSON_RPC_URL="http://client.$compat_cluster.aws.hlw3truzy4ls.com"
fi


pipenv run python3 setup.py pytest --addopts="$DIR/compat_tests $@"
