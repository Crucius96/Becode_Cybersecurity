# BeCode - Network Group Projects
BeCode Network Module - Network Group Project

## Guidelines

With a team of 4, we had 4 days to establish a network plan in Cisco Packet Tracer.

The network must have :
- An AD server, DNS.
- A DHCP server.
- A DMZ (firewall, proxy).
- A storage server (iscsi).
- 4 Sectors :
    - 1 Management, secretariat: 5 posts
    - 2 Study : 8 posts.
    - 3 Production : 10 posts.
    - 4 Support (2 sectors): 30 posts per sector.

The plan had to be as complete as possible. It had include the IP address, the type of connection used, the number of switches, etc...

## Team

- [Axel](https://github.com/Crucius96)
- [Nicolay](https://github.com/yadrychnikovNicolay)
- [Stéphane](https://github.com/RombinatoR)
- [Wouter](https://github.com/Hyamoto)

## Setups

We established **2 different Network plans**, one where the network would have switches as its central part and the other where routers are setup in OSPF.

_Hereunder you can find the networks plan(.pkt) link:_

- [Switch_Network_Plan](https://github.com/Crucius96/Becode-Projects/blob/master/Network%20Chapter/Group_Network_Project/Network_Models/Switch-Network-Plan.pkt)
- [Router_Network_OSPF](https://github.com/Crucius96/Becode-Projects/blob/master/Network%20Chapter/Group_Network_Project/Network_Models/Router-Network-OSPF.pkt)


### Switch Network

After setting up all the workstations in their allocated sectors, we connected all the sectors to a quadruple switch network in the middle, acting as a core. **(triple switch outside - one main switch inside)**

Every sector switch connects to all 3 outer core switches, thus enabling **redundancy** and allowing the network to work even if a switch was to go down.

We then added a server zone and set up FTP, DNS, DHCP and AD servers. (AD was added per request of the exercise but we did not manage to make it work)

After the basic network was ready and the sectors interconnected, we set a connection from the inner core switch to a firewall, allowing us to start connecting our network to the outside world.

We connect the firewall to the DMZ with a Web Server inside and to a router leading to the Cloud.


![network-project-switches](https://github.com/Crucius96/Becode-Projects/assets/130939051/a8d7136e-c9b9-42d0-831c-3ad13dc70551)

### Router Network

Instead of using only switches, we thought about a solution with routers.
Though it is theoretically a more expensive solution, especially so for a network of *this small size*, routing prevents congestion in the heart of the network, to some extent; since packets are sent through a single route instead of being spread out across all core switches then thrown away by switches that do not receive packets with a specific VLAN tag (or, that just die at the end of TTL if switches are setup to trunk on all interfaces, like in our example).

Instead of using static routing, that has to be redone each time the network evolves; we used dynamic routing using OSPF (Open Shortest Path First) protocol. https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/7039-1.html
What OSPF essentially does is allowing routers to learn routes from their neighbor routers, dynamically. Plus, OSPF picks the shortest available route (actually the one that has the *higher priority*) for each transmission. The protocol constantly checks the state of the known links and then transmits to other routers their state, periodically. That's why, if an interface is turned down or up on one of the routers, we can read on the other routers' CLI that X interface state has changed.
OSPF is therefore what we call a **link state protocol**.
Therefore, whenever a link state changes (its address, or subnet mask, or just its activity state), the whole network autonomously adapts to any changes as the routers re-learn their routes live.

All 6 routers in our network are configured with OPSF and all central routers' configs are found in the *running-config* files in the *configs* folder. [proposed todo: make that folder and push the running-config txt files].

__Here below is the addressing plan of the network__:

| Subnet name | Network address | First address |   Broadcast   |
|-------------|-----------------|---------------|---------------|
|Management   |192.168.1.0/28   |192.168.1.1/28 |192.168.1.15/28|
|Study        |192.168.1.16/28  |192.168.1.17/28|192.168.1.31/28|
|Production   |192.168.1.32/27  |192.168.1.33/27|192.168.1.63/27|
|Support 1    |192.168.1.64/27  |192.168.1.65/27|192.168.1.95/27|
|Support 2    |192.168.1.96/27  |192.168.1.97/27|192.168.1.127/27|

Addresses from 10.0.0.0/8 have been allocated to the core network; so to router interfaces that just make the link between routers.
For redundancy purposes (= resilience, in case *one* device crashes, the whole network still works), there are multiple core routers, and each subnet is connected to two switches.
Such architecture is of course not possible if the network covers large distances on site.

__DHCP__:

There is one PC that is also used as local DHCP server in each department. This is due to the fact we use routers, and we cannot route without IP, so giving an address across the network to a machine that doesn't have one, in this case, is not doable. So we give addresses within the subnets themselves.

![network-project-routers](https://github.com/Crucius96/Becode-Projects/assets/130939051/532c0c4b-ced1-4ede-8f61-e5c25f48d6b0)

## Last Step

The last step of the group project was to present said project as a collective in a 5 minutes time limit. Having 2 projects we split the presentation time for each one of them to 2 minutes and a half.
