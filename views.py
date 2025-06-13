from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint(__name__, "views")

tasks = []

@views.route("/", methods=["GET", "POST"])
def home(): 
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task) 
        return redirect(url_for("views.home")) # evita reenvio no F5
    
    return render_template("index.html", tasks=tasks)

@views.route("/delete/<int:index>", methods=["POST"])
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        return redirect(url_for("views.home"))