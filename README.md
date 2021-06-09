# shuati

## leetcode 官方题库网址

 <https://leetcode-cn.com/problemset/algorithms/>

## leetcode刷题指南:[代码随想录]

<https://leetcode-cn.com/circle/article/wGp7Y9/>

## 另外一组题解：[某位大神]

<https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3%20-%20%E7%9B%AE%E5%BD%95.md>

# leetcode 经典题：[熊]

## 数组

* 35 二分法求解
* 283
* 27 双指针
  * 26  (和27对比)--------------
  * 209 滑动窗口（双索引）-----------

* 75 三路快排的思路
* 88 归并排序归并的那一步
* 215 利用快排找到pivot之后，最大值肯定在右边，然后继续找
* 167 对撞指针（双索引技术）
  * 125
  * 345
  * 11
）
  * 3
  * 438
  * 76

## Set Map 使用

| 时间复杂度 | 普通数组 | 顺序数组 | 二分搜索树（平衡） | 哈希表 |
| ---------- | -------- | -------- | ------------------ | ------ |
| 插入       | 1        | n        | logn               | 1      |
| 查找       | n        | logn     | logn               | 1      |
| 删除       | n        | n        | logn               | 1      |

哈希表快，但是没有顺序了

* 349 set
* 350
* 如果 349 和 350 有序？数组的查找和有序是有关系的，比如二分查找
* 242
* 202
* 290
* 205
* 451
* 1 可以边往map里塞，边搜索
* 15
* 16
* 454
* 49
* 447 降复杂度
* 149
* 219 滑动窗口
  * 217
* 220 滑动窗口，查找表，桶排序

## 链表

* 206 翻转链表 经典
* 92 虚拟头节点 翻转的细节需要注意，经常用
* 203 虚拟头节点
  * 24
* 237
* 19 双指针，有点像滑动窗口，经典
  * 61 闭合成环
  * 143 快慢指针，找中点，后半段翻转
  * 234

## 栈和队列

* 20
  * 150
  * 71
* 144 二叉树递归遍历
  * 94
  * 145
  * 341
* 102 层序遍历
  * 103
  * 199
* 279 图的遍历
  * 127
  * 126
* 堆的底层实现
* 347 优先队列 topk
  * 23
<https://github.com/Alex660/Algorithms-and-data-structures/blob/master/demos/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E4%B8%89%E5%BA%8F%E9%81%8D%E5%8E%86.md>

<https://github.com/sisterAn/JavaScript-Algorithms/issues>

## JS 实现基本数据结构

<https://github.com/cunzaizhuyi/ds-algorithm>

## 二叉树和递归

> 一递归就蒙蔽

* 104
  * 226
  * 100
  * 101
  * 222
  * 110 这个不太懂
* 112 一脸懵逼
  * 257
  * 113
  * 129
* 437
* 二分搜索树：
  * 插入，查找，删除
  * 最大值，最小值
  * 前驱，后继
  * 上届，下届
  * 某个元素的排名
  * 第 K 大的元素
* 235 写起来简单，理解难的那种
  * 98
  * 450 这个有点意思，二叉搜索树的基本操作了
  * 108 取中点
  * 230
  * 236

* 二叉搜索树
  * 中序遍历是递增的 left->root->right
  * 前驱，比当前节点小，但是最大的那个节点
  * 后继，比当前节点大，但是最小的那个节点

## 递归和回溯

* 树形问题
  * 17
  * 93
  * 131

* 排列问题 Amn
  * 46
  * 47

* 组合问题 Cmn
  * 77
  * 39
  * 40
  * 216
  * 78
  * 90
  * 401（没做）

* 二维平面
  * 79

* floodfill
  * 200
  * 130
  * 417 先不做了 做 695

* 经典人工智能
  * 51 N 皇后，很多优化思路，还需要复习
  * 52
  * 37 数独

小总结一下就是，像 n 皇后这种，结果是在过程中的，helper 不需要返回值。但是像数独这种，只需要一个结果，可能就 helper 就需要返回值。
关键是 helper 要不要循环。暂时猜一下。如果树的第一层是一个节点，就不用循环，如果是多个节点就要循环。

## 动态规划

* 70
  * 120
  * 64
* 343 最优子结构 重叠子问题
  * 279
  * 91
  * 62
  * 63
* 198 状态转移
  * 213
  * 337 用了递归，应该用动态规划，还需要再看
  * 309

## 贪心算法

* 455
  * 392
  * 435
