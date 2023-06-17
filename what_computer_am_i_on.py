import socket


def main():
    print("Hostname:", get_computer_name())
    print("IP Address:", get_ip_address())


def get_computer_name():
    # Get the hostname of the computer
    return socket.gethostname()


def get_ip_address():
    # Get the IP address of the computer
    hostname = get_computer_name()
    return socket.gethostbyname(hostname)


if __name__ == "__main__":
    main()
