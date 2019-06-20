##02-HTML和CSS进阶


###00- 知识点预习
-	1.列表标签
- 	2.选择器及选择器的权重
-  3.CSS的文本样式属性
- 	4.表格标签
-  5.元素溢出
-  6.盒子模型



###01- 列表
- 无序列表 ul>li    unorder list
- 清除列表前面的标识 list-sytle:none;
- 列表默认有外边框和内边距



###02- CSS选择器02

```
    /* 1.ID选择器  id是唯一的; 配合js来操作*/
    #three{
        color:blue;
    }
    

   /* 2. strong标签 重要的内容  默认加粗*/
   /* 并集选择器 组选择器 */
   span,strong{
      color:green; 
   }

   /* 3.伪类选择器 '作用在标签身上 改变状态'
   鼠标悬浮: hover
   a:hover{
      color:orange; 
   }

```

###03-选择器权重计算
-	**层级选择器累加权重值**
- **权重较高会覆盖较低的**
- **权重相同时后写的会覆盖前面的**


选择器 |  权重值
---|---
1.标签    |    1
2.类      |   10
3.ID      |   100
4.行内式    | 1000
5.!important  |10000       **提升属性的权重**


###04- CSS常用属性

```
/* 1.文本对齐 left  center right*/
    text-align: left;

    /* 2.首行缩进  默认大小16px*/
    /* text-indent: 32px; */
    /* em 文字的倍数 */
    text-indent: 2em;

    /* 3.是否斜体   normal*/
    /* font-style: italic; */

    /* 4.是否加粗  normal*/
    font-weight: bold;
    font-size:10px;
    line-height: 20px;
    font-family: "microsoft yahei";


    /* 连写  一定规则*/
        /* 加粗       斜体  字体大小/行高  字体 */
    font:normal italic 10px/20px "microsoft yahei";


```

###05-表格(table)基本使用
```
table:
        tr row 行数
        td description  内容
        th head ;居中 加粗
		 /* 3.合并边框 */
        border-collapse: collapse;
         
        跨列合并: colspan  找到第几行的哪个内容, colspan="几列";多余的删除
        跨行合并: rowspan  找到第几行的那个内容, rowspan = "几行";多余的删除
```

###06-表格案例
![表格案例](./笔记中的图片/007_表格布局.jpg)

###07- 元素溢出
-	**overflow:**
	-  visible  默认 超出可视 
	- 	hidden  超出隐藏 裁剪
	-  scroll	  可滚动 不推荐使用
	-  auto  自动
	

###08-  盒子模型真实宽高

	真实的宽 = 左边框'border-left' + 右边框'border-right' + 内容宽'width' + 左边内边距'padding-left' + 右边内边距'padding-right';
	真实的高 = 上边框'border-top' + 下边框'border-right' + 内容高'height' + 顶部内边距'padding-top' + 底部内边距'padding-bottom';
	
	
**理解练习**  
通过盒子模型的原理，制作下面的盒子：

![课堂练习示例图片](./笔记中的图片/box_practice.jpg)




