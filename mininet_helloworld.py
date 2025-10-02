from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSBridge
from mininet.cli import CLI
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s1 = self.addSwitch('s1')
        self.addLink(h1, s1)
        self.addLink(h2, s1)

if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    # No controller; switch runs as a plain L2 bridge
    net = Mininet(topo=topo, controller=None, switch=OVSBridge)
    try:
        net.start()
        print("*** Running ping test")
        net.pingAll()
        print("*** Dropping to CLI (type 'exit' to quit)")
        CLI(net)
    finally:
        net.stop()
