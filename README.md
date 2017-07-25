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

    export GSENHA_NAME1_DESCRIPTION='value1'
    export GSENHA_NAME2_DESCRIPTION='value2'

Using Bash you can export variables using:

    command_output=$(gsenha get --folder folder --name name1 --name name2 ... ---prefix GSENHA_)
    eval "$(command_output)"

We did a [function example](https://gist.github.com/dmvieira/0b46b2ba61c8541349e9d106e88bbbe8) for it. 

### Need some enviroment variables:

* GSENHA_ENDPOINT: Endpoint for [gsenha-api](https://github.com/globocom/gsenha-api)
* GSENHA_USER: User for [gsenha-api](https://github.com/globocom/gsenha-api)
* GSENHA_PASS: Password for [gsenha-api](https://github.com/globocom/gsenha-api)
* GSENHA_KEY: User's private key for [gsenha-api](https://github.com/globocom/gsenha-api)
* GSENHA\_KEY\_PATH: User's private key path for [gsenha-api](https://github.com/globocom/gsenha-api)