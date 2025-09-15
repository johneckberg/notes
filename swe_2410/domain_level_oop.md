# Domain-Level Object Oriented Programming (Domain Driven Design)

- trying to present this like some silly version of platonic ideals?
[a good ddd link](https://alok-mishra.com/2021/06/22/user-journey-user-story-and-domain-story-a-visual-guide/)

- Domain level/driven design is primarily useful in situations with high business complexity and low technical complexity.
- **I truly believe that everything is a design job, this seems in the spirit of DDD**
- I think I'm struggling with the idea that this is being presented as THE way to do OOP not A way.

- [see reddit](https://www.reddit.com/r/ExperiencedDevs/comments/1gpfn6x/if_discord_reddit_twitter_and_uber_dont_use_ddd/)" There are fundamentally two types of (large) websites: deep-first, and broad-first.

A deep-first website is like the ideal function: it does one thing, and does it well. Twitter and Reddit probably only has 20-30 core functions (read feed, post comment, subscribe, etc.) but they need to do it very well, very fast, and scale to millions of users and billions of requests every day.

A broad-first website is your typical enterprise app. It's designed for a a relatively small number of users, and comparatively light load (at least where performance is concerned, heavy-load tasks can usually be extracted to async jobs without users complaining too much about the delay.) So instead of primary performance considerations, you have other problems, such as making sure hundreds of core functions, developed by multiple teams, all work together consistently. As well, you are adding many more functions and need many more refactors, compared to a depth-first site, and the core requirements may rapidly change as the business grows. Your main concerns are now not how performant the app is, but how reliably can you add and change features, and how well these features align with corporate requirements.

DDD is much more important to breadth-first software than depth-first software, because the things it emphasizes allow for better organizational scaling, rather than request scaling. "

- domain classes:
  - Persist across problem changes
  - Capture the fundamental things that clients and users will recognize 
  - Capture the requirements of the objects in the system

- Classes are defined by their responsibilities to the rest of the system
  - A class should should have 1 responsibility. He says, "Just one, but there are exceptions; no more than three"
  - "Classes should have 10-20 lines of code" I'm pretty sure he said classes but this sounds insane?? **DOUBLE CHECK with him, did I mishear him? did he say methods?**
  - Okay I'm reading that this is called the Single Responsibility Principle, "responsibility" exists only as an abstract concept. For example is it a responsibility of a car to drive? Yeah, so functions like drive() or steer() belong in that class. However is it a responsibility of a car to repair itself? Not really, repair() just like that probably isn't the best choice here. My understanding is that the class’s single responsibility is to model/represent something. That will require as many methods as necessary. But each method should itself have a single responsibility


- **Domain Objects have identity**
- **An Object is something with:**
  - **Responsibility, Identity, Behavior, and State (RIBS)**
- We need to understand the user stories and the requirements that arise from them. The requirements should be self evident from the user stories
- User stories represent a timeline of what the user wants do to/has to do and the scenarios that might arise from those actions. User Stories like, "I'm an x and i want to do y"
- From the DDD link above "Is a technique to describe specific functions the user must perform at each stage of a journey."
**IS THIS TOO ABSTRACT OF A DEFINITION? IS THIS A GOOD DEFINITION? YES OR NO? IF IT IS, WHAT NEEDS TO CHANGE?**
**I dont think this is the same definition of user story from Agile**

## The Domain-Level Object Oriented Programming Design Process 

1. Start with domain classes
– These persist across problem changes
– Capture things clients, users will recognize
– Capture requirements that go with those items
2. Explore interactions through sequence and state diagrams
3. Add containers, architectural elements
– Decisions about time/space/complexity tradeoffs
– Databases, network communications, GUI elements
4. Introduce design patterns, refine
– These generally reduce coupling, increase cohesion
– May REMOVE classes from previous steps
– Be careful about removing domain classes!

Preference for domain classes over solution-space
(implementation-specific) classes