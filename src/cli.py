import os
import click
from gsenha import PasswordManager

def validate_env(*envs_name):
    for env_name in envs_name:
        if os.environ.get(env_name):
            return True    
    click.echo("{env} not set, please export {env}".format(env=" or ".join(envs_name)))
    return False

@click.group()
def password():
    pass

@password.command()
@click.option('--folder', '-f', help='Number of greetings.', required=True)
@click.option('--name', '-n', help='Name of passwords', multiple=True, required=True)
def get(folder, name):
    passwd = PM.get_passwords(folder, *name)
    click.echo(passwd)

gsenha = click.CommandCollection(sources=[password])

if __name__ == '__main__':
    if validate_env('GSENHA_ENDPOINT') and validate_env('GSENHA_USER') and validate_env('GSENHA_PASS') and validate_env('GSENHA_KEY', 'GSENHA_KEY_PATH'):
        PM = PasswordManager()
        gsenha()    
    else:
        exit(1)