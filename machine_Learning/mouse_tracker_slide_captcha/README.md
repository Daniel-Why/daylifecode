# 概述
本项目拟通过鼠标轨迹判断使用滑动验证码的访客是否为 **Bot**.

# 文件描述

* 文件夹 orginal_data 用于存放原始数据
  * 原始数据格式："是否是bot|验证成功与否|验证数据获取时间戳[x0,y0,时间戳],[x1,y1,时间戳]..."
* 文件夹 clean_data 用于存放清洗后的数据
* clean_data_flow.py 能流程化地进行数据清洗和特征提取，主要运行以下文件：
  * clean_data_step_01.py :
    * 提取验证码验证数据，包括机器人与否、验证成功与否、数据获取时间、鼠标移动数据，并生成csv
  * clean_data_step_01.py
    * 删除点击拖动块、开始滑动之前的数据
  * extract_feature.py
    * 提取鼠标轨迹特征
* mouse_tracker_model.py 学习模型
* model_learning_curve.py 学习曲线