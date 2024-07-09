# Hotel-Management-System----Django

This is a comprehensive Hotel Management System built using Django. It includes features for admin login/logout, a simple dashboard, CRUD operations for room categories and rooms, booking rooms for guests, guest checkout, and viewing booking history.

## Features

- **Admin Authentication**: Secure login and logout for admin users.
- **Dashboard**: A user-friendly dashboard for managing the system.
- **Room Categories**: Add, update, view, and delete room categories.
- **Rooms Management**: CRUD operations for rooms, including availability status.
- **Booking Management**: Book rooms for guests, manage current bookings, and process checkouts.
- **Booking History**: View past booking records for analysis and tracking.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (default, can be changed to other databases like PostgreSQL, MySQL)

## Installation

1. **Clone the repository**:
    ```sh
    https://github.com/kavindu-vk/Hotel-Management-System----Django.git
    cd Hotel-Management-System----Django
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

7. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000`.
