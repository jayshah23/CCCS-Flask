import pickle
import numpy as np

modelA = pickle.load(open('Model_Jay.pkl', 'rb'))
final_data = np.array([[1854.03, 1013.50, 1243.09, 2000.0, 654.47, 1524.38, 1.00]])
prediction = modelA.predict(final_data)
print(prediction)