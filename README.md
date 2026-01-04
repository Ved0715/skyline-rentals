# Apartment Rental Portal

A full-stack application for managing residential apartment rentals, featuring a public user portal for booking and an admin portal for management. Built with Angular (v21), Flask, and PostgreSQL, fully containerized with Docker.

## Quick Start (Docker)

The easiest way to run the application is using Docker Compose.

### 1. Start Services

```bash
docker-compose up --build
```

This starts:

- **Frontend**: [http://localhost:4200](http://localhost:4200)
- **Backend**: [http://localhost:5001](http://localhost:5001)
- **Database**: PostgreSQL (internal)

### 2. Seed Database

Open a **new terminal** and run:

```bash
docker exec -it rental_backend python seed_data.py
```

This creates the admin user and sample data (apartments, amenities).

### 3. Login

- **Admin Portal**: [http://localhost:4200](http://localhost:4200) (redirects after login)
  - **Email**: `adminMain@gmail.com`
  - **Password**: `111`
- **User Portal**: Register a new account to browse and book.

---

## Tech Stack

- **Frontend**: Angular 21, Tailwind CSS, Nginx
- **Backend**: Python Flask, SQLAlchemy, Flask-Migrate, JWT Extended
- **Database**: PostgreSQL 15
- **Infrastructure**: Docker, Docker Compose

## Key Features

### User Portal

- **Browse Units**: View available apartments with amenities and photos.
- **Booking**: Request unit viewings/bookings.
- **Dashboard**: Track status of booking requests.

### Admin Portal

- **Dashboard**: Real-time stats (users, bookings, vacancy).
- **Unit Management**: Add/Edit apartment units.
- **Booking Workflow**: Approve or decline user booking requests.

## Project Structure

```
├── backend/            # Flask API
│   ├── app/models/     # SQLAlchemy Models
│   ├── app/routes/     # API Endpoints
│   └── seed_data.py    # Data seeding script
├── frontend/           # Angular App
│   ├── src/app/pages/  # Admin & User components
│   └── src/app/services# API & Auth services
└── docker-compose.yml  # Container orchestration
```

## Troubleshooting

**Login Failed?**

- Ensure you ran the **seed command** (Step 2 above).
- Check backend logs: `docker-compose logs -f backend`

**Registration Error?**

- Password must be at least **6 characters**.

**Stop Services**

```bash
docker-compose down
```
