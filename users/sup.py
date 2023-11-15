from ctypes import windll
import pyautogui, time, random, socket

def run_elevated_powershell_command(command):
    try:
        # ShellExecute関数を呼び出して管理者権限でPowerShellを起動
        windll.shell32.ShellExecuteW(
            None,
            "runas",
            "powershell",
            f"-Command \"{command}\"",
            None,
            1  # SW_SHOWNORMAL
        )

    except Exception as e:
        print(f"エラー: {e}")


def change_ip_address():
    ip_address = random.randint(1, 254)
    hostname_before = socket.gethostname()
    past_ip_address = socket.gethostbyname(hostname_before)

    # 実行したいコマンドを指定
    command_change_ip = f"New-NetIPAddress -InterfaceAlias Wi-Fi -AddressFamily IPv4 -IPAddress 172.29.191.{ip_address} -PrefixLength 24 -DefaultGateway 172.29.191.254"
    command_dhcp = 'netsh interface ip set address name="Wi-Fi" source=dhcp'

    # 管理者権限でPowerShellでコマンドを実行
    run_elevated_powershell_command(command_change_ip)
    print("changed ip address")

    time.sleep(50)

    run_elevated_powershell_command(command_dhcp)

    time.sleep(30)
    hostname_after = socket.gethostname()
    present_ip_address = socket.gethostbyname(hostname_after)
    print(f"ip address changed from {past_ip_address} to {present_ip_address}")


if __name__ == "__main__":
    change_ip_address()