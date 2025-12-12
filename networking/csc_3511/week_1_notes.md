# Security and Networking Week 1

## The Internet: A Nuts and Bolts View

* **Network Edge:** Consists of billions of connected **hosts** or **end systems** (computing devices) running network applications.
* **Network Core:** Made up of **packet switches** (routers and switches) that forward packets (chunks of data).
* **Communication Links:** Connect devices using technologies like **fiber**, **copper**, **radio**, or **satellite**.
    * The **transmission rate** of a link is referred to as its **bandwidth**.
* **Networks** are collections of devices, routers, and links managed by a single organization (e.g., mobile network, home network, datacenter network, national ISP).
* **Infrastructure Services:** The Internet provides services for applications such as the **Web**, streaming video, email, e-commerce, and social media.

---

## Protocols and Layering

* **Protocols:** Govern all communication on the Internet.
    * They define the **format** and **order** of messages sent and received among network entities.
    * Examples include **HTTP**, **TCP**, **IP**, and **Wi-Fi**.
* **Internet Standards:** Are developed by the **IETF** (Internet Engineering Task Force) and published as **RFCs** (Request for Comments).
* **Internet Layering (Abstraction):**
    * The Internet design is partitioned into different layers, where each layer provides services to the layer above it and relies on the layer below it.
    * This design ensures a change in one layer (like a physical wire) does not break the others.
* **TCP/IP Model (The Practical Model):** The course content follows this 5-layer model:
    1.  **Application Layer:** (e.g., HTTP, FTP, SMTP, DNS)
    2.  **Transport Layer:** (e.g., TCP, UDP)
    3.  **Internet (Network) Layer:** (e.g., IP, ICMP)
    4.  **Link Layer:** (e.g., Ethernet, Wi-Fi)
    5.  **Physical Layer:** (e.g., Copper, Fiber, Radio)

---

## Network Security and Attacks

* The Internet was not initially designed with robust security in mind, leading to current security considerations being necessary across all layers.
* A network is **only as secure as its single weakest layer** or the interconnection between layers.
* **Common Attacks:**
    * **Packet Sniffing:** Using a promiscuous network interface to read and record all packets passing by on broadcast media (e.g., capturing passwords). **Wireshark** is a common tool for this.
    * **Denial of Service (DoS):** Attackers make a resource (server, bandwidth) unavailable to legitimate users by overwhelming it with bogus traffic.

### Security Requirements and How to Address Them

| Requirement | Scenarios/Goal | How to Implement |
| :--- | :--- | :--- |
| **Confidentiality** | Protecting vital information (e.g., trade secrets, medical records). | Encrypted communications, secure transactions. |
| **Integrity** | Ensuring data integrity and preventing unauthorized modification (e.g., financial transactions, software updates). | Digital signatures, Message Authentication Codes (MAC). |
| **Authentication & Access Control** | Verifying user identity to control access to resources (e.g., online banking, restricted databases). | Multi-Factor Authentication (MFA), Public Key Infrastructure (PKI), biometric verification. |
| **Availability** | Guaranteeing access to resources (e.g., cloud services, critical infrastructure systems). | Redundant systems, load balancing. |