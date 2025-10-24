# Link Layer

## Things that tripped me up on this weeks quiz

* **Note this is different than the textbook website** 6.4-2. Different types of addressing (b). We've now learned about both IPv4 addresses and MAC addresses.  Consider the address properties below, and use the pulldown menu to indicate  which of these properties is only a property of IPv4 addresses (and therefore is not a property of MAC addresses - careful!). Answer: Link layer address, This address remains the same as a host moves from one network to another, This is a 48-bit address.


## Error Detection

### Single Bit Parity Checking
* **Mechanism:** An extra bit, called the **parity bit**, is appended to a block of data.
* **Detection:** It can only tell **that a bit is flipped**, but **not which one is flipped**. If two bits are flipped (a double error), the total count of 1s remains valid, and the error is undetected.
* **Even Parity Checking:** The parity bit is set so that the **total number of '1's** in the data block (including the parity bit) is **even**.
* **Odd Parity Checking:** The parity bit is set so that the **total number of '1's** in the data block (including the parity bit) is **odd**.

### 2-D Parity Checking (Two-Dimensional Parity)
* **Mechanism:** Data is arranged in a grid, and a parity bit is calculated for each **row** and each **column**.
* **Detect & Correct:** This method is powerful enough to **detect and correct a single bit error**.
    * A single flipped bit will cause parity errors in both its corresponding row and column.
    * The intersection of the row in error and the column in error identifies the exact location of the flipped bit, allowing for correction (flipping it back).

### Cyclic Redundancy Check (CRC)
* **Purpose:** A highly effective error detection scheme widely used in link layers (Ethernet, WiFi).
* **Generator Polynomial ($G$):** This is a predefined, specific bit pattern of $r+1$ bits (e.g., $x^3 + 1$ corresponds to 1001) used as the divisor.
* **Core Concept:** Treat the data bits as a polynomial and use polynomial arithmetic (modulo 2) based on the Generator $G$. The goal is to compute $r$ **CRC bits ($R$)** such that the resulting data frame **$<D, R>$** (Data + CRC bits) is exactly divisible by $G$.
* **Binary Division by XOR (Modulo-2 Arithmetic):** CRC division uses the **Exclusive OR (XOR)** operation for subtraction, which prevents carries and borrows.
    * The remainder of this division process is the set of CRC bits, $R$.
    * The receiver performs the same division. A **non-zero remainder** indicates an error has occurred.

***

## Link Layer and Addressing

### MAC Address (Interface Identifier)
* **Definition:** A unique, 48-bit physical address permanently assigned to every network interface card (NIC).
* **Purpose:** Used by Layer 2 switches to forward data frames within a local network (LAN).

### Multiple Access Protocols
* These are protocols required when multiple nodes share a **single, common transmission medium** (e.g., old bus topology Ethernet or wireless LANs).
* In modern switched Ethernet, the links are point-to-point (one host per switch port), making the collision domain smaller and often eliminating the need for these protocols on the wired links.

### Switches vs. Routers
| Feature | Switch (Layer 2) | Router (Layer 3) |
| :--- | :--- | :--- |
| **Primary Role** | Connects devices **within a single local network (LAN)**. | Interconnects **different networks** (subnets). |
| **Addressing** | Uses **MAC Addresses** (physical addresses). | Uses **IP Addresses** (logical addresses). |
| **Forwarding Table** | **MAC Address Table** (Self-learning). | **IP Forwarding Table** (Routing Table). |
| **Nature** | **Plug-and-play**, fast, simple forwarding. | Requires **configuration**, performs complex path selection. |

### Why Link Layer Can't Scale to the Internet
The Internet cannot be built solely using switches because the Layer 2 forwarding mechanism **does not scale** globally:
* **No Address Hierarchy:** MAC addresses are **random and unique** globally; they do not contain any information about the location of the host (unlike IP addresses, which are hierarchical).
* **No Route Aggregation:** Because MAC addresses are flat, a switch would have to store an entry for **every single device** on the Internet. It cannot aggregate or summarize routes (e.g., "all traffic for Continent X goes this way"). This results in an impossibly large forwarding table.
* **Broadcast Overload:** Layer 2 protocols (like ARP) rely heavily on **broadcasting** (sending a frame to all devices on the network). On an Internet scale, this would cause **broadcast storms** that would instantly overwhelm the network.

