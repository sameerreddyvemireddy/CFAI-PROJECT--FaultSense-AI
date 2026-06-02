from flask import Flask, request, render_template_string
from collections import deque
from dataclasses import dataclass

app = Flask(__name__)

# ==========================================================
# CO1 - Agent Model & State Representation
# ==========================================================

@dataclass
class SensorState:
    temperature: float
    pressure: float
    vibration: float


# ==========================================================
# CO2 - BFS Search
# ==========================================================

fault_graph = {
    "Sensor Alert": ["Motor Fault", "Bearing Fault", "Leakage Fault"],
    "Motor Fault": ["Overheating"],
    "Bearing Fault": ["Mechanical Wear"],
    "Leakage Fault": ["Pressure Drop"],
    "Overheating": [],
    "Mechanical Wear": [],
    "Pressure Drop": []
}


def bfs(start):
    queue = deque([start])
    visited = set()
    traversal = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            traversal.append(node)

            for neighbor in fault_graph[node]:
                queue.append(neighbor)

    return traversal


# ==========================================================
# CO3 - Constraint Satisfaction
# ==========================================================

def check_constraints(state):
    violations = []

    if state.temperature > 80:
        violations.append("Temperature exceeds safe limit (80°C)")

    if state.pressure < 50:
        violations.append("Pressure below safe limit (50 kPa)")

    if state.vibration > 7:
        violations.append("Vibration exceeds safe limit (7 mm/s)")

    return violations


# ==========================================================
# CO5 - Probabilistic Reasoning
# ==========================================================

def calculate_fault_probability(state):

    probability = 0.10

    if state.temperature > 80:
        probability += 0.40

    if state.pressure < 50:
        probability += 0.25

    if state.vibration > 7:
        probability += 0.25

    return min(probability, 1.0)


# ==========================================================
# CO4 - Utility Decision Making
# ==========================================================

def choose_action(probability):

    if probability >= 0.80:
        return "Emergency Shutdown"

    elif probability >= 0.40:
        return "Inspect Machine"

    return "Continue Operation"


# ==========================================================
# CO6 - Hybrid Diagnosis System
# ==========================================================

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Industrial Fault Diagnosis System</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Segoe UI',sans-serif;
}

body{
background:linear-gradient(135deg,#0f172a,#1e293b);
min-height:100vh;
padding:40px;
color:white;
}

.container{
max-width:900px;
margin:auto;
}

.header{
text-align:center;
margin-bottom:30px;
}

.header h1{
font-size:40px;
margin-bottom:10px;
}

.header p{
color:#cbd5e1;
}

.card{
background:rgba(255,255,255,0.08);
backdrop-filter:blur(10px);
padding:25px;
border-radius:20px;
box-shadow:0 10px 25px rgba(0,0,0,0.3);
margin-bottom:20px;
}

.input-group{
margin-bottom:20px;
}

label{
display:block;
margin-bottom:8px;
}

input{
width:100%;
padding:12px;
border:none;
border-radius:10px;
font-size:16px;
}

button{
width:100%;
padding:14px;
border:none;
border-radius:10px;
background:#2563eb;
color:white;
font-size:16px;
cursor:pointer;
}

button:hover{
background:#1d4ed8;
}

.result{
margin-top:20px;
}

.info{
background:#1e293b;
padding:12px;
border-radius:10px;
margin:10px 0;
}

.progress{
width:100%;
height:30px;
background:#334155;
border-radius:20px;
overflow:hidden;
margin-top:10px;
margin-bottom:20px;
}

.progress-fill{
height:100%;
background:linear-gradient(90deg,#22c55e,#eab308,#ef4444);
display:flex;
align-items:center;
justify-content:center;
font-weight:bold;
}

.node{
display:inline-block;
padding:8px 15px;
background:#3b82f6;
border-radius:20px;
margin:5px;
}

ul{
margin-left:20px;
margin-top:10px;
}

.status{
font-size:18px;
font-weight:bold;
}

</style>

</head>

<body>

<div class="container">

<div class="header">
<h1>Industrial Fault Diagnosis System</h1>
<p>AI-Based Fault Detection using Search, CSP, Probability and Decision Making</p>
</div>

<div class="card">

<form method="POST">

<div class="input-group">
<label>🌡 Temperature (°C)</label>
<input type="number" step="any" name="temperature" required>
</div>

<div class="input-group">
<label>⚙ Pressure (kPa)</label>
<input type="number" step="any" name="pressure" required>
</div>

<div class="input-group">
<label>📈 Vibration (mm/s)</label>
<input type="number" step="any" name="vibration" required>
</div>

<button type="submit">Run Diagnosis</button>

</form>

</div>

{% if result %}

<div class="card result">

<h2>Diagnosis Report</h2>

<div class="info">
<strong>Diagnosis:</strong> {{ result.diagnosis }}
</div>

<div class="info">
<strong>Fault Probability:</strong> {{ result.probability }}
</div>

<div class="progress">
<div class="progress-fill"
style="width: {{ result.probability * 100 }}%">
{{ (result.probability * 100)|round(0) }}%
</div>
</div>

<div class="info">
<strong>System Status:</strong>
<span class="status">{{ result.status }}</span>
</div>

<div class="info">
<strong>Recommended Action:</strong> {{ result.action }}
</div>

<h3>Constraint Violations</h3>

{% if result.violations %}
<ul>
{% for v in result.violations %}
<li>{{ v }}</li>
{% endfor %}
</ul>
{% else %}
<p>No violations detected.</p>
{% endif %}

<br>

<h3>BFS Fault Exploration</h3>

{% for node in result.bfs %}
<span class="node">{{ node }}</span>
{% endfor %}

</div>

{% endif %}

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        temperature = float(request.form["temperature"])
        pressure = float(request.form["pressure"])
        vibration = float(request.form["vibration"])

        state = SensorState(
            temperature,
            pressure,
            vibration
        )

        violations = check_constraints(state)

        bfs_result = bfs("Sensor Alert")

        if temperature > 80 and vibration > 7:
            diagnosis = "Motor Fault Suspected"

        elif pressure < 50:
            diagnosis = "Leakage Fault Suspected"

        else:
            diagnosis = "System Operating Normally"

        probability = calculate_fault_probability(state)

        action = choose_action(probability)

        if probability >= 0.80:
            status = "CRITICAL"
        elif probability >= 0.40:
            status = "WARNING"
        else:
            status = "HEALTHY"

        result = {
            "diagnosis": diagnosis,
            "probability": round(probability, 2),
            "action": action,
            "violations": violations,
            "bfs": bfs_result,
            "status": status
        }

    return render_template_string(
        HTML,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
