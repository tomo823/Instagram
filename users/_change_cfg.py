import subprocess
import sys
import click
from lib.config import Config

CMD_PRE = ["netsh", "interface", "ipv4", "set", "address"]

@click.group()
def cli():
    pass

@cli.command()
@click.argument("filename", type=click.Path(exists=True))
def static(filename):
    """
    change ipconfig to static address

    FILENAME: config yaml file of ipconfig
    """
    cfg = Config.load_yaml(filename)
    cmd = CMD_PRE + [f'"{cfg.name}"', "static", cfg.address, cfg.netmask]
    if cfg.gateway is not None and cfg.gateway != "":
        cmd.append(cfg.gateway)
    if cfg.metric is not None and cfg.metric != "":
        cmd.append(cfg.metric)
    print(f"Run command: {' '.join(cmd)}")

    cp = subprocess.run(cmd, capture_output=True, text=True)
    print(f"{cp.stdout}", file=sys.stdout)
    print(f"{cp.stderr}", file=sys.stderr)


@cli.command()
@click.argument("filename", type=click.Path(exists=True))
def dhcp(filename):
    """
    change ipconfig to dhcp address

    FILENAME: config yaml file of ipconfig, use only interface name
    """
    cfg = Config.load_yaml(filename)
    cmd = CMD_PRE + [f'"{cfg.name}"', "dhcp"]
    print(f"Run command: {' '.join(cmd)}")

    cp = subprocess.run(cmd, capture_output=True, text=True)
    print(f"{cp.stdout}", file=sys.stdout)
    print(f"{cp.stderr}", file=sys.stderr)


if __name__ == "__main__":
    cli()