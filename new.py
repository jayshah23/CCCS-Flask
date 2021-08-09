import pickle
import numpy as np

modelA = pickle.load(open('Model_Jay.pkl', 'rb'))
final_data = np.array([[129.84,1433.99,0.00,4000.0,1363.13,141.65,0.88]])

# modelA = pickle.load(open('model1.pkl', 'rb'))
# final_data = np.array([[1854.03, 1.00, 1013.50, 576.00, 437.50, 1243.09, 0.50, 0.08, 0.33, 0.08, 5, 15, 2000.0, 654.47, 
#                      1524.38, 0.00, 12, 20]])

prediction = modelA.predict(final_data)
print(prediction)

# import struct
# print(struct.calcsize("P")*8)