#算子总结
# Sobel算子和Scharr算子计算的都是一阶近似导数的值。通常情况下，可以将它们表示为：
# Sobel算子=|左-右| /|下-上|
# Scharr算子=|左-右| /|下-上|
# 式中“|左-右|”表示左侧像素值减右侧像素值的结果的绝对值，“|下-上|”表示下方像素值减上方像素值的结果的绝对值。
# Laplacian算子计算的是二阶近似导数值，可以将它表示为：
# Laplacian算子=|左-右|+|左-右|+|下-上|+|下-上|
# 通过公式可以发现，Sobel算子和Scharr算子各计算了一次“|左-右|”和“|下-上|”的值，而Laplacian算子分别计算了两次“|左-右|”和“|下-上|”的值。