# Transmedia Test Automation Project

This repo contains both UI and API tests for the Transmedia board/list app. The goal of this assignment is to validate key functionality like board creation, list manipulation, and basic flow checks.



## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/transmedia-test-automation-project.git
cd transmedia-test-automation-project
```

### 2. Install Python 3.11.9
Make sure you have **Python 3.11.9** installed. Use `pyenv` if you need to manage versions:
```bash
pyenv install 3.11.9
pyenv local 3.11.9
```

### 3. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

> If you don’t have `requirements.txt`, install manually:
```bash
pip install selenium pytest requests
```



## Run the App

Make sure the local app is running. In the frontend project folder (e.g., `qa-automation-home-assignment`):

```bash
npm install
npm start
```

App should run on [http://localhost:3000](http://localhost:3000)



## ✅ Running the Tests

### API Test
```bash
cd api/tests
pytest test_api.py
```

This will:
- Create a board via API
- Add a list under it
- Delete the list
- Clean up the board

### UI Test
```bash
cd tests
pytest test_board_list.py
```

> Note: Chrome browser must be installed. Selenium uses it by default.



## 📁 Project Structure

```
.
├── api
│   ├── endpoints          # API logic lives here
│   └── tests              # API test cases
├── pages                  # Page objects for UI
├── tests                  # UI test cases
├── conftest.py            # Pytest fixtures (like Selenium driver)
```



## 🧪 What’s Covered

- Create & delete board (API)
- Add & delete list (API)
- Full UI flow: Board + List interactions



## 📝 Notes

- If Chrome isn’t launching, make sure chromedriver is compatible with your version.
- All requests assume the app is running on `localhost:3000`.
- Don’t hardcode IDs if you plan to scale this — dynamic data is used in tests intentionally.



