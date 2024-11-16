#chocolate_data_application_project

### Prerequisites
- Python 3.x
- Django (latest version compatible with Python)
- SQLite (bundled with Python)
- Git (optional but recommended)
- Docker (for containerized setup)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/username/chocolate-house.git
   cd chocolate-house
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

### 5. **Setup and Running the Application**
Detail how to start and interact with the application:
```markdown
### Running the Application
1. Ensure the virtual environment is active.
2. Start the server with:
   ```bash
   python manage.py runserver
   ```
3. Open your web browser and navigate to `http://127.0.0.1:8000/`.

### Docker Setup (Optional)
1. Build the Docker image:
   ```bash
   docker build -t chocolate-house-app .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 chocolate-house-app
   ```
### Project Structure
- `myapp/`: Main project folder.
- `myapp_name/`: Django app with views, models, templates.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django’s command-line utility.
- `Dockerfile`: Instructions for building the Docker image.
- `requirements.txt`: List of Python dependencies.

#output
The admin can insert ,delete,update the detail in admin page  http://127.0.0.1:8000/admin/

