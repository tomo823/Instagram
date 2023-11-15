import click
from ctypes import windll

@click.command()
@click.argument("mode", type=click.Choice(["static", "dhcp"], case_sensitive=False))
@click.argument("filename", type=click.Path(exists=True))
def runas(mode, filename):
    """
    IPv4設定変更スクリプトを管理者権限で実行する

    {static|dhcp}: 固定IP設定とするかDHCP設定とするか

    FILENAME: IP設定がかかれたymlファイル。DHCPの場合はインターフェース名のみ読み取る
    """
    _shell = windll.shell32.ShellExecuteW
    print("Run as administrator...")

    return _shell(
        None,
        "runas",
        "python",
        f"_change_cfg.py {mode} {filename}",
        None,
        0,
    )

if __name__ == "__main__":
    runas()