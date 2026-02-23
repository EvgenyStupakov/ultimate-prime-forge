#  Ultimate Prime Forge Lab

**Ultimate Prime Forge Lab** is an experimental Python project for generating large prime numbers using multiple algorithmic strategies. It combines four generation approaches, checks candidates for primality, and provides real-time statistics.

---

## Generators

### 1. Chaotic Generator

Uses **chaotic sequences**:  
\[
x_{n+1} = (a \cdot x_n + b) \mod m
\]  

**Example primes (sample):**  

876511922772685957, 385023078151872827, 865161457773081653, ...


**Distribution heatmap (ASCII):**  

##### ###### ##### ###### ##### ##### ##### ######


---

### 2. Wave Generator

Uses **sinusoidal functions**:  
\[
y_n = A \cdot \sin(B \cdot n + C) + D
\]  

**Example primes (sample):**  

399625414571756801, 405577648247116801, 412215674311024193, ...

**Distribution heatmap (ASCII):**
##### ###### ##### ###### ##### ##### ##### ######


---

### 4. Hybrid Generator

Mixes **chaotic sequences and multi-wave methods**:  
\[
z_n = f_{\text{chaotic}}(x_n) + f_{\text{multiwave}}(n)
\]  

**Example primes (sample):**  


879520909440903809, 142461756425617697, 797717209043068801, ...

**Distribution heatmap (ASCII):**
##### ###### ##### ###### ##### ##### ##### ######


---

## Usage

### Run from Console
```bash
python -m core.ultimate_generator

Example session

Enter lower bound (e.g., 1e17): 1e17
Enter upper bound (e.g., 1e18): 1e18
Enter generation time in seconds (e.g., 30): 30

Program displays the last N generated primes per generator and a summary at the end:

Chaotic stats: primes=5140 | time=30.00s | rate=171.33 primes/sec
Wave stats: primes=12252 | time=30.00s | rate=408.39 primes/sec
MultiWave stats: primes=10041 | time=30.00s | rate=334.69 primes/sec
Hybrid stats: primes=10213 | time=30.01s | rate=340.32 primes/sec

Python Example

from core.ultimate_generator import UltimatePrimeGenerator

upg = UltimatePrimeGenerator(waves=6)
primes = upg.generate(lower=10**17, upper=10**18, duration=30, max_display=10)

for gen_name, nums in primes.items():
    print(f"{gen_name} found {len(nums)} primes. Last 5 primes: {nums[-5:]}")

Settings

waves — number of waves for MultiWave and Hybrid generators

lower and upper — range of numbers for generation

duration — generation time in seconds

max_display — number of last primes to show in console

Features

Generates large primes for cryptography or testing

Multiple algorithms with different number distributions

Primality check using Miller-Rabin

Real-time display of generated numbers

Visual ASCII-based distribution heatmaps per generator


