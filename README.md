![BookVault LMS Banner](/screenshots/banner.png)

# 📚 BookVault LMS

📚 BookVault LMS — A full-stack Library Management System built with React, Flask, and Oracle DB. Features genre-aware dashboards, real book covers, admin login, analytics graphs, and modular codebase. Designed for scalability, hackathons, and public sector impact.

---

## 🚀 Features

- 📖 **Genre-aware Dashboard** with icon-mapped cards
- 📊 **Analytics Dashboard** with real-time graphs
- 🔐 **Admin Login Panel** with secure access
- 📚 **Book Carousel** with flip animation and real cover images
- 📈 **Borrow/Return Tracking** with transaction logs
- 🧠 **Smart Search** by title, genre, and availability
- 🛠️ **Bulk Cover Seeder** for visual polish
- 🧩 Modular codebase with reusable components

---

## 🖼️ Screenshots
### 🧭  Dashboard  
![Dashboard](/screenshots/dashbord.png)

### 🧭 Genre Dashboard  
![Genre Dashboard](/screenshots/genre-dashboard.png)

### 🧭 Book Availablity Graph 
![Book Availablity](/screenshots/book-availability.png)

### 📚 Book Carousel  
![Book Carousel](/screenshots/book-carousel.png)

### 📚 Transaction History 
![Transaction History](/screenshots/admin-login.png)

### 📚 Member Profile Detail  
![Member Profile](/screenshots/admin-login.png)

### 🔐 Admin Login  
![Admin Login](/screenshots/admin-login.png)

### 📊 Admin Dashbord  
![Admin Dashboard](/screenshots/analytics-dashboard.png)

### 📊 Add Member 
![Add Member](/screenshots/register-member.png)

### 📦 Transaction Logs  
![Transactions](/screenshots/transactions.png)

---

## 🛠️ Tech Stack

| Frontend | Backend | Database | Styling     |
|----------|---------|----------|-------------|
| React    | Flask   | OracleDB | TailwindCSS |

---

## 📂 Folder Structure

```
BookVaultProject/
├── bookvault-backend/
|     ├── node_modules/          # Python cache files (ignored) 
|     ├── app/
|     |     ├── __pycache__/
|     |     ├── routes/
|     |     |        ├──__pycache__/
|     |     |        └── admin_login.py 
|     |     |        └── analytics.py 
|     |     |        └── book_routes.py 
|     |     |        └── issue_book.py 
|     |     |        └── member_routes.py  
|     |     |        └── return_book.py 
|     |     |        └── transactions.py 
|     |     ├── utils/
|     |     |      ├──__pycache__/
|     |     |      └── auth_utils.py
|     |     |      └── date_utils.py 
|     |     ├── __init__.py
|     |     └── db_config.py
|     |
|     |    
|     ├── venve/
|     ├── node_modules/  
|     ├── .env
|     ├── BookCoverSeeder.py
|     ├── main.py
|     ├── package-lock.json
|     ├── package.json
|     ├── README.md
|     └── requirements.txt
|        
├── bookvault-ui/
|     ├── node_modules/           
|     ├── public/    
|     ├── src/      
|     |     ├── components/
|     |     |     └──  AdminDashboard.jsx
|     |     |     └──  BookAvailabilityChart.jsx
|     |     |     └──  BookCarousel.css
|     |     |     └──  BookCarousel.jsx
|     |     |     └──  BookCarouselCard.css
|     |     |     └──  BookCarouselCard.jsx
|     |     |     └──  BookCoverUploader.jsx
|     |     |     └──  GenreBooksPage.jsx
|     |     |     └──  GraphPanel.jsx
|     |     |     └──  LoginForm.jsx
|     |     |     └──  MemberForm.jsx
|     |     |     └──  MemberProfile.jsx
|     |     |     └──  Navbar.jsx
|     |     |     └──  OverdueAlertPanel.jsx
|     |     |     └──  ReturnForm.jsx
|     |     |     └──  TransactionGraph.jsx
|     |     |     └──  UserForm.jsx
|     |     |     └──  WelcomeBanner.jsx
|     |     |
|     |     ├──pages/
|     |     |     └──  AdminPanel.jsx
|     |     |     └──  AnalyticsDashboard.jsx
|     |     |     └──  Dashboard.jsx
|     |     |     └──  Transactions.jsx
|     |     |
|     |     ├──api.js
|     |     ├──App.jsx
|     |     ├──index.css
|     |     └──index.js
|     |
|     ├──.gitignore
|     ├──package-lock.json
|     ├──package.json
|     ├──postcss.config.js
|     ├──tailwind.config.js
|     └──README.md
|
├──screenshots/
└──README.md
```


---

## 📦 Requirements

### 🔧 Backend

- Python 3.10+
- Flask
- cx_Oracle
- python-dotenv
- requests

### 🗄️ Oracle DB

- Oracle XE or Oracle 21c
- Table: `books` with columns:
  - `book_id` (NUMBER)
  - `title` (VARCHAR2)
  - `author` (VARCHAR2)
  - `genre` (VARCHAR2)
  - `total_copies` (NUMBER)
  - `available_copies` (NUMBER)
  - `cover_url` (VARCHAR2)

### 💻 Frontend

- Node.js 18+
- React 18+
- TailwindCSS
- react-router-dom
- react-icons

### 📁 Dev Tools

- VS Code
- Oracle SQL Developer
- Git & GitHub


---

## 🧪 Setup Instructions

### Backend

```bash
cd bookvault-backend
python main.py
```

### Frontend
```bash
cd bookvault-frontend
npm install
npm start
```
---

## 👨‍💻 Author
Ali Rizvi Backend-focused full-stack developer | Hackathon finalist | Civic tech enthusiast 
📍 Lucknow, India
 ![🔗 LinkedIn](www.linkedin.com/in/alirizvi110) ![🔗 Portfolio](https://ali-portfolio-full.vercel.app/)

---

## 📬 Feedback & Contributions
- 🛠️ **Feel free to fork, star ⭐, or raise issues. Contributions welcome!**



