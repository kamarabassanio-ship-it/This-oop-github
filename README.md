# DPG Agricultural Tracking System

A robust object-oriented Python application designed to manage and monitor farm crops and livestock health records. This system facilitates agricultural record-keeping, tracking crop yields per hectare alongside individual livestock health histories and district distributions.

---

## Features

- **Crop Yield Management (`FarmCrop`)**:
  - Track individual farm plots by ID, crop type, and area size in hectares.
  - Accumulate multiple harvest yields (in kilograms).
  - Automatically calculate yield performance metrics (e.g., $kg/ha$).

- **Livestock Record Tracking (`LivestockRecord`)**:
  - Maintain unique tag IDs, animal species/breeds, and regional/district locations.
  - Log immutable health history timelines using Python tuples (status, weight, vaccination status, and timestamp).
  - Utilize **Class Methods** for tracking total livestock population and factory-style creation of standardized tags.
  - Utilize **Static Methods** for strict format validation of farm tags (`AGR-DPG-XXXX`).

- **Centralized Database Container (`AgriculturalTrackerSystem`)**:
  - Store and manage livestock records efficiently using Python dictionaries indexed by tag IDs.
  - Validate and filter records before database entry.
  - Display comprehensive bulk summaries of all registered farm animals.

---

## Project Structure

```text
.
├── main.py                  # Core application script containing all classes and execution flow
└── README.md                # Project documentation
```

---

## Requirements

- Python 3.7 or higher
- Built-in `datetime` module (no external third-party dependencies required)

---

## Getting Started

1. Clone or download the script file (e.g., `main.py`).
2. Run the application from your terminal:

```bash
python main.py
```

---

## Code Architecture & Demonstration

The built-in execution block (`if __name__ == "__main__":`) demonstrates the following core workflows:
1. **Crop Tracking:** Instantiating `FarmCrop` objects for plots (e.g., NERICA Rice and Cassava), recording multiple harvests, and outputting productivity summaries.
2. **Livestock Registration:** Registering individual livestock through standard instantiation and factory methods (`create_anonymous_livestock`).
3. **Health Assessments:** Appending timestamped health status logs using tuple data structures.
4. **Validation Checks:** Verifying farm tags using static methods and querying total animal counts via class methods.

---

## License

This project is open-source and available for agricultural management and educational use.