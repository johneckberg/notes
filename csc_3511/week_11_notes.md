# Week 11: Focus on Integrity 

## Lecture 1: Digital Signatures, Certificates, PKI

### Digital Signatures

Big idea: Digital signatures are an asymmetric way of providing integrity and authenticity to data

This first slide deck has a great review of what we covered for public-key cryptography

### Certificates and Chain of trust

* A certificate is a signed endorsement/signature of someones public key. It contains two things, the identity and the key

* Issue: No mechanism to verify that a public key belongs to its claimed owner

* So how do we make a chain of trust? You cannot gain trust if you trust nothing. You need a root of trust!

* EvanBot: EvanBot is our trust anchor (root of trust)
  * Alice wants Bob’s public key. Alice trusts EvanBot
* We can expand/scale this idea to a **Hierarchal Trust Chain**
  * The root of trust (trusted directory) may delegate trust and signing power to other authorities
  * We can get around the brittleness of this scheme (single point of failure being root node) by creating multiple trust anchors.
  * Public keys are hard-coded into operating systems and devices

* We can use OpenSSL on the SEED virtual machine to obtain Google's certificate chain, or we can open cmd and type “certmgr.msc” to browse certificate chains on windows
  * Read cert chain from bottom to top, where the top is the for example web server, and you work up the chain

### PKI: Public Key Infrastructure

## Day 3:

### What makes a good hash function?

* our goal here is just to learn what makes a good fash function and when we need to use one 

* good hash functions should be deterministic
* good hash functions should be unpredictable
* good hash functions should be resistant to collisions 
* good hash functions should be one-way; near impossible to reverse

* he makes a note that because hash functions map variable length data to a fixed length, there are technically infinite collisions for a certain hash in the hash table

* he makes a note that hash functions don't give confidentiality, they make leak data

### Message Authentication Codes (MACs)

* MACs provide integrity
* NMAC (nested mac) is secure
* HMAC (hash-based mac) 
  * only requires one key
  * he said this is a good choice, more popular 

* note on how macs probably cant provide authenticity; researchers think it cant, but maybe dont know for sure
  * he said look into AEAD

### Diffie-Hellman Key Exchange

* funny note; apparently the paper was initially rejected from a journal for being too radical
* Relies on the discrete log problem 

* vulnerable to man in the middle attack 
  * can be solved via digital signatures
  * can also be solved if the parties have a pre-shared secret key. with this, we can authenticate the d-f params via MAC
    * so why if they already have a shared private key, why do we need d-f?
      * d-f provides forward secrecy