### Self-learning and Forwarding (Switch Logic)
A switch is a **self-learning** device that automatically builds its MAC Address Table:

1.  **Self-Learning:** When a frame arrives at a port, the switch inspects the **source MAC address** in the frame and records the pair **`<Source MAC, Incoming Port>`** in its table.
2.  **Forwarding:** The switch checks the **destination MAC address** of the frame:
    * **Found:** The frame is forwarded only out the port indicated in the table.
    * **Not Found (Unknown):** The frame is **flooded** (sent out on all ports except the one it arrived on). This ensures the destination receives the frame, and when the destination replies, the switch can learn its location.

    **all the switch knows is what interface its sending out of or receiving in when sending a frame across switches. It doesnt know the interface on the other side of the connection**
    lets consider two switches, connected via interface 8 on switch 2 and 7 on switch 1.
    * source entry: if the forwarding happens on switch one (node to node on switch one), all switch 2 gets from that is the letter of the node and the interface number on its side of the switch to switch connection
    * destination entry: In this case, switch 2 has no destination entry bc the destination was not on that switch

    Now, if we are sending data switch to switch;
    * source entry: the source entry from the receiving side is **its** interface thats connected to the other switch on
    * destination entry: the destination entry from the receiving side is **its** interface its sending out to the other switch on

    If it has knowledge of the device's interface (its on the switch), that will be the sending or receiving entry

    n/a happens when the switch "hears" a forward contained within the other switch

    **Dont forget to add the right receiving/sending node** 

### ARP: Address Resolution Protocol
* **Purpose:** To translate a Layer 3 **IP address** into a corresponding Layer 2 **MAC address** on the same local network (LAN).
* **Mechanism:** A host/router broadcasts an **ARP request** (containing the target IP) to the entire LAN. Only the host with the matching IP replies with an **ARP response** (containing its MAC address).

How it works
Step 1: If a source device want to communicate with another device, source device checks its Address Resolution Protocol (ARP) cache to find if it already has a resolved MAC Address of the destination device. If it is there, it will use that MAC Address for communication.

Step 2: If ARP resolution is not there in local cache, the source machine will generate an Address Resolution Protocol (ARP) request message, it puts its own data link layer address as the Sender Hardware Address and its own IPv4 Address as the Sender Protocol Address. It fills the destination IPv4 Address as the Target Protocol Address. The Target Hardware Address will be left blank, since the machine is trying to find that.

Step 3: The source broadcast the Address Resolution Protocol (ARP) request message to the local network.

Step 4: The message is received by each device on the LAN since it is a broadcast. Each device compare the Target Protocol Address (IPv4 Address of the machine to which the source is trying to communicate) with its own Protocol Address (IPv4 Address). Those who do not match will drop the packet without any action.

Step 5: When the targeted device checks the Target Protocol Address, it will find a match and will generate an Address Resolution Protocol (ARP) reply message. It takes the Sender Hardware Address and the Sender Protocol Address fields from the Address Resolution Protocol (ARP) request message and uses these values for the Targeted Hardware Address and Targeted Protocol Address of the reply message.

Step 6: The destination device will update its Address Resolution Protocol (ARP) cache, since it need to contact the sender machine soon.

Step 7: Destination device send the Address Resolution Protocol (ARP) reply message and it will NOT be a broadcast, but a unicast in order to save network resources.

Step 8: The source machine will process the Address Resolution Protocol (ARP) reply from destination, it stores the Sender Hardware Address as the layer 2 address of the destination.

Step 9: The source machine will update its Address Resolution Protocol (ARP) cache with the Sender Hardware Address and Sender Protocol Address it received from the Address Resolution Protocol (ARP) reply message.

Machines at local network can't communicate if they don't know the MAC Address of each other. Neither Internal IP Address can be used for that. If a router wants to communicate with its client or with the other router then it must know the MAC Address of its client and the other router as well.


#### Interaction between ARP and IP forwarding tables (Sending to another network)
A host uses its IP forwarding logic to decide whether a destination is **local** or **non-local**.

* **Case: Destination is Non-Local (Different Network)**
    1.  The host determines the destination IP is on a different network and must be sent to the **router** (the default gateway).
    2.  The host checks its ARP table for the **router's MAC address**.
    3.  If the router's MAC is not found, the host uses ARP to discover the router's MAC.
    4.  The host constructs the frame:
        * **IP Destination:** Final destination's IP address (e.g., B's IP) **(Does not change)**.
        * **MAC Destination:** Router's MAC address **(The next hop)**.

