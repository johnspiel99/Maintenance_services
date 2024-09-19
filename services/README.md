### Maintenance Services CLI

A command-line interface (CLI) tool for managing a maintenance services system. This application allows users to initialize the database, register and log in users and technicians, manage service categories, and services.

### Features

- Database Initialization: Create and set up the SQLite database with necessary tables.
- User Management: Register and log in users and technicians.
- Service Management: List, add, update, and delete service categories.
- Technician Management: List all registered technicians.

### Prerequisites

- Python 3.7 or higher
- pipenv for managing dependencies

### Installation

1. Clone the Repository:

    git clone <repository-url>
    cd <repository-directory>

2. Install Dependencies:

    Make sure you have pipenv installed. If not, you can install it via pip:

    pip install pipenv

    Install the required Python packages:

    pipenv install

### Usage

1. Initialize the Database:

    Set up the database and create necessary tables:

    pipenv run python main.py initdb

2. Run the Main Menu:

    Start the CLI and access the main menu:

    pipenv run python main.py menu

    The menu options are:
    - 0: Exit the program
    - 1: Login and Register Options
    - 2: List and Add Categories
    - 3: List Technicians
    - 4: Update and Delete Categories

### How the Maintenance_ service CLI Works

When you run `pipenv run python main.py menu`, the CLI displays a menu with several options:

1. **Login and Register Options**: 
    - **Register User**: Allows you to register a new user by providing a username and password.
    - **Register Technician**: Allows you to register a new technician by providing a username, password, and other details.
    - **Login User**: Allows existing users to log in using their username and password.
    - **Login Technician**: Allows existing technicians to log in using their username and password.

2. **List and Add Categories**:
    - **List Categories**: Displays all service categories currently in the system.
    - **Add Category**: Allows you to add a new service category by providing a name and description.

3. **List Technicians**:
    - **List Technicians**: Displays all registered technicians in the system.

4. **Update and Delete Categories**:
    - **Update Category**: Allows you to update the name and description of an existing service category.
    - **Delete Category**: Allows you to remove a service category from the system.

### To interact with the CLI:

- Choose an option by typing the corresponding number and press Enter.
- Follow the prompts to provide any necessary information.
- The CLI will execute the selected command and provide feedback or instructions as needed.

### Example

After running `pipenv run python main.py menu`, you might see the following options:

Please select an option:
0. Exit the program
1. Login and Register Options
2. List and Add Categories
3. List Technicians
4. Update and Delete Categories

Type the number corresponding to the action you want to perform and follow the on-screen instructions.

### Development

- Add/Update Features: Modify or add new functionality in the services/cli.py file.
- Database Models: Update the database schema in the services/models.py file.
- Testing: Add or update tests in a separate test suite to ensure code quality.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
