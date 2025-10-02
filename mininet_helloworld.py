from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.cli import CLI

class SingleSwitchTopo(Topo):
    def build(self):
        # Add two hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        # Add a switch
        s1 = self.addSwitch('s1')
        # Link hosts to switch
        self.addLink(h1, s1)
        self.addLink(h2, s1)

if __name__ == '__main__':
    topo = SingleSwitchTopo()
    net = Mininet(topo=topo, controller=OVSController)
    net.start()

    print("*** Running ping test")
    net.pingAll()

    print("*** Dropping to CLI (type 'exit' to quit)")
    CLI(net)

    net.stop()
