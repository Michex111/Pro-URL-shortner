<<<<<<< HEAD
# Pro-URL-shortner
Modern URL shortener built with FastAPI, async SQLAlchemy, Redis caching, and Base62 encoding. Features fast redirects, clean architecture, async PostgreSQL support, and a lightweight frontend UI.
=======
# Pro URL Shortener

A modern URL shortening service built with FastAPI, async SQLAlchemy, Redis caching, and Base62 encoding.

This project allows users to:

* Shorten long URLs
* Resolve short URLs through fast redirects
* Cache redirects using Redis
* Serve a lightweight frontend interface
* Generate compact Base62-based short codes

---

## ✨ Features

* ⚡ Fast URL shortening
* 🔗 HTTP redirects
* 🧠 Base62 encoding system
* 🗄️ Async PostgreSQL support with SQLAlchemy
* 🚀 Redis caching for fast lookups
* 🎨 Frontend UI with HTML/CSS/JavaScript
* 📦 Clean service-layer architecture
* 🔒 Pydantic validation using `HttpUrl`
* 🌙 Async-first backend design

---

## 🏗️ Project Structure

```text
Pro URL_shortner/
├── api/                 # API routes
├── core/                # App configuration + Redis
├── db/                  # Database models + session management
├── schemas/             # Pydantic schemas
├── services/            # Business logic
├── templates/           # Frontend templates
├── utils/               # Utility functions (Base62)
├── dependencies.py      # Dependency injection
├── main.py              # FastAPI app entrypoint
└── README.md
```

---

## 🧰 Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* Redis
* Pydantic

### Database

* PostgreSQL (Neon)

### Frontend

* HTML
* CSS
* Vanilla JavaScript

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Pro_URL_shortner
```

---

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

or if using uv:

```bash
uv sync
```

---

### 4. Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=your_database_url
REDIS_URL=your_redis_url
APP_NAME=Pro URL Shortener
```

---

### 5. Run the application

```bash
uvicorn main:app --reload
```

App will be available at:

```text
http://127.0.0.1:8000
```

---

## 🔌 API Endpoints

### Shorten URL

```http
POST /api/shorten
```

Request:

```json
{
  "url": "https://example.com"
}
```

Response:

```json
{
  "short_url": "http://localhost:8000/abc123"
}
```

---

### Resolve URL

```http
GET /{short_code}
```

Redirects to the original URL.

---

## 🧠 How Base62 Encoding Works

The application generates compact short codes using Base62 encoding.

Character set:

```text
0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
```

Example:

```text
100 -> 1C
```

This allows IDs to remain short while supporting millions of unique URLs.

---

## 🚀 Future Improvements

* 📊 Click analytics
* 👤 User accounts
* 🧾 URL expiration
* 🛡️ Rate limiting
* ✏️ Custom aliases
* 📱 QR code generation
* 🌐 Deployment support

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Built as a modern backend engineering project using FastAPI and async Python tooling.
>>>>>>> 65f4041 (feat: fixed db pinging & updated readme)
