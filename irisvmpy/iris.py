#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simple Iris data set classifier based on Support Vector Machines algorithm.
"""

from __future__ import print_function
import time
from sklearn import svm, datasets
import click
import numpy as np


# import some data to play with
iris = datasets.load_iris()

X = iris.data  # we only take the first two features. We could
# avoid this ugly slicing by using a two-dim dataset
y = iris.target
#click.echo(X);
#click.echo(y);


svc = svm.SVC(kernel='rbf', C=1, gamma=0.7).fit(X, y)

dimm_names = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']


@click.command()
@click.argument('dimensions', nargs=4, type=float)
def cli(dimensions):
    """Basic command line interface.

    Arguments:
    dimensions {list} -- list of flower dimensions: PL, PW, SL, SW
    """
    #click.echo("Iris Flower classifier\n")

    #click.echo("Calculating result...")
    results = zip(dimm_names, dimensions)
    prediction = svc.predict(np.reshape(dimensions,(1,-1)));
    #click.echo(prediction[0]);
    #click.echo("Input data:")
    #for i, j in results:
        #click.echo("{:12} -> {}".format(i, j))

    #click.echo()

    #click.echo("Your flower seems to be fine example of:")
    #click.secho("{}".format(prediction[0]), fg='green', bold=True)
    click.echo(prediction[0])


if __name__ == "__main__":
    cli()
