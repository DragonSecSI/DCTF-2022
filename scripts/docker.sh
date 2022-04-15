#!/bin/bash

set -x

dockerize() {
	folder="challs/$1"
	name="dctfint.azurecr.io/challs/$2:latest"
	pushd $folder
	docker build -t $name . &&
	docker push $name
	popd
}

# Pwn
dockerize "codechainz" "codechainz"
dockerize "key_recovery" "key-recovery"
dockerize "macdonalds-1" "macdonalds-1"
dockerize "macdonalds-2" "macdonalds-2"
dockerize "snailtime" "snailtime"
dockerize "vmstation" "vmstation"
dockerize "maze" "maze"
dockerize "dragons_lair" "dragons-lair"
dockerize "correcthorsebatterystaple" "correcthorsebatterystaple"
dockerize "safe_space" "safespace"
dockerize "phonebook" "phonebook"
dockerize "shitty_tpm" "shitty-tpm"
dockerize "secure_kernel" "secure-kernel"
dockerize "algebraic" "algebraic"

# Web
dockerize "eulers_license" "eulers-license"
dockerize "book_store" "book-store"

# Web + DB
dockerize "sqltutor" "sqltutor"
