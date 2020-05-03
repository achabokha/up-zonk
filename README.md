# up-zonk
up and zonk

## Up

Generate code from a JSON model to quickly stand up your Angular UI. 


- From MySQL 
    - TypeORM entities
    - (coming soon) Angular Material list, details, edit
    - (coming seen) TypeScrip model class
    - (coming seen) Angular service

## Zonk

... zzz ...

## Run Generator

Install Python3 (3.8)

Add pystache module 

Run: 

```zsh
python3 ./src/genie.py ./models/product.json ./templates/entity.mustache ./out/entities
```

## Development 

Recommended extensions for VS Code;

https://github.com/Microsoft/vscode-python

https://github.com/dnwhte/vscode-mustache-syntax-highlighting


Install nodemon

> Using nodemon to watch *.ts and *.mustache files and restart python3 if changes detected.

Install nodejs

Install nodemon 

```
nmp install nodemon -g
```

Run nodemon

```
nodemon --exec "python3 " ./src/genie.py ./models/product.json ./templates/entity.mustache ./out/entities --ext py,mustache
```
or run a script

```
zsh start.zsh
```

## Test App 

A test app is an Angular 9 + Angular Material 9 web app. It runs on a nodejs server. The server uses Ts.ED project (https://tsed.io/). 

./tests/catalog

### MySQL Database 

1. Create 'catalog' 
2. Run tests/catalog/database/seed.sql script 

It will create 'product' table with two records in it.  

### Run the App

open a terminal window

Server
```zsh
cd ./tests/catalog/server
nmp install
nmp start 
```

open another terminal window

Client 
```
cd /tests/catalog/client
npm install
npm start
```

Open browser 

http://localhost:8080/dashboard


### Prepare a Model

1. Execute in MySQLWorkbench 

```sql
select * from information_schema.columns where 
table_schema = 'catalog' and table_name = 'product'
order by table_name,ordinal_position
```

> Note: SHOW COLUMNS FROM tbl_name can also be used, however, it will need additional parsing effort.

2. Save result to product.json
