# Parking Management System Backend

This project involves developing a parking management system with mobile wireless chargers for electric cars.

## Documentation

The documentation for this project includes the following components:

1. **Class Diagram**: Provides an overview of the system's classes and their relationships.
2. **ER Diagram**: Shows the entity-relationship model for the database.
3. **Architecture Diagram**: Illustrates the system's architecture and components.
4. **System Flowcharts**: Depicts the workflow and processes within the system.
5. **Database Structure**: Details the database schema and tables.
6. **Backend Functionality**: Describes the backend logic and functionalities.
7. **Integration MQTT with MWBOTS**: Explains how MQTT is integrated with mobile wireless bots (MWBOTS).

## Backend Installation Steps

### Setup Installation Guide

1. **Python 3.8.10**
   - Download and install Python 3.8.10 from [python.org](https://www.python.org/downloads/release/python-3810/).
   - Verify installation:
     ```bash
     python --version

   - Create and activate a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
2. **Node.js v16**
   - Download and install Node.js v16 from nodejs.org.
   - Verify installation:
     ```bash
     node --version
     npm --version
3. **PostgreSQL 15**
   - Download and install PostgreSQL 15 from postgresql.org.
   - Open pgAdmin, create a new database named parking_system.
   - Verify installation:
     ```bash
     psql --version
4. **Mosquitto (for MQTT)**
   - Download and install Mosquitto from mosquitto.org.
   - Start the Mosquitto broker:
     ```bash
      mosquitto
   - Verify installation:
     ```bash
      mosquitto -h

### Installation
   - Install the required Python dependencies:
     ```bash
     pip install -r requirements.txt
### Usage
   - Run the following commands to set up and start the backend server:
     ```bash
     python manage.py makemigrations api
     python manage.py migrate
     python add_permission.py
     python populate.py
     python manage.py runserver
   - After running the server, open two additional terminals, activate the virtual environment in each, and run the following commands:
   - In the first terminal:
     ```bash
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     python manage.py mwbot
   - In the first terminal:
     ```bash
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     python manage.py run_mqtt


This Markdown file includes the complete backend setup, installation guide, and usage instructions for the parking management system, with the database creation step updated to use pgAdmin.