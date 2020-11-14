# Example 'Tasmota' device

This example config for a Gosund UP111 UK smart plug / energy monitor shows the configuration needed for a Tasmota device.



## Fields

This section describes the configuration file required for a "Tasmota" device within the network.



**Informational fields**

| Field         | Description                                  |
| ------------- | -------------------------------------------- |
| name          | Simple name used to refer to specific device |
| description   | Short description describing device purpose  |
| details       | Dictionary containing device brand and model |
| details.brand | Brand of device creator                      |
| details.model | Model number / name for device               |

**Connection fields**

| Field                 | Description                                   |
| --------------------- | --------------------------------------------- |
| device_type           | The type of the device [e.g. Tasmota, ZigBee] |
| active                | Boolean stating whether the device is active  |
| connection            | Dictionary containing IP connection details   |
| connection.ip_address | IP address of the device                      |
| connection.ip_port    | IP port of the device                         |

**Authentication fields**

| Field                   | Description                                  |
| ----------------------- | -------------------------------------------- |
| authentication          | Dictionary containing authentication details |
| authentication.username | Username set for devices web interface       |
| authentication.password | Password set for devices web interface       |

**Requests and Commands**

| Field    | Description                                                  |
| -------- | ------------------------------------------------------------ |
| requests | Collection of dictionary objects describing state request commands |
| commands | Collection of dictionary objects describing action commands  |

The following describes the request/command object structure

| Field       | Description                                            |
| ----------- | ------------------------------------------------------ |
| name        | Name associated with the command / request             |
| description | Short description describing the purpose               |
| command     | Command parameter required in URL                      |
| example     | Example of full web request required to perform action |

