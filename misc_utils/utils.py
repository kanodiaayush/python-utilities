import pickle
import statsmodels.api as sm

def load_pickle(filename):
    with open(filename, 'rb') as f:
        ans = pickle.load(f)
    return ans

def reg(X, Y, add_constant=True, print_model=True):
	if add_constant:
      X = sm.add_constant(X) # adding a constant
    
    model = sm.OLS(Y, X).fit()
    predictions = model.predict(X) 
    
    print_model = model.summary()
	if print_model:
    	print(print_model)
	return model
