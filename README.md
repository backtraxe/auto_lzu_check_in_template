# auto_lzu_check_in_template

兰州大学自动每日健康打卡

步骤：

1. 新建仓库。

<img src="imgs/step1.png" width="640px" />

2. 选择`Import a repository`。

<img src="imgs/step2.png" width="640px" />

3. 填入`https://github.com/backtraxe/auto_lzu_check_in_template`，名字随意，选择`private`（确保密码不公开），然后导入。

<img src="imgs/step3.png" width="640px" />

4. 进入创建的仓库。

<img src="imgs/step4.png" width="640px" />

5. 打开`main.py`。

<img src="imgs/step5.png" width="640px" />

6. 编辑`main.py`。

<img src="imgs/step6.png" width="640px" />

7. 填入自己的学号和密码（用来登录兰大个人工作台），然后保存并提交。

<img src="imgs/step7.png" width="640px" />

8. 编辑`.github/workflows/main.yml`，将`- cron: ''`改为`- cron: '0 17,20,23,2 * * *'`，然后保存并提交。

<img src="imgs/step8.png" width="640px" />
