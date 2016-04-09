# S3-Spiral

This is a 3D sprial my Dad and I stumbled upon a few years ago. We have been toying with it and what it means and does.

When running the command in a python interpeter, you type; `datagen(t,pmax,step)`

-  t = This is the value that is being calculated to make the sprial. This can be any intager value.

-  pmax = this is **important!** This is the number of points you are plotting! This can be any non-zero intager number. If you pmax is zero, you get no points.

-  step = this is the resolution of the data, how finely it is plotted. If you pick a number over 1, it will not be fine enough. It is suggested to start at 0.1 and refine as you see nessiarary.

##### Please take note! The script uses a web api called plot.ly, this script plots into the Plot.ly demo account if you plot over the same file too many times the data becomes corrupt.
Please modify `py.plot(fig, filename='')` to a new filename or put in your own **api key** and **username**.
