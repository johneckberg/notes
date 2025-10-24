# Week 8 Mid-term 

- similar number of questions, similar content. Open book, open note, no internet 

## Questions

## things to cover before thursday:

- congestion control graphing
    - Slow Start
        - slow start with exponential build in cwnd
    - loss via triple duplicate ack 
        - when triple duplicate ack detected, we decrease cwnd by half (SSThresh)
    - loss via timeout
        - when timeout detected, drop back 1, redo slow-start
    - SSTHRESH = cwnd/2
- socket syntax, UDP vs TCP python
    - Connection Setup:
    TCP uses listen(), accept(), and connect() to establish a connection. UDP does not establish a persistent connection; it sends and receives data directly using sendto() and recvfrom().
    Data Transfer:
    TCP uses send()/sendall() and recv() for data exchange over an established connection. UDP uses sendto() and recvfrom(), which include the destination/source address with each data packet.
    - TCP (Stream) Socket
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    - UDP (Datagram) Socket
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

- how to send a receive and packets, specify mac and IP address 
    - Sending packets on a lan using ARP:
    - Sending Packets
- udp guarantees?
    - best effort delivery
- review of sequence numbers
- dns time to live? done 
- Switches, dont change the mac address, routers do
    - source mac will be network interface at the router the network interface of the source is when taking intermediate hops. recall that the link layers only goal is to hop to hop 
- Calculating CRC bits
    - append a number of zeros equal to the CRC's bit length minus one to your data (add r), then perform binary division (using XOR) with the generator polynomial. recall that the xor operator is exclusive or, so 1 | 1 = 0, only 1 |0 or 0 | 1 is true/1. The final remainder of this division is the CRC value

- Aloha & CSMA done 
- Datagram vs packet vs frame, etc at each layer
- reading nslookup
    - did fine on that question, just remember that the value to the right of the domain name is TTL in SECONDS
- reading wireshark?
- Dijkstra's, dont update columns that have already been updated with the shortest path, see week 5 powerpoint (number 2 I think) 


Quesiton 7. a. facilitate application functions, he said transport layer is process to process, b. correct, c. Checksum, no discussion of application layer management, d. correct


### What layer's are process to process, host to host, etc.

* Checked this with him
link layer - node to node
IP layer, - host to host
Transport layer - process to process
Application layer - dont really care, all details of transport is now taken care of. 

* my understanding is: link layer is responsible for network node to network node, IP/internet layer is responsible for network host machine to network host machine, Transport layer is responsible for host machine process to host machine process by associating packets from the IP layer and attribute them to the correct application via port number. and Application is responsible for making this data usable for specific processes. It provides the applications with data to do something, but doesn't effect if/how/when the data gets to the machine via the network

#### What layers exclusively do what?
    
    * Link Layer: Framing, ARP, node to node transport via ARP
    * IP Layer: Host to Host, NAT, Packet Routing/Forwarding between different networks
    * Transport Layer: Process to process communication, service guarantees (only kinda true for udp), process to process multiplexing

## Properties of a MAC address: different in the textbook and quiz 

* **Note this is different than the textbook website** 6.4-2. Different types of addressing (b). We've now learned about both IPv4 addresses and MAC addresses.  Consider the address properties below, and use the pulldown menu to indicate  which of these properties is only a property of IPv4 addresses (and therefore is not a property of MAC addresses - careful!). 
Answer from textbook: Link layer address, This address remains the same as a host moves from one network to another, This is a 48-bit address.

## General large network stuff

- Content Delivery Networks/ Web Caches
- Internet as a network of networks
- ISP
- Internet Exchange Points 
- General idea of encapsulation 
- TCP/IP UDP/IP network model (application, transport, network, link)
    - What is the responsibility/actions of each layer
    - Define each of them

## Application Layer: HTTP

- HTTP Headers


## General Transport Layer stuff:

Neither Transport protocol has 

* Delay guarantees
* Bandwidth guarantees

## UDP

- header
- UDP guarantees

## TCP

- checksum (main thing is that its lightweight and easy)
    - Two's complement & binary calculation
- Header Fields
- performance guarantees
- TCP congestion control
- tcp flow control/ sliding window 
- writing out syn/ack numbers
    - Is the sequence number held in a cache? I guess im confused on why in the quiz 5 
    the Seq is repeated. I thought it worked by just taking the last seq and incrementing by the number of bytes? that the ack number it receives has no direct effect on what the sequence number is? I guess that doesnt make sense becuase if the seq doesnt match the ack the packet will get dropped
- those two methods of tcp transmission from quiz 5
    Stop and wait: send 1 packet per RTT
    Pipelined: send N packets per RTT
- when does re-transmission occur?


## IPv4

- Routing (dijkstra's)
- header fields 
- ipv4 subnetting 
- Channel partitioning
- Packet forwarding vs packet routing
    - Routing Tables
- NAT
- DHCP
- DNS (types; recursive, authoritative, etc)


## Link Layer

- Single Bit Parity Checking 
- 2-D Parity Checking
    - Detect & correct
- Cyclic Redundancy Check
    - Dont get lost in the linear algebra
    - Generator Polynomial
    - Binary Division by XOR
- MAC Address 
- multiple access protocols
- Switches vs Routers
- Why Link layer cant scale to internet (why we cant just use switches instead of routers)
- Self learning and forwarding
    - all the switch knows is what interface its sending out of or receiving in when sending a frame across switches 
- ARP: Address Resolution Protocol
    - Interaction between ARP and & IP forwarding tables (sending to another network)
    - In the lecture he provides a simplified example where the router is directly connected to both LANs

## A day in the life of a (google) web request



- Boot up computer
- First, get an IP address via DHCP
- You boot up your web browser, type in the URL
- Once you hit send, your browser begins the steps to get the data to form the HTTP request.
    -  A DNS query is formed from the URL & your browser sends a DNS query to a DNS resolver
    - Port: Can you specify a port in the URL? yes. Do people? no not typically, so its assumed by convention (default port)
    - Once the IP & port are known, we then establish the TCP handshake (if using a http version before http/3)
- Then finally, we can form & send the HTTP request
- This goes from your local network, through your router, to your ISP, to the web cache or web server hosting the site, or at least the site proxy/gateway most likely via public peering, which happens at IXPs
    - This gets deeper into BGP stuff that we will learn about later 
- We get the HTTP reply of the web sever and the clients web browser begins to process the HTML document we requested 
    - The browser starts reading the html from the top, and starts fetching all CSS and JavaScript files referenced in the HEAD section. The page will not be painted (shown) until all the CSS and JavaScript files in the HEAD have been downloaded and evaluated.
    - see [pre-load html attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload)