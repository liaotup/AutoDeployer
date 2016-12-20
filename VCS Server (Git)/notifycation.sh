#!/bin/bash
projectName='ProjectName'
token='888v8d6d66d7f8f87d6df78f9f9f9d8f'
cd /home/git/gitBase/ProjectName/
message=$(git log --pretty=format:"%s" -1)
isRedeploy=false
[[ $message =~ "[AUTODT]" ]] && isRedeploy=true
echo $message
curl 'http://yourTomcatServiceIp:8978/gohook?token='$token'&projectName='$projectName'&isNeedReploy='$isRedeploy
