from flask import Flask
import sqlite3

app = Flask(__name__)


@app.route("/names/")
def get_unique_names_count():
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(DISTINCT first_name) FROM customers")
        result = cursor.fetchone()[0]
        conn.close()

        # Build a string with the count of unique names
        response = f"Quantity of Unique Customer Names: {result}"

        return response
    except Exception as e:
        return str(e)


@app.route("/tracks/")
def get_tracks_count():
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM tracks")
        result = cursor.fetchone()[0]
        conn.close()

        # Build a string with the count of tracks
        response = f"Total tracks: {result}"

        return response
    except Exception as e:
        return str(e)


@app.route("/tracks-sec/")
def get_tracks_duration():
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tracks")
        tracks = cursor.fetchall()
        conn.close()

        # Build a string with each track's information
        response = ""
        for index, row in enumerate(tracks, start=1):
            response += (
                f"Track #{index}: Artist: {row[1]}, Duration (seconds): {row[2]}<br>"
            )

        return response
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)
