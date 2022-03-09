# Build a simple machine learning python program

# Create 2 empty lists
import random

from sklearn.linear_model import LinearRegression

feature_set = []
target_set = []

# Number of rows for the data set
number_of_rows = 200

# Limit the possible values in the data set
random_number_limit = 1000
for i in range(0, number_of_rows):
    x = random.randint(0, random_number_limit)
    y = random.randint(0, random_number_limit)
    z = random.randint(0, random_number_limit)
# Create a linear function for the target data set
function = (10 * x) + (2 * y) + (3 * z)

# Append the data to the list
feature_set.append([x, y, z])
target_set.append(function)

# Create the model
model = LinearRegression()
model.fit(feature_set, target_set)

# Create the test data set
test_set = [[2, 1, 8]]  # Expected output = function(8,10,0) = 100
prediction = model.predict(test_set)

print('Prediction:' + str(prediction) + 'Coefficients:' + str(model.coef_))
