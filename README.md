# homemade-pickles-and-snacks-using-AWS-Colud
🥒 Homemade Pickles & Snacks – AWS Cloud Project
📌 Project Overview

Homemade Pickles & Snacks – Taste the Best is a cloud-based web application that allows users to explore and order traditional homemade pickles and snacks online. The platform combines Flask web development with AWS cloud services to create a scalable and cost-effective solution for small food businesses.

The project demonstrates how cloud computing can be used to host, manage, and scale an e-commerce style application.

🚀 Features

✔ User Registration and Login
✔ Browse Homemade Pickles and Snacks
✔ Add Products to Cart
✔ Checkout System
✔ Product Categories (Veg Pickles, Non-Veg Pickles, Snacks)
✔ Cloud Deployment using AWS
✔ Simple and user-friendly interface

🛠️ Technologies Used
Frontend
HTML
CSS
Bootstrap
Backend
Python
Flask Framework
Cloud Services
AWS EC2 (Application Hosting)
AWS DynamoDB (Database)
AWS IAM (Security and Access Management)
Other Tools
Git & GitHub
Boto3 (AWS SDK for Python)

📂 Project Structure
Homemade-pickles-snacks-AWS_cloud_project
│
├── app.py
│
├── templates
│   ├── index.html
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── veg_pickles.html
│   ├── non_veg_pickles.html
│   ├── snacks.html
│   ├── cart.html
│   └── checkout.html
│
├── static
│   └── images
│
└── README.md


⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/Homemade-pickles-snacks-AWS_cloud_project.git
cd Homemade-pickles-snacks-AWS_cloud_project
2️⃣ Install Required Libraries
pip install flask
pip install boto3
3️⃣ Configure AWS

Create an AWS account
Create a DynamoDB table
Configure IAM credentials
Install AWS CLI and configure
aws configure
4️⃣ Run the Application
python app.py
Then open in browser:
http://127.0.0.1:5000
☁️ AWS Deployment Steps
Launch an EC2 Instance
Connect using SSH
Install Python and dependencies
Clone the GitHub repository
Run the Flask application
Configure security group to allow port 5000 or 80

📊 Workflow
User → Web Interface → Flask Backend → AWS DynamoDB → Response to User
🎯 Use Case

This project is useful for:

Small homemade food businesses
Cloud computing learning projects
AWS deployment practice
Beginner Flask projects

🔮 Future Enhancements

Online Payment Integration
Admin Dashboard
Order TrackingSystem
Mobile Responsive Design
Product Reviews

👩‍💻 Author

Hima Rashmi

Student | Cloud & Web Development Enthusiast

⭐ If you like this project

Give it a star ⭐ on GitHub to support the project
