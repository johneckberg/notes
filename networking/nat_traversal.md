# NAT and its problems (NAT Traversal)

## Big Idea: NAT creates the problem, and NAT traversal techniques, like UDP hole punching and port forwarding, are solutions to that problem.

A NAT's primary function is to translate private IP addresses to a single public IP address, conserving IPv4 addresses. So how do we talk to another machine behind one nat while we're behind another? We need to do **NAT Traversal**!

