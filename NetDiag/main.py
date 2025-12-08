from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    host = request.args.get("host")
    output = None
    error = None

    if host:
        try:
            cmd = f"ping -c 3 {host}"
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=5
            )
            output = result.stdout
            if result.stderr:
                error = result.stderr
        except subprocess.TimeoutExpired:
            error = "Время ожидания запроса истекло."

    return render_template("index.html", host=host or "", output=output, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
