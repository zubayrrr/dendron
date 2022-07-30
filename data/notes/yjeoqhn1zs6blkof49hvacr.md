
# Layer 1 – Physical layer

This where the transmission of bits across the network occurs and is focused on the physical and electrical characteristics of the network.

There is where we decide if we're using an [[devlog.Ethernet]] network or if we're using [[devlog.Fiber Optic]], or Copper cables.

No matter what method we're using to transmit our data, it will always be in the form of binary [[devlog.bit]]s

Binary [[devlog.bit]]s are series of 1s and 0s.

Each media has different ways of representing these [[devlog.bit]]s

For example, if we're using a Copper wire such as in a [[devlog.Cat5]] or [[devlog.Cat6]] network, you'll find that the voltage of the wire will be zero for a 0 [[devlog.bit]] and to represent a 1, you might use a +5 or -5 voltage on the Copper wire.

**Transition Modulation** is what dictates the change is (or how it should be interpreted), If it changed during the clock cycle, then a 1 is represented (otherwise it is a 0).

In case of a [[devlog.Fiber Optic]] cable, we'll be using light instead of voltages; when we want a 1, we turn the light on. when we want to represent a 0, we turn the light off.

---

Once we have the data from the [[devlog.Media]], we'll have [[devlog.Connector Types]] on the end of the cables that go inside our devices. These connectors are wired based on a standard.

- TIA/EIA-568-B
  - [[devlog.RJ-45]] cables and ports
- T-568A and T-568B
  - Crossover cables
- [[devlog.Straight-Through Patch Cable]] typically uses T-568B on both ends, but could also use T-568A.
- See: [[devlog.Pinouts]]

### Topology of the network at the Physical Layer

- Layer 1 devices view networks from a physical topology perspective, as discussed in [[devlog.Wired Network Topology]] & [[devlog.Wireless Network Topology]].

---

### Synchronizing communication at Physical Layer

How do we know that the receiving end is ready to accept the [[devlog.bit]]s that we're ready to send?

- We can work this out either Asynchronously or Synchronously:

#### Asynchronous

- Uses "start bits" and "stop bits" to indicate when transmissions occur from sender to receiver.

#### Synchronous

- Uses a reference block to coordinate the transmissions by both sender and receiver. Happens in Real-time. Uses a time source, transmits data on the cadence of the time.

---

### How is the bandwidth utilized?

There are again two ways, Broadband and Baseband.

#### Broadband

- Divides bandwidth into separate channels. (e.g. Cable TV)

#### Baseband

- Uses all available frequencies on a medium (cable) to transmit data and uses a reference clock to coordinate the transmissions by both sender and receiver. (e.g. Telephone, Home [[devlog.Ethernet]])

---

### If we're using a single Baseband using all of the bandwidth how can we get more out of a limited network?

- Time-Division Multiplexing (TDM)
  - Each session takes a turn, using time slots, to share the medium between all users.
- Statistical Time-Division Multiplexing (StatTDM)
  - More efficient version of TDM since it dynamically allocates time slots on an as-needed basis instead of statically assigning.
- Frequency-Division Multiplexing (FDM)
  - Medium is divided into various channels based on frequencies and each session is transmitted over a different channel.

---

### Media at Layer 1 (Layer 1 Examples)

Devices that give physical response, hence a physical layer device.

- Cables
  - [[devlog.Ethernet]]
  - [[devlog.Fiber Optic]]
- Radio Frequencies
  - [[devlog.Wi-Fi]]
  - [[devlog.Bluetooth]]
  - [[devlog.NFC]]
- Infrastructure Devices
  - [[devlog.Hub]]s
  - Wireless Access Points
  - [[devlog.Media Converters]]
