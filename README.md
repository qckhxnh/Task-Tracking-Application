Certainly! Here's the compiled version of the README file in Markdown format:

```markdown
# Personal Task Tracker

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Framework: Typer](https://img.shields.io/badge/Framework-Typer-lightgrey)
![Database: PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)

A command-line interface (CLI) Python application for managing personal tasks with a PostgreSQL database, Rich, and Typer frameworks.

## Features

- Add tasks with a specified category.
- Delete tasks by position.
- Update task details.
- Mark tasks as complete.
- View a list of all tasks with a rich and colorful display.

## Prerequisites

- Python 3.7 or higher
- PostgreSQL installed and configured
- Dependencies: See `requirements.txt`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/personal-task-tracker.git
   cd personal-task-tracker
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Setup PostgreSQL database:

   - Create a PostgreSQL database and update the connection details in `database.py`.

4. Run the application:

   ```bash
   python main.py --help
   ```

## Usage

- **Add a Task:**

  ```bash
  python main.py add "Buy groceries" "Shopping"
  ```

- **Delete a Task:**

  ```bash
  python main.py delete 1
  ```

- **Update a Task:**

  ```bash
  python main.py update 1 --task "Buy organic groceries"
  ```

- **Mark a Task as Complete:**

  ```bash
  python main.py complete 1
  ```

- **Show All Tasks:**

  ```bash
  python main.py show
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Typer](https://typer.tiangolo.com/)
- [Rich](https://rich.readthedocs.io/)
- [PostgreSQL](https://www.postgresql.org/)
```

Make sure to replace placeholders like `your-username` with your actual GitHub username, and adjust the content as needed based on the specifics of your project. Additionally, include screenshots in the `screenshots` directory to showcase the application in action.
