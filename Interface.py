import tkinter
from tkinter import ttk
import packets
from Generator import Generator


class Interface:
    import log

    def __init__(self,):
        self.log.clear()
        self.log.debug('Start interface')
        self.generator = Generator()
        self.window = tkinter.Tk()
        self.window.title('Packet Generator')
        self.saved_packets_combobox = None
        self.packets_list = list()
        self.packets_list_names = list()

    @staticmethod
    def get_udp_dict(udp_packet):
        udp_packet.src_port = udp_packet.src_port.get()
        udp_packet.dst_port = udp_packet.dst_port.get()
        udp_packet.checksum = udp_packet.checksum.get()
        udp_packet.length = udp_packet.length.get()
        udp_packet.data = udp_packet.data.get()

    @staticmethod
    def get_ip_dict(ip_header):
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
    def get_tcp_packet(tcp_packet):
        pass

    def button_tcp(self):
        self.log.debug('Button TCP clicked')

    def get_udp(self, window, udp_packet, ip_header):
        self.log.debug('get_udp method called')
        self.get_udp_dict(udp_packet)
        self.get_ip_dict(ip_header)

        #  TODO fix name check
        udp_packet.name = udp_packet.name.get()
        if udp_packet.name in self.packets_list:
            self.log.debug(f'Packet with name {udp_packet.name} already exists')
            window.destroy()
            return

        packet = {udp_packet.name: [ip_header, udp_packet]}
        self.packets_list.append(packet)
        self.packets_list_names.append(udp_packet.name)
        self.saved_packets_combobox['values'] = self.packets_list_names
        self.log.debug(f'udp_header == {udp_packet.packet()}\nip_header == {ip_header.packet()}')
        window.destroy()

    def button_udp(self):
        udp_packet = packets.UDPPacket()
        ip_header = packets.IPHeader()
        self.log.debug('Button UDP clicked')
        udp_window = tkinter.Toplevel(self.window)
        udp_window.title('UDP packet')
        udp_window.geometry('700x450+25+25')

        self.fill_ip_header_in_window(udp_window, ip_header)
        udp_h = tkinter.Label(udp_window, text='UDP header')
        udp_h.grid(column=4, row=0, sticky='w')

        # ===src_port===
        source_port = tkinter.Label(udp_window, text='Source port:')
        source_port.grid(column=3, row=1, sticky='w')
        entry_source_port = tkinter.Entry(udp_window, textvariable=udp_packet.src_port)
        entry_source_port.grid(column=4, row=1, padx=5, pady=5, sticky='w')

        # ===dst_port===
        destination_port = tkinter.Label(udp_window, text='Destination port:')
        destination_port.grid(column=3, row=2, sticky='w')
        entry_destination_port = tkinter.Entry(udp_window, textvariable=udp_packet.dst_port)
        entry_destination_port.grid(column=4, row=2, padx=5, pady=5, sticky='w')

        # ===length===
        length = tkinter.Label(udp_window, text='Length:')
        length.grid(column=3, row=3, sticky='w')
        entry_length = tkinter.Entry(udp_window, textvariable=udp_packet.length)
        entry_length.grid(column=4, row=3, padx=5, pady=5, sticky='w')

        # ===checksum===
        checksum = tkinter.Label(udp_window, text='Checksum:')
        checksum.grid(column=3, row=4, sticky='w')
        entry_checksum = tkinter.Entry(udp_window, textvariable=udp_packet.checksum)
        entry_checksum.grid(column=4, row=4, padx=5, pady=5, sticky='w')

        # ===name===
        name = tkinter.Label(udp_window, text='Name (for saving packet)')
        name.grid(column=3, row=5, sticky='w')
        entry_name = tkinter.Entry(udp_window, textvariable=udp_packet.name)
        entry_name.grid(column=4, row=5, padx=5, pady=5, sticky='w')

        # ===data===
        data = tkinter.Label(udp_window, text='Enter your data here:')
        data.grid(column=3, row=6, sticky='w')
        entry_data = tkinter.Entry(udp_window, textvariable=udp_packet.data)
        entry_data.grid(column=4, row=6, padx=5, pady=5, sticky='w')

        send_button = tkinter.Button(udp_window, text='Send', command=lambda: self.get_udp(udp_window, udp_packet, ip_header))
        send_button.grid(column=4, row=10, padx=5)
        udp_window.mainloop()

    def button_icmp(self):
        self.log.debug('ICMP button clicked')

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
