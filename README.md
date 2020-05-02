# up-zonk
up and zonk

## Setting up Test App 

A test app is an Angular 9 + Angular Material 9 web app with nodejs server. The server use tsed project. 

Server
```zsh
cd ./tests/catalog/server
nmp install
nmp start 
```

Client 
```
cd /tests/catalog/client
npm install
npm start
```

### MySQL Database 

1. Create 'catalog' 
2. Run tests/catalog/database/seed.sql script 

It will create 'product' table with two records in it.  

### Prepare a Model

1. Execute in MySQLWorkbench 

```sql
select * from information_schema.columns where 
table_schema = 'catalog' and table_name = 'product'
order by table_name,ordinal_position
```

> Note: SHOW COLUMNS FROM tbl_name needs can be also used but will need more parsing. 

2. Save result to product.json

## Run Generator

Install Python3 (3.8)
Add pystache module 

```zsh
nodemon --exec "python3 " ./src/genie.py ./models/catolog.json ./templates/entity.mustache ./out/entities --ext py,mustache

```

### Development 

Both python scripts and mustache 

Install nodejs

> Using nodemon to watch *.ts and *.mustache files and restart python3
Install nodemon 

```
nmp install nodemon -g
```

run a start.zsh script

```
zsh start.zsh
```


