from dataclasses import dataclass
from collections import deque
from typing import List


# =====================================================
# CO1 - Agent Model & State Representation
# =====================================================

@dataclass
class SensorState:
    temperature: float
    pressure: float
    vibration: float


class FaultDiagnosisAgent:

    def perceive(self, state: SensorState):
        return state

    def act(self, decision: str):
        print(f"\nRecommended Action: {decision}")


# =====================================================
# CO2 - BFS Search
# =====================================================

fault_graph = {
    "Sensor Alert": ["Motor Fault", "Bearing Fault", "Leakage Fault"],
    "Motor Fault": ["Overheating"],
    "Bearing Fault": ["Mechanical Wear"],
    "Leakage Fault": ["Pressure Drop"],
    "Overheating": [],
    "Mechanical Wear": [],
    "Pressure Drop": []
}


def bfs(start: str):
    queue = deque([start])
    visited = set()

    discovered = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            discovered.append(node)

            for neighbor in fault_graph[node]:
                queue.append(neighbor)

    return discovered


# =====================================================
# CO3 - Constraint Satisfaction
# =====================================================

def check_constraints(state: SensorState):

    violations = []

    if state.temperature > 80:
        violations.append(
            f"Temperature exceeded limit (80): {state.temperature}"
        )

    if state.pressure < 50:
        violations.append(
            f"Pressure below limit (50): {state.pressure}"
        )

    if state.vibration > 7:
        violations.append(
            f"Vibration exceeded limit (7): {state.vibration}"
        )

    return violations


# =====================================================
# CO5 - Probabilistic Reasoning
# =====================================================

def fault_probability(state: SensorState):

    probability = 0.10

    if state.temperature > 80:
        probability += 0.40

    if state.pressure < 50:
        probability += 0.25

    if state.vibration > 7:
        probability += 0.25

    return min(probability, 1.0)


# =====================================================
# CO4 - Utility Based Decision
# =====================================================

utilities = {
    "Continue Operation": -100,
    "Inspect Machine": 50,
    "Emergency Shutdown": 100
}


def choose_action(probability):

    if probability >= 0.8:
        return "Emergency Shutdown"

    elif probability >= 0.4:
        return "Inspect Machine"

    return "Continue Operation"


# =====================================================
# CO6 - Hybrid Fault Diagnosis System
# =====================================================

def diagnose(state: SensorState):

    print("\n======================================")
    print(" INDUSTRIAL FAULT DIAGNOSIS SYSTEM ")
    print("======================================")

    print("\nSensor Readings")

    print(f"Temperature : {state.temperature}")
    print(f"Pressure    : {state.pressure}")
    print(f"Vibration   : {state.vibration}")

    print("\n----- STEP 1 : Search Analysis (BFS) -----")

    search_trace = bfs("Sensor Alert")

    for item in search_trace:
        print(item)

    print("\n----- STEP 2 : Constraint Checking -----")

    violations = check_constraints(state)

    if violations:

        for violation in violations:
            print(violation)

    else:
        print("No constraint violations detected.")

    print("\n----- STEP 3 : Rule-Based Diagnosis -----")

    if state.temperature > 80 and state.vibration > 7:
        rule_result = "Motor Fault Suspected"

    elif state.pressure < 50:
        rule_result = "Leakage Fault Suspected"

    else:
        rule_result = "System Normal"

    print(rule_result)

    print("\n----- STEP 4 : Probabilistic Diagnosis -----")

    probability = fault_probability(state)

    print(f"Fault Probability = {probability:.2f}")

    print("\n----- STEP 5 : Utility Decision -----")

    action = choose_action(probability)

    print(f"Selected Action = {action}")

    print("\n----- REASONING TRACE -----")

    print("1. Sensor values received")
    print("2. Search graph explored")
    print("3. Constraints evaluated")
    print("4. Rules applied")
    print("5. Probability estimated")
    print("6. Utility-based decision selected")

    print("\n======================================")

    return action


# =====================================================
# MAIN
# =====================================================

def main():

    print("Industrial Fault Diagnosis System")

    try:

        temp = float(input("Enter Temperature: "))
        pressure = float(input("Enter Pressure: "))
        vibration = float(input("Enter Vibration: "))

        state = SensorState(
            temperature=temp,
            pressure=pressure,
            vibration=vibration
        )

        agent = FaultDiagnosisAgent()

        perceived_state = agent.perceive(state)

        decision = diagnose(perceived_state)

        agent.act(decision)

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
