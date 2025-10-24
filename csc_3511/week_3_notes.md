# DNS & UDP

## Things that tripped me up on this weeks quiz

* **Note** This is different in the actual textbook excercise in which this is true? From week #4 quiz but fits better here: 3.1-2 Transport-layer functionality. True or False: The transport layer provides for host-to-host delivery service?: False

* From week #4 quiz; 3.3-08 UDP Checksum: how good is it? True or False: When computing the Internet checksum for two numbers, a single flipped bit in each of the two numbers will always result in a changed checksum.: False, if you add two numbers, say 1 and 4, together and get a sum, and then change these numbers to 2 and 3, respectively, the sum remains 5. But if you change those original numbers to 2 and 6, the sum now changes to 8. So - if you change both of the numbers, the sum can change, but does not always change for all possible changes in the two values. Similar reasoning holds with a checksum.


## DNS, Dig command

* **Hostname vs. Domain Name**
    * A **Hostname** (e.g., `www.msoe.edu`) is a human-readable label that does not contain direct routing information.
    * The **Domain Name System (DNS)** is an application-layer protocol that translates a domain name into an **IP address**, which is necessary for machines to route datagrams.

* **DNS Tables (Resource Records)**
    * DNS uses a distributed database where information is stored in **Resource Records (RRs)**.
    * An **A Record (Address)** maps a hostname to an IP address.
    * An **NS Record (Name Server)** maps a domain to the hostname of the authoritative name server for that domain.

* **DNS Protocol Messages**
    * DNS is a client-server, request-response protocol, involving a **DNS Query** and a **DNS Response**.
    * The message header contains an ID number, **Flags** (like the QR bit for Query/Response and the RD bit for Recursion Desired), and counts for the different record types (Question, Answer, Authority, Additional).

* **Authoritative & Recursive DNS**
    * **Authoritative Servers** hold the definitive (non-cached) hostname-to-IP address mappings for a domain. They sit at the bottom of the DNS hierarchy.
    * The **Local DNS Server** (or **Recursive Resolver**) is the server a host first contacts. It performs **recursive queries** up the hierarchy (Root, TLD, then Authoritative) on the client's behalf to resolve the name, and then caches the result.
    * The **`dig` command** is a utility used for performing DNS lookups and troubleshooting.

* **DNS Caching**
    * Why does the local DNS server perform caching?: 1. DNS caching results in less load elsewhere in DNS, when the reply to a query is found in the local cache. 2. DNS caching provides for faster replies, if the reply to the query is found in the cache.

* **DNS Time to Live**
    * A setting in a DNS record that determines how long a piece of information should be cached by a resolving name server before it is refreshed. Measured in seconds, a higher TTL can speed up lookups by allowing more frequent use of cached data, while a lower TTL ensures that changes to DNS records, such as when migrating a server, are propagated more quickl

***

## UDP protocol

* **UDP Properties**
    * UDP (User Datagram Protocol) is a "bare bones," "best effort" transport protocol.
    * It provides **unreliable, unordered delivery**; segments may be **lost** or delivered to the application out-of-order.

* **Connectionless**
    * UDP is **connectionless**—it requires **no handshake** or connection setup (unlike TCP), which eliminates the delay of connection establishment.
    * Each UDP segment is handled independently.

* **HTTP/3 uses UDP**
    * Some modern protocols, such as **HTTP/3** (via QUIC), use UDP as their transport layer foundation.
    * If applications using UDP require reliability, in-order delivery, or congestion control, that functionality must be implemented in the **application layer**.

* **Checksum**
    * The UDP segment header includes a **checksum**.
    * Its sole goal is to detect errors (flipped bits) that may have occurred during transmission. The Internet checksum uses a one's complement sum for calculation and verification, offering weak error protection.

* **Multiplexing vs. De-multiplexing**
    * **Multiplexing (Sender):** The transport layer collects data from multiple application processes (sockets) and adds a transport header.
    * **De-multiplexing (Receiver):** The receiving host uses the header information, specifically the **destination port number**, to direct the incoming segment to the correct application **socket**.
    * UDP demultiplexing uses *only* the destination port number; segments with the same destination port but different source IP addresses or source ports are delivered to the same socket.