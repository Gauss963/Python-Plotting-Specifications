# Plotting Specifications

- Please place the legend at `upper right`, the second choice is `upper left`.
  ```Python
  ax.legend(loc = 'upper right')
  ```
  or
  ```Python
  ax.legend(loc = 'upper left')
  ```

- Please set the figure size as `8in * 6in`, or larger but in the same aspectratio.

  ```Python
  fig = plt.figure(figsize = (8, 6))
  ```
  or
  ```Python
  fig = plt.figure(figsize = (16, 12))
  ```

- Please use the matplotlib built in font: `serif`,
  - `siez = 20` for title.
  - `size = 24` for $x$ and $y$ label.

  ```Python
  font1 = {'family':'serif', 'color':'black', 'size':20}
  font2 = {'family':'serif', 'color':'black', 'size':14}

  ax.set_title('SomeTitle', fontdict = font1)
  ax.set_xlabel('SomeLabelName', fontdict = font2)
  ```

- Please use `tight_layout` before saving the figure.
  ```Python
  plt.tight_layout()
  ```

- Please save the figure into `.pdf` format, and use `dpi = 300`.

  ```Python
  plt.savefig('filename.pdf', dpi = 300, bbox_inches = 'tight')
  ```