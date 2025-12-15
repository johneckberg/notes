# Week 14 Notes:

## Week 14, Lecture 1: Firewalls

### Motivation: Scalable Defenses

* Observation: More network services = more risk
* Observation: More networked machines = more risk

**Solution: Instead of securing individual machines, we want to
secure the entire network!**

* Idea: Add a single point of access in and out of the network, with a monitor
* Any traffic that could affect vulnerable systems must pass through the firewall
* Ensure “complete mediation”

### Network access is controlled by a policy

* A security policy is a set of rules that defines what traffic is allowed or denied
* Defines what traffic is allowed to exit the network (outbound policy)
* Defines what traffic is allowed to enter the network (inbound policy)
* Policy model based on our threat model: We usually assume users “inside” the
network are trusted, and those outside are not

### What do the policies look like?

* Outbound policy: Allow outbound traffic
    * Users inside the network can connect to any service
* Inbound policy: Only some traffic is able to enter the network
    * Allow inbound traffic in response an outbound connection (e.g., FTP)
    * Allow inbound traffic to certain, trusted services (e.g. SSH)
    * Deny all other inbound traffic (e.g., IP forwarding)

### Packet Filters

* Firewalls are often packet filters: Works at network layer and transport layer
  * Filtering with incoming and outgoing interfaces
  * Inspect network packets and chooses a handling method: forward or drop

* Stateful Vs. Stateless Packet Filters

Stateful firewalls inspect traffic context by tracking active connections (using a state table) for enhanced security, while stateless firewalls filter packets individually based on static rules (IPs, ports) for speed and simplicity; stateful offers deep inspection but uses more resources, ideal for complex threats, whereas stateless provides basic, fast filtering, suitable for simple networks

* Potential fields for a stateful firewall

  * Source/Destination IP Addresses: Identifies where traffic is coming from and going to.
  * Source/Destination Ports: Specifies the application ports (e.g., 80 for HTTP, 443 for HTTPS).
  * Protocol: The transport protocol (TCP, UDP, ICMP) being used.
  * TCP Flags: For TCP, flags like SYN, ACK, FIN help track the connection's lifecycle (setup, data transfer, teardown).
  * Sequence Numbers: Ensures packets are in the correct order for TCP sessions.
  * Connection State: The firewall's internal record (state table) of established, valid conversations

  * For ICMP packets
    * ICMP Timeout
    * IMCP message type
    * ICMP ID

### Firewall Limits

* Deep Packet Inspection
* Evading Packet Filters
