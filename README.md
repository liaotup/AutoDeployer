## Auto Deployer Depend on VCS —— 基于VCS的项目自动部署工具
***
### 简介 —— Introduction

>适用于多种服务器环境的自动部署 ( Tomcat、Nginx、PHP、Python、NodeJS、Apache... )。

>适用于使用 VCS ( **GIT** / **SVN** ) 等管理版本的项目自动部署到服务器中 ( **同样适用于Git服务器和项目服务器不是同一主机的情况** )。

>AutoDeployer的实现由 **Python** 和 **Shell** 两种脚本组成。

 -

> MultiServer Support ( Tomcat、Nginx、PHP、Python、NodeJS、Apache... )

> Project automatic deploy to Server ( Include the occation that MultiServer )

> AutoDeployer compose with script of **Python** and **Shell**


### 如何使用? —— How To Use？

> 该工具包括两个部分 **VCS Server (Git)** 和 **Tomcat Server (Git Client)** ：

> * VCS Server (Git) 部分安装在版本管理服务器中，由版本服务器的 **构子脚本** 和 **通知脚本** 组成。
>   * 构子脚本 —— 当有新版本提交的时候会被触发的脚本。
>   * 通知脚本 —— 由 **构子脚本** 调用，它会通知 Tomcat服务器进一步执行相关操作。
> * Tomcat Server (Git Client) 部分安装在Tomcat服务器中，由 **更新监听器** 、**更新脚本** 和 **部署脚本** 组成。

>   * 更新监听器 —— 坚听由 **通知脚本** 发来的通知。

>   * 更新脚本 —— 由 **更新监听器** 调用，负责执行内容版本的更新。

>   * 部署脚本 —— 由 **更新监听器** 调用，负责部署新版本的内容到服务目录中的整理个过程（包括重启服务器等，若有需要）。

 -
> Tool include **VCS Server (Git)** and **Tomcat Server (Git Client)** ：

> * VCS Server (Git) part install in Version Control Server，consist of **Hook Script** and **Notification Script** .
>   * Hook Script —— It will call when a new version to push.
>   * Notification Script —— It charge of send the notification to Tomcat Server to excute more operation call By **Hook Script** .
> * Tomcat Server (Git Client) part install in Tomcat Server，consist of  **Update Listener** , **Pull Script** and **Deploy Script** .

>   * Update Listener —— Listen to the notification from **Notification Script** .

>   * Pull Script —— Call by **Update Listener** ，In charge of pull new version content.

>   * Deploy Script —— Call by **Update Listener** ，In charge of the whole stamp of deploy new version content to Tomcat server floder(include restart tomcat server if need).

 -

>![Swimlane](http://oifu7yyhu.bkt.clouddn.com/%E6%B3%B3%E9%81%93%E5%9B%BE.svg)

### PS
> VCS Server (Git)端脚本要放在具体的项目仓库里的 **/hooks**目录里。

> VCS Server (Git)端脚本后台运行命令：**#python main.py &**

> Tomcat Server (Git Client)端要先要配置免密码pull，方法有很多。 (希望有大家更多的pull request补充)

> 如 创建一个没密码的ssh key, 再配置 **/etc/ssh/ssh_config** 文件中的下面属性，如果被注释就打开。
- StrictHostKeyChecking no

> 这篇MarkDown已经用尽了我的洋墨水，应该是错漏百出的，希望有大家更多的pull request完善。

 -

 > VCS Server (Git) side script is locate in **/hooks** floder of project repository.

 > VCS Server (Git) side run in background with comander ：**#python main.py &**

 > Tomcat Server (Git Client) side need to config pull without password, There more ways。 ( hope your pull request to rich it! )

 > For Example : Create a ssh key with out key, and config the flowing property of the file **/etc/ssh/ssh_config**，if front a # then need to got rid it.
- StrictHostKeyChecking no

> This MarkDown is my best level of my English able，There should be many mistake，hope your pull request to fix it！
