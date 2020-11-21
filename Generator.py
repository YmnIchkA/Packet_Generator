import scapy


class Generator:
    import log

    def __init__(self):
        self.log.debug('Generator starts')

    def send_tcp(self, ip_header: dict, tcp_header: dict):
        self.log.debug('send_tcp method called!')
        pass

    def send_udp(self, ip_header: dict, udp_header: dict):
        self.log.debug('send_udp method called!')
        pass

    def send_icmp(self, ip_header: dict, icmp_header: dict):
        self.log.debug('send_icmp method called!')
        pass
