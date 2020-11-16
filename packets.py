from tkinter import StringVar, IntVar


class IPHeader:

    def __init__(self) -> None:
        self.version = 4
        self.ihl = StringVar()
        self.tos = StringVar()
        self.len = StringVar()
        self.id = StringVar()
        self.flags = StringVar()
        self.frag = StringVar()
        self.ttl = StringVar()
        self.proto = StringVar()
        self.chksum = StringVar()
        self.src = StringVar()
        self.dst = StringVar()

    def packet(self):
        return {'version': self.version,
                'ihl': self.ihl,
                'tos': self.tos,
                'len': self.len,
                'id': self.id,
                'flags': self.flags,
                'frag': self.frag,
                'ttl': self.ttl,
                'proto': self.proto,
                'chksum': self.chksum,
                'src': self.src,
                'dst': self.dst}


class UDPPacket:

    def __init__(self) -> None:
        self.src_port = StringVar()
        self.dst_port = StringVar()
        self.length = StringVar()
        self.checksum = StringVar()
        self.name = StringVar()
        self.data = StringVar()

    def packet(self):
        return {'name': self.name,
                'source port': self.src_port,
                'destination port': self.dst_port,
                'length': self.length,
                'checksum': self.checksum,
                'data': self.data}


class TCPPacket:

    def __init__(self) -> None:
        self.src_port = IntVar()
        self.dst_port = IntVar()
        self.length = IntVar()
        self.checksum = IntVar()
        self.src_ip = StringVar()
        self.dst_ip = StringVar()
        self.name = StringVar()
        self.data = StringVar()
        self.ack_number = IntVar()
        self.sequence = IntVar()

    def packet(self):
        return {'name': self.name,
                'source port': self.src_port,
                'destination port': self.dst_port,
                'source IP': self.src_ip,
                'destination IP': self.dst_ip,
                'ack_number': self.ack_number,
                'length': self.length,
                'checksum': self.checksum,
                'data': self.data}

class ICMPPacket:
    pass

