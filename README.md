# Fault Diagnosis in Industrial Systems Using Deterministic and Probabilistic Reasoning

## Project Overview

This project implements an Intelligent Fault Diagnosis System using core Artificial Intelligence concepts covered in the Computational Foundations for Artificial Intelligence (CFAI) course.

The system analyzes industrial sensor readings such as temperature, pressure, and vibration to identify potential machine faults. It combines graph search, constraint satisfaction, rule-based reasoning, probabilistic reasoning, and utility-based decision making to provide accurate fault diagnosis and maintenance recommendations.

---

## Objectives

* Represent industrial sensor data as AI state-space models.
* Perform fault exploration using graph search algorithms.
* Apply Constraint Satisfaction Problem (CSP) techniques for fault detection.
* Implement probabilistic reasoning under sensor uncertainty.
* Use utility-based decision making for maintenance recommendations.
* Integrate all modules into a complete AI-based fault diagnosis pipeline.

---

## AI Concepts Used

### CO1 – Problem Formulation & Representation

* State Space Representation
* PEAS Framework
* Rule-Based Knowledge Representation
* Sensor State Modeling

### CO2 – Graph Search Algorithms

* Breadth First Search (BFS)
* Fault Graph Exploration
* State Space Traversal

### CO3 – Constraint Satisfaction Problem (CSP)

* Constraint Checking
* Operational Limit Verification
* Constraint Violation Analysis

### CO4 – Decision Making Agent

* Utility-Based Agent
* Maintenance Action Selection
* Rational Decision Making

### CO5 – Reasoning Under Uncertainty

* Bayesian-Inspired Reasoning
* Fault Probability Estimation
* Sensor Uncertainty Handling

### CO6 – Integrated AI Pipeline

* Search + Constraints + Rules + Probability + Decision Making

---

## Project Structure

Fault-Diagnosis-AI/

├── app.py

├── README.md

├── requirements.txt

├── Project_Report.md

---

## How to Run

Run the application using Python:

```bash
python app.py
```

If the environment does not support user input, use predefined sensor values inside the code.

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
Motor Fault Suspected

Fault Probability = 1.00

Recommended Action = Emergency Shutdown
```

---

## Algorithm

1. Read sensor values.
2. Create a system state representation.
3. Explore possible faults using BFS.
4. Check operational constraints.
5. Apply rule-based diagnosis.
6. Estimate fault probability.
7. Select the appropriate maintenance action.
8. Display diagnosis results.
9. End.

---

## System Workflow

Sensor Readings

↓

State Representation

↓

BFS Fault Exploration

↓

Constraint Checking

↓

Rule-Based Diagnosis

↓

Probabilistic Reasoning

↓

Utility-Based Decision Making

↓

Maintenance Recommendation

↓

Reasoning Trace

---

## Applications

* Manufacturing Industries
* Smart Factories
* Industrial IoT Systems
* Predictive Maintenance
* Power Plants
* Oil and Gas Industries
* Process Control Systems

---

## Technologies Used

* Python 3.x
* Artificial Intelligence Algorithms
* Graph Search Techniques
* Constraint Satisfaction
* Probabilistic Reasoning
* Object-Oriented Programming

---

## Course Details

Course: Computational Foundations for Artificial Intelligence (CFAI)

Project Title: Fault Diagnosis in Industrial Systems Using Deterministic and Probabilistic Reasoning
