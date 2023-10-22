[代码规范来源](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)


# 模板样式

在 Django 模板代码中，在卷曲之间放置一个（并且只有一个）空格 括号和标记内容。

这样做：

`{{ foo }}`

别这样：

`{{foo}}`

# 视图样式

在 Django 视图中，应该调用视图函数中的第一个参数。request

这样做：

`def my_view(request, foo):
    ...`
    
别这样：

`def my_view(req, foo):
    ...`



