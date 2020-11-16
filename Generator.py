import scapy


class Generator:
    import log

    def __init__(self):
        self.log.debug('Generator starts')

    def send_tcp(self, ip_header: dict, tcp_header: dict):
        pass

    def send_udp(self, ip_header: dict, udp_header: dict):
        pass

    def send_icmp(self, ip_header: dict, icmp_header: dict):
        pass
