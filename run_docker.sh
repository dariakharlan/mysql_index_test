#!/usr/bin/env bash

docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=test -d -p 3306:3306  mysql
