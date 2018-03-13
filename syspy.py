import psutil
import json
import time
import datetime
import re


class SysSnapshot(object):
    """docstring"""
    def __init__(self):
        """Constructor"""
        self.float_cpu_percent = float(psutil.cpu_percent())
        self.float_percent_memory = float(str((re.findall(
                                          r'(?<=percent=)\d{1,}\.\d{1,}',
                                          str(psutil.virtual_memory())))[0]))
        self.float_UsedM = float(
                      (re.findall(r'(?<=used=)\d{1,}',
                       str(psutil.virtual_memory())))[0]
        ) / 1048576

        # find in output of command psutil.disk_usage("/") need string
        self.float_mount_used_root = float(
                      str((re.findall(r'(?<=used=)\d{1,}',
                           str(psutil.disk_usage("/"))))[0])
        ) / 1048576

        # find in output of command psutil.disk_usage("/") need string
        self.float_mount_total_root = float(
                      str((re.findall(r'(?<=total=)\d{1,}',
                           str(psutil.disk_usage("/"))))[0])
        ) / 1048576

        # find in output of command psutil.disk_usage("/boot") need string
        self.float_mount_used_boot = float(
                      str((re.findall(r'(?<=used=)\d{1,}',
                           str(psutil.disk_usage("/boot"))))[0])
        ) / 1048576

        # find in output of command psutil.disk_usage("/boot") need string
        self.float_mount_total_boot = float(
                      str((re.findall(r'(?<=total=)\d{1,}',
                           str(psutil.disk_usage("/boot"))))[0])
        ) / 1048576

        # find in output of command psutil.net_io_counters() need string
        self.float_network_bytes_sent = float(
                      str((re.findall(r'(?<=bytes_sent=)\d{1,}',
                           str(psutil.net_io_counters())))[0])
        )

        # find in output of command psutil.net_io_counters() need string
        self.float_network_bytes_recv = float(
                      str((re.findall(r'(?<=bytes_recv=)\d{1,}',
                           str(psutil.net_io_counters())))[0])
        )

        # find in output of command psutil.net_io_counters() need string
        self.float_network_packets_sent = float(
                      str((re.findall(r'(?<=packets_sent=)\d{1,}',
                           str(psutil.net_io_counters())))[0])
        )

        # find in output of command psutil.net_io_counters() need string
        self.float_network_packets_recv = float(
                      str((re.findall(r'(?<=packets_recv=)\d{1,}',
                           str(psutil.net_io_counters())))[0])
        )

        # find in output of command psutil.net_io_counters() need string
        self.float_network_dropin = float(
                      str((re.findall(r'(?<=dropin=)\d{1,}',
                           str(psutil.net_io_counters())))[0])
        )
        self.counter = 1
        self.block = 0
        # read config file
        f_config = open("config", 'r')
        # start parsing config file
        first_line = f_config.readline()
        second_line = f_config.readline()
        result = re.match(r'output=(json|txt)', first_line)
        result2 = re.search(r'interval=\d+', second_line)
        if result:
            print("First line is correct!")
            list_which_format = re.findall(r'(json|txt)', first_line)
            which_format = list_which_format[0]
            print(which_format)
            if which_format == "txt":
                self.format = 1
            else:
                self.format = 0
            print(self.format)
            if result2:
                print("Second line is correct!")
                list_which_format = re.findall(
                         r'(?<=interval=)\d+', second_line
                )
                self.interval = list_which_format[0]
                print(self.interval)
            else:
                string = "Config is not correct"
                string2 = "or specific format is not correct!"
                string3 = string + string2
                print(string3)
                self.block = 1
                return

        else:
            string = "Config is not correct"
            string2 = "or specific format is not correct!"
            string3 = string + string2
            print(string3)
            self.block = 1
            return
        # end of parsing config file
    # logging

    def logging(self):
        if self.block == 0:
            if self.format == 0:
                infinity = 5
                f = open('json_myClass.json', 'w')
                while infinity == 5:
                    d = {}
                    d["SNAPSHOT"] = str(self.counter)
                    d["TIMESTAMP"] = str(datetime.datetime.now())
                    d["Overall CPU"] = self.float_cpu_percent
                    d["Overall VM"] = self.float_percent_memory
                    d["Memory Usage"] = self.float_UsedM
                    d5 = {}
                    d5["Used(MB)"] = self.float_mount_used_root
                    d5["Total(MB)"] = self.float_mount_total_root
                    d2 = {}
                    d2["/"] = d5
                    d1 = {}
                    d1["Used(MB)"] = self.float_mount_used_boot
                    d1["Total(MB)"] = self.float_mount_total_boot
                    d2["/boot"] = d1
                    d3 = {}
                    d3["Mounted points"] = d2
                    d["IO Information"] = d3
                    d4 = {}
                    d4["bytes_sent(MB)"] = self.float_network_bytes_sent
                    d4["bytes_recv(MB)"] = self.float_network_bytes_recv
                    d4["packets_sent(MB)"] = self.float_network_packets_sent
                    d4["packets_recv(MB)"] = self.float_network_packets_recv
                    d4["droppin(times)"] = self.float_network_dropin
                    d["Network Information"] = d4
                    with open('json_myClass.json', 'a') as outfile:
                        json.dump(
                             d, outfile,
                             sort_keys=True, indent=4,
                             ensure_ascii=False
                        )
                        outfile.write("\n")
                    time.sleep(int(self.interval) * 60)
                    print("done")
                    self.counter += 1
            else:
                infinity = 5
                f = open('text_class.txt', 'w')
                while infinity == 5:
                    f = open('text_class.txt', 'a')
                    a30 = "\t\t\t\t\t\t\tSNAPSHOT"
                    string30 = a30 + str(self.counter) + "\n"
                    a31 = "\t\t\t\t\t\t\tTIMESTAMP "
                    string31 = a31 + str(datetime.datetime.now()) + "\n"
                    string1 = "Overall CPU load(%)\t"
                    string2 = "Overall VM(%)\t"
                    string3 = "Memory Usage(MB)\t"
                    string4 = "IO information"
                    first = string30 + string31 + string1
                    first += string2 + string3 + string4
                    second = str(self.float_cpu_percent)
                    second += "\t\t\t"
                    second += str(self.float_percent_memory)
                    second += "\t\t"
                    second += str(self.float_UsedM)
                    second += "\t\t"
                    second += "Mounted points:\n"
                    f.write(first + "\n")
                    f.write(second)
                    a10 = "\t\t\t\t\t\t\t\t\\:\n\t\t\t\t\t\t\t\t   Used(MB): "
                    string10 = a10 + str(self.float_mount_used_root) + "\n"
                    string11 = "\t\t\t\t\t \t\t\t   Total(MB): "
                    string11 += str(self.float_mount_total_root) + "\n"
                    string14 = "\t\t\t\t\t\t\t\t\\boot:\n\t\t\t\t\t\t\t\t"
                    string14 += "   Used(MB): "
                    string14 += str(self.float_mount_used_boot) + "\n"
                    string15 = "\t\t\t\t\t\t\t\t   Total(MB): "
                    string15 += str(self.float_mount_total_boot) + "\n"
                    string16 = "\tNetworkInformation:\n"
                    string18 = "\t\tbytes_sent = "
                    string18 += str(self.float_network_bytes_sent) + "\n"
                    string19 = "\t\tbytes_recv = "
                    string19 += str(self.float_network_bytes_recv) + "\n"
                    string20 = "\t\tpackets_sent = "
                    string20 += str(self.float_network_bytes_recv) + "\n"
                    string21 = "\t\tpackets_recv = "
                    string21 += str(self.float_network_packets_recv) + "\n"
                    string22 = "\t\tdropin = "
                    string22 += str(self.float_network_dropin) + "\n"
                    f.write(string10)
                    f.write(string11)
                    f.write(string14)
                    f.write(string15)
                    f.write(string16)
                    f.write(string18)
                    f.write(string19)
                    f.write(string20)
                    f.write(string21)
                    f.write(string22)
                    if self.counter != 1:
                        time.sleep(int(self.interval) * 60)
                    print("done")
                    self.counter += 1
        else:
            print("Not Correct config!")
            return

    # basics methods
    def get_age(self):
        return self.age

    def get_cpu(self):
        return self.float_cpu_percent

    def get_vm(self):
        return self.float_percent_memory

    def get_useM(self):
        return self.float_UsedM

    def get_name(self):
        return self.myname

    def get_used_root(self):
        return self.float_mount_used_root

    def get_total_root(self):
        return self.float_mount_total_root

    def get_used_boot(self):
        return self.float_mount_used_boot

    def get_total_boot(self):
        return self.float_mount_total_boot

    def get_bytes_sent(self):
        return self.float_network_bytes_sent

    def get_bytes_recv(self):
        return self.float_network_bytes_recv

    def get_packets_sent(self):
        return self.float_network_packets_sent

    def get_packets_recv(self):
        return self.float_network_packets_recv


# if __name__ == "__main__":
myobject = SysSnapshot()
myobject.logging()
