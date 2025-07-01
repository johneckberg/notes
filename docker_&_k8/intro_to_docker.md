# Intro to Docker

## Docker V. Virtualization

- Virtualization: A process where software is used to create an abstraction layer.
- Hypervisor: a abstraction layer for VM's that manage the real physical resources of the underlying hardware. Helps VMs emulate resources.
  - Can be type 1 or type2. Type 1 hypervisors directly access underlying machine resources. They can implement their own custom resource allocation strategies to service their VMs. Type 2 hypervisors sit above the host operating system so they have to negotiate resource allocation with the operating system. This makes the process slower and less efficient.
- VM: each VM has its own virtual memory, cpu, os etc.
- Container: instead of virtualizing the underlying hardware, we virtualize the *operating system*.
  - Don't get this confused with Kernel Level Virtualization. 
- Docker Engine: Creates and runs containers and interacts with the OS kernel.
  - Control Groups: Allocate Resources
  - Name Space: restricts containers access and visibility into the system, isolating the environment
  - Docker Images: Standalone executable package for all an applications dependencies
  - Docker Files: Build Docker Images

## VM use cases

- You want to run one operating system on an operating system that your device isn't running (Linux VM on Windows)
- Stringent isolation between resources
- Can be useful for isolating legacy software & their arcane dependencies

## Container use cases

- Microservices Microservices Microservices
- Things we nee to quickly spin up and spin down (like for example a CI/CD job runner)
- They share the same host kernel, giving them a smaller footprint

## Dockerhub

- Docker Hub is a container registry built for developers and open source contributors to find, use, and share their container images.
- If docker can't find a container image locally, it will pull it from dockerhub.