# What is Licensei?


Licensei is a self-hosted product license key manager.
Manage license keys or codes for your products on your own machine or infrastructure.
This is especially helpful for smaller businesses or startups that need to manage
access to their products for billing.

---
# Installation and Usage
### Requirements:
- Git
- Docker (WSL required for Windows)

Clone the repo
```angular2html
git clone https://github.com/jayryanj/licensei.git
```
`cd` into the project root directory and run the following command:
```angular2html
docker compose up
```

# For Contributors
## Tech Stack:
- Back-end:
  - Python
  - Flask
  - psycopg2
- Font-end:
  - TypeScript
  - React
  - Tailwind CSS, Bootstrap, Materialize, or Semantic UI (Choose one)
- PostgreSQL
- Docker
- Redis (Future use case for larger users/orgs)

## How it works
Licensei will run entirely in **Docker** or any other container orchestration service.
The point is that it's self-hosted which means the user chooses where to run it. Whether it be:
- Locally (preferred for now)
- Their own infrastructure/hardware
- Cloud

For now, development is primarily focused on running it locally in Docker using the following
command:
```angular2html
docker compose up # TODO change this to a bash script for further abstraction
```

This will run two containers:
- licensei-app (main Flask app)
- licensei-db (PostgeSQL database)


Once running, users will be able to access the Licensei UI via web browser by visiting `http://localhost/ui/`

For now, the React front-end will be served via the same server as the API until we need to support higher scale.

From the UI, the user can...
- Create a new license
- Check if a license is valid
- Delete a license (from the back-end, this will be a soft-delete)
- View all licenses in a table (features for sorting, pagination, filters, etc.)