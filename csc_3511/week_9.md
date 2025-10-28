# DNS Vulnerabilities & Attacks

## A Quick DNS review:

* A map between hostnames and IP addresses
* Name servers are arranged in a hierarchy 

## What exactly is in a DNS packet?

* Source & destination IP addresses
* Source and Destination Port numbers
* Query ID
* Counts 

## DNS Caching

* DNS responses are cached locally for quick translations
* Attach a TTL to the cached record so they time out and dont stay in the cache even though they may be wrong as the IP for the server has now changes
* DNS negative queries are also cached (sites that dont exist, mis-spelling of the actual domain name)

## Why Care about DNS security?

* Trust and the stability of the DNS system as a whole drives the global economy. Nobody, not even tech bros want to type in the IP address of a site, especially considering that is constantly subject to change.

* DNS hijacking occurs when the actor can illicitly modify DNS name records to point users to actor-controlled servers

## DNS Threat Model

* Malicious name server, external attacker
* Attacks that can be launched: Forged DNS data, Hijacked DNS name server
* DNS flood

### Malicious Name Servers

* Malicious name servers can lie and supply a malicious answer
* Malicious records could also poison the cache with other records
* DNS query results include Additional Records section:
* Provide records for anticipated next resolution step