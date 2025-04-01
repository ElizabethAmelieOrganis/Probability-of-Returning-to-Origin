import random
import matplotlib.pyplot as plt


def random_bool():
    """以0.5的概率返回True或False"""
    return random.random() < 0.5


def one_dimensional_random_walk(max_steps=1000000):
    """
    模拟一维随机游走，直到回到原点或达到最大步数
    返回值：1表示成功回到原点，0表示未在max_steps内回到原点
    """
    position = 0  # 起始位置
    steps = 0

    while steps < max_steps:
        # 随机决定移动方向
        if random_bool():
            position += 1  # 向右移动
        else:
            position -= 1  # 向左移动

        steps += 1

        # 检查是否回到原点
        if position == 0:
            return 1  # 成功回到原点

    return 0  # 超过最大步数未回到原点


def calculate_probability(num_simulations=1000, max_steps=1000):
    """
    计算不同步数下回到原点的概率
    返回一个字典，键是步数，值是概率
    """
    probabilities = {}

    for step in range(1, max_steps + 1):
        success_count = 0

        for _ in range(num_simulations):
            success_count += one_dimensional_random_walk(step)

        probabilities[step] = success_count / num_simulations

    return probabilities


def plot_probability(probabilities):
    """
    使用matplotlib绘制概率随步数变化的图
    """
    steps = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.plot(steps, probs, 'b-', alpha=0.7)
    plt.title('Probability of Returning to Origin vs. Steps (1D Random Walk)')
    plt.xlabel('Steps')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.show()


# 运行程序
if __name__ == "__main__":
    # 计算不同步数下的概率
    probabilities = calculate_probability(num_simulations=1000, max_steps=1000)

    # 绘制概率随步数变化的图
    plot_probability(probabilities)