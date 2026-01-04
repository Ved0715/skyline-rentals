# Rental Portal - Apartment Rental Management System

A complete full-stack application for managing residential apartment rentals with user and admin portals.

## Tech Stack

- **Frontend**: Angular 21 + Tailwind CSS
- **Backend**: Python Flask + SQLAlchemy
- **Database**: PostgreSQL
- **Deployment**: Docker + Docker Compose

## Features

### User Portal

- Browse available apartments
- View detailed apartment information with amenities
- Request bookings
- Track booking status
- User authentication (JWT)

### Admin Portal

- Dashboard with real-time statistics
- Manage apartment units
- Approve/decline booking requests
- View all users and bookings

## Quick Start with Docker

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. **Clone the repository**

```bash
cd "untitled folder"
```

2. **Start all services**

```bash
docker-compose up --build
```

3. **Access the application**

- Frontend: `http://localhost`
- Backend API: `http://localhost:5001`

### Default Credentials

**Admin User:**

- Email: `admin@gmail.com`
- Password: `1234`

**Test User:**

- Create your own account via registration

## Development Setup

### Backend (Flask)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

### Frontend (Angular)

```bash
cd frontend
npm install
npm start
```

### Database

PostgreSQL runs on `localhost:5432`

- Database: `apartment_rental`
- User: `postgres`
- Password: `postgres`

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── models/      # Database models
│   │   ├── routes/      # API endpoints
│   │   └── utils/       # Helper functions
│   ├── migrations/      # Database migrations
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── pages/   # Components
│   │   │   └── services/# API services
│   │   └── styles.css
│   ├── Dockerfile
│   └── nginx.conf
└── docker-compose.yml
```

## API Documentation

### Authentication

- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login
- `GET /api/auth/me` - Get current user

### Units

- `GET /api/units` - List all units
- `GET /api/units/{id}` - Get unit details
- `POST /api/units` - Create unit (admin)

### Bookings

- `GET /api/bookings/my` - Get user's bookings
- `POST /api/bookings/` - Create booking request
- `GET /api/bookings` - Get all bookings (admin)
- `PUT /api/bookings/{id}/status` - Update booking status (admin)

### Admin

- `GET /api/admin/dashboard/stats` - Get dashboard statistics

## Database Seed

To populate the database with sample data:

```bash
cd backend
python3 seed_data.py
```

This creates:

- 1 admin user
- 12 amenities
- 1 tower (Skyline Residences)
- 5 sample apartments with amenities

## Docker Commands

**Start services:**

```bash
docker-compose up
```

**Rebuild and start:**

```bash
docker-compose up --build
```

**Stop services:**

```bash
docker-compose down
```

**View logs:**

```bash
docker-compose logs -f
```

**Reset database:**

```bash
docker-compose down -v
docker-compose up --build
```

## Environment Variables

Create `.env` files if needed:

**Backend (.env)**

```
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/apartment_rental
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
```

## License

MIT License
