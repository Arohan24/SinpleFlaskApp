# 🍇 Flask JSON API App

A simple Flask application that serves a JSON list via an API route (`/api`). The data is stored in a backend file (`data.txt`) and returned as a JSON response when the route is accessed.

## 📋 Project Description

This app:

* Creates a local `data.txt` file (if it doesn't exist) and fills it with default fruit data.
* Reads the data from the file every time `/api` is accessed.
* Returns the data in JSON format using Flask's `jsonify`.

It is useful for learning how to:

* Work with Flask routes
* Read/write JSON data from files
* Serve JSON responses via REST API

## 🛠️ Tech Stack

* Python 3
* Flask
* JSON
* File I/O

## 📂 File Structure

```
project/
│
├── data.txt            # Created automatically if not found
├── app.py              # Main Flask app
├── requirements.txt
└── README.md
```

## 🔧 Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Arohan24/SinpleFlaskApp.git
   cd SinpleFlaskApp
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**

   ```bash
   python app.py
   ```

4. **Access the API**
   Visit: [http://localhost:5000/api](http://localhost:5000/api)

   You’ll receive a JSON response like:

   ```json
   [
     {"id": 1, "name": "apple", "color": "red"},
     {"id": 2, "name": "banana", "color": "yellow"},
     ...
   ]
   ```

## 📦 requirements.txt

```
Flask==2.3.2
```

## 📌 Notes

* The `data.txt` file is created only if it doesn't already exist.
* You can manually edit `data.txt` to change the API output.

## 📃 License

This project is free to use and modify for learning or development purposes.
