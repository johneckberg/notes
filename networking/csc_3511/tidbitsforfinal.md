# things from the practice test & from the mid-term

## MAC vs PKI

* MAC (Message Authentication Code) provides message integrity & authenticity using a shared secret key (symmetric), ideal for fast checks like verifying a file hasn't changed, while PKI (Public Key Infrastructure) uses asymmetric keys (public/private) & certificates for identity, non-repudiation, and scalable trust (like digital signatures), underpinning secure web (TLS), email, and device authentication, but involves more overhead because asymmetric encryption is heavier than symmetric

* How does confidentiality work with TLS? This is where the symmetric secret key stuff comes in. HMAC provides message integrity and authenticity, proving data hasn't changed and comes from a trusted source, but does not offer confidentiality.

## See week #11 notes for credit card ATM example

## See week #11 notes for MAC vs HMAC


## Notes on what you messed up with regards to the Dijkstra's shortest path

* how do we choose the starting node? its just in the far left column starting set for N'

![alt text](dijkstra.png)

**Remember, the big focus for is is 1. Authentication and 2. Integrity. Can we very who sent us the message, and can we verify it hasnt been tampered with?**

* Integrity: Can the recipient be confident that the message has not been accidentally modified?

* Authentication: Can the recipient be confident that the message originates from the sender?

* Non-repudiation: If the recipient passes the message and the proof to a third party, can the third party be confident that the message originated from the sender?

![alt text](macvssignature.png)


## Ownership vs issuer of a CA

