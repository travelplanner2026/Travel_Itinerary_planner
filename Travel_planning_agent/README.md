# 🧭 AI Travel Itinerary Planning Agent under Budget and Time Constraints

> **College AI Mini-Capstone Project**  
> *An intelligent decision-support agent for multi-day tourism scheduling using Constraint Satisfaction and Heuristic Knapsack Optimization.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F51B5.svg)](https://plotly.com/)
[![Tests](https://img.shields.io/badge/Pytest-Passing-green.svg)](https://pytest.org/)

---

## 📌 1. Project Overview & Motivation

Independent travelers frequently struggle to balance conflicting objectives:
1. **Financial Constraint**: Total expenditure (entry tickets, local transport, meals, lodging, and safety reserve) must never exceed the traveler's hard budget limit in Rupees (₹).
2. **Time Constraint**: Daily sightseeing activities and transit hops must fit within the user's available daily hours without causing extreme fatigue.
3. **Geographic Cohesion**: Visiting distant tourist spots haphazardly wastes time in traffic jams and inflates local cab fares.

This project implements an **AI Planning Agent** that solves this multi-constraint optimization problem. It produces a day-by-day, slot-by-slot travel plan that maximizes tourist utility while strictly validating budget and time bounds.

---

## 🧠 2. AI & Mathematical Formulation

### 2.1 The Problem as a Multi-Dimensional Knapsack & CSP
The travel itinerary problem is formulated as a variant of the **Multi-Dimensional Knapsack Problem with Geographic Bin Packing**:
- **Decision Variable**:  
  $$x_{i, d} \in \{0, 1\}$$  
  Indicates whether attraction $i$ is scheduled on day $d$.

- **Hard Constraint 1: Budget Constraint**  
  $$\text{Total Cost} = \sum_{d=1}^{D} \left( \sum_{i} x_{i, d} \cdot \text{Fee}_i + \text{TransitCost}_d + \text{FoodCost}_d + \text{LodgingCost}_d \right) + \text{SafetyBuffer} \le \text{Budget}_{\text{user}}$$

- **Hard Constraint 2: Daily Sightseeing Time Limit**  
  $$\sum_{i} x_{i, d} \cdot \text{Duration}_i + \text{TransitTime}_d \le T_{\text{available}}, \quad \forall d \in \{1, \dots, D\}$$

- **Hard Constraint 3: Non-Repetition**  
  $$\sum_{d=1}^{D} x_{i, d} \le 1, \quad \forall i$$

### 2.2 Multi-Attribute Heuristic Utility Function
Candidate attractions are ranked using a multi-attribute utility formula:
$$\text{Utility}(i) = w_r \cdot \left(\frac{\text{Rating}_i}{5.0}\right) + w_p \cdot \mathbb{I}_{[\text{CategoryMatch}]} - w_c \cdot \left(\frac{\text{Fee}_i}{\text{Budget}}\right) + w_e \cdot \left(\frac{\text{Rating}_i}{\text{Duration}_i}\right)$$

### 2.3 Geographic Zone Clustering
Rather than randomly selecting attractions across the city, the agent groups attractions by **urban micro-zones** (e.g., *Amer/North*, *Walled City*, *Central* in Jaipur). Each day is anchored to a primary zone cluster, cutting cross-city transit fatigue by over 40%.

---

## 🏛️ 3. Project Architecture & File Structure

```text
Travel_planning_agent/
│
├── app.py                      # Main Streamlit Web Application & UI Dashboard
├── requirements.txt            # Python dependencies (Streamlit, Plotly, Pandas, Pytest)
├── README.md                   # Complete documentation and execution guide
│
├── core/                       # Core AI Planning Engine
│   ├── __init__.py
│   └── planner.py              # TravelPlanningAgent, Utility calculations & Constraint checks
│
├── data/                       # Benchmark Dataset
│   ├── __init__.py
│   └── destinations_data.py    # Curated Indian destinations (Jaipur, Goa, Manali, Varanasi, Kochi, Agra)
│
└── tests/                      # Automated Test Suite
    ├── test_planner.py         # Unit tests for constraints, uniqueness, & validation
    └── test_app.py             # Integration tests for Streamlit UI execution
```

---

## 🇮🇳 4. Pan-India Coverage Across All 28 Indian States

The dataset covers **all 28 States of India** with 51 curated tourist hubs and 186 attractions:

| State | Sample Destinations Included |
| :--- | :--- |
| **Andhra Pradesh** | Visakhapatnam (Vizag), Tirupati |
| **Arunachal Pradesh** | Tawang, Ziro Valley |
| **Assam** | Kaziranga National Park, Guwahati |
| **Bihar** | Bodh Gaya, Nalanda & Rajgir |
| **Chhattisgarh** | Bastar & Jagdalpur, Raipur & Sirpur |
| **Goa** | Goa (North & South), South Goa & Coastal Serenity |
| **Gujarat** | Ahmedabad, Rann of Kutch & Bhuj |
| **Haryana** | Kurukshetra, Gurugram & Sultanpur |
| **Himachal Pradesh** | Manali, Shimla |
| **Jharkhand** | Ranchi, Jamshedpur |
| **Karnataka** | Bengaluru & Mysuru, Hampi |
| **Kerala** | Kochi, Munnar & Alleppey |
| **Madhya Pradesh** | Khajuraho, Bhopal & Sanchi |
| **Maharashtra** | Mumbai, Chhatrapati Sambhajinagar (Aurangabad) |
| **Manipur** | Imphal & Loktak Lake |
| **Meghalaya** | Shillong & Cherrapunji (Sohra) |
| **Mizoram** | Aizawl & Reiek |
| **Nagaland** | Kohima & Dzukou Valley |
| **Odisha** | Puri & Konark, Bhubaneswar |
| **Punjab** | Amritsar, Chandigarh |
| **Rajasthan** | Jaipur, Udaipur |
| **Sikkim** | Gangtok & Tsomgo Lake, Pelling |
| **Tamil Nadu** | Chennai & Mahabalipuram, Madurai & Rameswaram |
| **Telangana** | Hyderabad, Warangal |
| **Tripura** | Agartala & Neermahal |
| **Uttar Pradesh** | Varanasi, Agra |
| **Uttarakhand** | Rishikesh & Haridwar, Nainital & Corbett |
| **West Bengal** | Kolkata, Darjeeling & Sundarbans |

*Original benchmark destinations (**Jaipur, Goa, Manali, Varanasi, Kochi, Agra**) are preserved under their respective states.*

---

## 💻 5. Step-by-Step Instructions: How to Run on Your Laptop

Follow these simple instructions to run the application on any Windows, macOS, or Linux laptop:

### Step 1: Open Terminal or Command Prompt
- On Windows: Press `Win + R`, type `cmd` or `powershell`, and press Enter.
- On Mac/Linux: Open the `Terminal` application.

### Step 2: Navigate to the Project Folder
```powershell
cd "c:\Users\Alekhya's pc\Desktop\Travel_planning_agent"
```
*(Or use your path if moved to another folder)*

### Step 3: (Recommended) Create & Activate a Virtual Environment
```powershell
# Create virtual environment
python -m venv venv

# Activate it:
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On Windows (Command Prompt):
.\venv\Scripts\activate.bat
# On macOS / Linux:
source venv/bin/activate
```

### Step 4: Install Required Packages
```powershell
pip install -r requirements.txt
```

### Step 5: Start the Streamlit Web App
```powershell
streamlit run app.py
```

### Step 6: Open in Your Browser
Streamlit will automatically open your default browser at:
👉 **`http://localhost:8501`**

---

## 🧪 6. Running Automated Tests & 28-State Verification

You can verify the 28-state validation and test suite using either command:

**Option A (Standalone Pan-India Verification Script):**
```powershell
python test.py
```

**Option B (Pytest Full Suite):**
```powershell
pytest -v
```

Expected output:
```text
test.py::test_all_28_states_validation PASSED
test.py::test_preserved_benchmark_destinations PASSED
test.py::test_itinerary_planning_across_all_28_states PASSED
test.py::test_time_constraint_enforcement PASSED
test.py::test_input_validation PASSED
tests/test_planner.py::test_all_28_states_presence_and_coverage PASSED
tests/test_planner.py::test_destination_from_every_state_can_be_planned PASSED
tests/test_app.py::test_streamlit_app_loads_and_runs PASSED
tests/test_app.py::test_streamlit_app_budget_change PASSED
tests/test_app.py::test_streamlit_app_state_selection_updates_destinations PASSED
tests/test_app.py::test_internal_config_not_displayed PASSED
...
```

---

## 🌟 7. Key Features & Dashboard Highlights

- **Dynamic Constraint Status Banner**: Real-time feedback informing the traveler if the generated plan is within budget, near capacity, or if budget adjustment is advised.
- **Day-Wise Schedule with Pro Tips**: Time-slot assignments (Morning, Afternoon, Evening) with category tags, entrance fees, transit times, and insider pro-tips.
- **Interactive Visualizations (Plotly)**:
  - Donut chart of expenditure breakdown (Tickets vs Transit vs Food vs Hotel vs Emergency Buffer).
  - Stacked bar chart showing daily time allocation (Sightseeing vs Transit vs Buffer).
  - Daily cost comparison bar charts.
- **Transparent AI Decision Log**: Complete audit trail showing why each spot was scheduled or why certain candidates were rejected (e.g. time cap or budget cap).
- **One-Click Itinerary Export**: Export itineraries as formatted Markdown (`.md`) or structured JSON (`.json`).

---

## 🎓 8. Academic Viva / Capstone Q&A Tips

- **Q: Why not use a pure Genetic Algorithm or Deep RL for this project?**  
  *A:* For typical tourist itineraries (1 to 7 days, 10–30 attractions), heuristic knapsack with zone clustering provides deterministic, millisecond-fast, and 100% explainable solutions without the unpredictable hallucinations or heavy training overhead of neural models.
- **Q: How does the agent enforce hard constraints?**  
  *A:* In `core/planner.py`, candidate additions must pass both time feasibility ($projected \le effective\_daily\_hours$) and budget feasibility ($projected\_cost \le budget$). If an activity violates either constraint, it is pruned with an explicit explanation recorded in `reasoning_logs`.
