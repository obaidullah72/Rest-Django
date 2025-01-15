# Django REST Framework Practice Project

This **Django REST Framework (DRF) Practice Project** showcases various web development features such as JWT Authentication, CRUD operations, and RESTful API development using **Django REST Framework (DRF)**. The project includes the following key applications:
- **LoginSignupApp**: User authentication using JWT.
- **BookApp**: A CRUD API for managing book records.
- **Location & Item Management**: CRUD operations for managing location and item data through the Django Admin Panel.

Built with **Django**, **Django REST Framework (DRF)**, and **JWT Authentication**, this project provides a modern, RESTful approach to managing backend data and user authentication.

<img src="assets/splashscreen.gif" width="200">

---

## 📱 Features

### **LoginSignupApp (JWT Authentication)**
- Secure user login and registration using JWT Authentication.
- Users receive a token upon successful login for access to protected resources.
- API endpoints for login and signup with JSON response.

  <img src="assets/login_signup_app.jpg" width="200">

### **BookApp (CRUD with Django REST Framework)**
- Full Create, Read, Update, Delete (CRUD) functionality for books.
- Use of Django REST Framework to build API endpoints for book records.
- Supports filtering, pagination, and sorting of book records.

  <img src="assets/book_app_crud.jpg" width="200">

### **Location & Item Management (CRUD with Admin Panel)**
- Admin panel to manage location and item data (add, update, delete).
- Full CRUD operations available for managing location and item records.
- Modern admin interface with an easy-to-use experience.

  <img src="assets/location_item_crud.jpg" width="200">

---

## 📸 Screenshots

| Login Screen      | Signup Screen      | JWT Authentication  |
|-------------------|--------------------|----------------------|
| <img src="assets/login.jpg" width="150"> | <img src="assets/signup.jpg" width="150"> | <img src="assets/jwt_authentication.jpg" width="150"> |

| Book API          | CRUD Operations    | Admin Panel         |
|-------------------|--------------------|---------------------|
| <img src="assets/book_api.jpg" width="150"> | <img src="assets/crud_operations.jpg" width="150"> | <img src="assets/admin_panel.jpg" width="150"> |

---

## 🛠️ Built With

- **Django**: Web framework for backend development.
- **Django REST Framework (DRF)**: For building RESTful APIs for Book CRUD operations.
- **JWT Authentication**: For secure user login and token-based authentication.
- **SQLite**: Default database (can be switched to other databases if needed).
- **Bootstrap**: For a modern, responsive admin interface.
- **CSS & JavaScript**: For additional styling and interactivity.

---

## 📂 Project Structure

```plaintext
rest_django/
│
├── myproject/                      # Main project directory
│   ├── settings.py                 # Django settings file
│   ├── urls.py                     # URL routing for the whole project
│   └── wsgi.py                     # WSGI entry point
│
├── loginsignupapp/                 # Login and Signup app with JWT authentication
│   ├── migrations/                 # Database migrations
│   ├── models.py                   # User model (for JWT authentication)
│   ├── views.py                    # Views for login and signup
│   ├── urls.py                     # URL routing for the login/signup app
│   └── serializers.py              # Serializers for login/signup requests
│
├── bookapp/                        # Book CRUD with Django REST Framework
│   ├── migrations/                 # Database migrations
│   ├── models.py                   # Book model
│   ├── views.py                    # Views for the book API (CRUD)
│   ├── urls.py                     # URL routing for the book API
│   ├── serializers.py              # Serializers for book data
│   └── permissions.py              # Custom permissions for book access
│
├── locationitemapp/                # Location and Item CRUD operations (via Admin Panel)
│   ├── migrations/                 # Database migrations
│   ├── models.py                   # Location and Item models
│   ├── admin.py                    # Admin panel configurations
│   └── views.py                    # Views for location and item data management
│
├── manage.py                       # Django management script
└── README.md                       # Project documentation
```

---

## 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/obaidullah72/Rest-Django.git
   cd Rest-Django
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser to access the admin panel**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Visit `http://127.0.0.1:8000/` to access the API and test endpoints.
   - Visit `http://127.0.0.1:8000/admin/` to access the Django Admin Panel for managing location and item data.

---

## 🚀 Future Enhancements

- **User Profile Management**: Add user profile settings and the ability to update user data.
- **Search Functionality**: Implement a search endpoint for filtering book, location, and item data.
- **Swagger API Docs**: Integrate Swagger for interactive API documentation.
- **Email Verification**: Implement email verification for user sign-up.
- **Advanced Permissions**: Add custom permissions for more complex access control.

---

## 🤝 Contributing

We welcome contributions! Feel free to submit a **pull request** or open an issue to discuss potential improvements.

---

## 🛡️ License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

For any questions or suggestions, feel free to reach out:

- **GitHub**: [obaidullah72](https://github.com/obaidullah72)
- **LinkedIn**: [obaidullah72](https://www.linkedin.com/in/obaidullah72/)

---

[![Visitor Count](https://visitcount.itsvg.in/api?id=obaidullah72&label=Profile%20Views&color=0&icon=0&pretty=true)](https://visitcount.itsvg.in)
