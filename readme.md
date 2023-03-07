
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

## Setup Instruction locally
if the projects is going to run using django server locally 
- Rename the .env.staging to .env
- Install redis server; Default port can be changed on the .env
- For using django server the default database would be sqlite but for docker its postgress
to change default for locally add your database variables on the .env and change ``ENV`` to 
``STAGING``
- If your django server doesn't run on default port ``8000``, change it on the .env , the
 ``CSRF_TRUSTED_ORIGINS`` variable
- Create superuser to access admin
- Install the requirements.


## API Collection
- [Postman Collection link](https://api.postman.com/collections/4541468-1f83c930-c9cf-4bfd-8d9f-1faac672dbc8?access_key=PMAT-01GTVXX6NDGNQAM4RCTS894EC4)
- This collection has 3 endpoints
  - Upload csv file : ``{url}/users/upload/ ``
  - list users search and sort (on postman parameters) : ``{url}/users ``
  - view Uploaded files states: ``{url}/users/files/`` (can be viewed on admin panel)

## Access Django Admin Panel
- `http://localhost:4020/admin`
    - *username:* admin
    - *password:* gateway
- Admin panel is used to view state changes in files

## Finite State Machine 
- States available   
    - uploading
    - pending
    - inserting
    - processed
    - failed
