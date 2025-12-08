# Week 10 notes: Encryption week

## AES is a block cipher, ChaCha20 is a stream cipher

## Lecture 1: One-Time Pads, Stream Cipher, and Block Cipher

* Efficient attack scheme means faster than brute force

* Practical issue: from a security perspective, we would prefer to not re-use keys, but from a practical perspective, key generation is expensive and we would like to re-use keys because of this...

* You would want to convert a Block Cipher (like AES) into a Stream Cipher to achieve the benefits of stream encryption, primarily when encrypting arbitrarily long data streams or when speed and low latency are critical, even though block ciphers are not inherently designed for this.
  * But why not just use a stream cipher in the first place?
  * smaller library less moving parts to deal with, some companies support only AES because

* Every encryption algorithm has three components:
  1. Key Generation
  2. Encryption
  3. Decryption

* Claude Shannon proposed that there are two primitives with which strong encryptions algorithms can be built
  1. Confusion: an operation where the relationship between the key and ciphertext is obscured
  2. Diffusion: an operation where the influence of one plaintext symbol is spread over many ciphertext symbols with the goal of hiding the statistical properties/pattern in the plaintext
* Both operations by themselves cannot provide security, the idea is to mix elements to build security. Like for example diffusion 1 -> confusion 1 -> diffusion -> 2 -> confusion 2 ->...

### One-Time Pads

* Nice property of XOR: (x XOR y)XOR x = y
* This is in the symmetric key setting, so we assume both alice and bob know this key (share the key)
* The key is a randomly chosen bitstring; the key is equal length to the message
* Problems to solve that we can't solve with this basic scheme
  1. Key Exchange
  2. Key re-use
* The message is encoded by taking the XOR between the key and the message
* The message is de-coded by taking the XOR between the Key and the cypher
* Intuition of why this is secure: for a random encryption key, the distribution over the cypher bits is random (this doesn't really help me)

* So what happens if we re-use a key? The attacker can take the XOR between both messages

* Part of the issue is that the key must be the same length as the data, so 1 GB key for 1 GB data

### Stream Cypher

* Family of Encryption Algorithms

* QUICK NOTE: pseudo-random can be informally defined as some sequence that can not be distinguished from uniform sampling. More formally, you have to pass a set of statistical tests to be truly pseudo-random
  * NIST SP 800-90A provides the statistical tests

* ChaCha20
  * He made a special note about making sure we understand the initialization vector

* So how to we generate actually random stuff? We collect sources of entropy from the real world (hopefully our computer hardware, maybe using the unpredictable behavior of hardware interrupts)
  * There are NIST approved RNGs

## Block Cypher

* **we should know that DES is a block cypher and that its unsecure**

* A family of cryptographic algorithms consisting for fixed size blocks of bits

* Note on how DES is bad

* Note on S-box

* Note on Feistel network. Encrypts half of the plaintext each round 

* AES was introduced by NIST as a more secure block cypher in 2001. As of right now, AES 128 is secure
  * AES uses a substitution-permutation network 

## Lecture 2: Public Key Cryptography, RSA




