This package is designed for probability distributions. Therefore, it contains two classes for performing calculations and their graphics.


Available distributions:
-Gaussian
-Binomial

These distributions have some methods such as mean calculation, standard deviation calculation, histograms, sum of distributions, ...

Each object has its data attribute, so you can put a list on the object and perform all calculations


Example:

    from distributions import Gaussian, Binomial

    dist_gaussian=Gaussian(3, 5)  mean=3, std=5
    dist_gaussian.data=[1, 3, 5, 6 ,2,  1, 2, 3, 4, 3, 2, 5, 2, 4, 6, 2, 3, 5, 8]
    dist_gaussian.replace_stats_with_data()
    dist_gaussian.plot_histogram_pdf()
