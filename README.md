# 🚀 Global Space Rocket Launches Analysis (1957–2026)
### End-to-End Data Engineering & Exploratory Data Analysis Pipeline

An end-to-end data analysis project scraping, validating, cleaning, and analyzing over **7,600+ historical rocket launches** worldwide using **The Space Devs (Launch Library 2) REST API**.

---

## 📌 Project Overview
* **Data Source:** Launch Library 2 API (`v2.3.0` by *The Space Devs*)
* **Scope:** 7,600+ orbital rocket launches spanning nearly 70 years (from Sputnik 1 in 1957 to 2026).
* **Pipeline:** API Extraction $\rightarrow$ Pydantic Schema Validation $\rightarrow$ Pandas Cleaning $\rightarrow$ Multi-Dimensional EDA $\rightarrow$ Vercel Web Deployment.

---

## 🏗️ Technical Pipeline & Methodology

1. **API Scraping (`fetch.py`):**
   * Paginates through historical launches (100 records per page).
   * Implements automated checkpointing (`launches_raw.json`) and HTTP 429 rate-limit handling with dynamic `Retry-After` backoff.
2. **Schema & Data Validation:**
   * Validated every launch record using **Pydantic** (`BaseModel`) to enforce strict type constraints, required fields, and nullable schema fallbacks.
3. **Data Cleaning & Feature Engineering (`clean.ipynb`):**
   * Handled missing values and removed duplicates.
   * Converted ISO 8601 timestamps into temporal features (`Year`, `Decade`, `Decade_Label`).
   * Engineered binary success metrics (`Is_Success`) and historical era classifications.
4. **Multi-Pillar Exploratory Data Analysis (EDA):**
   * **Launch Trends Over Time:** Evaluated annual frequency, highlighting the Cold War Apollo peak (1966–1967) and the modern commercial boom (surpassing 300+ launches/year in 2024–2025).
   * **Provider & Rocket Reliability:** Ranked top historical providers (Soviet Program, SpaceX, USAF, CASC) and workhorse rockets (Falcon 9 Block 5, Soyuz U) by volume and success rate.
   * **Global Spaceports:** Identified the world's busiest launch complexes (SLC-40, Baikonur Site 31/6, Gagarin's Start 1/5) and leading spacefaring nations.
   * **Mission Purpose & Orbits:** Analyzed payload objectives (Government/Top Secret, Communications, Earth Observation) and orbital destinations (LEO, GEO, SSO, MEO).

---

## 📁 Repository Structure
```text
├── fetch.py                            # API extraction script with checkpointing
├── launches_raw.json                   # Raw API dataset (7,600+ records)
├── clean.ipynb                         # Jupyter Notebook with Pydantic validation & Pandas EDA
├── space_launch_master_analysis.xlsx   # Consolidated 9-sheet analyzed Excel workbook
└── index.html                          # Compiled interactive HTML dashboard for Vercel deployment
```

---

## 📊 Key Findings
* **Most Active Year in History:** **2025** leads with **341 launches** (~2.5× higher than the peak Cold War year).
* **Workhorse Rocket:** **Falcon 9 Block 5** is the most flown single configuration (640+ flights with >99.8% success rate).
* **Target Orbits:** **Low Earth Orbit (LEO)** represents **>56%** of all human spaceflights, driven by commercial satellite constellations.
* **Global Safety Evolution:** Spaceflight reliability improved from **~88% in the 1960s** to **>96.5% in the 2020s**.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** `pandas`, `pydantic`, `requests`, `openpyxl`, `json`
* **Deployment:** Vercel (Static Web Report)
