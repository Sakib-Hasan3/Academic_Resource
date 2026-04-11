# ICMP Pinger Lab in Python

A Python-based project to implement a simple ICMP ping application that measures round-trip times and provides network latency statistics.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ItsTHEAvro/ICMP_Pinger_Lab.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ICMP_Pinger_Lab
   ```
3. Ensure Python is installed on your system. This project uses Python 3.

## Usage

Run the project with the following command:

```bash
python ICMP_Pinger.py <hostname>
```

Example usage:

```bash
python ICMP_Pinger.py google.com
```

## Features

- Sends ICMP Echo Request messages to a specified host.
- Calculates round-trip time for each ping.
- Tracks and displays statistics:
  - Average round-trip time.
  - Minimum and maximum round-trip time.
  - Packet loss percentage.
- Timeout mechanism for handling non-responsive hosts.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Maintainer: [Jyotirmoy Avro](https://github.com/ItsTHEAvro)  
For any questions or suggestions, feel free to open an issue on GitHub or contact the maintainer.
