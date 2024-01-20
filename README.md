This repo is meant to guide you in your fastapi container deployment with binding to host machine (0.0.0.0) and using local


## setting -w option (worker count)
```
workers = (2 * CPU count) + 1
```
Remember: max requests should always be equal to (2*CPU) + 1
so if using threads remember threads + workers = (2*CPU) + 1

## more on gunicorn:
Link [https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7]

## Docker Build
```
docker build . -t my_fastapi_image
```

## Docker Run
```
docker run -p 8000:8000 -v absolute/path/to/local/dir:/logs my_fastapi_image
```
1. -v option needs fully qualified path on both sides
2. e.g. /home/john/logs:/logs (in this case fastapi can write to /logs and those files are in host file system)
3. e.g. docker run -p 8000:8000 -v /Users/johndoe/Downloads/fastapi-boilerplate-main/logs:/logs my_fastapi_image