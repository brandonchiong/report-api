# report-api

## Setup
- Install python3 if needed:
```
brew install python3
```

- Git Clone this repository
- Change directories to this project's location

## Make virtualenv
On Terminal:

```
python3 -m venv venv
source venv/bin/activate
```

## Install Requirements
```
(venv) pip install -r requirements.txt
```

## Migrate DB
```
(venv) python manage.py migrate
```

## Run Server
```
(venv) python manage.py runserver
```

## API Endpoints

### Create Report
- URL: `http://127.0.0.1:8000/create/`
- Method: POST
- Body Payload (JSON):
```
{
    "title": "Example Title",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 
                    ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
                    ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "created_by": "Jane Doe"
}
```
- Success Response: 
```
Code: 200
Content: {
    "content": "Report ID: 3"
}
```

### Read Report
- URL: `http://127.0.0.1:8000/read/[id]`
- Method: GET
- Success Response: 
```
Code: 200
Content: {
    "title": "Example Title",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 
                    ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
                    ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "created_by": "Jonathan Smith",
    "created_at_timestamp": 1572750697
}
```

### Update Report
- URL: `http://127.0.0.1:8000/update/[id]`
- Method: POST
- Note: Only given fields will be updated.  All fields not required in payload.
- Body Payload (JSON):
```
{
    "title": "Example Revision",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 
                    ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
                    ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "created_by": "Jane Doe"
}
```
- Success Response: 
```
Code: 200
Content: {
    "title": "Example Revision",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 
                    ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
                    ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "created_by": "Jane Doe",
    "created_at_timestamp": 1572750697
}
```

### Delete Report
- URL: `http://127.0.0.1:8000/delete/[id]`
- Method: DELETE
- Success Response: 
```
Code: 200
Content: {
    "content": "Report deleted successfully."
}
```

### List All Reports
List all reports in format: `{"report_id": "report_title"}`
- URL: `http://127.0.0.1:8000/all/`
- Method: Get
- Success Response: 
```
Code: 200
Content: {
    "1": "Example Title",
    "2": "Example Revision",
    "3": "Example Title 3",
}
```