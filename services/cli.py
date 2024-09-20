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

@cli.group()
def menu():
    """Main menu for the CLI application."""
    pass

@menu.command(name='1')
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
        click.echo("Invalid choice.")

@menu.command(name='2')
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
        click.echo("Invalid choice.")

@menu.command(name='3')
def list_technicians():
    """List Technicians."""
    list_technicians_cmd()

@menu.command(name='4')
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
        click.echo("Invalid choice.")

@menu.command(name='0')
def exit_program():
    """Exit the program."""
    click.echo("Exiting...")
    exit()


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

    # Check if username already exists
    if session.query(User).filter_by(username=username).first():
        click.echo(f"Username '{username}' is already taken.")
        return

    # Create new user and set password
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

    # Check if technician username already exists
    if session.query(Technician).filter_by(username=username).first():
        click.echo(f"Technician '{username}' is already registered.")
        return

    # Create new technician and set password
    technician = Technician(name=username, username=username)
    technician.set_password(password)

    session.add(technician)
    session.commit()
    click.echo(f"Technician '{username}' registered successfully!")

def add_category():
    """Add a new category"""
    name = click.prompt("Category Name")
    engine = get_engine()
    session = get_session(engine)

    category = Category(name=name)
    session.add(category)
    session.commit()
    click.echo(f"Category '{name}' added successfully!")

def list_categories():
    """List all categories"""
    engine = get_engine()
    session = get_session(engine)

    categories = session.query(Category).all()
    for category in categories:
        click.echo(f"ID: {category.id}, Name: {category.name}")

def list_technicians_cmd():
    """List all technicians"""
    engine = get_engine()
    session = get_session(engine)

    technicians = session.query(Technician).all()
    for technician in technicians:
        click.echo(f"ID: {technician.id}, Username: {technician.username}, Name: {technician.name}")

def update_category():
    """Update a category"""
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
    """Delete a category"""
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

# Register commands with the CLI group
cli.add_command(initdb)
cli.add_command(menu)

if __name__ == '__main__':
    cli()
