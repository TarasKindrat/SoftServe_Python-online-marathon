"""
An IP network is a set of routers that communicate routing information using a protocol.
A router is uniquely identified by an IP address.
In IPv4, an IP address consists of 32 bits, canonically represented as 4 decimal numbers of 8 bits each.
The decimal numbers range from 0 (00000000) to 255 (11111111).
Each router has a "routing table" that contains a list of IP addresses, for the router to know where to send IP packets.

Route summarization in IP networks
As the network grows large (hundreds of routers), the number of IP addresses in the routing table increases rapidly.
Maintaining a high number of IP addresses in the routing table would result in a loss of performances
(memory, bandwidth and CPU resources limitation).
Route summarization, also called route aggregation, consists in reducing the number of routes by aggregating them
into a "summary route".

Let's consider the following example:

We have 4 routers connected to A. A is aware about all 4 IP addresses, because it has a direct interface to each
 of them. However, A will not send them all to B.
Instead, it will aggregate the addresses into a summary route, and send this new route to B.
This implies that:

    - Less bandwidth is used on the link between A and B.
    - B saves memory: it has only one route to store in its routing table
    - B saves CPU resources: there are less entries to consider when handling incoming IP packets

Computing a summary route
A has all 4 addresses stored in its routing table.

Address 1 	172.16.12.0
Address 2	172.16.13.0
Address 3 	172.16.14.0
Address 4	172.16.15.0


A will convert these IP addresses to binary format, align them and find the boundary line between the
common prefix on the left , and the remaining bits on the right.

Address 1	10101100	00010000	000011    00	00000000
Address 2	10101100	00010000	000011    01	00000000
Address 3	10101100	00010000	000011    10	00000000
Address 4	10101100	00010000	000011    11	00000000


A creates a new IP address made of the common bits, and all other bits set to "0 ".
This new IP address is converted back to decimal numbers.
Finally, A computes the number of common bits, also called "subnet ".
The summary route is this new IP address, followed by a slash and the subnet: 172.16.12.0/22

Input: A list of strings containing the IP addresses

Output: A string containing the summary route, represented as an IP address, followed by a slash and the subnet.

Preconditions:
all(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$ ",d) for d in data))
all(-1 < int(n) < 256 for n in d.split(". ") for d in data)
len(data) == len(set(data)) and len(data) > 1
"""

import re


def valid_ip_address(data):
    if all(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", d) for d in data) and \
       all(-1 < int(n) < 256 for d in data for n in d.split(".")) and len(data) == len(set(data)) and len(data) > 1:
        return True
    else:
        return False


def route_summarization_in_ip_networks(data):
    if valid_ip_address(data):
        list_network_address = []
        list_bin_ip_1 = []
        list_bin_ip = []
        list_bin_ip_2 = []
        # Create template for binary format
        binary_template = "{0:08b}{1:08b}{2:08b}{3:08b}"
        # print(bin(int('172')) and bin(172))
        # print(int(0b10101100))
        # Add lists with IP octets to list like [['10', '1', '57', '0'], ['10', '1', '59', '0'], ['10', '1', '61', '0']]
        for d in data:
            list_bin_ip_1.append([n for n in d.split(".")])
        # Convert to binary format use template
        for item in list_bin_ip_1:
            list_bin_ip_2.append(bin(int(''.join(item))))
            list_bin_ip.append(binary_template.format(int(item[0]), int(item[1]), int(item[2]), int(item[3])))

        for i in range(0, len(list(list_bin_ip[0]))):
            if all(list(list_bin_ip[0])[i] in j[i] for j in list_bin_ip):
                list_network_address.append(list(list_bin_ip[0])[i])
            else:
                break
        network_mask = len(list_network_address)
        # Add zeros to net_adress
        for j in range(0, 32 - network_mask):
            list_network_address.append('0')

        network_address_string = "".join(list_network_address)
        # Convert from bin to decimal like int(int('0b1010',2))
        network_address = f"{int('0b'+network_address_string[0:8],2)}.{int('0b'+network_address_string[8:16],2)}." \
                          f"{int('0b'+network_address_string[16:24],2)}.{int('0b'+network_address_string[24:],2)}" \
                          f"/{network_mask}"

        # for ip_adr in range(1, len(list_bin_ip_2)):
        #     result = list_bin_ip_2[0] and ip_adr
        # print(int(result))

        return network_address
    else:
        return "Not valid IP"





#print(route_summarization_in_ip_networks(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]))
#
# # 172.16.12.0 / 22
# #
# # None
#
#print(route_summarization_in_ip_networks(["172.16.12.0", "172.16.13.0", "172.155.43.9"]))
#
# # 172.0.0.0 / 8
# #
# # None
#
#print(route_summarization_in_ip_networks(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]))
#
# # 128.0.0.0 / 2
# #
# # None
#
print(route_summarization_in_ip_networks(["10.1.57.0", "10.1.59.0", "10.1.61.0"]))
#
# # 10.1.56.0 / 21
# #
# # None
#
#print(route_summarization_in_ip_networks(["192.168.97.0", "192.168.100.0"]))
#
# # 192.168.96.0 / 21
# #
# # None
#
#print(route_summarization_in_ip_networks(["172.16.14.0", "172.16.17.0", "172.16.25.0"]))
#
# # 172.16.0.0 / 19
# #
# # None
#
print(route_summarization_in_ip_networks(["172.16.14.0", "172.16.17.0", "172.16.25.0", "10.1.57.0", "10.1.59.0", "10.1.61.0"]))
# 0.0.0.0/0