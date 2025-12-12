# Week 6: IPv4 Header

## Things that tripped me up on this weeks quiz

* What layers are process to process?
    * review quizzes theres a question about process to process idk which quiz
    * IP layer is process to process? He's discussing the protocol number field in the header.
* Dijkstra's Algorithm diagrams 

## Dijkstra's Pseudo Code

The algorithm requires a starting node, and computes the shortest distance from that starting node to each other node. Dijkstra's algorithm starts with infinite distances and tries to improve them step by step:

    Create a set of all unvisited nodes: the unvisited set.
    Assign to every node a distance from start value: for the starting node, it is zero, and for all other nodes, it is infinity, since initially no path is known to these nodes. During execution, the distance of a node N is the length of the shortest path discovered so far between the starting node and N.[18]
    From the unvisited set, select the current node to be the one with the smallest (finite) distance; initially, this is the starting node (distance zero). If the unvisited set is empty, or contains only nodes with infinite distance (which are unreachable), then the algorithm terminates by skipping to step 6. If the only concern is the path to a target node, the algorithm terminates once the current node is the target node. Otherwise, the algorithm continues.
    For the current node, consider all of its unvisited neighbors and update their distances through the current node; compare the newly calculated distance to the one currently assigned to the neighbor and assign the smaller one to it. For example, if the current node A is marked with a distance of 6, and the edge connecting it with its neighbor B has length 2, then the distance to B through A is 6 + 2 = 8. If B was previously marked with a distance greater than 8, then update it to 8 (the path to B through A is shorter). Otherwise, keep its current distance (the path to B through A is not the shortest).
    After considering all of the current node's unvisited neighbors, the current node is removed from the unvisited set. Thus a visited node is never rechecked, which is correct because the distance recorded on the current node is minimal (as ensured in step 3), and thus final. Repeat from step 3.
    Once the loop exits (steps 3–5), every visited node contains its shortest distance from the starting node.

## IP Header 

* length of the IP header is **not** fixed!
* The length of the IP header is **not fixed** due to the optional "Options" field. The **Header Length (IHL)** field specifies the header's size.
* The IP address is logically attached to a specific **interface**.
* The **Protocol field** (Upper layer field) is used for **demultiplexing**, indicating the transport-layer protocol (e.g., TCP or UDP) that should receive the payload upon reaching the destination host.
* The IP header checksum is different from UDP/TCP checksums because it must be **recalculated at every hop**.
* Recalculation is necessary because the **Time-to-Live (TTL)** field is decremented by every router, thus changing the header.
* Every link layer protocol imposes a specific **Maximum Transmission Unit (MTU)**, which is the largest IP datagram size it can carry.

### IP Header Field Definitions

| Field | Definition |
| :--- | :--- |
| **Version Field** | This field contains the **IP protocol version number**. |
| **Type-of-service field** | This field contains **ECN** (Explicit Congestion Notification) and **differentiated service bits**. |
| **Fragmentation offset field** | This field is used for datagram **fragmentation/reassembly**. |
| **Time-to-live field (TTL)** | The value in this field is **decremented at each router**; when it reaches zero, the packet must be dropped. |
| **Header checksum field** | This field contains the **Internet checksum** of this datagram's header fields. |
| **Upper layer field (Protocol)** | This field contains the "protocol number" for the transport-layer protocol (e.g., UDP or TCP) to which this datagram's payload will be **demultiplexed**. |
| **Payload/data field** | This field contains a **UDP or TCP segment**, for example. |
| **Datagram length field** | This field indicates the **total number of bytes in datagram** (header + payload). |

***

## Link Layer

The link layer is responsible for transferring data between **adjacent nodes** over a single communication link. Its key functions ensure:

* **Reliable data transfer** between directly connected nodes (used primarily on high bit-error links like wireless).
* **Flow control** between adjacent sending and receiving nodes.
* **Coordinated access to a shared physical medium** (Managed by Multiple Access Protocols, e.g., CSMA/CD).
* **Bit-level error detection and correction** (Receiver detects errors, signals retransmission, or drops frame).
* **Multiplexing down from / multiplexing up to a network-layer protocol** (via **Framing**, which encapsulates the Network layer datagram into a link-layer frame).

***



## Subnetting and Addressing

A subnet mask uses a bitwise AND operation with an IP address to isolate its network portion, determining which part of the address identifies the network and which identifies the specific host. This operation works by converting both the IP address and the subnet mask to binary. A bitwise AND performs a comparison on each bit position: if both bits are 1, the result is 1; otherwise, it's 0. The result of this operation is the network address

for example, a /8 subnet mask is 255.255.255.0

### Calculations

| Question | Calculation/Reasoning | Answer |
| :--- | :--- | :--- |
| What is the maximum number of hosts possible in the larger 128.119.160/24 network? | The /24 subnet mask leaves 8 bits for the host ID ($32 - 24 = 8$). The total number of addresses is $2^8 = 256$. (The number of *usable* hosts is $2^8 - 2 = 254$). | 256 |
| How many bits are needed to be able to address all of the hosts in subnet A? | To address up to 62 usable hosts (or 64 total addresses), you need **6 host bits** ($2^6 = 64$ addresses). | 6 |
| Suppose that subnet A has a CIDRized subnet address range of 128.119.160.128/26; Subnet B has an CIDRied subnet address range of 128.119.160.64/26. We now want a valid CIDRized IP subnet address range for subnet C of the form 128.119.160.x/26. What is a valid value of x? | A /26 network has a block size (increment) of $2^{32-26} = 64$. The available network addresses start at multiples of 64: **0**, 64, 128, 192. Subnet A uses the $128$ block, and Subnet B uses the $64$ block. The next unused, valid block starts at $0$. | 0 |