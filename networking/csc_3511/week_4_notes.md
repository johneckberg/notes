# Week 4 Notes: TCP protocol

## Things that tripped me up on this weeks quiz

* This is from quiz #3 but i think it fits better here in the tcp section: * 2.7-4 How many sockets? Suppose a Web server has five ongoing connections that use TCP receiver port 80, and assume there are no other TCP connections (open or being opened or closed) at that server.  How many TCP sockets are in use at this server?: 6; one listening socket

## Reliable Data Transmission

TCP (Transmission Control Protocol) implements reliability mechanisms on top of IP's unreliable (best-effort) service model to ensure data is delivered **exactly once** and **in order**.

| Issue | TCP Mechanism | How It Works |
| :--- | :--- | :--- |
| **Packets can be dropped** | **Acknowledgments (ACKs) and Retransmission Timers** | The sender sets a **timer** after sending a segment. The receiver sends a **cumulative ACK** indicating the sequence number of the *next* byte it expects. If the timer expires before the expected ACK arrives, the sender assumes the segment is lost and **retransmits** it. The sender also uses **Fast Retransmit**, resending data upon receiving three duplicate ACKs. |
| **Packets can be corrupted** | **Checksums** | Both the sender and receiver calculate a **checksum** for the segment header and data. If the receiver's calculated checksum does not match the one in the header, the segment is considered corrupt and is **silently discarded**. Since the receiver does not send an ACK for the dropped segment, a timeout occurs on the sender, triggering a retransmission of the data. |
| **Packets can be delayed** | **Dynamic RTT Estimation and Sequence Numbers** | **Delays** are mostly managed by the retransmission mechanism. TCP dynamically calculates the Round Trip Time (**RTT**) to set an appropriate timer value, minimizing unnecessary retransmissions due to minor delays. If a segment is delayed so long it causes a premature timeout and a duplicate is sent, the receiver uses the **sequence number** (see below) to discard the late-arriving original segment. |
| **Packets can be duplicated** | **Sequence Numbers** | TCP uses **byte-level sequence numbers** to identify the data payload in each segment. The receiver keeps track of the highest sequence number received so far. If a duplicate segment arrives (e.g., due to a delayed segment arriving after a retransmission), the receiver detects the redundant sequence number and **discards** the duplicate data, ensuring **exactly-once delivery**. |
| **Packets can be re-ordered** | **Sequence Numbers and Receiver Buffering** | The **sequence numbers** allow the receiver to determine the correct order of the data segments, even if they arrive out of sequence. The receiver uses a **buffer** to hold any segments that arrive out-of-order until the missing preceding segments are received. Data is only passed up to the application layer **in correct sequence**. |


## TCP congestion control

    - Slow Start
        - slow start with exponential build in cwnd
    - loss via triple duplicate ack 
        - when triple duplicate ack detected, we decrease cwnd by half (SSThresh)
    - loss via timeout
        - when timeout detected, drop back 1, redo slow-start

![alt text](congestioncontrol.png)
