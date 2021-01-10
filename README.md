# heyboxAutoSignIn
小黑盒自动签到

## 使用

0. 先fork本项目 [![GitHub forks](https://img.shields.io/github/forks/cyb233/heyboxAutoSignIn?style=social)](https://github.com/cyb233/heyboxAutoSignIn)

1. 使用抓包软件获取小黑盒的`COOKIE`
 - 抓包软件怎么用？请去问百度谷歌

2. 在设置中创建action secrets `COOKIE`;
![secrets1](/pic/Screenshot_2021_0110_131637.png)

3. 在actions中开启
 - **请勿滥用GitHub Actions！**

4. 修改自动运行时间：
 - 打开`heyboxAutoSignIn/.github/workflows/auto_sign_in.yml`
 - 在`第12行`修改`cron表达式`，默认北京时间每天`3:30`,`17:30`执行
 - cron表达式怎么改？请去问百度谷歌

5. (可选)使用server酱推送到微信：
 - 在server酱官网 sc.ftqq.com 登录并复制`SCKEY`
 - 在设置中创建action secrets `SCKEY`
![secrets2](/pic/Screenshot_2021_0110_131647.png)

6. 使用效果：  
hkey算法太旧无法获得奖励……
![result](/pic/IMG20210111054842.jpg)

## 致谢
[小黑盒逆向分析笔记（二）](https://blog.chrxw.com/archives/2020/08/05/1347.html)中hkey的获取方法
