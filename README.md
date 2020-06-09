演示视频参考
<video id="video" controls="" preload="none" poster="http://om2bks7xs.bkt.clouddn.com/2017-08-26-Markdown-Advance-Video.jpg">
<source id="mp4" src="https://www.iqiyi.com/v_19rxoxbkhk.html#curid=16678996500_b4cdcb4320cdfae5f480487b73576efb" type="video/mp4">
</video>

作者：范东同学
链接：https://www.jianshu.com/p/0742bb15c2dd
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

项目的深度学习代码基于[GPT-2 Chinese](https://github.com/Morizeyao/GPT2-Chinese)项目。
安装方法：
请先于NVIDIA官网下载

  0)  显卡驱动
  1)  CUDA 10.1
  2)  cuDNN 7.6.5 for CUDA 10.1

之后，在Windows Terminal中将工作路径跳转到gpt-2 chinese目录下输入pip install -r requirements.txt


本人在几乎对GPT-2没有改动的前提下，为该项目添加了bat脚本：

  0)  train.bat  训练脚本
  1)  generate.bat  生成脚本

可以根据自己的需要调整bat脚本


# -语料库-
如果您想使用我们的语料库，可以在[网盘链接](https://pan.baidu.com/s/1LcHMtyhUEqpGa46bA1aDTg)（提取码：9k3e）下载语料库。语料库包含：

  0)  已经转换为GPT-2 Chinese要求的JSON格式的《最终幻想14》截至5.1版本的剧本
  1） 已经转换为GPT-2 Chinese要求的JSON格式的《少女前线》截至4月1日的剧本
  2） 尚未转换为GPT-2 Chinese要求的JSON格式的《Fate/Grand Order》1.0的剧本

爬取和整合数据的方式可以参考文件夹“Spider”中的Python脚本

# -模 型-
本人使用了[散文语料](https://github.com/Morizeyao/GPT2-Chinese)预模型、[百度贴吧语料](https://github.com/brightmart/nlp_chinese_corpus)预模型训练了一些可以生成《最终幻想14》风格剧本和《少女前线》风格剧本的模型，如果有需要可以通过[网盘链接](https://pan.baidu.com/s/1xXD8JPS4ibdweMUhu3AwOA)（提取码：uu7p）下载。
