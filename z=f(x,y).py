import random
import matplotlib.pyplot as plt


def random_direction():
    """随机选择一个三维方向"""
    directions = [
        (1, 0, 0), (-1, 0, 0),  # x轴方向
        (0, 1, 0), (0, -1, 0),  # y轴方向
        (0, 0, 1), (0, 0, -1)  # z轴方向
    ]
    return random.choice(directions)


def three_dimensional_random_walk(max_steps=1000):
    """
    模拟三维随机游走，直到回到原点或达到最大步数
    返回值：1表示成功回到原点，0表示未在max_steps内回到原点
    """
    x, y, z = 0, 0, 0  # 起始位置
    steps = 0

    while steps < max_steps:
        dx, dy, dz = random_direction()
        x += dx
        y += dy
        z += dz

        steps += 1

        # 检查是否回到原点
        if x == 0 and y == 0 and z == 0:
            return 1  # 成功回到原点

    return 0  # 超过最大步数未回到原点


def calculate_probability(num_simulations=1000, max_steps=100):
    """
    计算不同步数下回到原点的概率
    返回一个字典，键是步数，值是概率
    """
    probabilities = {}

    for step in range(1, max_steps + 1):
        success_count = 0

        for _ in range(num_simulations):
            success_count += three_dimensional_random_walk(step)

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
    plt.title('Probability of Returning to Origin vs. Steps (3D Random Walk)')
    plt.xlabel('Steps')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.show()


# 运行程序
if __name__ == "__main__":
    # 计算不同步数下的概率
    probabilities = calculate_probability(num_simulations=1000, max_steps=100)

    # 绘制概率随步数变化的图
    plot_probability(probabilities)