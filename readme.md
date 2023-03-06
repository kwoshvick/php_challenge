
# Pbp Challenge

## Input data
API must take the following fields as input:
 - first_name
 - last_name 
 - national_id
 - birth_date
 - address
 - country
 - phone_number
 - email,
 - finger_print_signature

## Setup Instruction
- [Install docker](https://docs.docker.com/engine/install/)
- [Install docker compose](https://docs.docker.com/compose/install/)
- Clone the project
- Insider the project folder do the following:
    - Build containers
        - `docker-compose build`
    - Run the containers
        - `docker-compose up -d `
        
- Access the application via `http://localhost:4020`

## API Collection
- [Postman Collection link](https://api.postman.com/collections/4541468-1f83c930-c9cf-4bfd-8d9f-1faac672dbc8?access_key=PMAT-01GTVXX6NDGNQAM4RCTS894EC4)

## Access Django Admin Panel
- `http://localhost:4020/admin`
    - *username:* admin
    - *password:* gateway
