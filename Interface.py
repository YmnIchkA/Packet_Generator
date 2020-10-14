import tkinter
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
        self.udp_packets_list = list()

    @staticmethod
    def get_udp_dict(udp_packet):
        udp_packet.src_port = udp_packet.src_port.get()
        udp_packet.dst_port = udp_packet.dst_port.get()
        udp_packet.src_ip = udp_packet.src_ip.get()
        udp_packet.dst_ip = udp_packet.dst_ip.get()
        udp_packet.checksum = udp_packet.checksum.get()
        udp_packet.length = udp_packet.length.get()
        udp_packet.data = udp_packet.data.get()
        return udp_packet

    @staticmethod
    def get_tcp_packet(tcp_packet):
        pass

    def button_tcp(self):
        self.log.debug('Button TCP clicked')

    def get_udp(self, window, udp_packet, is_save=False):
        self.log.debug('get_udp method called')
        udp_packet = self.get_udp_dict(udp_packet)
        if is_save:
            udp_packet.name = udp_packet.name.get()
            self.udp_packets_list.append(udp_packet.packet_named())
            self.log.debug(f' packet ==\n {udp_packet.packet_named()}')

        self.log.debug(f'packet == \n {udp_packet.packet()}')
        window.destroy()

    def button_udp(self):
        udp_packet = packets.UDPPacket()
        self.log.debug('Button UDP clicked')
        udp_window = tkinter.Toplevel(self.window)
        udp_window.title('UDP packet')
        udp_window.geometry('700x450+25+25')
        ip_h = tkinter.Label(udp_window, text='IP header')
        ip_h.grid(column=2, row=0, sticky='w')
        udp_h = tkinter.Label(udp_window, text='UDP header')
        udp_h.grid(column=4, row=0, sticky='w')

        # ===src_ip===
        src_ip = tkinter.Label(udp_window, text='Source IP:')
        src_ip.grid(column=0, row=1, padx=5, pady=5, sticky='w')
        entry_src_ip = tkinter.Entry(udp_window, textvariable=udp_packet.src_ip)
        entry_src_ip.grid(column=1, row=1, padx=5, pady=5, sticky='w')

        # ===dst_ip===
        dst_ip = tkinter.Label(udp_window, text='Destination IP:')
        dst_ip.grid(column=0, row=2, padx=5, pady=5, sticky='w')
        entry_dst_ip = tkinter.Entry(udp_window, textvariable=udp_packet.dst_ip)
        entry_dst_ip.grid(column=1, row=2, padx=5, pady=5, sticky='w')

        # ===src_port===
        source_port = tkinter.Label(udp_window, text='Source port:')
        source_port.grid(column=3, row=1, padx=5, pady=5, sticky='w')
        entry_source_port = tkinter.Entry(udp_window, textvariable=udp_packet.src_port)
        entry_source_port.grid(column=4, row=1, padx=5, pady=5, sticky='w')

        # ===dst_port===
        destination_port = tkinter.Label(udp_window, text='Destination port:')
        destination_port.grid(column=3, row=2, padx=5, pady=5)
        entry_destination_port = tkinter.Entry(udp_window, textvariable=udp_packet.dst_port)
        entry_destination_port.grid(column=4, row=2, padx=5, pady=5, sticky='w')

        # ===length===
        length = tkinter.Label(udp_window, text='Length:')
        length.grid(column=3, row=3, padx=5, pady=5)
        entry_length = tkinter.Entry(udp_window, textvariable=udp_packet.length)
        entry_length.grid(column=4, row=3, padx=5, pady=5, sticky='w')

        # ===checksum===
        checksum = tkinter.Label(udp_window, text='Checksum:')
        checksum.grid(column=3, row=4, padx=5, pady=5)
        entry_checksum = tkinter.Entry(udp_window, textvariable=udp_packet.checksum)
        entry_checksum.grid(column=4, row=4, padx=5, pady=5, sticky='w')

        # ===name===
        name = tkinter.Label(udp_window, text='Name (for saving packet)')
        name.grid(column=3, row=5, padx=5, pady=5)
        entry_name = tkinter.Entry(udp_window, textvariable=udp_packet.name)
        entry_name.grid(column=4, row=5, padx=5, pady=5, sticky='w')

        # ===data===
        data = tkinter.Label(udp_window, text='Enter your data here:')
        data.grid(column=0, row=5, padx=5, pady=5)
        entry_data = tkinter.Entry(udp_window, textvariable=udp_packet.data)
        entry_data.grid(column=0, row=6, padx=5, pady=5, sticky='w')

        ok_button = tkinter.Button(udp_window, text='Ok', command=lambda: self.get_udp(udp_window, udp_packet))
        ok_button.grid(column=4, row=10, padx=5)
        save_button = tkinter.Button(udp_window, text='Save packet', command=lambda: self.get_udp(udp_window,
                                                                                                  udp_packet,
                                                                                                  True))
        save_button.grid(column=5, row=10, padx=5)
        udp_window.mainloop()

    def main(self):
        self.log.debug('Start main loop')
        self.window.geometry('200x200+600+200')
        btn_tcp = tkinter.Button(self.window, text="Create TCP", command=self.button_tcp)
        btn_udp = tkinter.Button(self.window, text="Create UDP", command=self.button_udp)

        btn_tcp.grid(column=0, row=0, padx=5, pady=10)
        btn_udp.grid(column=0, row=1)
        self.window.mainloop()
