# Django + MinIO

This is a simple django project showing how to use MinIO S3 Object Storage budled with it.


## SETUP

### Deploy MinIO in Fandogh PaaS

```py title="MinIO Managed Service"
fandogh managed-service deploy minio latest \
       -c service_name=minio \
       -c minio_access_key=12charchters \
       -c minio_secret_key=12charchters \
       -c volume_name=VOLUME_NAME \
       -m 512Mi 
```
**⚠ WARNING:** you should create a volume before deploying MinIO with command below:

```py
fandogh volume add -n VOLUME_NAME -c 10
```

### Local Test

* run below commands first (in root):
```py
pip install -r requirements.txt
```
```py
python manage.py migrate
```
* Run project
```
python manage.py runserver
```
    
### Fandogh Test

* Initialize a Django Project
```py
fandogh source init --name django
```
    
* Deploy generated manifest
```py
fandogh source run
```
