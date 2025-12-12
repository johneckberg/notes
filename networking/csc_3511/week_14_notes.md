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

### Firewall Limits

* Deep Packet Inspection
* Evading Packet Filters
