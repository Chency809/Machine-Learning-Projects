from interesting_try.parameters_initialization import *

weights = [0 ,0 ,0]
b = 0

def forward_propagation(weights, x1, x2, x3, b):

    y_hat = weights[0]*x1 + weights[1]*x2 + weights[2]*x3 + b
    parameters = {"y_hat": y_hat,
                    "weights":weights,
                    "b":b,
                    "x":x1,
                    "x":x2,
                    "x":x3,
                    "m":x1.shape[0]}

    return parameters

def cost_funciton(parameters, labels):

    y_hat = parameters["y_hat"]
    m = parameters["m"]

    cost = (np.sum(y_hat - labels)**2)/(2*m)

    return cost

def back_propagation(parameters, labels):

    y_hat = parameters["y_hat"]
    m = parameters["m"]

    dw= x.T.dot((1/m)* (y_hat - labels))
    db = (1/m)*sum(y_hat - labels)

    grads = {"dw": dw,
            "db": db}

    return grads

def update_parameters(epochs, w, b, x, labels, lr):

    parameters = forward_propagation(w ,b, x)
    grads = back_propagation(parameters, labels)

    for i in range(epochs):
        parameters["w"] -= lr*grads["dw"]
        parameters["b"] -= lr * grads["db"]

        parameters = forward_propagation(parameters["w"], parameters["b"] , x)
        grads = back_propagation(parameters, labels)

    print(parameters["w"], parameters["b"])