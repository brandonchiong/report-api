# report-api

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

### - Create Report
`http://127.0.0.1:8000/create/`
- Method: POST
- Payload:
```
{
	"title": "Example Title",
	"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
                        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
                        ullamco laboris nisi ut aliquip ex ea commodo consequat.",
	"created_by": "Jane Doe"
}
```


### - Read Report
`http://127.0.0.1:8000/read/[id]`
- Method: GET

### - Update Report
`http://127.0.0.1:8000/update/[id]`
- Method: POST
- Note: Only given fields will be updated.  All fields not required in payload.
- Payload:
```
{
	"title": "Example Revision",
	"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
                        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
                        ullamco laboris nisi ut aliquip ex ea commodo consequat.",
	"created_by": "Jane Doe"
}
```

### - Delete Report
`http://127.0.0.1:8000/delete/[id]`
- Method: DELETE