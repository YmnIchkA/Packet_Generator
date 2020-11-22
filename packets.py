from tkinter import StringVar


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


class UDPHeader:

    def __init__(self) -> None:
        self.sport = StringVar()
        self.dport = StringVar()
        self.len = StringVar()
        self.chksum = StringVar()
        self.name = StringVar()
        self.data = StringVar()

    def packet(self):
        return {'source port': self.sport,
                'destination port': self.dport,
                'len': self.len,
                'chksum': self.chksum,
                'data': self.data}


class TCPHeader:

    def __init__(self) -> None:
        self.sport = StringVar()
        self.dport = StringVar()
        self.seq = StringVar()
        self.ack = StringVar()
        self.dataofs = StringVar()
        self.flags = StringVar()
        self.window = StringVar()
        self.chksum = StringVar()
        self.urgptr = StringVar()
        self.options = StringVar()
        self.data = StringVar()
        self.name = StringVar()

    def packet(self):
        return {'sport': self.sport,
                'dport': self.dport,
                'seq': self.seq,
                'ack': self.ack,
                'dataofs': self.dataofs,
                'flags': self.flags,
                'window': self.window,
                'chksum': self.chksum,
                'urgptr': self.urgptr,
                'options': self.options}


class ICMPHeader:
    def __init__(self) -> None:
        self.type = StringVar()
        self.code = StringVar()
        self.chksum = StringVar()
        self.id = StringVar()
        self.seq = StringVar()
        self.name = StringVar()

    def packet(self):
        return{'type': self.type,
               'code': self.code,
               'chksum': self.chksum,
               'id': self.id,
               'seq': self.seq}

