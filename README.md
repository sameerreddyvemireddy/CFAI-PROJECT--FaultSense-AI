# CFAI-PROJECT--FaultSense-AI
# FaultSense AI — Industrial Fault Diagnosis System
## Project 07: Fault Diagnosis in Industrial Systems

### 🚀 Quick Start

```bash
# 1. Install dependencies
python3 -m pip install flask flask-cors

# 2. Run the application
python3 app.py

# 3. Open in browser
open http://localhost:5002
```

The system will start automatically and you can access it at **http://localhost:5000**

---

## 📚 System Architecture (CO1-CO6)

### CO1: Agent Model & Knowledge Representation
- **PEAS Analysis**: Performance measure, Environment, Actuators, Sensors
- **Environment Properties**: Partially observable, stochastic, sequential, dynamic
- **State Representation**: Dataclass-based fault states with proper typing
- **Knowledge Graph**: Industrial fault state space with 12 states
- **Sensors**: Temperature, Pressure, Vibration, Current, Voltage (with Gaussian noise)

### CO2: Search Algorithm
- **Algorithm**: A* Search (Optimal + Complete)
- **Heuristic**: Euclidean distance in normalized sensor space (Admissible & Consistent)
- **Properties**: 
  - Time Complexity: O(b^d)
  - Space Complexity: O(b^d)
  - Optimal path guaranteed with admissible heuristic
- **Features**: 
  - Open/Closed set management
  - f(n) = g(n) + h(n) evaluation
  - Step-by-step execution trace

### CO3: Constraint Satisfaction
- Fault state constraints encoded in graph structure
- State transitions follow physical causality rules
- Goal states: Terminal fault diagnoses or NORMAL operation

### CO5: Probabilistic Reasoning
- Sensor noise simulation (Gaussian distribution)
- Sensor fusion through multi-dimensional state space
- Uncertainty handling in diagnosis

### CO6: Hybrid Architecture
- Combines search (A*) + knowledge representation (graph)
- Explainable step-by-step traces
- Clear severity classification (CRITICAL, MAJOR, NORMAL)

---

## 🎮 How to Use

### 1. **Sensor Input**
   - Adjust the 5 sensor sliders (Temperature, Pressure, Vibration, Current, Voltage)
   - Add sensor noise (0-20%) to simulate real-world measurement errors
   - Use **Quick Presets** for common fault scenarios

### 2. **Run Diagnosis**
   - Click "⚡ Run Diagnosis" button
   - Watch the A* algorithm explore the fault state space

### 3. **Interpret Results**
   - **Severity Level**: Shows CRITICAL/MAJOR/NORMAL status
   - **Fault State**: The identified fault (e.g., OVERHEATING, PUMP_FAILURE)
   - **Description**: What's wrong and recommended action
   - **Path Taken**: The sequence of states explored
   - **Statistics**: Nodes expanded, path cost

### 4. **Step-by-Step Trace**
   - See exactly how A* algorithm works
   - Track frontier size and closed set growth
   - Understand heuristic evaluation at each step

---

## 📋 Fault Scenarios

| Scenario | Fault | Severity |
|----------|-------|----------|
| **Normal** | System Operating Normally | ✓ NORMAL |
| **Overheating** | Extreme temperature (>90°C) | ⚠️ CRITICAL |
| **Pump Failure** | No pressure, pump not responding | ⚠️ CRITICAL |
| **Bearing Wear** | High vibration, elevated temperature | ⚠️ MAJOR |
| **Coolant Leak** | High temp + low pressure | ⚠️ CRITICAL |

---

## 🔧 Project Structure

```
fault_diagnosis/
├── app.py                    # Flask backend (A* search, CO1-CO6)
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── templates/
    ├── index.html           # Main UI (clean, educational)
    └── index_old.html       # Previous version (backup)
```

---

## 🧠 Algorithm Details

### A* Search Implementation
1. **Initialization**: Start node with g(n)=0, h(n)=heuristic(START)
2. **Frontier**: Priority queue ordered by f(n) = g(n) + h(n)
3. **Expansion**: Pop lowest f(n) node, add successors to frontier
4. **Goal Test**: When dequeued node is in GOAL_STATES
5. **Termination**: Path reconstruction or failure

### Admissible Heuristic
- Uses Euclidean distance in normalized sensor space
- Never overestimates true cost
- Guarantees optimal solution

---

## 📊 Features

✅ **A* Search Algorithm** - Optimal, complete search  
✅ **Sensor Noise Simulation** - Realistic uncertainty  
✅ **Step-by-Step Visualization** - See algorithm execution  
✅ **Quick Presets** - Test predefined scenarios  
✅ **Clear Severity Levels** - CRITICAL/MAJOR/NORMAL  
✅ **Educational Design** - Understand AI at each step  
✅ **No Algorithm Selector** - A* is the best choice  

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Algorithm**: A* Graph Search
- **Data Structure**: Priority Queue (heapq), Dataclasses

---

## 📖 Course Learning Outcomes

- Understand PEAS models and environment types
- Implement informed search algorithms (A*)
- Design admissible heuristics
- Work with graphs and state spaces
- Handle sensor uncertainty
- Create explainable AI systems

---

## 📝 Notes

- The system uses **A* algorithm exclusively** for optimal fault diagnosis
- Sensor readings support real-time adjustment via sliders
- Noise level simulates real-world measurement uncertainties
- All traces show the exact reasoning process
- Suitable for understanding AI algorithms in practice
