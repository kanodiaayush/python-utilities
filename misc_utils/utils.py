import pickle
import statsmodels.api as sm
import subprocess

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

def run_command(command, verbose=True):
    if verbose:
        print(command)
    output = subprocess.check_output(command, shell=True)
    output = output.decode('utf-8')
    if verbose:
        print(output)
        print("-------------------------------------------------------")
        print ("\n\n\nCompleted %s\n\n\n" % command)
        print("-------------------------------------------------------")

def make_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

