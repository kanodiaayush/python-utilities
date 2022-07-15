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

## Automatic reload of classes in notebooks
