# Lab 9: DNS Attack

* tasks 4 & 5 not required 
* Code skeleton; need to just quick implement the rest. Don't think it will be a lot
* Task one code is swapping headers, creating DNS payload, stack them together 

* Spoofing a dns packet takes time; so we need to reduce the speed of traffic between the internet and and local dns server/cache so we run a command to delay the network traffic by 100ms on each container? (maybe just the router) for each task 

* Task 1 & 2 is spoofing type A record
* Task 1: launch a dns spoofing attack
  * First will keep attacker program running
  * switch to user: user will do dns query via dig
  * Then the attacker can send the spoofed response
  * should be able to see the response to the spoofed packet via the print command 
  * terminate the attackers program, then repeat the query and hit the actual local dns server and get the real dns record 
* Task 2: Spoof the local 
  * RNDC flush?
  * Next, we run attacker code
  * in this task the target is the router, not a host on the network 
  * perform request on host
  * dump router cache to see if the attack worked 
    * its gonna be long as hell but you should be able to find the record by coming through it 
* Task 3: Spoofing NS records
  * attacker is a fake authority server for the local dns server
  * flush dns cache on router to confirm this attack works
