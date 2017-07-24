import os
import re
import click
from gsenha import PasswordManager

EXPORT_KEYS = re.compile(r"[^a-zA-Z1-9_]+")

def validate_env(*envs_name):
    for env_name in envs_name:
        if os.environ.get(env_name):
            return True    
    click.echo("{env} not set, please export {env}".format(env=" or ".join(envs_name)), err=True)
    return False

@click.group()
def password():
    pass

@password.command()
@click.option('--folder', '-f', help='Number of greetings.', required=True)
@click.option('--name', '-n', help='Name of password', multiple=True, required=True)
@click.option('--prefix', '-p', help='Prefix for exports', default="GSENHA_")
def get(folder, name, prefix):
    export_string = ''
    passwd = PM.get_passwords(folder, *name)
    for p in passwd:
        export_string += '\n'                
        export_string += '#'*20        
        export_string += ' Keys for {name} \n\n'.format(name=p)
        for key in passwd[p]:
            key_name = EXPORT_KEYS.sub('', '{p}_{key}'.format(p=p.upper(), key=key.upper()))
            export_string += 'export {prefix}{key}=\'{value}\' \n'.format(prefix=prefix, key=key_name, value=passwd[p][key])
    click.echo(export_string)

gsenha = click.CommandCollection(sources=[password])

if __name__ == '__main__':
    if validate_env('GSENHA_ENDPOINT') and validate_env('GSENHA_USER') and validate_env('GSENHA_PASS') and validate_env('GSENHA_KEY', 'GSENHA_KEY_PATH'):
        PM = PasswordManager()
        gsenha()    
    else:
        exit(1)
