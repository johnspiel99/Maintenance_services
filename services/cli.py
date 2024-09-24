import click
from services.maintenance import get_engine, create_tables, get_session
from services.models import User, Technician, Service, Category

@click.group()
def cli():
    """Main entry point for CLI commands."""
    pass

@cli.command()
def initdb():
    """Initialize the database."""
    click.echo("Initializing the database...")
    engine = get_engine()
    create_tables(engine)
    click.echo("Database initialized successfully!")

@cli.command()
def menu():
    """Main menu for the CLI application."""
    while True:
        click.echo("\n--- Main Menu ---")
        click.echo("1. Login/Register")
        click.echo("2. List/Add Categories")
        click.echo("3. List Technicians")
        click.echo("4. Update/Delete Categories")
        click.echo("5. Add Service to Category")
        click.echo("0. Exit")
        
        choice = click.prompt("Choose an option", type=int)

        if choice == 1:
            login_register()
        elif choice == 2:
            list_add_categories()
        elif choice == 3:
            list_technicians_cmd()
        elif choice == 4:
            update_delete_categories()
        elif choice == 5:
            try:
                add_service_to_category()
            except Exception as e:
                click.echo(f"An error occurred while adding a service to the category: {e}")
        elif choice == 0:
            click.echo("Exiting the program...")
            break
        else:
            click.echo("Invalid choice. Please try again.")

# Function for adding a service to a category
def add_service_to_category():
    """Add a new service to a category."""
    try:
        list_categories()
        category_id = click.prompt("Enter Category ID", type=int)
        service_name = click.prompt("Enter Service Name")
        
        engine = get_engine()
        session = get_session(engine)

        category = session.query(Category).filter_by(id=category_id).first()

        if category:
            new_service = Service(name=service_name, category=category)
            session.add(new_service)
            session.commit()
            click.echo(f"Service '{service_name}' added to category '{category.name}' successfully!")
        else:
            click.echo(f"Category ID {category_id} not found.")
    except Exception as e:
        click.echo(f"An error occurred: {e}")

# Other command functions
def login_register():
    """Login and Register Options."""
    click.echo("\n1. Login")
    click.echo("2. Register")
    click.echo("0. Back to Main Menu")
    
    choice = click.prompt("Choose an option", type=int)

    if choice == 1:
        click.echo("\n1. User Login")
        click.echo("2. Technician Login")
        click.echo("0. Back to Main Menu")
        
        login_choice = click.prompt("Choose an option", type=int)
        
        if login_choice == 1:
            login_user()
        elif login_choice == 2:
            login_technician()
        elif login_choice == 0:
            return  # Return to the main menu
        else:
            click.echo("Invalid choice.")
            
    elif choice == 2:
        click.echo("\n1. Register User")
        click.echo("2. Register Technician")
        click.echo("0. Back to Main Menu")
        
        register_choice = click.prompt("Choose an option", type=int)
        
        if register_choice == 1:
            register_user()
        elif register_choice == 2:
            register_technician()
        elif register_choice == 0:
            return  # Return to the main menu
        else:
            click.echo("Invalid choice.")
            
    elif choice == 0:
        return  # Return to the main menu
    else:
        click.echo("Invalid choice. Please try again.")

def list_add_categories():
    """List and Add Categories."""
    click.echo("\n1. List Categories")
    click.echo("2. Add Category")
    click.echo("0. Back to Main Menu")
    
    choice = click.prompt("Choose an option", type=int)

    if choice == 1:
        list_categories()
    elif choice == 2:
        add_category()
    elif choice == 0:
        return  # Return to the main menu
    else:
        click.echo("Invalid choice. Please try again.")

def update_delete_categories():
    """Update and Delete Categories."""
    click.echo("\n1. Update Category")
    click.echo("2. Delete Category")
    click.echo("0. Back to Main Menu")
    
    choice = click.prompt("Choose an option", type=int)

    if choice == 1:
        update_category()
    elif choice == 2:
        delete_category()
    elif choice == 0:
        return  # Return to the main menu
    else:
        click.echo("Invalid choice. Please try again.")

def login_user():
    """Login as a user (client)."""
    username = click.prompt("Username")
    password = click.prompt("Password", hide_input=True)
    engine = get_engine()
    session = get_session(engine)

    user = session.query(User).filter_by(username=username).first()

    if user and user.check_password(password):
        click.echo(f"Login successful! Welcome {username}.")
    else:
        click.echo("Invalid username or password.")

def login_technician():
    """Login as a technician."""
    username = click.prompt("Username")
    password = click.prompt("Password", hide_input=True)
    engine = get_engine()
    session = get_session(engine)

    technician = session.query(Technician).filter_by(username=username).first()

    if technician and technician.check_password(password):
        click.echo(f"Login successful! Welcome {username}.")
    else:
        click.echo("Invalid username or password.")

def register_user():
    """Register a new user (client)."""
    username = click.prompt("Username")
    password = click.prompt("Password", hide_input=True, confirmation_prompt=True)
    engine = get_engine()
    session = get_session(engine)

    if session.query(User).filter_by(username=username).first():
        click.echo(f"Username '{username}' is already taken.")
        return

    user = User(username=username)
    user.set_password(password)
    
    session.add(user)
    session.commit()
    click.echo(f"User '{username}' registered successfully!")

def register_technician():
    """Register a new technician.""" 
    username = click.prompt("Username")
    password = click.prompt("Password", hide_input=True, confirmation_prompt=True)
    engine = get_engine()
    session = get_session(engine)

    if session.query(Technician).filter_by(username=username).first():
        click.echo(f"Technician '{username}' is already registered.")
        return

    technician = Technician(name=username, username=username)
    technician.set_password(password)

    session.add(technician)
    session.commit()
    click.echo(f"Technician '{username}' registered successfully!")

def list_categories():
    """List all categories."""
    engine = get_engine()
    session = get_session(engine)

    categories = session.query(Category).all()
    for category in categories:
        click.echo(f"ID: {category.id}, Name: {category.name}")

def add_category():
    """Add a new category."""
    name = click.prompt("Category Name")
    engine = get_engine()
    session = get_session(engine)

    category = Category(name=name)
    session.add(category)
    session.commit()
    click.echo(f"Category '{name}' added successfully!")

def update_category():
    """Update a category."""
    category_id = click.prompt("Category ID", type=int)
    new_name = click.prompt("New Category Name")
    engine = get_engine()
    session = get_session(engine)

    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        category.name = new_name
        session.commit()
        click.echo(f"Category ID {category_id} updated to '{new_name}'!")
    else:
        click.echo(f"Category ID {category_id} not found.")

def delete_category():
    """Delete a category."""
    category_id = click.prompt("Category ID", type=int)
    engine = get_engine()
    session = get_session(engine)

    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        click.echo(f"Category ID {category_id} deleted successfully!")
    else:
        click.echo(f"Category ID {category_id} not found.")


if __name__ == '__main__':
    cli()
