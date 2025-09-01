# Wireguard

- It helps to think of WireGuard primarily as a network interface, like any other. It will have the usual attributes, like IP address, CIDR, and there will be some routing associated with it. But it also has WireGuard-specific attributes, which handle the VPN part of things.

- A big thing to understand about wireguard is that unlike say OpenVPN, there isnt a client server relationship. Both ends of the vpn tunnel in wireguard are client, both can be configured the same. The difference would be that on the server you can allow clients to access local network and you don't generally want the server to allow access to the network on the client. And on the server you would allow multiple peers (clients) to access it and on the client(s) you have only one peer, the server. 

## Allowed IPs & A Note on Routing Tables

- Every machine has a routing table. This table is a list of rules that tells the device where to send network traffic based on the destination IP address and network interface. Longest prefix match is used to determine which entry in the table the packet needs to be sent to. For example, take the two IPv4 addresses 192.168.20.16/28 & 192.168.0.0/16. When the address 192.168.20.19 needs to be looked up, both entries in the forwarding table "match". That is, both entries contain the looked up address. In this case, the longest prefix of the candidate routes is 192.168.20.16/28 because it has a longer subnet mask.
- allowed_ips  defines the IP ranges for which a peer will route traffic. On simple clients, this is usually a single address (the VPN address of the simple client itself)

When WireGuard sends a network packet to a peer:

1. WireGuard reads the destination IP from the packet and compares it to the list of allowed IP addresses in the local configuration. If the peer is not found, WireGuard drops the packet.
2. If the peer is valid, WireGuard encrypts the packet using the peer’s public key.
3. The sending host looks up the most recent Internet IP address of the host and sends the encrypted packet to it.

When WireGuard receives a packet:

1. WireGuard decrypts the packet using the private key of the remote host.
2. WireGuard reads the internal source address from the packet and looks up whether the IP is configured in the list of allowed IP addresses in the settings for the peer on the local host. If the source IP is on the allowlist, WireGuard accepts the packet. If the IP address is not on the list, WireGuard drops the packet.

AllowedIPs is used as a routing key when sending traffic, and as an ACL when receiving traffic.