* **Simplified Example: Router Directly Connected to Both LANs**
    * When the packet travels from Host A $\rightarrow$ Router R $\rightarrow$ Host B:
        * **A $\rightarrow$ R:** The Link Layer frame uses **R's MAC address** as the destination. The IP datagram inside still lists **B's IP address** as the final destination.
        * **R $\rightarrow$ B:** The Router creates a **new Link Layer frame** for the outgoing network. It uses **B's MAC address** as the destination (after an ARP lookup on that LAN) and its own interface's MAC as the source. The IP datagram inside remains the same (IP Source: A, IP Destination: B).
    * The **IP addresses remain constant**, while the **MAC addresses change at every hop** (router interface).
    

* **Multiple Access Protocols - Random Access Protocols**

* In random access protocols, all stations have equal priority. Transmission decisions are based on the state of the channel (idle or busy).
    * Aloha
        * Designed for wireless LANs and shared media.
        * Multiple stations can transmit simultaneously, leading to collisions.
    * CSMA (Carrier Sense Multiple Access)
        * A device first listens to the network to see if it's clear, and if so, begins transmitting. If a collision is detected during transmission, the devices involved immediately stop, send a jam signal, and then wait a random amount of time before attempting to retransmit
    * CSMA/CD (Collision Detection)
        *
    * CSMA/CA (Collision Avoidance)

Quiz #7

Question 3 (6.3-3): 
For message 1 (t = 0.3): Channel is idle; Starts transmitting at t = 0.3, completes at t = 1.3; Signal propagates to other nodes by t = 0.5.
For message 2 (t = 1.7): Message 1 finished at t = 1.3, and message 2's sender detects channel is idle since t = 1.5 (0.2 propagation delay); Message 2 starts transmitting at t=1.7.
For message 3 (t = 1.8): The sender of message 3 detects channel is idle at t = 1.8 (message 1 has finished, message 2 hasn't been detected), starts transmitting at t = 1.8. Then, messages 2 and 3 collide.
For message 4 (t = 2.5): The collision of messages 2 and 3 is ongoing until t=2.8; The sender of message 4 has to defer transmission.
For message 5 (t = 4.2): Collision ended at t=2.8, channel has been idle since t=3.0; Starts transmitting at t=4.2, completes at t=5.2; Signal propagates to other nodes by t=5.4
For message 6 (t = 4.6): Message 5 started at t=4.2, signal reached all nodes by t=4.4; At t=4.6, the channel is sensed as busy; The sender of message 6 has to defer transmission.
So: Successfully transmitted packets are messages 1 and 5.

Question 4 (6.3-4):
For message 1 (t = 0.3): Channel is idle; Starts transmitting at t = 0.3, completes at t = 1.3; Signal propagates to other nodes by t = 0.5.
For message 2 (t = 1.7): Message 1 finished at t = 1.3, and message 2's sender detects channel is idle since t = 1.5 (0.2 propagation delay); Message 2 starts transmitting at t=1.7.
For message 3 (t = 1.8): The sender of message 3 detects channel is idle at t = 1.8 (message 1 has finished, message 2 hasn't been detected), starts transmitting at t = 1.8. Then, messages 2 and 3 collide.
Key difference:
At t=1.9: Message 3's sender detects Message 2's signal → stops transmitting immediately
At t=2.0: Message 2's sender detects Message 3's signal → stops transmitting immediately
For message 4 (t = 2.5): Channel has been idle since t=2.2; At t=2.5, channel is sensed as idle; Message 4 was transmitted successfully from t=2.5 to t=3.5
For message 5 (t = 4.2): Message 4 ended at t=3.5, last bit propagates until t=3.7; So, at t=4.2, channel is idle; Message 5 starts transmitting at t=4.2, completes at t=5.2; Signal propagates to other nodes by t=5.4
For message 6 (t = 4.6): Message 5 started at t=4.2, signal reached all nodes by t=4.4; At t=4.6, the channel is sensed as busy; The sender of message 6 has to defer transmission.
So: Successfully transmitted packets are messages 1, 4, and 5.