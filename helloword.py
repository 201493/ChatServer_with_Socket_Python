
print("Hello, World!")# 初始化 Git 儲存庫
git init

# 新增檔案到 Git 儲存庫
git add hello_world.py

# 提交變更
git commit -m "Add hello world script"

# 將本地儲存庫連接到 GitHub 遠端儲存庫
# 替換 <USERNAME> 和 <REPOSITORY> 為你的 GitHub 使用者名稱和儲存庫名稱
git remote add origin https://github.com/<USERNAME>/<REPOSITORY>.git

# 推送變更到 GitHub
git push -u origin master