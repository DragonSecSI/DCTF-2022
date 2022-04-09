#!/bin/bash

set -x

dockerize() {
	folder="challs/$1"
	name="dctfsi.azurecr.io/challs/$2:latest"
	pushd $folder
	docker build -t $name . &&
	docker push $name
	popd
}

# Pwn
dockerize "printf" "printf"
dockerize "where_is_my_flag" "where-is-my-flag"
dockerize "try_harder" "try-harder"
dockerize "codechainz" "codechainz"
dockerize "correcthorsebatterystaple" "correct-horse-battery-staple"
dockerize "padawan" "padawan"

# Web
dockerize "eulers_license" "eulers-license"
dockerize "path" "path"
dockerize "rockjwt" "rockjwt"
dockerize "lolcode_web" "lolcode"

# Web + DB
dockerize "web_course" "web-course"
