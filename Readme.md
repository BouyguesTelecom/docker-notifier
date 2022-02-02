# Docker teams notifier

This is a very basic Docker image that sends Microsoft Teams notification 

## Build

Use 
```
docker build . -t teams-notifier 
```

## Usage
```
docker run -e WEBHOOK_URL=<webhook_url> \
           -e MESSAGE_TITLE=Title \
           -e MESSAGE_CONTENT=Content \
           -it teams-notifier 
```
