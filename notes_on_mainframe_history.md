# Back to Big Iron:

## Cloud notes

Cloud is useful because you longer have to worry about the mapping of code to the hardware that will run it. You pay up front for designing the code around the architecture, but you win every time it runs in that theres essentially zero maintenance overhead associated with it. This is compared to a mainframe; you sling your app on the mainframe, ask for resources and let it run. If you run out of capacity, buy another mainframe and link it to the old one. Need a new region/reliability zone? pay a license, install a fat network link and jobs golden. However, this tight coupling of code/process/data/apps to the platform is why mainframe migrations have a strong tendency to crash and burn. On prem and hiring for the most niche and aging developers in the world with high chance for catastrophe when things go awry isn't cheap either.

Capex vs Opex

Remember: “the cloud” is not just a buzzword for “someone else’s computer”. It wouldn't be as popular then. It's a buzzword for someone else's computer, networking, data centres, custom managed services, and very importantly, control plane. You telling me you can guarantee the same or better upkeep as AWS / Google Cloud with your own on-premises solution? And even if you could keep up (doubt)- at what cost is that kind of oversight going to come at?

The cloud is a no-brainer for most. Unless you value complete freedom / control over your hosting or have insanely low latency requirements. Which some hardos do. Not weird to read Linux admin threads and see cloud hate.

Part of the benefits of cloud is virtualization for networking hardware not just computing hardware

People seem to be arguing about what hardware runs cloud services at the end of the day. Obviously part of the point is to have a variety of compute nodes; some services to provide cloud access to mainframes but others  **are just big banks of consumer grade cpus.**

## Note from Reddit

So, I've worked in one of the few sectors that actually still needs mainframes to run its core business (airlines/air transport) for quite a while. There truly is demand in banking. transportation and utilities where you need a bulletproof system that won't sell the same seat twice or forget to credit an account during a wire transfer or fail when managing the electric grid. Companies have migrated almost everything they can off the mainframe because it's so expensive to run, and what's left is the stuff that truly cannot be allowed to fail and actually needs that RAS and massive shared data model. That's the stuff you can't have untrained idiots or cowboy 20-deploys-a-day DevOps people running.

I see a TON of parallels with the cloud. Around 2013 or so was when the "VMs and data centers are for dinosaurs, migrate to Azure/AWS now!" drums really started beating outside of Big Tech and 2010s startups. Anything on-prem was and still is labeled legacy. All the cloud vendors gave away free training, free service, anything to get companies to lock their workloads in with them. The freebies have been scaled back a bit but they're still there to catch the stragglers. This all but ensures that new people entering the field are going to skip learning the fundamentals and jump straight into DevOps bootcamp. By labeling anything outside a cloud as old, the cloud providers are paralleling the mainframe customers of the 90s and 2000s when it was all about sending all that work off to some Indian body shop. For 20 years mainframes have been a backwater and people have avoided learning them because the CIO will just go golfing with the Infosys guy and send their job offshore when the price is right. I still have 20 years left to retirement, and I wonder if there will be a similar situation with companies who can't or don't want to use the cloud and can't find anyone who knows how a computer that isn't abstracted behind an API works anymore.

IBM would have a huge road to convince people to spend the effort learning mainframe skills. Previous efforts have targeted India and other developing markets because that's where mainframe customers send the work and need the cheap bodies...but it would be very interesting to see what would happen if demand was stoked in people in the US/Europe. It would be a great semi-retirement job for people who have a wealth of experience and enough fundamentals knowledge to even comprehend something as ancient as CICS or JCL or punch-card analogies in file structure.

## Mainframe vs supercomputer

### The UNIVAC 1103 was around 60 feet long, 30 feet wide, and weighed over 17 tons

But to dig in; we need to define what a supercomputer is; and that starts with the CDC 6600. These days Cray is pretty much just a nameplate that HPE uses for Nvidia based gpu servers, and before cray the distinction between mainframes and supercomputers was very blurry. The CDC 6600 standouts from precursors and contemporaries like the univac 1107 or 1103 or CDC 1604 because its production was not at all limited by silly things like software compatibility or cost. No hardware engineering trade offs, no software technical debt, just speed. It was liquid nitrogen cooled, cost roughly 7 million per unit (not adjusted for inflation) and obviously never made money. It wasn’t supposed to. Similar in philosophy to the IBM stretch, except IBM stretch cost 13.5 million initially and **definitely** didn’t make money. IBM for their credit realized that things like “compatibility” and “portability” mattered and came out with the system 360 and the rest is history. CDC for their part had plenty of government contracts and a successful peripherals business, until all they had was the peripherals business which sold to seagate(I got to tour the facility when I was a kid). Big difference now is purpose and metrics: supercomputers care about flops while mainframes care about reliable transaction handling and often use MIPs:millions of instructions per second. Supercomputers are designed for high performance scientific computing while mainframes are designed for frankly pretty much just things like transaction handling. For example, cray (the company which the man left because he wanted to engineer) started just measuring performance in solely FLOPS in the 80s as the supercomputers began to use vector processors more. Cray and cray were at this point both naming computers under the cray nameplate concurrently via different companies🤷.But in previous decades the difference between scientific computers and mainframes was mute, with models like most univac models and the IBM 701 specifically being designed to be scientific computing mainframes. This makes sense from the server terminal perspective, but also companies like Remington Rand were developed primarily via M&A not by pumping sales. This meant that for example, univac and ERA got merged together inside Remington Rand. Univac did business computing and era did scientific computing (with a background as being formed during ww2 in the naval code breaking office). Suits went “computing and computing? Why are these two different departments?” Lots of ERA employees left to form CDC and univac leaned into embedded systems harder (which they had started to work in in the mid 50s right before cray & morris left)

## midrange servers vs commodity servers

History of the [Mainframe](https://www.tomshardware.com/picturestory/508-mainframe-computer-history-2.html)

Okay this is a doozy that most people don’t actually know about.

**Commodity computing** (also known as  **commodity cluster computing** ) involves the use of large numbers of already-available computing components for parallel computing, to get the greatest amount of useful computation at low cost. Commodity servers are servers you can buy in normal shops (i.e. they are easy to buy), which are not usually of low quality, but do not possess a special build. Examples include Amazon EC2 instances. Or anything from the HP power edge lineup([See this google search case study on HPE racks](https://web.archive.org/web/20110520232758/http://www.dell.com/downloads/global/casestudies/508_2007_google_v11.pdf)).

Midrange servers **are servers whose processing power falls somewhere between that of a mainframe and that of a standard x86 commodity server. For the first couple decades of their history, there was no such thing as a commodity server; x86 servers only came into widespread use starting in the late 1980s. Midrange servers were originally designed for small and medium-sized businesses. These organizations didn’t need the massive computing power of a mainframe.**

Mainframes, big iron on the other hand are bespoke computers with bespoke operating systems and software designed to run specifically on mainframes (z/OS typically with cobol programs). Mainframes are still used for extremely high through put applications like transaction processing. You can’t simply move mainframe-native workloads to commodity servers, but you can typically move a commodity server to a mainframe with virtualization (z/VM).

## Who’s left today?

The industry in Minnesota began to die as integrated circuitry became possible, with Silicon Valley firms like intel and HP taking the lead. IBM was the only one from the bunch that effectively transitioned into different markets.

* Unisys for Burroughs, Sperry, Remington Rand, univac
* HPE for Cray after he left cdc then died
  * Cray was resistant to massively parallel systems that are the backbone now
* CDC as dayforce in a very convoluted set of M&A
