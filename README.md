# up-zonk

Up and zonk

## Up

Generate code from a JSON models to quickly stand up an Angular UI.

For MySQL JSON table models:

-   TypeORM entities <https://github.com/typeorm/typeorm> for ts.ed framework (https://tsed.io/)
-   TypeScrip interface
-   Angular service
-   Place holders for action, list, details, edit Angular components

Next:

-   Angular Material list, details, edit/create templates
-   support for enhanced models
-   bug fixes for current templates
-   extending testing

Known issues:

-   sometimes throws exception if base out folder does not exists, but finishes correctly.
-   excludes must be specified, not optional, geez.

## Zonk

... zzz ...

## Create Python virtual env

python3 -m venv {workspaceDir}/.env
source {workspaceDir}.env/bin/activate

## Installation

Install Python3 (3.8)

Add pystache module (<https://github.com/defunkt/pystache>)
Add inflect module

```bash
pip install inflect
pip install pystache
pystache-test
```

## Run Generator

```zsh
python3 ./src/genie.py product
```

## Configuration

Main configuration file to locate meta-model, specify templates base folder and output base folder.

up-zonk.yaml

A sample meta-model configuration:

.models/product.yaml

A sample original MySQL models:

models/original/product.json

A sample of enhanced model (coming soon):

models/enhanced/product.json

## Development

Recommended extensions for VS Code;

<https://github.com/Microsoft/vscode-python>

<https://github.com/dnwhte/vscode-mustache-syntax-highlighting>

<https://github.com/MicrosoftDocs/intellicode>

> make sure you have Python3 correctly configured on Mac, see the docs.

### Install nodemon

> Using nodemon to watch _.ts, _.mustache, _.yaml and _.json files and restart python3 if changes detected. Speeds up development.

Install nodejs

Install nodemon

```bash
npm install nodemon -g
```

Run nodemon

```bash
nodemon --exec "python3 " ./src/genie.py product. --ext py,mustache,yaml,json
```

or run a script

```zsh
zsh start.zsh
```

## Test App

A test app is an Angular 9 + Angular Material 9 web app. It runs on a nodejs server. The server uses Ts.ED project (<https://tsed.io/>).

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
npm install
npm start
```

open another terminal window

Client

```bash
cd tests/catalog/client
npm install
npm start
```

Open browser

<http://localhost:8080/dashboard>

### Create MySQL server

Get Docker up and running

```bash
docker pull mysql
docker run --name mysql1 -e MYSQL_ROOT_HOST=% -p 3306:3306 -e MYSQL_ROOT_PASSWORD=pass -d mysql:latest
```

### Prepare a Model

1. Execute in MySQLWorkbench

    ```sql
    select * from information_schema.columns where
    table_schema = 'catalog' and table_name = 'product'
    order by table_name,ordinal_position
    ```

    > Note: SHOW COLUMNS FROM tbl_name can also be used, however, it lucks details and will need additional parsing effort.

2. Save result to product.json
3. Place product.json to models/original
