# Week 12 Notes

## Week 12, Lecture 1: Transport Layer Security

### TLS Handshake Protocol

* Big Idea: Enabling security at the Transport layer. To avoiding sniffing & spoofing attacks, we need our data to have *confidentiality*

* TLS sits between transport and application layer
* Replaces SSL (secure socket) which is an older version of the same idea

#### TLS Handshake

* Step 1: Exchange Hellos
  * The client sends ClientHello with
    * A 256-bit random number RC (“client random”)
    * A list of supported cryptographic algorithms (Cipher Spec)
  * The server sends ServerHello with
    * A 256-bit random number RS (“server random”)
    * The algorithms to use (chosen from the client’s list)
* Step 2: Certificate
  * Server sends its certificate containing:
    * public key signed by a trusted certificate authority
  * Client validates signature certificate
  * **HOWEVER** The client is not yet sure that they are talking to the legitimate server (not an impersonator). Certificates are public. Anyone can provide a certificate for anybody
* Step 3: Premaster Secret
  * Make sure the client is talking to the legitimate server
    * Because the attacker can collect legitimate certificates, the server must prove that it owns the private key corresponding to the public key in the certificate
    * The RSA version has been deprecated (maybe all versions?) because it lacks forward secrecy
* Step 4: Derive Symmetric Keys
  * Derive 4 keys
    * CC: For encrypting client-to-server messages
    * CS: For encrypting server-to-client messages
    * IC: For MACing client-to-server messages
    * IS: For MACing server-to-client messages
    * Note: Both client and server know all four keys
* Step 5: Exchange MACs
  * With MACs, any tampering on the handshake will be detected
* Step 6: Send Messages
  * Two approaches: Encrypt-then-MAC, MAC-then-encrypt
    * Modern cryptographic best practices favor Encrypt-then-MAC, where the message is first encrypted, and the MAC is calculated over the ciphertext.
**Now we can send messages securely!**

#### TLS Guarantees

* TLS prevents the attacker from knowing who you are talking to, not what you are talking about. It focuses on application layer
* Talking to the Legitimate Server 
* Securing Messages
* Replay Attacks
* Forward Secrecy
* Provides End-to-End Security

## Week 12, Lecture 2: DNS security

### DNS over TLS

* Bare metal DNS has no methods for verifying the correctness of the response. We would like to add authenticity and integrity to prevent things like the kaminsky DNS attack.

* TLS, easy solution

### DNSSEC

As always, we have a trade-off between security and speed; we assume a lot (all?) of the higher level dns servers we delegate to are not compromised