# Netzob.org #
<font color='red'>Netzob's official website has been released and contains more updated informations.<br>
see <a href='http://www.netzob.org'>http://www.netzob.org</a> for more informations on Netzob.</font>

# Netzob : Inferring Communication Protocols #

## About Netzob ##

### Functional Description ###

Netzob is an opensource tool for reverse engineering, traffic generation
and fuzzing of communication protocols. This tool allows to infer the message format (vocabulary)
and the state machine (grammar) of a protocol through passive and active processes.
Its objective is to bring state of art academic researches to the operational field,
by leveraging bio-informatic and grammatical inferring algorithms in a semi-automatic manner.

Netzob is suitable for reversing network protocols, structured files and system and
process flows (IPC and communication with drivers and devices).
Dedicated modules are provided to capture and import data in multiple contexts (network, file and process data acquisition).
Once inferred, a protocol model can afterward be exported to third party tools (Peach, Scapy, Wireshark, etc.)
or used in the traffic generation engine, to allow simulation of realistic and controllable communication endpoints and flows.

Netzob handles different types of protocols: text protocols (like HTTP and IRC), delimiter-based protocols,
fixed fields protocols (like IP and TCP) and variable-length fields protocols (like TLV-based protocols).

### Technical Description ###

Netzob's source code is mostly made of Python (90%) with some specific
extensions in C (6%). It includes a graphical interface based on GTK3.

The tool is made of a core (officially maintained) and of bunch of
plugins (exporters, importers, ...). Some plugins are provided by the team while others are
created and managed directly by users.

# Demo #
Watch the Demo : [Infering and simulating a proprietary communication protocol using Netzob](http://vimeo.com/34964757).

# Screenshots #

The Netzob interface :

![https://netzob.googlecode.com/svn/trunk/doc/netzob_1.png](https://netzob.googlecode.com/svn/trunk/doc/netzob_1.png)

Blue columns represent the dynamic/variable fields. Black columns represent the static fields.

When analysing DNS traffic (and with no previous knowledge of the protocols), Netzob discovers the IP.total\_length field, the UDP.length field and their associated payloads :

<img src='https://netzob.googlecode.com/svn/trunk/doc/netzob_3.png' border='1'>