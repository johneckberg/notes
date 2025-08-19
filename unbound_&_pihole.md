# Unbound and Pi-Hole

## Pi-Hole

Pi-hole is software that runs on a Raspberry Pi (can technically run even outside a Pi) that acts as the Domain Name Service (DNS) proxy within your own network. ihole is built atop of Dnsmasq. Digging under the hood of Pihole a little, there's actually a surprisingly small amount of customisation to make it function as an ad-blocker compared with a vanilla installation of dnsmasq. **Pi-hole is a forwarding dns server** It's primary job is to filter DNS requests against blocklists (ad domains, trackers, etc.). If it's a blocked domain (like an ad server), Pi-hole immediately denies the request. If it's a legitimate domain, then pi-hole still needs to call an upstream dns server to get the ip address.