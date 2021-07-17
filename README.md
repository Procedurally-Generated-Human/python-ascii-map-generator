Creates maps using cellular automata rather then the more popular perlin noise

2-5 generations and a land percentage between 40-60 tend to create the best looking maps

Note: there is not a singular cellular automata algorithm, the one used in this code turns a point into a land(#) if 5-7 of its neighbours are land.
     the function "cellular_automata" is where you can change the rules.
