import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import random
import argparse
from pathlib import Path

font_prop = FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
SENTENCES = [
    "想去度假的地方",
    "喜欢的运动",
    "喜欢的音乐",
    "家里有几个成员",
    "去过几个国家",
    "在几个学校读过书",
    "喜欢什麽书或是电影",
    "喜欢的颜色",
    "如果中乐透，你想做什麽",
]

# Adjust the code to remove spaces between cells and ensure grid lines are continuous


def gen_nine_cell_with_texts(output_path: str, file_name: str):
    sents = SENTENCES.copy()
    random.shuffle(sents)

    # Create a new figure with tightly packed cells
    fig, axs = plt.subplots(3, 3, figsize=(8, 8))
    plt.rcParams["font.family"] = "Hiragino Sans GB"
    # Set the entire figure background to white
    fig.patch.set_facecolor("white")

    # Adjust subplot parameters to remove spaces between cells
    plt.subplots_adjust(wspace=0, hspace=0)

    # Loop through the axes to set the background color and remove ticks
    for ax in axs.flat:
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_facecolor(
            "white"
        )  # Set background color of each subplot to white

    # Fill each cell with a Chinese sentence and draw continuous grid lines
    for i, ax in enumerate(axs.flat):
        ax.text(
            0.5,
            0.75,
            sents[i],
            ha="center",
            va="center",
            fontsize=12,
            fontproperties=font_prop,
        )
        # Draw continuous borders
        ax.spines["left"].set_visible(True)
        ax.spines["left"].set_color("black")
        ax.spines["left"].set_linewidth(2)
        ax.spines["bottom"].set_visible(True)
        ax.spines["bottom"].set_color("black")
        ax.spines["bottom"].set_linewidth(2)
        ax.spines["right"].set_visible(True)
        ax.spines["right"].set_color("black")
        ax.spines["right"].set_linewidth(2)
        ax.spines["top"].set_visible(True)
        ax.spines["top"].set_color("black")
        ax.spines["top"].set_linewidth(2)

    # Manually adjust the outer border to ensure continuity
    for spine in plt.gca().spines.values():
        spine.set_visible(True)
        spine.set_color("black")
        spine.set_linewidth(2)
    p = Path(output_path)

    plt.savefig(p / file_name, dpi=300, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output_path",
        "-o",
        type=str,
        help="The path to save the generated image",
    )
    parser.add_argument(
        "--number", "-n", type=int, help="The number of images to generate"
    )
    args = parser.parse_args()
    for i in range(args.number):
        gen_nine_cell_with_texts(args.output_path, f"nine_cell{i}.png")
