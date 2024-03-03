# Python Flask Email Queue Redis

This is a Flask application that allows users to send emails asynchronously using the Python RQ library. The application uses Redis as a message broker to queue and process email sending tasks, allowing users to initiate email actions without waiting for them to complete.

## Usage

- Open your browser and go to <http://localhost:5000>.
- Use the application to send emails asynchronously.

## Setup

### Virtual Environment

- Isolation of project dependencies
- Easy replication of the development environment
- Create a virtual environment:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:
    On Windows:

    ```bash
    .\venv\Scripts\activate
    ```

   On Unix or MacOS:

    ```bash
    source venv/bin/activate
    ```

### Install Dependencies

- Install the project dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

### Configuration

- Add project configuration file at `instance/config.py` with the following content:

  ```python
    SECRET_KEY = "your_sever_secret"
    MAIL_SERVER = "your_mail_server"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "your_mail_username"
    MAIL_PASSWORD = "your_mail_password"

    REDIS_URL = 'redis://127.0.0.1:6379/0'
    QUEUES = ['email-tasks']
  ```

- Replace the placeholders with your actual values.

### Run the Project

- Execute the following command to run the project:

  ```bash
  // start redis worker
  flask redis_task run_worker

  // run flask server
  flask run
  ```

- Feel free to customize and expand upon this to better fit the specifics of your project!

## Contributing

Welcome to the community! We encourage and appreciate contributions to enhance this project. Please review our [contribution guidelines](CONTRIBUTING.md) for details on how to contribute.

## Acknowledgments

A big thank you to the open-source community for their invaluable contributions and resources that have played a crucial role in making this project a reality.

## License

This project is licensed under the MIT License. For more information, refer to the [LICENSE](LICENSE) file.
