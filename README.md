# python  
for learning python here

＃ 第一次将远程仓库导入到本地  
git clone https://github.com/connonfodder/python.git  
git init  

git add README.md  
＃添加文件进去  
git add .           ＃一定是在根目录下使用这个命令  
git commit -m "first commit"  
git remote add origin https://github.com/connonfodder/python.git  

git push -u origin master  

＃以后再提交  
git add .  
git push -u origin master  