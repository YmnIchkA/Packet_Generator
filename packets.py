from tkinter import StringVar, IntVar


class IPHeader:

    def __init__(self) -> None:
        self.version = 4
        self.ihl = IntVar(value=0)
        self.tos = IntVar(value=0)
        self.len = IntVar(value=0)
        self.id = IntVar(value=0)
        self.flags = StringVar(value='0')
        self.frag = IntVar(value=0)
        self.ttl = IntVar(value=0)
        self.proto = StringVar(value='0')
        self.chksum = IntVar(value=0)
        self.src = StringVar(value='0')
        self.dst = StringVar(value='0')

    def packet(self):
        class_dict = self.__dict__
        return_dict = dict()
        for key in class_dict:
            if class_dict[key] == 0 or class_dict[key] == '0':
                continue
            return_dict[key] = class_dict[key]

        return return_dict


class UDPHeader:

    def __init__(self) -> None:
        self.sport = IntVar(value=0)
        self.dport = IntVar(value=0)
        self.len = IntVar(value=0)
        self.chksum = IntVar(value=0)
        self.name = StringVar(value='0')
        self.data = StringVar(value='0')

    def packet(self):
        class_dict = self.__dict__
        return_dict = dict()
        for key in class_dict:
            if class_dict[key] == 0 or class_dict[key] == '0':
                continue
            return_dict[key] = class_dict[key]

        return return_dict


class TCPHeader:

    def __init__(self) -> None:
        self.sport = IntVar(value=0)
        self.dport = IntVar(value=0)
        self.seq = IntVar(value=0)
        self.ack = IntVar(value=0)
        self.dataofs = IntVar(value=0)
        self.flags = StringVar(value='0')
        self.window = IntVar(value=0)
        self.chksum = IntVar(value=0)
        self.urgptr = IntVar(value=0)
        self.options = StringVar(value='0')
        self.data = StringVar(value='0')
        self.name = StringVar(value='0')

    def packet(self):
        class_dict = self.__dict__
        return_dict = dict()
        for key in class_dict:
            if class_dict[key] == 0 or class_dict[key] == '0':
                continue
            return_dict[key] = class_dict[key]

        return return_dict


class ICMPHeader:
    def __init__(self) -> None:
        self.type = StringVar(value='0')
        self.code = IntVar(value=0)
        self.chksum = IntVar(value=0)
        self.id = IntVar(value=0)
        self.seq = IntVar(value=0)
        self.name = StringVar(value='0')

    def packet(self):
        class_dict = self.__dict__
        return_dict = dict()
        for key in class_dict:
            if class_dict[key] == 0 or class_dict[key] == '0':
                continue
            return_dict[key] = class_dict[key]

        return return_dict
