#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


source ${SCRIPT_DIR}/bin/activate;
${SCRIPT_DIR}/version.py $1


deactivate

