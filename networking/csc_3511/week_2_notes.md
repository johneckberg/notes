# CSC 3511 Security and Networking - Week 2 Notes

## Things that tripped me up on this weeks quiz

* This is from the week #3 quiz but I think it fits better here: 2.2-13 Cookies. What is the purpose of a cookie value in the HTTP GET request?: The cookie value itself doesn't mean anything.  It is just a value that was returned by a web server to this client during an earlier interaction. 

### Lecture 1: Network Structure

#### 1. The Internet Overview

* The Internet is a vast "network of networks."
* It consists of billions of connected computing devices.

| Component | Description | Examples |
| :--- | :--- | :--- |
| **Network Edge (Hosts/End Systems)** | Devices running network applications. | PCs, smartphones, servers, smart devices. |
| **Network Core (Packet Switches)** | Forward packets (chunks of data). | Routers, switches. |
| **Communication Links** | Connect the devices and switches. | Fiber, copper, radio, satellite. |
| **Transmission Rate (Bandwidth)** | The rate at which data is transmitted. | |

#### 2. Protocols

* **Definition:** Protocols define the format and order of messages sent and received among network entities, as well as the actions taken upon transmission or receipt.
* **Function:** All communication activity in the Internet is governed by network protocols.

#### 3. Network Core Functions: Routing vs. Forwarding

The network core performs two key functions to move packets:

* **Routing (Global Action):**
    * Finds paths through the network.
    * Determines the source-destination paths taken by packets using **routing algorithms**.
* **Forwarding (Local Action / Switching):**
    * Local action performed at each router.
    * Moves an arriving packet from the router's input link to the appropriate output link based on a **local forwarding table**.

#### 4. Internet Structure: Network of Networks

* **Access ISPs:** Provide the physical connection and IP address to hosts (e.g., residential, mobile).
* **Hierarchical Structure:** To manage scale, Access ISPs connect to **Regional ISPs**, which connect to large **"Tier-1" Commercial ISPs** (national/international coverage).
* **Interconnection:** Networks connect at **Internet Exchange Points (IXPs)**.
* **Content Provider Networks (CPNs):** Large companies (e.g., Google, Facebook) run their own private networks to deliver content closer to users, often bypassing ISP tiers.

#### 5. Internet Layering: TCP/IP Model

The internet uses a layered abstraction:

| Layer | Name | Protocols/Technologies | Service Provided |
| :--- | :--- | :--- | :--- |
| **5** | **Application** | HTTP, FTP, SMTP, DNS | Implement services on top of the infrastructure. |
| **4** | **Transport** | TCP, UDP | Reliably deliver packets, forming connections. |
| **3** | **Network** | IP, ICMP | Connect many local networks to form the Internet. |
| **2** | **Link** | Ethernet, Wi-Fi | Create links in a local network. |
| **1** | **Physical** | Copper, Fiber, Radio | Move bits across space. |

#### 6. Encapsulation and Decapsulation

* **Encapsulation (Sender):** As a packet moves from a higher layer to a lower layer, additional headers (and sometimes a trailer) are wrapped around the packet.
* **Decapsulation (Receiver):** As a packet moves from a lower layer to a higher layer, headers are peeled off.
* **Layer Interaction:** Peers at the same layer communicate with each other using the header specific to that layer.

---

### Lecture 2: Application Layer and HTTP

#### 1. Application Communication: Processes & Sockets

* **Process:** A program running within a host.
* **Network Application:** Programs running on different end systems that exchange messages over a network.
* **Client vs. Server:**
    * **Client Process:** Initiates communication.
    * **Server Process:** Waits to be contacted.
* **Socket:** The network interface where a process sends and receives messages.
* **Process Identifier:** A process is identified by the combination of its host's **IP Address** and the process's **Port Number** (e.g., HTTP server uses port 80).

#### 2. Application Architectures

| Architecture | Description | Examples |
| :--- | :--- | :--- |
| **Client-Server** | Server is an always-on host; clients connect intermittently and do not communicate directly. | HTTP, IMAP, FTP. |
| **Peer-to-Peer (P2P)** | No always-on server; arbitrary end systems communicate directly and provide/request service from each other. | P2P file sharing (e.g., BitTorrent). |

#### 3. HTTP (HyperText Transfer Protocol)

* HTTP is the protocol for Web browsers to request resources from Web servers.
* **Properties:**
    * **Client-Server Protocol.**
    * **Request-Response Protocol:** Client sends a request, receives one response.
    * **Stateless:** The server maintains no information about past client requests.
    * **Runs over TCP:** Ensures reliable, in-order data transfer.
    * **Default Port:** 80 (HTTP) or 443 (HTTPS).

* **HTTP Request Messages:** Human-readable plaintext, including **Method** (`GET`, `POST`), **URL**, and **HTTP Version**.
* **HTTP Response Messages:** Includes **HTTP Version**, **Status Code**, Description, and **Content**.
    * **Status Code Categories:** `200s` (Successful), `400s` (Client error, e.g., `404 Not Found`), `500s` (Server error).

#### 4. Speeding Up HTTP: Web Caching

* **Web Cache (Proxy Server):** A local server that stores copies of frequently requested web content closer to the client.
* **Process:** Client sends requests to the cache. If the object is not in the cache, the cache fetches it from the origin server, saves a copy, and returns it to the client.
* **Benefits:** Reduces client response time and reduces traffic on the institution's access link.
* **Note** A content delivery network (CDN) is a geographically distributed group of web cache servers. A CDN allows for the quick transfer of assets needed for loading Internet content, including HTML pages, JavaScript files, stylesheets, images, and videos.

#### 5. Network Performance: Delay, Loss, and Throughput

| Delay Component | Formula (if applicable) | Description |
| :--- | :--- | :--- |
| **Processing Delay ($d_{\text{proc}}$)** | - | Time to check bit errors and determine the output link at a node (router). |
| **Queueing Delay ($d_{\text{queue}}$)** | - | Time waiting in the router's output buffer; depends on network congestion. |
| **Transmission Delay ($d_{\text{trans}}$)** | $L/R$ | Time to push all packet bits (length $L$) onto the link (rate $R$). |
| **Propagation Delay ($d_{\text{prop}}$)** | $d/s$ | Time for the signal to travel across the physical link (length $d$, speed $s$). |

* **Total Nodal Delay:** $d_{\text{nodal}} = d_{\text{proc}} + d_{\text{queue}} + d_{\text{trans}} + d_{\text{prop}}$.
* **Packet Loss:** Occurs when packets arrive at a full router buffer (buffer overflow) and must be dropped.
* **Throughput:** The rate at which bits are transferred from sender to receiver.
* **Bottleneck Link:** The link on the end-to-end path that constrains the overall throughput.

#### 6. Maintaining State: Cookies

* **Cookies** are used to maintain state because HTTP is stateless.
* **How they work:**
    1.  Server's response includes a `Set-cookie` header with a unique ID.
    2.  Client stores this ID locally.
    3.  Subsequent requests from the client include the `Cookie` header line with the ID.
    4.  Server uses the ID to look up the client's state in its database.
* **First-party cookie:** From the website you directly visited.
* **Third-party cookie (tracking cookie):** From a different, embedded website (e.g., an ad network) used to track a user's identity across multiple independent sites.