import numpy as np

x = np.random.rand(100).reshape((-1,1))

#print(x.shape, x.shape[0])

w = 0
b = 0

labels = 3 * x + 5

def forward_propagation(w, b, x):

    y_hat = w*x + b
    parameters = {"y_hat": y_hat,
                    "w":w,
                    "b":b,
                    "x":x,
                    "m":x.shape[0]}

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

update_parameters(10000, w, b, x, labels, 0.01)