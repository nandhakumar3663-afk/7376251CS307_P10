# 🍽️ Recipe Book

A menu-driven **Core Python** application that helps users explore recipes, view ingredients and step-by-step cooking instructions, and manage a simple cooking queue.

## 👨‍🎓 Student Details

| Field | Details |
|---|---|
| **Name** | Nandha Kumar PS |
| **Register Number** | 7376251CS307 |
| **Project Number** | P10 |
| **Project Title** | Recipe Book |

## ✨ Features

- **View Recipe Menu** — display the available recipes.
- **Select a Recipe** — view preparation time, cooking time, servings, ingredients, and numbered cooking instructions.
- **Add to Cooking Queue** — choose whether to add a selected recipe to the queue.
- **View Cooking Queue** — see queued recipes in order.
- **Prepare Next Recipe** — display the next recipe's details and remove it from the queue.
- **Input Validation** — handle invalid menu choices and non-numeric input.

## 🥗 Available Recipes

1. Lemon Juice
2. Tea
3. Coffee
4. Tomato Rice
5. Chocolate Milkshake

## 🛠️ Technologies Used

- **Language:** Python 3
- **Concepts:** Classes and objects, dictionaries, lists, loops, conditional statements, exception handling, and FIFO queue operations.
- **Storage:** A Python list manages the cooking queue. The project also includes `data.txt` and `sample_run.txt` files.

## 📁 Project Structure

```text
7376251CS307_P10/
├── main.py         # Main Recipe Book application
├── data.txt        # Project data file
├── sample_run.txt  # Sample program run/output
└── README.md       # Project documentation
```

## ▶️ How to Run

1. Install **Python 3** if it is not already installed.
2. Clone the repository:

   ```bash
   git clone https://github.com/nandhakumar3663-afk/7376251CS307_P10.git
   ```

3. Open the project folder:

   ```bash
   cd 7376251CS307_P10
   ```

4. Run the program:

   ```bash
   python main.py
   ```

   On some Windows installations, use:

   ```bash
   py main.py
   ```

## 🧭 Main Menu

When the program starts, it displays the following options:

| Option | Action |
|---|---|
| 1 | View Recipe Menu |
| 2 | Select a Recipe |
| 3 | View Cooking Queue |
| 4 | Prepare Next Recipe |
| 5 | Exit |

## 🧠 Queue Logic

Recipes are added to the end of the cooking queue. The **Prepare Next Recipe** option uses `pop(0)` to remove the first recipe, following **First In, First Out (FIFO)** order.

## 🎯 Project Objective

The objective of this project is to practise fundamental Python programming by building a practical, interactive recipe manager with recipe details and queue handling.

---

**Project:** P10 — Recipe Book  
**Student:** Nandha Kumar PS  
