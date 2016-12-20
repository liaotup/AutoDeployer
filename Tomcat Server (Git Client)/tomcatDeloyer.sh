#!/bin/bash
service tomcat stop
echo 'Redeploy project:'$1
webAppPath='/home/tomcat/apache-tomcat-8.5.8/webapps/'
gitBasePath='/home/gitBase/'
configurePath='/home/AutoDeployer/Configure/'
cp -r -f $gitBasePath$1'/out/artifacts/'$1 $webAppPath
cp -f $configurePath$1'/configure.properties' $webAppPath$1'/WEB-INF/classes/configure.properties'
service tomcat start