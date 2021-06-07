# Stock-Trading-Using-RL-custom-env-

#1. Creating custom environment for stock trading 
#2. Here we created a stock environment(stock-v0) for below condition,
    if ( Open < Price ): # As there are Open, High, Low, Price and Volume columns in the stock timeseries(dataset).
      action = Buy # an agent should take action buy
    elif ( Open > Price ):
      action = Sell # an agent should take action sell
      
#3. we used that custom environment in this program and we uses one of the RL algorithem such as A2C and PPo2.
#4. In PPO2 we used "Mlppolicy", it is Artificial neural networks. (MLP stands for multi layered perceptron)
