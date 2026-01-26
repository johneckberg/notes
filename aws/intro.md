# Intro to AWS

## Setup

* billing setup
* root vs IAM user login
  * setting user permissions
* Cloudwatch monitoring setup
* MFA setup 

## Domain 1: Cloud Concepts

* Task Statement 1.1: Define the benefits of the AWS Cloud
  * trade capex for opex, pay for what you consume
  * economies of scale
  * Scalability
  * Speed and agility
  * No spend on on prem data center specific operating costs
  * Deploy globally
  * Security 
  * Reliability 
  * Cloud providers keep things current (hardware, software etc)
* Task Statement 1.2: Identify design principles of the AWS Cloud
  * s
* Task Statement 1.3: Understand the benefits of and strategies for migration to the AWS Cloud
* Task Statement 1.4: Understand concepts of cloud economics

* An AWS Region is a large, distinct geographic area (like "US East") containing multiple isolated, physically separate data centers called Availability Zones (AZs), which each have independent power, cooling, and networking for high availability.
  * Regions are just a description for a general geographic location. AZs are clusters of multiple data centers - you can think of them like a collection of buildings in a business park. To the end user, the data centers themselves are abstracted away - you just think of things at the AZ level holistically.
  * AZs in the same Region are built to be in different failure zones, so in separate flood plains, fault zones, different utility suppliers, etc. But they are close enough to be connected by high speed links, so latency between AZs in the same Region is often sub-ms or 1-2ms at most. Most applications can be deployed across AZs in the same Region without any noticeable performance hit. 

* AWS services are either Regional (tied to a specific geographic location like us-east-1 for data and control) or Global (managed from a single endpoint, with data distributed worldwide for broad access). Regional services (like EC2, RDS) offer locality and cost benefits, while Global services (IAM, Route 53, CloudFront, WAF) provide centralized management and content distribution for multi-region architectures. S3 is a hybrid: buckets are regional, but data is accessible globally
  * Generally, anything that allows you lots of granular control is going to have an AZ setup. Anything that does not open up specific controls / allows you to configure it minutely is usually regional. 

* Horizontal v.s. Vertical Scaling:
  * More servers vs bigger server

## Domain 2: Security and Compliance

## Content Domain 3: Cloud Technology and Services

## Content Domain 4: Billing, Pricing, and Support