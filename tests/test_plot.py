import matplotlib.pyplot as plt
import numpy as np
import pytest

import dufte


@pytest.mark.parametrize(
    "filename, light, noise, offsets",
    [[None, True, 0.1, (1.0, 1.50, 1.60)], [None, True, 0.0, (1.0, 1.50, 1.51)]],
)
def test_plot(filename, light: bool, noise, offsets):
    rng = np.random.default_rng(0)
    x0 = np.linspace(0.0, 3.0, 100)
    labels = ["no balancing", "CRV-27", "CRV-27*"]

    with plt.style.context(dufte.style):
        for label, offset in zip(labels, offsets):
            y0 = offset * x0 / (x0 + 1)
            y0 += noise * rng.random(len(y0))
            plt.plot(x0, y0, label=label)

        plt.xlabel("distance [m]")
        dufte.ylabel("voltage [V]")
        # plt.title("title")
        dufte.legend()

        if not light:
            gh_dark_bg = "#0d1117"
            plt.gca().set_facecolor(gh_dark_bg)
            plt.gcf().patch.set_facecolor(gh_dark_bg)

        if filename:
            plt.savefig(filename, transparent=True, bbox_inches="tight")
        else:
            plt.show()


def test_no_labels():
    plt.style.use(dufte.style)

    np.random.seed(0)
    n = 100
    x0 = np.linspace(0.0, 3.0, n)
    y0 = 1.0 + 0.1 * np.random.rand(n)
    plt.plot(x0, y0, label="rand 1")

    y0 = 2.0 + 0.1 * np.random.rand(n)
    # no label
    plt.plot(x0, y0)

    y0 = 3.0 + 0.1 * np.random.rand(n)
    plt.plot(x0, y0, label="rand 3")

    dufte.legend()
    # plt.legend()
    plt.show()


def test_nan():
    plt.style.use(dufte.style)
    x0 = [0.0, 0.5, 1.0]
    y0 = [0.0, 0.5, np.nan]
    plt.plot(x0, y0, label="nan")

    dufte.legend()
    # plt.legend()
    plt.show()


def test_all_nan():
    plt.style.use(dufte.style)
    x0 = [0.0, 0.5, 1.0]
    y0 = [np.nan, np.nan, np.nan]
    plt.plot(x0, y0, label="nan")

    dufte.legend()
    # plt.legend()
    plt.show()


if __name__ == "__main__":
    # test_plot(None, True, 0.1, (1.0, 1.5, 1.6))
    # test_plot("ex1-light.svg", True, 0.1, (1.0, 1.5, 1.6))
    # plt.close()
    # test_plot("ex1-dark.svg", False, 0.1, (1.0, 1.5, 1.6))
    test_plot("ex1.svg", False, 0.1, (1.0, 1.5, 1.6))
    plt.close()
