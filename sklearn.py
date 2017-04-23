from skelearn import svm, datasets

class Dataset(object):
	 
	def __init__(self, name):
		self.name = name

	def download_data(self):
		if self.name == 'iris':
			self.download_data = datasets.load_iris()
		elif self.name == 'digits':
			self.download_data = datasets.load_digits()
		else:
			print('Dataset Error : No named datasets')
	
	def generate_xy(self):
		self.download_data()
		x = self.download_data.data
		y = self.download_data.target
		print('\nOriginal data looks like this: \n', x)
		print('\nLables looks like this: \n', y)
		return x, y

	def get_train_test_set(self, ratio):
		x, y = self.generate_xy()
		n_samples = len(x)
		n_train = n_samples * ratio
		x_train = x[:n_train]
		y_train = y[:n_train]
		x_test = x[n_train:]
		y_test = y[n_train:]
		return x_train, y_train, x_test, y_test

data = Dataset('digits')
			
		
