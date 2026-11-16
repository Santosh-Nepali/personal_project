#Mini miner
The game will have a stationary miner at the top, while gold, rocks, diamonds, and bombs automatically travel upward from the bottom. The player uses mining tools to destroy or collect objects before they reach the miner.

## Gameplay rules

```python
Element	            Behaviour
Miner	        Stays at the top
Gold	        Moves upward; collect with mining tool
Diamond	        Moves upward; collect with mining tool
Rock	        Requires multiple hits to break
Bomb	        Moves upward; damages miner if it reaches the danger zone
Pickaxe	        Attacks nearby objects
Hammer	        Deals more damage to rocks
Health	        Decreases when bombs reach the miner
Score	        Increases when minerals are collected
```

How we will use matrices
We will use 3×3 matrices for all 2D transformations.

```python

  Matrix	                        Application in your game
Translation	                    Move gold, rocks, diamonds and bombs upward
Rotation	                    Rotate diamonds, bombs and pickaxes
Scaling	                        Animate rock damage and bomb explosions
Combined transformation	        Position, rotate and scale objects together

```

For example, when a gold object moves upward:
\[
T=
\begin{bmatrix}
1&0&0\\
0&1&-v\\
0&0&1
\end{bmatrix}
\]

Here, \(v\) is the object's upward movement speed.

When a diamond rotates:
\[
R=
\begin{bmatrix}
\cos\theta&-\sin\theta&0\\
\sin\theta&\cos\theta&0\\
0&0&1
\end{bmatrix}
\]

When a rock breaks:
\[
S=
\begin{bmatrix}
s&0&0\\
0&s&0\\
0&0&1
\end{bmatrix}
\]

We will combine these matrices into one transformation:
\[
M=T\times R\times S
\]

This is the mathematical foundation of our JavaScript game engine.
