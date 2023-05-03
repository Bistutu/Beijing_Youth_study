# 北京青年大学习-使用说明


```sh
# 首次运行建立环境
cd ~
git clone https://github.com/Bistutu/Beijing_Youth_study.git
cd Beijing_Youth_study
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

### 命令行手动运行：

```shell
python3 main.py 你的账号 你的密码
```

#### shell脚本自动运行：

当前目录新建 `run.sh`，写入以下内容：

```
#!/usr/bin/bash
python3 main.py 你的账号 你的密码
```

之后使用 crontab 配置自动运行，执行 `crontab -e`，在打开的编辑器中写入：

```shell
0 8 */3 * * ~/Beijing_Youth_study/run.sh
```

重启 cron  即可：

```shell
sudo service cron restart
```



