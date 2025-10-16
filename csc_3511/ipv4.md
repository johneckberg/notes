# Week 6: IPv4

## Questions for Dr. Z
* What layers are process to process?
    * review quizzes theres a question about process to process

## IP Header
- length of the IP header is **not** fixed!
- IP layer is process to process? He's discussing the protocol number field in the header.
- IP checksum is very different than udp/tcp checksum 
    - checksum needs to be recalculated every hop because the ttl changes
- every link layer protocol has a specific MTU, or maximum transmission unit.
- IP address is attached to a specific interface

Version Field - b
b. This field contains the IP protocol version number.

Type-of-service field - h
h. This field contains ECN and differentiated service bits.

Fragmentation offset field - d
d. This field is used for datagram fragmentation/reassembly.

Time-to-live field - g
g. The value in this field is decremented at each router; when it reaches zero, the packet must be dropped.

Header checksum field - a
a. This field contains the Internet checksum of this datagram's header fields.

Upper layer field - e
e. This field contains the "protocol number" for the transport-layer protocol to which this datagram's payload will be demultiplexed - UDP or TCP, for example.

Payload/data field - c
c. This field contains a UDP or TCP segment, for example.

Datagram length field - f
f. This field indicates the total number of bytes in datagram


Link layer ensures
- Reliable data transfer between directly connected nodes.
- Flow control between directly connected nodes.
- Coordinated access to a shared physical medium.
- Bit-level error detection and correction.
- Multiplexing down from / multiplexing up to a network-layer protocol.

What is the maximum number of hosts possible in the larger 128.119.160/24 network? 256

How many bits are needed to be able to address all of the host in subnet A? 6

Suppose that subnet A has a CIDRized subnet address range of 128.119.160.128/26 (hint: 128 is 1000 0000 in binary); Subnet B has an CIDRied subnet address range of 128.119.160.64/26. We now want a valid CIDRized IP subnet address range for subnet C of the form 128.119.160.x/26. What is a valid value of x? 0