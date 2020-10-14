from tkinter import StringVar, IntVar

class IPHeader:

    def __init__(self) -> None:
        self.version = None
        self.ihl = None
        self.tos = None
        self.len = None
        self.id = None
        self.flags = None
        self.ttl = None
        self.proto = None

        self.data = None


class UDPPacket:

    def __init__(self) -> None:
        self.src_port = IntVar()
        self.dst_port = IntVar()
        self.length = IntVar()
        self.checksum = IntVar()
        self.src_ip = StringVar()
        self.dst_ip = StringVar()
        self.name = StringVar()
        self.data = StringVar()

    def packet(self):
        return {'source port': self.src_port,
                'destination port': self.dst_port,
                'source IP': self.src_ip,
                'destination IP': self.dst_ip,
                'length': self.length,
                'checksum': self.checksum,
                'data': self.data}

    def packet_named(self):
        return {'name': self.name,
                'source port': self.src_port,
                'destination port': self.dst_port,
                'source IP': self.src_ip,
                'destination IP': self.dst_ip,
                'length': self.length,
                'checksum': self.checksum,
                'data': self.data}
