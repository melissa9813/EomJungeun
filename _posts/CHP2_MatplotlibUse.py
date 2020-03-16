# HISTOGRAM

    import matplotlib.pyplot as plt

    # making histogram (bins, figsize)
    housing.hist(bins=50, figsize=(20,15))
    # to make the histogram in jupyter noteboook
    plt.show()

# Visualization - SCATTER

    housing.plot(kind="scatter", x="longitude", y="latitude")

    # to show better density,
    housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)
    