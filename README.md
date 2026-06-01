# Fault Diagnosis in Industrial Systems Using Deterministic and Probabilistic Reasoning

## Introduction

Fault diagnosis is an important process in industrial systems used to detect, identify, and analyze faults in machinery and equipment. Modern industries rely on sensors to monitor parameters such as temperature, pressure, and vibration. However, sensor readings often contain noise and uncertainty, making fault detection challenging.

This project develops an intelligent fault diagnosis system that combines rule-based reasoning, search techniques, constraint checking, probabilistic reasoning, and decision-making methods. The system analyzes sensor readings, identifies possible faults, estimates fault probabilities, and recommends appropriate actions.

---

## Aim

To design and implement an AI-based fault diagnosis system that uses noisy sensor readings to detect faults and compare deterministic reasoning with probabilistic reasoning for industrial decision-making.

---

## Course Outcomes (COs) Used

### CO1 – Agent Model and Knowledge Representation

* PEAS-based intelligent agent concept
* State representation using Python dataclasses
* Rule-based knowledge representation
* Use of Python data structures such as lists, dictionaries, and sets

### CO2 – Search Algorithms

* Breadth First Search (BFS)
* Fault graph exploration
* State-space traversal for fault discovery

### CO3 – Constraint Satisfaction Problems (CSP)

* Constraint checking
* Detection of sensor limit violations
* Explainable reasoning through constraint failure analysis

### CO4 – Decision Making

* Utility-based decision selection
* Action recommendation based on fault severity
* Rational decision-making under uncertainty

### CO5 – Probabilistic Reasoning

* Bayesian-inspired fault probability estimation
* Sensor fusion concepts
* Uncertainty-aware diagnosis

### CO6 – Hybrid Intelligent Systems

* Integration of search, constraints, rules, probability, and decision logic
* Explainable reasoning trace
* Performance-oriented fault diagnosis architecture

---

## Technologies Used

* Python 3.x
* Dataclasses
* Collections Module (Deque)
* Typing Module
* Object-Oriented Programming (OOP)
* Artificial Intelligence Concepts
* Rule-Based Systems
* Graph Search Techniques

---

## Algorithm

### Step 1: Input Collection

Collect sensor readings:

* Temperature
* Pressure
* Vibration

### Step 2: Search Analysis

Use Breadth First Search (BFS) to explore the fault graph and identify possible fault paths.

### Step 3: Constraint Checking

Verify whether sensor values satisfy predefined operational constraints.

### Step 4: Rule-Based Diagnosis

Apply deterministic rules to identify likely faults.

### Step 5: Probabilistic Diagnosis

Calculate fault probability based on abnormal sensor readings.

### Step 6: Decision Making

Select an appropriate maintenance action using utility-based reasoning.

### Step 7: Generate Reasoning Trace

Provide a transparent explanation of how the final decision was reached.

---

## How to Run the Code

### Prerequisites

Install Python 3.9 or above.

Verify installation:

```bash
python --version
```

### Run the Application

Navigate to the project directory and execute:

```bash
python app.py
```

---

## Example Input

```text
Temperature = 92
Pressure = 45
Vibration = 8.5
```

---

## Example Output

```text
======================================
INDUSTRIAL FAULT DIAGNOSIS SYSTEM
======================================

Sensor Readings

Temperature : 92
Pressure    : 45
Vibration   : 8.5


---

## Conclusion

The developed system demonstrates how Artificial Intelligence techniques can be applied to industrial fault diagnosis. By combining deterministic rules, search algorithms, constraint satisfaction, probabilistic reasoning, and utility-based decisions, the system provides reliable and explainable fault detection. The project also illustrates the practical implementation of multiple AI concepts covered throughout the course outcomes.
