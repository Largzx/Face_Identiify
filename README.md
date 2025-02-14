# 简要介绍

- 使用pyqt5+opencv级联数据库实现多人脸动态识别
- 在使用流程上，仍旧存在某些bug  

## 文件说明  

Facedata——存放录入的人脸图片  

Haar——存放opencv的正脸分类器模型，用于检测人脸 

skin——界面皮肤

trainer——根据facedata训练的模型  

Face_Identiify_ALL.py、Main.py——均可直接运行  

record.json——用于匹配Facedata中人脸编号与姓名，使编号范围与人名对应  



