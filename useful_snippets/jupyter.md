## Save Jupyter notebook state and reload

This is very useful because a dead kernel means that you need to run the notebook again.

```
# To save the model state
import dill
dill.dump_session('SAVE_PATH.db') # note that the file format is .db

# To reload the model from a saved state
import dill
dill.load_session('SAVE_PATH.db')
```

## Automatic reload in notebooks

This is to reload packages automatically in Jupyter notebooks. We keep running into situations where we have made changes to an external python file which we need to use in the jupyter notebook. This code snippet automatically reloads in your notebook.

Note: this snippet needs to be the absolute first thing that you run in your jupyter notebook. It won't work otherwise.
```
%load_ext autoreload
%autoreload 2
```
