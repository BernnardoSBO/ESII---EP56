## Flask Endpoint Checklist

This is an implementation of a simple checklist in flask. The following endpoints are used to manage the checklist:


### GET /tasks
Get all the tasks

### POST /tasks
Create a new task
body = {"task" : value}

### DELETE /tasks/:taskid
Delete task with taskid

### PATCH /tasks/:taskid/complete
Set task with taskid as completed

This repo uses github actions to manage automated testing (CI/CD) of the application in multiple environments (macos, ubuntu, windows)
