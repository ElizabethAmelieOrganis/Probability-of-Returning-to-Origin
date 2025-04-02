import random
import matplotlib.pyplot as plt
from collections import defaultdict


def random_direction():
    """随机选择一个方向（左或右）"""
    return random.choice([-1, 1])


def one_dimensional_random_walk(max_steps=1000):
    """
    模拟一维随机游走，记录每一步的位置
    返回最终位置
    """
    position = 0  # 起始位置

    for _ in range(max_steps):
        position += random_direction()

    return position


def calculate_position_probabilities(num_simulations=100000, max_steps=1000):
    """
    计算不同位置的概率
    返回一个字典，键是位置，值是概率
    """
    position_counts = defaultdict(int)

    for _ in range(num_simulations):
        final_position = one_dimensional_random_walk(max_steps)
        position_counts[final_position] += 1

    # 计算概率
    probabilities = {}
    total_simulations = num_simulations
    for position, count in position_counts.items():
        probabilities[position] = count / total_simulations

    return probabilities


def plot_probability_distribution(probabilities):
    """
    使用matplotlib绘制位置概率分布图
    """
    positions = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(12, 6))
    plt.bar(positions, probs, width=0.8)
    plt.title('Probability Distribution of Final Positions (1D Random Walk)')
    plt.xlabel('Position')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.show()


# 运行程序
if __name__ == "__main__":
    # 计算不同位置的概率
    probabilities = calculate_position_probabilities(num_simulations=100000, max_steps=1000)

    # 绘制位置概率分布图
    plot_probability_distribution(probabilities)
