# GSenha CLI

CLI for [gsenha-api](https://github.com/globocom/gsenha-api) using [gsenha-python](https://github.com/globocom/gsenha-python)

## Install for development

    make install

## Make binary

    make dist

Now **dist/gsenha** binary will me available.

## Usage

    gsenha get --folder folder --name name1 --name name2 ... ---prefix GSENHA_

This will return an export for each variable as uppercase as follows:

    export GSENHA\_NAME1\_DESCRIPTION='value1'
    export GSENHA\_NAME2\_DESCRIPTION='value2'

Using Bash you can export variables using:

    command_output=$(gsenha get --folder folder --name name1 --name name2 ... ---prefix GSENHA_)
    eval "$(command_output)"

### Need some enviroment variables:

* GSENHA_ENDPOINT: Endpoint for [gsenha-api](https://github.com/globocom/gsenha-api)
* GSENHA_USER: User for [gsenha-api](https://github.com/globocom/gsenha-api)
* GSENHA_PASS: Password for [gsenha-api](https://github.com/globocom/gsenha-api)
* GSENHA_KEY: User's private key for [gsenha-api](https://github.com/globocom/gsenha-api)
* GSENHA\_KEY\_PATH: User's private key path for [gsenha-api](https://github.com/globocom/gsenha-api)