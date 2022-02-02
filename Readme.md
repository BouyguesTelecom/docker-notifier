# Docker notifier

This is a very basic Docker image that sends Microsoft Teams notification 

## Motivation
This image is used to send notification from kubernetes operators 

## Build

Use 
```
docker build . -t docker-notifier 
```

## Usage

### From command line 

#### Teams 
```
docker run -e WEBHOOK_URL=<webhook_url> \
           -e NOTIFICATION_TYPE=Teams \
           -e MESSAGE_TITLE=Title \
           -e MESSAGE_CONTENT=Content \
           -it bouyguestelecom/docker-notifier 
```

#### Mail 
```
docker run -e SMTP_HOST=<smtp_host> \
           -e NOTIFICATION_TYPE=Mail \
           -e MAIL_FROM=foo@bar.com \
           -e MAIL_TO=foo2@bar2.com \
           -e MESSAGE_TITLE=Title \
           -e MESSAGE_CONTENT=Content \
           -it bouyguestelecom/docker-notifier 
```


### From kubernetes 

* Teams: [example here](sample/kubernetes-job-teams.yaml)
* Mail: [example here](sample/kubernetes-job-mail.yaml)
