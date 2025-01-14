from PIL import Image

# 打开两张图片
image1 = Image.open('1.jpg')
image2 = Image.open('2.jpg')

# 获取图片尺寸
width1, height1 = image1.size
width2, height2 = image2.size

# 创建一个新的空白图片，宽度为两张图片宽度之和，高度为较高的那张
result_width = width1 + width2
result_height = max(height1, height2)
result = Image.new('RGB', (result_width, result_height))

# 将两张图片粘贴到新图片上
result.paste(image1, (0, 0))
result.paste(image2, (width1, 0))

# 保存结果
result.save('merged_image.jpg')
