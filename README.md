# Xerver: The Darth Star

**License**: GNU Affero General Public License (AGPL)

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Challenges](#challenges)
- [Next Steps](#next-steps)
- [License](#license)

---

## Project Overview
**Xerver: The Darth Star** is a minimalist, custom-built server designed to serve as an HTTP server, database interface, and frontend for a tech-focused website. Built without frameworks, it delivers core web functionalities, handling HTTP requests, database interactions, and dynamic content delivery. The project combines C for server functionality, Python for MySQL database management, and JavaScript for client-side interactivity. It is an exploration of core server technology, modular programming, and system networking under time constraints.

## Features
1. **HTTP Server in C**: A custom HTTP server built from scratch, capable of handling basic requests and serving HTML files.
2. **MySQL Database Integration**: Structured data storage with CRUD operations, managed through Python.
3. **Frontend Interface**: Interactive website using HTML5, CSS, and JavaScript.
4. **Modular Code Structure**: Separation of concerns through modular design in each language for ease of maintenance.
5. **Scalable Design**: Built with the potential to expand, allowing for easy future feature additions.

## Technologies Used
- **C**: Core HTTP server functionality
- **Python**: Database interaction and management
- **MySQL**: Relational database
- **HTML5, CSS, JavaScript**: Frontend presentation
- **Emacs**: Code editor for all development
- **Bash**: Command-line scripting for server setup and configuration

## Project Structure
```
Xerver-The-Darth-Star/
├── src/                 # C source files for HTTP server
├── frontend/            # HTML, CSS, JavaScript files for website
├── sql/                 # SQL files for database setup
├── scripts/             # Bash scripts for setup and deployment
├── test/                # Automated tests for server and database
└── README.md            # Project documentation
```

## Installation
1. **Clone the Repository**
```bash
git clone https://github.com/username/Xerver-The-Darth-Star.git
cd Xerver-The-Darth-Star
```

2. **Install Dependencies**
Ensure MySQL and GCC are installed on the server:
```bash
sudo apt update
sudo apt install mysql-server gcc
```

3. **Compile the C Server**
```bash
cd src
gcc -o xerver server.c -lpthread
```

4. **Prepare the Database**
- Start MySQL: `sudo service mysql start`
- Run setup script to create the database:
```bash
mysql -u knight -p < sql/setup.sql
```

## Configuration
1. **Network Configuration**:
- Configure IP and port settings in `server.c` to make the server discoverable on the network.
- Ensure clients can reach the server by replacing `localhost` with the local IP (`192.168.x.x`).

2. **Database Configuration**:
- Update `config.py` with database credentials if needed.

3. **Server Security**:
- Basic configurations; ensure network access is secure for internal or same-network access only.

## Usage
1. **Start the Server**:
```bash
./xerver
```
2. **Access the Website**:
- Visit `http://192.168.x.x:8080` from a browser on the same network.
3. **Database Management**:
- Use Python scripts in `src` to handle database operations.

## Challenges
1. **Developing the C Server**: Handling multi-client requests without frameworks was challenging and required detailed research.
2. **Python-MySQL Integration**: Efficiently managing database operations in Python without high-level abstractions demanded careful planning.
3. **Old Laptop Server Configuration**: Network setup required an Ethernet (LAN) connection, leading to a switch to VM-based hosting.
4. **Static IP Requirement**: Realized the need for a static IP, which is out of scope. Local hosting remains restricted to the same network.

## Next Steps
1. **Security Enhancements**: Explore methods to secure requests and data.
2. **Scalability Planning**: Refactor server to handle higher loads and more complex requests.
3. **Business Feasibility**: Aim to expand Xerver as a low-cost server solution for small businesses with simple needs.

## License
This project is licensed under the [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) (AGPL), which requires that all modifications are also licensed under AGPL.

---

With this README, *Xerver: The Darth Star* is thoroughly documented and ready for deployment, contribution, and further development. Let me know if you need additional details in any section!