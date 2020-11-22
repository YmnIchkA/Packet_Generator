import tkinter
from tkinter import ttk
import packets
from Generator import Generator

'''
[*]button_<> methods:
creates fields and entries for all fields of ip header and <> header

[*]get_<> methods:
this method collects information about ip and <> header
check packet name and if this name already exists packet drops
otherwise creates dict like {name: [ip header, udp header]}
then window destroys and packet sends

get_<>_header methods:
only make get() for all properties for specified class
'''


class Interface:
    import log

    def __init__(self, ):
        self.log.clear()
        self.log.debug('Start interface')
        self.generator = Generator()
        self.window = tkinter.Tk()
        self.window.title('Packet Generator')
        self.saved_packets_combobox = None
        self.packets_list = list()
        self.packets_list_names = list()  # used only for combobox list

    @staticmethod
    def get_ip_header(ip_header):
        ip_header.ihl = ip_header.ihl.get()
        ip_header.tos = ip_header.tos.get()
        ip_header.len = ip_header.len.get()
        ip_header.id = ip_header.id.get()
        ip_header.flags = ip_header.flags.get()
        ip_header.frag = ip_header.frag.get()
        ip_header.ttl = ip_header.ttl.get()
        ip_header.proto = ip_header.proto.get()
        ip_header.chksum = ip_header.chksum.get()
        ip_header.src = ip_header.src.get()
        ip_header.dst = ip_header.dst.get()

    @staticmethod
    def fill_ip_header_in_window(window, ip_packet):
        label = tkinter.Label
        ip_h = label(window, text='IPv4 header')
        ip_h.grid(column=1, row=0, sticky='w')

        #  ***** ihl *****
        ip_ihl = label(window, text='ihl:')
        ip_ihl.grid(column=0, row=1, sticky='w')
        entry_ip_ihl = tkinter.Entry(window, textvariable=ip_packet.ihl)
        entry_ip_ihl.grid(column=1, row=1, padx=5, pady=5, sticky='w')

        #  ***** tos *****
        ip_tos = label(window, text='tos:')
        ip_tos.grid(column=0, row=2, sticky='w')
        entry_ip_tos = tkinter.Entry(window, textvariable=ip_packet.tos)
        entry_ip_tos.grid(column=1, row=2, padx=5, pady=5, sticky='w')

        #  ***** len *****
        ip_len = label(window, text='len:')
        ip_len.grid(column=0, row=3, sticky='w')
        entry_ip_len = tkinter.Entry(window, textvariable=ip_packet.len)
        entry_ip_len.grid(column=1, row=3, padx=5, pady=5, sticky='w')

        #  ***** id *****
        ip_id = label(window, text='id:')
        ip_id.grid(column=0, row=4, sticky='w')
        entry_ip_id = tkinter.Entry(window, textvariable=ip_packet.id)
        entry_ip_id.grid(column=1, row=4, padx=5, pady=5, sticky='w')

        #  ***** flags *****
        ip_flags = label(window, text='flags:')
        ip_flags.grid(column=0, row=5, sticky='w')
        entry_ip_flags = tkinter.Entry(window, textvariable=ip_packet.flags)
        entry_ip_flags.grid(column=1, row=5, padx=5, pady=5, sticky='w')

        #  ***** frag *****
        ip_frag = label(window, text='frag:')
        ip_frag.grid(column=0, row=6, sticky='w')
        entry_ip_frag = tkinter.Entry(window, textvariable=ip_packet.frag)
        entry_ip_frag.grid(column=1, row=6, padx=5, pady=5, sticky='w')

        #  ***** ttl *****
        ip_ttl = label(window, text='ttl:')
        ip_ttl.grid(column=0, row=7, sticky='w')
        entry_ip_ttl = tkinter.Entry(window, textvariable=ip_packet.ttl)
        entry_ip_ttl.grid(column=1, row=7, padx=5, pady=5, sticky='w')

        #  ***** proto *****
        ip_proto = label(window, text='proto:')
        ip_proto.grid(column=0, row=8, sticky='w')
        entry_ip_proto = tkinter.Entry(window, textvariable=ip_packet.proto)
        entry_ip_proto.grid(column=1, row=8, padx=5, pady=5, sticky='w')

        #  ***** chksum *****
        ip_chksum = label(window, text='chksum:')
        ip_chksum.grid(column=0, row=9, sticky='w')
        entry_ip_chksum = tkinter.Entry(window, textvariable=ip_packet.chksum)
        entry_ip_chksum.grid(column=1, row=9, padx=5, pady=5, sticky='w')

        #  ***** src *****
        ip_src = label(window, text='src:')
        ip_src.grid(column=0, row=10, sticky='w')
        entry_ip_src = tkinter.Entry(window, textvariable=ip_packet.src)
        entry_ip_src.grid(column=1, row=10, padx=5, pady=5, sticky='w')

        #  ***** dst *****
        ip_dst = label(window, text='dst:')
        ip_dst.grid(column=0, row=11, sticky='w')
        entry_ip_dst = tkinter.Entry(window, textvariable=ip_packet.dst)
        entry_ip_dst.grid(column=1, row=11, padx=5, pady=5, sticky='w')

    @staticmethod
    def get_tcp_header(tcp_header):
        tcp_header.sport = tcp_header.sport.get()
        tcp_header.dport = tcp_header.dport.get()
        tcp_header.seq = tcp_header.seq.get()
        tcp_header.ack = tcp_header.ack.get()
        tcp_header.dataofs = tcp_header.dataofs.get()
        tcp_header.flags = tcp_header.flags.get()
        tcp_header.window = tcp_header.window.get()
        tcp_header.chksum = tcp_header.chksum.get()
        tcp_header.urgptr = tcp_header.urgptr.get()
        tcp_header.options = tcp_header.options.get()
        tcp_header.data = tcp_header.data.get()
        tcp_header.name = tcp_header.name.get()

    def handle_tcp(self, window, tcp_header, ip_header):
        self.log.debug('[IM]get_tcp method called')
        self.get_tcp_header(tcp_header)
        self.get_ip_header(ip_header)

        if not tcp_header.name:
            self.log.debug(f'(No name)[{ip_header.packet()}, {tcp_header.packet()}]')
            window.destroy()
            self.generator.send_tcp(ip_header.packet(), tcp_header.packet())

        if tcp_header.name in self.packets_list_names:
            self.log.debug(f"Packet with name '{tcp_header.name}' already exists")
            window.destroy()
            return

        packet = {tcp_header.name: [ip_header.packet(), tcp_header.packet()]}
        self.packets_list.append(packet)
        self.packets_list_names.append(tcp_header.name)
        self.saved_packets_combobox['values'] = self.packets_list_names
        self.log.debug(f'packet generated:{tcp_header.name}: [{ip_header.packet()}, {tcp_header.packet()}]')
        window.destroy()
        self.generator.send_udp(ip_header.packet(), tcp_header.packet())

    def button_tcp(self):
        tcp_header = packets.TCPHeader()
        ip_header = packets.IPHeader()
        self.log.debug('[IM] button TCP clicked')
        tcp_window = tkinter.Toplevel(self.window)
        tcp_window.title('TCP packet')
        tcp_window.geometry('480x380+25+25')

        self.fill_ip_header_in_window(tcp_window, ip_header)
        udp_h = tkinter.Label(tcp_window, text='TCP header')
        udp_h.grid(column=4, row=0, sticky='w')

        # ===sport===
        source_port = tkinter.Label(tcp_window, text='Source port:')
        source_port.grid(column=3, row=1, sticky='w')
        entry_source_port = tkinter.Entry(tcp_window, textvariable=tcp_header.sport)
        entry_source_port.grid(column=4, row=1, padx=5, pady=5, sticky='w')

        # ===dport===
        destination_port = tkinter.Label(tcp_window, text='Destination port:')
        destination_port.grid(column=3, row=2, sticky='w')
        entry_destination_port = tkinter.Entry(tcp_window, textvariable=tcp_header.dport)
        entry_destination_port.grid(column=4, row=2, padx=5, pady=5, sticky='w')

        # ===seq===
        seq = tkinter.Label(tcp_window, text='seq:')
        seq.grid(column=3, row=3, sticky='w')
        entry_seq = tkinter.Entry(tcp_window, textvariable=tcp_header.seq)
        entry_seq.grid(column=4, row=3, padx=5, pady=5, sticky='w')

        # ===ack===
        ack = tkinter.Label(tcp_window, text='ack:')
        ack.grid(column=3, row=4, sticky='w')
        entry_ack = tkinter.Entry(tcp_window, textvariable=tcp_header.ack)
        entry_ack.grid(column=4, row=4, padx=5, pady=5, sticky='w')

        # ===dataofs===
        dataofs = tkinter.Label(tcp_window, text='dataofs:')
        dataofs.grid(column=3, row=5, sticky='w')
        entry_dataofs = tkinter.Entry(tcp_window, textvariable=tcp_header.dataofs)
        entry_dataofs.grid(column=4, row=5, padx=5, pady=5, sticky='w')

        # ===flags===
        flags = tkinter.Label(tcp_window, text='flags:')
        flags.grid(column=3, row=6, sticky='w')
        entry_flags = tkinter.Entry(tcp_window, textvariable=tcp_header.flags)
        entry_flags.grid(column=4, row=6, padx=5, pady=5, sticky='w')

        # ===window===
        wndow = tkinter.Label(tcp_window, text='window:')
        wndow.grid(column=3, row=6, sticky='w')
        entry_wndow = tkinter.Entry(tcp_window, textvariable=tcp_header.window)
        entry_wndow.grid(column=4, row=6, padx=5, pady=5, sticky='w')

        # ===chksum===
        chksum = tkinter.Label(tcp_window, text='chksum:')
        chksum.grid(column=3, row=7, sticky='w')
        entry_chksum = tkinter.Entry(tcp_window, textvariable=tcp_header.chksum)
        entry_chksum.grid(column=4, row=7, padx=5, pady=5, sticky='w')

        # ===urgptr===
        urgptr = tkinter.Label(tcp_window, text='urgptr:')
        urgptr.grid(column=3, row=8, sticky='w')
        entry_urgptr = tkinter.Entry(tcp_window, textvariable=tcp_header.urgptr)
        entry_urgptr.grid(column=4, row=8, padx=5, pady=5, sticky='w')

        # ===options===
        options = tkinter.Label(tcp_window, text='options:')
        options.grid(column=3, row=9, sticky='w')
        entry_options = tkinter.Entry(tcp_window, textvariable=tcp_header.options)
        entry_options.grid(column=4, row=9, padx=5, pady=5, sticky='w')

        # ===data===
        data = tkinter.Label(tcp_window, text='Enter your data here:')
        data.grid(column=3, row=10, sticky='w')
        entry_data = tkinter.Entry(tcp_window, textvariable=tcp_header.data)
        entry_data.grid(column=4, row=10, padx=5, pady=5, sticky='w')

        # ===name===
        name = tkinter.Label(tcp_window, text='Name (for saving packet)')
        name.grid(column=3, row=11, sticky='w')
        entry_name = tkinter.Entry(tcp_window, textvariable=tcp_header.name)
        entry_name.grid(column=4, row=11, padx=5, pady=5, sticky='w')

        send_button = tkinter.Button(tcp_window,
                                     text='Send',
                                     command=lambda: self.handle_tcp(tcp_window, tcp_header, ip_header))
        send_button.grid(column=4, row=12, padx=5)
        tcp_window.mainloop()

    @staticmethod
    def get_udp_header(udp_header):
        udp_header.sport = udp_header.sport.get()
        udp_header.dport = udp_header.dport.get()
        udp_header.chksum = udp_header.chksum.get()
        udp_header.len = udp_header.len.get()
        udp_header.data = udp_header.data.get()
        udp_header.name = udp_header.name.get()

    def handle_udp(self, window, udp_header, ip_header):
        self.log.debug('[IM] get_udp method called')
        self.get_udp_header(udp_header)
        self.get_ip_header(ip_header)

        if not udp_header.name:
            self.log.debug(f'(No name)[{ip_header.packet()}, {udp_header.packet()}]')
            window.destroy()
            self.generator.send_udp(ip_header.packet(), udp_header.packet())

        if udp_header.name in self.packets_list_names:
            self.log.debug(f"Packet with name '{udp_header.name}' already exists")
            window.destroy()
            return

        packet = {udp_header.name: [ip_header.packet(), udp_header.packet()]}
        self.packets_list.append(packet)
        self.packets_list_names.append(udp_header.name)
        self.saved_packets_combobox['values'] = self.packets_list_names
        self.log.debug(f'packet generated:{udp_header.name}: [{ip_header.packet()}, {udp_header.packet()}]')
        window.destroy()
        self.generator.send_udp(ip_header.packet(), udp_header.packet())

    def button_udp(self):
        udp_header = packets.UDPHeader()
        ip_header = packets.IPHeader()
        self.log.debug('[IM] button UDP clicked')
        udp_window = tkinter.Toplevel(self.window)
        udp_window.title('UDP packet')
        udp_window.geometry('480x380+25+25')

        self.fill_ip_header_in_window(udp_window, ip_header)
        udp_h = tkinter.Label(udp_window, text='UDP header')
        udp_h.grid(column=4, row=0, sticky='w')

        # ===sport===
        source_port = tkinter.Label(udp_window, text='Source port:')
        source_port.grid(column=3, row=1, sticky='w')
        entry_source_port = tkinter.Entry(udp_window, textvariable=udp_header.sport)
        entry_source_port.grid(column=4, row=1, padx=5, pady=5, sticky='w')

        # ===dport===
        destination_port = tkinter.Label(udp_window, text='Destination port:')
        destination_port.grid(column=3, row=2, sticky='w')
        entry_destination_port = tkinter.Entry(udp_window, textvariable=udp_header.dport)
        entry_destination_port.grid(column=4, row=2, padx=5, pady=5, sticky='w')

        # ===len===
        length = tkinter.Label(udp_window, text='len:')
        length.grid(column=3, row=3, sticky='w')
        entry_len = tkinter.Entry(udp_window, textvariable=udp_header.len)
        entry_len.grid(column=4, row=3, padx=5, pady=5, sticky='w')

        # ===checksum===
        checksum = tkinter.Label(udp_window, text='checksum:')
        checksum.grid(column=3, row=4, sticky='w')
        entry_checksum = tkinter.Entry(udp_window, textvariable=udp_header.chksum)
        entry_checksum.grid(column=4, row=4, padx=5, pady=5, sticky='w')

        # ===data===
        data = tkinter.Label(udp_window, text='Enter your data here:')
        data.grid(column=3, row=5, sticky='w')
        entry_data = tkinter.Entry(udp_window, textvariable=udp_header.data)
        entry_data.grid(column=4, row=5, padx=5, pady=5, sticky='w')

        # ===name===
        name = tkinter.Label(udp_window, text='Name (for saving packet)')
        name.grid(column=3, row=5, sticky='w')
        entry_name = tkinter.Entry(udp_window, textvariable=udp_header.name)
        entry_name.grid(column=4, row=5, padx=5, pady=5, sticky='w')

        send_button = tkinter.Button(udp_window,
                                     text='Send',
                                     command=lambda: self.handle_udp(udp_window, udp_header, ip_header))
        send_button.grid(column=4, row=10, padx=5)
        udp_window.mainloop()

    @staticmethod
    def get_icmp_header(icmp_header):
        icmp_header.type = icmp_header.type.get()
        icmp_header.code = icmp_header.code.get()
        icmp_header.chksum = icmp_header.chksum.get()
        icmp_header.id = icmp_header.id.get()
        icmp_header.seq = icmp_header.seq.get()
        icmp_header.name = icmp_header.name.get()

    def handle_icmp(self, window, icmp_header, ip_header):
        self.log.debug('[IM] get_icmp method called')
        self.get_icmp_header(icmp_header)
        self.get_ip_header(ip_header)

        if not icmp_header.name:
            self.log.debug(f'(No name)[{ip_header.packet()}, {icmp_header.packet()}]')
            window.destroy()
            self.generator.send_udp(ip_header.packet(), icmp_header.packet())

        if icmp_header.name in self.packets_list_names:
            self.log.debug(f"Packet with name '{icmp_header.name}' already exists")
            window.destroy()
            return

        packet = {icmp_header.name: [ip_header, icmp_header]}
        self.packets_list.append(packet)
        self.packets_list_names.append(icmp_header.name)
        self.saved_packets_combobox['values'] = self.packets_list_names
        self.log.debug(f'packet generated:{icmp_header.name}: [{ip_header.packet()}, {icmp_header.packet()}]')
        window.destroy()
        self.generator.send_udp(ip_header.packet(), icmp_header.packet())

    def button_icmp(self):
        icmp_header = packets.ICMPHeader()
        ip_header = packets.IPHeader()
        self.log.debug('[IM] button ICMP clicked')
        icmp_window = tkinter.Toplevel(self.window)
        icmp_window.title('ICMP packet')
        icmp_window.geometry('480x380+25+25')

        self.fill_ip_header_in_window(icmp_window, ip_header)
        udp_h = tkinter.Label(icmp_window, text='ICMP header')
        udp_h.grid(column=4, row=0, sticky='w')

        # ===type===
        type = tkinter.Label(icmp_window, text='Type:')
        type.grid(column=3, row=1, sticky='w')
        entry_type = tkinter.Entry(icmp_window, textvariable=icmp_header.type)
        entry_type.grid(column=4, row=1, padx=5, pady=5, sticky='w')

        # ===code===
        code = tkinter.Label(icmp_window, text='Code:')
        code.grid(column=3, row=2, sticky='w')
        entry_code = tkinter.Entry(icmp_window, textvariable=icmp_header.code)
        entry_code.grid(column=4, row=2, padx=5, pady=5, sticky='w')

        # ===checksum===
        checksum = tkinter.Label(icmp_window, text='checksum:')
        checksum.grid(column=3, row=3, sticky='w')
        entry_checksum = tkinter.Entry(icmp_window, textvariable=icmp_header.chksum)
        entry_checksum.grid(column=4, row=3, padx=5, pady=5, sticky='w')

        # ===id===
        id = tkinter.Label(icmp_window, text='id:')
        id.grid(column=3, row=4, sticky='w')
        entry_id = tkinter.Entry(icmp_window, textvariable=icmp_header.id)
        entry_id.grid(column=4, row=4, padx=5, pady=5, sticky='w')

        # ===name===
        name = tkinter.Label(icmp_window, text='Name (for saving packet)')
        name.grid(column=3, row=5, sticky='w')
        entry_name = tkinter.Entry(icmp_window, textvariable=icmp_header.name)
        entry_name.grid(column=4, row=5, padx=5, pady=5, sticky='w')

        # # ===data===
        # data = tkinter.Label(udp_window, text='Enter your data here:')
        # data.grid(column=3, row=6, sticky='w')
        # entry_data = tkinter.Entry(udp_window, textvariable=udp_header.data)
        # entry_data.grid(column=4, row=6, padx=5, pady=5, sticky='w')

        send_button = tkinter.Button(icmp_window,
                                     text='Send',
                                     command=lambda: self.handle_icmp(icmp_window, icmp_header, ip_header))
        send_button.grid(column=4, row=10, padx=5)
        icmp_window.mainloop()

    def main(self):
        self.log.debug('Start main loop')
        self.window.geometry('300x150+600+200')
        btn_tcp = tkinter.Button(self.window, text="Create TCP ", command=self.button_tcp)
        btn_udp = tkinter.Button(self.window, text="Create UDP ", command=self.button_udp)
        btn_icmp = tkinter.Button(self.window, text="Create ICMP", command=self.button_icmp)
        self.saved_packets_combobox = ttk.Combobox(self.window, textvariable=tkinter.StringVar())

        self.saved_packets_combobox['values'] = ['No packets available']
        self.saved_packets_combobox.grid(column=1, row=0)
        self.saved_packets_combobox.current()

        btn_tcp.grid(column=0, row=0, padx=5, pady=5)
        btn_udp.grid(column=0, row=1, padx=5, pady=5)
        btn_icmp.grid(column=0, row=2, padx=5, pady=5)
        self.window.mainloop()
